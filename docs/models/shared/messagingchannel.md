# MessagingChannel


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `name`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `created_at`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `description`                                                          | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `has_subchannels`                                                      | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `id`                                                                   | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `is_active`                                                            | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `is_private`                                                           | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `members`                                                              | List[[shared.MessagingMember](../../models/shared/messagingmember.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `parent_channel_id`                                                    | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `raw`                                                                  | Dict[str, *Any*]                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `updated_at`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `web_url`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |