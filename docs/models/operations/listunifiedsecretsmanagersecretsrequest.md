# ListUnifiedSecretsmanagerSecretsRequest


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `limit`                                  | *Optional[float]*                        | :heavy_minus_sign:                       | Maximum number of secrets to return      |
| `offset`                                 | *Optional[float]*                        | :heavy_minus_sign:                       | Number of secrets to skip                |
| `query`                                  | *Optional[str]*                          | :heavy_minus_sign:                       | Filter secrets by name                   |
| `secretsmanager_id`                      | *str*                                    | :heavy_check_mark:                       | The secrets manager to list secrets from |