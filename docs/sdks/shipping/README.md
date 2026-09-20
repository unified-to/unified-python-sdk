# Shipping

## Overview

### Available Operations

* [create_shipping_label](#create_shipping_label) - Create a label
* [create_shipping_rate](#create_shipping_rate) - Create a rate
* [create_shipping_shipment](#create_shipping_shipment) - Create a shipment
* [get_shipping_carrier](#get_shipping_carrier) - Retrieve a carrier
* [get_shipping_label](#get_shipping_label) - Retrieve a label
* [get_shipping_shipment](#get_shipping_shipment) - Retrieve a shipment
* [get_shipping_tracking](#get_shipping_tracking) - Retrieve a tracking
* [list_shipping_carriers](#list_shipping_carriers) - List all carriers
* [list_shipping_labels](#list_shipping_labels) - List all labels
* [list_shipping_shipments](#list_shipping_shipments) - List all shipments
* [list_shipping_trackings](#list_shipping_trackings) - List all trackings
* [patch_shipping_label](#patch_shipping_label) - Update a label
* [patch_shipping_shipment](#patch_shipping_shipment) - Update a shipment
* [remove_shipping_label](#remove_shipping_label) - Remove a label
* [remove_shipping_shipment](#remove_shipping_shipment) - Remove a shipment
* [update_shipping_label](#update_shipping_label) - Update a label
* [update_shipping_shipment](#update_shipping_shipment) - Update a shipment

## create_shipping_label

Create a label

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingLabel" method="post" path="/shipping/{connection_id}/label" example="shipping_label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.create_shipping_label(request={
        "shipping_label": {
            "created_at": parse_datetime("2022-11-18T16:45:38.067Z"),
            "id": "b2aded1f-7596-4303-8a09-ceed7300ecd7",
            "is_voided": False,
            "label_cost": 40.83653403213248,
            "label_cost_currency": "USD",
            "label_format": shared.LabelFormat.PNG,
            "label_url": "https://optimal-meadow.net",
            "service_code": "GIz",
            "status": shared.ShippingLabelStatus.EXCEPTION,
            "tracking_number": "zYv60FOIBUJ6",
            "updated_at": parse_datetime("2024-04-17T05:57:43.685Z"),
        },
        "connection_id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateShippingLabelRequest](../../models/operations/createshippinglabelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateShippingLabelResponse](../../models/operations/createshippinglabelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.shipping.create_shipping_rate(request={
        "shipping_rate": {
            "currency": "USD",
            "id": "52b7ebb3-d2c2-4908-9a7c-fb74016a2c27",
            "rates": [
                {
                    "amount": 54.679719475097954,
                    "base_amount": 76.45537888631225,
                    "currency": "USD",
                    "delivery_days": 8.0,
                    "description": "Bos turpis pax amet dolorem sufficio demonstro complectus benevolentia rerum.",
                    "estimated_days": 10.0,
                    "estimated_delivery_end_at": parse_datetime("2024-02-01T14:18:25.664Z"),
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

## create_shipping_shipment

Create a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingShipment" method="post" path="/shipping/{connection_id}/shipment" example="shipping_shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.create_shipping_shipment(request={
        "shipping_shipment": {
            "carrier_name": "Bogisich, Franey and Koelpin",
            "created_at": parse_datetime("2022-09-12T03:11:28.960Z"),
            "id": "4750832a-4eff-4b48-932e-e1e873baf666",
            "rate_amount": 8.86546263936907,
            "rate_currency": "USD",
            "rate_estimated_days": 8.0,
            "rate_service_name": "Fisher - Kilback",
            "service_code": "F7U",
            "shipped_at": parse_datetime("2025-08-25T17:31:33.336Z"),
            "status": shared.ShippingShipmentStatus.PENDING,
            "tracking_url": "https://shallow-secrecy.info/",
            "updated_at": parse_datetime("2025-07-04T00:10:36.701Z"),
        },
        "connection_id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateShippingShipmentRequest](../../models/operations/createshippingshipmentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateShippingShipmentResponse](../../models/operations/createshippingshipmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.shipping.get_shipping_carrier(request={
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

## get_shipping_label

Retrieve a label

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingLabel" method="get" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.get_shipping_label(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetShippingLabelRequest](../../models/operations/getshippinglabelrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetShippingLabelResponse](../../models/operations/getshippinglabelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_shipping_shipment

Retrieve a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingShipment" method="get" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.get_shipping_shipment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetShippingShipmentRequest](../../models/operations/getshippingshipmentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetShippingShipmentResponse](../../models/operations/getshippingshipmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.shipping.get_shipping_tracking(request={
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

    res = unified_to.shipping.list_shipping_carriers(request={
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

## list_shipping_labels

List all labels

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingLabels" method="get" path="/shipping/{connection_id}/label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_labels(request={
        "connection_id": "<id>",
    })

    assert res.shipping_labels is not None

    # Handle response
    print(res.shipping_labels)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListShippingLabelsRequest](../../models/operations/listshippinglabelsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListShippingLabelsResponse](../../models/operations/listshippinglabelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_shipments

List all shipments

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingShipments" method="get" path="/shipping/{connection_id}/shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_shipments(request={
        "connection_id": "<id>",
    })

    assert res.shipping_shipments is not None

    # Handle response
    print(res.shipping_shipments)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListShippingShipmentsRequest](../../models/operations/listshippingshipmentsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListShippingShipmentsResponse](../../models/operations/listshippingshipmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_trackings

List all trackings

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingTrackings" method="get" path="/shipping/{connection_id}/tracking" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_trackings(request={
        "connection_id": "<id>",
    })

    assert res.shipping_trackings is not None

    # Handle response
    print(res.shipping_trackings)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListShippingTrackingsRequest](../../models/operations/listshippingtrackingsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListShippingTrackingsResponse](../../models/operations/listshippingtrackingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_shipping_label

Update a label

### Example Usage

<!-- UsageSnippet language="python" operationID="patchShippingLabel" method="patch" path="/shipping/{connection_id}/label/{id}" example="shipping_label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.patch_shipping_label(request={
        "shipping_label": {
            "created_at": parse_datetime("2022-11-18T16:45:38.067Z"),
            "id": "c77e74ea-c43b-4233-b195-c7a213fbc4e8",
            "is_voided": False,
            "label_cost": 40.83653403213248,
            "label_cost_currency": "USD",
            "label_format": shared.LabelFormat.PNG,
            "label_url": "https://optimal-meadow.net",
            "service_code": "GIz",
            "status": shared.ShippingLabelStatus.EXCEPTION,
            "tracking_number": "zYv60FOIBUJ6",
            "updated_at": parse_datetime("2024-04-17T05:57:43.690Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchShippingLabelRequest](../../models/operations/patchshippinglabelrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchShippingLabelResponse](../../models/operations/patchshippinglabelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_shipping_shipment

Update a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchShippingShipment" method="patch" path="/shipping/{connection_id}/shipment/{id}" example="shipping_shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.patch_shipping_shipment(request={
        "shipping_shipment": {
            "carrier_name": "Bogisich, Franey and Koelpin",
            "created_at": parse_datetime("2022-09-12T03:11:28.960Z"),
            "id": "89f7b1ce-2091-482b-bc47-adc643dab6ff",
            "rate_amount": 8.86546263936907,
            "rate_currency": "USD",
            "rate_estimated_days": 8.0,
            "rate_service_name": "Fisher - Kilback",
            "service_code": "F7U",
            "shipped_at": parse_datetime("2025-08-25T17:31:33.410Z"),
            "status": shared.ShippingShipmentStatus.PENDING,
            "tracking_url": "https://shallow-secrecy.info/",
            "updated_at": parse_datetime("2025-07-04T00:10:36.772Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchShippingShipmentRequest](../../models/operations/patchshippingshipmentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchShippingShipmentResponse](../../models/operations/patchshippingshipmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_shipping_label

Remove a label

### Example Usage

<!-- UsageSnippet language="python" operationID="removeShippingLabel" method="delete" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.remove_shipping_label(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveShippingLabelRequest](../../models/operations/removeshippinglabelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveShippingLabelResponse](../../models/operations/removeshippinglabelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_shipping_shipment

Remove a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="removeShippingShipment" method="delete" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.remove_shipping_shipment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveShippingShipmentRequest](../../models/operations/removeshippingshipmentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveShippingShipmentResponse](../../models/operations/removeshippingshipmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_shipping_label

Update a label

### Example Usage

<!-- UsageSnippet language="python" operationID="updateShippingLabel" method="put" path="/shipping/{connection_id}/label/{id}" example="shipping_label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.update_shipping_label(request={
        "shipping_label": {
            "created_at": parse_datetime("2022-11-18T16:45:38.067Z"),
            "id": "c77e74ea-c43b-4233-b195-c7a213fbc4e8",
            "is_voided": False,
            "label_cost": 40.83653403213248,
            "label_cost_currency": "USD",
            "label_format": shared.LabelFormat.PNG,
            "label_url": "https://optimal-meadow.net",
            "service_code": "GIz",
            "status": shared.ShippingLabelStatus.EXCEPTION,
            "tracking_number": "zYv60FOIBUJ6",
            "updated_at": parse_datetime("2024-04-17T05:57:43.690Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateShippingLabelRequest](../../models/operations/updateshippinglabelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateShippingLabelResponse](../../models/operations/updateshippinglabelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_shipping_shipment

Update a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="updateShippingShipment" method="put" path="/shipping/{connection_id}/shipment/{id}" example="shipping_shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.update_shipping_shipment(request={
        "shipping_shipment": {
            "carrier_name": "Bogisich, Franey and Koelpin",
            "created_at": parse_datetime("2022-09-12T03:11:28.960Z"),
            "id": "89f7b1ce-2091-482b-bc47-adc643dab6ff",
            "rate_amount": 8.86546263936907,
            "rate_currency": "USD",
            "rate_estimated_days": 8.0,
            "rate_service_name": "Fisher - Kilback",
            "service_code": "F7U",
            "shipped_at": parse_datetime("2025-08-25T17:31:33.410Z"),
            "status": shared.ShippingShipmentStatus.PENDING,
            "tracking_url": "https://shallow-secrecy.info/",
            "updated_at": parse_datetime("2025-07-04T00:10:36.772Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateShippingShipmentRequest](../../models/operations/updateshippingshipmentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateShippingShipmentResponse](../../models/operations/updateshippingshipmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |