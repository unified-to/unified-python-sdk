# Availability

## Overview

### Available Operations

* [list_commerce_availabilities2](#list_commerce_availabilities2) - List all availabilities

## list_commerce_availabilities2

List all availabilities

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceAvailabilities2" method="get" path="/commerce/{connection_id}/availability" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.availability.list_commerce_availabilities2(request={
        "connection_id": "<id>",
    })

    assert res.commerce_availabilities is not None

    # Handle response
    print(res.commerce_availabilities)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListCommerceAvailabilities2Request](../../models/operations/listcommerceavailabilities2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListCommerceAvailabilities2Response](../../models/operations/listcommerceavailabilities2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |