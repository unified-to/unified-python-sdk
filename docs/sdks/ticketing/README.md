# ticketing

### Available Operations

* [delete_ticketing_connection_id_agent_id](#delete_ticketing_connection_id_agent_id) - Remove a agent
* [delete_ticketing_connection_id_customer_id](#delete_ticketing_connection_id_customer_id) - Remove a customer
* [delete_ticketing_connection_id_notes_ticket_id_id](#delete_ticketing_connection_id_notes_ticket_id_id) - Remove a note
* [delete_ticketing_connection_id_ticket_id](#delete_ticketing_connection_id_ticket_id) - Remove a ticket
* [get_ticketing_connection_id_agent](#get_ticketing_connection_id_agent) - List all agents
* [get_ticketing_connection_id_agent_id](#get_ticketing_connection_id_agent_id) - Retrieve a agent
* [get_ticketing_connection_id_customer](#get_ticketing_connection_id_customer) - List all customers
* [get_ticketing_connection_id_customer_id](#get_ticketing_connection_id_customer_id) - Retrieve a customer
* [get_ticketing_connection_id_notes_ticket_id](#get_ticketing_connection_id_notes_ticket_id) - List all notes
* [get_ticketing_connection_id_notes_ticket_id_id](#get_ticketing_connection_id_notes_ticket_id_id) - Retrieve a note
* [get_ticketing_connection_id_ticket](#get_ticketing_connection_id_ticket) - List all tickets
* [get_ticketing_connection_id_ticket_id](#get_ticketing_connection_id_ticket_id) - Retrieve a ticket
* [patch_ticketing_connection_id_agent_id](#patch_ticketing_connection_id_agent_id) - Update a agent
* [patch_ticketing_connection_id_customer_id](#patch_ticketing_connection_id_customer_id) - Update a customer
* [patch_ticketing_connection_id_notes_ticket_id_id](#patch_ticketing_connection_id_notes_ticket_id_id) - Update a note
* [patch_ticketing_connection_id_ticket_id](#patch_ticketing_connection_id_ticket_id) - Update a ticket
* [post_ticketing_connection_id_agent](#post_ticketing_connection_id_agent) - Create a agent
* [post_ticketing_connection_id_customer](#post_ticketing_connection_id_customer) - Create a customer
* [post_ticketing_connection_id_notes_ticket_id](#post_ticketing_connection_id_notes_ticket_id) - Create a note
* [post_ticketing_connection_id_ticket](#post_ticketing_connection_id_ticket) - Create a ticket
* [put_ticketing_connection_id_agent_id](#put_ticketing_connection_id_agent_id) - Update a agent
* [put_ticketing_connection_id_customer_id](#put_ticketing_connection_id_customer_id) - Update a customer
* [put_ticketing_connection_id_notes_ticket_id_id](#put_ticketing_connection_id_notes_ticket_id_id) - Update a note
* [put_ticketing_connection_id_ticket_id](#put_ticketing_connection_id_ticket_id) - Update a ticket

## delete_ticketing_connection_id_agent_id

Remove a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='fuga',
    id='3fc73a5a-034b-4114-9924-3afa6987a472',
)

res = s.ticketing.delete_ticketing_connection_id_agent_id(req, operations.DeleteTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTicketingConnectionIDAgentIDRequest](../../models/operations/deleteticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.DeleteTicketingConnectionIDAgentIDSecurity](../../models/operations/deleteticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.DeleteTicketingConnectionIDAgentIDResponse](../../models/operations/deleteticketingconnectionidagentidresponse.md)**


## delete_ticketing_connection_id_customer_id

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDCustomerIDRequest(
    connection_id='libero',
    id='709a153e-2230-4106-8539-ce0932d10acd',
)

res = s.ticketing.delete_ticketing_connection_id_customer_id(req, operations.DeleteTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.DeleteTicketingConnectionIDCustomerIDRequest](../../models/operations/deleteticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.DeleteTicketingConnectionIDCustomerIDSecurity](../../models/operations/deleteticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.DeleteTicketingConnectionIDCustomerIDResponse](../../models/operations/deleteticketingconnectionidcustomeridresponse.md)**


## delete_ticketing_connection_id_notes_ticket_id_id

Remove a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDNotesTicketIDIDRequest(
    connection_id='vitae',
    id='5d8cc306-b786-4b3d-b7bd-204a1f340bb3',
    ticket_id='ex',
)

res = s.ticketing.delete_ticketing_connection_id_notes_ticket_id_id(req, operations.DeleteTicketingConnectionIDNotesTicketIDIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.DeleteTicketingConnectionIDNotesTicketIDIDRequest](../../models/operations/deleteticketingconnectionidnotesticketididrequest.md)   | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `security`                                                                                                                                     | [operations.DeleteTicketingConnectionIDNotesTicketIDIDSecurity](../../models/operations/deleteticketingconnectionidnotesticketididsecurity.md) | :heavy_check_mark:                                                                                                                             | The security requirements to use for the request.                                                                                              |


### Response

**[operations.DeleteTicketingConnectionIDNotesTicketIDIDResponse](../../models/operations/deleteticketingconnectionidnotesticketididresponse.md)**


## delete_ticketing_connection_id_ticket_id

Remove a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDTicketIDRequest(
    connection_id='voluptatibus',
    id='677a4851-9c33-4749-8284-8826bb03c7fd',
)

res = s.ticketing.delete_ticketing_connection_id_ticket_id(req, operations.DeleteTicketingConnectionIDTicketIDSecurity(
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


## get_ticketing_connection_id_agent

List all agents

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDAgentRequest(
    connection_id='consequuntur',
    limit=1427.69,
    offset=3147.32,
    order='debitis',
    query='dolore',
    sort='in',
    updated_gte=dateutil.parser.isoparse('2022-01-15T17:11:52.134Z'),
)

res = s.ticketing.get_ticketing_connection_id_agent(req, operations.GetTicketingConnectionIDAgentSecurity(
    jwt="",
))

if res.ticketing_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetTicketingConnectionIDAgentRequest](../../models/operations/getticketingconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetTicketingConnectionIDAgentSecurity](../../models/operations/getticketingconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetTicketingConnectionIDAgentResponse](../../models/operations/getticketingconnectionidagentresponse.md)**


## get_ticketing_connection_id_agent_id

Retrieve a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDAgentIDRequest(
    connection_id='architecto',
    id='a88ed72a-2d4a-4f41-98ac-2d0f0f58c3b8',
)

res = s.ticketing.get_ticketing_connection_id_agent_id(req, operations.GetTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDAgentIDRequest](../../models/operations/getticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.GetTicketingConnectionIDAgentIDSecurity](../../models/operations/getticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.GetTicketingConnectionIDAgentIDResponse](../../models/operations/getticketingconnectionidagentidresponse.md)**


## get_ticketing_connection_id_customer

List all customers

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDCustomerRequest(
    connection_id='in',
    limit=7360.32,
    offset=2850.04,
    order='molestiae',
    query='eaque',
    sort='tempora',
    updated_gte=dateutil.parser.isoparse('2022-03-06T22:27:54.190Z'),
)

res = s.ticketing.get_ticketing_connection_id_customer(req, operations.GetTicketingConnectionIDCustomerSecurity(
    jwt="",
))

if res.ticketing_customers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetTicketingConnectionIDCustomerRequest](../../models/operations/getticketingconnectionidcustomerrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.GetTicketingConnectionIDCustomerSecurity](../../models/operations/getticketingconnectionidcustomersecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.GetTicketingConnectionIDCustomerResponse](../../models/operations/getticketingconnectionidcustomerresponse.md)**


## get_ticketing_connection_id_customer_id

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDCustomerIDRequest(
    connection_id='aut',
    id='d98e9d82-c5e3-406f-9576-f5cdeb0286d0',
)

res = s.ticketing.get_ticketing_connection_id_customer_id(req, operations.GetTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetTicketingConnectionIDCustomerIDRequest](../../models/operations/getticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.GetTicketingConnectionIDCustomerIDSecurity](../../models/operations/getticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.GetTicketingConnectionIDCustomerIDResponse](../../models/operations/getticketingconnectionidcustomeridresponse.md)**


## get_ticketing_connection_id_notes_ticket_id

List all notes

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDNotesTicketIDRequest(
    connection_id='distinctio',
    limit=8031.14,
    offset=3028.92,
    order='adipisci',
    query='harum',
    sort='veritatis',
    ticket_id='quas',
    updated_gte=dateutil.parser.isoparse('2021-07-31T21:20:45.941Z'),
)

res = s.ticketing.get_ticketing_connection_id_notes_ticket_id(req, operations.GetTicketingConnectionIDNotesTicketIDSecurity(
    jwt="",
))

if res.ticketing_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetTicketingConnectionIDNotesTicketIDRequest](../../models/operations/getticketingconnectionidnotesticketidrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.GetTicketingConnectionIDNotesTicketIDSecurity](../../models/operations/getticketingconnectionidnotesticketidsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.GetTicketingConnectionIDNotesTicketIDResponse](../../models/operations/getticketingconnectionidnotesticketidresponse.md)**


## get_ticketing_connection_id_notes_ticket_id_id

Retrieve a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDNotesTicketIDIDRequest(
    connection_id='ipsum',
    id='78f2fcff-81dd-4f7e-888f-74ef54c9216e',
    ticket_id='atque',
)

res = s.ticketing.get_ticketing_connection_id_notes_ticket_id_id(req, operations.GetTicketingConnectionIDNotesTicketIDIDSecurity(
    jwt="",
))

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetTicketingConnectionIDNotesTicketIDIDRequest](../../models/operations/getticketingconnectionidnotesticketididrequest.md)   | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `security`                                                                                                                               | [operations.GetTicketingConnectionIDNotesTicketIDIDSecurity](../../models/operations/getticketingconnectionidnotesticketididsecurity.md) | :heavy_check_mark:                                                                                                                       | The security requirements to use for the request.                                                                                        |


### Response

**[operations.GetTicketingConnectionIDNotesTicketIDIDResponse](../../models/operations/getticketingconnectionidnotesticketididresponse.md)**


## get_ticketing_connection_id_ticket

List all tickets

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDTicketRequest(
    agent_id='unde',
    connection_id='qui',
    customer_id='aliquid',
    limit=1977.7,
    offset=641.35,
    order='velit',
    query='libero',
    sort='soluta',
    updated_gte=dateutil.parser.isoparse('2022-01-21T15:01:10.881Z'),
)

res = s.ticketing.get_ticketing_connection_id_ticket(req, operations.GetTicketingConnectionIDTicketSecurity(
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
    connection_id='quo',
    id='2c8d2701-096b-466a-96e3-e1d9d3b66033',
)

res = s.ticketing.get_ticketing_connection_id_ticket_id(req, operations.GetTicketingConnectionIDTicketIDSecurity(
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


## patch_ticketing_connection_id_agent_id

Update a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-05-08T09:12:54.892Z'),
        emails=[
            shared.TicketingEmail(
                email='Brad.Olson@gmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='5d2247de-9b3d-4461-b0e7-68a96bb39878',
        name='Jimmy Metz',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='tempore',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-15T11:30:38.762Z'),
    ),
    connection_id='cum',
    id='f7143356-f634-49a1-a424-9b211ce46b95',
)

res = s.ticketing.patch_ticketing_connection_id_agent_id(req, operations.PatchTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchTicketingConnectionIDAgentIDRequest](../../models/operations/patchticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PatchTicketingConnectionIDAgentIDSecurity](../../models/operations/patchticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PatchTicketingConnectionIDAgentIDResponse](../../models/operations/patchticketingconnectionidagentidresponse.md)**


## patch_ticketing_connection_id_customer_id

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-07-29T08:43:35.611Z'),
        emails=[
            shared.TicketingEmail(
                email='Brandi35@gmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='ca9142f0-5263-42b3-9cad-692ffc874500',
        name='Lorena Moore',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'temporibus',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='excepturi',
                type=shared.TicketingTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-02-14T22:17:14.340Z'),
    ),
    connection_id='aperiam',
    id='36f5c388-664f-4698-9530-a2e2aed6aaf8',
)

res = s.ticketing.patch_ticketing_connection_id_customer_id(req, operations.PatchTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PatchTicketingConnectionIDCustomerIDRequest](../../models/operations/patchticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.PatchTicketingConnectionIDCustomerIDSecurity](../../models/operations/patchticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.PatchTicketingConnectionIDCustomerIDResponse](../../models/operations/patchticketingconnectionidcustomeridresponse.md)**


## patch_ticketing_connection_id_notes_ticket_id_id

Update a note

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDNotesTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='ea',
        created_at=dateutil.parser.isoparse('2022-03-24T22:55:36.292Z'),
        customer_id='eos',
        description='praesentium',
        id='d040c69a-3d90-46f6-abd5-ad7ec7394f25',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='repellat',
    ),
    connection_id='ex',
    id='34b37307-14e6-4be8-83e0-9c64d342ac29',
    ticket_id='provident',
)

res = s.ticketing.patch_ticketing_connection_id_notes_ticket_id_id(req, operations.PatchTicketingConnectionIDNotesTicketIDIDSecurity(
    jwt="",
))

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PatchTicketingConnectionIDNotesTicketIDIDRequest](../../models/operations/patchticketingconnectionidnotesticketididrequest.md)   | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |
| `security`                                                                                                                                   | [operations.PatchTicketingConnectionIDNotesTicketIDIDSecurity](../../models/operations/patchticketingconnectionidnotesticketididsecurity.md) | :heavy_check_mark:                                                                                                                           | The security requirements to use for the request.                                                                                            |


### Response

**[operations.PatchTicketingConnectionIDNotesTicketIDIDResponse](../../models/operations/patchticketingconnectionidnotesticketididresponse.md)**


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
        category='officia',
        closed_at=dateutil.parser.isoparse('2022-01-28T05:10:10.473Z'),
        created_at=dateutil.parser.isoparse('2022-02-09T11:50:25.266Z'),
        customer_id='quam',
        description='dolorum',
        id='ef13402e-945f-4537-83ef-de1198221f9b',
        priority='inventore',
        raw=shared.PropertyTicketingTicketRaw(),
        source='tenetur',
        source_ref='nihil',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='iste',
        tags=[
            'deserunt',
        ],
        updated_at=dateutil.parser.isoparse('2020-02-21T15:04:19.759Z'),
    ),
    connection_id='repudiandae',
    id='69682ace-efb0-44f8-8512-caabea708ed5',
)

res = s.ticketing.patch_ticketing_connection_id_ticket_id(req, operations.PatchTicketingConnectionIDTicketIDSecurity(
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


## post_ticketing_connection_id_agent

Create a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-05-21T16:53:45.567Z'),
        emails=[
            shared.TicketingEmail(
                email='Raven.Frami@yahoo.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='460599d5-c334-4957-ad55-209e9a2253b6',
        name='Clinton Huel',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='laudantium',
                type=shared.TicketingTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2020-03-13T17:02:39.583Z'),
    ),
    connection_id='similique',
)

res = s.ticketing.post_ticketing_connection_id_agent(req, operations.PostTicketingConnectionIDAgentSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostTicketingConnectionIDAgentRequest](../../models/operations/postticketingconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.PostTicketingConnectionIDAgentSecurity](../../models/operations/postticketingconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostTicketingConnectionIDAgentResponse](../../models/operations/postticketingconnectionidagentresponse.md)**


## post_ticketing_connection_id_customer

Create a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2021-11-22T08:46:26.211Z'),
        emails=[
            shared.TicketingEmail(
                email='Sabina.Gulgowski59@hotmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='8a149067-8f13-4c68-ad83-9fc9e175ffa9',
        name='Ella Murazik',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'corporis',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='error',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-11-08T14:43:03.666Z'),
    ),
    connection_id='debitis',
)

res = s.ticketing.post_ticketing_connection_id_customer(req, operations.PostTicketingConnectionIDCustomerSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PostTicketingConnectionIDCustomerRequest](../../models/operations/postticketingconnectionidcustomerrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PostTicketingConnectionIDCustomerSecurity](../../models/operations/postticketingconnectionidcustomersecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PostTicketingConnectionIDCustomerResponse](../../models/operations/postticketingconnectionidcustomerresponse.md)**


## post_ticketing_connection_id_notes_ticket_id

Create a note

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDNotesTicketIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='quidem',
        created_at=dateutil.parser.isoparse('2022-07-05T14:59:15.588Z'),
        customer_id='magnam',
        description='vel',
        id='030fe183-76c2-4bed-ae76-790ed0c16a7b',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='id',
    ),
    connection_id='dolore',
    ticket_id='quam',
)

res = s.ticketing.post_ticketing_connection_id_notes_ticket_id(req, operations.PostTicketingConnectionIDNotesTicketIDSecurity(
    jwt="",
))

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.PostTicketingConnectionIDNotesTicketIDRequest](../../models/operations/postticketingconnectionidnotesticketidrequest.md)   | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `security`                                                                                                                             | [operations.PostTicketingConnectionIDNotesTicketIDSecurity](../../models/operations/postticketingconnectionidnotesticketidsecurity.md) | :heavy_check_mark:                                                                                                                     | The security requirements to use for the request.                                                                                      |


### Response

**[operations.PostTicketingConnectionIDNotesTicketIDResponse](../../models/operations/postticketingconnectionidnotesticketidresponse.md)**


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
        category='rem',
        closed_at=dateutil.parser.isoparse('2022-12-31T16:32:53.167Z'),
        created_at=dateutil.parser.isoparse('2022-09-20T04:19:27.059Z'),
        customer_id='totam',
        description='unde',
        id='f6770ef0-4809-41a2-ba25-ee6c75af8a60',
        priority='laborum',
        raw=shared.PropertyTicketingTicketRaw(),
        source='quam',
        source_ref='laborum',
        status=shared.TicketingTicketStatus.CLOSED,
        subject='dolor',
        tags=[
            'dolore',
        ],
        updated_at=dateutil.parser.isoparse('2022-01-27T16:39:01.281Z'),
    ),
    connection_id='perferendis',
)

res = s.ticketing.post_ticketing_connection_id_ticket(req, operations.PostTicketingConnectionIDTicketSecurity(
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


## put_ticketing_connection_id_agent_id

Update a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-02-01T01:30:25.348Z'),
        emails=[
            shared.TicketingEmail(
                email='Sigrid_Hilll@yahoo.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='60acaca6-45de-4986-b551-a9cce61ec2c7',
        name='Gerard Feest',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='officiis',
                type=shared.TicketingTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-05-28T17:33:55.487Z'),
    ),
    connection_id='assumenda',
    id='5a65b4d5-562d-49b7-99e2-d6fcf557629d',
)

res = s.ticketing.put_ticketing_connection_id_agent_id(req, operations.PutTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTicketingConnectionIDAgentIDRequest](../../models/operations/putticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PutTicketingConnectionIDAgentIDSecurity](../../models/operations/putticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PutTicketingConnectionIDAgentIDResponse](../../models/operations/putticketingconnectionidagentidresponse.md)**


## put_ticketing_connection_id_customer_id

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2021-11-27T14:28:08.554Z'),
        emails=[
            shared.TicketingEmail(
                email='Enola63@yahoo.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='90282a51-f41c-4f67-96ed-3d724c18f581',
        name='Terrence Langworth',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'officiis',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='consectetur',
                type=shared.TicketingTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-11-17T00:52:06.013Z'),
    ),
    connection_id='autem',
    id='600da0e3-aa61-4c6f-a09d-852b53b32c8c',
)

res = s.ticketing.put_ticketing_connection_id_customer_id(req, operations.PutTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PutTicketingConnectionIDCustomerIDRequest](../../models/operations/putticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.PutTicketingConnectionIDCustomerIDSecurity](../../models/operations/putticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.PutTicketingConnectionIDCustomerIDResponse](../../models/operations/putticketingconnectionidcustomeridresponse.md)**


## put_ticketing_connection_id_notes_ticket_id_id

Update a note

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDNotesTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='dignissimos',
        created_at=dateutil.parser.isoparse('2022-06-05T09:20:14.169Z'),
        customer_id='eligendi',
        description='esse',
        id='10e1673d-905c-4b4b-adef-3c127c390995',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='veniam',
    ),
    connection_id='consequuntur',
    id='8250dcbb-cd3b-4121-b88c-1ee5e7a06139',
    ticket_id='quasi',
)

res = s.ticketing.put_ticketing_connection_id_notes_ticket_id_id(req, operations.PutTicketingConnectionIDNotesTicketIDIDSecurity(
    jwt="",
))

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PutTicketingConnectionIDNotesTicketIDIDRequest](../../models/operations/putticketingconnectionidnotesticketididrequest.md)   | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `security`                                                                                                                               | [operations.PutTicketingConnectionIDNotesTicketIDIDSecurity](../../models/operations/putticketingconnectionidnotesticketididsecurity.md) | :heavy_check_mark:                                                                                                                       | The security requirements to use for the request.                                                                                        |


### Response

**[operations.PutTicketingConnectionIDNotesTicketIDIDResponse](../../models/operations/putticketingconnectionidnotesticketididresponse.md)**


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
        category='placeat',
        closed_at=dateutil.parser.isoparse('2021-06-17T09:59:15.139Z'),
        created_at=dateutil.parser.isoparse('2021-01-22T11:03:32.954Z'),
        customer_id='aut',
        description='soluta',
        id='7d176492-6b0c-4f5e-acb6-ebabe5e0b99f',
        priority='velit',
        raw=shared.PropertyTicketingTicketRaw(),
        source='nobis',
        source_ref='illo',
        status=shared.TicketingTicketStatus.ACTIVE,
        subject='enim',
        tags=[
            'quas',
        ],
        updated_at=dateutil.parser.isoparse('2021-10-30T17:09:24.055Z'),
    ),
    connection_id='deserunt',
    id='87bb7aec-be56-49d7-8cb0-69907f989441',
)

res = s.ticketing.put_ticketing_connection_id_ticket_id(req, operations.PutTicketingConnectionIDTicketIDSecurity(
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

