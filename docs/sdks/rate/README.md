# Rate

## Overview

### Available Operations

* [create_shipping_rate2](#create_shipping_rate2) - Create a rate

## create_shipping_rate2

Create a rate

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingRate2" method="post" path="/shipping/{connection_id}/rate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.rate.create_shipping_rate2(request={
        "shipping_rate": {},
        "connection_id": "<id>",
    })

    assert res.shipping_rate is not None

    # Handle response
    print(res.shipping_rate)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateShippingRate2Request](../../models/operations/createshippingrate2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateShippingRate2Response](../../models/operations/createshippingrate2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |