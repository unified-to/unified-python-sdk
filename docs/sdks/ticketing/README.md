# Ticketing

## Overview

### Available Operations

* [create_ticketing_category](#create_ticketing_category) - Create a category
* [create_ticketing_customer](#create_ticketing_customer) - Create a customer
* [create_ticketing_note](#create_ticketing_note) - Create a note
* [create_ticketing_ticket](#create_ticketing_ticket) - Create a ticket
* [get_ticketing_category](#get_ticketing_category) - Retrieve a category
* [get_ticketing_customer](#get_ticketing_customer) - Retrieve a customer
* [get_ticketing_note](#get_ticketing_note) - Retrieve a note
* [get_ticketing_ticket](#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_categories](#list_ticketing_categories) - List all categories
* [list_ticketing_customers](#list_ticketing_customers) - List all customers
* [list_ticketing_notes](#list_ticketing_notes) - List all notes
* [list_ticketing_tickets](#list_ticketing_tickets) - List all tickets
* [patch_ticketing_category](#patch_ticketing_category) - Update a category
* [patch_ticketing_customer](#patch_ticketing_customer) - Update a customer
* [patch_ticketing_note](#patch_ticketing_note) - Update a note
* [patch_ticketing_ticket](#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_category](#remove_ticketing_category) - Remove a category
* [remove_ticketing_customer](#remove_ticketing_customer) - Remove a customer
* [remove_ticketing_note](#remove_ticketing_note) - Remove a note
* [remove_ticketing_ticket](#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_category](#update_ticketing_category) - Update a category
* [update_ticketing_customer](#update_ticketing_customer) - Update a customer
* [update_ticketing_note](#update_ticketing_note) - Update a note
* [update_ticketing_ticket](#update_ticketing_ticket) - Update a ticket

## create_ticketing_category

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createTicketingCategory" method="post" path="/ticketing/{connection_id}/category" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.create_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "5ac2d511-1ea8-4ac2-9c12-e64f60d29e93",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-15T15:10:31.164Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateTicketingCategoryRequest](../../models/operations/createticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateTicketingCategoryResponse](../../models/operations/createticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ticketing_customer

Create a customer

### Example Usage

<!-- UsageSnippet language="python" operationID="createTicketingCustomer" method="post" path="/ticketing/{connection_id}/customer" example="ticketing_customer" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.create_ticketing_customer(request={
        "ticketing_customer": {
            "created_at": parse_datetime("2021-03-15T12:33:14.875Z"),
            "emails": [
                {
                    "email": "Christian_Windler@gmail.com",
                    "type": shared.TicketingEmailType.HOME,
                },
            ],
            "id": "7aaf843a-eb51-4f52-8529-70aa2d242803",
            "name": "Christian Windler",
            "tags": [
                "casso",
                "peccatus",
            ],
            "telephones": [
                {
                    "telephone": "(532) 242-0482",
                    "type": shared.TicketingTelephoneType.OTHER,
                },
                {
                    "telephone": "(826) 283-7431",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
                {
                    "telephone": "(483) 314-6826",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-05-04T07:38:52.565Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ticketing_customer is not None

    # Handle response
    print(res.ticketing_customer)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateTicketingCustomerRequest](../../models/operations/createticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateTicketingCustomerResponse](../../models/operations/createticketingcustomerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.ticketing.create_ticketing_note(request={
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

    res = unified_to.ticketing.create_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "4b783299-a1bd-4aa8-b927-8ef63968bd27",
                "1e29f1cb-e9a0-414f-a7b9-62a74aa6b95f",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-20T03:56:57.584Z"),
            "id": "ee500ada-985e-46ce-99ff-e1403b9b33dc",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "3598fc4e-a2fd-4eea-a97f-367fe161591f",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T07:25:19.149Z"),
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

## get_ticketing_category

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingCategory" method="get" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.get_ticketing_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetTicketingCategoryRequest](../../models/operations/getticketingcategoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetTicketingCategoryResponse](../../models/operations/getticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ticketing_customer

Retrieve a customer

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingCustomer" method="get" path="/ticketing/{connection_id}/customer/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.get_ticketing_customer(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_customer is not None

    # Handle response
    print(res.ticketing_customer)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetTicketingCustomerRequest](../../models/operations/getticketingcustomerrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetTicketingCustomerResponse](../../models/operations/getticketingcustomerresponse.md)**

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

    res = unified_to.ticketing.get_ticketing_note(request={
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

    res = unified_to.ticketing.get_ticketing_ticket(request={
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

## list_ticketing_categories

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingCategories" method="get" path="/ticketing/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.list_ticketing_categories(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_categories is not None

    # Handle response
    print(res.ticketing_categories)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTicketingCategoriesRequest](../../models/operations/listticketingcategoriesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListTicketingCategoriesResponse](../../models/operations/listticketingcategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ticketing_customers

List all customers

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingCustomers" method="get" path="/ticketing/{connection_id}/customer" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.list_ticketing_customers(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_customers is not None

    # Handle response
    print(res.ticketing_customers)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListTicketingCustomersRequest](../../models/operations/listticketingcustomersrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListTicketingCustomersResponse](../../models/operations/listticketingcustomersresponse.md)**

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

    res = unified_to.ticketing.list_ticketing_notes(request={
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

    res = unified_to.ticketing.list_ticketing_tickets(request={
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

## patch_ticketing_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingCategory" method="patch" path="/ticketing/{connection_id}/category/{id}" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.patch_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "a4a3eb17-54d3-419a-aafa-5473e1d8a0f0",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-15T15:10:31.172Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchTicketingCategoryRequest](../../models/operations/patchticketingcategoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchTicketingCategoryResponse](../../models/operations/patchticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ticketing_customer

Update a customer

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingCustomer" method="patch" path="/ticketing/{connection_id}/customer/{id}" example="ticketing_customer" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.patch_ticketing_customer(request={
        "ticketing_customer": {
            "created_at": parse_datetime("2021-03-15T12:33:14.875Z"),
            "emails": [
                {
                    "email": "Christian_Windler@gmail.com",
                    "type": shared.TicketingEmailType.HOME,
                },
            ],
            "id": "81231dce-2c6b-48df-af99-3f67b7571c0d",
            "name": "Christian Windler",
            "tags": [
                "casso",
                "peccatus",
            ],
            "telephones": [
                {
                    "telephone": "(532) 242-0482",
                    "type": shared.TicketingTelephoneType.OTHER,
                },
                {
                    "telephone": "(826) 283-7431",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
                {
                    "telephone": "(483) 314-6826",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-05-04T07:38:52.574Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_customer is not None

    # Handle response
    print(res.ticketing_customer)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchTicketingCustomerRequest](../../models/operations/patchticketingcustomerrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchTicketingCustomerResponse](../../models/operations/patchticketingcustomerresponse.md)**

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

    res = unified_to.ticketing.patch_ticketing_note(request={
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

    res = unified_to.ticketing.patch_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "468214ca-392e-4132-bf6c-8ec3404068e3",
                "e4f148af-512f-40c7-895f-4b9a804e181c",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-20T03:56:57.591Z"),
            "id": "b2013661-c6d4-406a-928f-474f32294ac7",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "a653a581-d9bb-4ca6-868f-20015c9bf928",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T07:25:19.152Z"),
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

## remove_ticketing_category

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingCategory" method="delete" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.remove_ticketing_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveTicketingCategoryRequest](../../models/operations/removeticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveTicketingCategoryResponse](../../models/operations/removeticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ticketing_customer

Remove a customer

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingCustomer" method="delete" path="/ticketing/{connection_id}/customer/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.remove_ticketing_customer(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveTicketingCustomerRequest](../../models/operations/removeticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveTicketingCustomerResponse](../../models/operations/removeticketingcustomerresponse.md)**

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

    res = unified_to.ticketing.remove_ticketing_note(request={
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

    res = unified_to.ticketing.remove_ticketing_ticket(request={
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

## update_ticketing_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingCategory" method="put" path="/ticketing/{connection_id}/category/{id}" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.update_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "a4a3eb17-54d3-419a-aafa-5473e1d8a0f0",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-15T15:10:31.172Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateTicketingCategoryRequest](../../models/operations/updateticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateTicketingCategoryResponse](../../models/operations/updateticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ticketing_customer

Update a customer

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingCustomer" method="put" path="/ticketing/{connection_id}/customer/{id}" example="ticketing_customer" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ticketing.update_ticketing_customer(request={
        "ticketing_customer": {
            "created_at": parse_datetime("2021-03-15T12:33:14.875Z"),
            "emails": [
                {
                    "email": "Christian_Windler@gmail.com",
                    "type": shared.TicketingEmailType.HOME,
                },
            ],
            "id": "81231dce-2c6b-48df-af99-3f67b7571c0d",
            "name": "Christian Windler",
            "tags": [
                "casso",
                "peccatus",
            ],
            "telephones": [
                {
                    "telephone": "(532) 242-0482",
                    "type": shared.TicketingTelephoneType.OTHER,
                },
                {
                    "telephone": "(826) 283-7431",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
                {
                    "telephone": "(483) 314-6826",
                    "type": shared.TicketingTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-05-04T07:38:52.574Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_customer is not None

    # Handle response
    print(res.ticketing_customer)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateTicketingCustomerRequest](../../models/operations/updateticketingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateTicketingCustomerResponse](../../models/operations/updateticketingcustomerresponse.md)**

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

    res = unified_to.ticketing.update_ticketing_note(request={
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

    res = unified_to.ticketing.update_ticketing_ticket(request={
        "ticketing_ticket": {
            "attachment_ids": [
                "468214ca-392e-4132-bf6c-8ec3404068e3",
                "e4f148af-512f-40c7-895f-4b9a804e181c",
            ],
            "category_id": "vilicus",
            "created_at": parse_datetime("2021-06-25T19:19:31.279Z"),
            "description": "Cura dignissimos aut clibanus vulgaris patrocinor. Laborum acies curiositas antepono coniuratio. Correptius curiositas sono censura coma. Bestia suus tot cotidie terror subito coniecto beneficium.",
            "due_at": parse_datetime("2025-07-20T03:56:57.591Z"),
            "id": "b2013661-c6d4-406a-928f-474f32294ac7",
            "priority": "LOW",
            "source": "atavus",
            "source_ref": "a653a581-d9bb-4ca6-868f-20015c9bf928",
            "status": shared.TicketingTicketStatus.ACTIVE,
            "subject": "Thymbra ratione minus arbitro tricesimus cetera validus.",
            "tags": [
                "tamen",
                "vitae",
                "torrens",
            ],
            "updated_at": parse_datetime("2023-05-28T07:25:19.152Z"),
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