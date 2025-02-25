# UpdateAtsJobRequest


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `ats_job`                                      | [shared.AtsJob](../../models/shared/atsjob.md) | :heavy_check_mark:                             | N/A                                            |
| `connection_id`                                | *str*                                          | :heavy_check_mark:                             | ID of the connection                           |
| `id`                                           | *str*                                          | :heavy_check_mark:                             | ID of the Job                                  |
| `fields`                                       | List[*str*]                                    | :heavy_minus_sign:                             | Comma-delimited fields to return               |