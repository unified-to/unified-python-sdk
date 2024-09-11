# CreateMartechListRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `connection_id`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | ID of the connection                                                   |
| `marketing_list`                                                       | [Optional[shared.MarketingList]](../../models/shared/marketinglist.md) | :heavy_minus_sign:                                                     | Mailing List                                                           |
| `fields`                                                               | List[*str*]                                                            | :heavy_minus_sign:                                                     | Comma-delimited fields to return                                       |