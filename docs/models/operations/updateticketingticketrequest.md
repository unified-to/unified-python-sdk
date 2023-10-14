# UpdateTicketingTicketRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `ticketing_ticket`                                                         | [Optional[shared.TicketingTicket]](../../models/shared/ticketingticket.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `connection_id`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | ID of the connection                                                       |
| `fields_`                                                                  | list[*str*]                                                                | :heavy_minus_sign:                                                         | Comma-delimited fields to return                                           |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | ID of the Ticket                                                           |