# UpdateAtsCandidateRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `ats_candidate`                                            | [shared.AtsCandidate](../../models/shared/atscandidate.md) | :heavy_check_mark:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | ID of the Candidate                                        |
| `fields`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |