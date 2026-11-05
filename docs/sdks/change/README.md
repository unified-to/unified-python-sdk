# Change

## Overview

### Available Operations

* [create_plm_change](#create_plm_change) - Create a change
* [get_plm_change](#get_plm_change) - Retrieve a change
* [get_task_change](#get_task_change) - Retrieve a change
* [list_plm_changes](#list_plm_changes) - List all changes
* [list_task_changes](#list_task_changes) - List all changes
* [patch_plm_change](#patch_plm_change) - Update a change
* [update_plm_change](#update_plm_change) - Update a change

## create_plm_change

Creates a PlmChange. Provide the unified PlmChange fields in the request body; they are mapped to the provider's API. Returns the created PlmChange.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmChange" method="post" path="/plm/{connection_id}/change" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.create_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "df7134ee-1b08-46f0-a2ea-ad708a2c6c76",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-18T15:49:21.631Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePlmChangeRequest](../../models/operations/createplmchangerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreatePlmChangeResponse](../../models/operations/createplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_change

Retrieves a single PlmChange by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmChange" method="get" path="/plm/{connection_id}/change/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.get_plm_change(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetPlmChangeRequest](../../models/operations/getplmchangerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetPlmChangeResponse](../../models/operations/getplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_task_change

Retrieves a single TaskChange by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskChange" method="get" path="/task/{connection_id}/change/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.get_task_change(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_change is not None

    # Handle response
    print(res.task_change)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetTaskChangeRequest](../../models/operations/gettaskchangerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetTaskChangeResponse](../../models/operations/gettaskchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_changes

Returns a list of PlmChanges. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmChanges" method="get" path="/plm/{connection_id}/change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.list_plm_changes(request={
        "connection_id": "<id>",
    })

    assert res.plm_changes is not None

    # Handle response
    print(res.plm_changes)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListPlmChangesRequest](../../models/operations/listplmchangesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListPlmChangesResponse](../../models/operations/listplmchangesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_changes

Returns a list of TaskChanges. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskChanges" method="get" path="/task/{connection_id}/change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.list_task_changes(request={
        "connection_id": "<id>",
    })

    assert res.task_changes is not None

    # Handle response
    print(res.task_changes)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListTaskChangesRequest](../../models/operations/listtaskchangesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListTaskChangesResponse](../../models/operations/listtaskchangesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_change

Updates the PlmChange identified by `id`. Provide the unified PlmChange fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmChange" method="patch" path="/plm/{connection_id}/change/{id}" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.patch_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "9ece7ed0-fe95-4128-a958-cf29c1d1f872",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-18T15:49:21.664Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchPlmChangeRequest](../../models/operations/patchplmchangerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchPlmChangeResponse](../../models/operations/patchplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_change

Updates the PlmChange identified by `id`. Provide the unified PlmChange fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmChange" method="put" path="/plm/{connection_id}/change/{id}" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.update_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "9ece7ed0-fe95-4128-a958-cf29c1d1f872",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-18T15:49:21.664Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdatePlmChangeRequest](../../models/operations/updateplmchangerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdatePlmChangeResponse](../../models/operations/updateplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |