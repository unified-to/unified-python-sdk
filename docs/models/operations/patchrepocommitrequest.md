# PatchRepoCommitRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `repo_commit`                                          | [shared.RepoCommit](../../models/shared/repocommit.md) | :heavy_check_mark:                                     | N/A                                                    |
| `connection_id`                                        | *str*                                                  | :heavy_check_mark:                                     | ID of the connection                                   |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | ID of the Commit                                       |
| `fields`                                               | List[*str*]                                            | :heavy_minus_sign:                                     | Comma-delimited fields to return                       |