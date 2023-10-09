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
    ticket_id='Associate',
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
    connection_id='New',
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
        emails=[
            shared.TicketingEmail(
                email='Albertha.Bernier63@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='Borders parse',
            ),
        ],
    ),
    connection_id='driver',
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
        emails=[
            shared.TicketingEmail(
                email='Jaren_Ryan@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Waco',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='youthfully orange',
            ),
        ],
    ),
    connection_id='Smyrna Hialeah auxiliary',
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
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='compress Oganesson',
    id='<ID>',
    ticket_id='York Fantastic',
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
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'Polygender',
        ],
    ),
    connection_id='calculate midst female',
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
        emails=[
            shared.TicketingEmail(
                email='Adele80@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='Unbranded Sedan',
            ),
        ],
    ),
    connection_id='wireless absent',
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
        emails=[
            shared.TicketingEmail(
                email='Jaquelin.Boyer@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'withdrawal',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Configuration neural',
            ),
        ],
    ),
    connection_id='Product Hybrid',
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
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='Plantation blue',
    ticket_id='Ford',
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
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'Alabama',
        ],
    ),
    connection_id='Jewelery',
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
        emails=[
            shared.TicketingEmail(
                email='Samara_Botsford@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='newton Coordinator Refined',
            ),
        ],
    ),
    connection_id='asynchronous',
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
        emails=[
            shared.TicketingEmail(
                email='Raleigh.Torp42@gmail.com',
            ),
        ],
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'copy',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Developer Buckinghamshire Sausages',
            ),
        ],
    ),
    connection_id='kilogram',
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
        raw=shared.PropertyTicketingNoteRaw(),
    ),
    connection_id='SMTP Cis',
    id='<ID>',
    ticket_id='East benchmark',
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
        raw=shared.PropertyTicketingTicketRaw(),
        tags=[
            'driver',
        ],
    ),
    connection_id='Finland',
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

