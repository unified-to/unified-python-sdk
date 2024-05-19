# UpdateAccountingAccountRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `connection_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | ID of the connection                                                           |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | ID of the Account                                                              |
| `accounting_account`                                                           | [Optional[shared.AccountingAccount]](../../models/shared/accountingaccount.md) | :heavy_minus_sign:                                                             | Chart of accounts                                                              |