# UpdateStorageFileRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the File                                                     |
| `storage_file`                                                     | [Optional[shared.StorageFile]](../../models/shared/storagefile.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |