# Rate

## Overview

### Available Operations

* [create_shipping_rate](#create_shipping_rate) - Create a rate

## create_shipping_rate

Create a rate

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
            "id": "879f40c7-6f54-4e02-97dc-cdfe88df4e1a",
            "rates": [
                {
                    "amount": 54.679719475097954,
                    "base_amount": 76.45537888631225,
                    "currency": "USD",
                    "delivery_days": 8.0,
                    "description": "Bos turpis pax amet dolorem sufficio demonstro complectus benevolentia rerum.",
                    "estimated_days": 10.0,
                    "estimated_delivery_end_at": parse_datetime("2024-02-02T07:19:52.185Z"),
                    "is_guaranteed": True,
                    "is_negotiated_rate": True,
                    "tax_amount": 2.2701712837442756,
                    "title": "Turcotte Inc",
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