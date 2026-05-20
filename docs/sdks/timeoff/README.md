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

Create a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeoff" method="post" path="/hris/{connection_id}/timeoff" -->
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
            "start_at": parse_datetime("2024-09-03T22:31:51.863Z"),
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

Retrieve a timeoff

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

List all timeoffs

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

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeoff" method="patch" path="/hris/{connection_id}/timeoff/{id}" -->
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
            "start_at": parse_datetime("2024-01-26T05:49:44.056Z"),
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

Remove a timeoff

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

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeoff" method="put" path="/hris/{connection_id}/timeoff/{id}" -->
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
            "start_at": parse_datetime("2026-02-26T01:59:20.061Z"),
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