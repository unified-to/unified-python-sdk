# UpdateCalendarEventRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `calendar_event`                                             | [shared.CalendarEvent](../../models/shared/calendarevent.md) | :heavy_check_mark:                                           | N/A                                                          |
| `connection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the connection                                         |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | ID of the Event                                              |
| `fields`                                                     | List[*str*]                                                  | :heavy_minus_sign:                                           | Comma-delimited fields to return                             |