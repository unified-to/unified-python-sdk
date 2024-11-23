# PatchCommerceMetadataRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `connection_id`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | ID of the connection                                                         |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | ID of the Metadata                                                           |
| `commerce_metadata`                                                          | [Optional[shared.CommerceMetadata]](../../models/shared/commercemetadata.md) | :heavy_minus_sign:                                                           | N/A                                                                          |
| `fields`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Comma-delimited fields to return                                             |