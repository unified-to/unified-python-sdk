# Property

## Overview

### Available Operations

* [create_analytics_property](#create_analytics_property) - Create a property
* [create_property_conversation](#create_property_conversation) - Create a conversation
* [create_property_guest](#create_property_guest) - Create a guest
* [create_property_listing](#create_property_listing) - Create a listing
* [create_property_quote](#create_property_quote) - Create a quote
* [create_property_reservation](#create_property_reservation) - Create a reservation
* [get_analytics_property](#get_analytics_property) - Retrieve a property
* [get_property_conversation](#get_property_conversation) - Retrieve a conversation
* [get_property_guest](#get_property_guest) - Retrieve a guest
* [get_property_listing](#get_property_listing) - Retrieve a listing
* [get_property_reservation](#get_property_reservation) - Retrieve a reservation
* [get_property_review](#get_property_review) - Retrieve a review
* [get_property_unittype](#get_property_unittype) - Retrieve an unittype
* [list_analytics_properties](#list_analytics_properties) - List all properties
* [list_property_availabilities](#list_property_availabilities) - List all availabilities
* [list_property_conversations](#list_property_conversations) - List all conversations
* [list_property_guests](#list_property_guests) - List all guests
* [list_property_listings](#list_property_listings) - List all listings
* [list_property_reservations](#list_property_reservations) - List all reservations
* [list_property_reviews](#list_property_reviews) - List all reviews
* [list_property_unittypes](#list_property_unittypes) - List all unittypes
* [patch_analytics_property](#patch_analytics_property) - Update a property
* [patch_property_guest](#patch_property_guest) - Update a guest
* [patch_property_listing](#patch_property_listing) - Update a listing
* [patch_property_reservation](#patch_property_reservation) - Update a reservation
* [patch_property_review](#patch_property_review) - Update a review
* [remove_analytics_property](#remove_analytics_property) - Remove a property
* [remove_property_listing](#remove_property_listing) - Remove a listing
* [update_analytics_property](#update_analytics_property) - Update a property
* [update_property_guest](#update_property_guest) - Update a guest
* [update_property_listing](#update_property_listing) - Update a listing
* [update_property_reservation](#update_property_reservation) - Update a reservation
* [update_property_review](#update_property_review) - Update a review

## create_analytics_property

Creates a AnalyticsProperty. Provide the unified AnalyticsProperty fields in the request body; they are mapped to the provider's API. Returns the created AnalyticsProperty.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsProperty" method="post" path="/analytics/{connection_id}/property" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "356b761c-5c80-454e-a1a3-d5679bfc615f",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:35:17.508Z"),
        },
        "connection_id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAnalyticsPropertyRequest](../../models/operations/createanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAnalyticsPropertyResponse](../../models/operations/createanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_property_conversation

Creates a PropertyConversation. Provide the unified PropertyConversation fields in the request body; they are mapped to the provider's API. Returns the created PropertyConversation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyConversation" method="post" path="/property/{connection_id}/conversation" example="property_conversation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_property_conversation(request={
        "property_conversation": {
            "created_at": parse_datetime("2022-06-20T00:02:46.530Z"),
            "guest_name": "Evie Okuneva",
            "id": "278f6fbd-dbe3-4fae-8ef3-f12c4c287b08",
            "is_unread": False,
            "messages": [
                {
                    "attachments": [],
                    "created_at": parse_datetime("2025-04-22T23:30:42.003Z"),
                    "id": "ea884b5c-bba9-4360-9ceb-a2ebd2cc9e45",
                    "is_automatic": False,
                    "message": "Vinitor caterva amor sophismata admitto colo tempore aufero torrens.",
                    "sender_name": "Evie Okuneva",
                    "sender_type": shared.SenderType.GUEST,
                },
                {
                    "attachments": [],
                    "created_at": parse_datetime("2026-05-06T10:57:43.865Z"),
                    "id": "b89d74c0-0765-4b04-84f4-075103e00b13",
                    "message": "Aequitas torqueo curiositas cimentarius repellendus auditor degero ademptio adnuo.",
                    "sender_name": "Ms. Patti Lynch",
                    "sender_type": shared.SenderType.HOST,
                },
            ],
            "metadata": [],
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-05-06T10:57:43.865Z"),
        },
        "connection_id": "<id>",
    })

    assert res.property_conversation is not None

    # Handle response
    print(res.property_conversation)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreatePropertyConversationRequest](../../models/operations/createpropertyconversationrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreatePropertyConversationResponse](../../models/operations/createpropertyconversationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_property_guest

Creates a PropertyGuest. Provide the unified PropertyGuest fields in the request body; they are mapped to the provider's API. Returns the created PropertyGuest.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyGuest" method="post" path="/property/{connection_id}/guest" example="property_guest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_property_guest(request={
        "property_guest": {
            "address": {
                "address1": "874 Rice Trafficway",
                "city": "East Dollyside",
                "country": "Cameroon",
                "country_code": "MX",
                "postal_code": "51113-4329",
                "region": "Missouri",
            },
            "company_name": "Kertzmann, Bednar and Bashirian",
            "created_at": parse_datetime("2021-10-17T05:59:05.070Z"),
            "emails": [
                {
                    "email": "melissa.green@icloud.com",
                    "type": shared.PropertyEmailType.HOME,
                },
            ],
            "first_name": "Melissa",
            "id": "92181be2-9857-410c-8369-42b2b541547b",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/36.jpg",
            "language": "es",
            "last_name": "Green",
            "metadata": [],
            "name": "Melissa Green",
            "nationality": "SI",
            "notes": "Minus incidunt corporis.",
            "telephones": [
                {
                    "telephone": "+14564841285",
                    "type": shared.PropertyTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2025-07-04T05:01:00.304Z"),
        },
        "connection_id": "<id>",
    })

    assert res.property_guest is not None

    # Handle response
    print(res.property_guest)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePropertyGuestRequest](../../models/operations/createpropertyguestrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreatePropertyGuestResponse](../../models/operations/createpropertyguestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.property.create_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "9262 Bramley Close",
                "city": "New Andrewshire",
                "country": "United States",
                "country_code": "US",
                "postal_code": "53615-4664",
                "region": "Nebraska",
                "region_code": "IL",
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
                    "web_url": "https://frightened-hyphenation.net/",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cuius deputo cruentus demoror censura caveo sponte statim vespillo cursim. Arbitro barba summopere. Curto vulticulus comparo surgo vociferor carmen deputo defluo.",
            "house_rules": "No smoking. No parties or events.",
            "id": "8446e746-d54b-471e-99f8-720b20541cbe",
            "image_urls": [
                "https://loremflickr.com/23/1328?lock=5798241296161663",
                "https://loremflickr.com/12/1312?lock=6354590363728966",
            ],
            "latitude": -5.4327,
            "longitude": 98.9045,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "accurate Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-09-07T17:46:26.386Z"),
            "web_url": "https://tight-pronoun.info/",
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

## create_property_quote

Creates a PropertyQuote. Provide the unified PropertyQuote fields in the request body; they are mapped to the provider's API. Returns the created PropertyQuote.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyQuote" method="post" path="/property/{connection_id}/quote" example="property_quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_property_quote(request={
        "property_quote": {
            "adults": 1.0,
            "children": 1.0,
            "created_at": parse_datetime("2020-12-18T19:14:11.415Z"),
            "currency": "USD",
            "deposit_amount": 594.54,
            "end_at": parse_datetime("2026-11-14"),
            "guests": 2.0,
            "id": "3a6896b1-881f-4e05-ba3d-decd2dffcb6e",
            "line_items": [
                {
                    "amount": 1665.0,
                    "description": "9 nights",
                    "is_mandatory": True,
                    "name": "Accommodation",
                    "type": shared.PropertyLineitemType.BASE,
                },
                {
                    "amount": 117.0,
                    "is_mandatory": True,
                    "name": "Cleaning fee",
                    "type": shared.PropertyLineitemType.FEE,
                },
                {
                    "amount": 199.8,
                    "is_mandatory": True,
                    "name": "Lodging tax",
                    "type": shared.PropertyLineitemType.TAX,
                },
            ],
            "start_at": parse_datetime("2026-11-05"),
            "total_amount": 1981.8,
        },
        "connection_id": "<id>",
    })

    assert res.property_quote is not None

    # Handle response
    print(res.property_quote)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePropertyQuoteRequest](../../models/operations/createpropertyquoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreatePropertyQuoteResponse](../../models/operations/createpropertyquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_property_reservation

Creates a PropertyReservation. Provide the unified PropertyReservation fields in the request body; they are mapped to the provider's API. Returns the created PropertyReservation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyReservation" method="post" path="/property/{connection_id}/reservation" example="property_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.create_property_reservation(request={
        "property_reservation": {
            "adults": 4.0,
            "balance_amount": 2181.6,
            "children": 2.0,
            "confirmation_code": "GNLTDDQ88Z",
            "created_at": parse_datetime("2022-06-03T01:40:03.655Z"),
            "currency": "USD",
            "end_at": parse_datetime("2022-10-06T17:17:08.838Z"),
            "estimated_departure_time": "10:00",
            "guest_email": "anya.parisian@hotmail.com",
            "guest_name": "Anya Parisian",
            "guests": 6.0,
            "id": "3179f48d-be97-45a4-90f6-253d80f87384",
            "line_items": [
                {
                    "amount": 1980.0,
                    "description": "11 nights",
                    "is_mandatory": True,
                    "name": "Accommodation",
                    "type": shared.PropertyLineitemType.BASE,
                },
                {
                    "amount": 162.0,
                    "is_mandatory": True,
                    "name": "Cleaning fee",
                    "type": shared.PropertyLineitemType.FEE,
                },
                {
                    "amount": 237.6,
                    "is_mandatory": True,
                    "name": "Lodging tax",
                    "type": shared.PropertyLineitemType.TAX,
                },
                {
                    "amount": -198.0,
                    "is_mandatory": False,
                    "name": "Weekly discount",
                    "type": shared.PropertyLineitemType.DISCOUNT,
                },
            ],
            "metadata": [],
            "nights": 11.0,
            "notes": "Conculco volaticus vis volva quas trepide vae earum temptatio tertius.",
            "paid_amount": 0.0,
            "pets": 1.0,
            "source": "Vrbo",
            "start_at": parse_datetime("2022-09-25T17:17:08.838Z"),
            "status": shared.PropertyReservationStatus.PENDING,
            "total_amount": 2181.6,
            "updated_at": parse_datetime("2022-11-16T12:57:24.143Z"),
            "web_url": "https://antique-tennis.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.property_reservation is not None

    # Handle response
    print(res.property_reservation)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreatePropertyReservationRequest](../../models/operations/createpropertyreservationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreatePropertyReservationResponse](../../models/operations/createpropertyreservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_property

Retrieves a single AnalyticsProperty by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsProperty" method="get" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_analytics_property(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsPropertyRequest](../../models/operations/getanalyticspropertyrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsPropertyResponse](../../models/operations/getanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_conversation

Retrieves a single PropertyConversation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyConversation" method="get" path="/property/{connection_id}/conversation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_property_conversation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_conversation is not None

    # Handle response
    print(res.property_conversation)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetPropertyConversationRequest](../../models/operations/getpropertyconversationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetPropertyConversationResponse](../../models/operations/getpropertyconversationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_guest

Retrieves a single PropertyGuest by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyGuest" method="get" path="/property/{connection_id}/guest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_property_guest(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_guest is not None

    # Handle response
    print(res.property_guest)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPropertyGuestRequest](../../models/operations/getpropertyguestrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetPropertyGuestResponse](../../models/operations/getpropertyguestresponse.md)**

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

    res = unified_to.property.get_property_listing(request={
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

## get_property_reservation

Retrieves a single PropertyReservation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyReservation" method="get" path="/property/{connection_id}/reservation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_property_reservation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_reservation is not None

    # Handle response
    print(res.property_reservation)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetPropertyReservationRequest](../../models/operations/getpropertyreservationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetPropertyReservationResponse](../../models/operations/getpropertyreservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_review

Retrieves a single PropertyReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyReview" method="get" path="/property/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_property_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPropertyReviewRequest](../../models/operations/getpropertyreviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetPropertyReviewResponse](../../models/operations/getpropertyreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_unittype

Retrieves a single PropertyUnittype by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyUnittype" method="get" path="/property/{connection_id}/unittype/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.get_property_unittype(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_unittype is not None

    # Handle response
    print(res.property_unittype)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPropertyUnittypeRequest](../../models/operations/getpropertyunittyperequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetPropertyUnittypeResponse](../../models/operations/getpropertyunittyperesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_properties

Returns a list of AnalyticsProperties. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsProperties" method="get" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_analytics_properties(request={
        "connection_id": "<id>",
    })

    assert res.analytics_properties is not None

    # Handle response
    print(res.analytics_properties)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAnalyticsPropertiesRequest](../../models/operations/listanalyticspropertiesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAnalyticsPropertiesResponse](../../models/operations/listanalyticspropertiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_availabilities

Returns a list of PropertyAvailabilities. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyAvailabilities" method="get" path="/property/{connection_id}/availability" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_availabilities(request={
        "connection_id": "<id>",
    })

    assert res.property_availabilities is not None

    # Handle response
    print(res.property_availabilities)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListPropertyAvailabilitiesRequest](../../models/operations/listpropertyavailabilitiesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListPropertyAvailabilitiesResponse](../../models/operations/listpropertyavailabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_conversations

Returns a list of PropertyConversations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyConversations" method="get" path="/property/{connection_id}/conversation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_conversations(request={
        "connection_id": "<id>",
    })

    assert res.property_conversations is not None

    # Handle response
    print(res.property_conversations)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListPropertyConversationsRequest](../../models/operations/listpropertyconversationsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListPropertyConversationsResponse](../../models/operations/listpropertyconversationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_guests

Returns a list of PropertyGuests. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyGuests" method="get" path="/property/{connection_id}/guest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_guests(request={
        "connection_id": "<id>",
    })

    assert res.property_guests is not None

    # Handle response
    print(res.property_guests)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPropertyGuestsRequest](../../models/operations/listpropertyguestsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListPropertyGuestsResponse](../../models/operations/listpropertyguestsresponse.md)**

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

    res = unified_to.property.list_property_listings(request={
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

## list_property_reservations

Returns a list of PropertyReservations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyReservations" method="get" path="/property/{connection_id}/reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_reservations(request={
        "connection_id": "<id>",
    })

    assert res.property_reservations is not None

    # Handle response
    print(res.property_reservations)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListPropertyReservationsRequest](../../models/operations/listpropertyreservationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListPropertyReservationsResponse](../../models/operations/listpropertyreservationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_reviews

Returns a list of PropertyReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyReviews" method="get" path="/property/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_reviews(request={
        "connection_id": "<id>",
    })

    assert res.property_reviews is not None

    # Handle response
    print(res.property_reviews)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListPropertyReviewsRequest](../../models/operations/listpropertyreviewsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListPropertyReviewsResponse](../../models/operations/listpropertyreviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_unittypes

Returns a list of PropertyUnittypes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyUnittypes" method="get" path="/property/{connection_id}/unittype" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.list_property_unittypes(request={
        "connection_id": "<id>",
    })

    assert res.property_unittypes is not None

    # Handle response
    print(res.property_unittypes)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListPropertyUnittypesRequest](../../models/operations/listpropertyunittypesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListPropertyUnittypesResponse](../../models/operations/listpropertyunittypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_property

Updates the AnalyticsProperty identified by `id`. Provide the unified AnalyticsProperty fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsProperty" method="patch" path="/analytics/{connection_id}/property/{id}" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.patch_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "00805ab0-d887-43c8-8dc7-e5d63a76401a",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:35:17.508Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAnalyticsPropertyRequest](../../models/operations/patchanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAnalyticsPropertyResponse](../../models/operations/patchanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_property_guest

Updates the PropertyGuest identified by `id`. Provide the unified PropertyGuest fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPropertyGuest" method="patch" path="/property/{connection_id}/guest/{id}" example="property_guest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.patch_property_guest(request={
        "property_guest": {
            "address": {
                "address1": "874 Rice Trafficway",
                "city": "East Dollyside",
                "country": "Cameroon",
                "country_code": "MX",
                "postal_code": "51113-4329",
                "region": "Missouri",
            },
            "company_name": "Kertzmann, Bednar and Bashirian",
            "created_at": parse_datetime("2021-10-17T05:59:05.070Z"),
            "emails": [
                {
                    "email": "melissa.green@icloud.com",
                    "type": shared.PropertyEmailType.HOME,
                },
            ],
            "first_name": "Melissa",
            "id": "92b89f9c-66d7-4090-b134-c76336b53754",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/36.jpg",
            "language": "es",
            "last_name": "Green",
            "metadata": [],
            "name": "Melissa Green",
            "nationality": "SI",
            "notes": "Minus incidunt corporis.",
            "telephones": [
                {
                    "telephone": "+14564841285",
                    "type": shared.PropertyTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2025-07-04T05:01:00.325Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_guest is not None

    # Handle response
    print(res.property_guest)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchPropertyGuestRequest](../../models/operations/patchpropertyguestrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchPropertyGuestResponse](../../models/operations/patchpropertyguestresponse.md)**

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

    res = unified_to.property.patch_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "9262 Bramley Close",
                "city": "New Andrewshire",
                "country": "United States",
                "country_code": "US",
                "postal_code": "53615-4664",
                "region": "Nebraska",
                "region_code": "IL",
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
                    "web_url": "https://frightened-hyphenation.net/",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cuius deputo cruentus demoror censura caveo sponte statim vespillo cursim. Arbitro barba summopere. Curto vulticulus comparo surgo vociferor carmen deputo defluo.",
            "house_rules": "No smoking. No parties or events.",
            "id": "8e727717-cf6c-48ee-8118-6bcfa3baf786",
            "image_urls": [
                "https://loremflickr.com/23/1328?lock=5798241296161663",
                "https://loremflickr.com/12/1312?lock=6354590363728966",
            ],
            "latitude": -5.4327,
            "longitude": 98.9045,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "accurate Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-09-07T17:46:26.414Z"),
            "web_url": "https://tight-pronoun.info/",
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

## patch_property_reservation

Updates the PropertyReservation identified by `id`. Provide the unified PropertyReservation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPropertyReservation" method="patch" path="/property/{connection_id}/reservation/{id}" example="property_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.patch_property_reservation(request={
        "property_reservation": {
            "adults": 4.0,
            "balance_amount": 2181.6,
            "children": 2.0,
            "confirmation_code": "GNLTDDQ88Z",
            "created_at": parse_datetime("2022-06-03T01:40:03.655Z"),
            "currency": "USD",
            "end_at": parse_datetime("2022-10-06T17:17:08.838Z"),
            "estimated_departure_time": "10:00",
            "guest_email": "anya.parisian@hotmail.com",
            "guest_name": "Anya Parisian",
            "guests": 6.0,
            "id": "123c0806-3c83-489e-ac5e-56ebfdccd8b3",
            "line_items": [
                {
                    "amount": 1980.0,
                    "description": "11 nights",
                    "is_mandatory": True,
                    "name": "Accommodation",
                    "type": shared.PropertyLineitemType.BASE,
                },
                {
                    "amount": 162.0,
                    "is_mandatory": True,
                    "name": "Cleaning fee",
                    "type": shared.PropertyLineitemType.FEE,
                },
                {
                    "amount": 237.6,
                    "is_mandatory": True,
                    "name": "Lodging tax",
                    "type": shared.PropertyLineitemType.TAX,
                },
                {
                    "amount": -198.0,
                    "is_mandatory": False,
                    "name": "Weekly discount",
                    "type": shared.PropertyLineitemType.DISCOUNT,
                },
            ],
            "metadata": [],
            "nights": 11.0,
            "notes": "Conculco volaticus vis volva quas trepide vae earum temptatio tertius.",
            "paid_amount": 0.0,
            "pets": 1.0,
            "source": "Vrbo",
            "start_at": parse_datetime("2022-09-25T17:17:08.838Z"),
            "status": shared.PropertyReservationStatus.PENDING,
            "total_amount": 2181.6,
            "updated_at": parse_datetime("2022-11-16T12:57:24.145Z"),
            "web_url": "https://antique-tennis.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_reservation is not None

    # Handle response
    print(res.property_reservation)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchPropertyReservationRequest](../../models/operations/patchpropertyreservationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PatchPropertyReservationResponse](../../models/operations/patchpropertyreservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_property_review

Updates the PropertyReview identified by `id`. Provide the unified PropertyReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPropertyReview" method="patch" path="/property/{connection_id}/review/{id}" example="property_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.patch_property_review(request={
        "property_review": {
            "author_name": "Benton Jast",
            "category_ratings": [
                {
                    "category": shared.PropertyCategoryratingCategory.CLEANLINESS,
                    "comment": "Umquam perferendis amitto voluptas sum blanditiis terreo.",
                    "rating": 5.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.ACCURACY,
                    "comment": "Capitulus dolorem verus.",
                    "rating": 4.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.COMMUNICATION,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.CHECKIN,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.LOCATION,
                    "rating": 2.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.VALUE,
                    "comment": "Quos constans aperte tero sollers.",
                    "rating": 5.0,
                },
            ],
            "content": "Delectus conscendo communis custodia statim. Tutis adsuesco attonbitus comitatus auditor ea tergo nostrum deleo. Comprehendo tertius summopere vaco apparatus incidunt tabula pauci confido colo.",
            "created_at": parse_datetime("2022-10-17T11:17:07.682Z"),
            "id": "7105607c-e96b-4c00-8984-01976ff92170",
            "is_public": True,
            "metadata": [],
            "private_feedback": "Tripudio neque communis.",
            "rating": 3.0,
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-02-19T02:55:03.454Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchPropertyReviewRequest](../../models/operations/patchpropertyreviewrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchPropertyReviewResponse](../../models/operations/patchpropertyreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_property

Deletes the AnalyticsProperty identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsProperty" method="delete" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.remove_analytics_property(request={
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
| `request`                                                                                              | [operations.RemoveAnalyticsPropertyRequest](../../models/operations/removeanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAnalyticsPropertyResponse](../../models/operations/removeanalyticspropertyresponse.md)**

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

    res = unified_to.property.remove_property_listing(request={
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

## update_analytics_property

Updates the AnalyticsProperty identified by `id`. Provide the unified AnalyticsProperty fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsProperty" method="put" path="/analytics/{connection_id}/property/{id}" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.update_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "00805ab0-d887-43c8-8dc7-e5d63a76401a",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:35:17.508Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAnalyticsPropertyRequest](../../models/operations/updateanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAnalyticsPropertyResponse](../../models/operations/updateanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_property_guest

Updates the PropertyGuest identified by `id`. Provide the unified PropertyGuest fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePropertyGuest" method="put" path="/property/{connection_id}/guest/{id}" example="property_guest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.update_property_guest(request={
        "property_guest": {
            "address": {
                "address1": "874 Rice Trafficway",
                "city": "East Dollyside",
                "country": "Cameroon",
                "country_code": "MX",
                "postal_code": "51113-4329",
                "region": "Missouri",
            },
            "company_name": "Kertzmann, Bednar and Bashirian",
            "created_at": parse_datetime("2021-10-17T05:59:05.070Z"),
            "emails": [
                {
                    "email": "melissa.green@icloud.com",
                    "type": shared.PropertyEmailType.HOME,
                },
            ],
            "first_name": "Melissa",
            "id": "92b89f9c-66d7-4090-b134-c76336b53754",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/36.jpg",
            "language": "es",
            "last_name": "Green",
            "metadata": [],
            "name": "Melissa Green",
            "nationality": "SI",
            "notes": "Minus incidunt corporis.",
            "telephones": [
                {
                    "telephone": "+14564841285",
                    "type": shared.PropertyTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2025-07-04T05:01:00.325Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_guest is not None

    # Handle response
    print(res.property_guest)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdatePropertyGuestRequest](../../models/operations/updatepropertyguestrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdatePropertyGuestResponse](../../models/operations/updatepropertyguestresponse.md)**

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

    res = unified_to.property.update_property_listing(request={
        "property_listing": {
            "address": {
                "address1": "9262 Bramley Close",
                "city": "New Andrewshire",
                "country": "United States",
                "country_code": "US",
                "postal_code": "53615-4664",
                "region": "Nebraska",
                "region_code": "IL",
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
                    "web_url": "https://frightened-hyphenation.net/",
                },
            ],
            "check_in_end_time": "22:00",
            "check_in_start_time": "15:00",
            "check_out_time": "11:00",
            "cleaning_fee_amount": 134.0,
            "created_at": parse_datetime("2021-01-08T09:27:35.485Z"),
            "currency": "USD",
            "description": "Cuius deputo cruentus demoror censura caveo sponte statim vespillo cursim. Arbitro barba summopere. Curto vulticulus comparo surgo vociferor carmen deputo defluo.",
            "house_rules": "No smoking. No parties or events.",
            "id": "8e727717-cf6c-48ee-8118-6bcfa3baf786",
            "image_urls": [
                "https://loremflickr.com/23/1328?lock=5798241296161663",
                "https://loremflickr.com/12/1312?lock=6354590363728966",
            ],
            "latitude": -5.4327,
            "longitude": 98.9045,
            "max_nights": 15.0,
            "max_occupancy": 5.0,
            "metadata": [],
            "min_nights": 1.0,
            "name": "accurate Loft",
            "rating": 4.9,
            "review_count": 343.0,
            "start_price_amount": 470.0,
            "timezone": "America/Los_Angeles",
            "type": shared.PropertyListingType.ROOM,
            "updated_at": parse_datetime("2026-09-07T17:46:26.414Z"),
            "web_url": "https://tight-pronoun.info/",
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

## update_property_reservation

Updates the PropertyReservation identified by `id`. Provide the unified PropertyReservation fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePropertyReservation" method="put" path="/property/{connection_id}/reservation/{id}" example="property_reservation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.update_property_reservation(request={
        "property_reservation": {
            "adults": 4.0,
            "balance_amount": 2181.6,
            "children": 2.0,
            "confirmation_code": "GNLTDDQ88Z",
            "created_at": parse_datetime("2022-06-03T01:40:03.655Z"),
            "currency": "USD",
            "end_at": parse_datetime("2022-10-06T17:17:08.838Z"),
            "estimated_departure_time": "10:00",
            "guest_email": "anya.parisian@hotmail.com",
            "guest_name": "Anya Parisian",
            "guests": 6.0,
            "id": "123c0806-3c83-489e-ac5e-56ebfdccd8b3",
            "line_items": [
                {
                    "amount": 1980.0,
                    "description": "11 nights",
                    "is_mandatory": True,
                    "name": "Accommodation",
                    "type": shared.PropertyLineitemType.BASE,
                },
                {
                    "amount": 162.0,
                    "is_mandatory": True,
                    "name": "Cleaning fee",
                    "type": shared.PropertyLineitemType.FEE,
                },
                {
                    "amount": 237.6,
                    "is_mandatory": True,
                    "name": "Lodging tax",
                    "type": shared.PropertyLineitemType.TAX,
                },
                {
                    "amount": -198.0,
                    "is_mandatory": False,
                    "name": "Weekly discount",
                    "type": shared.PropertyLineitemType.DISCOUNT,
                },
            ],
            "metadata": [],
            "nights": 11.0,
            "notes": "Conculco volaticus vis volva quas trepide vae earum temptatio tertius.",
            "paid_amount": 0.0,
            "pets": 1.0,
            "source": "Vrbo",
            "start_at": parse_datetime("2022-09-25T17:17:08.838Z"),
            "status": shared.PropertyReservationStatus.PENDING,
            "total_amount": 2181.6,
            "updated_at": parse_datetime("2022-11-16T12:57:24.145Z"),
            "web_url": "https://antique-tennis.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_reservation is not None

    # Handle response
    print(res.property_reservation)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdatePropertyReservationRequest](../../models/operations/updatepropertyreservationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdatePropertyReservationResponse](../../models/operations/updatepropertyreservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_property_review

Updates the PropertyReview identified by `id`. Provide the unified PropertyReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePropertyReview" method="put" path="/property/{connection_id}/review/{id}" example="property_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.property.update_property_review(request={
        "property_review": {
            "author_name": "Benton Jast",
            "category_ratings": [
                {
                    "category": shared.PropertyCategoryratingCategory.CLEANLINESS,
                    "comment": "Umquam perferendis amitto voluptas sum blanditiis terreo.",
                    "rating": 5.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.ACCURACY,
                    "comment": "Capitulus dolorem verus.",
                    "rating": 4.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.COMMUNICATION,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.CHECKIN,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.LOCATION,
                    "rating": 2.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.VALUE,
                    "comment": "Quos constans aperte tero sollers.",
                    "rating": 5.0,
                },
            ],
            "content": "Delectus conscendo communis custodia statim. Tutis adsuesco attonbitus comitatus auditor ea tergo nostrum deleo. Comprehendo tertius summopere vaco apparatus incidunt tabula pauci confido colo.",
            "created_at": parse_datetime("2022-10-17T11:17:07.682Z"),
            "id": "7105607c-e96b-4c00-8984-01976ff92170",
            "is_public": True,
            "metadata": [],
            "private_feedback": "Tripudio neque communis.",
            "rating": 3.0,
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-02-19T02:55:03.454Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdatePropertyReviewRequest](../../models/operations/updatepropertyreviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdatePropertyReviewResponse](../../models/operations/updatepropertyreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |