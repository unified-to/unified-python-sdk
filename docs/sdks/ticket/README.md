# Ticket
(*ticket*)

### Available Operations

* [delete_ticketing_connection_id_ticket_id](#delete_ticketing_connection_id_ticket_id) - Remove a ticket
* [get_ticketing_connection_id_ticket](#get_ticketing_connection_id_ticket) - List all tickets
* [get_ticketing_connection_id_ticket_id](#get_ticketing_connection_id_ticket_id) - Retrieve a ticket
* [patch_ticketing_connection_id_ticket_id](#patch_ticketing_connection_id_ticket_id) - Update a ticket
* [post_ticketing_connection_id_ticket](#post_ticketing_connection_id_ticket) - Create a ticket
* [put_ticketing_connection_id_ticket_id](#put_ticketing_connection_id_ticket_id) - Update a ticket

## delete_ticketing_connection_id_ticket_id

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

req = operations.DeleteTicketingConnectionIDTicketIDRequest(
    connection_id='brownie azure payment',
    id='<ID>',
)

res = s.ticket.delete_ticketing_connection_id_ticket_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTicketingConnectionIDTicketIDRequest](../../models/operations/deleteticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteTicketingConnectionIDTicketIDResponse](../../models/operations/deleteticketingconnectionidticketidresponse.md)**


## get_ticketing_connection_id_ticket

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

req = operations.GetTicketingConnectionIDTicketRequest(
    agent_id='New',
    connection_id='hertz Savings Steel',
    customer_id='payment biopsy Kids',
    limit=7673.64,
    offset=5134.74,
    order='quantifying orange',
    query='male dynamic',
    sort='Sedan Tricycle Honda',
    updated_gte=dateutil.parser.isoparse('2022-08-06T21:30:52.879Z'),
)

res = s.ticket.get_ticketing_connection_id_ticket(req)

if res.ticketing_tickets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetTicketingConnectionIDTicketRequest](../../models/operations/getticketingconnectionidticketrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetTicketingConnectionIDTicketResponse](../../models/operations/getticketingconnectionidticketresponse.md)**


## get_ticketing_connection_id_ticket_id

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

req = operations.GetTicketingConnectionIDTicketIDRequest(
    connection_id='yellow',
    id='<ID>',
)

res = s.ticket.get_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDTicketIDRequest](../../models/operations/getticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTicketingConnectionIDTicketIDResponse](../../models/operations/getticketingconnectionidticketidresponse.md)**


## patch_ticketing_connection_id_ticket_id

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

req = operations.PatchTicketingConnectionIDTicketIDRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='Representative calculate',
        closed_at=dateutil.parser.isoparse('2023-12-03T14:58:54.732Z'),
        created_at=dateutil.parser.isoparse('2022-09-11T04:52:37.095Z'),
        customer_id='indigo extend given',
        description='Profound motivating utilisation',
        id='<ID>',
        priority='Hill Jazz',
        raw=shared.PropertyTicketingTicketRaw(),
        source='West Macedonia City',
        source_ref='orange West doubtfully',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='Pizza',
        tags=[
            'definition',
        ],
        updated_at=dateutil.parser.isoparse('2021-10-05T23:17:22.031Z'),
    ),
    connection_id='engage henry',
    id='<ID>',
)

res = s.ticket.patch_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchTicketingConnectionIDTicketIDRequest](../../models/operations/patchticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PatchTicketingConnectionIDTicketIDResponse](../../models/operations/patchticketingconnectionidticketidresponse.md)**


## post_ticketing_connection_id_ticket

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

req = operations.PostTicketingConnectionIDTicketRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='North',
        closed_at=dateutil.parser.isoparse('2021-08-03T02:12:35.164Z'),
        created_at=dateutil.parser.isoparse('2023-05-12T14:26:26.768Z'),
        customer_id='mull hierarchy',
        description='Triple-buffered solution-oriented info-mediaries',
        id='<ID>',
        priority='person Idaho',
        raw=shared.PropertyTicketingTicketRaw(),
        source='Convertible whenever feed',
        source_ref='solid Electric Bespoke',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='sint uplift',
        tags=[
            'Idaho',
        ],
        updated_at=dateutil.parser.isoparse('2022-06-24T01:04:15.890Z'),
    ),
    connection_id='Oriental outrage',
)

res = s.ticket.post_ticketing_connection_id_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostTicketingConnectionIDTicketRequest](../../models/operations/postticketingconnectionidticketrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PostTicketingConnectionIDTicketResponse](../../models/operations/postticketingconnectionidticketresponse.md)**


## put_ticketing_connection_id_ticket_id

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

req = operations.PutTicketingConnectionIDTicketIDRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='North Finland',
        closed_at=dateutil.parser.isoparse('2023-12-08T00:37:44.739Z'),
        created_at=dateutil.parser.isoparse('2023-04-01T07:24:49.830Z'),
        customer_id='Marketing',
        description='Future-proofed high-level system engine',
        id='<ID>',
        priority='drat knottily',
        raw=shared.PropertyTicketingTicketRaw(),
        source='Upgradable knuckle',
        source_ref='anenst',
        status=shared.TicketingTicketStatus.ACTIVE,
        subject='indexing Wooden Crew',
        tags=[
            'anti',
        ],
        updated_at=dateutil.parser.isoparse('2023-08-10T07:27:15.153Z'),
    ),
    connection_id='neural orchestrate',
    id='<ID>',
)

res = s.ticket.put_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTicketingConnectionIDTicketIDRequest](../../models/operations/putticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PutTicketingConnectionIDTicketIDResponse](../../models/operations/putticketingconnectionidticketidresponse.md)**

