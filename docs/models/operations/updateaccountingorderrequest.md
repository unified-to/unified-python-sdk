# UpdateAccountingOrderRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `connection_id`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | ID of the connection                                                       |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | ID of the Order                                                            |
| `accounting_order`                                                         | [Optional[shared.AccountingOrder]](../../models/shared/accountingorder.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `fields`                                                                   | List[*str*]                                                                | :heavy_minus_sign:                                                         | Comma-delimited fields to return                                           |