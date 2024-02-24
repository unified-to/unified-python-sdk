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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateTicketingTicketRequest(
    connection_id='<value>',
)

res = s.ticket.create_ticketing_ticket(req, operations.CreateTicketingTicketSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateTicketingTicketRequest](../../models/operations/createticketingticketrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.CreateTicketingTicketSecurity](../../models/operations/createticketingticketsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.CreateTicketingTicketResponse](../../models/operations/createticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ticketing_ticket

Retrieve a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingTicketRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.ticket.get_ticketing_ticket(req, operations.GetTicketingTicketSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetTicketingTicketRequest](../../models/operations/getticketingticketrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetTicketingTicketSecurity](../../models/operations/getticketingticketsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetTicketingTicketResponse](../../models/operations/getticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ticketing_tickets

List all tickets

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListTicketingTicketsRequest(
    connection_id='<value>',
)

res = s.ticket.list_ticketing_tickets(req, operations.ListTicketingTicketsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_tickets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListTicketingTicketsRequest](../../models/operations/listticketingticketsrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.ListTicketingTicketsSecurity](../../models/operations/listticketingticketssecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.ListTicketingTicketsResponse](../../models/operations/listticketingticketsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ticketing_ticket

Update a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchTicketingTicketRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.ticket.patch_ticketing_ticket(req, operations.PatchTicketingTicketSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchTicketingTicketRequest](../../models/operations/patchticketingticketrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.PatchTicketingTicketSecurity](../../models/operations/patchticketingticketsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.PatchTicketingTicketResponse](../../models/operations/patchticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ticketing_ticket

Remove a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveTicketingTicketRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.ticket.remove_ticketing_ticket(req, operations.RemoveTicketingTicketSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveTicketingTicketRequest](../../models/operations/removeticketingticketrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.RemoveTicketingTicketSecurity](../../models/operations/removeticketingticketsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.RemoveTicketingTicketResponse](../../models/operations/removeticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ticketing_ticket

Update a ticket

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateTicketingTicketRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.ticket.update_ticketing_ticket(req, operations.UpdateTicketingTicketSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_ticket is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateTicketingTicketRequest](../../models/operations/updateticketingticketrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.UpdateTicketingTicketSecurity](../../models/operations/updateticketingticketsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.UpdateTicketingTicketResponse](../../models/operations/updateticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
