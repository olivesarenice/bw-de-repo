# Data Model

**Overview of improvements:**
- All tables have explicit `System_Time` (row-append time) to allow queries without Look-Ahead Bias. This applies to all data, regardless of whether it is mutable in reality.
- All system timestamps are assumed to be UTC for global consistency.
- All datestamps (business event time) are assumed to be UTC-5 (Eastern Time) for consistency with U.S. markets.
- For SCD2 DIM tables, we do not add a `valid_to_date` column to maintain append-only consistency. Validity is handled by checking both `date` (i.e. valid time) and `System_Time` (i.e. transaction time) meet the point-in-time criteria.
- Minor assumptions and changes covered per table.

---

## 1. Security
**Purpose:** Reference table for each underlying security.
**Type:** DIM
**Logical Grain:** `Security_ID`
**Physical PK:** `Security_ID + System_Time`

| Column          | Type        | Description                             | Example               | Notes                                                                                                                                                                                                                                                |
| :-------------- | :---------- | :-------------------------------------- | :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Security ID** | `int`       | Unique identifier.                      | `10001001`            | Primary Key. Set to `int` for smaller size and faster joins.                                                                                                                                                                                         |
| CUSIP           | `varchar`   | First 8 digits of CUSIP.                | `03783310`            | 9th digit is dropped as it is a checksum.<br><br>The 9th digit and beyond are not guranteed to be consistent across data vendors.<br><br>https://www.cusip.com/identifiers.html<br>                                                                  |
| Ticker          | `varchar`   | Inception (IPO) ticker base.            | `AAPL`                | `Security` table is strictly append-only. This `ticker` is locked at inception. <br><br>Analysts must `JOIN Security_Name` using point-in-time filter.<br><br>For general querying, we publish a View (`VW_Security_Current`) to abstract the joins. |
| SIC             | `varchar`   | SIC code.                               | `3571`                | Stored as string to preserve leading zeros.<br><br>https://www.sec.gov/search-filings/standard-industrial-classification-sic-code-list                                                                                                               |
| Index Flag      | `boolean`   | Indicates whether security is an index. | `0` (False)           | Assumes that further differentiation between different types of index are not needed (ETF vs. SPX)                                                                                                                                                   |
| Exchange Flags  | `varchar`   | Encoded exchange or listing flags.      | `Q`                   | Typically single-letter codes.<br><br>https://toslc.thinkorswim.com/center/howToTos/thinkManual/Miscellaneous/Exchange-Codes                                                                                                                         |
| Class           | `varchar`   | Security class designator.              | `A`                   |                                                                                                                                                                                                                                                      |
| Issue Type      | `varchar`   | Type of security (CS, ETF, ADR).        | `CS`                  |                                                                                                                                                                                                                                                      |
| Industry Group  | `varchar`   | 3-digit Morningstar classification.     | `311`                 |                                                                                                                                                                                                                                                      |
| **System_Time** | `timestamp` | UTC time for record append              | `2016-01-01 00:00:00` | Needed even on core Security table in case data comes late for a particular newly listed security.                                                                                                                                                   |

---

## 2. Security_Name
**Purpose:** Historical record of changes to the security's identifying details.
**Type:** DIM (SCD2)
**Logical Grain:** `Security_ID + Date`
**Physical PK:** `Security_ID + Date + System_Time`

| Column             | Type        | Description                       | Example               | Notes                                                   |
| :----------------- | :---------- | :-------------------------------- | :-------------------- | :------------------------------------------------------ |
| **Security ID**    | `int`       | Underlying security identifier.   | `10001001`            |                                                         |
| **Date**           | `date`      | Effective date of the change.     | `2014-06-09`          | Tracks corporate identity change (e.g. `FB` -> `META`). |
| CUSIP              | `varchar`   | First 8 digits of the CUSIP.      | `03783310`            |                                                         |
| Ticker             | `varchar`   | Ticker base as of that date.      | `AAPL`                |                                                         |
| Class              | `varchar`   | Class designator as of that date. | `A`                   |                                                         |
| Issuer Description | `varchar`   | Description of issuing company.   | `APPLE INC`           |                                                         |
| Issue Description  | `varchar`   | Description of the issue.         | `Issued for ...`      |                                                         |
| SIC                | `varchar`   | SIC code as of that date.         | `3571`                |                                                         |
| **System_Time**    | `timestamp` | UTC time for record append        | `2016-01-01 00:00:00` |                                                         |

---

## 3. Exchange
**Purpose:** Historical record of listing, delisting, and exchange changes.
**Type:** FACT
**Logical Grain:** `Security_ID + Date + Sequence`
**Physical PK:** `Security_ID + Date + Sequence + System_Time`

| Column               | Type        | Description                               | Example               | Notes                                                                         |
| :------------------- | :---------- | :---------------------------------------- | :-------------------- | :---------------------------------------------------------------------------- |
| **Security ID**      | `int`       | Underlying security identifier.           | `10001001`            |                                                                               |
| **Date**             | `date`      | Effective date of the exchange change.    | `1980-12-12`          |                                                                               |
| **Sequence Number**  | `int`       | Distinguishes multiple intraday events.   | `1`                   | Assumes multiple, sequenced rows are created for multi-exchange delists/lists |
| Status               | `varchar`   | Event code (listed, delisted, suspended). | `A`                   |                                                                               |
| Exchange             | `varchar`   | Exchange added or deleted.                | `Q`                   |                                                                               |
| Add/Delete Indicator | `varchar`   | Shows whether exchange was added/removed. | `A`                   | Assumes only 2 values `A` or `D`                                              |
| Exchange Flags       | `varchar`   | Primary exchange after the change.        | `Q`                   |                                                                               |
| **System_Time**      | `timestamp` | UTC time for record append                | `1980-12-12 16:30:00` |                                                                               |

---

## 4. Distribution
**Purpose:** Corporate-action and distribution history for the security.
**Type:** FACT
**Logical Grain:** `Security ID + Record_Date + Sequence`
**Physical PK:** `Security ID + Record_Date + Sequence + System_Time`

| Column              | Type        | Description                           | Example            | Notes                                                                      |
| :------------------ | :---------- | :------------------------------------ | :----------------- | :------------------------------------------------------------------------- |
| **Security ID**     | `int`       | Underlying security identifier.       | `10001001`         |                                                                            |
| **Record Date**     | `date`      | Record date for the distribution.     | `2023-08-14`       |                                                                            |
| **Sequence Number** | `int`       | Distinguishes multiple distributions. | `1`                |                                                                            |
| Ex Date             | `date`      | Date security trades ex-distrib.      | `2023-08-11`       | Date which the action is applied, affecting adjustments in actual price.   |
| Amount              | `numeric`   | Cash amount or yield.                 | `0.24`             | Precision numeric to prevent fractional scaling errors.                    |
| Adjustment Factor   | `numeric`   | Adjustment used to compare prices.    | `1.0`              | Assumption 8: Reconstructs synthetically broken histories.                 |
| Declare Date        | `date`      | Declaration date.                     | `2023-08-03`       | Date that information becomes public affecting **forward price** modeling. |
| Payment Date        | `date`      | Payment date.                         | `2023-08-17`       |                                                                            |
| Link Security ID    | `int`       | ID of acquiring/spun-off security.    | `NULL`             | Populated if Distribution Type = Merger/Spin-off.                          |
| Distribution Type   | `varchar`   | Type of distribution.                 | `1` (Cash Div)     | This affects if `Amount` is cash or yield.                                 |
| Frequency           | `varchar`   | Dividend-payment frequency.           | `Q` (Quarterly)    |                                                                            |
| Currency            | `varchar`   | ISO currency code.                    | `USD`              |                                                                            |
| Approximate Flag    | `boolean`   | Exact/approximate flag.               | `0` (False)        |                                                                            |
| Cancel Flag         | `boolean`   | Cancelled or omitted indicator.       | `0` (False)        | A new row is created if a cancellation for this action is issued.          |
| Liquidation Flag    | `boolean`   | Shows if distribution is liquidating. | `0` (False)        | Cascades to Delisting event in Exchange table.                             |
| **System_Time**     | `timestamp` | UTC time for record append            | `2023-08-03 16:30` |                                                                            |

---

## 5. Security_Price
**Purpose:** Daily price history for the underlying security.
**Type:** FACT
**Logical Grain:** `Security ID + Date`
**Physical PK:** `Security ID + Date + System_Time`

| Column             | Type        | Description                                        | Example            | Notes                                                                                                                |
| :----------------- | :---------- | :------------------------------------------------- | :----------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Security ID**    | `int`       | Underlying security identifier.                    | `10001001`         |                                                                                                                      |
| **Date**           | `date`      | Date of the price record.                          | `2023-08-11`       |                                                                                                                      |
| Bid / Low          | `numeric`   | If positive, low price; if negative, closing bid.  | `177.35`           | Absolute magnitude math `ABS(...)` required due to overloading negative flag for zero-volume days.                   |
| Ask / High         | `numeric`   | If positive, high price; if negative, closing ask. | `178.62`           | same as above                                                                                                        |
| Close Price        | `numeric`   | Closing price.                                     | `177.79`           | If zero-volume day, relies on midpoint of negative EOD Bid/Ask quotes. Need to be `ABS()` after                      |
| Volume             | `bigint`    | Sum of volume across exchanges.                    | `51988100`         | `bigint` (exceeds 32-bit limits) to handle days with massive flow > 2bn                                              |
| Total Return       | `numeric`   | Holding-period return.                             | `0.0003`           | From the last good (valid) pricing date to this date, adjusted.                                                      |
| Adjustment Factor  | `numeric`   | Cumulative split-style factor.                     | `224.0`            | P_t2 = P_t1 * adj_t1 / adj_t2                                                                                        |
| Open Price         | `numeric`   | Opening price.                                     | `177.32`           | 0 if no opening price                                                                                                |
| Shares Outstanding | `bigint`    | Public shares outstanding.                         | `15634200`         | `bigint` to handle large values                                                                                      |
| Adjustment Factor2 | `numeric`   | Cumulative total-return factor.                    | `255.43`           | Total Return factor (Dividends + splits) used for raw historical alpha PM generation. Same method of recalculations. |
| **System_Time**    | `timestamp` | UTC time for record append                         | `2023-08-11 16:30` |                                                                                                                      |

---

## 6. Option_Info
**Purpose:** Option conventions recorded at the underlying-security level.
**Type:** DIM
**Logical Grain:** `Security ID`
**Physical PK:** `Security ID + System_Time`

**Note**: A better name for this table would be `Security_OptionInfo`

| Column              | Type        | Description                     | Example            | Notes                                           |
| :------------------ | :---------- | :------------------------------ | :----------------- | :---------------------------------------------- |
| **Security ID**     | `int`       | Underlying security identifier. | `10001001`         |                                                 |
| Dividend Convention | `varchar`   | Dividend pricing expectation.   | `D`                | Assumed to be rarely changed (regulated by OCC) |
| Exercise Style      | `varchar`   | American or European.           | `A`                |                                                 |
| **System_Time**     | `timestamp` | UTC time for record append      | `2023-08-11 16:30` |                                                 |

---

## 7. Option_Contract [new]
**Purpose:**  Normalized table for per contract characteristics.
**Type:** DIM
**Logical Grain:** `Option ID`
**Physical PK:** `Option ID + System_Time`

**Note:** In some cases, the Options Clearing Council (OCC) may deprecate an old option symbol (`AAPL --> AAPL1`) which is treated as a new Option ID.  See [reference](https://www.webull.com/help/faq/10831-Corporate-Actions-and-Non-Standard-Options) explanation.

The fields in this table are expected to be constant for each Option ID and hence are normalized out of the `Option_Price` table.

| Column          | Type        | Description                      | Example             | Notes                                                                                          |
| :-------------- | :---------- | :------------------------------- | :------------------ | :--------------------------------------------------------------------------------------------- |
| **Option ID**   | `bigint`    | Unique identifier.               | `99827371`          | `bigint` because option count may grow into billions.                                          |
| Security ID     | `int`       | Underlying security identifier.  | `10001001`          | Allows for joining back to `Options_Info`                                                      |
| Symbol          | `varchar`   | Option symbol                    | `AAPL 230818C00180` | Is unique. Option ID serves as the surrogate key.                                              |
| Symbol Flag     | `int`       | Notation version flag.           | `1`                 |                                                                                                |
| Strike          | `int`       | Strike price multiplied by 1000. | `180000`            | OptionMetrics integer standard to normalize non-integer strikes on underlying with low prices. |
| Expiration      | `date`      | Contract expiration date.        | `2023-08-18`        |                                                                                                |
| Call / Put      | `varchar`   | Call or Put specifier.           | `C`                 |                                                                                                |
| ContractSize    | `int`       | Deliverable quantity.            | `100`               |                                                                                                |
| AMSettlement    | `int`       | Settlement timing indicator.     | `0`                 | 0 = PM settlement (close); 1 = AM settlement (open). Impacts option "Days to Expiration" math. |
| ExpiryIndicator | `varchar`   | Weekly, Daily, Monthly flag.     | `W`                 |                                                                                                |
| **System_Time** | `timestamp` | UTC time for record append       | `2023-08-11 16:30`  |                                                                                                |

---

## 8. Option_Price
**Purpose:** Pure Fact table strictly daily contract pricing and Greeks.
**Type:** FACT
**Logical Grain:** `option_id + date`
**Physical PK:** `option_id + date + System_Time`

**Note:** There is no closing price, but can be assumed to be computed as `(Best_Bid + Best_Offer) / 2`

| Column             | Type        | Description                        | Example            | Notes                                                                                                     |
| :----------------- | :---------- | :--------------------------------- | :----------------- | :-------------------------------------------------------------------------------------------------------- |
| **Option ID**      | `bigint`    | Unique contract identifier.        | `99827371`         |                                                                                                           |
| **Date**           | `date`      | Observation date.                  | `2023-08-11`       |                                                                                                           |
| Best Bid           | `numeric`   | Highest bid across exchanges.      | `1.45`             |                                                                                                           |
| Best Offer         | `numeric`   | Lowest ask across exchanges.       | `1.48`             |                                                                                                           |
| Last Trade Date    | `date`      | Date the contract last traded.     | `2023-08-11`       | For handling zero volume days.                                                                            |
| Volume             | `bigint`    | Total contract volume.             | `2405`             | Zero volume days still generate database rows ensuring MM quotes/Greeks are available for market pricing. |
| Open Interest      | `bigint`    | Contracts outstanding.             | `15034`            |                                                                                                           |
| Special Settlement | `int`       | Expiration special-case indicator. | `0`                | Enum triggering on market events (Trading Halts, Cash-Merger).                                            |
| Implied Volatility | `numeric`   | Calculated implied volatility.     | `0.185`            |                                                                                                           |
| Delta              | `numeric`   | Option delta.                      | `0.42`             |                                                                                                           |
| Gamma              | `numeric`   | Option gamma.                      | `0.05`             |                                                                                                           |
| Vega               | `numeric`   | Option vega.                       | `0.08`             |                                                                                                           |
| Theta              | `numeric`   | Option theta.                      | `-0.02`            |                                                                                                           |
| Adjustment Factor  | `numeric`   | Cumulative adjustment factor.      | `1.0`              | Maps split mechanics of the underlying for back calculation of bids and offers.                           |
| **System_Time**    | `timestamp` | UTC time for record append         | `2023-08-11 16:30` |                                                                                                           |
|                    |             |                                    |                    |                                                                                                           |

---

## 9. Forward_Price
**Purpose:** Expected forward price by underlying and expiration. Used as inputs for calculation of other fields.
**Type:** FACT
**Logical Grain:** `Security ID + Date + Expiration
**Physical PK:** `Security ID + Date + Expiration + System_Time`

| Column          | Type        | Description                     | Example      | Notes |
| :-------------- | :---------- | :------------------------------ | :----------- | :---- |
| **Security ID** | `int`       | Underlying security identifier. | `10001001`   |       |
| **Date**        | `date`      | Date of the record.             | `2023-08-11` |       |
| **Expiration**  | `date`      | Option expiration date.         | `2023-08-18` |       |
| Forward Price   | `numeric`   | Expected underlying baseline.   | `177.85`     |       |
| **System_Time** | `timestamp` | UTC time for record append      | `2023-08-11` |       |

---

## 10. Zero_Curve
**Purpose:** Pure interest-rate cost-of-capital extraction mapping globally across the framework.
**Type:** REFERENCE (FACT)
**Logical Grain:** `Date + Days`
**Physical PK:** `Date + Days + System_Time`

| Column          | Type        | Description                     | Example            | Notes                                                          |
| :-------------- | :---------- | :------------------------------ | :----------------- | :------------------------------------------------------------- |
| **Date**        | `date`      | Date of the zero curve.         | `2023-08-11`       |                                                                |
| **Days**        | `int`       | Days to maturity.               | `7`                |                                                                |
| Expiration Date | `date`      | Pre-computed expiration anchor. | `2023-08-18`       | New pre-computation based on `Days` to reduce runtime compute. |
| Rate            | `numeric`   | Continuously compounded rate.   | `0.053`            |                                                                |
| **System_Time** | `timestamp` | UTC time for record append      | `2023-08-11 16:30` |                                                                |

---

