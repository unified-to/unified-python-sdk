# CreateLmsCourseRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `connection_id`                                                | *str*                                                          | :heavy_check_mark:                                             | ID of the connection                                           |
| `lms_course`                                                   | [Optional[shared.LmsCourse]](../../models/shared/lmscourse.md) | :heavy_minus_sign:                                             | N/A                                                            |
| `fields`                                                       | List[*str*]                                                    | :heavy_minus_sign:                                             | Comma-delimited fields to return                               |