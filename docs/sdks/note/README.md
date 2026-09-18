# Note

## Overview

### Available Operations

* [create_ticketing_note](#create_ticketing_note) - Create a note
* [get_ticketing_note](#get_ticketing_note) - Retrieve a note
* [list_ticketing_notes](#list_ticketing_notes) - List all notes
* [patch_ticketing_note](#patch_ticketing_note) - Update a note
* [remove_ticketing_note](#remove_ticketing_note) - Remove a note
* [update_ticketing_note](#update_ticketing_note) - Update a note

## create_ticketing_note

Create a note

### Example Usage

<!-- UsageSnippet language="python" operationID="createTicketingNote" method="post" path="/ticketing/{connection_id}/note" example="ticketing_note" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.create_ticketing_note(request={
        "ticketing_note": {
            "created_at": parse_datetime("2019-07-23T15:05:03.241Z"),
            "description": "Civitas absum adipisci vitiosus recusandae tristis dedico libero comminor cena. Spes virgo absorbeo defluo nostrum.",
            "id": "0a4a5e64-48a5-4fd9-b0c9-24cc704840a6",
            "updated_at": parse_datetime("2024-09-05T15:38:07.962Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ticketing_note is not None

    # Handle response
    print(res.ticketing_note)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateTicketingNoteRequest](../../models/operations/createticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateTicketingNoteResponse](../../models/operations/createticketingnoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ticketing_note

Retrieve a note

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingNote" method="get" path="/ticketing/{connection_id}/note/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.get_ticketing_note(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_note is not None

    # Handle response
    print(res.ticketing_note)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetTicketingNoteRequest](../../models/operations/getticketingnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetTicketingNoteResponse](../../models/operations/getticketingnoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ticketing_notes

List all notes

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingNotes" method="get" path="/ticketing/{connection_id}/note" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.list_ticketing_notes(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_notes is not None

    # Handle response
    print(res.ticketing_notes)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListTicketingNotesRequest](../../models/operations/listticketingnotesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListTicketingNotesResponse](../../models/operations/listticketingnotesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ticketing_note

Update a note

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingNote" method="patch" path="/ticketing/{connection_id}/note/{id}" example="ticketing_note" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.patch_ticketing_note(request={
        "ticketing_note": {
            "created_at": parse_datetime("2019-07-23T15:05:03.241Z"),
            "description": "Civitas absum adipisci vitiosus recusandae tristis dedico libero comminor cena. Spes virgo absorbeo defluo nostrum.",
            "id": "cf1b0373-6e5a-409c-a90c-214e826c7259",
            "updated_at": parse_datetime("2024-09-05T15:38:07.966Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_note is not None

    # Handle response
    print(res.ticketing_note)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchTicketingNoteRequest](../../models/operations/patchticketingnoterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchTicketingNoteResponse](../../models/operations/patchticketingnoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ticketing_note

Remove a note

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingNote" method="delete" path="/ticketing/{connection_id}/note/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.remove_ticketing_note(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveTicketingNoteRequest](../../models/operations/removeticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveTicketingNoteResponse](../../models/operations/removeticketingnoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ticketing_note

Update a note

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingNote" method="put" path="/ticketing/{connection_id}/note/{id}" example="ticketing_note" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.note.update_ticketing_note(request={
        "ticketing_note": {
            "created_at": parse_datetime("2019-07-23T15:05:03.241Z"),
            "description": "Civitas absum adipisci vitiosus recusandae tristis dedico libero comminor cena. Spes virgo absorbeo defluo nostrum.",
            "id": "cf1b0373-6e5a-409c-a90c-214e826c7259",
            "updated_at": parse_datetime("2024-09-05T15:38:07.966Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_note is not None

    # Handle response
    print(res.ticketing_note)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateTicketingNoteRequest](../../models/operations/updateticketingnoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateTicketingNoteResponse](../../models/operations/updateticketingnoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |