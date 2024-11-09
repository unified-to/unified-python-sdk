# UpdateLmsStudentRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `connection_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | ID of the connection                                             |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | ID of the Student                                                |
| `lms_student`                                                    | [Optional[shared.LmsStudent]](../../models/shared/lmsstudent.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `fields`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Comma-delimited fields to return                                 |