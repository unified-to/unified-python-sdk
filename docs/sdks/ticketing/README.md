# Ticketing
(*ticketing*)

### Available Operations

* [create_ticketing_agent](#create_ticketing_agent) - Create a agent
* [create_ticketing_customer](#create_ticketing_customer) - Create a customer
* [create_ticketing_note](#create_ticketing_note) - Create a note
* [create_ticketing_ticket](#create_ticketing_ticket) - Create a ticket
* [get_ticketing_agent](#get_ticketing_agent) - Retrieve a agent
* [get_ticketing_customer](#get_ticketing_customer) - Retrieve a customer
* [get_ticketing_note](#get_ticketing_note) - Retrieve a note
* [get_ticketing_ticket](#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_agents](#list_ticketing_agents) - List all agents
* [list_ticketing_customers](#list_ticketing_customers) - List all customers
* [list_ticketing_notes](#list_ticketing_notes) - List all notes
* [list_ticketing_tickets](#list_ticketing_tickets) - List all tickets
* [patch_ticketing_agent](#patch_ticketing_agent) - Update a agent
* [patch_ticketing_customer](#patch_ticketing_customer) - Update a customer
* [patch_ticketing_note](#patch_ticketing_note) - Update a note
* [patch_ticketing_ticket](#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_agent](#remove_ticketing_agent) - Remove a agent
* [remove_ticketing_customer](#remove_ticketing_customer) - Remove a customer
* [remove_ticketing_note](#remove_ticketing_note) - Remove a note
* [remove_ticketing_ticket](#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_agent](#update_ticketing_agent) - Update a agent
* [update_ticketing_customer](#update_ticketing_customer) - Update a customer
* [update_ticketing_note](#update_ticketing_note) - Update a note
* [update_ticketing_ticket](#update_ticketing_ticket) - Update a ticket

## create_ticketing_agent

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

req = operations.CreateTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Paolo.Cole8@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='scarcely Soap navigating',
            ),
        ],
    ),
    connection_id='smoothly Algeria',
)

res = s.ticketing.create_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateTicketingAgentRequest](../../models/operations/createticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateTicketingAgentResponse](../../models/operations/createticketingagentresponse.md)**


## create_ticketing_customer

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

req = operations.CreateTicketingCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        emails=[
            shared.TicketingEmail(
                email='Guadalupe78@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Borders',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Cargo Georgia earum',
            ),
        ],
    ),
    connection_id='Osmium blissfully',
)

res = s.ticketing.create_ticketing_customer(req)

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateTicketingCustomerRequest](../../models/operations/createticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateTicketingCustomerResponse](../../models/operations/createticketingcustomerresponse.md)**


## create_ticketing_note

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

req = operations.CreateTicketingNoteRequest(
    ticketing_note=shared.TicketingNote(
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='Books kilogram hmph',
    ticket_id='Dakota function interface',
)

res = s.ticketing.create_ticketing_note(req)

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateTicketingNoteRequest](../../models/operations/createticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreateTicketingNoteResponse](../../models/operations/createticketingnoteresponse.md)**


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
            'sky',
        ],
    ),
    connection_id='indigo',
)

res = s.ticketing.create_ticketing_ticket(req)

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


## get_ticketing_agent

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

req = operations.GetTicketingAgentRequest(
    connection_id='Lamborghini',
    id='<ID>',
)

res = s.ticketing.get_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTicketingAgentRequest](../../models/operations/getticketingagentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetTicketingAgentResponse](../../models/operations/getticketingagentresponse.md)**


## get_ticketing_customer

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

req = operations.GetTicketingCustomerRequest(
    connection_id='benchmark',
    id='<ID>',
)

res = s.ticketing.get_ticketing_customer(req)

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetTicketingCustomerRequest](../../models/operations/getticketingcustomerrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetTicketingCustomerResponse](../../models/operations/getticketingcustomerresponse.md)**


## get_ticketing_note

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

req = operations.GetTicketingNoteRequest(
    connection_id='joule program',
    id='<ID>',
    ticket_id='Fitness Applications Switchable',
)

res = s.ticketing.get_ticketing_note(req)

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetTicketingNoteRequest](../../models/operations/getticketingnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetTicketingNoteResponse](../../models/operations/getticketingnoteresponse.md)**


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
    connection_id='Zimbabwe Dollar',
    id='<ID>',
)

res = s.ticketing.get_ticketing_ticket(req)

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


## list_ticketing_agents

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

req = operations.ListTicketingAgentsRequest(
    connection_id='Mazda',
)

res = s.ticketing.list_ticketing_agents(req)

if res.ticketing_agents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListTicketingAgentsRequest](../../models/operations/listticketingagentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListTicketingAgentsResponse](../../models/operations/listticketingagentsresponse.md)**


## list_ticketing_customers

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

req = operations.ListTicketingCustomersRequest(
    connection_id='Carrollton yellow',
)

res = s.ticketing.list_ticketing_customers(req)

if res.ticketing_customers is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListTicketingCustomersRequest](../../models/operations/listticketingcustomersrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListTicketingCustomersResponse](../../models/operations/listticketingcustomersresponse.md)**


## list_ticketing_notes

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

req = operations.ListTicketingNotesRequest(
    connection_id='Hybrid North',
    ticket_id='Kroon Marvin Ford',
)

res = s.ticketing.list_ticketing_notes(req)

if res.ticketing_notes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListTicketingNotesRequest](../../models/operations/listticketingnotesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListTicketingNotesResponse](../../models/operations/listticketingnotesresponse.md)**


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
    connection_id='Tools Southwest',
)

res = s.ticketing.list_ticketing_tickets(req)

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


## patch_ticketing_agent

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

req = operations.PatchTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Danyka87@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='envious',
            ),
        ],
    ),
    connection_id='by',
    id='<ID>',
)

res = s.ticketing.patch_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchTicketingAgentRequest](../../models/operations/patchticketingagentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PatchTicketingAgentResponse](../../models/operations/patchticketingagentresponse.md)**


## patch_ticketing_customer

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

req = operations.PatchTicketingCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        emails=[
            shared.TicketingEmail(
                email='Raymundo93@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Brownsville',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='psst',
            ),
        ],
    ),
    connection_id='Fermium Northeast Metal',
    id='<ID>',
)

res = s.ticketing.patch_ticketing_customer(req)

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchTicketingCustomerRequest](../../models/operations/patchticketingcustomerrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchTicketingCustomerResponse](../../models/operations/patchticketingcustomerresponse.md)**


## patch_ticketing_note

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

req = operations.PatchTicketingNoteRequest(
    ticketing_note=shared.TicketingNote(
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='Bicycle Southwest Darmstadtium',
    id='<ID>',
    ticket_id='index',
)

res = s.ticketing.patch_ticketing_note(req)

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchTicketingNoteRequest](../../models/operations/patchticketingnoterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PatchTicketingNoteResponse](../../models/operations/patchticketingnoteresponse.md)**


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
            'Bespoke',
        ],
    ),
    connection_id='Pizza Concrete',
    id='<ID>',
)

res = s.ticketing.patch_ticketing_ticket(req)

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


## remove_ticketing_agent

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

req = operations.RemoveTicketingAgentRequest(
    connection_id='monitor',
    id='<ID>',
)

res = s.ticketing.remove_ticketing_agent(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveTicketingAgentRequest](../../models/operations/removeticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RemoveTicketingAgentResponse](../../models/operations/removeticketingagentresponse.md)**


## remove_ticketing_customer

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

req = operations.RemoveTicketingCustomerRequest(
    connection_id='salmon',
    id='<ID>',
)

res = s.ticketing.remove_ticketing_customer(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveTicketingCustomerRequest](../../models/operations/removeticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveTicketingCustomerResponse](../../models/operations/removeticketingcustomerresponse.md)**


## remove_ticketing_note

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

req = operations.RemoveTicketingNoteRequest(
    connection_id='Granite hm West',
    id='<ID>',
    ticket_id='in',
)

res = s.ticketing.remove_ticketing_note(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveTicketingNoteRequest](../../models/operations/removeticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.RemoveTicketingNoteResponse](../../models/operations/removeticketingnoteresponse.md)**


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
    connection_id='Handmade',
    id='<ID>',
)

res = s.ticketing.remove_ticketing_ticket(req)

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


## update_ticketing_agent

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

req = operations.UpdateTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Lorenz39@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='female',
            ),
        ],
    ),
    connection_id='beside Usability Bedfordshire',
    id='<ID>',
)

res = s.ticketing.update_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateTicketingAgentRequest](../../models/operations/updateticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateTicketingAgentResponse](../../models/operations/updateticketingagentresponse.md)**


## update_ticketing_customer

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

req = operations.UpdateTicketingCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        emails=[
            shared.TicketingEmail(
                email='Mohamed.Friesen@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Barium',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='navigating',
            ),
        ],
    ),
    connection_id='Avon Southwest',
    id='<ID>',
)

res = s.ticketing.update_ticketing_customer(req)

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateTicketingCustomerRequest](../../models/operations/updateticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateTicketingCustomerResponse](../../models/operations/updateticketingcustomerresponse.md)**


## update_ticketing_note

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

req = operations.UpdateTicketingNoteRequest(
    ticketing_note=shared.TicketingNote(
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='via among Quality',
    id='<ID>',
    ticket_id='Brand when',
)

res = s.ticketing.update_ticketing_note(req)

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateTicketingNoteRequest](../../models/operations/updateticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.UpdateTicketingNoteResponse](../../models/operations/updateticketingnoteresponse.md)**


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
            'Rhode',
        ],
    ),
    connection_id='Agender caring optimal',
    id='<ID>',
)

res = s.ticketing.update_ticketing_ticket(req)

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

