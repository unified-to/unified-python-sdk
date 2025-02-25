# UpdateTaskProjectRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `task_project`                                           | [shared.TaskProject](../../models/shared/taskproject.md) | :heavy_check_mark:                                       | N/A                                                      |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the Project                                        |
| `fields`                                                 | List[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |