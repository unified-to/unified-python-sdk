# PatchAccountingJournalRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `connection_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | ID of the connection                                                           |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | ID of the Journal                                                              |
| `accounting_journal`                                                           | [Optional[shared.AccountingJournal]](../../models/shared/accountingjournal.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `fields`                                                                       | List[*str*]                                                                    | :heavy_minus_sign:                                                             | Comma-delimited fields to return                                               |