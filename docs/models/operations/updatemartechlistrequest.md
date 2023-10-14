# UpdateMartechListRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `marketing_list`                                                       | [Optional[shared.MarketingList]](../../models/shared/marketinglist.md) | :heavy_minus_sign:                                                     | Mailing List                                                           |
| `connection_id`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | ID of the connection                                                   |
| `fields_`                                                              | list[*str*]                                                            | :heavy_minus_sign:                                                     | Comma-delimited fields to return                                       |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | ID of the List                                                         |