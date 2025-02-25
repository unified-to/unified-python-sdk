# UpdateCommerceCollectionRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `commerce_collection`                                                  | [shared.CommerceCollection](../../models/shared/commercecollection.md) | :heavy_check_mark:                                                     | A collection of items/products/services                                |
| `connection_id`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | ID of the connection                                                   |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | ID of the Collection                                                   |
| `fields`                                                               | List[*str*]                                                            | :heavy_minus_sign:                                                     | Comma-delimited fields to return                                       |