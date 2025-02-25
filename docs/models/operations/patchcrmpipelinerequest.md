# PatchCrmPipelineRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `crm_pipeline`                                           | [shared.CrmPipeline](../../models/shared/crmpipeline.md) | :heavy_check_mark:                                       | N/A                                                      |
| `connection_id`                                          | *str*                                                    | :heavy_check_mark:                                       | ID of the connection                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | ID of the Pipeline                                       |
| `fields`                                                 | List[*str*]                                              | :heavy_minus_sign:                                       | Comma-delimited fields to return                         |