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
            "id": "41d7eebd-d447-45fb-8b37-ede133592538",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "b5d9f924-beaf-4c8b-a1c1-4b0a30f58906",
                    "metadata": [
                        {
                            "id": "0d81242f-a73d-44ee-9675-36c63bdf9605",
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
                    "id": "6783982c-bcf4-42e7-a8e4-50970c361f1a",
                    "metadata": [
                        {
                            "id": "4003197f-7efd-48f5-92a6-3d274fbb99d6",
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
                    "id": "956e98d7-c54f-47f8-a31f-c962db726e1a",
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
            "updated_at": parse_datetime("2022-04-15T15:31:50.670Z"),
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
            "id": "c8bf1dc0-b5a4-4c28-a8bd-60c5d56d7a88",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "e342898e-b8ff-4270-ad55-91b834b0cf94",
                    "metadata": [
                        {
                            "id": "3396bd5d-1f0c-4687-88be-4eb978a9f097",
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
                    "id": "21a77d36-4126-4aac-b304-9557a09f9167",
                    "metadata": [
                        {
                            "id": "c2efc8e7-3cc7-4873-8959-ca90b5198730",
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
                    "id": "91a1b635-18dc-40b0-99ba-d329dd0179ca",
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
            "updated_at": parse_datetime("2022-04-15T15:31:50.680Z"),
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
            "id": "c8bf1dc0-b5a4-4c28-a8bd-60c5d56d7a88",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "e342898e-b8ff-4270-ad55-91b834b0cf94",
                    "metadata": [
                        {
                            "id": "3396bd5d-1f0c-4687-88be-4eb978a9f097",
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
                    "id": "21a77d36-4126-4aac-b304-9557a09f9167",
                    "metadata": [
                        {
                            "id": "c2efc8e7-3cc7-4873-8959-ca90b5198730",
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
                    "id": "91a1b635-18dc-40b0-99ba-d329dd0179ca",
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
            "updated_at": parse_datetime("2022-04-15T15:31:50.680Z"),
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