# Commerce

## Overview

### Available Operations

* [create_commerce_collection](#create_commerce_collection) - Create a collection
* [create_commerce_inventory](#create_commerce_inventory) - Create an inventory
* [create_commerce_item](#create_commerce_item) - Create an item
* [create_commerce_itemvariant](#create_commerce_itemvariant) - Create an itemvariant
* [create_commerce_location](#create_commerce_location) - Create a location
* [create_commerce_reservation](#create_commerce_reservation) - Create a reservation
* [create_commerce_review](#create_commerce_review) - Create a review
* [create_commerce_saleschannel](#create_commerce_saleschannel) - Create a saleschannel
* [get_commerce_collection](#get_commerce_collection) - Retrieve a collection
* [get_commerce_inventory](#get_commerce_inventory) - Retrieve an inventory
* [get_commerce_item](#get_commerce_item) - Retrieve an item
* [get_commerce_itemvariant](#get_commerce_itemvariant) - Retrieve an itemvariant
* [get_commerce_location](#get_commerce_location) - Retrieve a location
* [get_commerce_reservation](#get_commerce_reservation) - Retrieve a reservation
* [get_commerce_review](#get_commerce_review) - Retrieve a review
* [get_commerce_saleschannel](#get_commerce_saleschannel) - Retrieve a saleschannel
* [list_commerce_availabilities](#list_commerce_availabilities) - List all availabilities
* [list_commerce_collections](#list_commerce_collections) - List all collections
* [list_commerce_inventories](#list_commerce_inventories) - List all inventories
* [list_commerce_items](#list_commerce_items) - List all items
* [list_commerce_itemvariants](#list_commerce_itemvariants) - List all itemvariants
* [list_commerce_locations](#list_commerce_locations) - List all locations
* [list_commerce_reservations](#list_commerce_reservations) - List all reservations
* [list_commerce_reviews](#list_commerce_reviews) - List all reviews
* [list_commerce_saleschannels](#list_commerce_saleschannels) - List all saleschannels
* [patch_commerce_collection](#patch_commerce_collection) - Update a collection
* [patch_commerce_inventory](#patch_commerce_inventory) - Update an inventory
* [patch_commerce_item](#patch_commerce_item) - Update an item
* [patch_commerce_itemvariant](#patch_commerce_itemvariant) - Update an itemvariant
* [patch_commerce_location](#patch_commerce_location) - Update a location
* [patch_commerce_reservation](#patch_commerce_reservation) - Update a reservation
* [patch_commerce_review](#patch_commerce_review) - Update a review
* [patch_commerce_saleschannel](#patch_commerce_saleschannel) - Update a saleschannel
* [remove_commerce_collection](#remove_commerce_collection) - Remove a collection
* [remove_commerce_inventory](#remove_commerce_inventory) - Remove an inventory
* [remove_commerce_item](#remove_commerce_item) - Remove an item
* [remove_commerce_itemvariant](#remove_commerce_itemvariant) - Remove an itemvariant
* [remove_commerce_location](#remove_commerce_location) - Remove a location
* [remove_commerce_reservation](#remove_commerce_reservation) - Remove a reservation
* [remove_commerce_review](#remove_commerce_review) - Remove a review
* [remove_commerce_saleschannel](#remove_commerce_saleschannel) - Remove a saleschannel
* [update_commerce_collection](#update_commerce_collection) - Update a collection
* [update_commerce_inventory](#update_commerce_inventory) - Update an inventory
* [update_commerce_item](#update_commerce_item) - Update an item
* [update_commerce_itemvariant](#update_commerce_itemvariant) - Update an itemvariant
* [update_commerce_location](#update_commerce_location) - Update a location
* [update_commerce_reservation](#update_commerce_reservation) - Update a reservation
* [update_commerce_review](#update_commerce_review) - Update a review
* [update_commerce_saleschannel](#update_commerce_saleschannel) - Update a saleschannel

## create_commerce_collection

Creates a CommerceCollection. Provide the unified CommerceCollection fields in the request body; they are mapped to the provider's API. Returns the created CommerceCollection.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceCollection" method="post" path="/commerce/{connection_id}/collection" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "10a382c3-1b9e-4f13-8d3a-0274049afae4",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "d11fd957-f48c-438b-a10e-c0f4f9ffef81",
                    "metadata": [
                        {
                            "id": "25d084d6-f88f-4820-873a-7fca6cfc051d",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "171f9e26-b39d-4ac2-b79b-d94d6bae53e6",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-03-18T23:10:02.073Z"),
        },
        "connection_id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateCommerceCollectionRequest](../../models/operations/createcommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateCommerceCollectionResponse](../../models/operations/createcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_commerce_inventory

Creates a CommerceInventory. Provide the unified CommerceInventory fields in the request body; they are mapped to the provider's API. Returns the created CommerceInventory.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceInventory" method="post" path="/commerce/{connection_id}/inventory" example="commerce_inventory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_inventory(request={
        "commerce_inventory": {
            "available": 337.0,
            "id": "5617a56b-6e2c-45f1-8e02-32e2373bbd14",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T13:57:19.713Z"),
        },
        "connection_id": "<id>",
    })

    assert res.commerce_inventory is not None

    # Handle response
    print(res.commerce_inventory)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateCommerceInventoryRequest](../../models/operations/createcommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateCommerceInventoryResponse](../../models/operations/createcommerceinventoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.commerce.create_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "c1cd7664-fb2a-4779-98fc-d8245ae8f2db",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "2cd67fa4-874b-4ca7-83cf-bae4fd7cdbd8",
                    "metadata": [
                        {
                            "id": "c792ccf3-787f-4c89-b011-aeeaf6f6cd17",
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
                    "id": "28ee7c28-18b4-40d0-80a1-239ff719c83c",
                    "metadata": [
                        {
                            "id": "5efbc092-7311-430c-bf48-de78cd4e231d",
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
                    "id": "6b96f38f-ed3d-401a-ba15-78e3ec61fe2e",
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
            "updated_at": parse_datetime("2022-04-22T10:55:13.896Z"),
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

    res = unified_to.commerce.create_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "ce809556-ffe8-4a34-9047-d7d902cbdc22",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "ff9f90f6-d7a0-4a3c-9e44-2d8f38e8e293",
                    "metadata": [
                        {
                            "id": "11db6b0e-103f-4981-af13-6f407cb2b9d0",
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
                    "id": "ed6b4d4c-10f8-4bfe-99c1-36906ad663e1",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "e5823cc7-6f01-4eb2-a3f3-8e448aea4452",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "2276d566-5755-47f7-91e8-6a90a0a78f2f",
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
            "updated_at": parse_datetime("2026-03-16T08:19:23.007Z"),
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

## create_commerce_location

Creates a CommerceLocation. Provide the unified CommerceLocation fields in the request body; they are mapped to the provider's API. Returns the created CommerceLocation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceLocation" method="post" path="/commerce/{connection_id}/location" example="commerce_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_location(request={
        "commerce_location": {
            "address": {
                "address1": "29896 The Limes",
                "city": "New Kenny",
                "country_code": "US",
                "postal_code": "14490-0609",
                "region": "Virginia",
                "region_code": "MS",
            },
            "categories": [],
            "created_at": parse_datetime("2022-12-29T04:15:21.195Z"),
            "currency": "XCD",
            "description": "Adsidue audentia.",
            "id": "c71a6491-4137-4bf2-ac35-5e0ac4ef7ebb",
            "image_url": "https://picsum.photos/seed/hjFt1/1036/2220",
            "is_active": False,
            "language_locale": "vulgaris",
            "latitude": 0.0,
            "location_type": shared.LocationType.RESTAURANT,
            "longitude": 0.0,
            "media": [
                {
                    "alt": "Addo.",
                    "height": 283.0,
                    "id": "f72ef792-8ac5-4b4d-9191-007f0530db78",
                    "metadata": [
                        {
                            "id": "e9e17c7d-e836-4a4a-bc3d-b620b588c0cd",
                            "slug": "abutor",
                            "value": "damno",
                        },
                    ],
                    "position": 40.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/QVh7ViTV/3964/1567",
                    "width": 1.0,
                },
            ],
            "metadata": [],
            "name": "Olson - Mraz",
            "price_level": "",
            "rating": 0.0,
            "review_count": 0.0,
            "telephones": [
                {
                    "telephone": "(872) 522-3201",
                    "type": shared.CommerceTelephoneType.OTHER,
                },
                {
                    "telephone": "(236) 274-2445",
                    "type": shared.CommerceTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2024-04-23T09:10:04.254Z"),
            "web_url": "https://chilly-edge.info",
        },
        "connection_id": "<id>",
    })

    assert res.commerce_location is not None

    # Handle response
    print(res.commerce_location)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateCommerceLocationRequest](../../models/operations/createcommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateCommerceLocationResponse](../../models/operations/createcommercelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_commerce_reservation

Creates a CommerceReservation. Provide the unified CommerceReservation fields in the request body; they are mapped to the provider's API. Returns the created CommerceReservation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceReservation" method="post" path="/commerce/{connection_id}/reservation" example="commerce_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "ba0dd327-028c-4435-8553-bbf001563e7b",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T13:22:13.107Z"),
            "url": "https://expensive-gift.org",
        },
        "connection_id": "<id>",
    })

    assert res.commerce_reservation is not None

    # Handle response
    print(res.commerce_reservation)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateCommerceReservationRequest](../../models/operations/createcommercereservationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreateCommerceReservationResponse](../../models/operations/createcommercereservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_commerce_review

Creates a CommerceReview. Provide the unified CommerceReview fields in the request body; they are mapped to the provider's API. Returns the created CommerceReview.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceReview" method="post" path="/commerce/{connection_id}/review" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "3d4d31eb-6be7-46ff-bcd6-14db1295c6e4",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "8f5eddd7-2476-45d4-a773-a4fd740645c9",
                    "metadata": [
                        {
                            "id": "5a8d652a-d0ce-46a4-bb04-97fdb1beef7a",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "d2924f18-417e-4e3d-ba59-72a891f01529",
                    "metadata": [
                        {
                            "id": "6bc9cb03-7b1a-40e8-9a52-798a09b4ae38",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-27T17:19:20.590Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
        },
        "connection_id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateCommerceReviewRequest](../../models/operations/createcommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateCommerceReviewResponse](../../models/operations/createcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_commerce_saleschannel

Creates a CommerceSaleschannel. Provide the unified CommerceSaleschannel fields in the request body; they are mapped to the provider's API. Returns the created CommerceSaleschannel.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceSaleschannel" method="post" path="/commerce/{connection_id}/saleschannel" example="commerce_saleschannel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.create_commerce_saleschannel(request={
        "commerce_saleschannel": {
            "collections": [],
            "created_at": parse_datetime("2021-12-12T06:19:55.421Z"),
            "description": "Utroque denuncio solutio.",
            "id": "725238af-282e-4e21-9750-8d1176c456fc",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T22:29:11.165Z"),
        },
        "connection_id": "<id>",
    })

    assert res.commerce_saleschannel is not None

    # Handle response
    print(res.commerce_saleschannel)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateCommerceSaleschannelRequest](../../models/operations/createcommercesaleschannelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateCommerceSaleschannelResponse](../../models/operations/createcommercesaleschannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_collection

Retrieves a single CommerceCollection by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceCollection" method="get" path="/commerce/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCommerceCollectionRequest](../../models/operations/getcommercecollectionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetCommerceCollectionResponse](../../models/operations/getcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_inventory

Retrieves a single CommerceInventory by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceInventory" method="get" path="/commerce/{connection_id}/inventory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_inventory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_inventory is not None

    # Handle response
    print(res.commerce_inventory)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCommerceInventoryRequest](../../models/operations/getcommerceinventoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetCommerceInventoryResponse](../../models/operations/getcommerceinventoryresponse.md)**

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

    res = unified_to.commerce.get_commerce_item(request={
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

    res = unified_to.commerce.get_commerce_itemvariant(request={
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

## get_commerce_location

Retrieves a single CommerceLocation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceLocation" method="get" path="/commerce/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_location is not None

    # Handle response
    print(res.commerce_location)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCommerceLocationRequest](../../models/operations/getcommercelocationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetCommerceLocationResponse](../../models/operations/getcommercelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_reservation

Retrieves a single CommerceReservation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceReservation" method="get" path="/commerce/{connection_id}/reservation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_reservation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_reservation is not None

    # Handle response
    print(res.commerce_reservation)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCommerceReservationRequest](../../models/operations/getcommercereservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetCommerceReservationResponse](../../models/operations/getcommercereservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_review

Retrieves a single CommerceReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceReview" method="get" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetCommerceReviewRequest](../../models/operations/getcommercereviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetCommerceReviewResponse](../../models/operations/getcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_saleschannel

Retrieves a single CommerceSaleschannel by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceSaleschannel" method="get" path="/commerce/{connection_id}/saleschannel/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.get_commerce_saleschannel(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_saleschannel is not None

    # Handle response
    print(res.commerce_saleschannel)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCommerceSaleschannelRequest](../../models/operations/getcommercesaleschannelrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetCommerceSaleschannelResponse](../../models/operations/getcommercesaleschannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_availabilities

Returns a list of CommerceAvailabilities. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceAvailabilities" method="get" path="/commerce/{connection_id}/availability" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_availabilities(request={
        "connection_id": "<id>",
    })

    assert res.commerce_availabilities is not None

    # Handle response
    print(res.commerce_availabilities)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListCommerceAvailabilitiesRequest](../../models/operations/listcommerceavailabilitiesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListCommerceAvailabilitiesResponse](../../models/operations/listcommerceavailabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_collections

Returns a list of CommerceCollections. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceCollections" method="get" path="/commerce/{connection_id}/collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_collections(request={
        "connection_id": "<id>",
    })

    assert res.commerce_collections is not None

    # Handle response
    print(res.commerce_collections)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCommerceCollectionsRequest](../../models/operations/listcommercecollectionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListCommerceCollectionsResponse](../../models/operations/listcommercecollectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_inventories

Returns a list of CommerceInventories. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceInventories" method="get" path="/commerce/{connection_id}/inventory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_inventories(request={
        "connection_id": "<id>",
    })

    assert res.commerce_inventories is not None

    # Handle response
    print(res.commerce_inventories)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCommerceInventoriesRequest](../../models/operations/listcommerceinventoriesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListCommerceInventoriesResponse](../../models/operations/listcommerceinventoriesresponse.md)**

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

    res = unified_to.commerce.list_commerce_items(request={
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

    res = unified_to.commerce.list_commerce_itemvariants(request={
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

## list_commerce_locations

Returns a list of CommerceLocations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceLocations" method="get" path="/commerce/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_locations(request={
        "connection_id": "<id>",
    })

    assert res.commerce_locations is not None

    # Handle response
    print(res.commerce_locations)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCommerceLocationsRequest](../../models/operations/listcommercelocationsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListCommerceLocationsResponse](../../models/operations/listcommercelocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_reservations

Returns a list of CommerceReservations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceReservations" method="get" path="/commerce/{connection_id}/reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_reservations(request={
        "connection_id": "<id>",
    })

    assert res.commerce_reservations is not None

    # Handle response
    print(res.commerce_reservations)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListCommerceReservationsRequest](../../models/operations/listcommercereservationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListCommerceReservationsResponse](../../models/operations/listcommercereservationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_reviews

Returns a list of CommerceReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceReviews" method="get" path="/commerce/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_reviews(request={
        "connection_id": "<id>",
    })

    assert res.commerce_reviews is not None

    # Handle response
    print(res.commerce_reviews)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListCommerceReviewsRequest](../../models/operations/listcommercereviewsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListCommerceReviewsResponse](../../models/operations/listcommercereviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_saleschannels

Returns a list of CommerceSaleschannels. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceSaleschannels" method="get" path="/commerce/{connection_id}/saleschannel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.list_commerce_saleschannels(request={
        "connection_id": "<id>",
    })

    assert res.commerce_saleschannels is not None

    # Handle response
    print(res.commerce_saleschannels)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListCommerceSaleschannelsRequest](../../models/operations/listcommercesaleschannelsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListCommerceSaleschannelsResponse](../../models/operations/listcommercesaleschannelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_collection

Updates the CommerceCollection identified by `id`. Provide the unified CommerceCollection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceCollection" method="patch" path="/commerce/{connection_id}/collection/{id}" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "f6563954-8867-4b40-a4d2-34a908d18100",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "b72459f9-f0b2-4e5d-a024-96b6b0347648",
                    "metadata": [
                        {
                            "id": "9c38d571-cad4-4eb5-9aa2-020cae6c261c",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "afcc1f58-6019-40d6-bfb5-1f1bad67854d",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-03-18T23:10:02.084Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchCommerceCollectionRequest](../../models/operations/patchcommercecollectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchCommerceCollectionResponse](../../models/operations/patchcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_inventory

Updates the CommerceInventory identified by `id`. Provide the unified CommerceInventory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceInventory" method="patch" path="/commerce/{connection_id}/inventory/{id}" example="commerce_inventory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_inventory(request={
        "commerce_inventory": {
            "available": 337.0,
            "id": "38435e5a-1cae-46da-a190-9704dcde1a7a",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T13:57:19.720Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_inventory is not None

    # Handle response
    print(res.commerce_inventory)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchCommerceInventoryRequest](../../models/operations/patchcommerceinventoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchCommerceInventoryResponse](../../models/operations/patchcommerceinventoryresponse.md)**

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

    res = unified_to.commerce.patch_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "86c46546-9be8-49bb-a880-2104e4122295",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "9ab06be3-2b28-445a-b573-17c589333c6e",
                    "metadata": [
                        {
                            "id": "43308512-7983-45db-8952-1533c367aeea",
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
                    "id": "63f00f57-ffd1-4908-82b7-2bc605ce0050",
                    "metadata": [
                        {
                            "id": "7ed480f6-0ea1-4576-b291-8eb27f419693",
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
                    "id": "a63f40bc-f7b9-4cf7-9e6f-8a0dfc373417",
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
            "updated_at": parse_datetime("2022-04-22T10:55:13.908Z"),
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

    res = unified_to.commerce.patch_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "2e6557c0-efed-432c-89ac-affe84e41ec1",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "3587eb58-16ec-4879-9031-54ef99880c3c",
                    "metadata": [
                        {
                            "id": "e4b8b025-d58f-448a-86fc-26ba7c942af7",
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
                    "id": "37bddd38-ae13-456b-9a32-fcd496643b2a",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "b5d0a63c-6cb2-4e7d-8420-6f66f9b5c65d",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "4537b292-a092-4501-a622-88430d4c8d72",
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
            "updated_at": parse_datetime("2026-03-16T08:19:23.036Z"),
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

## patch_commerce_location

Updates the CommerceLocation identified by `id`. Provide the unified CommerceLocation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceLocation" method="patch" path="/commerce/{connection_id}/location/{id}" example="commerce_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_location(request={
        "commerce_location": {
            "address": {
                "address1": "29896 The Limes",
                "city": "New Kenny",
                "country_code": "US",
                "postal_code": "14490-0609",
                "region": "Virginia",
                "region_code": "MS",
            },
            "categories": [],
            "created_at": parse_datetime("2022-12-29T04:15:21.195Z"),
            "currency": "XCD",
            "description": "Adsidue audentia.",
            "id": "0fc6e241-1b47-4120-a61e-aca7e732f00c",
            "image_url": "https://picsum.photos/seed/hjFt1/1036/2220",
            "is_active": False,
            "language_locale": "vulgaris",
            "latitude": 0.0,
            "location_type": shared.LocationType.RESTAURANT,
            "longitude": 0.0,
            "media": [
                {
                    "alt": "Addo.",
                    "height": 283.0,
                    "id": "db16b084-3f79-422b-b008-35eb394b0bed",
                    "metadata": [
                        {
                            "id": "fd4c6685-5756-4ac2-b685-4a0abcbb245d",
                            "slug": "abutor",
                            "value": "damno",
                        },
                    ],
                    "position": 40.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/QVh7ViTV/3964/1567",
                    "width": 1.0,
                },
            ],
            "metadata": [],
            "name": "Olson - Mraz",
            "price_level": "",
            "rating": 0.0,
            "review_count": 0.0,
            "telephones": [
                {
                    "telephone": "(872) 522-3201",
                    "type": shared.CommerceTelephoneType.OTHER,
                },
                {
                    "telephone": "(236) 274-2445",
                    "type": shared.CommerceTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2024-04-23T09:10:04.262Z"),
            "web_url": "https://chilly-edge.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_location is not None

    # Handle response
    print(res.commerce_location)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchCommerceLocationRequest](../../models/operations/patchcommercelocationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchCommerceLocationResponse](../../models/operations/patchcommercelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_reservation

Updates the CommerceReservation identified by `id`. Provide the unified CommerceReservation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceReservation" method="patch" path="/commerce/{connection_id}/reservation/{id}" example="commerce_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "2e29db6d-60de-4e33-8db4-bad28a4c1723",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T13:22:13.111Z"),
            "url": "https://expensive-gift.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_reservation is not None

    # Handle response
    print(res.commerce_reservation)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchCommerceReservationRequest](../../models/operations/patchcommercereservationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PatchCommerceReservationResponse](../../models/operations/patchcommercereservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_review

Updates the CommerceReview identified by `id`. Provide the unified CommerceReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceReview" method="patch" path="/commerce/{connection_id}/review/{id}" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "bffcefdf-1286-41fc-99f7-1286cdf55635",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "3b56bb82-45b0-4c58-bc27-e1a5cbe3ff89",
                    "metadata": [
                        {
                            "id": "2be425f2-b2a6-435a-8fd8-174980ce3937",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "4c0f18d7-99bc-44c8-8bd4-583d524a40e9",
                    "metadata": [
                        {
                            "id": "a50c14eb-194d-48aa-ae83-74f8dd8d8023",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-27T17:19:20.614Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchCommerceReviewRequest](../../models/operations/patchcommercereviewrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchCommerceReviewResponse](../../models/operations/patchcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_saleschannel

Updates the CommerceSaleschannel identified by `id`. Provide the unified CommerceSaleschannel fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceSaleschannel" method="patch" path="/commerce/{connection_id}/saleschannel/{id}" example="commerce_saleschannel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.patch_commerce_saleschannel(request={
        "commerce_saleschannel": {
            "collections": [],
            "created_at": parse_datetime("2021-12-12T06:19:55.421Z"),
            "description": "Utroque denuncio solutio.",
            "id": "4e88f54c-5c9b-433f-b696-d304474c0e32",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T22:29:11.172Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_saleschannel is not None

    # Handle response
    print(res.commerce_saleschannel)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchCommerceSaleschannelRequest](../../models/operations/patchcommercesaleschannelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchCommerceSaleschannelResponse](../../models/operations/patchcommercesaleschannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_collection

Deletes the CommerceCollection identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceCollection" method="delete" path="/commerce/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveCommerceCollectionRequest](../../models/operations/removecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveCommerceCollectionResponse](../../models/operations/removecommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_inventory

Deletes the CommerceInventory identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceInventory" method="delete" path="/commerce/{connection_id}/inventory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_inventory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveCommerceInventoryRequest](../../models/operations/removecommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveCommerceInventoryResponse](../../models/operations/removecommerceinventoryresponse.md)**

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

    res = unified_to.commerce.remove_commerce_item(request={
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

    res = unified_to.commerce.remove_commerce_itemvariant(request={
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

## remove_commerce_location

Deletes the CommerceLocation identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceLocation" method="delete" path="/commerce/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveCommerceLocationRequest](../../models/operations/removecommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveCommerceLocationResponse](../../models/operations/removecommercelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_reservation

Deletes the CommerceReservation identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceReservation" method="delete" path="/commerce/{connection_id}/reservation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_reservation(request={
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
| `request`                                                                                                  | [operations.RemoveCommerceReservationRequest](../../models/operations/removecommercereservationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.RemoveCommerceReservationResponse](../../models/operations/removecommercereservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_review

Deletes the CommerceReview identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceReview" method="delete" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_review(request={
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
| `request`                                                                                        | [operations.RemoveCommerceReviewRequest](../../models/operations/removecommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveCommerceReviewResponse](../../models/operations/removecommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_saleschannel

Deletes the CommerceSaleschannel identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceSaleschannel" method="delete" path="/commerce/{connection_id}/saleschannel/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.remove_commerce_saleschannel(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.RemoveCommerceSaleschannelRequest](../../models/operations/removecommercesaleschannelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveCommerceSaleschannelResponse](../../models/operations/removecommercesaleschannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_collection

Updates the CommerceCollection identified by `id`. Provide the unified CommerceCollection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceCollection" method="put" path="/commerce/{connection_id}/collection/{id}" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "f6563954-8867-4b40-a4d2-34a908d18100",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "b72459f9-f0b2-4e5d-a024-96b6b0347648",
                    "metadata": [
                        {
                            "id": "9c38d571-cad4-4eb5-9aa2-020cae6c261c",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "afcc1f58-6019-40d6-bfb5-1f1bad67854d",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-03-18T23:10:02.084Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateCommerceCollectionRequest](../../models/operations/updatecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateCommerceCollectionResponse](../../models/operations/updatecommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_inventory

Updates the CommerceInventory identified by `id`. Provide the unified CommerceInventory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceInventory" method="put" path="/commerce/{connection_id}/inventory/{id}" example="commerce_inventory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_inventory(request={
        "commerce_inventory": {
            "available": 337.0,
            "id": "38435e5a-1cae-46da-a190-9704dcde1a7a",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T13:57:19.720Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_inventory is not None

    # Handle response
    print(res.commerce_inventory)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateCommerceInventoryRequest](../../models/operations/updatecommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateCommerceInventoryResponse](../../models/operations/updatecommerceinventoryresponse.md)**

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

    res = unified_to.commerce.update_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Decretum vulnero ustulo abeo.",
            "duration": 104.0,
            "global_code": "978-0-85270-680-0",
            "id": "86c46546-9be8-49bb-a880-2104e4122295",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "9ab06be3-2b28-445a-b573-17c589333c6e",
                    "metadata": [
                        {
                            "id": "43308512-7983-45db-8952-1533c367aeea",
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
                    "id": "63f00f57-ffd1-4908-82b7-2bc605ce0050",
                    "metadata": [
                        {
                            "id": "7ed480f6-0ea1-4576-b291-8eb27f419693",
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
                    "id": "a63f40bc-f7b9-4cf7-9e6f-8a0dfc373417",
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
            "updated_at": parse_datetime("2022-04-22T10:55:13.908Z"),
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

    res = unified_to.commerce.update_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-06T18:14:41.644Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Stylish Salad designed to make you stand out with little looks",
            "height": 54.0,
            "id": "2e6557c0-efed-432c-89ac-affe84e41ec1",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "3587eb58-16ec-4879-9031-54ef99880c3c",
                    "metadata": [
                        {
                            "id": "e4b8b025-d58f-448a-86fc-26ba7c942af7",
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
                    "id": "37bddd38-ae13-456b-9a32-fcd496643b2a",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "b5d0a63c-6cb2-4e7d-8420-6f66f9b5c65d",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "4537b292-a092-4501-a622-88430d4c8d72",
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
            "updated_at": parse_datetime("2026-03-16T08:19:23.036Z"),
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

## update_commerce_location

Updates the CommerceLocation identified by `id`. Provide the unified CommerceLocation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceLocation" method="put" path="/commerce/{connection_id}/location/{id}" example="commerce_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_location(request={
        "commerce_location": {
            "address": {
                "address1": "29896 The Limes",
                "city": "New Kenny",
                "country_code": "US",
                "postal_code": "14490-0609",
                "region": "Virginia",
                "region_code": "MS",
            },
            "categories": [],
            "created_at": parse_datetime("2022-12-29T04:15:21.195Z"),
            "currency": "XCD",
            "description": "Adsidue audentia.",
            "id": "0fc6e241-1b47-4120-a61e-aca7e732f00c",
            "image_url": "https://picsum.photos/seed/hjFt1/1036/2220",
            "is_active": False,
            "language_locale": "vulgaris",
            "latitude": 0.0,
            "location_type": shared.LocationType.RESTAURANT,
            "longitude": 0.0,
            "media": [
                {
                    "alt": "Addo.",
                    "height": 283.0,
                    "id": "db16b084-3f79-422b-b008-35eb394b0bed",
                    "metadata": [
                        {
                            "id": "fd4c6685-5756-4ac2-b685-4a0abcbb245d",
                            "slug": "abutor",
                            "value": "damno",
                        },
                    ],
                    "position": 40.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/QVh7ViTV/3964/1567",
                    "width": 1.0,
                },
            ],
            "metadata": [],
            "name": "Olson - Mraz",
            "price_level": "",
            "rating": 0.0,
            "review_count": 0.0,
            "telephones": [
                {
                    "telephone": "(872) 522-3201",
                    "type": shared.CommerceTelephoneType.OTHER,
                },
                {
                    "telephone": "(236) 274-2445",
                    "type": shared.CommerceTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2024-04-23T09:10:04.262Z"),
            "web_url": "https://chilly-edge.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_location is not None

    # Handle response
    print(res.commerce_location)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateCommerceLocationRequest](../../models/operations/updatecommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateCommerceLocationResponse](../../models/operations/updatecommercelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_reservation

Updates the CommerceReservation identified by `id`. Provide the unified CommerceReservation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceReservation" method="put" path="/commerce/{connection_id}/reservation/{id}" example="commerce_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "2e29db6d-60de-4e33-8db4-bad28a4c1723",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T13:22:13.111Z"),
            "url": "https://expensive-gift.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_reservation is not None

    # Handle response
    print(res.commerce_reservation)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateCommerceReservationRequest](../../models/operations/updatecommercereservationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdateCommerceReservationResponse](../../models/operations/updatecommercereservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_review

Updates the CommerceReview identified by `id`. Provide the unified CommerceReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceReview" method="put" path="/commerce/{connection_id}/review/{id}" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "bffcefdf-1286-41fc-99f7-1286cdf55635",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "3b56bb82-45b0-4c58-bc27-e1a5cbe3ff89",
                    "metadata": [
                        {
                            "id": "2be425f2-b2a6-435a-8fd8-174980ce3937",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "4c0f18d7-99bc-44c8-8bd4-583d524a40e9",
                    "metadata": [
                        {
                            "id": "a50c14eb-194d-48aa-ae83-74f8dd8d8023",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-27T17:19:20.614Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateCommerceReviewRequest](../../models/operations/updatecommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateCommerceReviewResponse](../../models/operations/updatecommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_saleschannel

Updates the CommerceSaleschannel identified by `id`. Provide the unified CommerceSaleschannel fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceSaleschannel" method="put" path="/commerce/{connection_id}/saleschannel/{id}" example="commerce_saleschannel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.commerce.update_commerce_saleschannel(request={
        "commerce_saleschannel": {
            "collections": [],
            "created_at": parse_datetime("2021-12-12T06:19:55.421Z"),
            "description": "Utroque denuncio solutio.",
            "id": "4e88f54c-5c9b-433f-b696-d304474c0e32",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T22:29:11.172Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_saleschannel is not None

    # Handle response
    print(res.commerce_saleschannel)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateCommerceSaleschannelRequest](../../models/operations/updatecommercesaleschannelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateCommerceSaleschannelResponse](../../models/operations/updatecommercesaleschannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |