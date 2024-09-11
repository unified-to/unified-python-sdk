# CreateHrisCompanyRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `hris_company`                                                     | [Optional[shared.HrisCompany]](../../models/shared/hriscompany.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |