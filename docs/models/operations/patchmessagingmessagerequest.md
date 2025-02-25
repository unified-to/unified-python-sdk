# PatchMessagingMessageRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `messaging_message`                                                | [shared.MessagingMessage](../../models/shared/messagingmessage.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the Message                                                  |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |