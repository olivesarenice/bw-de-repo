[!] This file was originally downloaded and converted to Markdown from: https://lib.tsinghua.edu.cn/PDF/OptionMetricsshiyongzhinan.pdf

---

## Introduction[cite: 1]

IvyDB is a comprehensive database of historical price, implied volatility, and sensitivity information for the entire US listed index and equity options markets.[cite: 1] The product has been designed to provide data of the highest obtainable quality, suitable for empirical and/or econometric studies of the options markets, development and testing of option trading strategies, and options research support.[cite: 1] IvyDB includes historical data for all US listed equities and market indices and all US listed index and equity options from 1996 till present.[cite: 1] IvyDB data files are updated nightly to reflect new closing prices, dividend payments or other corporate actions, and option contract expirations, new listings, or other changes.[cite: 1]

OptionMetrics compiles the IvyDB data from raw 3:59PM ET price information.[cite: 1] This raw data is edited and organized to facilitate its use in options market research.[cite: 1] Interest rate curves, dividend projections, and option implied volatilities and sensitivities are calculated by OptionMetrics using our proprietary algorithms, which are based on standard market conventions.[cite: 1]

---

## File Formats[cite: 1]

The data within IvyDB is organized in several files:[cite: 1]
*   Security file (IVYSECUR.yyyymmddD.txt)[cite: 1]
*   Security_Name file (IVYSECNM.yyyymmddD.txt)[cite: 1]
*   Exchange file (IVYEXCHG.yyyymmddD.txt)[cite: 1]
*   Distribution file (IVYDISTR.yyyymmddD.txt)[cite: 1]
*   Distribution_Projection file (IVYDISTRPROJ.yyyymmddD.txt)[cite: 1]
*   Security_Price file (IVYSECPR.yyyymmddD.txt)[cite: 1]
*   Option_Info file (IVYOPINF.yyymmddD.txt)[cite: 1]
*   Option_Price file (IVYOPPRC.yyyymmddD.txt)[cite: 1]
*   Zero_Curve file (IVYZEROC.yyyymmddD.txt)[cite: 1]
*   Index_Dividend file (IVYIDXDV.yyyymmddD.txt)[cite: 1]
*   Std_Option_Price file (IVYSTDOP.yyyymmddD.txt)[cite: 1]
*   Option_Volume file (IVYOPVOL.yyyymmddD.txt)[cite: 1]
*   Volatility_Surface file (IVYVSURF.yyyymmddD.txt)[cite: 1]
*   Historical Volatility file (IVYHVOL.yyyymmddD.txt)[cite: 1]
*   Open_Interest file (IVYOPTOI.txt)[cite: 1]
*   Forward_Price file (IVYFWDPR. yyyymmddD.txt)[cite: 1]

Files are produced nightly in a tab-delimited format.[cite: 1] Security, Security_Name, Exchange, Distribution and Option_Info files contain a full copy of the tables by the same name.[cite: 1] Therefore, these five tables are being truncated during the nightly data load processes.[cite: 1]

In the descriptions below, the layout of each file is shown, giving the data type, maximum field length (for character fields) and the field name.[cite: 1] All dates are given in YYYYMMDD format.[cite: 1] The primary key (unique fields) for each file is shown in bold.[cite: 1]

---

### Security File[cite: 1]

The Security file contains information on all equity and index securities known to IvyDB.[cite: 1]

**File layout**[cite: 1]

| Data type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| char | 8 | CUSIP[cite: 1] |
| char | 6 | Ticker[cite: 1] |
| char | 4 | SIC[cite: 1] |
| char | 1 | Index Flag[cite: 1] |
| integer | | Exchange Flags[cite: 1] |
| char | 1 | Class[cite: 1] |
| char | 1 | Issue Type[cite: 1] |
| char | 3 | Industry Group[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID is the unique identifier for this security.[cite: 1] Unlike CUSIP numbers and ticker symbols, Security IDs are unique over the security's lifetime and are not recycled.[cite: 1] The Security ID is the primary key for all data contained in IvyDB.[cite: 1]
*   **CUSIP**: The first 8 digits of the security's current CUSIP number[cite: 1]
*   **Ticker**: Ticker is the security's current ticker symbol.[cite: 1] For stocks with multiple classes, this field contains only the base of the complete ticker.[cite: 1] For example, NYSE tickers BKS.A and BKS.B would both contain BKS in the ticker field.[cite: 1] Class indicators are stored in the Class field.[cite: 1] If the field is empty the security is delisted.[cite: 1]
*   **SIC**: The security's SIC code[cite: 1]
*   **Index Flag**: This flag indicates whether the security is an index.[cite: 1] It is set to '1' if the security is an index and to '0' otherwise.[cite: 1]
*   **Exchange Flags**: The sum of all exchange flags indicating the US exchanges where the security is currently listed.[cite: 1] This field can be set to any of the below or the sum of any combination of the below exchange flags: 00000 - Currently delisted; 00001 - NYSE/ARCA; 00002 - AMEX; 00004 - NASDAQ National Markets System; 00008 - NASDAQ Small Cap; 00016 - OTC Bulletin Board; 00032 - BATS Global Markets; 00064 - Investors Exchange; 32768 - The security is an index.[cite: 1]
*   **Class**: The class designator, if any, of the security on the effective date[cite: 1]
*   **Issue Type**: The type of security: 0 - Common Stock; A - Market index; 7 - Mutual or investment trust fund; F - ADR/ADS; % - Exchange-traded fund; S - Structured Product; U - Unit; (blank) - Unspecified.[cite: 1]
*   **Industry Group**: IndustryGroup field is a 3-digit classification code for the security in the North American Industry Groups database provided by MorningStar.[cite: 1] The first digit represents the security's macroeconomic sector classification; the second digit represents the security's business segment; and the third digit represents the security's industry group.[cite: 1] A complete listing of the MG Sector Classification Code is given in Appendix A.[cite: 1]

---

### Security_Name File[cite: 1]

The Security_Name file contains a historical record of changes to the ticker, issuer and issue descriptions, and CUSIP for a security.[cite: 1]

**File layout**[cite: 1]

| Data type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| char | 8 | CUSIP[cite: 1] |
| char | 6 | Ticker[cite: 1] |
| char | 1 | Class[cite: 1] |
| char | 28 | Issuer Description[cite: 1] |
| char | 20 | Issue Description[cite: 1] |
| char | 4 | SIC[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the security[cite: 1]
*   **Date**: The effective date of the change[cite: 1]
*   **CUSIP**: The first 8 digits of the security's CUSIP as of the effective date[cite: 1]
*   **Ticker**: The base portion of the security's ticker on the effective date.[cite: 1] If the field is empty the security is delisted.[cite: 1]
*   **Class**: The class designator, if any, of the security on the effective date[cite: 1]
*   **Issuer Description**: A description of the issuing company or entity[cite: 1]
*   **Issue Description**: A description of the issue[cite: 1]
*   **SIC**: The SIC code for the security[cite: 1]

> **Notes:** All securities have at least one Security Name record dating from the start of the historical record, containing the security's ticker, CUSIP, and descriptive information as of the starting date of IvyDB.[cite: 1]

---

### Exchange File[cite: 1]

The Exchange file contains a historical record of changes to the active exchange for a security, and new listing and delisting information.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| integer | | **Sequence Number**[cite: 1] |
| char | 1 | Status[cite: 1] |
| char | 1 | Exchange[cite: 1] |
| char | 1 | Add/Delete (Indicator)[cite: 1] |
| integer | | Exchange Flags[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the security.[cite: 1]
*   **Date**: The effective date of the exchange change[cite: 1]
*   **Sequence Number**: A unique integer, starting from 1, to distinguish between multiple exchange changes occurring on the same day.[cite: 1]
*   **Status**: The change in the status of the security that generated the exchange record: \$ - Initial entry (start of historical record); A - The security is inactive (no longer being priced); C - The security has been purged due to inactivity; D - The security has been delisted; E - The security's exchange has changed; L - The security has been listed; N - The security has been newly listed (but not yet priced); S - Trading in the security has been suspended; X - Security is inactive due to an acquisition or merger; 3 - The security has been reactivated, and this is the first day priced; 4 - The security is new, and this is the first day priced; 5 - Matured, called or expired.[cite: 1]
*   **Exchange**: The exchange added or deleted: A - NYSE; B - AMEX; F - NASDAQ National Market System; G - Index; H - NASDAQ Small Cap; O - OTC Bulletin Board; % - Other OTC; ? - Exchange not known; D - Chicago Stock Exchange; E - ARCA Stock Exchange; I - Investors Exchange (IEX); J - Toronto Stock Exchange; K - Montreal Stock Exchange; N - Archipelago/Pacific Exchange (ARCA); S - BATS Global Markets; T - Boston Stock Exchange; U - Non-NASDAQ OTC; V - Canadian Venture Exchange (CDNX); X - OTC Equipment Trust.[cite: 1]
*   **Add/Delete**: * - Exchange was added; (blank) - Exchange was deleted.[cite: 1]
*   **Exchange Flags**: The primary exchange for the issue, after the change: 00000 - Currently delisted; 00001 - NYSE/ARCA; 00002 - AMEX; 00004 - NASDAQ National Markets System; 00008 - NASDAQ Small Cap; 00016 - OTC Bulletin Board; 00032 - BATS Global Markets; 00064 - IEX; 32768 - The security is an index.[cite: 1]

> **Notes:** All securities have at least one Exchange record dating from the start of the historical record, with status '\$', containing the security's exchange listing information as of the starting date of IvyDB.[cite: 1]

---

### Distribution File[cite: 1]

The Distribution file contains information on a security's distributions and splits*.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Record Date**[cite: 1] |
| integer | | **Sequence Number**[cite: 1] |
| date | | Ex Date[cite: 1] |
| real | | Amount[cite: 1] |
| real | | Adjustment Factor[cite: 1] |
| date | | Declare Date[cite: 1] |
| date | | Payment Date[cite: 1] |
| integer | | Link Security ID[cite: 1] |
| char | 1 | Distribution Type[cite: 1] |
| char | 1 | Frequency[cite: 1] |
| char | 3 | Currency[cite: 1] |
| char | 1 | Approximate flag[cite: 1] |
| char | 1 | Cancel flag[cite: 1] |
| char | 1 | Liquidation flag[cite: 1] |

*\* Do not use the Distribution File for Market Indices.*[cite: 1]

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the security[cite: 1]
*   **Record Date**: The record date for the distribution[cite: 1]
*   **Sequence Number**: A unique integer, starting from 1, to distinguish between multiple distributions with the same record date[cite: 1]
*   **Ex Date**: The ex-distribution or ex-dividend date[cite: 1]
*   **Amount**: The dollar amount of the cash distribution if the distribution was announced; yield if the dividend is projected (the dividend is projected when the Distribution Type is %)[cite: 1]
*   **Adjustment Factor**: The adjustment to the security's price that is required to compare pre-distribution to post-distribution prices[cite: 1]
*   **Declare Date**: The declaration date for the distribution (if available)[cite: 1]
*   **Payment Date**: The payment date for the distribution[cite: 1]
*   **Link Security ID**: For mergers and acquisitions LinkSecurityID is the Security ID corresponding to the equity of the acquiring company.[cite: 1] For spin-offs, it is the Security ID of the spun-off security.[cite: 1]
*   **Distribution Type**: The type of distribution: 0 - Unknown or not yet classified; 1 - Regular dividend; 2 - Split; 3 - Stock dividend; 4 - Capital gain distribution; 5 - Special dividend; 6 - Spin-off; 7 - New equity issue (same company); 8 - Rights offering; 9 - Warrants issue; % - Regular dividend projection.[cite: 1]
*   **Frequency**: Payment frequency: 0 - Dividend omitted; 1 - Annual; 2 - Semiannual; 3 - Quarterly; 4 - Monthly; 5 - Frequency varies; blank - Not available.[cite: 1]
*   **Currency**: The ISO code for currency of the cash distribution[cite: 1]
*   **Approximate flag**: 0 - Amount field is exact; 1 - Amount field is approximate.[cite: 1]
*   **Cancel flag**: 0 - The distribution was or will be made as scheduled; 1 - The distribution was cancelled, or a regular payment was omitted.[cite: 1]
*   **Liquidation Flag**: 0 - The distribution is a non-liquidating distribution; 1 - The distribution is either a partial or total liquidating distribution.[cite: 1]

---

### Distribution_Projection File[cite: 1]

The Distribution_Projection file contains forecasted discrete dividends as of each day of option pricing.[cite: 1] The projections are made five years out based on the past dividend pattern.[cite: 1] This file also includes any announced dividend that have not gone ex as of the projection date.[cite: 1]

**File layout**[cite: 1]

| Datatype | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Projection Date**[cite: 1] |
| date | | **Ex Date**[cite: 1] |
| real | | Amount[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Projection Date**: The date as of which the projections were made.[cite: 1] Only the information known as of the date is considered to project future dividends.[cite: 1]
*   **Ex Date**: The forecasted exercise date of the regular dividend.[cite: 1]
*   **Yield** *(listed as Amount in layout)*: The forecasted yield of the regular dividend.[cite: 1]

---

### Security_Price File[cite: 1]

The Security_Price file contains the price history for the security.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| real | | Bid/Low[cite: 1] |
| real | | Ask/High[cite: 1] |
| real | | Close Price[cite: 1] |
| bigint | | Volume[cite: 1] |
| real | | Total Return[cite: 1] |
| real | | Adjustment Factor[cite: 1] |
| real | | Open Price[cite: 1] |
| integer | | Shares Outstanding[cite: 1] |
| real | | Adjustment Factor2[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the security.[cite: 1]
*   **Date**: The date for this price record[cite: 1]
*   **Bid/Low**: If this field is positive, then it is the low price for the security on this date.[cite: 1] If it is negative, there was no trading on this date, and the field represents the closing bid price for the security.[cite: 1]
*   **Ask/High**: If this field is positive, then it is the high price for the security on this date.[cite: 1] If it is negative, there was no trading on this date, and the field represents the closing ask price for the security.[cite: 1]
*   **Close Price**: If this field is positive, then it is the closing price for the security on this date.[cite: 1] If it is negative, then it is the average of the closing bid and ask prices for the security on this date.[cite: 1] In case there are no valid bid or ask for the day, the record does not appear in the table at all.[cite: 1]
*   **Volume**: Volume field is set to the sum of volumes on all exchanges where the security traded given day.[cite: 1]
*   **Total Return**: The holding period return for this security, from the last good pricing date to this date.[cite: 1] The holding period return is calculated as the total price appreciation for the security over the holding period (adjusted for splits and other price factor changes) plus the cash value of any distributions which go ex-dividend during the holding period, divided by the security's last available closing price (or bid-ask midpoint).[cite: 1]
*   **Adjustment Factor (Cumulative Adjustment Factor)**: This is the cumulative product of all the adjustment factors for this security as of this date.[cite: 1] When a security is first listed, its Cumulative Adjustment factor is set to 1.0.[cite: 1] For all subsequent dates, the Cumulative Adjustment Factor is the product of all non-zero Adjustment Factors from the Distribution file having ex-date prior or equal to the date of this price.[cite: 1] For example, if a security has a 2-for-1 split on day T1 and a 3-for-1 split on day T2, the initial adjustment factor of 1 would become 2 on T1, and 6 on T2.[cite: 1] If there is a subsequent 3-for-2 split on day T3, the cumulative adjustment factor would become 9.[cite: 1] To calculate an adjusted close price for a security on a given day, multiply the Close Price by the Cumulative Adjustment Factor on that day and divide by the value of the Cumulative Adjustment Factor for this security as of today (i.e., the last date in the Security Price file for this security).[cite: 1]
*   **Open Price**: The opening price for this security, if available (equal to 0 if there is no opening price).[cite: 1]
*   **Shares Outstanding**: The total number of publicly traded shares at a security level lagged by one business day.[cite: 1] For ADRs the number represents the total shares outstanding of the foreign security up until June 8, 2018.[cite: 1] Starting from June 11, 2018 the number represents actual ADR shares outstanding.[cite: 1] All values in this field are shown in thousands.[cite: 1]
*   **Adjustment Factor2 (Cumulative Total Return Factor)**: Similar to the Cumulative Adjustment Factor but includes the effect of dividends and spin-offs.[cite: 1] When a security is first listed, its Cumulative Total Return factor is set to 1.0.[cite: 1] To calculate an adjusted close price for a security on a given day including dividends, multiply the Close Price by the Cumulative Total Return Factor on that day and divide by the value of the Cumulative Total Return Factor for this security as of today (i.e., the last date in the Security Price file for this security).[cite: 1]

---

### Option_Info File[cite: 1]

The Option_Info file contains information about the options for an underlying security.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| char | 1 | Dividend Convention[cite: 1] |
| char | 1 | Exercise Style[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Dividend Convention**: The method of incorporating dividends into the option calculations: (blank) - Discrete dividend payments, constant projected dividend yield; ? - Unknown or not yet classified; I - Continuous implied dividend yield; F - Options on futures.[cite: 1]
*   **Exercise Style**: A - American; E - European; ? - Unknown or not yet classified.[cite: 1]

---

### Option_Price File[cite: 1]

The Option_Price file contains the historical price, implied volatility, and sensitivity information for the options on an underlying security.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| char | 21 | **Symbol**[cite: 1] |
| char | 1 | Symbol Flag[cite: 1] |
| integer | | Strike[cite: 1] |
| date | | Expiration[cite: 1] |
| char | 1 | Call/Put[cite: 1] |
| real | | Best Bid[cite: 1] |
| real | | Best Offer[cite: 1] |
| date | | Last Trade Date[cite: 1] |
| integer | | Volume[cite: 1] |
| integer | | Open Interest[cite: 1] |
| char | 1 | Special Settlement[cite: 1] |
| real | | Implied Volatility[cite: 1] |
| real | | Delta[cite: 1] |
| real | | Gamma[cite: 1] |
| real | | Vega[cite: 1] |
| real | | Theta[cite: 1] |
| integer | | Option ID[cite: 1] |
| integer | | Adjustment Factor[cite: 1] |
| integer | | AMSettlement[cite: 1] |
| integer | | ContractSize[cite: 1] |
| char | | ExpiryIndicator[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date of this price[cite: 1]
*   **Symbol**: The option symbol[cite: 1]
*   **Symbol Flag**: The flag is set to 0 for the old option notation (i.e. root and suffix) and it is set to 1 if the symbol is the new OSI symbol.[cite: 1]
*   **Strike**: The strike price of the option times 1000.[cite: 1]
*   **Expiration**: The expiration date of the option[cite: 1]
*   **Call/Put**: C - Call; P - Put.[cite: 1]
*   **Best Bid**: The best, or highest bid price across all exchanges on which the option trades.[cite: 1] Until March 5, 2008, end-of-day quotes are used.[cite: 1] From then until July 29, 2009, 16:00 Eastern Time quotes are used.[cite: 1] From July 30, 2009 onward, 15:59 ET quotes are used.[cite: 1]
*   **Best Offer**: The best, or lowest ask price across all exchanges on which the option trades.[cite: 1] Until March 5, 2008, end-of-day quotes are used.[cite: 1] From then until July 29, 2009, 16:00 Eastern Time quotes are used.[cite: 1] From July 30, 2009 onward, 15:59 ET quotes are used.[cite: 1]
*   **Last Trade Date**: The date on which the option last traded[cite: 1]
*   **Volume**: The total volume of option contracts[cite: 1]
*   **Open Interest**: This is the open interest for the option, i.e. number of contracts outstanding.[cite: 1] Open interest is lagged by one day after November 28, 2000.[cite: 1] Prior to this date, the open interest is not lagged.[cite: 1] An Open Interest file with updated values is posted on the following morning (see Open_Interest file specs).[cite: 1]
*   **Special Settlement**: 0 - The option has a standard settlement (100 shares of underlying security are to be delivered at exercise; the strike price and premium multipliers are \$100 per tick).[cite: 1] 1 - The option has a non-standard settlement.[cite: 1] The number of shares to be delivered may be different from 100 (fractional shares); additional securities and/or cash may be required; and the strike price and premium multipliers may be different than \$100 per tick.[cite: 1] E - The option has a non-standard expiration date.[cite: 1] This is usually due to an error in the historical data which has not yet been researched and fixed.[cite: 1]
*   **Implied Volatility**: This is the calculated implied volatility of the option.[cite: 1] Implied volatilities are not calculated for options with non-standard settlement.[cite: 1]
*   **Delta**: Delta of an option indicates the change in option premium for a \$1.00 change in underlying price.[cite: 1]
*   **Gamma**: The gamma of an option indicates the absolute change in Delta for a \$1.00 change in underlying price.[cite: 1]
*   **Vega (Kappa)**: The vega/kappa of an option indicates the change in option premium, in cents, for one percentage point change in volatility.[cite: 1]
*   **Theta**: The theta of an option indicates the change in option premium as time passes, in terms of dollars per year.[cite: 1]
*   **Option ID**: Option ID is a unique integer identifier for the option contract.[cite: 1] This identifier can be used to track specific option contracts over time.[cite: 1]
*   **Adjustment Factor**: This is the cumulative product of all the adjustment factors for this option as of this date.[cite: 1] When an option is first listed, its adjustment factor is set to 1.[cite: 1] For all subsequent dates, the Adjustment Factor is the product of all non-zero Adjustment Factors from the Distribution file having ex-date prior or equal to the date of this price which result in an adjustment in the number of option contracts held.[cite: 1]
*   **AMSettlement**: 0 - options on the security expire at the market close of the last trading day; 1 - options on the security expire at the market open of the last trading day.[cite: 1] In other words, if an option is AM settled, as most cash-settled index option classes are, we use one less day than we use for PM-settled options to count days to expiration.[cite: 1]
*   **ContractSize**: It is the deliverable quantity of underlying entities, the standardized amount that tells buyers and sellers exact quantities that are being bought or sold based on the terms of the contract.[cite: 1] The standardized contract size for an option is 100 shares.[cite: 1]
*   **ExpiryIndicator**: This field indicates if the option is a regular, weekly or monthly option.[cite: 1] blank - regular option expiring on the third Friday of a month or unknown; w - weekly option; d - daily option; m - end of month option.[cite: 1]

---

### Forward Price File[cite: 1]

The Forward_Price file contains the forward price for each combination of each security sharing same expiration and Amsettlement indicator.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| date | | **Expiration**[cite: 1] |
| integer | | **AMSettlement**[cite: 1] |
| decimal | 14,6 | Forward Price[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the security.[cite: 1]
*   **Date**: The date for this price record[cite: 1]
*   **Expiration**: The expiration date of the option[cite: 1]
*   **AMSettlement**: 0 - options on the security expire at the market close of the last trading day; 1 - options on the security expire at the market open of the last trading day.[cite: 1] In other words, if an option is AM settled, as most cash-settled index option classes are, we use one less day than we use for PM-settled options to count days to expiration.[cite: 1]
*   **Forward Price**: This is the price of a single share of the underlying security on the expiration date of the option.[cite: 1] The forward security price is calculated based on the last closing security price, plus the interest, less projected dividends[cite: 1]

---

### Zero_Curve File[cite: 1]

The Zero_Curve file contains the current zero-coupon interest rate curve used by IvyDB.[cite: 1]

**File layout**[cite: 1]

| Datatype | Length | Field Name |
| :--- | :--- | :--- |
| date | | **Date**[cite: 1] |
| integer | | **Days**[cite: 1] |
| real | | Rate[cite: 1] |

**Field descriptions**[cite: 1]
*   **Date**: The date of the zero curve[cite: 1]
*   **Days**: The number of days to maturity[cite: 1]
*   **Rate**: The continuously compounded zero-coupon interest rate[cite: 1]

---

### Index Dividend File[cite: 1]

The Index_Dividend file contains the current dividend yield used for implied volatility calculations on index options.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| real | | Rate[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID of the underlying index[cite: 1]
*   **Date**: The date of this dividend yield[cite: 1]
*   **Rate**: The annualized dividend yield[cite: 1]

---

### Std_Option_Price File[cite: 1]

The Std_Option_Price file contains information on "standardized" (interpolated) options.[cite: 1] Currently, this file contains information on at-the-money-forward options with expirations of 10, 30, 60, 91, 122, 152, 182, 273, 365, 547 and 730 calendar days.[cite: 1] A standardized option is only included if there exists enough option price data on that date to accurately interpolate the required values.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| integer | | **Days**[cite: 1] |
| real | | Forward Price[cite: 1] |
| real | | Strike[cite: 1] |
| char | 1 | **Call/Put**[cite: 1] |
| real | | Premium[cite: 1] |
| real | | Implied Volatility[cite: 1] |
| real | | Delta[cite: 1] |
| real | | Gamma[cite: 1] |
| real | | Theta[cite: 1] |
| real | | Vega[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date of this option price[cite: 1]
*   **Days**: The number of days to expiration[cite: 1]
*   **Forward Price**: This is the price of a single share of the underlying security on the expiration date of the option.[cite: 1] The forward security price is calculated based on the last closing security price, plus the interest, less projected dividends.[cite: 1]
*   **Strike**: The strike price of the standardized option set to be equal to the forward price.[cite: 1]
*   **Call/Put**: C - Call; P - Put.[cite: 1]
*   **Premium**: The premium for the option is interpolated from Volatility Surface file.[cite: 1]
*   **Implied Volatility**: The implied volatility of the standardized option is derived by linear interpolation from the Volatility Surface file.[cite: 1]
*   **Delta**: Delta has units \$/\$.[cite: 1]
*   **Gamma**: Gamma has units \$/(\$^2).[cite: 1]
*   **Theta**: Theta of the option is annualized.[cite: 1]
*   **Vega/Kappa**: Vega/kappa of the option has the units of \$/volatility.[cite: 1] This can also be read as cents/%.[cite: 1]

---

### Option_Volume File[cite: 1]

The Option_Volume file contains daily total contract volume information for each underlying security.[cite: 1] Volume is aggregated by calls, puts, and total.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| char | 1 | **Call/Put**[cite: 1] |
| integer | | Volume[cite: 1] |
| integer | | Open Interest[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date of this option volume record[cite: 1]
*   **Call/Put**: C - Call; P - Put; blank - Total.[cite: 1]
*   **Volume**: The total contract volume for (call, put, all) options for the underlying security on the specified date.[cite: 1]
*   **Open Interest**: The total contract open interest for (call, put, all) options for the underlying security on the specified date.[cite: 1]

---

### Volatility_Surface File[cite: 1]

The Volatility_Surface file contains the interpolated volatility surface for each security on each day, using a methodology based on a kernel smoothing algorithm.[cite: 1] This file contains information on standardized options, both calls and puts, with expirations of 10, 30, 60, 91, 122, 152, 182, 273, 365, 547, and 730 calendar days, at deltas of 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90 (negative deltas for puts).[cite: 1] A standardized option is only included if there exists enough option price data on that date to accurately interpolate the required values.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| integer | | **Days**[cite: 1] |
| integer | | **Delta**[cite: 1] |
| char | 1 | **Call/Put**[cite: 1] |
| real | | Implied Volatility[cite: 1] |
| real | | Implied Strike[cite: 1] |
| real | | Implied Premium[cite: 1] |
| real | | Dispersion[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date of this option volume[cite: 1]
*   **Days**: The number of days to expiration[cite: 1]
*   **Delta**: Delta of the option[cite: 1]
*   **Call/Put**: C - Call; P - Put.[cite: 1]
*   **Implied Volatility**: The calculated interpolated implied volatility of the option[cite: 1]
*   **Implied Strike**: The strike price corresponding to this delta[cite: 1]
*   **Implied Premium**: The premium of a theoretical option with this delta and implied volatility[cite: 1]
*   **Dispersion**: Dispersion is a measure of the accuracy of the implied volatility calculation, roughly corresponding to a weighted standard deviation.[cite: 1] A larger dispersion indicates a less accurate smoothed implied volatility.[cite: 1] Dispersion is only calculated if there are at least two contracts with non-negative implied volatility in OPTION_PRICE for the day for the underlying security.[cite: 1] Otherwise dispersion is set to -99.99.[cite: 1]
    $$Dispersion=\sqrt{\frac{\sum_{i}V_{i}\sigma_{i}^{2}\Phi(x_{ij}y_{j}z_{jj})}{\sum_{i}V_{i}\Phi(x_{ij}y_{j}z_{j})}-\hat{\sigma}_{j}^{2}}$$[cite: 1]
    *\* Please refer to Calculation section for details.*[cite: 1]

---

### Historical_Volatility File[cite: 1]

The Historical_Volatility file contains the realized volatility for each optionable security on each day.[cite: 1] Realized volatility is calculated over date ranges of 10, 14, 30, 60, 91, 122, 152, 182, 273, 365, 547, 730 and 1825 calendar days, using a simple standard deviation calculation on the logarithm of the close-to-close daily total return.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| integer | | **Days**[cite: 1] |
| float | | Volatility[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date of this realized volatility calculation[cite: 1]
*   **Days**: The number of days included in the calculation[cite: 1]
*   **Volatility**: The calculated realized volatility[cite: 1]

---

### Open_Interest File*[cite: 1]

*\*Data is not provided as a part of the release files.*[cite: 1]

The Open_Interest file contains the previous day's open interest information for each option.[cite: 1] This file is provided each morning by 9:00 a.m. ET and is intended for clients who wish to receive this data earlier than in the Option_Price file.[cite: 1]

**File layout**[cite: 1]

| Data Type | Length | Field Name |
| :--- | :--- | :--- |
| integer | | **Security ID**[cite: 1] |
| date | | **Date**[cite: 1] |
| char | 21 | **Symbol**[cite: 1] |
| char | 1 | Symbol Flag[cite: 1] |
| integer | | Open Interest[cite: 1] |

**Field descriptions**[cite: 1]
*   **Security ID**: The Security ID for the underlying security[cite: 1]
*   **Date**: The date for the morning it was created.[cite: 1]
*   **Symbol**: The option symbol[cite: 1]
*   **Symbol Flag**: The flag is set to 0 for the old option notation (i.e. root and suffix) and it is set to 1 if the symbol is the new OSI symbol.[cite: 1]
*   **Open Interest**: The open interest for the option[cite: 1]

---

## Calculations[cite: 1]

The implied volatilities and option sensitivities contained in IvyDB are calculated in accordance with standard conventions used by participants in the equity and index option markets.[cite: 1]

### Interest Rates[cite: 1]

Each of the option pricing models used by IvyDB requires a continuously-compounded interest rate as input.[cite: 1] This interest rate is calculated from a collection of continuously-compounded zero-coupon interest rates at various maturities, collectively referred to as the zero curve.[cite: 1] The zero curve used by the IvyDB option models is derived from ICE IBA LIBOR rates and settlement prices of CME Eurodollar futures.[cite: 1]

For a given option, the appropriate interest rate input corresponds to the zero-coupon rate that has a maturity equal to the option's expiration, and is obtained by linearly interpolating between the two closest zero-coupon rates on the zero curve.[cite: 1]

The zero curve is calculated as follows:[cite: 1]

**Step 1.** The IBA LIBOR rates for maturities of 1 week and 1-12 months are converted to discount factors using the formula:[cite: 1]
$$DF=(1+r\times d/360)^{-1}$$[cite: 1]
where r is the IBA LIBOR rate and d is the actual number of days to maturity.[cite: 1]

**Step 2.** The LIBOR discount factors are converted to continuous LIBOR zero rates using the Actual/365 day-count convention:[cite: 1]
$$L=-365/d\times ln(DF)$$[cite: 1]
where L is the continuously-compounded LIBOR zero rate.[cite: 1]

**Step 3.** The zero rate on the nearest futures contract date (greater than one week) is obtained by linear interpolation between the two closest LIBOR zero rates computed in Step 2.[cite: 1]

**Step 4.** Each subsequent zero rate is computing by treating the Eurodollar strip implied future rate as a forward rate:[cite: 1]
$$F_{i}=100-P_{i}$$[cite: 1]
$$DF_{i}=DF_{i-1}/[1+(F_{i-1}/100)\times(n/360)]$$[cite: 1]
where $P_{i}$ is the Eurodollar settlement price and $F_{t}$ is the implied Eurodollar future rate for futures settlement date i, $DF_{i}$ is the discount factor to futures date i, and n is the number of days between futures settlement date $i-1$ and futures settlement date i.[cite: 1] This step is repeated to generate discount factors out to ten years.[cite: 1]

**Step 5.** Each of the calculated discount factors is converted into a zero rate by using the formula from Step 2.[cite: 1]

There is currently no convexity adjustment applied to the computed zero-coupon rates.[cite: 1]

### Dividends[cite: 1]

When the underlying equity or index pays dividends, each of the option pricing models requires an estimate of the dividends to be paid up until the option's expiration.[cite: 1] The methodology used by IvyDB for dividend payments depends on the type of the underlying security.[cite: 1]

The IvyDB option pricing methodology for equity options assumes that the security's current dividend yield (defined as the most recently announced dividend payment divided by the most recent closing price for the security) remains constant over the remaining term of the option.[cite: 1] This "constant dividend yield" assumption is consistent with most dividend-based equity pricing models (such as the Gordon growth model) under the additional assumptions of constant average security return and a constant earnings growth rate.[cite: 1]

Even though the dividend yield is constant, IvyDB assumes that the security pays dividends at specific pre-determined times, namely on the security's regularly scheduled ex-dividend date.[cite: 1] In the case of dividends that have already been declared, the ex-dividend dates are known.[cite: 1] For dividend payments that are yet unannounced, IvyDB uses a proprietary extrapolation algorithm to create a set of projected ex-dividend dates according to the security's usual dividend payment frequency.[cite: 1] These projections are listed in the distribution file as Distribution Type = '%' and extend out to five years.[cite: 1]

Because the actual cash dividend to be received on the ex-dividend date is a function of the security price on that date, and is computed internally by the option pricing models, the Amount field for the projected dates is set equal to dividend yield.[cite: 1]

For dividend-paying indices, IvyDB assumes that the security pays dividends continuously, according to a continuously-compounded dividend yield.[cite: 1] A put-call parity relationship is assumed, and the implied index dividend is calculated from the following linear regression model:[cite: 1]
$$C-P=b_{0}+b_{1}S+b_{2}ST+b_{3}K+b_{4}KT+b_{5}D_{BA}$$[cite: 1]
In this model, C-P is difference between the price of a call option and the price of a put option with the same expiration and strike.[cite: 1] When calculating this difference, the bid price of the call is used with the offer price of the put, and vice versa.[cite: 1] $D_{BA}$ is a dummy variable set equal to 1 if the call option's bid price is used.[cite: 1] S is the underlying security's (index's) closing price, K is the strike price of the call and put options, and T is the time to expiration in years.[cite: 1] The regression is calculated using three months of option data across all strikes and expirations with an exception of contracts expiring in less than 15 days, for a single underlying.[cite: 1] According to the principle of put-call parity, the dividend yield on the underlying index will be approximately equal to the negative of the estimated parameter $b_{2}$.[cite: 1]

This put-call parity relationship only holds exactly for European options.[cite: 1] There are only a few index options which trade according to American exercise: The AMEX Computer Technology Index; the Amex Oil Index; the CBOE Internet Index; the PHLX Semiconductor Index, the PHLX Gold Index; and the CBOE S&P 100 Index.[cite: 1] For the S&P 100 index, we assume that the dividend yield is equal to that computed for the S&P 500 index.[cite: 1] For the other American-exercise indices, we use the results of the dividend regression unmodified.[cite: 1] While this may induce a slight bias into the calculations, we expect the overall effect on the computed implied volatilities to be minimal.[cite: 1]

### European Options[cite: 1]

Most index options have a European-style exercise feature, and can be priced according to the Black-Scholes model:[cite: 1]

$$C=Se^{-qT}N(d_{1})-Ke^{-rT}N(d_{2})$$[cite: 1]
$$P=Ke^{-rT}N(-d_{2})-Se^{-qT}N(-d_{1})$$[cite: 1]
where
$$d_{1}=[ln(S/K)+(r-q+\frac{1}{2}\sigma^{2})T]/\sigma\sqrt{T}$$[cite: 1]
$$d_{2}=d_{1}-\sigma\sqrt{T}$$[cite: 1]

C is the price of a call option, P is the price of a put option, S is the current underlying security price, K is the strike price of the option, T is the time in years remaining to option expiration, r is the continuously-compounded interest rate, q is the continuously-compounded annualized dividend yield, and o is the implied volatility.[cite: 1]

For calculating implied volatilities and associated option sensitivities, the theoretical option price is set equal to the midpoint of the best closing bid price and best closing offer price for the option.[cite: 1] The Black-Scholes formula is then inverted using a numerical search technique to calculate the implied volatility for the option.[cite: 1]

### American Options[cite: 1]

Options that have an American-style exercise feature are priced using a proprietary pricing algorithm that is based on the industry-standard Cox-Ross-Rubinstein (CRR) binomial tree model.[cite: 1] This model can accommodate underlying securities with either discrete dividend payments or a continuous dividend yield.[cite: 1]

In the framework of the CRR model, the time between now and option expiration is divided into N sub-periods.[cite: 1] Over the course of each sub-period, the security price is assumed to move either "up" or "down".[cite: 1] The size of the security price move is determined by the implied volatility and the size of the sub-period.[cite: 1] Specifically, the security price at the end of sub-period i is given by one of the following:[cite: 1]
$$S_{i+1}^{up}=S_{i}u\equiv S_{i}exp(\sigma\sqrt{h})$$[cite: 1]
$$S_{i+1}^{down}=S_{i}d\equiv S_{i}exp(-\sigma\sqrt{h})$$[cite: 1]
where $h\equiv T/N$ is the size of the sub-period, and $S_{i}$ is the security price at the beginning of the sub-period.[cite: 1]

The price of a call option at the beginning of each sub-period is dependent on its price at the end of the sub-period, and is given by:[cite: 1]
$$C_{i}=max\{\begin{matrix}[pC_{i+1}^{up}+(1-p)C_{i+1}^{down}]/R\\ S_{i}-K\end{matrix}\}$$[cite: 1]
and likewise, for a put option.[cite: 1] Here, r is the interest rate, q is the continuous dividend yield (if the security is an index), $R\equiv exp([r-q]h)$ and $C_{i+1}^{up}$ and $C_{i+1}^{down}$ are the price of the option at the end of the sub-period, depending on whether the security price moves "up" or "down".[cite: 1] The "risk-neutral" probability p is given by:[cite: 1]
$$p=\frac{R-d}{u-d}$$[cite: 1]

To use the CRR approach to value an option, we start at the current security price S and build a "tree" of all the possible security prices at the end of each sub-period, under the assumption that the security price can move only either up or down.[cite: 1] The tree is constructed out to time T (option expiration).[cite: 1]

Next the option is priced at expiration by setting the option expiration value equal to the exercise value: $C=max(S-K,0)$ and $P=max(K-S,0)$.[cite: 1] The option price at the beginning of each sub-period is determined by the option prices at the end of the sub-period, using the formula above.[cite: 1] Working backwards, the calculated price of the option at time $i=0$ is the theoretical model price.[cite: 1]

To compute the implied volatility of an option given its price, the model is run iteratively with new values of $\sigma$ until the model price of the option converges to its market price, defined as the midpoint of the option's best closing bid and best closing offer prices.[cite: 1] At this point, the final value of o is the option's implied volatility.[cite: 1]

The CRR model is adapted to securities that pay discrete dividends as follows: When calculating the price of the option from equation (1), the security price $S_{i}$ used in the equation is set equal to the original tree price ${S_{i}}^{0}$ minus the sum of all dividend payments received between the start of the tree and time i.[cite: 1] Under the constant dividend yield assumption, this means that the security price $S_{i}$ used in equation (1) should be set equal to $S_{i}^{0}(1-n\delta)$, where ${S_{i}}^{\theta}$ is the original tree price, $\delta$ is the dividend yield, and n is the number of dividend payments received up to time i.[cite: 1] All other calculations are the same.[cite: 1]

The CRR model usually requires a very large number of sub-periods to achieve good results (typically, $N>1000)$, and this often results in a large computational requirement.[cite: 1] The IvyDB proprietary pricing algorithm uses advanced techniques to achieve convergence in a fraction of the processing time required by the standard CRR model.[cite: 1]

### Standardized Option Prices[cite: 1]

The standardized option prices and implied volatilities in the Std_Option_Price file are calculated using linear interpolation from the Volatility_Surface file.[cite: 1] First the forward price of the underlying security is calculated using the zero curve and the projected distributions.[cite: 1] Next, the volatility surface points are linearly interpolated to the forward price and the target expiration, to generate an at-the-money-forward implied volatility.[cite: 1]

### Volatility Surface[cite: 1]

The standardized option implied volatilities in the Volatility_Surface file are calculated using a kernel smoothing technique.[cite: 1] The data is first organized by the log of days to expiration and by "call-equivalent delta" (delta for a call, one plus delta for a put).[cite: 1] A kernel smoother is then used to generate a smoothed volatility value at each of the specified interpolation grid points.[cite: 1]

At each grid point j on the volatility surface, the smoothed volatility $\hat{\sigma}_{j}$ is calculated as a weighted sum of option implied volatilities:[cite: 1]
$$\hat{\sigma}_{j}=\frac{\sum_{i}V_{i}\sigma_{i}\Phi(x_{ij},y_{ij},z_{ij})}{\sum_{i}V_{i}\Phi(x_{ij},y_{ij},z_{ij})}$$[cite: 1]
where i is indexed over all the options for that day, $V_{i}$ is the vega of the option, $\sigma_i$ is the implied volatility, and $\Phi(.)$ is the kernel function:[cite: 1]
$$\Phi(x,y,z)=\frac{1}{\sqrt{2\pi}}e^{-[(x^{2}/2h_{1})+(y^{2}/2h_{2})+(z^{2}/2h_{3})]}$$[cite: 1]
The parameters to the kernel function, $x_{ij}$, $y_{ij}$, and $z_{ij}$ are measures of the "distance" between the option and the target grid point:[cite: 1]
$$x_{ij}=log(T_{i}/T_{j})$$[cite: 1]
$$y_{ij}=\Delta_{i}-\Delta_{j}$$[cite: 1]
$$z_{ij}=I_{\{CP_{i}=CP_{j}\}}$$[cite: 1]
where $T_{i}(T_{j})$ is the number of days to expiration of the option (grid point); $\Delta_{i}(\Delta_{j})$ is the "call-equivalent delta" of the option (grid point); $CP_{i}(CP_{j})$ is the call/put identifier of the option (grid point); and $I\{.\}$ is an indicator function $(=0$ if the call/put identifiers are equal, or 1 if they are different).[cite: 1]

The kernel "bandwidth" parameters were chosen empirically and are set as $h_{I}=0.05$, $h_{2}=0.005$ and $h_{3}=0.001$.[cite: 1]

Options with vega value below 0.5 are exclude from volatility surface calculation to provide more stable surface.[cite: 1]

### Option and Underlying Price[cite: 1]

The option price used in implied volatility calculation is an average between max Bid and min Ask.[cite: 1] These are selected across all exchanges the contract is traded on.[cite: 1] Option prices used in implied volatility calculations up to March 4, 2008 are end of day prices.[cite: 1] Starting from March 5, 2008 we have been capturing best bid and best offer as close to 4 o'clock as possible to better synchronize the option price with the underlying close.[cite: 1] Currently all option quotes are captured at 15:59 ET.[cite: 1] The underlying price used is the official (composite) close.[cite: 1]

### Missing Values[cite: 1]

There are several situations where the implied volatilities cannot be calculated for the OPTION PRICE, STD OPTION PRICE, and VOLATILITY SURFACE tables.[cite: 1] These reasons change based on the method of calculation used and as a result differ by table.[cite: 1] These reasons are detailed below and are organized by tables.[cite: 1]

For the OPTION_PRICE table the implied volatility will be set to -99.99 if any of the following conditions hold:[cite: 1]
1.  The option is a "special settlement" (Special Settlement Flag = 1)[cite: 1]
2.  The midpoint of the bid/ask price is below intrinsic value[cite: 1]
3.  The implied volatility calculation fails to converge[cite: 1]
4.  The underlying price is not available[cite: 1]

For the STD_OPTION_PRICE and VOLATILITY_SURFACE tables the implied volatility will be set to -99.99 if an insufficient number of option data points are available to perform the interpolation.[cite: 1]

---

## Appendix[cite: 1]

### Industry Group Codes[cite: 1]

| Code | Description                                       | Code | Description                                      |
| :--- | :------------------------------------------------ | :--- | :----------------------------------------------- |
| 1    | Basic Materials[cite: 1]                          | 427  | Closed-End Fund - Foreign[cite: 1]               |
| 2    | Conglomerates[cite: 1]                            | 430  | Life Insurance[cite: 1]                          |
| 3    | Consumer Goods[cite: 1]                           | 431  | Accident & Health Insurance[cite: 1]             |
| 4    | Financial[cite: 1]                                | 432  | Property & Casualty Insurance[cite: 1]           |
| 5    | Healthcare[cite: 1]                               | 433  | Surety & Title Insurance[cite: 1]                |
| 6    | Industrial Goods[cite: 1]                         | 434  | Insurance Brokers[cite: 1]                       |
| 7    | Services[cite: 1]                                 | 440  | REIT - Diversified[cite: 1]                      |
| 8    | Technology[cite: 1]                               | 441  | REIT - Office[cite: 1]                           |
| 9    | Utilities[cite: 1]                                | 442  | REIT - Healthcare Facilities[cite: 1]            |
| 11   | Chemicals[cite: 1]                                | 443  | REIT- Hotel/Motel[cite: 1]                       |
| 12   | Energy[cite: 1]                                   | 444  | REIT- Industrial[cite: 1]                        |
| 13   | Metals & Mining[cite: 1]                          | 445  | REIT - Residential[cite: 1]                      |
| 21   | Conglomerates[cite: 1]                            | 446  | REIT - Retail[cite: 1]                           |
| 31   | Consumer Durables[cite: 1]                        | 447  | Mortgage Investment[cite: 1]                     |
| 32   | Consumer Non-Durables[cite: 1]                    | 448  | Property Management[cite: 1]                     |
| 33   | Automotive[cite: 1]                               | 449  | Real Estate Development[cite: 1]                 |
| 34   | Food & Beverage[cite: 1]                          | 510  | Drug Manufacturers - Major[cite: 1]              |
| 35   | Tobacco[cite: 1]                                  | 511  | Drug Manufacturers - Other[cite: 1]              |
| 41   | Banking[cite: 1]                                  | 512  | Drugs Generic[cite: 1]                           |
| 42   | Financial Services[cite: 1]                       | 513  | Drug Delivery[cite: 1]                           |
| 43   | Insurance[cite: 1]                                | 514  | Drug Related Products[cite: 1]                   |
| 44   | Real Estate[cite: 1]                              | 515  | Biotechnology[cite: 1]                           |
| 51   | Drugs[cite: 1]                                    | 516  | Diagnostic Substances[cite: 1]                   |
| 52   | Health Services[cite: 1]                          | 520  | Medical Instruments & Supplies[cite: 1]          |
| 61   | Aerospace/Defense[cite: 1]                        | 521  | Medical Appliances & Equipment[cite: 1]          |
| 62   | Industrial[cite: 1]                               | 522  | Health Care Plans[cite: 1]                       |
| 63   | Materials & Construction[cite: 1]                 | 523  | Long-Term Care Facilities[cite: 1]               |
| 71   | Leisure[cite: 1]                                  | 524  | Hospitals[cite: 1]                               |
| 72   | Media[cite: 1]                                    | 525  | Medical Laboratories & Research[cite: 1]         |
| 73   | Retail[cite: 1]                                   | 526  | Home Health Care[cite: 1]                        |
| 74   | Specialty Retail[cite: 1]                         | 527  | Medical Practitioners[cite: 1]                   |
| 75   | Wholesale[cite: 1]                                | 528  | Specialized Health Services[cite: 1]             |
| 76   | Diversified Services[cite: 1]                     | 610  | Aerospace/Defense - Major Diversified[cite: 1]   |
| 77   | Transportation[cite: 1]                           | 611  | Aerospace/Defense - Products & Services[cite: 1] |
| 81   | Computer Hardware[cite: 1]                        | 620  | Farm & Construction Machinery[cite: 1]           |
| 82   | Computer Software & Services[cite: 1]             | 621  | Industrial Equipment & Components[cite: 1]       |
| 83   | Electronics[cite: 1]                              | 622  | Diversified Machinery[cite: 1]                   |
| 84   | Telecommunications[cite: 1]                       | 623  | Pollution and Treatment Controls[cite: 1]        |
| 85   | Internet[cite: 1]                                 | 624  | Machine Tools & Accessories[cite: 1]             |
| 91   | Utilities[cite: 1]                                | 625  | Small Tools & Accessories[cite: 1]               |
| 110  | Chemicals - Major Diversified[cite: 1]            | 626  | Metals Fabrication[cite: 1]                      |
| 111  | Synthetics[cite: 1]                               | 627  | Industrial Electrical Equipment[cite: 1]         |
| 112  | Agricultural Chemicals[cite: 1]                   | 628  | Textile Manufacturing[cite: 1]                   |
| 113  | Specialty Chemicals[cite: 1]                      | 630  | Residential Construction[cite: 1]                |
| 120  | Major Integrated Oil & Gas[cite: 1]               | 631  | Manufactured Housing[cite: 1]                    |
| 121  | Independent Oil & Gas[cite: 1]                    | 632  | Lumber, Wood Production[cite: 1]                 |
| 122  | Oil & Gas Refining & Marketing[cite: 1]           | 633  | Cement[cite: 1]                                  |
| 123  | Oil & Gas Drilling and Exploration[cite: 1]       | 634  | General Building Materials[cite: 1]              |
| 124  | Oil & Gas Equipment & Services[cite: 1]           | 635  | Heavy Construction[cite: 1]                      |
| 125  | Oil & Gas Pipelines[cite: 1]                      | 636  | General Contractors[cite: 1]                     |
| 130  | Steel & Iron[cite: 1]                             | 637  | Waste Management[cite: 1]                        |
| 131  | Copper[cite: 1]                                   | 710  | Lodging[cite: 1]                                 |
| 132  | Aluminum[cite: 1]                                 | 711  | Resorts & Casinos[cite: 1]                       |
| 133  | Industrial Metals & Minerals[cite: 1]             | 712  | Restaurants[cite: 1]                             |
| 134  | Gold[cite: 1]                                     | 713  | Specialty Eateries[cite: 1]                      |
| 135  | Silver[cite: 1]                                   | 714  | Gaming Activities[cite: 1]                       |
| 136  | Nonmetallic Mineral Mining[cite: 1]               | 715  | Sporting Activities[cite: 1]                     |
| 210  | Conglomerates[cite: 1]                            | 716  | General Entertainment[cite: 1]                   |
| 310  | Appliances[cite: 1]                               | 720  | Advertising Agencies[cite: 1]                    |
| 311  | Home Furnishings & Fixtures[cite: 1]              | 721  | Marketing Services[cite: 1]                      |
| 312  | Housewares & Accessories[cite: 1]                 | 722  | Entertainment - Diversified[cite: 1]             |
| 313  | Business Equipment[cite: 1]                       | 723  | Broadcasting - TV[cite: 1]                       |
| 314  | Electronic Equipment[cite: 1]                     | 724  | Broadcasting - Radio[cite: 1]                    |
| 315  | Toys & Games[cite: 1]                             | 725  | CATV Systems[cite: 1]                            |
| 316  | Sporting Goods[cite: 1]                           | 726  | Movie Production, Theaters[cite: 1]              |
| 317  | Recreational Goods, Other[cite: 1]                | 727  | Publishing - Newspapers[cite: 1]                 |
| 318  | Photographic Equipment & Supplies[cite: 1]        | 728  | Publishing - Periodicals[cite: 1]                |
| 320  | Textile Apparel Clothing[cite: 1]                 | 729  | Publishing - Books[cite: 1]                      |
| 321  | Textile - Apparel Footwear & Accessories[cite: 1] | 730  | Apparel Stores[cite: 1]                          |
| 322  | Rubber & Plastics[cite: 1]                        | 731  | Department Stores[cite: 1]                       |
| 323  | Personal Products[cite: 1]                        | 732  | Discount, Variety Stores[cite: 1]                |
| 324  | Paper & Paper Products[cite: 1]                   | 733  | Drug Stores[cite: 1]                             |
| 325  | Packaging & Containers[cite: 1]                   | 734  | Grocery Stores[cite: 1]                          |
| 326  | Cleaning Products[cite: 1]                        | 735  | Electronics Stores[cite: 1]                      |
| 327  | Office Supplies[cite: 1]                          | 736  | Home Improvement Stores[cite: 1]                 |
| 330  | Auto Manufacturers - Major[cite: 1]               | 737  | Home Furnishing Stores[cite: 1]                  |
| 331  | Trucks & Other Vehicles[cite: 1]                  | 738  | Auto Parts Stores[cite: 1]                       |
| 332  | Recreational Vehicles[cite: 1]                    | 739  | Catalog & Mail Order Houses[cite: 1]             |
| 333  | Auto Parts[cite: 1]                               | 740  | Sporting Goods Stores[cite: 1]                   |
| 340  | Food - Major Diversified[cite: 1]                 | 741  | Toy & Hobby Stores[cite: 1]                      |
| 341  | Farm Products[cite: 1]                            | 742  | Jewelry Stores[cite: 1]                          |
| 342  | Processed & Packaged Goods[cite: 1]               | 743  | Music & Video Stores[cite: 1]                    |
| 343  | Meat Products[cite: 1]                            | 744  | Auto Dealerships[cite: 1]                        |
| 344  | Dairy Products[cite: 1]                           | 745  | Specialty Retail, Other[cite: 1]                 |
| 345  | Confectioners[cite: 1]                            | 750  | Auto Parts Wholesale[cite: 1]                    |
| 346  | Beverages - Brewers[cite: 1]                      | 751  | Building Materials Wholesale[cite: 1]            |
| 347  | Beverages - Wineries & Distillers[cite: 1]        | 752  | Industrial Equipment Wholesale[cite: 1]          |
| 348  | Beverages - Soft Drinks[cite: 1]                  | 753  | Electronics Wholesale[cite: 1]                   |
| 350  | Cigarettes[cite: 1]                               | 754  | Medical Equipment Wholesale[cite: 1]             |
| 351  | Tobacco Products, Other[cite: 1]                  | 755  | Computers Wholesale[cite: 1]                     |
| 410  | Money Center Banks[cite: 1]                       | 756  | Drugs Wholesale[cite: 1]                         |
| 411  | Regional - Northeast Banks[cite: 1]               | 757  | Food Wholesale[cite: 1]                          |
| 412  | Regional - Mid-Atlantic Banks[cite: 1]            | 758  | Basic Materials Wholesale[cite: 1]               |
| 413  | Regional - Southeast Banks[cite: 1]               | 759  | Wholesale, Other[cite: 1]                        |
| 414  | Regional - Midwest Banks[cite: 1]                 | 760  | Business Services[cite: 1]                       |
| 415  | Regional - Southwest Banks[cite: 1]               | 761  | Rental & Leasing Services[cite: 1]               |
| 416  | Regional - Pacific Banks[cite: 1]                 | 762  | Personal Services[cite: 1]                       |
| 417  | Foreign Money Center Banks[cite: 1]               | 763  | Consumer Services[cite: 1]                       |
| 418  | Foreign Regional Banks[cite: 1]                   | 764  | Staffing & Outsourcing Services[cite: 1]         |
| 419  | Savings & Loans[cite: 1]                          | 765  | Security & Protection Services[cite: 1]          |
| 420  | Investment Brokerage - National[cite: 1]          | 766  | Education & Training Services[cite: 1]           |
| 421  | Investment Brokerage - Regional[cite: 1]          | 767  | Technical Services[cite: 1]                      |
| 422  | Asset Management[cite: 1]                         | 768  | Research Services[cite: 1]                       |
| 423  | Diversified Investments[cite: 1]                  | 769  | Management Services[cite: 1]                     |
| 424  | Credit Services[cite: 1]                          | 770  | Major Airlines[cite: 1]                          |
| 425  | Closed-End Fund - Debt[cite: 1]                   | 771  | Regional Airlines[cite: 1]                       |
| 426  | Closed-End Fund - Equity[cite: 1]                 | 772  | Air Services, Other[cite: 1]                     |
| 773  | Air Delivery & Freight Services[cite: 1]          | 830  | Semiconductor - Broad Line[cite: 1]              |
| 774  | Trucking[cite: 1]                                 | 831  | Semiconductor - Memory Chips[cite: 1]            |
| 775  | Shipping[cite: 1]                                 | 832  | Semiconductor - Specialized[cite: 1]             |
| 776  | Railroads[cite: 1]                                | 833  | Semiconductor - Integrated Circuits[cite: 1]     |
| 810  | Diversified Computer Systems[cite: 1]             | 834  | Semiconductor Equipment & Materials[cite: 1]     |
| 811  | Personal Computers[cite: 1]                       | 835  | Printed Circuit Boards[cite: 1]                  |
| 812  | Computer Based Systems[cite: 1]                   | 836  | Diversified Electronics[cite: 1]                 |
| 813  | Data Storage Devices[cite: 1]                     | 837  | Scientific & Technical Instruments[cite: 1]      |
| 814  | Networking & Communication Devices[cite: 1]       | 840  | Wireless Communications[cite: 1]                 |
| 815  | Computer Peripherals[cite: 1]                     | 841  | Communication Equipment[cite: 1]                 |
| 820  | Multimedia & Graphics Software[cite: 1]           | 842  | Processing Systems & Products[cite: 1]           |
| 821  | Application Software[cite: 1]                     | 843  | Long Distance Carriers[cite: 1]                  |
| 822  | Technical & System Software[cite: 1]              | 844  | Telecom Services - Domestic[cite: 1]             |
| 823  | Security Software & Services[cite: 1]             | 845  | Telecom Services - Foreign[cite: 1]              |
| 824  | Information Technology Services[cite: 1]          | 846  | Diversified Communication Services[cite: 1]      |
| 825  | Healthcare Information Services[cite: 1]          | 850  | Internet Service Providers[cite: 1]              |
| 826  | Business Software & Services[cite: 1]             | 851  | Internet Information Providers[cite: 1]          |
| 827  | Information & Delivery Services[cite: 1]          | 852  | Internet Software & Services[cite: 1]            |
| 910  | Foreign Utilities[cite: 1]                        | 913  | Diversified Utilities[cite: 1]                   |
| 911  | Electric Utilities[cite: 1]                       | 914  | Water Utilities[cite: 1]                         |
| 912  | Gas Utilities[cite: 1]                            |      |                                                  |