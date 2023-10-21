# GetUnifiedIntegrationAuthRequest


## Fields

| Field                                                                                                                                                                                               | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `env`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `external_xref`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Your user identifier to associate with the new Integration                                                                                                                                          |
| `failure_redirect`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The URL where you want the user to be redirect to after an unsuccessful authentication. An "error" variable will be appended.                                                                       |
| `integration_type`                                                                                                                                                                                  | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | Type of the supported integration                                                                                                                                                                   |
| `lang`                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Language: en, fr, es, it, pt, zh, hi                                                                                                                                                                |
| `redirect`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `scopes`                                                                                                                                                                                            | List[[GetUnifiedIntegrationAuthScopes](../../models/operations/getunifiedintegrationauthscopes.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `state`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Extra state to send back to your success URL                                                                                                                                                        |
| `subdomain`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `success_redirect`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The URL where you want the user to be redirect to after a successful authentication.  The connection ID will be appended with (id=<connectionId>) to this URL, as will the state that was provided. |
| `workspace_id`                                                                                                                                                                                      | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | The ID of the workspace                                                                                                                                                                             |