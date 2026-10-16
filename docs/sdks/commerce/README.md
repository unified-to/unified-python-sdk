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

Create a collection

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
            "id": "58dcf1ae-f432-4554-befe-3f7671781c97",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "11a8ef94-c81b-442b-9cb1-9b0a8357f77f",
                    "metadata": [
                        {
                            "id": "37a9c11c-d97f-43ab-b210-88cb74deda38",
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
                    "id": "6333486a-6be8-4f75-a5a1-2ddabbacf82a",
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
            "updated_at": parse_datetime("2025-03-12T10:28:32.465Z"),
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

Create an inventory

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
            "updated_at": parse_datetime("2025-11-16T06:38:37.017Z"),
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

    res = unified_to.commerce.create_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "2ced1c9f-ea7a-43e7-9782-bbc044971de6",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "bed940a2-a2c9-454a-8e44-69200c6e3e9c",
                    "metadata": [
                        {
                            "id": "7ba951e2-b4f0-49a0-a4ca-7f5ade2f0b71",
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
                    "id": "a149690c-6550-498e-a311-14585720bc85",
                    "metadata": [
                        {
                            "id": "0e06f1e2-715b-4b17-9a5e-4b8f2cd8ab8c",
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
                    "id": "643e1d80-5db7-4206-8d2f-c37ca431e5a0",
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
            "updated_at": parse_datetime("2022-04-17T12:34:09.617Z"),
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

    res = unified_to.commerce.create_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "596b38e3-eb16-4f93-9d4b-7d3da0ec6580",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "1c72f70a-5098-4b97-88cb-5d619e6878ee",
                    "metadata": [
                        {
                            "id": "f02142e0-29fa-4e83-94a5-c17394aabd70",
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
                    "id": "13424dcf-42c0-4389-9faa-1fd2c9846606",
                    "metadata": [
                        {
                            "id": "bfe694cb-51e6-40cb-91f3-1a20d65d8302",
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
                    "id": "0c1e7229-a8ac-4ce9-aa1c-4fc271694705",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "53b53cf7-7619-4d45-a627-b347b9e5b084",
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
            "updated_at": parse_datetime("2025-06-13T09:22:25.174Z"),
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

## create_commerce_location

Create a location

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
            "id": "cb374ddf-3f62-4741-af8e-c2e3db085360",
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
                    "id": "0b01fa92-f704-4cd4-9187-0b1dfb89ebe3",
                    "metadata": [
                        {
                            "id": "84cd7620-819c-473c-8c0b-4d7ccf117834",
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
            "updated_at": parse_datetime("2024-04-18T23:37:40.684Z"),
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

Create a reservation

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
            "guest_email": "Sunny.Strosin77@yahoo.com",
            "guest_name": "Annette Franecki",
            "guest_phone": "(990) 317-6213",
            "id": "175cd9d9-072a-4cfe-b293-33dde0e09870",
            "item_name": "Practical Ceramic Shoes",
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "staff_name": "Vickie Fahey",
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-02T18:38:22.169Z"),
            "url": "https://cluttered-pine.info/",
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

Create a review

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
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "2adae035-5159-44ab-bee7-2324e48fd658",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "8a598d1c-5147-48ab-8707-ac2c9ec87c97",
                    "metadata": [
                        {
                            "id": "5acb0410-251f-4f21-b8d7-865356bb7b81",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "3a3902f0-5850-4aa0-b084-87e5b6143be2",
                    "metadata": [
                        {
                            "id": "b4bc3ddd-10e5-48b0-8f5e-ca834a0de376",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "2d1ab3cb-0ed8-44fe-b19f-fe2a7fe7d09a",
                    "metadata": [
                        {
                            "id": "da9e2d98-c700-4da3-b2d1-fdf0957dfb96",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-08-17T02:33:08.431Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
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

Create a saleschannel

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
            "id": "b2f6ec11-6c4b-48d0-bd73-725af71b9259",
            "is_active": False,
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-01-24T16:44:19.988Z"),
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

Retrieve a collection

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

Retrieve an inventory

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

Retrieve a location

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

Retrieve a reservation

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

Retrieve a review

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

Retrieve a saleschannel

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

List all availabilities

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

List all collections

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

List all inventories

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

List all locations

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

List all reservations

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

List all reviews

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

List all saleschannels

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

Update a collection

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
            "id": "997ee7a0-a8ff-4556-8128-0b61c516bf06",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "9441d2c1-c6ca-49e1-8ebf-b1a4cbabcc51",
                    "metadata": [
                        {
                            "id": "830a9af8-509d-4c84-9782-aaf265f855ff",
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
                    "id": "09d190c1-f53b-454e-bf71-590cfc511276",
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
            "updated_at": parse_datetime("2025-03-12T10:28:32.483Z"),
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

Update an inventory

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
            "updated_at": parse_datetime("2025-11-16T06:38:37.023Z"),
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

    res = unified_to.commerce.patch_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "8bc796cc-ddee-4cb9-bd76-99fb8a3371ce",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "5bd4418f-1412-47be-ad89-6fbb136aa5f0",
                    "metadata": [
                        {
                            "id": "2a957115-2d92-47a4-9794-f69ab94044e0",
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
                    "id": "e5d33be6-1a30-4092-9235-623277a08650",
                    "metadata": [
                        {
                            "id": "c469c97a-170d-4ba1-b12c-5637a8e7a19f",
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
                    "id": "2eed0374-b275-46e9-a9d3-5b14261d4a91",
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
            "updated_at": parse_datetime("2022-04-17T12:34:09.633Z"),
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

    res = unified_to.commerce.patch_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "42d11ae6-5c61-4d18-b593-c1e1de50b539",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "370c4222-92a0-419e-80b0-c733439275b9",
                    "metadata": [
                        {
                            "id": "7d6edbba-78d1-4f20-9c79-fd078a040ed1",
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
                    "id": "e22d9f93-0727-40f7-9c57-a960216cccdb",
                    "metadata": [
                        {
                            "id": "d2b39e90-a163-4c21-9099-cb626af96f87",
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
                    "id": "b522b344-5246-4671-8799-51d523381ab5",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "722af448-dab3-48a1-a785-a9529cd6af05",
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
            "updated_at": parse_datetime("2025-06-13T09:22:25.204Z"),
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

## patch_commerce_location

Update a location

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
            "id": "14a07798-1753-415f-8717-8baa84028c2e",
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
                    "id": "578ef951-b12c-4009-9d90-cbc858fa8efa",
                    "metadata": [
                        {
                            "id": "06d1c0a8-42ef-4674-adb8-eccf57dd3ac3",
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
            "updated_at": parse_datetime("2024-04-18T23:37:40.697Z"),
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

Update a reservation

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
            "guest_email": "Sunny.Strosin77@yahoo.com",
            "guest_name": "Annette Franecki",
            "guest_phone": "(990) 317-6213",
            "id": "d3f15a82-c9c1-4711-95a4-887796a03f60",
            "item_name": "Practical Ceramic Shoes",
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "staff_name": "Vickie Fahey",
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-02T18:38:22.172Z"),
            "url": "https://cluttered-pine.info/",
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

Update a review

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
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "7827eec4-0aec-4f73-8eaa-d9bfff0aa312",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "6c1920c5-9d97-4c8e-8101-fab6890d142e",
                    "metadata": [
                        {
                            "id": "8fa9f37b-add4-4014-a560-3cf7e2f1a4d7",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "3d6d9ddf-b7c4-4a40-bf2d-3f6f49585242",
                    "metadata": [
                        {
                            "id": "594101df-a3cd-47db-ae34-da4817d57d2c",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "6dda4eb7-7084-49c5-b72c-7ff5db8554c1",
                    "metadata": [
                        {
                            "id": "f798145d-e8ca-473c-a88a-c334e182f898",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-08-17T02:33:08.472Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
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

Update a saleschannel

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
            "id": "01a23697-959d-4e58-85c7-74a36d2a4433",
            "is_active": False,
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-01-24T16:44:19.994Z"),
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

Remove a collection

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

Remove an inventory

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

Remove a location

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

Remove a reservation

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

Remove a review

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

Remove a saleschannel

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

Update a collection

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
            "id": "997ee7a0-a8ff-4556-8128-0b61c516bf06",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "9441d2c1-c6ca-49e1-8ebf-b1a4cbabcc51",
                    "metadata": [
                        {
                            "id": "830a9af8-509d-4c84-9782-aaf265f855ff",
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
                    "id": "09d190c1-f53b-454e-bf71-590cfc511276",
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
            "updated_at": parse_datetime("2025-03-12T10:28:32.483Z"),
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

Update an inventory

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
            "updated_at": parse_datetime("2025-11-16T06:38:37.023Z"),
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

    res = unified_to.commerce.update_commerce_item(request={
        "commerce_item": {
            "collections": [],
            "created_at": parse_datetime("2019-06-21T20:16:18.628Z"),
            "description": "Vulnero ustulo abeo.",
            "duration": 87.0,
            "global_code": "calamitas",
            "id": "8bc796cc-ddee-4cb9-bd76-99fb8a3371ce",
            "is_active": False,
            "is_featured": True,
            "is_taxable": True,
            "is_visible": True,
            "media": [
                {
                    "alt": "Caterva eveniet acies candidus.",
                    "height": 663.0,
                    "id": "5bd4418f-1412-47be-ad89-6fbb136aa5f0",
                    "metadata": [
                        {
                            "id": "2a957115-2d92-47a4-9794-f69ab94044e0",
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
                    "id": "e5d33be6-1a30-4092-9235-623277a08650",
                    "metadata": [
                        {
                            "id": "c469c97a-170d-4ba1-b12c-5637a8e7a19f",
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
                    "id": "2eed0374-b275-46e9-a9d3-5b14261d4a91",
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
            "updated_at": parse_datetime("2022-04-17T12:34:09.633Z"),
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

    res = unified_to.commerce.update_commerce_itemvariant(request={
        "commerce_itemvariant": {
            "available_at": parse_datetime("2022-02-02T16:10:33.503Z"),
            "created_at": parse_datetime("2022-01-20T13:49:12.968Z"),
            "description": "Featuring Helium-enhanced technology, our Chips offers unparalleled helpful performance",
            "height": 52.0,
            "id": "42d11ae6-5c61-4d18-b593-c1e1de50b539",
            "is_active": False,
            "is_featured": False,
            "is_visible": False,
            "length": 94.0,
            "media": [
                {
                    "alt": "Calcar delibero cursim summisse.",
                    "height": 394.0,
                    "id": "370c4222-92a0-419e-80b0-c733439275b9",
                    "metadata": [
                        {
                            "id": "7d6edbba-78d1-4f20-9c79-fd078a040ed1",
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
                    "id": "e22d9f93-0727-40f7-9c57-a960216cccdb",
                    "metadata": [
                        {
                            "id": "d2b39e90-a163-4c21-9099-cb626af96f87",
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
                    "id": "b522b344-5246-4671-8799-51d523381ab5",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "nihil",
                },
            ],
            "name": "Keyboard",
            "options": [
                {
                    "id": "722af448-dab3-48a1-a785-a9529cd6af05",
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
            "updated_at": parse_datetime("2025-06-13T09:22:25.204Z"),
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

## update_commerce_location

Update a location

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
            "id": "14a07798-1753-415f-8717-8baa84028c2e",
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
                    "id": "578ef951-b12c-4009-9d90-cbc858fa8efa",
                    "metadata": [
                        {
                            "id": "06d1c0a8-42ef-4674-adb8-eccf57dd3ac3",
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
            "updated_at": parse_datetime("2024-04-18T23:37:40.697Z"),
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

Update a reservation

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
            "guest_email": "Sunny.Strosin77@yahoo.com",
            "guest_name": "Annette Franecki",
            "guest_phone": "(990) 317-6213",
            "id": "d3f15a82-c9c1-4711-95a4-887796a03f60",
            "item_name": "Practical Ceramic Shoes",
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "staff_name": "Vickie Fahey",
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-02T18:38:22.172Z"),
            "url": "https://cluttered-pine.info/",
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

Update a review

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
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "7827eec4-0aec-4f73-8eaa-d9bfff0aa312",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "6c1920c5-9d97-4c8e-8101-fab6890d142e",
                    "metadata": [
                        {
                            "id": "8fa9f37b-add4-4014-a560-3cf7e2f1a4d7",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "3d6d9ddf-b7c4-4a40-bf2d-3f6f49585242",
                    "metadata": [
                        {
                            "id": "594101df-a3cd-47db-ae34-da4817d57d2c",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "6dda4eb7-7084-49c5-b72c-7ff5db8554c1",
                    "metadata": [
                        {
                            "id": "f798145d-e8ca-473c-a88a-c334e182f898",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-08-17T02:33:08.472Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
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

Update a saleschannel

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
            "id": "01a23697-959d-4e58-85c7-74a36d2a4433",
            "is_active": False,
            "slug": "amiculum-congregatio-suspendo",
            "updated_at": parse_datetime("2025-01-24T16:44:19.994Z"),
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