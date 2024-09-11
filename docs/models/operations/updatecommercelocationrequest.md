# UpdateCommerceLocationRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `connection_id`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | ID of the connection                                                         |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | ID of the Location                                                           |
| `commerce_location`                                                          | [Optional[shared.CommerceLocation]](../../models/shared/commercelocation.md) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `fields`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Comma-delimited fields to return                                             |