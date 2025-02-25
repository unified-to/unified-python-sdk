# CreateHrisEmployeeRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `hris_employee`                                            | [shared.HrisEmployee](../../models/shared/hrisemployee.md) | :heavy_check_mark:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `fields`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |