# UpdateKmsSpaceRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `kms_space`                                        | [shared.KmsSpace](../../models/shared/kmsspace.md) | :heavy_check_mark:                                 | N/A                                                |
| `connection_id`                                    | *str*                                              | :heavy_check_mark:                                 | ID of the connection                               |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | ID of the Space                                    |
| `fields`                                           | List[*str*]                                        | :heavy_minus_sign:                                 | Comma-delimited fields to return                   |