# Session

## Overview

### Available Operations

* [get_analytics_session](#get_analytics_session) - Retrieve a session
* [list_analytics_sessions](#list_analytics_sessions) - List all sessions

## get_analytics_session

Retrieve a session

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsSession" method="get" path="/analytics/{connection_id}/session/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.session.get_analytics_session(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_session is not None

    # Handle response
    print(res.analytics_session)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAnalyticsSessionRequest](../../models/operations/getanalyticssessionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetAnalyticsSessionResponse](../../models/operations/getanalyticssessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_sessions

List all sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsSessions" method="get" path="/analytics/{connection_id}/session" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.session.list_analytics_sessions(request={
        "connection_id": "<id>",
    })

    assert res.analytics_sessions is not None

    # Handle response
    print(res.analytics_sessions)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAnalyticsSessionsRequest](../../models/operations/listanalyticssessionsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAnalyticsSessionsResponse](../../models/operations/listanalyticssessionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |