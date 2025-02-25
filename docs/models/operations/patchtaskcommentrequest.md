# PatchTaskCommentRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `task_comment`                                           | [shared.TaskComment](../../models/shared/taskcomment.md) | :heavy_check_mark:                                       | N/A                                                      |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the Comment                                        |
| `fields`                                                 | List[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |