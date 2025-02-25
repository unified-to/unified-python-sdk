# UpdateRepoRepositoryRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `repo_repository`                                              | [shared.RepoRepository](../../models/shared/reporepository.md) | :heavy_check_mark:                                             | N/A                                                            |
| `connection_id`                                                | *str*                                                          | :heavy_check_mark:                                             | ID of the connection                                           |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | ID of the Repository                                           |
| `fields`                                                       | List[*str*]                                                    | :heavy_minus_sign:                                             | Comma-delimited fields to return                               |