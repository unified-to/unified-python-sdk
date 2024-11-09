# CreateRepoCommitRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `connection_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | ID of the connection                                             |
| `repo_commit`                                                    | [Optional[shared.RepoCommit]](../../models/shared/repocommit.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `fields`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Comma-delimited fields to return                                 |