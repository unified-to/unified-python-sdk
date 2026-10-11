# UcRecordingTranscript


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `contact_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | (reference to UcContact)                                             |
| `end_at`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `start_at`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)                             |
| `text`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `user_id`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | reference to HrisEmployee (reference to HrisEmployee)                |