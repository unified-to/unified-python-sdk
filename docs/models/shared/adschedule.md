# AdSchedule


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `bid_modifier`                                       | *Optional[float]*                                    | :heavy_minus_sign:                                   | 0.1-10.0                                             |
| `day_of_week`                                        | [shared.DayOfWeek](../../models/shared/dayofweek.md) | :heavy_check_mark:                                   | N/A                                                  |
| `end_hour`                                           | *float*                                              | :heavy_check_mark:                                   | 0-24 (24 = end of day)                               |
| `end_minute`                                         | *Optional[float]*                                    | :heavy_minus_sign:                                   | 0, 15, 30, 45                                        |
| `start_hour`                                         | *float*                                              | :heavy_check_mark:                                   | 0-23                                                 |
| `start_minute`                                       | *Optional[float]*                                    | :heavy_minus_sign:                                   | 0, 15, 30, 45                                        |