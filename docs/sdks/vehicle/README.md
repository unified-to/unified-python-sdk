# Vehicle

## Overview

### Available Operations

* [create_dms_vehicle](#create_dms_vehicle) - Create a vehicle
* [get_dms_vehicle](#get_dms_vehicle) - Retrieve a vehicle
* [list_dms_vehicles](#list_dms_vehicles) - List all vehicles
* [patch_dms_vehicle](#patch_dms_vehicle) - Update a vehicle
* [update_dms_vehicle](#update_dms_vehicle) - Update a vehicle

## create_dms_vehicle

Creates a DmsVehicle. Provide the unified DmsVehicle fields in the request body; they are mapped to the provider's API. Returns the created DmsVehicle.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsVehicle" method="post" path="/dms/{connection_id}/vehicle" example="dms_vehicle" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vehicle.create_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "4358dccb-bdc7-4288-b764-0e780bf0e448",
            "image_urls": [
                "https://picsum.photos/seed/tOUr5K/1358/1877",
            ],
            "interior_color": "Black",
            "internet_price_amount": 29526.0,
            "is_active": True,
            "is_certified": False,
            "is_inventory": True,
            "is_published": False,
            "make": "Citroën",
            "metadata": [],
            "model": "Silverado",
            "model_code": "PMU8KI",
            "msrp_amount": 33100.0,
            "odometer": 1.0,
            "odometer_unit": shared.DmsVehicleOdometerUnit.MILES,
            "options": [
                {
                    "code": "SXE",
                    "cost_amount": 250.0,
                    "description": "Tow package",
                    "price_amount": 1400.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
                {
                    "code": "458",
                    "cost_amount": 700.0,
                    "description": "Tow package",
                    "price_amount": 600.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
            ],
            "price_amount": 29926.0,
            "received_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "status": shared.DmsVehicleStatus.OTHER,
            "stock_number": "N24959",
            "transmission": "Manual",
            "trim": "Base",
            "type": shared.DmsVehicleType.SUV,
            "updated_at": parse_datetime("2023-11-03T14:01:02.539Z"),
            "vin": "C29ZDU474DDR70955",
            "warranty_expires_at": parse_datetime("2022-03-28T09:10:09.889Z"),
            "year": 2023.0,
        },
        "connection_id": "<id>",
    })

    assert res.dms_vehicle is not None

    # Handle response
    print(res.dms_vehicle)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateDmsVehicleRequest](../../models/operations/createdmsvehiclerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateDmsVehicleResponse](../../models/operations/createdmsvehicleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_vehicle

Retrieves a single DmsVehicle by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsVehicle" method="get" path="/dms/{connection_id}/vehicle/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vehicle.get_dms_vehicle(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehicle is not None

    # Handle response
    print(res.dms_vehicle)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDmsVehicleRequest](../../models/operations/getdmsvehiclerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetDmsVehicleResponse](../../models/operations/getdmsvehicleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_vehicles

Returns a list of DmsVehicles. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsVehicles" method="get" path="/dms/{connection_id}/vehicle" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vehicle.list_dms_vehicles(request={
        "connection_id": "<id>",
    })

    assert res.dms_vehicles is not None

    # Handle response
    print(res.dms_vehicles)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListDmsVehiclesRequest](../../models/operations/listdmsvehiclesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListDmsVehiclesResponse](../../models/operations/listdmsvehiclesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_vehicle

Updates the DmsVehicle identified by `id`. Provide the unified DmsVehicle fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsVehicle" method="patch" path="/dms/{connection_id}/vehicle/{id}" example="dms_vehicle" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vehicle.patch_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "21719c3c-cbfa-402c-aa76-52b9e5c4fbce",
            "image_urls": [
                "https://picsum.photos/seed/tOUr5K/1358/1877",
            ],
            "interior_color": "Black",
            "internet_price_amount": 29526.0,
            "is_active": True,
            "is_certified": False,
            "is_inventory": True,
            "is_published": False,
            "make": "Citroën",
            "metadata": [],
            "model": "Silverado",
            "model_code": "PMU8KI",
            "msrp_amount": 33100.0,
            "odometer": 1.0,
            "odometer_unit": shared.DmsVehicleOdometerUnit.MILES,
            "options": [
                {
                    "code": "SXE",
                    "cost_amount": 250.0,
                    "description": "Tow package",
                    "price_amount": 1400.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
                {
                    "code": "458",
                    "cost_amount": 700.0,
                    "description": "Tow package",
                    "price_amount": 600.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
            ],
            "price_amount": 29926.0,
            "received_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "status": shared.DmsVehicleStatus.OTHER,
            "stock_number": "N24959",
            "transmission": "Manual",
            "trim": "Base",
            "type": shared.DmsVehicleType.SUV,
            "updated_at": parse_datetime("2023-11-03T14:01:02.556Z"),
            "vin": "C29ZDU474DDR70955",
            "warranty_expires_at": parse_datetime("2022-03-28T09:10:09.889Z"),
            "year": 2023.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehicle is not None

    # Handle response
    print(res.dms_vehicle)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchDmsVehicleRequest](../../models/operations/patchdmsvehiclerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchDmsVehicleResponse](../../models/operations/patchdmsvehicleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_vehicle

Updates the DmsVehicle identified by `id`. Provide the unified DmsVehicle fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsVehicle" method="put" path="/dms/{connection_id}/vehicle/{id}" example="dms_vehicle" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vehicle.update_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "21719c3c-cbfa-402c-aa76-52b9e5c4fbce",
            "image_urls": [
                "https://picsum.photos/seed/tOUr5K/1358/1877",
            ],
            "interior_color": "Black",
            "internet_price_amount": 29526.0,
            "is_active": True,
            "is_certified": False,
            "is_inventory": True,
            "is_published": False,
            "make": "Citroën",
            "metadata": [],
            "model": "Silverado",
            "model_code": "PMU8KI",
            "msrp_amount": 33100.0,
            "odometer": 1.0,
            "odometer_unit": shared.DmsVehicleOdometerUnit.MILES,
            "options": [
                {
                    "code": "SXE",
                    "cost_amount": 250.0,
                    "description": "Tow package",
                    "price_amount": 1400.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
                {
                    "code": "458",
                    "cost_amount": 700.0,
                    "description": "Tow package",
                    "price_amount": 600.0,
                    "type": shared.DmsVehicleOptionType.DEALER,
                },
            ],
            "price_amount": 29926.0,
            "received_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "status": shared.DmsVehicleStatus.OTHER,
            "stock_number": "N24959",
            "transmission": "Manual",
            "trim": "Base",
            "type": shared.DmsVehicleType.SUV,
            "updated_at": parse_datetime("2023-11-03T14:01:02.556Z"),
            "vin": "C29ZDU474DDR70955",
            "warranty_expires_at": parse_datetime("2022-03-28T09:10:09.889Z"),
            "year": 2023.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehicle is not None

    # Handle response
    print(res.dms_vehicle)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateDmsVehicleRequest](../../models/operations/updatedmsvehiclerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateDmsVehicleResponse](../../models/operations/updatedmsvehicleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |