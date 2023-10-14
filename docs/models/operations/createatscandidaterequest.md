# CreateAtsCandidateRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `ats_candidate`                                                      | [Optional[shared.AtsCandidate]](../../models/shared/atscandidate.md) | :heavy_minus_sign:                                                   | A candidate looking for work                                         |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `fields_`                                                            | list[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |