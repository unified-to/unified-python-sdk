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
            "id": "e91bd93d-f42d-411b-94a7-65de6a5266f0",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "0df68d48-9b71-42c0-9969-280f1fdfe13c",
                    "metadata": [
                        {
                            "id": "e7d8e687-46cc-46fd-a40f-6f4bfee0573a",
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
                    "id": "b3d97b80-9ce7-451f-84d6-8915c6572400",
                    "metadata": [
                        {
                            "id": "0603e178-df79-48f5-bf17-d7407cc55fad",
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
                    "id": "62d59580-daa5-47f6-be71-16d9a091f88c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "dd40d854-d6df-4abb-85af-484f0f8e438f",
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
            "updated_at": parse_datetime("2025-05-24T09:43:44.260Z"),
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
            "id": "fd2b82ff-c6ef-47a1-afd0-6d70bceda470",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "3108e06a-1e96-4c0c-828e-08c3aab51784",
                    "metadata": [
                        {
                            "id": "adb2dd1f-776a-4dd2-ad42-99d0a9fa02cc",
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
                    "id": "e61ab1fa-6a83-4092-b44d-6834239c6dc1",
                    "metadata": [
                        {
                            "id": "0ec8612f-e417-4ed7-84ee-cfa4e1791828",
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
                    "id": "56754fab-a4c3-44db-9852-e5d9ce383b99",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "f99075f0-3294-4e09-85af-893aa8e611d4",
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
            "updated_at": parse_datetime("2025-05-24T09:43:44.303Z"),
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
            "id": "fd2b82ff-c6ef-47a1-afd0-6d70bceda470",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "3108e06a-1e96-4c0c-828e-08c3aab51784",
                    "metadata": [
                        {
                            "id": "adb2dd1f-776a-4dd2-ad42-99d0a9fa02cc",
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
                    "id": "e61ab1fa-6a83-4092-b44d-6834239c6dc1",
                    "metadata": [
                        {
                            "id": "0ec8612f-e417-4ed7-84ee-cfa4e1791828",
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
                    "id": "56754fab-a4c3-44db-9852-e5d9ce383b99",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "f99075f0-3294-4e09-85af-893aa8e611d4",
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
            "updated_at": parse_datetime("2025-05-24T09:43:44.303Z"),
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