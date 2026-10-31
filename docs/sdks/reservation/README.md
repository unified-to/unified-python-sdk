# Reservation

## Overview

### Available Operations

* [create_commerce_reservation](#create_commerce_reservation) - Create a reservation
* [create_property_reservation](#create_property_reservation) - Create a reservation
* [get_commerce_reservation](#get_commerce_reservation) - Retrieve a reservation
* [get_property_reservation](#get_property_reservation) - Retrieve a reservation
* [list_commerce_reservations](#list_commerce_reservations) - List all reservations
* [list_property_reservations](#list_property_reservations) - List all reservations
* [patch_commerce_reservation](#patch_commerce_reservation) - Update a reservation
* [patch_property_reservation](#patch_property_reservation) - Update a reservation
* [remove_commerce_reservation](#remove_commerce_reservation) - Remove a reservation
* [update_commerce_reservation](#update_commerce_reservation) - Update a reservation
* [update_property_reservation](#update_property_reservation) - Update a reservation

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

    res = unified_to.reservation.create_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "f1f4641b-d2c3-4abc-a5e7-896d1d6384d9",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-06T01:02:40.984Z"),
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

    res = unified_to.reservation.create_property_reservation(request={
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

    res = unified_to.reservation.get_commerce_reservation(request={
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

    res = unified_to.reservation.get_property_reservation(request={
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

    res = unified_to.reservation.list_commerce_reservations(request={
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

    res = unified_to.reservation.list_property_reservations(request={
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

    res = unified_to.reservation.patch_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "5d99ac29-04bf-43c6-9aab-7df1740d2d71",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-06T01:02:40.987Z"),
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

    res = unified_to.reservation.patch_property_reservation(request={
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

    res = unified_to.reservation.remove_commerce_reservation(request={
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

    res = unified_to.reservation.update_commerce_reservation(request={
        "commerce_reservation": {
            "created_at": parse_datetime("2021-12-14T19:50:31.151Z"),
            "end_at": parse_datetime("2022-01-01T22:00:17.868Z"),
            "guest_email": "julien.bartoletti@icloud.com",
            "guest_name": "Julien Bartoletti",
            "guest_phone": "(728) 596-2620",
            "id": "5d99ac29-04bf-43c6-9aab-7df1740d2d71",
            "metadata": [],
            "notes": "Adsum textilis ipsum despecto.",
            "size": 10.0,
            "start_at": parse_datetime("2021-12-18T00:40:25.125Z"),
            "status": shared.CommerceReservationStatus.PENDING,
            "updated_at": parse_datetime("2023-01-06T01:02:40.987Z"),
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

    res = unified_to.reservation.update_property_reservation(request={
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