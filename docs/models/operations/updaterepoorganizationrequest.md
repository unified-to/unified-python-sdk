# UpdateRepoOrganizationRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `repo_organization`                                                | [shared.RepoOrganization](../../models/shared/repoorganization.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the Organization                                             |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |