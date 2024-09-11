# CreatePaymentPaymentRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `connection_id`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | ID of the connection                                                     |
| `payment_payment`                                                        | [Optional[shared.PaymentPayment]](../../models/shared/paymentpayment.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `fields`                                                                 | List[*str*]                                                              | :heavy_minus_sign:                                                       | Comma-delimited fields to return                                         |