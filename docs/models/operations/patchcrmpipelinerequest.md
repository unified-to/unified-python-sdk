# PatchCrmPipelineRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `crm_pipeline`                                                     | [Optional[shared.CrmPipeline]](../../models/shared/crmpipeline.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `fields_`                                                          | list[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the Pipeline                                                 |