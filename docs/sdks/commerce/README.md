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
            "id": "4f9bb7d4-c062-4e04-9b4d-999fdcc578b0",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "b1fe1524-ac27-4b09-98a8-6631d9cfc701",
                    "metadata": [
                        {
                            "id": "a52e68fb-d36e-45db-a5ac-4aa717f612d9",
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
                    "id": "39bf4973-3ed7-4c04-9679-3fc47cb1a329",
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
            "updated_at": parse_datetime("2025-03-18T15:29:36.315Z"),
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
            "id": "19b9a272-ef95-4f7d-99ae-394076c8bfa9",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T01:50:36.999Z"),
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
            "id": "9736e8cb-1362-4970-84d9-5c5a85bb6831",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "6292f009-676d-4593-9f4d-1fa8c22d01d5",
                    "metadata": [
                        {
                            "id": "a5bb539d-4f42-4f15-8bb1-102ef696d230",
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
                    "id": "5061a3c5-e827-487b-9580-665e6a20bc86",
                    "metadata": [
                        {
                            "id": "d994bdbf-0bff-4dd9-bd9d-9d4601ab4368",
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
                    "id": "cadd9819-262b-423a-80a6-765b740a18d8",
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
            "updated_at": parse_datetime("2022-04-22T05:07:27.786Z"),
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
            "id": "38088a7b-a906-461e-a7ee-807e22fec475",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "cf695498-b979-4117-8f96-cdf2b22c9b23",
                    "metadata": [
                        {
                            "id": "b55d29f9-353b-4105-813e-f0e0e048dd39",
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
                    "id": "7b1adf8e-6de0-4b74-b5cb-d734513dcfd8",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "500cca3e-f9df-4740-a292-6df1ec4a9b88",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "96b6ed20-d1af-427f-bc2a-f28f0ae190b7",
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
            "updated_at": parse_datetime("2026-03-15T19:14:37.696Z"),
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
            "id": "0d0f6c51-dec5-4ff9-b2ba-568203395832",
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
                    "id": "a72641f6-25e3-428f-b005-6d52cee79df9",
                    "metadata": [
                        {
                            "id": "1e25f5f7-1561-411b-9240-757b67f4658e",
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
            "updated_at": parse_datetime("2024-04-23T03:59:56.885Z"),
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
            "id": "971a3932-c718-422f-b54d-a5ffec665c46",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T10:06:08.045Z"),
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
            "id": "7f53f920-fb89-4679-ab43-fffea9aa50dc",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "99e2bffd-7ea0-41b6-9417-e960f47d265b",
                    "metadata": [
                        {
                            "id": "1b91bc6c-69c3-49fe-9934-8e2cf9538870",
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
                    "id": "0520c6b4-54ff-4ef0-bd0f-4eb1f4142eda",
                    "metadata": [
                        {
                            "id": "b309deb1-f46a-4755-8666-895eb3c36fb8",
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
            "updated_at": parse_datetime("2025-08-27T04:50:43.002Z"),
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
            "id": "fbd6f8e4-fc62-4894-9e11-50913042faa5",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T12:48:07.046Z"),
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
            "id": "5425878b-7599-4b57-853c-6f7600bee675",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "f4f8d545-9ec4-41fa-9bce-fc1999eecddb",
                    "metadata": [
                        {
                            "id": "a9575bdb-453d-4b5b-8e74-4640baced1ff",
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
                    "id": "85f97759-1f26-4944-b214-b5c7d2ad56f1",
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
            "updated_at": parse_datetime("2025-03-18T15:29:36.329Z"),
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
            "id": "aa1c00f3-915c-404f-8e2d-26debb47420b",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T01:50:37.018Z"),
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
            "id": "d38945bb-4da9-45ee-bc8c-143b20372bba",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "c64401f2-9728-4de9-aba7-b37d9ab2560f",
                    "metadata": [
                        {
                            "id": "7ba93568-19ef-49b0-948b-1d4a441a1f7f",
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
                    "id": "c6870b0b-b66f-432b-aa6a-69964ab543a7",
                    "metadata": [
                        {
                            "id": "9bdd6cc6-4c2e-451b-b01e-2d12f1db115e",
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
                    "id": "6408580b-e4f4-44fd-a65d-b6bea396422e",
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
            "updated_at": parse_datetime("2022-04-22T05:07:27.801Z"),
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
            "id": "4ef71045-cdae-45ac-ba61-8755eee141b8",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "172b655f-6c9a-477d-89e0-120a4de666c0",
                    "metadata": [
                        {
                            "id": "45ede27f-75ff-4cc4-b8cc-b1a607698188",
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
                    "id": "b95778e1-adc5-4ab6-bb82-b7f2d908c4bf",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "6c1f0891-d28c-4222-bb75-01dd3c49e8c3",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "7362b491-63aa-47cd-986e-354084738f09",
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
            "updated_at": parse_datetime("2026-03-15T19:14:37.736Z"),
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
            "id": "43df297f-5066-4600-9980-effd2d9fa63e",
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
                    "id": "d68e41c4-7690-469c-923e-9a8f46816cd5",
                    "metadata": [
                        {
                            "id": "0696607c-52f3-4f01-9c2e-0cd307f61865",
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
            "updated_at": parse_datetime("2024-04-23T03:59:56.901Z"),
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
            "id": "6adc7cb1-9534-43bd-8042-4c17d38a7d00",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T10:06:08.053Z"),
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
            "id": "cd42cc21-88ad-484c-a5d6-272fc39a28ac",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "8fa94204-37b2-416b-98cc-78915cae5064",
                    "metadata": [
                        {
                            "id": "45b13428-e363-42b1-a5b8-7805ad222255",
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
                    "id": "55e527e7-4361-4804-bfeb-b620e6fd63f4",
                    "metadata": [
                        {
                            "id": "2c607df0-290a-42bd-a057-f47b18b27001",
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
            "updated_at": parse_datetime("2025-08-27T04:50:43.035Z"),
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
            "id": "dbb12b9a-eb9c-4cb9-95ac-25e95a614df6",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T12:48:07.056Z"),
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
            "id": "5425878b-7599-4b57-853c-6f7600bee675",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "f4f8d545-9ec4-41fa-9bce-fc1999eecddb",
                    "metadata": [
                        {
                            "id": "a9575bdb-453d-4b5b-8e74-4640baced1ff",
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
                    "id": "85f97759-1f26-4944-b214-b5c7d2ad56f1",
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
            "updated_at": parse_datetime("2025-03-18T15:29:36.329Z"),
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
            "id": "aa1c00f3-915c-404f-8e2d-26debb47420b",
            "metadata": [],
            "updated_at": parse_datetime("2025-11-26T01:50:37.018Z"),
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
            "id": "d38945bb-4da9-45ee-bc8c-143b20372bba",
            "is_active": False,
            "is_featured": False,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 876.0,
                    "id": "c64401f2-9728-4de9-aba7-b37d9ab2560f",
                    "metadata": [
                        {
                            "id": "7ba93568-19ef-49b0-948b-1d4a441a1f7f",
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
                    "id": "c6870b0b-b66f-432b-aa6a-69964ab543a7",
                    "metadata": [
                        {
                            "id": "9bdd6cc6-4c2e-451b-b01e-2d12f1db115e",
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
                    "id": "6408580b-e4f4-44fd-a65d-b6bea396422e",
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
            "updated_at": parse_datetime("2022-04-22T05:07:27.801Z"),
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
            "id": "4ef71045-cdae-45ac-ba61-8755eee141b8",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "length": 92.0,
            "media": [
                {
                    "alt": "Hic desipio thorax.",
                    "height": 961.0,
                    "id": "172b655f-6c9a-477d-89e0-120a4de666c0",
                    "metadata": [
                        {
                            "id": "45ede27f-75ff-4cc4-b8cc-b1a607698188",
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
                    "id": "b95778e1-adc5-4ab6-bb82-b7f2d908c4bf",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "absens",
                },
            ],
            "name": "Chair",
            "options": [
                {
                    "id": "6c1f0891-d28c-4222-bb75-01dd3c49e8c3",
                    "name": "Color",
                    "position": 1.0,
                    "values": [
                        "olive",
                    ],
                },
                {
                    "id": "7362b491-63aa-47cd-986e-354084738f09",
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
            "updated_at": parse_datetime("2026-03-15T19:14:37.736Z"),
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
            "id": "43df297f-5066-4600-9980-effd2d9fa63e",
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
                    "id": "d68e41c4-7690-469c-923e-9a8f46816cd5",
                    "metadata": [
                        {
                            "id": "0696607c-52f3-4f01-9c2e-0cd307f61865",
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
            "updated_at": parse_datetime("2024-04-23T03:59:56.901Z"),
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
            "id": "6adc7cb1-9534-43bd-8042-4c17d38a7d00",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-05T10:06:08.053Z"),
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
            "id": "cd42cc21-88ad-484c-a5d6-272fc39a28ac",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "8fa94204-37b2-416b-98cc-78915cae5064",
                    "metadata": [
                        {
                            "id": "45b13428-e363-42b1-a5b8-7805ad222255",
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
                    "id": "55e527e7-4361-4804-bfeb-b620e6fd63f4",
                    "metadata": [
                        {
                            "id": "2c607df0-290a-42bd-a057-f47b18b27001",
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
            "updated_at": parse_datetime("2025-08-27T04:50:43.035Z"),
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
            "id": "dbb12b9a-eb9c-4cb9-95ac-25e95a614df6",
            "is_active": False,
            "metadata": [],
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-02-01T12:48:07.056Z"),
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