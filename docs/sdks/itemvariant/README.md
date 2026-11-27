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
            "description": "Our dog-friendly Bacon ensures pessimistic comfort for your pets",
            "height": 54.0,
            "id": "40baffde-538e-4c46-a373-a617c821221a",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 961.0,
                    "id": "06f5269a-3fc8-4411-bbf4-65203b6f9940",
                    "metadata": [
                        {
                            "id": "a9564912-fb84-4401-bbef-26077f76d591",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/3208/3394",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "fa6c31a8-deaa-41fb-95b2-71acee059fb7",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "colligo",
                },
            ],
            "name": "Table",
            "options": [
                {
                    "id": "8032ad84-c6d4-4a94-9b25-002e439dbef6",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "purple",
                    ],
                },
                {
                    "id": "3850ca63-d220-4662-b20c-cff575105ea3",
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
            "public_description": "New teal Gloves with ergonomic design for favorite comfort",
            "public_name": "Table",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-05-109555-9",
            "tags": [
                "labore",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-10T21:39:53.605Z"),
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
            "description": "Our dog-friendly Bacon ensures pessimistic comfort for your pets",
            "height": 54.0,
            "id": "e5bf4cf4-77b6-478e-9653-e5fb30284409",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 961.0,
                    "id": "01b80f1d-2e93-4d8d-abe2-03c811fd0639",
                    "metadata": [
                        {
                            "id": "7c8b705f-29e3-447d-81dc-f615e5254112",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/3208/3394",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "9cf1764a-e94b-4708-a414-2a70a60a54f2",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "colligo",
                },
            ],
            "name": "Table",
            "options": [
                {
                    "id": "521eeb4c-aad4-43fd-81ad-25bfcbe220cd",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "purple",
                    ],
                },
                {
                    "id": "b49befee-b1c4-4bbd-81be-ff697a83cd65",
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
            "public_description": "New teal Gloves with ergonomic design for favorite comfort",
            "public_name": "Table",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-05-109555-9",
            "tags": [
                "labore",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-10T21:39:53.626Z"),
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
            "description": "Our dog-friendly Bacon ensures pessimistic comfort for your pets",
            "height": 54.0,
            "id": "e5bf4cf4-77b6-478e-9653-e5fb30284409",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 961.0,
                    "id": "01b80f1d-2e93-4d8d-abe2-03c811fd0639",
                    "metadata": [
                        {
                            "id": "7c8b705f-29e3-447d-81dc-f615e5254112",
                            "slug": "illo",
                            "value": "quia",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/u0YdHqlRu/3208/3394",
                    "width": 35.0,
                },
            ],
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CommerceMetadataFormat.TEXT,
                    "id": "9cf1764a-e94b-4708-a414-2a70a60a54f2",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "colligo",
                },
            ],
            "name": "Table",
            "options": [
                {
                    "id": "521eeb4c-aad4-43fd-81ad-25bfcbe220cd",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "purple",
                    ],
                },
                {
                    "id": "b49befee-b1c4-4bbd-81be-ff697a83cd65",
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
            "public_description": "New teal Gloves with ergonomic design for favorite comfort",
            "public_name": "Table",
            "requires_shipping": False,
            "size_unit": shared.SizeUnit.CM,
            "sku": "978-1-05-109555-9",
            "tags": [
                "labore",
            ],
            "total_stock": 436.0,
            "updated_at": parse_datetime("2026-04-10T21:39:53.626Z"),
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