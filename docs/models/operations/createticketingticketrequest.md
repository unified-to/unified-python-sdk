# CreateTicketingTicketRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `ticketing_ticket`                                               | [shared.TicketingTicket](../../models/shared/ticketingticket.md) | :heavy_check_mark:                                               | N/A                                                              |
| `connection_id`                                                  | *str*                                                            | :heavy_check_mark:                                               | ID of the connection                                             |
| `fields`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Comma-delimited fields to return                                 |