# PatchCommerceItemRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `commerce_item`                                            | [shared.CommerceItem](../../models/shared/commerceitem.md) | :heavy_check_mark:                                         | N/A                                                        |
| `connection_id`                                            | *str*                                                      | :heavy_check_mark:                                         | ID of the connection                                       |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | ID of the Item                                             |
| `fields`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Comma-delimited fields to return                           |