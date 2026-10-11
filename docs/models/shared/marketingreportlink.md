# MarketingReportLink


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `click_percentage`                                                   | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Percentage of total clicks                                           |
| `last_click_at`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Last click timestamp (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)        |
| `total_clicks`                                                       | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Total clicks on this link                                            |
| `unique_click_percentage`                                            | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Percentage of unique clicks                                          |
| `unique_clicks`                                                      | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Unique clicks on this link                                           |
| `url`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The URL                                                              |