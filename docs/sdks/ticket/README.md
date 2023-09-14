# ticket

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDTicketIDRequest(
    connection_id='vel',
    id='e8dbf812-f83b-41ca-aa9f-fc561929cca9',
)

res = s.ticket.delete_ticketing_connection_id_ticket_id(req, operations.DeleteTicketingConnectionIDTicketIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.DeleteTicketingConnectionIDTicketIDRequest](../../models/operations/deleteticketingconnectionidticketidrequest.md)   | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `security`                                                                                                                       | [operations.DeleteTicketingConnectionIDTicketIDSecurity](../../models/operations/deleteticketingconnectionidticketidsecurity.md) | :heavy_check_mark:                                                                                                               | The security requirements to use for the request.                                                                                |


### Response

**[operations.DeleteTicketingConnectionIDTicketIDResponse](../../models/operations/deleteticketingconnectionidticketidresponse.md)**


## get_ticketing_connection_id_ticket

List all tickets

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDTicketRequest(
    agent_id='nemo',
    connection_id='laboriosam',
    customer_id='eaque',
    limit=6814.58,
    offset=977.35,
    order='adipisci',
    query='occaecati',
    sort='exercitationem',
    updated_gte=dateutil.parser.isoparse('2022-11-09T17:01:20.907Z'),
)

res = s.ticket.get_ticketing_connection_id_ticket(req, operations.GetTicketingConnectionIDTicketSecurity(
    jwt="",
))

if res.ticketing_tickets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetTicketingConnectionIDTicketRequest](../../models/operations/getticketingconnectionidticketrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.GetTicketingConnectionIDTicketSecurity](../../models/operations/getticketingconnectionidticketsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.GetTicketingConnectionIDTicketResponse](../../models/operations/getticketingconnectionidticketresponse.md)**


## get_ticketing_connection_id_ticket_id

Retrieve a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDTicketIDRequest(
    connection_id='quas',
    id='da1d48e7-8e3c-4f8e-9143-da9308b27a08',
)

res = s.ticket.get_ticketing_connection_id_ticket_id(req, operations.GetTicketingConnectionIDTicketIDSecurity(
    jwt="",
))

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetTicketingConnectionIDTicketIDRequest](../../models/operations/getticketingconnectionidticketidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.GetTicketingConnectionIDTicketIDSecurity](../../models/operations/getticketingconnectionidticketidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.GetTicketingConnectionIDTicketIDResponse](../../models/operations/getticketingconnectionidticketidresponse.md)**


## patch_ticketing_connection_id_ticket_id

Update a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDTicketIDRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='animi',
        closed_at=dateutil.parser.isoparse('2022-06-11T08:56:14.494Z'),
        created_at=dateutil.parser.isoparse('2022-11-29T12:43:22.264Z'),
        customer_id='voluptatum',
        description='eius',
        id='439b3de8-756c-4cce-870c-d2147b6e6152',
        priority='placeat',
        raw=shared.PropertyTicketingTicketRaw(),
        source='voluptatibus',
        source_ref='ipsa',
        status=shared.TicketingTicketStatus.ACTIVE,
        subject='quibusdam',
        tags=[
            'doloremque',
        ],
        updated_at=dateutil.parser.isoparse('2021-05-28T17:29:45.347Z'),
    ),
    connection_id='eligendi',
    id='3a4b9a5b-f935-4dfe-974f-a4b1e9c097ed',
)

res = s.ticket.patch_ticketing_connection_id_ticket_id(req, operations.PatchTicketingConnectionIDTicketIDSecurity(
    jwt="",
))

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PatchTicketingConnectionIDTicketIDRequest](../../models/operations/patchticketingconnectionidticketidrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.PatchTicketingConnectionIDTicketIDSecurity](../../models/operations/patchticketingconnectionidticketidsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.PatchTicketingConnectionIDTicketIDResponse](../../models/operations/patchticketingconnectionidticketidresponse.md)**


## post_ticketing_connection_id_ticket

Create a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDTicketRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='animi',
        closed_at=dateutil.parser.isoparse('2022-11-09T20:11:20.304Z'),
        created_at=dateutil.parser.isoparse('2022-09-13T02:47:18.896Z'),
        customer_id='numquam',
        description='fugit',
        id='e1a9237e-9984-4c80-b479-e891923c18ca',
        priority='rem',
        raw=shared.PropertyTicketingTicketRaw(),
        source='facere',
        source_ref='vel',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='porro',
        tags=[
            'enim',
        ],
        updated_at=dateutil.parser.isoparse('2022-06-24T00:19:38.232Z'),
    ),
    connection_id='cupiditate',
)

res = s.ticket.post_ticketing_connection_id_ticket(req, operations.PostTicketingConnectionIDTicketSecurity(
    jwt="",
))

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PostTicketingConnectionIDTicketRequest](../../models/operations/postticketingconnectionidticketrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PostTicketingConnectionIDTicketSecurity](../../models/operations/postticketingconnectionidticketsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PostTicketingConnectionIDTicketResponse](../../models/operations/postticketingconnectionidticketresponse.md)**


## put_ticketing_connection_id_ticket_id

Update a ticket

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDTicketIDRequest(
    ticketing_ticket=shared.TicketingTicket(
        category='explicabo',
        closed_at=dateutil.parser.isoparse('2022-09-23T16:36:11.812Z'),
        created_at=dateutil.parser.isoparse('2021-01-13T15:10:22.653Z'),
        customer_id='consequuntur',
        description='doloremque',
        id='207e4fae-038c-4d7f-9bc2-cabaf7fc2ccb',
        priority='id',
        raw=shared.PropertyTicketingTicketRaw(),
        source='numquam',
        source_ref='libero',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='asperiores',
        tags=[
            'aperiam',
        ],
        updated_at=dateutil.parser.isoparse('2020-02-02T17:11:25.452Z'),
    ),
    connection_id='nisi',
    id='8eaedb2e-e70b-4e06-9fb3-6add704080e0',
)

res = s.ticket.put_ticketing_connection_id_ticket_id(req, operations.PutTicketingConnectionIDTicketIDSecurity(
    jwt="",
))

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PutTicketingConnectionIDTicketIDRequest](../../models/operations/putticketingconnectionidticketidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.PutTicketingConnectionIDTicketIDSecurity](../../models/operations/putticketingconnectionidticketidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.PutTicketingConnectionIDTicketIDResponse](../../models/operations/putticketingconnectionidticketidresponse.md)**

