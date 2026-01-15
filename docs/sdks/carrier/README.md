# Carrier

## Overview

### Available Operations

* [get_shipping_carrier](#get_shipping_carrier) - Retrieve a carrier
* [list_shipping_carriers](#list_shipping_carriers) - List all carriers

## get_shipping_carrier

Retrieve a carrier

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingCarrier" method="get" path="/shipping/{connection_id}/carrier/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.carrier.get_shipping_carrier(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_carrier is not None

    # Handle response
    print(res.shipping_carrier)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetShippingCarrierRequest](../../models/operations/getshippingcarrierrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetShippingCarrierResponse](../../models/operations/getshippingcarrierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_carriers

List all carriers

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingCarriers" method="get" path="/shipping/{connection_id}/carrier" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.carrier.list_shipping_carriers(request={
        "connection_id": "<id>",
    })

    assert res.shipping_carriers is not None

    # Handle response
    print(res.shipping_carriers)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListShippingCarriersRequest](../../models/operations/listshippingcarriersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListShippingCarriersResponse](../../models/operations/listshippingcarriersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |