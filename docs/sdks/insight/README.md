# Insight

## Overview

### Available Operations

* [get_social_insight](#get_social_insight) - Retrieve an insight
* [list_social_insights](#list_social_insights) - List all insights

## get_social_insight

Retrieve an insight

### Example Usage

<!-- UsageSnippet language="python" operationID="getSocialInsight" method="get" path="/social/{connection_id}/insight/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insight.get_social_insight(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.social_insight is not None

    # Handle response
    print(res.social_insight)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetSocialInsightRequest](../../models/operations/getsocialinsightrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetSocialInsightResponse](../../models/operations/getsocialinsightresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_social_insights

List all insights

### Example Usage

<!-- UsageSnippet language="python" operationID="listSocialInsights" method="get" path="/social/{connection_id}/insight" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insight.list_social_insights(request={
        "connection_id": "<id>",
    })

    assert res.social_insights is not None

    # Handle response
    print(res.social_insights)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListSocialInsightsRequest](../../models/operations/listsocialinsightsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListSocialInsightsResponse](../../models/operations/listsocialinsightsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |