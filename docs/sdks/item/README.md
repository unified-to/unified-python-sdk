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
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "17a843d5-dd63-46c2-a51f-7115832f0f89",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "7b473a4a-ab24-4983-96af-2892c782e3c3",
                    "metadata": [
                        {
                            "id": "4008c157-3550-41e1-b6f5-417b1bfb3017",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/v73y0uzyK/3001/972",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "cfdb69e7-a7e0-4889-bc61-1c270821dd42",
                    "metadata": [
                        {
                            "id": "df38f10d-2809-4d78-b525-6b42b6e3728c",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "0c8a119c-bc7d-47bf-9b7b-3364cf7a6a9d",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "handcrafted-rubber-tuna",
            "tags": [
                "beatae",
                "blanditiis",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-04-24T21:42:50.472Z"),
            "vendor_name": "Mayer - Flatley",
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
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "968fccc8-8b1b-4c02-92eb-4ca0d8723639",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "2c0e825b-00dd-403b-8000-94e87cab3cd6",
                    "metadata": [
                        {
                            "id": "5c7f0111-725c-4aa5-b6da-d654bbb24405",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/v73y0uzyK/3001/972",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "c81b134b-c2e1-4bff-8c85-2b912cf8fe62",
                    "metadata": [
                        {
                            "id": "e36c551b-a445-4b93-a118-a6450a383488",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "5e7c901e-2e18-4ec5-940a-628f252bbc38",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "handcrafted-rubber-tuna",
            "tags": [
                "beatae",
                "blanditiis",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-04-24T21:42:50.482Z"),
            "vendor_name": "Mayer - Flatley",
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
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "968fccc8-8b1b-4c02-92eb-4ca0d8723639",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "2c0e825b-00dd-403b-8000-94e87cab3cd6",
                    "metadata": [
                        {
                            "id": "5c7f0111-725c-4aa5-b6da-d654bbb24405",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 21.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/v73y0uzyK/3001/972",
                    "width": 67.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 651.0,
                    "id": "c81b134b-c2e1-4bff-8c85-2b912cf8fe62",
                    "metadata": [
                        {
                            "id": "e36c551b-a445-4b93-a118-a6450a383488",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 51.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 3.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "5e7c901e-2e18-4ec5-940a-628f252bbc38",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "abstergo",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "currency": "USD",
                    "price": 78.11,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "handcrafted-rubber-tuna",
            "tags": [
                "beatae",
                "blanditiis",
            ],
            "total_stock": 682.0,
            "type": "SERVICE",
            "updated_at": parse_datetime("2022-04-24T21:42:50.482Z"),
            "vendor_name": "Mayer - Flatley",
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