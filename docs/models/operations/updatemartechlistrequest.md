# UpdateMartechListRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `marketing_list`                                             | [shared.MarketingList](../../models/shared/marketinglist.md) | :heavy_check_mark:                                           | Mailing List                                                 |
| `connection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the connection                                         |
| `fields`                                                     | List[*str*]                                                  | :heavy_minus_sign:                                           | Comma-delimited fields to return                             |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | ID of the List                                               |