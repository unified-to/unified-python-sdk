# PatchMartechMemberRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `marketing_member`                                               | [shared.MarketingMember](../../models/shared/marketingmember.md) | :heavy_check_mark:                                               | A member represents a person                                     |
| `connection_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | ID of the connection                                             |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | ID of the Member                                                 |
| `fields`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Comma-delimited fields to return                                 |