# Itemvariant

## Overview

### Available Operations

* [create_commerce_itemvariant](#create_commerce_itemvariant) - Create an itemvariant
* [get_commerce_itemvariant](#get_commerce_itemvariant) - Retrieve an itemvariant
* [list_commerce_itemvariants](#list_commerce_itemvariants) - List all itemvariants
* [patch_commerce_itemvariant](#patch_commerce_itemvariant) - Update an itemvariant
* [remove_commerce_itemvariant](#remove_commerce_itemvariant) - Remove an itemvariant
* [update_commerce_itemvariant](#update_commerce_itemvariant) - Update an itemvariant

## create_commerce_itemvariant

Create an itemvariant

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceItemvariant" method="post" path="/commerce/{connection_id}/itemvariant" example="commerce_itemvariant" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.create_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "5c490591-d2a1-470c-a016-2a6bc92b5377",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "adbef15f-8a7d-4e18-9ef1-afe5f9510c49",
                    "metadata": [
                        {
                            "id": "1ccc71f9-b4b2-4a6b-a857-a85c5ebacefa",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 92.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/2007/3208",
                    "width": 54.0,
                },
                {
                    "alt": "Civitas acies substantia tergo.",
                    "height": 351.0,
                    "id": "c4f98acb-c50f-45a8-abab-3ea6a74d9a59",
                    "metadata": [
                        {
                            "id": "d3334b35-1a0e-44c0-a048-8e40794de17c",
                            "slug": "libero",
                            "value": "capitulus",
                        },
                    ],
                    "position": 44.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2230/1237?lock=8628070842159966",
                    "width": 55.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "06ff2d54-be89-434e-a272-0cb2cfa18c70",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "f889225a-cbca-42ae-b96c-aa0e18aabed0",
                    "name": "Steel",
                    "position": 97.0,
                    "values": [
                        "Granite",
                        "Plastic",
                    ],
                },
            ],
            "prices": [
                {
                    "compare_at_price": 3745.0,
                    "currency": "COP",
                    "price": 4913.0,
                },
                {
                    "compare_at_price": 438.0,
                    "currency": "PHP",
                    "price": 1378.0,
                },
                {
                    "compare_at_price": 1614.0,
                    "currency": "PHP",
                    "price": 8702.0,
                },
            ],
            "public_description": "Stylish Soap designed to make you stand out with insistent looks",
            "public_name": "Keyboard",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-0-7051-0955-0",
            "tags": [
                "vomito",
                "custodia",
            ],
            "total_stock": 929.0,
            "updated_at": parse_datetime("2025-06-09T21:37:46.891Z"),
            "weight": 61.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 26.0,
        },
        "connection_id": "<id>",
    })

    assert res.commerce_itemvariant is not None

    # Handle response
    print(res.commerce_itemvariant)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateCommerceItemvariantRequest](../../models/operations/createcommerceitemvariantrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreateCommerceItemvariantResponse](../../models/operations/createcommerceitemvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_itemvariant

Retrieve an itemvariant

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceItemvariant" method="get" path="/commerce/{connection_id}/itemvariant/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.get_commerce_itemvariant(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_itemvariant is not None

    # Handle response
    print(res.commerce_itemvariant)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCommerceItemvariantRequest](../../models/operations/getcommerceitemvariantrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetCommerceItemvariantResponse](../../models/operations/getcommerceitemvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_itemvariants

List all itemvariants

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceItemvariants" method="get" path="/commerce/{connection_id}/itemvariant" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.list_commerce_itemvariants(request={
        "connection_id": "<id>",
    })

    assert res.commerce_itemvariants is not None

    # Handle response
    print(res.commerce_itemvariants)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListCommerceItemvariantsRequest](../../models/operations/listcommerceitemvariantsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListCommerceItemvariantsResponse](../../models/operations/listcommerceitemvariantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_itemvariant

Update an itemvariant

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceItemvariant" method="patch" path="/commerce/{connection_id}/itemvariant/{id}" example="commerce_itemvariant" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.patch_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "1e16a20d-5b27-4741-9336-be01a198bdf4",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "63a8cf91-9c6f-44cf-8407-0d091259559d",
                    "metadata": [
                        {
                            "id": "4d748301-86bc-4b80-a72a-df88546c9736",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 92.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/2007/3208",
                    "width": 54.0,
                },
                {
                    "alt": "Civitas acies substantia tergo.",
                    "height": 351.0,
                    "id": "a7773b2c-5552-4ffe-b159-ae2a43fd49ca",
                    "metadata": [
                        {
                            "id": "60134ea9-6179-4a4a-b2d3-9d1de0c36de0",
                            "slug": "libero",
                            "value": "capitulus",
                        },
                    ],
                    "position": 44.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2230/1237?lock=8628070842159966",
                    "width": 55.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "8a751d96-7b45-4f96-b698-b05f80be5677",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "2909b676-0d4a-4229-bc9a-1fa00cffb292",
                    "name": "Steel",
                    "position": 97.0,
                    "values": [
                        "Granite",
                        "Plastic",
                    ],
                },
            ],
            "prices": [
                {
                    "compare_at_price": 3745.0,
                    "currency": "COP",
                    "price": 4913.0,
                },
                {
                    "compare_at_price": 438.0,
                    "currency": "PHP",
                    "price": 1378.0,
                },
                {
                    "compare_at_price": 1614.0,
                    "currency": "PHP",
                    "price": 8702.0,
                },
            ],
            "public_description": "Stylish Soap designed to make you stand out with insistent looks",
            "public_name": "Keyboard",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-0-7051-0955-0",
            "tags": [
                "vomito",
                "custodia",
            ],
            "total_stock": 929.0,
            "updated_at": parse_datetime("2025-06-09T21:37:46.912Z"),
            "weight": 61.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 26.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_itemvariant is not None

    # Handle response
    print(res.commerce_itemvariant)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchCommerceItemvariantRequest](../../models/operations/patchcommerceitemvariantrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PatchCommerceItemvariantResponse](../../models/operations/patchcommerceitemvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_itemvariant

Remove an itemvariant

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceItemvariant" method="delete" path="/commerce/{connection_id}/itemvariant/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.remove_commerce_itemvariant(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveCommerceItemvariantRequest](../../models/operations/removecommerceitemvariantrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.RemoveCommerceItemvariantResponse](../../models/operations/removecommerceitemvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_itemvariant

Update an itemvariant

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceItemvariant" method="put" path="/commerce/{connection_id}/itemvariant/{id}" example="commerce_itemvariant" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.itemvariant.update_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "1e16a20d-5b27-4741-9336-be01a198bdf4",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "63a8cf91-9c6f-44cf-8407-0d091259559d",
                    "metadata": [
                        {
                            "id": "4d748301-86bc-4b80-a72a-df88546c9736",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 92.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/2007/3208",
                    "width": 54.0,
                },
                {
                    "alt": "Civitas acies substantia tergo.",
                    "height": 351.0,
                    "id": "a7773b2c-5552-4ffe-b159-ae2a43fd49ca",
                    "metadata": [
                        {
                            "id": "60134ea9-6179-4a4a-b2d3-9d1de0c36de0",
                            "slug": "libero",
                            "value": "capitulus",
                        },
                    ],
                    "position": 44.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2230/1237?lock=8628070842159966",
                    "width": 55.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "8a751d96-7b45-4f96-b698-b05f80be5677",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "2909b676-0d4a-4229-bc9a-1fa00cffb292",
                    "name": "Steel",
                    "position": 97.0,
                    "values": [
                        "Granite",
                        "Plastic",
                    ],
                },
            ],
            "prices": [
                {
                    "compare_at_price": 3745.0,
                    "currency": "COP",
                    "price": 4913.0,
                },
                {
                    "compare_at_price": 438.0,
                    "currency": "PHP",
                    "price": 1378.0,
                },
                {
                    "compare_at_price": 1614.0,
                    "currency": "PHP",
                    "price": 8702.0,
                },
            ],
            "public_description": "Stylish Soap designed to make you stand out with insistent looks",
            "public_name": "Keyboard",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-0-7051-0955-0",
            "tags": [
                "vomito",
                "custodia",
            ],
            "total_stock": 929.0,
            "updated_at": parse_datetime("2025-06-09T21:37:46.912Z"),
            "weight": 61.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 26.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_itemvariant is not None

    # Handle response
    print(res.commerce_itemvariant)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateCommerceItemvariantRequest](../../models/operations/updatecommerceitemvariantrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdateCommerceItemvariantResponse](../../models/operations/updatecommerceitemvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |