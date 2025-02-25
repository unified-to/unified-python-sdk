# UpdateLmsStudentRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `lms_student`                                          | [shared.LmsStudent](../../models/shared/lmsstudent.md) | :heavy_check_mark:                                     | N/A                                                    |
| `connection_id`                                        | *str*                                                  | :heavy_check_mark:                                     | ID of the connection                                   |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | ID of the Student                                      |
| `fields`                                               | List[*str*]                                            | :heavy_minus_sign:                                     | Comma-delimited fields to return                       |