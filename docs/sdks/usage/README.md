# Usage

## Overview

### Available Operations

* [list_compute_usages](#list_compute_usages) - List all usages

## list_compute_usages

List all usages

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeUsages" method="get" path="/compute/{connection_id}/usage" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.usage.list_compute_usages(request={
        "connection_id": "<id>",
    })

    assert res.compute_usages is not None

    # Handle response
    print(res.compute_usages)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListComputeUsagesRequest](../../models/operations/listcomputeusagesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListComputeUsagesResponse](../../models/operations/listcomputeusagesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |