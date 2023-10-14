# PatchCrmUserRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `crm_user`                                                 | [Optional[shared.CrmUser]](../../models/shared/crmuser.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `fields_`                                                  | list[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | ID of the User                                             |