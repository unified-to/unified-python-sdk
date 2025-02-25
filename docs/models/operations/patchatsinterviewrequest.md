# PatchAtsInterviewRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `ats_interview`                                            | [shared.AtsInterview](../../models/shared/atsinterview.md) | :heavy_check_mark:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | ID of the Interview                                        |
| `fields`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |