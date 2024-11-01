# AccountingOrder


## Fields

| Field                                                                                                                    | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `account_id`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `billing_address`                                                                                                        | [Optional[shared.PropertyAccountingOrderBillingAddress]](../../models/shared/propertyaccountingorderbillingaddress.md)   | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `contact_id`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `created_at`                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                     | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `currency`                                                                                                               | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `id`                                                                                                                     | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `lineitems`                                                                                                              | List[[shared.AccountingLineitem](../../models/shared/accountinglineitem.md)]                                             | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `raw`                                                                                                                    | Dict[str, *Any*]                                                                                                         | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `shipping_address`                                                                                                       | [Optional[shared.PropertyAccountingOrderShippingAddress]](../../models/shared/propertyaccountingordershippingaddress.md) | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `status`                                                                                                                 | [Optional[shared.AccountingOrderStatus]](../../models/shared/accountingorderstatus.md)                                   | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `total_amount`                                                                                                           | *Optional[float]*                                                                                                        | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `type`                                                                                                                   | [Optional[shared.AccountingOrderType]](../../models/shared/accountingordertype.md)                                       | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `updated_at`                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                     | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |