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
                "bd2db230-3791-4715-89d3-d978274ebc5e",
                "1dc11f22-bddd-4b64-a067-ab3f242916b5",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-08-10T00:55:32.498Z"),
            "id": "1eb0d028-e5bb-490c-8e80-584036c3ab5f",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "baa5b5c8-28ff-44da-a9f8-ac9895ea00db",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-06-07T04:01:21.376Z"),
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
                "08c45e12-be29-448d-9aca-4b27bdfc355e",
                "c0d8a552-dfcd-4681-86a0-e30e818738d7",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-08-10T00:55:32.509Z"),
            "id": "b33fe623-6833-436e-9cf9-e84ba53d5f09",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "88d45051-66af-4193-b9b1-af39b05ece43",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-06-07T04:01:21.381Z"),
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
                "08c45e12-be29-448d-9aca-4b27bdfc355e",
                "c0d8a552-dfcd-4681-86a0-e30e818738d7",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-08-10T00:55:32.509Z"),
            "id": "b33fe623-6833-436e-9cf9-e84ba53d5f09",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "88d45051-66af-4193-b9b1-af39b05ece43",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-06-07T04:01:21.381Z"),
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