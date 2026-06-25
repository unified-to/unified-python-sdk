# Tracking

## Overview

### Available Operations

* [get_shipping_tracking2](#get_shipping_tracking2) - Retrieve a tracking
* [list_shipping_trackings2](#list_shipping_trackings2) - List all trackings

## get_shipping_tracking2

Retrieve a tracking

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingTracking2" method="get" path="/shipping/{connection_id}/tracking/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.tracking.get_shipping_tracking2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_tracking is not None

    # Handle response
    print(res.shipping_tracking)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetShippingTracking2Request](../../models/operations/getshippingtracking2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetShippingTracking2Response](../../models/operations/getshippingtracking2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_trackings2

List all trackings

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingTrackings2" method="get" path="/shipping/{connection_id}/tracking" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.tracking.list_shipping_trackings2(request={
        "connection_id": "<id>",
    })

    assert res.shipping_trackings is not None

    # Handle response
    print(res.shipping_trackings)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListShippingTrackings2Request](../../models/operations/listshippingtrackings2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListShippingTrackings2Response](../../models/operations/listshippingtrackings2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |