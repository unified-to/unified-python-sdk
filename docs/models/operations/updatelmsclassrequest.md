# UpdateLmsClassRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `lms_class`                                        | [shared.LmsClass](../../models/shared/lmsclass.md) | :heavy_check_mark:                                 | N/A                                                |
| `connection_id`                                    | *str*                                              | :heavy_check_mark:                                 | ID of the connection                               |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | ID of the Class                                    |
| `fields`                                           | List[*str*]                                        | :heavy_minus_sign:                                 | Comma-delimited fields to return                   |