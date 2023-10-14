# PatchAtsApplicationRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `ats_application`                                                        | [Optional[shared.AtsApplication]](../../models/shared/atsapplication.md) | :heavy_minus_sign:                                                       | An application is an association object between a candidate and a job    |
| `connection_id`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | ID of the connection                                                     |
| `fields_`                                                                | list[*str*]                                                              | :heavy_minus_sign:                                                       | Comma-delimited fields to return                                         |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | ID of the Application                                                    |