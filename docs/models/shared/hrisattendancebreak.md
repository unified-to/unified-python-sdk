# HrisAttendanceBreak


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `duration_minutes`                                                   | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |
| `end_at`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_paid`                                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | break type label, e.g. "Lunch"                                       |
| `start_at`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |