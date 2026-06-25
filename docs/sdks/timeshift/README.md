# Timeshift

## Overview

### Available Operations

* [create_hris_timeshift2](#create_hris_timeshift2) - Create a timeshift
* [get_hris_timeshift2](#get_hris_timeshift2) - Retrieve a timeshift
* [list_hris_timeshifts2](#list_hris_timeshifts2) - List all timeshifts
* [patch_hris_timeshift2](#patch_hris_timeshift2) - Update a timeshift
* [remove_hris_timeshift2](#remove_hris_timeshift2) - Remove a timeshift
* [update_hris_timeshift2](#update_hris_timeshift2) - Update a timeshift

## create_hris_timeshift2

Create a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeshift2" method="post" path="/hris/{connection_id}/timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.create_hris_timeshift2(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateHrisTimeshift2Request](../../models/operations/createhristimeshift2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateHrisTimeshift2Response](../../models/operations/createhristimeshift2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeshift2

Retrieve a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeshift2" method="get" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.get_hris_timeshift2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetHrisTimeshift2Request](../../models/operations/gethristimeshift2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetHrisTimeshift2Response](../../models/operations/gethristimeshift2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeshifts2

List all timeshifts

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeshifts2" method="get" path="/hris/{connection_id}/timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.list_hris_timeshifts2(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeshifts is not None

    # Handle response
    print(res.hris_timeshifts)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListHrisTimeshifts2Request](../../models/operations/listhristimeshifts2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListHrisTimeshifts2Response](../../models/operations/listhristimeshifts2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeshift2

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeshift2" method="patch" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.patch_hris_timeshift2(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchHrisTimeshift2Request](../../models/operations/patchhristimeshift2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchHrisTimeshift2Response](../../models/operations/patchhristimeshift2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeshift2

Remove a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeshift2" method="delete" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.remove_hris_timeshift2(request={
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
| `request`                                                                                        | [operations.RemoveHrisTimeshift2Request](../../models/operations/removehristimeshift2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveHrisTimeshift2Response](../../models/operations/removehristimeshift2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeshift2

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeshift2" method="put" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.update_hris_timeshift2(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateHrisTimeshift2Request](../../models/operations/updatehristimeshift2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateHrisTimeshift2Response](../../models/operations/updatehristimeshift2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |