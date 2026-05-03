### Revision to Dividend Yield (Look-Ahead Bias)
**Case**: 

A special dividend is declared on T. On T+2, the exchange corrects the yield. How does the model prevent an algorithm simulating T+1 from seeing the T+2 correction?

**Adjustment**: 
See original example in [A. Bitemporal Data Model (`System_Time`)](../README.md#a-bitemporal-data-model-system_time)

### Mergers
**Case:**
Company A is acquired by Company B. How does the model ensure Company A's legacy orphaned options correctly price themselves using Company B's underlying price?

**Implementation**
- `Distribution` table adds new "Merger" event for Company A with `Link_Security_ID = CompanyB` 
- `Option_Price.Special_Settlement = 1` for Company A moving forward
- When querying for Company A, if `Option_Price.Special_Settlement = 1`, join in `Link_Security_ID` and get Company B's prices instead.

### Vendor pipeline failure
**Issue** 
The `Security_Price` data arrived, but `Option_price` data will be 4 hours delayed. How does downstream algorithms handle partial data?

**Adjustment** 
A separate pipeline table tracks the arrival of data and completeness. 

Downstream users can only query on rows where the ELT table assures that all data for that day is available. This can include a staging area for data to arrive and be verified before being written to the source tables.

**Example**

| Batch_ID | Table_Name       | Data_Date    | Status          | Record_Count | System_Time (UTC)     |
| -------- | ---------------- | ------------ | --------------- | ------------ | --------------------- |
| `1`      | `Security_Price` | `2023-08-11` | `COMMITTED`     | `10 245`     | `2023-08-11 18:10:00` |
| `2`      | `Option_Price`   | `2023-08-11` | `FAILED_NODATA` | `0`          | `2023-08-11 18:10:00` |
| `3`      | `Option_Price`   | `2023-08-11` | `COMMITTED`     | `1 503 405`  | `2023-08-11 22:30:00` |
