# Timeentry

## Overview

### Available Operations

* [create_legal_timeentry](#create_legal_timeentry) - Create a timeentry
* [get_legal_timeentry](#get_legal_timeentry) - Retrieve a timeentry
* [list_legal_timeentries](#list_legal_timeentries) - List all timeentries
* [patch_legal_timeentry](#patch_legal_timeentry) - Update a timeentry
* [remove_legal_timeentry](#remove_legal_timeentry) - Remove a timeentry
* [update_legal_timeentry](#update_legal_timeentry) - Update a timeentry

## create_legal_timeentry

Creates a LegalTimeentry. Provide the unified LegalTimeentry fields in the request body; they are mapped to the provider's API. Returns the created LegalTimeentry.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalTimeentry" method="post" path="/legal/{connection_id}/timeentry" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.create_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "ae2c0d52-8cb7-4a6b-9d3d-ae3ff9f57b82",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-30T02:37:32.644Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateLegalTimeentryRequest](../../models/operations/createlegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateLegalTimeentryResponse](../../models/operations/createlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_legal_timeentry

Retrieves a single LegalTimeentry by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalTimeentry" method="get" path="/legal/{connection_id}/timeentry/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.get_legal_timeentry(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetLegalTimeentryRequest](../../models/operations/getlegaltimeentryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetLegalTimeentryResponse](../../models/operations/getlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_legal_timeentries

Returns a list of LegalTimeentries. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalTimeentries" method="get" path="/legal/{connection_id}/timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.list_legal_timeentries(request={
        "connection_id": "<id>",
    })

    assert res.legal_timeentries is not None

    # Handle response
    print(res.legal_timeentries)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListLegalTimeentriesRequest](../../models/operations/listlegaltimeentriesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListLegalTimeentriesResponse](../../models/operations/listlegaltimeentriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_legal_timeentry

Updates the LegalTimeentry identified by `id`. Provide the unified LegalTimeentry fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalTimeentry" method="patch" path="/legal/{connection_id}/timeentry/{id}" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.patch_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "4e531b0d-4ddd-4eee-9a69-1e4583eca5bc",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-30T02:37:32.645Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchLegalTimeentryRequest](../../models/operations/patchlegaltimeentryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchLegalTimeentryResponse](../../models/operations/patchlegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_legal_timeentry

Deletes the LegalTimeentry identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalTimeentry" method="delete" path="/legal/{connection_id}/timeentry/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.remove_legal_timeentry(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveLegalTimeentryRequest](../../models/operations/removelegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveLegalTimeentryResponse](../../models/operations/removelegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_legal_timeentry

Updates the LegalTimeentry identified by `id`. Provide the unified LegalTimeentry fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalTimeentry" method="put" path="/legal/{connection_id}/timeentry/{id}" example="legal_timeentry" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeentry.update_legal_timeentry(request={
        "legal_timeentry": {
            "billable_minutes": 390.0,
            "created_at": parse_datetime("2022-05-06T03:26:03.756Z"),
            "currency": "ZAR",
            "description": "Ea derideo adulatio torrens.",
            "id": "4e531b0d-4ddd-4eee-9a69-1e4583eca5bc",
            "is_billable": True,
            "metadata": [],
            "minutes": 390.0,
            "rate_amount": 637.0,
            "total_amount": 4140.5,
            "updated_at": parse_datetime("2022-06-30T02:37:32.645Z"),
            "worked_at": parse_datetime("2022-05-06T03:26:03.756Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_timeentry is not None

    # Handle response
    print(res.legal_timeentry)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateLegalTimeentryRequest](../../models/operations/updatelegaltimeentryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateLegalTimeentryResponse](../../models/operations/updatelegaltimeentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |