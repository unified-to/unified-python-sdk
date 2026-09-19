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

Create an item

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
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "f524c64e-79c8-4157-8671-ff276ff91fd2",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "ec0aa835-01e3-45ea-92a4-ef27d65d23f9",
                    "metadata": [
                        {
                            "id": "5f8a36fa-40ce-4fed-b8f5-6709aa7a270d",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 67.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/73y0uzyK/972/3753",
                    "width": 88.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 189.0,
                    "id": "dd0fbbd6-c303-4062-8244-65286f001291",
                    "metadata": [
                        {
                            "id": "1bf11ed4-a05a-4de9-8b54-057f8d67a8c9",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 3.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 66.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "3c9dbed8-1cdd-4df4-8445-7edeb7976153",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "terebro",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "compare_at_price": 474.0,
                    "currency": "OMR",
                    "price": 1438.0,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "cohors-turba-optio",
            "tags": [
                "blanditiis",
                "tandem",
            ],
            "total_stock": 579.0,
            "type": "beatae",
            "updated_at": parse_datetime("2022-04-07T03:14:09.324Z"),
            "vendor_name": "Mayer - Flatley",
            "weight": 22.0,
            "weight_unit": shared.WeightUnit.KG,
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

Retrieve an item

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

List all items

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

Update an item

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
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "f40de5ca-c137-4131-8b91-5b8919566595",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "ca3fa487-495b-47ac-91bd-fd8c00207b9d",
                    "metadata": [
                        {
                            "id": "8681b6a4-d92c-46ae-b46c-c1cfb22349ba",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 67.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/73y0uzyK/972/3753",
                    "width": 88.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 189.0,
                    "id": "974c5ab9-4e5a-43f3-a3b6-09c7df786545",
                    "metadata": [
                        {
                            "id": "cfee8d02-ce66-45af-8294-7c9035ab65aa",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 3.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 66.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "7d958f7f-eeee-4f8c-a2a2-995d6c711a6e",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "terebro",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "compare_at_price": 474.0,
                    "currency": "OMR",
                    "price": 1438.0,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "cohors-turba-optio",
            "tags": [
                "blanditiis",
                "tandem",
            ],
            "total_stock": 579.0,
            "type": "beatae",
            "updated_at": parse_datetime("2022-04-07T03:14:09.342Z"),
            "vendor_name": "Mayer - Flatley",
            "weight": 22.0,
            "weight_unit": shared.WeightUnit.KG,
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

Remove an item

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

Update an item

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
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "f40de5ca-c137-4131-8b91-5b8919566595",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "ca3fa487-495b-47ac-91bd-fd8c00207b9d",
                    "metadata": [
                        {
                            "id": "8681b6a4-d92c-46ae-b46c-c1cfb22349ba",
                            "slug": "doloremque",
                            "value": "allatus",
                        },
                    ],
                    "position": 67.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/73y0uzyK/972/3753",
                    "width": 88.0,
                },
                {
                    "alt": "Comedo.",
                    "height": 189.0,
                    "id": "974c5ab9-4e5a-43f3-a3b6-09c7df786545",
                    "metadata": [
                        {
                            "id": "cfee8d02-ce66-45af-8294-7c9035ab65aa",
                            "slug": "bis",
                            "value": "somniculosus",
                        },
                    ],
                    "position": 3.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/Ao4iatfO/771/3906",
                    "width": 66.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "7d958f7f-eeee-4f8c-a2a2-995d6c711a6e",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "terebro",
                },
            ],
            "name": "Handcrafted Rubber Tuna",
            "prices": [
                {
                    "compare_at_price": 474.0,
                    "currency": "OMR",
                    "price": 1438.0,
                },
            ],
            "public_description": "Custodia ventus solio compono.",
            "public_name": "Handcrafted Rubber Tuna",
            "requires_shipping": True,
            "slug": "cohors-turba-optio",
            "tags": [
                "blanditiis",
                "tandem",
            ],
            "total_stock": 579.0,
            "type": "beatae",
            "updated_at": parse_datetime("2022-04-07T03:14:09.342Z"),
            "vendor_name": "Mayer - Flatley",
            "weight": 22.0,
            "weight_unit": shared.WeightUnit.KG,
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