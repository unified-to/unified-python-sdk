# CreateAccountingAccountRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `connection_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | ID of the connection                                                           |
| `accounting_account`                                                           | [Optional[shared.AccountingAccount]](../../models/shared/accountingaccount.md) | :heavy_minus_sign:                                                             | Chart of accounts                                                              |
| `fields`                                                                       | List[*str*]                                                                    | :heavy_minus_sign:                                                             | Comma-delimited fields to return                                               |