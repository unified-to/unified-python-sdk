# CommerceItemVariant


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `available_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_minus_sign:                                                           | N/A                                                                          |
| `description`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `height`                                                                     | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | N/A                                                                          |
| `id`                                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `inventory_id`                                                               | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `is_active`                                                                  | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `is_featured`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `is_visible`                                                                 | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `length`                                                                     | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | N/A                                                                          |
| `media`                                                                      | List[[shared.CommerceItemMedia](../../models/shared/commerceitemmedia.md)]   | :heavy_minus_sign:                                                           | N/A                                                                          |
| `options`                                                                    | List[[shared.CommerceItemOption](../../models/shared/commerceitemoption.md)] | :heavy_minus_sign:                                                           | N/A                                                                          |
| `prices`                                                                     | List[[shared.CommerceItemPrice](../../models/shared/commerceitemprice.md)]   | :heavy_minus_sign:                                                           | N/A                                                                          |
| `public_description`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `public_name`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `requires_shipping`                                                          | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `size_unit`                                                                  | [Optional[shared.SizeUnit]](../../models/shared/sizeunit.md)                 | :heavy_minus_sign:                                                           | N/A                                                                          |
| `sku`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `tags`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `total_stock`                                                                | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | N/A                                                                          |
| `weight`                                                                     | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | N/A                                                                          |
| `weight_unit`                                                                | [Optional[shared.WeightUnit]](../../models/shared/weightunit.md)             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `width`                                                                      | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | N/A                                                                          |