# UpdateTicketingCustomerRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `ticketing_customer`                                                 | [shared.TicketingCustomer](../../models/shared/ticketingcustomer.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `connection_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | ID of the connection                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | ID of the Customer                                                   |
| `fields`                                                             | List[*str*]                                                          | :heavy_minus_sign:                                                   | Comma-delimited fields to return                                     |