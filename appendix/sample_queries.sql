-- The Quantitative SQL Crucible: Bitemporal Time-Capsule Query
-- Scenario: Extracting the EOD Midpoint Mark, Physical Strike, and Contract Size 
-- for all active META options on 2023-02-27.
-- Constraint: The simulation runs at 18:00:00. Must not suffer look-ahead bias from T+2 vendor restatements.

SELECT * FROM (
  SELECT 
    op.date,
    op.option_id,
    s.ticker,
    (op.best_offer + op.best_bid)/2 AS eod_midpoint,
    oc.strike,
    oc.contractsize,
    -- BITEMPORAL GATE: Isolate the absolute latest known truth AS OF the execution time.
    ROW_NUMBER() OVER(
      PARTITION BY op.date, op.option_id 
      ORDER BY op.system_time DESC
    ) AS latest_rn 
  FROM Option_Price op
  JOIN Option_Contract oc
    ON op.option_id = oc.option_id
  JOIN Security s
    ON s.s_id = oc.s_id 
  WHERE s.ticker = 'META'
    AND op.date = '2023-02-27'
    
    -- SYSTEM TIME FILTER: The Time Machine.
    -- Mathematically blinds the query from ever seeing corrections published after 6 PM.
    AND op.system_time <= '2023-02-27 18:00:00'
    AND oc.system_time <= '2023-02-27 18:00:00'
)
WHERE latest_rn = 1;
