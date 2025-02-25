# PatchKmsCommentRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `kms_comment`                                          | [shared.KmsComment](../../models/shared/kmscomment.md) | :heavy_check_mark:                                     | N/A                                                    |
| `connection_id`                                        | *str*                                                  | :heavy_check_mark:                                     | ID of the connection                                   |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | ID of the Comment                                      |
| `fields`                                               | List[*str*]                                            | :heavy_minus_sign:                                     | Comma-delimited fields to return                       |