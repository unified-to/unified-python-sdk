# Timeoff

## Overview

### Available Operations

* [create_hris_timeoff](#create_hris_timeoff) - Create a timeoff
* [get_hris_timeoff](#get_hris_timeoff) - Retrieve a timeoff
* [list_hris_timeoffs](#list_hris_timeoffs) - List all timeoffs
* [patch_hris_timeoff](#patch_hris_timeoff) - Update a timeoff
* [remove_hris_timeoff](#remove_hris_timeoff) - Remove a timeoff
* [update_hris_timeoff](#update_hris_timeoff) - Update a timeoff

## create_hris_timeoff

Creates a HrisTimeoff. Provide the unified HrisTimeoff fields in the request body; they are mapped to the provider's API. Returns the created HrisTimeoff.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeoff" method="post" path="/hris/{connection_id}/timeoff" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.create_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-24T03:10:09.538Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2025-01-04T01:30:02.221Z"),
            "id": "17cc4429-90b2-4ba2-baef-d1aad9517ba2",
            "is_paid": True,
            "metadata": [],
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-09-08T13:31:11.656Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-14T07:43:33.352Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisTimeoffRequest](../../models/operations/createhristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisTimeoffResponse](../../models/operations/createhristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeoff

Retrieves a single HrisTimeoff by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeoff" method="get" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.get_hris_timeoff(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisTimeoffRequest](../../models/operations/gethristimeoffrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisTimeoffResponse](../../models/operations/gethristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeoffs

Returns a list of HrisTimeoffs. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeoffs" method="get" path="/hris/{connection_id}/timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.list_hris_timeoffs(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeoffs is not None

    # Handle response
    print(res.hris_timeoffs)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisTimeoffsRequest](../../models/operations/listhristimeoffsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisTimeoffsResponse](../../models/operations/listhristimeoffsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeoff

Updates the HrisTimeoff identified by `id`. Provide the unified HrisTimeoff fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeoff" method="patch" path="/hris/{connection_id}/timeoff/{id}" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.patch_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-24T03:10:09.539Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2025-01-04T01:30:02.230Z"),
            "id": "25029424-cd0e-4a4c-9384-dbecc7f819b7",
            "is_paid": True,
            "metadata": [],
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-09-08T13:31:11.661Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-14T07:43:33.354Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisTimeoffRequest](../../models/operations/patchhristimeoffrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisTimeoffResponse](../../models/operations/patchhristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeoff

Deletes the HrisTimeoff identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeoff" method="delete" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.remove_hris_timeoff(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveHrisTimeoffRequest](../../models/operations/removehristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisTimeoffResponse](../../models/operations/removehristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeoff

Updates the HrisTimeoff identified by `id`. Provide the unified HrisTimeoff fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeoff" method="put" path="/hris/{connection_id}/timeoff/{id}" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.update_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-24T03:10:09.539Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2025-01-04T01:30:02.230Z"),
            "id": "25029424-cd0e-4a4c-9384-dbecc7f819b7",
            "is_paid": True,
            "metadata": [],
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-09-08T13:31:11.661Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-14T07:43:33.354Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisTimeoffRequest](../../models/operations/updatehristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisTimeoffResponse](../../models/operations/updatehristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |