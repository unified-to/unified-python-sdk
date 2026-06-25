# Busy

## Overview

### Available Operations

* [list_calendar_busies2](#list_calendar_busies2) - List all busies

## list_calendar_busies2

List all busies

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarBusies2" method="get" path="/calendar/{connection_id}/busy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.busy.list_calendar_busies2(request={
        "connection_id": "<id>",
    })

    assert res.calendar_busies is not None

    # Handle response
    print(res.calendar_busies)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListCalendarBusies2Request](../../models/operations/listcalendarbusies2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListCalendarBusies2Response](../../models/operations/listcalendarbusies2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |