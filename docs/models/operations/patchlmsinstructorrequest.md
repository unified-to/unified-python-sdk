# PatchLmsInstructorRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `lms_instructor`                                             | [shared.LmsInstructor](../../models/shared/lmsinstructor.md) | :heavy_check_mark:                                           | N/A                                                          |
| `connection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the connection                                         |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | ID of the Instructor                                         |
| `fields`                                                     | List[*str*]                                                  | :heavy_minus_sign:                                           | Comma-delimited fields to return                             |