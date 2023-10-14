# CreateAtsScorecardRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `ats_scorecard`                                                      | [Optional[shared.AtsScorecard]](../../models/shared/atsscorecard.md) | :heavy_minus_sign:                                                   | A scorecard is feedback/assessment of a candidate's interview        |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `fields_`                                                            | list[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |