# PatchTaskProjectRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the Project                                                  |
| `task_project`                                                     | [Optional[shared.TaskProject]](../../models/shared/taskproject.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |