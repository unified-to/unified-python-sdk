# PatchRepoBranchRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `connection_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | ID of the connection                                             |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | ID of the Branch                                                 |
| `repo_branch`                                                    | [Optional[shared.RepoBranch]](../../models/shared/repobranch.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `fields`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Comma-delimited fields to return                                 |