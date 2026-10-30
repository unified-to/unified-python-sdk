# Guest

## Overview

### Available Operations

* [create_property_guest](#create_property_guest) - Create a guest
* [get_property_guest](#get_property_guest) - Retrieve a guest
* [list_property_guests](#list_property_guests) - List all guests
* [patch_property_guest](#patch_property_guest) - Update a guest
* [update_property_guest](#update_property_guest) - Update a guest

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

    res = unified_to.guest.create_property_guest(request={
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
            "id": "3ab96698-bfbc-4eb7-9044-3adc4ae04822",
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
            "updated_at": parse_datetime("2025-07-03T13:46:20.304Z"),
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

    res = unified_to.guest.get_property_guest(request={
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

    res = unified_to.guest.list_property_guests(request={
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

    res = unified_to.guest.patch_property_guest(request={
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
            "id": "4e5184a6-781d-4dd2-aa29-4c22b88ebd99",
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
            "updated_at": parse_datetime("2025-07-03T13:46:20.324Z"),
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

    res = unified_to.guest.update_property_guest(request={
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
            "id": "4e5184a6-781d-4dd2-aa29-4c22b88ebd99",
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
            "updated_at": parse_datetime("2025-07-03T13:46:20.324Z"),
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