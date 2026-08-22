# Notification

## Overview

### Available Operations

* [list_unified_notifications](#list_unified_notifications) - List event notifications

## list_unified_notifications

List event notifications

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedNotifications" method="get" path="/unified/notification" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.notification.list_unified_notifications(request={})

    assert res.notifications is not None

    # Handle response
    print(res.notifications)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListUnifiedNotificationsRequest](../../models/operations/listunifiednotificationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListUnifiedNotificationsResponse](../../models/operations/listunifiednotificationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |