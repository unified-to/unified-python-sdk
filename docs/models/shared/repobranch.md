# RepoBranch


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `metadata`                                                           | List[[shared.RepoMetadata](../../models/shared/repometadata.md)]     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `raw`                                                                | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `repo_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | (reference to RepoRepository)                                        |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |