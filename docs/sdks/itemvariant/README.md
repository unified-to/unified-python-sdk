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

Creates a CommerceItemvariant. Provide the unified CommerceItemvariant fields in the request body; they are mapped to the provider's API. Returns the created CommerceItemvariant.

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
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "e284565e-74ea-43eb-bf21-ee6924e38c7f",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "f301e71a-076b-4b6e-949b-0c1a7c72c18e",
                    "metadata": [
                        {
                            "id": "9b304265-eb4e-4111-ad85-c41d735b77cf",
                            "slug": "ubi",
                            "value": "textus",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2126/721?lock=8820088623807162",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "f4a96446-6f59-4ed2-95b3-4884a50b67dc",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "793fe162-2776-4e4c-bfd9-4e8ef1e0a40e",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "e28322e3-269e-402a-aaf3-322d539bce21",
                    "name": "Size",
                    "position": 2.0,
                    "values": [
                        "S",
                    ],
                },
            ],
            "prices": [
                {
                    "currency": "USD",
                    "price": 382.23,
                },
            ],
            "public_description": "Stylish Cheese designed to make you stand out with grave looks",
            "public_name": "Chair",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-368-44270-1",
            "tags": [
                "deserunt",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-03T22:06:01.037Z"),
            "weight": 46.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 40.0,
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

Retrieves a single CommerceItemvariant by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of CommerceItemvariants. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the CommerceItemvariant identified by `id`. Provide the unified CommerceItemvariant fields to change in the request body.

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
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "24148d3a-6caa-46be-8c52-5ff825efe97c",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "b20ced3b-2b62-4026-9614-7bc5ef02d48c",
                    "metadata": [
                        {
                            "id": "72750f93-b2bb-400e-b2b9-8a55ec0a5f67",
                            "slug": "ubi",
                            "value": "textus",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2126/721?lock=8820088623807162",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "f8a295ce-b53f-456e-8e1d-e3998884688d",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "b0ac5cc4-8e9b-4198-854c-76430bf12f01",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "2d491143-206c-4dcb-96e6-12fbf9d14cb3",
                    "name": "Size",
                    "position": 2.0,
                    "values": [
                        "S",
                    ],
                },
            ],
            "prices": [
                {
                    "currency": "USD",
                    "price": 382.23,
                },
            ],
            "public_description": "Stylish Cheese designed to make you stand out with grave looks",
            "public_name": "Chair",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-368-44270-1",
            "tags": [
                "deserunt",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-03T22:06:01.068Z"),
            "weight": 46.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 40.0,
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

Deletes the CommerceItemvariant identified by `id`.

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

Updates the CommerceItemvariant identified by `id`. Provide the unified CommerceItemvariant fields to change in the request body.

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
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "24148d3a-6caa-46be-8c52-5ff825efe97c",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "b20ced3b-2b62-4026-9614-7bc5ef02d48c",
                    "metadata": [
                        {
                            "id": "72750f93-b2bb-400e-b2b9-8a55ec0a5f67",
                            "slug": "ubi",
                            "value": "textus",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/2126/721?lock=8820088623807162",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "f8a295ce-b53f-456e-8e1d-e3998884688d",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "b0ac5cc4-8e9b-4198-854c-76430bf12f01",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "2d491143-206c-4dcb-96e6-12fbf9d14cb3",
                    "name": "Size",
                    "position": 2.0,
                    "values": [
                        "S",
                    ],
                },
            ],
            "prices": [
                {
                    "currency": "USD",
                    "price": 382.23,
                },
            ],
            "public_description": "Stylish Cheese designed to make you stand out with grave looks",
            "public_name": "Chair",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-368-44270-1",
            "tags": [
                "deserunt",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-03T22:06:01.068Z"),
            "weight": 46.0,
            "weight_unit": shared.CommerceItemvariantWeightUnit.OZ,
            "width": 40.0,
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