# CreateScimUsersRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `connection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the connection                                         |
| `scim_user`                                                  | [Optional[shared.ScimUser]](../../models/shared/scimuser.md) | :heavy_minus_sign:                                           | N/A                                                          |
| `count`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | N/A                                                          |
| `filter_`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `sort_by`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `sort_order`                                                 | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `start_index`                                                | *Optional[float]*                                            | :heavy_minus_sign:                                           | N/A                                                          |