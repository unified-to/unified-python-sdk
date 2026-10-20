# AdsPromoted

Promoted entity (e.g. page, app, product, tweet) for ads create


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `metadata`                                                       | List[[shared.AdsMetadata](../../models/shared/adsmetadata.md)]   | :heavy_minus_sign:                                               | N/A                                                              |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `raw`                                                            | Dict[str, *Any*]                                                 | :heavy_minus_sign:                                               | N/A                                                              |
| `type`                                                           | [shared.AdsPromotedType](../../models/shared/adspromotedtype.md) | :heavy_check_mark:                                               | Promoted entity types for ads_promoted list endpoint             |