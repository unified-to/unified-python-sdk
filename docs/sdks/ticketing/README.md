# Ticketing
(*ticketing*)

### Available Operations

* [delete_ticketing_connection_id_agent_id](#delete_ticketing_connection_id_agent_id) - Remove a agent
* [delete_ticketing_connection_id_customer_id](#delete_ticketing_connection_id_customer_id) - Remove a customer
* [delete_ticketing_connection_id_note_ticket_id_id](#delete_ticketing_connection_id_note_ticket_id_id) - Remove a note
* [delete_ticketing_connection_id_ticket_id](#delete_ticketing_connection_id_ticket_id) - Remove a ticket
* [get_ticketing_connection_id_agent](#get_ticketing_connection_id_agent) - List all agents
* [get_ticketing_connection_id_agent_id](#get_ticketing_connection_id_agent_id) - Retrieve a agent
* [get_ticketing_connection_id_customer](#get_ticketing_connection_id_customer) - List all customers
* [get_ticketing_connection_id_customer_id](#get_ticketing_connection_id_customer_id) - Retrieve a customer
* [get_ticketing_connection_id_note_ticket_id](#get_ticketing_connection_id_note_ticket_id) - List all notes
* [get_ticketing_connection_id_note_ticket_id_id](#get_ticketing_connection_id_note_ticket_id_id) - Retrieve a note
* [get_ticketing_connection_id_ticket](#get_ticketing_connection_id_ticket) - List all tickets
* [get_ticketing_connection_id_ticket_id](#get_ticketing_connection_id_ticket_id) - Retrieve a ticket
* [patch_ticketing_connection_id_agent_id](#patch_ticketing_connection_id_agent_id) - Update a agent
* [patch_ticketing_connection_id_customer_id](#patch_ticketing_connection_id_customer_id) - Update a customer
* [patch_ticketing_connection_id_note_ticket_id_id](#patch_ticketing_connection_id_note_ticket_id_id) - Update a note
* [patch_ticketing_connection_id_ticket_id](#patch_ticketing_connection_id_ticket_id) - Update a ticket
* [post_ticketing_connection_id_agent](#post_ticketing_connection_id_agent) - Create a agent
* [post_ticketing_connection_id_customer](#post_ticketing_connection_id_customer) - Create a customer
* [post_ticketing_connection_id_note_ticket_id](#post_ticketing_connection_id_note_ticket_id) - Create a note
* [post_ticketing_connection_id_ticket](#post_ticketing_connection_id_ticket) - Create a ticket
* [put_ticketing_connection_id_agent_id](#put_ticketing_connection_id_agent_id) - Update a agent
* [put_ticketing_connection_id_customer_id](#put_ticketing_connection_id_customer_id) - Update a customer
* [put_ticketing_connection_id_note_ticket_id_id](#put_ticketing_connection_id_note_ticket_id_id) - Update a note
* [put_ticketing_connection_id_ticket_id](#put_ticketing_connection_id_ticket_id) - Update a ticket

## delete_ticketing_connection_id_agent_id

Remove a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='navigate',
    id='<ID>',
)

res = s.ticketing.delete_ticketing_connection_id_agent_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.DeleteTicketingConnectionIDAgentIDRequest](../../models/operations/deleteticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.DeleteTicketingConnectionIDAgentIDResponse](../../models/operations/deleteticketingconnectionidagentidresponse.md)**


## delete_ticketing_connection_id_customer_id

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDCustomerIDRequest(
    connection_id='Electric Gloves pish',
    id='<ID>',
)

res = s.ticketing.delete_ticketing_connection_id_customer_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.DeleteTicketingConnectionIDCustomerIDRequest](../../models/operations/deleteticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.DeleteTicketingConnectionIDCustomerIDResponse](../../models/operations/deleteticketingconnectionidcustomeridresponse.md)**


## delete_ticketing_connection_id_note_ticket_id_id

Remove a note

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDNoteTicketIDIDRequest(
    connection_id='DRAM Liaison',
    id='<ID>',
    ticket_id='Tasty exploit',
)

res = s.ticketing.delete_ticketing_connection_id_note_ticket_id_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.DeleteTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/deleteticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.DeleteTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/deleteticketingconnectionidnoteticketididresponse.md)**


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

res = s.ticketing.delete_ticketing_connection_id_ticket_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTicketingConnectionIDTicketIDRequest](../../models/operations/deleteticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteTicketingConnectionIDTicketIDResponse](../../models/operations/deleteticketingconnectionidticketidresponse.md)**


## get_ticketing_connection_id_agent

List all agents

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

req = operations.GetTicketingConnectionIDAgentRequest(
    connection_id='East Steel Frozen',
    limit=8285.04,
    offset=5507.07,
    order='Korea West Ryan',
    query='invoice coulomb soluta',
    sort='adored',
    updated_gte=dateutil.parser.isoparse('2023-11-15T19:25:12.859Z'),
)

res = s.ticketing.get_ticketing_connection_id_agent(req)

if res.ticketing_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetTicketingConnectionIDAgentRequest](../../models/operations/getticketingconnectionidagentrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetTicketingConnectionIDAgentResponse](../../models/operations/getticketingconnectionidagentresponse.md)**


## get_ticketing_connection_id_agent_id

Retrieve a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDAgentIDRequest(
    connection_id='Hat gas Cisgender',
    id='<ID>',
)

res = s.ticketing.get_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetTicketingConnectionIDAgentIDRequest](../../models/operations/getticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetTicketingConnectionIDAgentIDResponse](../../models/operations/getticketingconnectionidagentidresponse.md)**


## get_ticketing_connection_id_customer

List all customers

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

req = operations.GetTicketingConnectionIDCustomerRequest(
    connection_id='SDD because Salad',
    limit=8049.62,
    offset=4323.42,
    order='override',
    query='Rolls 1080p',
    sort='quantifying Southeast Kansas',
    updated_gte=dateutil.parser.isoparse('2023-12-20T19:18:39.254Z'),
)

res = s.ticketing.get_ticketing_connection_id_customer(req)

if res.ticketing_customers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDCustomerRequest](../../models/operations/getticketingconnectionidcustomerrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTicketingConnectionIDCustomerResponse](../../models/operations/getticketingconnectionidcustomerresponse.md)**


## get_ticketing_connection_id_customer_id

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDCustomerIDRequest(
    connection_id='further Ebert',
    id='<ID>',
)

res = s.ticketing.get_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetTicketingConnectionIDCustomerIDRequest](../../models/operations/getticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetTicketingConnectionIDCustomerIDResponse](../../models/operations/getticketingconnectionidcustomeridresponse.md)**


## get_ticketing_connection_id_note_ticket_id

List all notes

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

req = operations.GetTicketingConnectionIDNoteTicketIDRequest(
    connection_id='Account revolutionary',
    limit=2310.88,
    offset=6688.82,
    order='AI',
    query='stanch Investor attitude',
    sort='Cotton',
    ticket_id='Handmade Kia',
    updated_gte=dateutil.parser.isoparse('2022-05-26T17:12:11.333Z'),
)

res = s.ticketing.get_ticketing_connection_id_note_ticket_id(req)

if res.ticketing_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetTicketingConnectionIDNoteTicketIDRequest](../../models/operations/getticketingconnectionidnoteticketidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetTicketingConnectionIDNoteTicketIDResponse](../../models/operations/getticketingconnectionidnoteticketidresponse.md)**


## get_ticketing_connection_id_note_ticket_id_id

Retrieve a note

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDNoteTicketIDIDRequest(
    connection_id='for',
    id='<ID>',
    ticket_id='female',
)

res = s.ticketing.get_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/getticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/getticketingconnectionidnoteticketididresponse.md)**


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

res = s.ticketing.get_ticketing_connection_id_ticket(req)

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

res = s.ticketing.get_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDTicketIDRequest](../../models/operations/getticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTicketingConnectionIDTicketIDResponse](../../models/operations/getticketingconnectionidticketidresponse.md)**


## patch_ticketing_connection_id_agent_id

Update a agent

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

req = operations.PatchTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-06-01T22:24:40.372Z'),
        emails=[
            shared.TicketingEmail(
                email='Antonette63@gmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='Hop',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='driver',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-07-09T08:35:36.354Z'),
    ),
    connection_id='Soft Diesel Springs',
    id='<ID>',
)

res = s.ticketing.patch_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PatchTicketingConnectionIDAgentIDRequest](../../models/operations/patchticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PatchTicketingConnectionIDAgentIDResponse](../../models/operations/patchticketingconnectionidagentidresponse.md)**


## patch_ticketing_connection_id_customer_id

Update a customer

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

req = operations.PatchTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2023-01-22T19:33:25.134Z'),
        emails=[
            shared.TicketingEmail(
                email='Ora.Labadie94@yahoo.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='sensitise whiteboard Smyrna',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Hialeah',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='connect',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2023-12-28T17:48:45.929Z'),
    ),
    connection_id='Tennessine',
    id='<ID>',
)

res = s.ticketing.patch_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PatchTicketingConnectionIDCustomerIDRequest](../../models/operations/patchticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PatchTicketingConnectionIDCustomerIDResponse](../../models/operations/patchticketingconnectionidcustomeridresponse.md)**


## patch_ticketing_connection_id_note_ticket_id_id

Update a note

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

req = operations.PatchTicketingConnectionIDNoteTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='compress Oganesson',
        created_at=dateutil.parser.isoparse('2022-02-16T08:13:19.991Z'),
        customer_id='demystify',
        description='Fundamental demand-driven workforce',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='Nissan',
    ),
    connection_id='Chicken',
    id='<ID>',
    ticket_id='frictionless convergence officia',
)

res = s.ticketing.patch_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PatchTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/patchticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.PatchTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/patchticketingconnectionidnoteticketididresponse.md)**


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

res = s.ticketing.patch_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchTicketingConnectionIDTicketIDRequest](../../models/operations/patchticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PatchTicketingConnectionIDTicketIDResponse](../../models/operations/patchticketingconnectionidticketidresponse.md)**


## post_ticketing_connection_id_agent

Create a agent

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

req = operations.PostTicketingConnectionIDAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-12-14T10:20:29.412Z'),
        emails=[
            shared.TicketingEmail(
                email='Eleazar_Beatty22@gmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='exploit our wireless',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='Korea wireless Ferrari',
                type=shared.TicketingTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-24T13:41:54.208Z'),
    ),
    connection_id='capacity copy Blues',
)

res = s.ticketing.post_ticketing_connection_id_agent(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostTicketingConnectionIDAgentRequest](../../models/operations/postticketingconnectionidagentrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostTicketingConnectionIDAgentResponse](../../models/operations/postticketingconnectionidagentresponse.md)**


## post_ticketing_connection_id_customer

Create a customer

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

req = operations.PostTicketingConnectionIDCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-05-23T15:06:12.012Z'),
        emails=[
            shared.TicketingEmail(
                email='Austin44@yahoo.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='<ID>',
        name='Configuration neural',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'engineer',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Gasoline North gorgeous',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-10-09T07:25:23.111Z'),
    ),
    connection_id='mole purple',
)

res = s.ticketing.post_ticketing_connection_id_customer(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PostTicketingConnectionIDCustomerRequest](../../models/operations/postticketingconnectionidcustomerrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PostTicketingConnectionIDCustomerResponse](../../models/operations/postticketingconnectionidcustomerresponse.md)**


## post_ticketing_connection_id_note_ticket_id

Create a note

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

req = operations.PostTicketingConnectionIDNoteTicketIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='Plantation blue',
        created_at=dateutil.parser.isoparse('2021-06-11T06:54:31.529Z'),
        customer_id='asymmetric',
        description='Expanded intermediate attitude',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='naturally',
    ),
    connection_id='Wagon Sulfur',
    ticket_id='digital',
)

res = s.ticketing.post_ticketing_connection_id_note_ticket_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostTicketingConnectionIDNoteTicketIDRequest](../../models/operations/postticketingconnectionidnoteticketidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PostTicketingConnectionIDNoteTicketIDResponse](../../models/operations/postticketingconnectionidnoteticketidresponse.md)**


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

res = s.ticketing.post_ticketing_connection_id_ticket(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostTicketingConnectionIDTicketRequest](../../models/operations/postticketingconnectionidticketrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PostTicketingConnectionIDTicketResponse](../../models/operations/postticketingconnectionidticketresponse.md)**


## put_ticketing_connection_id_agent_id

Update a agent

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

req = operations.PutTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-12-19T19:47:13.993Z'),
        emails=[
            shared.TicketingEmail(
                email='Augustus_Kessler34@hotmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='reintermediate impression Refined',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='asynchronous',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-04-29T18:13:42.824Z'),
    ),
    connection_id='synergistic Uzbekistan green',
    id='<ID>',
)

res = s.ticketing.put_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PutTicketingConnectionIDAgentIDRequest](../../models/operations/putticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PutTicketingConnectionIDAgentIDResponse](../../models/operations/putticketingconnectionidagentidresponse.md)**


## put_ticketing_connection_id_customer_id

Update a customer

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

req = operations.PutTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2021-04-21T09:25:32.395Z'),
        emails=[
            shared.TicketingEmail(
                email='Shawna42@hotmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='gray',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Associate',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Sausages ivory Small',
                type=shared.TicketingTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-09-01T05:56:15.314Z'),
    ),
    connection_id='mobile Cotton',
    id='<ID>',
)

res = s.ticketing.put_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PutTicketingConnectionIDCustomerIDRequest](../../models/operations/putticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PutTicketingConnectionIDCustomerIDResponse](../../models/operations/putticketingconnectionidcustomeridresponse.md)**


## put_ticketing_connection_id_note_ticket_id_id

Update a note

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

req = operations.PutTicketingConnectionIDNoteTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='SMTP Cis',
        created_at=dateutil.parser.isoparse('2022-07-27T18:14:06.584Z'),
        customer_id='Carolina',
        description='Integrated asymmetric strategy',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='Northeast Morocco supposing',
    ),
    connection_id='DNS Fermium',
    id='<ID>',
    ticket_id='Southwest round',
)

res = s.ticketing.put_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PutTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/putticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PutTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/putticketingconnectionidnoteticketididresponse.md)**


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

res = s.ticketing.put_ticketing_connection_id_ticket_id(req)

if res.ticketing_ticket is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTicketingConnectionIDTicketIDRequest](../../models/operations/putticketingconnectionidticketidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PutTicketingConnectionIDTicketIDResponse](../../models/operations/putticketingconnectionidticketidresponse.md)**

