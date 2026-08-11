# Feedback

## Overview

### Available Operations

* [create_performance_feedback](#create_performance_feedback) - Create a feedback
* [get_performance_feedback](#get_performance_feedback) - Retrieve a feedback
* [list_performance_feedbacks](#list_performance_feedbacks) - List all feedbacks

## create_performance_feedback

Create a feedback

### Example Usage

<!-- UsageSnippet language="python" operationID="createPerformanceFeedback" method="post" path="/performance/{connection_id}/feedback" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.feedback.create_performance_feedback(request={
        "performance_feedback": {
            "user_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.performance_feedback is not None

    # Handle response
    print(res.performance_feedback)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreatePerformanceFeedbackRequest](../../models/operations/createperformancefeedbackrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreatePerformanceFeedbackResponse](../../models/operations/createperformancefeedbackresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_performance_feedback

Retrieve a feedback

### Example Usage

<!-- UsageSnippet language="python" operationID="getPerformanceFeedback" method="get" path="/performance/{connection_id}/feedback/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.feedback.get_performance_feedback(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.performance_feedback is not None

    # Handle response
    print(res.performance_feedback)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetPerformanceFeedbackRequest](../../models/operations/getperformancefeedbackrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetPerformanceFeedbackResponse](../../models/operations/getperformancefeedbackresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_performance_feedbacks

List all feedbacks

### Example Usage

<!-- UsageSnippet language="python" operationID="listPerformanceFeedbacks" method="get" path="/performance/{connection_id}/feedback" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.feedback.list_performance_feedbacks(request={
        "connection_id": "<id>",
    })

    assert res.performance_feedbacks is not None

    # Handle response
    print(res.performance_feedbacks)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListPerformanceFeedbacksRequest](../../models/operations/listperformancefeedbacksrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListPerformanceFeedbacksResponse](../../models/operations/listperformancefeedbacksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |