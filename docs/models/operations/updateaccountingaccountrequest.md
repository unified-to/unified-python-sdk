# UpdateAccountingAccountRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `accounting_account`                                                 | [shared.AccountingAccount](../../models/shared/accountingaccount.md) | :heavy_check_mark:                                                   | Chart of accounts                                                    |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Account                                                    |