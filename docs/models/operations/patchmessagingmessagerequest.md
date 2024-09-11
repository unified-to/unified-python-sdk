# PatchMessagingMessageRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `connection_id`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | ID of the connection                                                         |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | ID of the Message                                                            |
| `messaging_message`                                                          | [Optional[shared.MessagingMessage]](../../models/shared/messagingmessage.md) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `fields`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Comma-delimited fields to return                                             |