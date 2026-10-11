# Location

## Overview

### Available Operations

* [create_commerce_location](#create_commerce_location) - Create a location
* [create_hris_location](#create_hris_location) - Create a location
* [get_clubs_location](#get_clubs_location) - Retrieve a location
* [get_commerce_location](#get_commerce_location) - Retrieve a location
* [get_hris_location](#get_hris_location) - Retrieve a location
* [list_clubs_locations](#list_clubs_locations) - List all locations
* [list_commerce_locations](#list_commerce_locations) - List all locations
* [list_hris_locations](#list_hris_locations) - List all locations
* [patch_commerce_location](#patch_commerce_location) - Update a location
* [patch_hris_location](#patch_hris_location) - Update a location
* [remove_commerce_location](#remove_commerce_location) - Remove a location
* [remove_hris_location](#remove_hris_location) - Remove a location
* [update_commerce_location](#update_commerce_location) - Update a location
* [update_hris_location](#update_hris_location) - Update a location

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

    res = unified_to.location.create_commerce_location(request={
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
            "id": "3d7eb4c9-224d-4192-909a-ffee9511a2d6",
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
                    "id": "81a94236-8cdf-4d10-b3f3-892e5a415dd9",
                    "metadata": [
                        {
                            "id": "369a99a4-0314-496e-b8fb-b6dd2cc284e0",
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
            "updated_at": parse_datetime("2024-04-17T07:27:52.972Z"),
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

## create_hris_location

Create a location

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisLocation" method="post" path="/hris/{connection_id}/location" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.create_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "a95fb085-1de2-4952-a92c-4b2d394ad136",
            "id": "71d77c71-c403-4af9-b84d-9873ee590086",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-17T10:41:43.024Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisLocationRequest](../../models/operations/createhrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisLocationResponse](../../models/operations/createhrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_location

Retrieve a location

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsLocation" method="get" path="/clubs/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.get_clubs_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_location is not None

    # Handle response
    print(res.clubs_location)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetClubsLocationRequest](../../models/operations/getclubslocationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetClubsLocationResponse](../../models/operations/getclubslocationresponse.md)**

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

    res = unified_to.location.get_commerce_location(request={
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

## get_hris_location

Retrieve a location

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisLocation" method="get" path="/hris/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.get_hris_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisLocationRequest](../../models/operations/gethrislocationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisLocationResponse](../../models/operations/gethrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_locations

List all locations

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsLocations" method="get" path="/clubs/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.list_clubs_locations(request={
        "connection_id": "<id>",
    })

    assert res.clubs_locations is not None

    # Handle response
    print(res.clubs_locations)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListClubsLocationsRequest](../../models/operations/listclubslocationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListClubsLocationsResponse](../../models/operations/listclubslocationsresponse.md)**

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

    res = unified_to.location.list_commerce_locations(request={
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

## list_hris_locations

List all locations

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisLocations" method="get" path="/hris/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.list_hris_locations(request={
        "connection_id": "<id>",
    })

    assert res.hris_locations is not None

    # Handle response
    print(res.hris_locations)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisLocationsRequest](../../models/operations/listhrislocationsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisLocationsResponse](../../models/operations/listhrislocationsresponse.md)**

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

    res = unified_to.location.patch_commerce_location(request={
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
            "id": "807edb13-f876-457a-98dd-258282cc6997",
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
                    "id": "4c1f73b2-fee9-4130-a73e-8e0f227a6cf0",
                    "metadata": [
                        {
                            "id": "0a9a7714-e2ce-49e5-9936-149141d0e05f",
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
            "updated_at": parse_datetime("2024-04-17T07:27:52.982Z"),
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

## patch_hris_location

Update a location

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisLocation" method="patch" path="/hris/{connection_id}/location/{id}" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.patch_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "019aebc6-abcb-41bd-842e-f9315e842363",
            "id": "bf9eb454-3fd7-45f7-8a51-2b1635dfe888",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-17T10:41:43.030Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisLocationRequest](../../models/operations/patchhrislocationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisLocationResponse](../../models/operations/patchhrislocationresponse.md)**

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

    res = unified_to.location.remove_commerce_location(request={
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

## remove_hris_location

Remove a location

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisLocation" method="delete" path="/hris/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.remove_hris_location(request={
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
| `request`                                                                                    | [operations.RemoveHrisLocationRequest](../../models/operations/removehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisLocationResponse](../../models/operations/removehrislocationresponse.md)**

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

    res = unified_to.location.update_commerce_location(request={
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
            "id": "807edb13-f876-457a-98dd-258282cc6997",
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
                    "id": "4c1f73b2-fee9-4130-a73e-8e0f227a6cf0",
                    "metadata": [
                        {
                            "id": "0a9a7714-e2ce-49e5-9936-149141d0e05f",
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
            "updated_at": parse_datetime("2024-04-17T07:27:52.982Z"),
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

## update_hris_location

Update a location

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisLocation" method="put" path="/hris/{connection_id}/location/{id}" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.location.update_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "019aebc6-abcb-41bd-842e-f9315e842363",
            "id": "bf9eb454-3fd7-45f7-8a51-2b1635dfe888",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-17T10:41:43.030Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisLocationRequest](../../models/operations/updatehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisLocationResponse](../../models/operations/updatehrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |