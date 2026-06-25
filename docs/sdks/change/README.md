# Change

## Overview

### Available Operations

* [get_task_change2](#get_task_change2) - Retrieve a change
* [list_task_changes2](#list_task_changes2) - List all changes

## get_task_change2

Retrieve a change

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskChange2" method="get" path="/task/{connection_id}/change/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.get_task_change2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_change is not None

    # Handle response
    print(res.task_change)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTaskChange2Request](../../models/operations/gettaskchange2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetTaskChange2Response](../../models/operations/gettaskchange2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_changes2

List all changes

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskChanges2" method="get" path="/task/{connection_id}/change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.change.list_task_changes2(request={
        "connection_id": "<id>",
    })

    assert res.task_changes is not None

    # Handle response
    print(res.task_changes)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTaskChanges2Request](../../models/operations/listtaskchanges2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListTaskChanges2Response](../../models/operations/listtaskchanges2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |