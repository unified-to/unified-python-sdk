# PatchPaymentSubscriptionRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `payment_subscription`                                                   | [shared.PaymentSubscription](../../models/shared/paymentsubscription.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `connection_id`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | ID of the connection                                                     |
| `fields`                                                                 | List[*str*]                                                              | :heavy_minus_sign:                                                       | Comma-delimited fields to return                                         |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | ID of the Subscription                                                   |