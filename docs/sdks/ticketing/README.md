# Ticketing
(*ticketing*)

### Available Operations

* [create_ticketing_customer](#create_ticketing_customer) - Create a customer
* [create_ticketing_note](#create_ticketing_note) - Create a note
* [create_ticketing_ticket](#create_ticketing_ticket) - Create a ticket
* [get_ticketing_customer](#get_ticketing_customer) - Retrieve a customer
* [get_ticketing_note](#get_ticketing_note) - Retrieve a note
* [get_ticketing_ticket](#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_customers](#list_ticketing_customers) - List all customers
* [list_ticketing_notes](#list_ticketing_notes) - List all notes
* [list_ticketing_tickets](#list_ticketing_tickets) - List all tickets
* [patch_ticketing_customer](#patch_ticketing_customer) - Update a customer
* [patch_ticketing_note](#patch_ticketing_note) - Update a note
* [patch_ticketing_ticket](#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_customer](#remove_ticketing_customer) - Remove a customer
* [remove_ticketing_note](#remove_ticketing_note) - Remove a note
* [remove_ticketing_ticket](#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_customer](#update_ticketing_customer) - Update a customer
* [update_ticketing_note](#update_ticketing_note) - Update a note
* [update_ticketing_ticket](#update_ticketing_ticket) - Update a ticket

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
            'string',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
    connection_id='string',
    ticket_id='string',
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
            'string',
        ],
    ),
    connection_id='string',
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
    connection_id='string',
    fields_=[
        'string',
    ],
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
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
    ticket_id='string',
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
    connection_id='string',
    fields_=[
        'string',
    ],
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
    connection_id='string',
    fields_=[
        'string',
    ],
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
    connection_id='string',
    fields_=[
        'string',
    ],
    ticket_id='string',
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
    connection_id='string',
    fields_=[
        'string',
    ],
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
            'string',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
    connection_id='string',
    id='<ID>',
    ticket_id='string',
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
            'string',
        ],
    ),
    connection_id='string',
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
    connection_id='string',
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
    connection_id='string',
    id='<ID>',
    ticket_id='string',
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
    connection_id='string',
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
            'string',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
    connection_id='string',
    id='<ID>',
    ticket_id='string',
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
            'string',
        ],
    ),
    connection_id='string',
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

