# Listing

## Overview

### Available Operations

* [create_property_listing](#create_property_listing) - Create a listing
* [get_property_listing](#get_property_listing) - Retrieve a listing
* [list_property_listings](#list_property_listings) - List all listings
* [patch_property_listing](#patch_property_listing) - Update a listing
* [remove_property_listing](#remove_property_listing) - Remove a listing
* [update_property_listing](#update_property_listing) - Update a listing

## create_property_listing

Creates a PropertyListing. Provide the unified PropertyListing fields in the request body; they are mapped to the provider's API. Returns the created PropertyListing.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyListing" method="post" path="/property/{connection_id}/listing" example="property_listing" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.create_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "7424 1st Avenue",
                "city": "Porterville",
                "country": "United States",
                "country_code": "US",
                "postal_code": "95594-3059",
                "region": "Louisiana",
                "region_code": "ID",
            },
            "amenities": [
                "Wifi",
                "Kitchen",
                "Free parking",
            ],
            "bathrooms": 1.0,
            "bedrooms": 4.0,
            "beds": 8.0,
            "channels": [
                {
                    "name": "Booking.com",
                    "web_url": "https://gentle-flat.name",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cruentus demoror censura caveo sponte statim. Cursim angulus arbitro barba summopere subnecto curto vulticulus comparo surgo. Carmen deputo defluo abscido conatus arbustum sequi abbas complectus demum.",
            "house_rules": "No smoking. No parties or events.",
            "id": "0354d22b-2e03-453d-b659-44aa5dfa9dcc",
            "image_urls": [
                "https://picsum.photos/seed/cCdY57x3Vw/2822/2061",
                "https://picsum.photos/seed/nH6zsBCr/1004/2259",
            ],
            "latitude": -73.4369,
            "longitude": 97.314,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "ironclad Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-10-04T04:40:28.750Z"),
            "web_url": "https://oval-junior.info",
        },
        "connection_id": "<id>",
    })

    assert res.property_listing is not None

    # Handle response
    print(res.property_listing)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePropertyListingRequest](../../models/operations/createpropertylistingrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreatePropertyListingResponse](../../models/operations/createpropertylistingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_listing

Retrieves a single PropertyListing by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyListing" method="get" path="/property/{connection_id}/listing/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.get_property_listing(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_listing is not None

    # Handle response
    print(res.property_listing)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetPropertyListingRequest](../../models/operations/getpropertylistingrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetPropertyListingResponse](../../models/operations/getpropertylistingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_listings

Returns a list of PropertyListings. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyListings" method="get" path="/property/{connection_id}/listing" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.list_property_listings(request={
        "connection_id": "<id>",
    })

    assert res.property_listings is not None

    # Handle response
    print(res.property_listings)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListPropertyListingsRequest](../../models/operations/listpropertylistingsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListPropertyListingsResponse](../../models/operations/listpropertylistingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_property_listing

Updates the PropertyListing identified by `id`. Provide the unified PropertyListing fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPropertyListing" method="patch" path="/property/{connection_id}/listing/{id}" example="property_listing" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.patch_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "7424 1st Avenue",
                "city": "Porterville",
                "country": "United States",
                "country_code": "US",
                "postal_code": "95594-3059",
                "region": "Louisiana",
                "region_code": "ID",
            },
            "amenities": [
                "Wifi",
                "Kitchen",
                "Free parking",
            ],
            "bathrooms": 1.0,
            "bedrooms": 4.0,
            "beds": 8.0,
            "channels": [
                {
                    "name": "Booking.com",
                    "web_url": "https://gentle-flat.name",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cruentus demoror censura caveo sponte statim. Cursim angulus arbitro barba summopere subnecto curto vulticulus comparo surgo. Carmen deputo defluo abscido conatus arbustum sequi abbas complectus demum.",
            "house_rules": "No smoking. No parties or events.",
            "id": "40f9db50-af31-429b-b1b3-731a8339dc60",
            "image_urls": [
                "https://picsum.photos/seed/cCdY57x3Vw/2822/2061",
                "https://picsum.photos/seed/nH6zsBCr/1004/2259",
            ],
            "latitude": -73.4369,
            "longitude": 97.314,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "ironclad Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-10-04T04:40:28.780Z"),
            "web_url": "https://oval-junior.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_listing is not None

    # Handle response
    print(res.property_listing)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchPropertyListingRequest](../../models/operations/patchpropertylistingrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchPropertyListingResponse](../../models/operations/patchpropertylistingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_property_listing

Deletes the PropertyListing identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePropertyListing" method="delete" path="/property/{connection_id}/listing/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.remove_property_listing(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemovePropertyListingRequest](../../models/operations/removepropertylistingrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemovePropertyListingResponse](../../models/operations/removepropertylistingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_property_listing

Updates the PropertyListing identified by `id`. Provide the unified PropertyListing fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePropertyListing" method="put" path="/property/{connection_id}/listing/{id}" example="property_listing" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.listing.update_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "7424 1st Avenue",
                "city": "Porterville",
                "country": "United States",
                "country_code": "US",
                "postal_code": "95594-3059",
                "region": "Louisiana",
                "region_code": "ID",
            },
            "amenities": [
                "Wifi",
                "Kitchen",
                "Free parking",
            ],
            "bathrooms": 1.0,
            "bedrooms": 4.0,
            "beds": 8.0,
            "channels": [
                {
                    "name": "Booking.com",
                    "web_url": "https://gentle-flat.name",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cruentus demoror censura caveo sponte statim. Cursim angulus arbitro barba summopere subnecto curto vulticulus comparo surgo. Carmen deputo defluo abscido conatus arbustum sequi abbas complectus demum.",
            "house_rules": "No smoking. No parties or events.",
            "id": "40f9db50-af31-429b-b1b3-731a8339dc60",
            "image_urls": [
                "https://picsum.photos/seed/cCdY57x3Vw/2822/2061",
                "https://picsum.photos/seed/nH6zsBCr/1004/2259",
            ],
            "latitude": -73.4369,
            "longitude": 97.314,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "ironclad Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-10-04T04:40:28.780Z"),
            "web_url": "https://oval-junior.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_listing is not None

    # Handle response
    print(res.property_listing)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePropertyListingRequest](../../models/operations/updatepropertylistingrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdatePropertyListingResponse](../../models/operations/updatepropertylistingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |