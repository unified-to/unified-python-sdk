# PatchStorageFileRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `storage_file`                                           | [shared.StorageFile](../../models/shared/storagefile.md) | :heavy_check_mark:                                       | N/A                                                      |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the File                                           |
| `fields`                                                 | List[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |