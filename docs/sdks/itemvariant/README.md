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
            "id": "97298d3f-f688-41d8-a794-7d17faabf6f2",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "7d7fb8ac-fb11-46d7-98f3-56029c0bbe20",
                    "metadata": [
                        {
                            "id": "c174f277-34b4-463b-9032-e3b9a0f227b0",
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
                    "id": "1a9d4c25-48fe-43c8-b2dc-4dd1734cb282",
                    "metadata": [
                        {
                            "id": "2e417cca-e939-4b4c-940a-ece1ada726d6",
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
                    "id": "61fb1766-e8b4-44ba-8e52-0b788abd2b5b",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "74cc2efd-e3fb-408c-9544-592b3482c2ff",
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
            "updated_at": parse_datetime("2025-06-10T12:46:12.315Z"),
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
            "id": "bb3362fa-d811-4d00-b38a-b06e7898627d",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "d455d6d2-b3db-40fd-8787-608122164b23",
                    "metadata": [
                        {
                            "id": "78009afc-a817-4e81-bb5b-8c29a4dc514b",
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
                    "id": "ac64f26a-084c-4058-8896-0610323e72f8",
                    "metadata": [
                        {
                            "id": "8cc5e9e5-d8cb-4069-adaf-25be33ed9b2c",
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
                    "id": "c3d7734a-6929-494a-bb29-f00b29e6d150",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "455d6079-0512-4428-9041-d44d502a3708",
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
            "updated_at": parse_datetime("2025-06-10T12:46:12.343Z"),
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
            "id": "bb3362fa-d811-4d00-b38a-b06e7898627d",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "d455d6d2-b3db-40fd-8787-608122164b23",
                    "metadata": [
                        {
                            "id": "78009afc-a817-4e81-bb5b-8c29a4dc514b",
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
                    "id": "ac64f26a-084c-4058-8896-0610323e72f8",
                    "metadata": [
                        {
                            "id": "8cc5e9e5-d8cb-4069-adaf-25be33ed9b2c",
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
                    "id": "c3d7734a-6929-494a-bb29-f00b29e6d150",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "455d6079-0512-4428-9041-d44d502a3708",
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
            "updated_at": parse_datetime("2025-06-10T12:46:12.343Z"),
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