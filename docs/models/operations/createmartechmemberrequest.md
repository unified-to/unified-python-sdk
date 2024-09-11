# CreateMartechMemberRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `connection_id`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | ID of the connection                                                       |
| `marketing_member`                                                         | [Optional[shared.MarketingMember]](../../models/shared/marketingmember.md) | :heavy_minus_sign:                                                         | A member represents a person                                               |
| `fields`                                                                   | List[*str*]                                                                | :heavy_minus_sign:                                                         | Comma-delimited fields to return                                           |