# PropertyCrmEventMeeting

The meeting object, when type = meeting


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `description`                                                               | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The event meeting's agendadescription                                       |
| `end_at`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)        | :heavy_minus_sign:                                                          | The event meeting's end datetime (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format)   |
| `start_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)        | :heavy_minus_sign:                                                          | The event meeting's start datetime (ISO-8601 / YYYY-MM-DDTHH:MM:SSZ format) |
| `title`                                                                     | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The event meeting's topicsubject                                            |