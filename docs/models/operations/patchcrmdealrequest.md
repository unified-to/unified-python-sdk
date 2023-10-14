# PatchCrmDealRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `crm_deal`                                                      | [Optional[shared.CrmDeal]](../../models/shared/crmdeal.md)      | :heavy_minus_sign:                                              | A deal represents an opportunity with companies and/or contacts |
| `connection_id`                                                 | *str*                                                           | :heavy_check_mark:                                              | ID of the connection                                            |
| `fields_`                                                       | list[*str*]                                                     | :heavy_minus_sign:                                              | Comma-delimited fields to return                                |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | ID of the Deal                                                  |