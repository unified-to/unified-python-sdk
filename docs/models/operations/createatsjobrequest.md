# CreateAtsJobRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `ats_job`                                                | [Optional[shared.AtsJob]](../../models/shared/atsjob.md) | :heavy_minus_sign:                                       | An opened position/job                                   |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `fields_`                                                | list[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |