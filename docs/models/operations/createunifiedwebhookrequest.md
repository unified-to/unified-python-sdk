# CreateUnifiedWebhookRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `webhook`                                                         | [Optional[shared.Webhook]](../../models/shared/webhook.md)        | :heavy_minus_sign:                                                | A webhook is used to POST new/updated information to your server. |
| `include_all`                                                     | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | When set, all of the existing data will sent back to your server. |