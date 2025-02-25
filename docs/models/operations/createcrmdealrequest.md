# CreateCrmDealRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `crm_deal`                                                      | [shared.CrmDeal](../../models/shared/crmdeal.md)                | :heavy_check_mark:                                              | A deal represents an opportunity with companies and/or contacts |
| `connection_id`                                                 | *str*                                                           | :heavy_check_mark:                                              | ID of the connection                                            |
| `fields`                                                        | List[*str*]                                                     | :heavy_minus_sign:                                              | Comma-delimited fields to return                                |