# Issue


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `created_at`                                             | *Optional[str]*                                          | :heavy_minus_sign:                                       | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                 |
| `customer_note`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `id`                                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `importance`                                             | *Optional[float]*                                        | :heavy_minus_sign:                                       | 1-5, 1 is lowest                                         |
| `resolution_time`                                        | *Optional[float]*                                        | :heavy_minus_sign:                                       | N/A                                                      |
| `size`                                                   | *Optional[float]*                                        | :heavy_minus_sign:                                       | 1-5, 1 is lowest                                         |
| `status`                                                 | [shared.IssueStatus](../../models/shared/issuestatus.md) | :heavy_check_mark:                                       | N/A                                                      |
| `ticket_ref`                                             | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `title`                                                  | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `type`                                                   | List[*str*]                                              | :heavy_minus_sign:                                       | N/A                                                      |
| `updated_at`                                             | *Optional[str]*                                          | :heavy_minus_sign:                                       | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                 |
| `url`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `workspace_id`                                           | *str*                                                    | :heavy_check_mark:                                       | (reference to KmsSpace)                                  |