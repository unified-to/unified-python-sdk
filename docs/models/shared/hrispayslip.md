# HrisPayslip


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `raw`                                                                      | Dict[str, *Any*]                                                           | :heavy_check_mark:                                                         | N/A                                                                        |
| `user_id`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `currency`                                                                 | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `details`                                                                  | List[[shared.HrisPayslipDetail](../../models/shared/hrispayslipdetail.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |
| `end_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `gross_amount`                                                             | *Optional[float]*                                                          | :heavy_minus_sign:                                                         | N/A                                                                        |
| `id`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `net_amount`                                                               | *Optional[float]*                                                          | :heavy_minus_sign:                                                         | N/A                                                                        |
| `paid_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `payment_type`                                                             | [Optional[shared.PaymentType]](../../models/shared/paymenttype.md)         | :heavy_minus_sign:                                                         | N/A                                                                        |
| `start_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `updated_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | N/A                                                                        |