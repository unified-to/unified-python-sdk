# Item

## Overview

### Available Operations

* [create_commerce_item](#create_commerce_item) - Create an item
* [get_commerce_item](#get_commerce_item) - Retrieve an item
* [list_commerce_items](#list_commerce_items) - List all items
* [patch_commerce_item](#patch_commerce_item) - Update an item
* [remove_commerce_item](#remove_commerce_item) - Remove an item
* [update_commerce_item](#update_commerce_item) - Update an item

## create_commerce_item

Creates a CommerceItem. Provide the unified CommerceItem fields in the request body; they are mapped to the provider's API. Returns the created CommerceItem.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceItem" method="post" path="/commerce/{connection_id}/item" example="commerce_item" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.create_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Abeo surculus custodia ventus solio.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "3429677e-7b05-4786-9bac-ef6f59b6f6b7",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Eveniet acies.",
                    "height": 876.0,
                    "id": "56f386e2-98dc-434b-b1ad-9e1488b53bed",
                    "metadata": [
                        {
                            "id": "76cc78fc-661c-4c74-bd3a-7b84f26c8dcf",
                            "slug": "candidus",
                            "value": "doloremque",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/uzyKI/235/2194",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "bae11f2c-3b1d-416b-b851-21e8879e57ed",
                    "metadata": [
                        {
                            "id": "b727375f-08f5-4a84-aa5f-f84c61a5b371",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/NFAo4iatfO/383/771",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "81f6216f-e4f4-4eb6-9406-81169f1c51a8",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Oriental Gold Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Adfero neque.",
            "public_name": "Oriental Gold Tuna",
            "requires_shipping": True,
            "slug": "oriental-gold-tuna",
            "tags": [
                "dolores",
                "amplus",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-05-04T03:48:52.616Z"),
            "vendor_name": "Rohan - Pouros",
            "weight": 37.0,
            "weight_unit": shared.WeightUnit.OZ,
        },
        "connection_id": "<id>",
    })

    assert res.commerce_item is not None

    # Handle response
    print(res.commerce_item)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCommerceItemRequest](../../models/operations/createcommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateCommerceItemResponse](../../models/operations/createcommerceitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_item

Retrieves a single CommerceItem by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceItem" method="get" path="/commerce/{connection_id}/item/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.get_commerce_item(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_item is not None

    # Handle response
    print(res.commerce_item)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCommerceItemRequest](../../models/operations/getcommerceitemrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetCommerceItemResponse](../../models/operations/getcommerceitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_items

Returns a list of CommerceItems. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceItems" method="get" path="/commerce/{connection_id}/item" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.list_commerce_items(request={
        "connection_id": "<id>",
    })

    assert res.commerce_items is not None

    # Handle response
    print(res.commerce_items)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCommerceItemsRequest](../../models/operations/listcommerceitemsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListCommerceItemsResponse](../../models/operations/listcommerceitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_item

Updates the CommerceItem identified by `id`. Provide the unified CommerceItem fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceItem" method="patch" path="/commerce/{connection_id}/item/{id}" example="commerce_item" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.patch_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Abeo surculus custodia ventus solio.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "86163823-b418-43f5-a8bc-d88049a01557",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Eveniet acies.",
                    "height": 876.0,
                    "id": "0fc62cdf-0603-4b34-955e-48988057adb2",
                    "metadata": [
                        {
                            "id": "0536c10d-cd72-41c4-8935-75ae0529ab90",
                            "slug": "candidus",
                            "value": "doloremque",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/uzyKI/235/2194",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "0aa139ef-ffe3-45a9-80b1-e55cdf5c124b",
                    "metadata": [
                        {
                            "id": "9e9c2343-7c3d-4d90-b0eb-7c138c64ade0",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/NFAo4iatfO/383/771",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "1457e44b-630f-4a93-b3e3-6f908dcbda5c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Oriental Gold Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Adfero neque.",
            "public_name": "Oriental Gold Tuna",
            "requires_shipping": True,
            "slug": "oriental-gold-tuna",
            "tags": [
                "dolores",
                "amplus",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-05-04T03:48:52.631Z"),
            "vendor_name": "Rohan - Pouros",
            "weight": 37.0,
            "weight_unit": shared.WeightUnit.OZ,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_item is not None

    # Handle response
    print(res.commerce_item)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCommerceItemRequest](../../models/operations/patchcommerceitemrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchCommerceItemResponse](../../models/operations/patchcommerceitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_item

Deletes the CommerceItem identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceItem" method="delete" path="/commerce/{connection_id}/item/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.remove_commerce_item(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCommerceItemRequest](../../models/operations/removecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveCommerceItemResponse](../../models/operations/removecommerceitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_item

Updates the CommerceItem identified by `id`. Provide the unified CommerceItem fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceItem" method="put" path="/commerce/{connection_id}/item/{id}" example="commerce_item" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.item.update_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Abeo surculus custodia ventus solio.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "86163823-b418-43f5-a8bc-d88049a01557",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Eveniet acies.",
                    "height": 876.0,
                    "id": "0fc62cdf-0603-4b34-955e-48988057adb2",
                    "metadata": [
                        {
                            "id": "0536c10d-cd72-41c4-8935-75ae0529ab90",
                            "slug": "candidus",
                            "value": "doloremque",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/uzyKI/235/2194",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "0aa139ef-ffe3-45a9-80b1-e55cdf5c124b",
                    "metadata": [
                        {
                            "id": "9e9c2343-7c3d-4d90-b0eb-7c138c64ade0",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/NFAo4iatfO/383/771",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "1457e44b-630f-4a93-b3e3-6f908dcbda5c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Oriental Gold Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Adfero neque.",
            "public_name": "Oriental Gold Tuna",
            "requires_shipping": True,
            "slug": "oriental-gold-tuna",
            "tags": [
                "dolores",
                "amplus",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-05-04T03:48:52.631Z"),
            "vendor_name": "Rohan - Pouros",
            "weight": 37.0,
            "weight_unit": shared.WeightUnit.OZ,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_item is not None

    # Handle response
    print(res.commerce_item)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCommerceItemRequest](../../models/operations/updatecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateCommerceItemResponse](../../models/operations/updatecommerceitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |