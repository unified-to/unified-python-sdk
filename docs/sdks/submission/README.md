# Submission

## Overview

### Available Operations

* [get_forms_submission2](#get_forms_submission2) - Retrieve a submission
* [list_forms_submissions2](#list_forms_submissions2) - List all submissions

## get_forms_submission2

Retrieve a submission

### Example Usage

<!-- UsageSnippet language="python" operationID="getFormsSubmission2" method="get" path="/forms/{connection_id}/submission/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.submission.get_forms_submission2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.forms_submission is not None

    # Handle response
    print(res.forms_submission)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetFormsSubmission2Request](../../models/operations/getformssubmission2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetFormsSubmission2Response](../../models/operations/getformssubmission2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_forms_submissions2

List all submissions

### Example Usage

<!-- UsageSnippet language="python" operationID="listFormsSubmissions2" method="get" path="/forms/{connection_id}/submission" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.submission.list_forms_submissions2(request={
        "connection_id": "<id>",
    })

    assert res.forms_submissions is not None

    # Handle response
    print(res.forms_submissions)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListFormsSubmissions2Request](../../models/operations/listformssubmissions2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListFormsSubmissions2Response](../../models/operations/listformssubmissions2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |