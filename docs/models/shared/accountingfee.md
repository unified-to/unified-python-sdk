# AccountingFee


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `amount`                                                                 | *float*                                                                  | :heavy_check_mark:                                                       | N/A                                                                      |
| `currency`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | ISO 4217 currency code, e.g. USD                                         |
| `original_type`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The provider's original fee label, e.g. "VAT" or a shipping carrier name |
| `type`                                                                   | [shared.AccountingFeeType](../../models/shared/accountingfeetype.md)     | :heavy_check_mark:                                                       | Unified fee category                                                     |