# UpdateHrisGroupRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `hris_group`                                         | [shared.HrisGroup](../../models/shared/hrisgroup.md) | :heavy_check_mark:                                   | N/A                                                  |
| `connection_id`                                      | *str*                                                | :heavy_check_mark:                                   | ID of the connection                                 |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | ID of the Group                                      |
| `fields`                                             | List[*str*]                                          | :heavy_minus_sign:                                   | Comma-delimited fields to return                     |