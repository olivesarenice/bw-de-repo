-- =========================================================================
-- Edge Case 1: Look-Ahead Bias & Bitemporal Restatements
-- Scenario: On 2023-02-01, the data vendor corrects a bad forward price 
-- originally published on 2023-01-05 for FB. 
-- We must prove our T+1 simulation (ran on 2023-01-06) didn't see the future.
-- =========================================================================

-- Look ahead bias, INCORRECT - Uses latest data, bleeding future bias
SELECT 
    date, 
    forward_price, 
    system_time as ingestion_timestamp
FROM Forward_Price
WHERE s_id = 10001002 
  AND date = '2023-01-05'
ORDER BY system_time DESC 
LIMIT 1;
-- Output will show system_time = '2023-02-01', which the algo couldn't know on Jan 5.

-- The "Strict Point-in-Time" Query (CORRECT - Bitemporal Guard rails applied)
SELECT * FROM (
    SELECT 
        date, 
        forward_price, 
        system_time as ingestion_timestamp,
        ROW_NUMBER() OVER(
            PARTITION BY s_id, date 
            ORDER BY system_time DESC
        ) as rn
    FROM Forward_Price
    WHERE s_id = 10001002 
      AND date = '2023-01-05'
      AND system_time <= '2023-01-06 00:00:00' -- BITEMPORAL GATE
) WHERE rn = 1;
-- Output safely returns the original value ingested on 2023-01-05.


-- =========================================================================
-- Edge Case 2: Regulatory Halts & Delisting Physics
-- Scenario: SVB (s_id: 10001005) halted on 2023-02-23 and liquidated 2023-02-28.
-- Goal: Identify the halted state for risk systems to freeze IV calculations.
-- =========================================================================

SELECT 
    date,
    close_price,
    equity_volume,
    option_volume,
    special_settlement
FROM (
    SELECT 
        sp.date,
        sp.close_price,
        sp.volume as equity_volume,
        op.volume as option_volume,
        op.special_settlement,
        -- BITEMPORAL GATE: Get the latest known price ticks
        ROW_NUMBER() OVER(
            PARTITION BY sp.s_id, sp.date 
            ORDER BY sp.system_time DESC
        ) as rn_sp,
        ROW_NUMBER() OVER(
            PARTITION BY op.option_id, op.date 
            ORDER BY op.system_time DESC
        ) as rn_op
    FROM Security_Price sp
    JOIN Option_Contract oc 
      ON sp.s_id = oc.s_id
    JOIN Option_Price op 
      ON oc.option_id = op.option_id 
      AND sp.date = op.date
    WHERE sp.s_id = 10001005 
      AND sp.date BETWEEN '2023-02-20' AND '2023-02-27'
      -- Filter to an arbitrary option just to observe the state
      AND op.option_id = 80006 
)
WHERE rn_sp = 1 AND rn_op = 1
ORDER BY date ASC;
-- Output will show negative close_prices (signaling midpoint logic) 
-- and volume = 0 with special_settlement = 1 during the halted days.


-- =========================================================================
-- Edge Case 3: Derivative Mutations (Corporate Action / Split Cascade)
-- Scenario: META executes a 2-for-1 split, followed immediately by a 3-for-1 split.
-- Options standard size (100) mutates, strikes shift, and new Option IDs are spawned.
-- =========================================================================

SELECT 
    date,
    symbol,
    strike,
    contractsize,
    volume,
    adjustment_factor
FROM (
    SELECT 
        op.date,
        oc.symbol,
        oc.strike,
        oc.contractsize,
        op.volume,
        op.adjustment_factor,
        -- BITEMPORAL GATE: Get the latest option price ticks
        ROW_NUMBER() OVER(
            PARTITION BY op.option_id, op.date 
            ORDER BY op.system_time DESC
        ) as rn_op
    FROM Option_Price op
    JOIN Option_Contract oc
      ON op.option_id = oc.option_id
    WHERE oc.s_id = 10001002
      -- Looking at the evolution of the ~150 Strike options family around late Feb 2023
      AND op.date BETWEEN '2023-02-17' AND '2023-02-28'
)
WHERE rn_op = 1
ORDER BY date ASC, contractsize ASC;
-- Output will show the standard option stopping, the 200-size 1st-generation appearing, 
-- and finally the 600-size 2nd-generation taking over.
