# CreateUnifiedWebhookRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `webhook`                                                  | [Optional[shared.Webhook]](../../models/shared/webhook.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `events`                                                   | List[[Events](../../models/operations/events.md)]          | :heavy_minus_sign:                                         | Which events to subscribe to.                              |
| `object`                                                   | *str*                                                      | :heavy_check_mark:                                         | The object to subscribe to                                 |