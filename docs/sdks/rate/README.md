# Rate

## Overview

### Available Operations

* [create_shipping_rate](#create_shipping_rate) - Create a rate

## create_shipping_rate

Creates a ShippingRate. Provide the unified ShippingRate fields in the request body; they are mapped to the provider's API. Returns the created ShippingRate.

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingRate" method="post" path="/shipping/{connection_id}/rate" example="shipping_rate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.rate.create_shipping_rate(request={
        "shipping_rate": {
            "currency": "USD",
            "id": "b7f74658-eaed-4189-84c3-80b2f8d9044f",
            "metadata": [],
            "rates": [
                {
                    "amount": 44.72,
                    "base_amount": 46.01,
                    "currency": "USD",
                    "delivery_days": 2.0,
                    "description": "Veniam denego vulgo bos turpis pax.",
                    "discount_amount": 4.6,
                    "estimated_days": 2.0,
                    "estimated_delivery_end_at": parse_datetime("2021-09-03T01:03:36.021Z"),
                    "is_negotiated_rate": True,
                    "tax_amount": 3.31,
                    "title": "Express",
                },
            ],
        },
        "connection_id": "<id>",
    })

    assert res.shipping_rate is not None

    # Handle response
    print(res.shipping_rate)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateShippingRateRequest](../../models/operations/createshippingraterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateShippingRateResponse](../../models/operations/createshippingrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |