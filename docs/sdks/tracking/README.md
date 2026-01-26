# Tracking

## Overview

### Available Operations

* [get_shipping_tracking](#get_shipping_tracking) - Retrieve a tracking

## get_shipping_tracking

Retrieve a tracking

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingTracking" method="get" path="/shipping/{connection_id}/tracking/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.tracking.get_shipping_tracking(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_tracking is not None

    # Handle response
    print(res.shipping_tracking)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetShippingTrackingRequest](../../models/operations/getshippingtrackingrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetShippingTrackingResponse](../../models/operations/getshippingtrackingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |