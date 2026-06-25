# Timeoff

## Overview

### Available Operations

* [create_hris_timeoff2](#create_hris_timeoff2) - Create a timeoff
* [get_hris_timeoff2](#get_hris_timeoff2) - Retrieve a timeoff
* [list_hris_timeoffs2](#list_hris_timeoffs2) - List all timeoffs
* [patch_hris_timeoff2](#patch_hris_timeoff2) - Update a timeoff
* [remove_hris_timeoff2](#remove_hris_timeoff2) - Remove a timeoff
* [update_hris_timeoff2](#update_hris_timeoff2) - Update a timeoff

## create_hris_timeoff2

Create a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeoff2" method="post" path="/hris/{connection_id}/timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.create_hris_timeoff2(request={
        "hris_timeoff": {
            "user_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisTimeoff2Request](../../models/operations/createhristimeoff2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisTimeoff2Response](../../models/operations/createhristimeoff2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeoff2

Retrieve a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeoff2" method="get" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.get_hris_timeoff2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisTimeoff2Request](../../models/operations/gethristimeoff2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisTimeoff2Response](../../models/operations/gethristimeoff2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeoffs2

List all timeoffs

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeoffs2" method="get" path="/hris/{connection_id}/timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.list_hris_timeoffs2(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeoffs is not None

    # Handle response
    print(res.hris_timeoffs)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisTimeoffs2Request](../../models/operations/listhristimeoffs2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisTimeoffs2Response](../../models/operations/listhristimeoffs2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeoff2

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeoff2" method="patch" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.patch_hris_timeoff2(request={
        "hris_timeoff": {
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
| `request`                                                                                  | [operations.PatchHrisTimeoff2Request](../../models/operations/patchhristimeoff2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisTimeoff2Response](../../models/operations/patchhristimeoff2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeoff2

Remove a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeoff2" method="delete" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.remove_hris_timeoff2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisTimeoff2Request](../../models/operations/removehristimeoff2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisTimeoff2Response](../../models/operations/removehristimeoff2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeoff2

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeoff2" method="put" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeoff.update_hris_timeoff2(request={
        "hris_timeoff": {
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

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisTimeoff2Request](../../models/operations/updatehristimeoff2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisTimeoff2Response](../../models/operations/updatehristimeoff2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |