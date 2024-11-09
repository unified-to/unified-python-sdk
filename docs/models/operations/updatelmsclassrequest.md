# UpdateLmsClassRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `connection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the connection                                         |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | ID of the Class                                              |
| `lms_class`                                                  | [Optional[shared.LmsClass]](../../models/shared/lmsclass.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `fields`                                                     | List[*str*]                                                  | :heavy_minus_sign:                                           | Comma-delimited fields to return                             |