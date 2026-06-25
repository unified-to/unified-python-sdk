# Label

## Overview

### Available Operations

* [create_shipping_label2](#create_shipping_label2) - Create a label
* [get_shipping_label2](#get_shipping_label2) - Retrieve a label
* [list_shipping_labels2](#list_shipping_labels2) - List all labels
* [patch_shipping_label2](#patch_shipping_label2) - Update a label
* [remove_shipping_label2](#remove_shipping_label2) - Remove a label
* [update_shipping_label2](#update_shipping_label2) - Update a label

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

    res = unified_to.label.create_shipping_label2(request={
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

    res = unified_to.label.get_shipping_label2(request={
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

    res = unified_to.label.list_shipping_labels2(request={
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

    res = unified_to.label.patch_shipping_label2(request={
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

    res = unified_to.label.remove_shipping_label2(request={
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

    res = unified_to.label.update_shipping_label2(request={
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