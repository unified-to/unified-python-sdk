# Session

## Overview

### Available Operations

* [get_analytics_session2](#get_analytics_session2) - Retrieve a session
* [list_analytics_sessions2](#list_analytics_sessions2) - List all sessions

## get_analytics_session2

Retrieve a session

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsSession2" method="get" path="/analytics/{connection_id}/session/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.session.get_analytics_session2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_session is not None

    # Handle response
    print(res.analytics_session)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsSession2Request](../../models/operations/getanalyticssession2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsSession2Response](../../models/operations/getanalyticssession2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_sessions2

List all sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsSessions2" method="get" path="/analytics/{connection_id}/session" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.session.list_analytics_sessions2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_sessions is not None

    # Handle response
    print(res.analytics_sessions)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAnalyticsSessions2Request](../../models/operations/listanalyticssessions2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAnalyticsSessions2Response](../../models/operations/listanalyticssessions2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |