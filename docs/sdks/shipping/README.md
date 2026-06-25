# Shipping

## Overview

### Available Operations

* [create_shipping_label2](#create_shipping_label2) - Create a label
* [create_shipping_rate2](#create_shipping_rate2) - Create a rate
* [create_shipping_shipment2](#create_shipping_shipment2) - Create a shipment
* [get_shipping_carrier2](#get_shipping_carrier2) - Retrieve a carrier
* [get_shipping_label2](#get_shipping_label2) - Retrieve a label
* [get_shipping_shipment2](#get_shipping_shipment2) - Retrieve a shipment
* [get_shipping_tracking2](#get_shipping_tracking2) - Retrieve a tracking
* [list_shipping_carriers2](#list_shipping_carriers2) - List all carriers
* [list_shipping_labels2](#list_shipping_labels2) - List all labels
* [list_shipping_shipments2](#list_shipping_shipments2) - List all shipments
* [list_shipping_trackings2](#list_shipping_trackings2) - List all trackings
* [patch_shipping_label2](#patch_shipping_label2) - Update a label
* [patch_shipping_shipment2](#patch_shipping_shipment2) - Update a shipment
* [remove_shipping_label2](#remove_shipping_label2) - Remove a label
* [remove_shipping_shipment2](#remove_shipping_shipment2) - Remove a shipment
* [update_shipping_label2](#update_shipping_label2) - Update a label
* [update_shipping_shipment2](#update_shipping_shipment2) - Update a shipment

## create_shipping_label2

Create a label

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingLabel2" method="post" path="/shipping/{connection_id}/label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.create_shipping_label2(request={
        "shipping_label": {},
        "connection_id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateShippingLabel2Request](../../models/operations/createshippinglabel2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateShippingLabel2Response](../../models/operations/createshippinglabel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.shipping.create_shipping_rate2(request={
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

## create_shipping_shipment2

Create a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="createShippingShipment2" method="post" path="/shipping/{connection_id}/shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.create_shipping_shipment2(request={
        "shipping_shipment": {},
        "connection_id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateShippingShipment2Request](../../models/operations/createshippingshipment2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateShippingShipment2Response](../../models/operations/createshippingshipment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_shipping_carrier2

Retrieve a carrier

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingCarrier2" method="get" path="/shipping/{connection_id}/carrier/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.get_shipping_carrier2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_carrier is not None

    # Handle response
    print(res.shipping_carrier)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetShippingCarrier2Request](../../models/operations/getshippingcarrier2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetShippingCarrier2Response](../../models/operations/getshippingcarrier2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_shipping_label2

Retrieve a label

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingLabel2" method="get" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.get_shipping_label2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetShippingLabel2Request](../../models/operations/getshippinglabel2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetShippingLabel2Response](../../models/operations/getshippinglabel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_shipping_shipment2

Retrieve a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="getShippingShipment2" method="get" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.get_shipping_shipment2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetShippingShipment2Request](../../models/operations/getshippingshipment2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetShippingShipment2Response](../../models/operations/getshippingshipment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.shipping.get_shipping_tracking2(request={
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

## list_shipping_carriers2

List all carriers

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingCarriers2" method="get" path="/shipping/{connection_id}/carrier" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_carriers2(request={
        "connection_id": "<id>",
    })

    assert res.shipping_carriers is not None

    # Handle response
    print(res.shipping_carriers)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListShippingCarriers2Request](../../models/operations/listshippingcarriers2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListShippingCarriers2Response](../../models/operations/listshippingcarriers2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_labels2

List all labels

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingLabels2" method="get" path="/shipping/{connection_id}/label" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_labels2(request={
        "connection_id": "<id>",
    })

    assert res.shipping_labels is not None

    # Handle response
    print(res.shipping_labels)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListShippingLabels2Request](../../models/operations/listshippinglabels2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListShippingLabels2Response](../../models/operations/listshippinglabels2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_shipping_shipments2

List all shipments

### Example Usage

<!-- UsageSnippet language="python" operationID="listShippingShipments2" method="get" path="/shipping/{connection_id}/shipment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.list_shipping_shipments2(request={
        "connection_id": "<id>",
    })

    assert res.shipping_shipments is not None

    # Handle response
    print(res.shipping_shipments)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListShippingShipments2Request](../../models/operations/listshippingshipments2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListShippingShipments2Response](../../models/operations/listshippingshipments2response.md)**

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

    res = unified_to.shipping.list_shipping_trackings2(request={
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

## patch_shipping_label2

Update a label

### Example Usage

<!-- UsageSnippet language="python" operationID="patchShippingLabel2" method="patch" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.patch_shipping_label2(request={
        "shipping_label": {},
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
| `request`                                                                                      | [operations.PatchShippingLabel2Request](../../models/operations/patchshippinglabel2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchShippingLabel2Response](../../models/operations/patchshippinglabel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_shipping_shipment2

Update a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchShippingShipment2" method="patch" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.patch_shipping_shipment2(request={
        "shipping_shipment": {},
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
| `request`                                                                                            | [operations.PatchShippingShipment2Request](../../models/operations/patchshippingshipment2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchShippingShipment2Response](../../models/operations/patchshippingshipment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_shipping_label2

Remove a label

### Example Usage

<!-- UsageSnippet language="python" operationID="removeShippingLabel2" method="delete" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.remove_shipping_label2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveShippingLabel2Request](../../models/operations/removeshippinglabel2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveShippingLabel2Response](../../models/operations/removeshippinglabel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_shipping_shipment2

Remove a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="removeShippingShipment2" method="delete" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.remove_shipping_shipment2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveShippingShipment2Request](../../models/operations/removeshippingshipment2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveShippingShipment2Response](../../models/operations/removeshippingshipment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_shipping_label2

Update a label

### Example Usage

<!-- UsageSnippet language="python" operationID="updateShippingLabel2" method="put" path="/shipping/{connection_id}/label/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.update_shipping_label2(request={
        "shipping_label": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_label is not None

    # Handle response
    print(res.shipping_label)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateShippingLabel2Request](../../models/operations/updateshippinglabel2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateShippingLabel2Response](../../models/operations/updateshippinglabel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_shipping_shipment2

Update a shipment

### Example Usage

<!-- UsageSnippet language="python" operationID="updateShippingShipment2" method="put" path="/shipping/{connection_id}/shipment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.shipping.update_shipping_shipment2(request={
        "shipping_shipment": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.shipping_shipment is not None

    # Handle response
    print(res.shipping_shipment)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateShippingShipment2Request](../../models/operations/updateshippingshipment2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateShippingShipment2Response](../../models/operations/updateshippingshipment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |