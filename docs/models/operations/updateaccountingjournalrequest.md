# UpdateAccountingJournalRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `accounting_journal`                                                 | [shared.AccountingJournal](../../models/shared/accountingjournal.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Journal                                                    |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |