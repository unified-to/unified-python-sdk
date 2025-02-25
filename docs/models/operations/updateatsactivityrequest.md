# UpdateAtsActivityRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `ats_activity`                                           | [shared.AtsActivity](../../models/shared/atsactivity.md) | :heavy_check_mark:                                       | N/A                                                      |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the Activity                                       |
| `fields`                                                 | List[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |