# Ticket

## Overview

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

<!-- UsageSnippet language="python" operationID="createTicketingTicket" method="post" path="/ticketing/{connection_id}/ticket" example="ticketing_ticket" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.create_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "b4afed16-0825-41e9-a8c5-2820095024c0",
                "7488ad37-8895-4b87-82b6-9e20f980fe67",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-21T04:30:13.695Z"),
            "id": "e616437e-b939-4a19-8cf3-a161dd34f622",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "8cd03440-6ab4-45c2-83d9-aedac48a1c8a",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T19:01:06.776Z"),
            "url": "https://yellowish-testimonial.biz",
        },
        "connection_id": "<id>",
    })

    assert res.ticketing_ticket is not None

    # Handle response
    print(res.ticketing_ticket)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateTicketingTicketRequest](../../models/operations/createticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateTicketingTicketResponse](../../models/operations/createticketingticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ticketing_ticket

Retrieve a ticket

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingTicket" method="get" path="/ticketing/{connection_id}/ticket/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.get_ticketing_ticket(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_ticket is not None

    # Handle response
    print(res.ticketing_ticket)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetTicketingTicketRequest](../../models/operations/getticketingticketrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetTicketingTicketResponse](../../models/operations/getticketingticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ticketing_tickets

List all tickets

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingTickets" method="get" path="/ticketing/{connection_id}/ticket" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.list_ticketing_tickets(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_tickets is not None

    # Handle response
    print(res.ticketing_tickets)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListTicketingTicketsRequest](../../models/operations/listticketingticketsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListTicketingTicketsResponse](../../models/operations/listticketingticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ticketing_ticket

Update a ticket

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingTicket" method="patch" path="/ticketing/{connection_id}/ticket/{id}" example="ticketing_ticket" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.patch_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "70c80951-a6f1-489f-af45-846330b9964b",
                "6e82e258-2eac-4f71-a27c-b1f006e4daea",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-21T04:30:13.702Z"),
            "id": "c72614eb-1882-44c7-bf84-b6d725d374bc",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "78cad760-be85-4e0c-a9ae-bf23c4d98112",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T19:01:06.779Z"),
            "url": "https://yellowish-testimonial.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_ticket is not None

    # Handle response
    print(res.ticketing_ticket)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchTicketingTicketRequest](../../models/operations/patchticketingticketrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchTicketingTicketResponse](../../models/operations/patchticketingticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ticketing_ticket

Remove a ticket

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingTicket" method="delete" path="/ticketing/{connection_id}/ticket/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.remove_ticketing_ticket(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveTicketingTicketRequest](../../models/operations/removeticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveTicketingTicketResponse](../../models/operations/removeticketingticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ticketing_ticket

Update a ticket

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingTicket" method="put" path="/ticketing/{connection_id}/ticket/{id}" example="ticketing_ticket" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticket.update_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "70c80951-a6f1-489f-af45-846330b9964b",
                "6e82e258-2eac-4f71-a27c-b1f006e4daea",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-21T04:30:13.702Z"),
            "id": "c72614eb-1882-44c7-bf84-b6d725d374bc",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "78cad760-be85-4e0c-a9ae-bf23c4d98112",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T19:01:06.779Z"),
            "url": "https://yellowish-testimonial.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_ticket is not None

    # Handle response
    print(res.ticketing_ticket)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateTicketingTicketRequest](../../models/operations/updateticketingticketrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateTicketingTicketResponse](../../models/operations/updateticketingticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |