# UpdateCrmPipelineRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `connection_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | ID of the connection                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | ID of the Pipeline                                                 |
| `crm_pipeline`                                                     | [Optional[shared.CrmPipeline]](../../models/shared/crmpipeline.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `fields`                                                           | List[*str*]                                                        | :heavy_minus_sign:                                                 | Comma-delimited fields to return                                   |