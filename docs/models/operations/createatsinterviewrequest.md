# CreateAtsInterviewRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `ats_interview`                                                      | [Optional[shared.AtsInterview]](../../models/shared/atsinterview.md) | :heavy_minus_sign:                                                   | An interview between a candidate for a specific job                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `fields_`                                                            | list[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |