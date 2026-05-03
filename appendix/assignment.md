
# Options Data Model Exercise

## What we want you to do
* Review the dataset summary and table definitions below.
* Come prepared to describe a logical data model for the selected tables.
* Your model should cover table relationships, row grain, keys, column types, and any assumptions or open questions.
* You do not need to build the warehouse, write DDL, or implement pipelines.

## Dataset overview
This dataset is a historical dataset for US listed equity and index options. For this exercise, focus on the core records needed to represent the underlying security, historical changes to that security, daily underlying prices, option conventions, daily option observations, corporate actions, and a small set of supporting pricing inputs.

## What to prepare
* A proposed logical data model for the tables listed in this brief.
* How the tables relate to one another.
* What you believe the row grain is for each table.
* Which columns should act as primary keys, foreign keys, and natural identifiers.
* Any important data-type, scaling, or history-handling decisions.

## Scope
Only model the tables in this brief. The full dataset manual contains additional derived analytical files, but you do not need those for this exercise.

## Tables to include in your model
* Security
* Security_Name
* Exchange
* Distribution
* Security_Price
* Option_Info
* Option_Price
* Forward_Price
* Zero Curve

---

## Security
**Purpose:** Current reference table for each underlying security.

| Column | Description |
|---|---|
| Security ID | Unique identifier for the security. |
| CUSIP | First 8 digits of the current CUSIP. |
| Ticker | Current ticker symbol base. Class is stored separately. |
| SIC | SIC code. |
| Index Flag | Indicates whether the security is an index. |
| Exchange Flags | Encoded exchange or listing flags. |
| Class | Security class designator, if any. |
| Issue Type | Type of security, such as common stock, index, ETF, ADR, fund, or unit. |
| Industry Group | 3-digit Morningstar industry-group classification. |

## Security_Name
**Purpose:** Historical record of changes to the security's identifying details.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Date | Effective date of the change. |
| CUSIP | First 8 digits of the CUSIP as of that date. |
| Ticker | Ticker base as of that date. |
| Class | Class designator as of that date. |
| Issuer Description | Description of the issuing company or entity. |
| Issue Description | Description of the issue. |
| SIC | SIC code as of that date. |

## Exchange
**Purpose:** Historical record of listing, delisting, and exchange changes.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Date | Effective date of the exchange change. |
| Sequence Number | Distinguishes multiple exchange events on the same date. |
| Status | Status or event code, such as listed, delisted, suspended, reactivated, or inactive. |
| Exchange | Exchange added or deleted. |
| Add/Delete Indicator | Shows whether the exchange was added or removed. |
| Exchange Flags | Primary exchange after the change. |

## Distribution
**Purpose:** Corporate-action and distribution history for the security.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Record Date | Record date for the distribution. |
| Sequence Number | Distinguishes multiple distributions with the same record date. |
| Ex Date | Date the security begins trading without the value of the next distribution. |
| Amount | Cash amount if announced; yield if the dividend is projected. |
| Adjustment Factor | Adjustment used to compare pre- and post-distribution prices. |
| Declare Date | Declaration date, if available. |
| Payment Date | Payment date. |
| Link Security ID | Security ID of an acquiring company or spun-off security when relevant. |
| Distribution Type | Type of distribution, such as regular dividend, split, stock dividend, special dividend, or spin-off. |
| Frequency | Dividend-payment frequency. |
| Currency | ISO currency code. |
| Approximate Flag | Shows whether the amount is exact or approximate. |
| Cancel Flag | Shows whether the distribution was cancelled or omitted. |
| Liquidation Flag | Shows whether the distribution is liquidating or non-liquidating. |

## Security_Price
**Purpose:** Daily price history for the underlying security.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Date | Date of the price record. |
| Bid/Low | If positive, low price; if negative, closing bid when there was no trading. |
| Ask/High | If positive, high price; if negative, closing ask when there was no trading. |
| Close Price | Closing price; if negative, average of closing bid and ask. |
| Volume | Sum of volume across exchanges. |
| Total Return | Holding-period return from the last good pricing date. |
| Adjustment Factor | Cumulative split-style adjustment factor. |
| Open Price | Opening price, or 0 if unavailable. |
| Shares Outstanding | Public shares outstanding, shown in thousands. |
| Adjustment Factor2 | Cumulative total-return factor, including dividends and spin-offs. |

## Option_Info
**Purpose:** Option conventions recorded at the underlying-security level.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Dividend Convention | How dividends are incorporated into option calculations. |
| Exercise Style | Exercise style, such as American or European. |

## Option_Price
**Purpose:** Daily option observations for individual contracts.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Date | Observation date. |
| Symbol | Option symbol. |
| Symbol Flag | Indicates old notation versus OSI notation. |
| Strike | Strike price multiplied by 1000. |
| Expiration | Expiration date of the contract. |
| Call/Put | Call or put. |
| Best Bid | Highest bid across exchanges. |
| Best Offer | Lowest ask across exchanges. |
| Last Trade Date | Date the contract last traded. |
| Volume | Total contract volume. |
| Open Interest | Contracts outstanding. |
| Special Settlement | Settlement or expiration special-case indicator. |
| Implied Volatility | Calculated implied volatility when available. |
| Delta | Option delta. |
| Gamma | Option gamma. |
| Vega | Option vega. |
| Theta | Option theta. |
| Option ID | Unique identifier for the option contract. |
| Adjustment Factor | Cumulative adjustment factor for the option. |
| AMSettlement | Indicates whether expiration is based on market open or market close. |
| ContractSize | Deliverable quantity, usually 100. |
| ExpiryIndicator | Regular, weekly, daily, end-of-month, or unknown. |

## Forward_Price
**Purpose:** Forward price inputs by underlying and expiration.

| Column | Description |
|---|---|
| Security ID | Underlying security identifier. |
| Date | Date of the record. |
| Expiration | Option expiration date. |
| AMSettlement | Open-settled versus close-settled convention. |
| Forward Price | Forward price of one share of the underlying on the expiration date. |

## Zero_Curve
**Purpose:** Interest-rate curve used in option pricing.

| Column | Description |
|---|---|
| Date | Date of the zero curve. |
| Days | Days to maturity. |
| Rate | Continuously compounded zero-coupon rate. |

---

## Reminder
* Do not assume the structure shown here is already the correct model.
* Part of the exercise is deciding how the tables should relate, what the correct grain is, and which columns should be keys.
* You can make reasonable assumptions, as long as you can explain them.
