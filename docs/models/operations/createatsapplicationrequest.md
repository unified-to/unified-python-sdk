# CreateAtsApplicationRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `connection_id`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | ID of the connection                                                     |
| `ats_application`                                                        | [Optional[shared.AtsApplication]](../../models/shared/atsapplication.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `fields`                                                                 | List[*str*]                                                              | :heavy_minus_sign:                                                       | Comma-delimited fields to return                                         |