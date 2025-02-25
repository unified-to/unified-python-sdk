# UpdateHrisLocationRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `hris_location`                                            | [shared.HrisLocation](../../models/shared/hrislocation.md) | :heavy_check_mark:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | ID of the Location                                         |
| `fields`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |