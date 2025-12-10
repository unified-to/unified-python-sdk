# Timeshift

## Overview

### Available Operations

* [create_hris_timeshift](#create_hris_timeshift) - Create a timeshift
* [get_hris_timeshift](#get_hris_timeshift) - Retrieve a timeshift
* [list_hris_timeshifts](#list_hris_timeshifts) - List all timeshifts
* [patch_hris_timeshift](#patch_hris_timeshift) - Update a timeshift
* [remove_hris_timeshift](#remove_hris_timeshift) - Remove a timeshift
* [update_hris_timeshift](#update_hris_timeshift) - Update a timeshift

## create_hris_timeshift

Create a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeshift" method="post" path="/hris/{connection_id}/timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.create_hris_timeshift(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2025-10-18T00:03:45.822Z"),
            "start_at": parse_datetime("2024-06-03T05:33:48.715Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateHrisTimeshiftRequest](../../models/operations/createhristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateHrisTimeshiftResponse](../../models/operations/createhristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeshift

Retrieve a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeshift" method="get" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.get_hris_timeshift(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisTimeshiftRequest](../../models/operations/gethristimeshiftrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetHrisTimeshiftResponse](../../models/operations/gethristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeshifts

List all timeshifts

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeshifts" method="get" path="/hris/{connection_id}/timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.list_hris_timeshifts(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeshifts is not None

    # Handle response
    print(res.hris_timeshifts)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisTimeshiftsRequest](../../models/operations/listhristimeshiftsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisTimeshiftsResponse](../../models/operations/listhristimeshiftsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeshift

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeshift" method="patch" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.patch_hris_timeshift(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2023-11-17T18:53:02.172Z"),
            "start_at": parse_datetime("2023-01-19T02:48:41.002Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchHrisTimeshiftRequest](../../models/operations/patchhristimeshiftrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchHrisTimeshiftResponse](../../models/operations/patchhristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeshift

Remove a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeshift" method="delete" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.remove_hris_timeshift(request={
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
| `request`                                                                                      | [operations.RemoveHrisTimeshiftRequest](../../models/operations/removehristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveHrisTimeshiftResponse](../../models/operations/removehristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeshift

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeshift" method="put" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.timeshift.update_hris_timeshift(request={
        "hris_timeshift": {
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2025-03-03T22:04:09.340Z"),
            "start_at": parse_datetime("2024-05-30T21:19:58.772Z"),
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
| `request`                                                                                      | [operations.UpdateHrisTimeshiftRequest](../../models/operations/updatehristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateHrisTimeshiftResponse](../../models/operations/updatehristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |