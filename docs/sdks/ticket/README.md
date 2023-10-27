# Ticket
(*ticket*)

### Available Operations

* [create_ticketing_ticket](#create_ticketing_ticket) - Create a ticket
* [get_ticketing_ticket](#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_tickets](#list_ticketing_tickets) - List all tickets
* [patch_ticketing_ticket](#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_ticket](#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_ticket](#update_ticketing_ticket) - Update a ticket

## create_ticketing_ticket

Create a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateTicketingTicketRequest(
    ticketing_ticket=shared.TicketingTicket(
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
)

res = s.ticket.create_ticketing_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateTicketingTicketRequest](../../models/operations/createticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateTicketingTicketResponse](../../models/operations/createticketingticketresponse.md)**


## get_ticketing_ticket

Retrieve a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingTicketRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.ticket.get_ticketing_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetTicketingTicketRequest](../../models/operations/getticketingticketrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetTicketingTicketResponse](../../models/operations/getticketingticketresponse.md)**


## list_ticketing_tickets

List all tickets

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListTicketingTicketsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.ticket.list_ticketing_tickets(req)

if res.ticketing_tickets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListTicketingTicketsRequest](../../models/operations/listticketingticketsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ListTicketingTicketsResponse](../../models/operations/listticketingticketsresponse.md)**


## patch_ticketing_ticket

Update a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchTicketingTicketRequest(
    ticketing_ticket=shared.TicketingTicket(
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ticket.patch_ticketing_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchTicketingTicketRequest](../../models/operations/patchticketingticketrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PatchTicketingTicketResponse](../../models/operations/patchticketingticketresponse.md)**


## remove_ticketing_ticket

Remove a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveTicketingTicketRequest(
    connection_id='string',
    id='<ID>',
)

res = s.ticket.remove_ticketing_ticket(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveTicketingTicketRequest](../../models/operations/removeticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RemoveTicketingTicketResponse](../../models/operations/removeticketingticketresponse.md)**


## update_ticketing_ticket

Update a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.UpdateTicketingTicketRequest(
    ticketing_ticket=shared.TicketingTicket(
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ticket.update_ticketing_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateTicketingTicketRequest](../../models/operations/updateticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.UpdateTicketingTicketResponse](../../models/operations/updateticketingticketresponse.md)**

