# Dms

## Overview

### Available Operations

* [create_dms_appointment](#create_dms_appointment) - Create an appointment
* [create_dms_opcode](#create_dms_opcode) - Create an opcode
* [create_dms_part](#create_dms_part) - Create a part
* [create_dms_partsale](#create_dms_partsale) - Create a partsale
* [create_dms_repairorder](#create_dms_repairorder) - Create a repairorder
* [create_dms_vehicle](#create_dms_vehicle) - Create a vehicle
* [create_dms_vehiclesale](#create_dms_vehiclesale) - Create a vehiclesale
* [get_dms_appointment](#get_dms_appointment) - Retrieve an appointment
* [get_dms_opcode](#get_dms_opcode) - Retrieve an opcode
* [get_dms_part](#get_dms_part) - Retrieve a part
* [get_dms_partsale](#get_dms_partsale) - Retrieve a partsale
* [get_dms_repairorder](#get_dms_repairorder) - Retrieve a repairorder
* [get_dms_vehicle](#get_dms_vehicle) - Retrieve a vehicle
* [get_dms_vehiclesale](#get_dms_vehiclesale) - Retrieve a vehiclesale
* [list_dms_appointments](#list_dms_appointments) - List all appointments
* [list_dms_opcodes](#list_dms_opcodes) - List all opcodes
* [list_dms_parts](#list_dms_parts) - List all parts
* [list_dms_partsales](#list_dms_partsales) - List all partsales
* [list_dms_repairorders](#list_dms_repairorders) - List all repairorders
* [list_dms_vehicles](#list_dms_vehicles) - List all vehicles
* [list_dms_vehiclesales](#list_dms_vehiclesales) - List all vehiclesales
* [patch_dms_appointment](#patch_dms_appointment) - Update an appointment
* [patch_dms_opcode](#patch_dms_opcode) - Update an opcode
* [patch_dms_part](#patch_dms_part) - Update a part
* [patch_dms_partsale](#patch_dms_partsale) - Update a partsale
* [patch_dms_repairorder](#patch_dms_repairorder) - Update a repairorder
* [patch_dms_vehicle](#patch_dms_vehicle) - Update a vehicle
* [patch_dms_vehiclesale](#patch_dms_vehiclesale) - Update a vehiclesale
* [remove_dms_appointment](#remove_dms_appointment) - Remove an appointment
* [update_dms_appointment](#update_dms_appointment) - Update an appointment
* [update_dms_opcode](#update_dms_opcode) - Update an opcode
* [update_dms_part](#update_dms_part) - Update a part
* [update_dms_partsale](#update_dms_partsale) - Update a partsale
* [update_dms_repairorder](#update_dms_repairorder) - Update a repairorder
* [update_dms_vehicle](#update_dms_vehicle) - Update a vehicle
* [update_dms_vehiclesale](#update_dms_vehiclesale) - Update a vehiclesale

## create_dms_appointment

Creates a DmsAppointment. Provide the unified DmsAppointment fields in the request body; they are mapped to the provider's API. Returns the created DmsAppointment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsAppointment" method="post" path="/dms/{connection_id}/appointment" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.610Z"),
            "id": "430e7b3d-b8dd-439a-b13f-8bdf6962dc64",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "4c2736ea-f419-4ae0-997a-4991e091d780",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "62b7aa53-d974-49b9-a2ae-a89a668b90aa",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "94fb6c00-9163-48d5-8efd-784e629482a9",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.610Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.986Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDmsAppointmentRequest](../../models/operations/createdmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDmsAppointmentResponse](../../models/operations/createdmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dms_opcode

Creates a DmsOpcode. Provide the unified DmsOpcode fields in the request body; they are mapped to the provider's API. Returns the created DmsOpcode.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsOpcode" method="post" path="/dms/{connection_id}/opcode" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "954698ce-2e67-4d5f-83be-eadc7f421dad",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T12:17:13.054Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateDmsOpcodeRequest](../../models/operations/createdmsopcoderequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateDmsOpcodeResponse](../../models/operations/createdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dms_part

Creates a DmsPart. Provide the unified DmsPart fields in the request body; they are mapped to the provider's API. Returns the created DmsPart.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsPart" method="post" path="/dms/{connection_id}/part" example="dms_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "22491d01-65de-41d8-9e74-a6471e5f3b6c",
            "last_sold_at": parse_datetime("2020-11-23T02:58:30.888Z"),
            "list_price_amount": 39.61,
            "manufacturer_code": "TOY",
            "max_stock_quantity": 21.0,
            "metadata": [],
            "min_stock_quantity": 3.0,
            "pack_quantity": 1.0,
            "part_number": "73992-IM3FI",
            "quantity_available": 13.0,
            "quantity_on_hand": 15.0,
            "quantity_on_order": 14.0,
            "source_code": "30",
            "trade_price_amount": 29.05,
            "updated_at": parse_datetime("2023-11-22T17:30:11.488Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_part is not None

    # Handle response
    print(res.dms_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateDmsPartRequest](../../models/operations/createdmspartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateDmsPartResponse](../../models/operations/createdmspartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dms_partsale

Creates a DmsPartsale. Provide the unified DmsPartsale fields in the request body; they are mapped to the provider's API. Returns the created DmsPartsale.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsPartsale" method="post" path="/dms/{connection_id}/partsale" example="dms_partsale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_partsale(request={
        "dms_partsale": {
            "cost_amount": 0.0,
            "created_at": parse_datetime("2023-05-22T03:39:30.335Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "freight_amount": 0.0,
            "id": "8c8fcfa6-dca2-491c-9275-b6a5936d328a",
            "lines": [
                {
                    "id": "3675b135-1418-494c-bbb8-9b768f22c5cd",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "99850d2e-ecde-4846-bc73-e9e1b93c4214",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "49f90062-4f84-478b-a7c0-a8caa949741a",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 3.0,
                    "quantity_ordered": 3.0,
                    "total_amount": 249.54,
                    "unit_price_amount": 83.18,
                },
            ],
            "metadata": [],
            "number": "P292867",
            "pay_type": shared.DmsPartsalePayType.CUSTOMER,
            "status": shared.DmsPartsaleStatus.VOIDED,
            "subtotal_amount": 981.89,
            "tax_amount": 68.73,
            "total_amount": 1050.62,
            "type": shared.DmsPartsaleType.SALE,
            "updated_at": parse_datetime("2026-04-17T16:03:18.260Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_partsale is not None

    # Handle response
    print(res.dms_partsale)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateDmsPartsaleRequest](../../models/operations/createdmspartsalerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateDmsPartsaleResponse](../../models/operations/createdmspartsaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dms_repairorder

Creates a DmsRepairorder. Provide the unified DmsRepairorder fields in the request body; they are mapped to the provider's API. Returns the created DmsRepairorder.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsRepairorder" method="post" path="/dms/{connection_id}/repairorder" example="dms_repairorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_repairorder(request={
        "dms_repairorder": {
            "balance_amount": 3193.86,
            "completed_at": parse_datetime("2026-11-12T19:17:42.253Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "7fb2dd80-bcfa-4c94-8c60-b2d2b9a4343a",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "a3e10710-eaf3-42c0-a284-3b2bb7a069e7",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "9dfd5a09-1f6c-421b-b16c-aed61a5c14e6",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 213.0,
                            "sold_hours": 3.2,
                            "technician_user_ids": [],
                            "total_amount": 681.6,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "A",
                    "parts": [],
                    "parts_amount": 0.0,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.2,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 681.6,
                },
                {
                    "actual_hours": 3.0,
                    "cause": "Worn brake pads",
                    "complaint": "Vibration at highway speed",
                    "correction": "Somnus avaritia utroque vulnero ullam ancilla.",
                    "id": "45a15ebd-8869-4c49-9e59-c8ab00015b01",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "d18cb9c4-81bd-4cd5-bf32-eff004254921",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 144.0,
                            "sold_hours": 3.1,
                            "technician_user_ids": [],
                            "total_amount": 446.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "B",
                    "parts": [
                        {
                            "id": "a9f379cc-9f18-4ac2-9723-7fda4061e45e",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "884c9571-00e2-402a-9c24-6522d26444c3",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 216.18,
                            "unit_price_amount": 108.09,
                        },
                    ],
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.1,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 1553.02,
                },
                {
                    "actual_hours": 1.5,
                    "cause": "Scheduled maintenance",
                    "complaint": "Noise when braking",
                    "correction": "Degero theca natus.",
                    "id": "e20d5136-0721-4308-84ca-8e748a8afbe4",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "18657ec3-723a-4418-9319-fdb6e7cfd8e9",
                            "pay_type": shared.DmsRepairorderLaborPayType.CUSTOMER,
                            "rate_amount": 166.0,
                            "sold_hours": 1.4,
                            "technician_user_ids": [],
                            "total_amount": 232.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "C",
                    "parts": [
                        {
                            "id": "b26e6eaa-eadf-444f-b4be-3438e950d554",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "775ba6c5-dc39-4dfd-9c5e-f2139c2f652f",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 358.16,
                            "unit_price_amount": 179.08,
                        },
                    ],
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.CUSTOMER,
                    "sold_hours": 1.4,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 806.58,
                },
            ],
            "labor_amount": 1360.4,
            "metadata": [],
            "misc_amount": 35.0,
            "number": "143398",
            "odometer_in": 7776.0,
            "odometer_out": 7776.0,
            "odometer_unit": shared.DmsRepairorderOdometerUnit.MILES,
            "opened_at": parse_datetime("2025-02-07T19:13:16.323Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T03:13:16.323Z"),
            "purchase_order_number": "182743",
            "status": shared.DmsRepairorderStatus.COMPLETED,
            "sublet_amount": 0.0,
            "tag_number": "758",
            "tax_amount": 117.66,
            "technician_user_ids": [],
            "total_amount": 3193.86,
            "totals": [
                {
                    "discount_amount": 0.0,
                    "labor_amount": 232.4,
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.CUSTOMER,
                    "sublet_amount": 0.0,
                    "total_amount": 806.58,
                },
                {
                    "discount_amount": 0.0,
                    "labor_amount": 1128.0,
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.WARRANTY,
                    "sublet_amount": 0.0,
                    "total_amount": 2234.62,
                },
            ],
            "transport_type": shared.DmsRepairorderTransportType.LOANER,
            "updated_at": parse_datetime("2025-11-27T22:05:41.752Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_repairorder is not None

    # Handle response
    print(res.dms_repairorder)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDmsRepairorderRequest](../../models/operations/createdmsrepairorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDmsRepairorderResponse](../../models/operations/createdmsrepairorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.dms.create_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "e02606d0-aeac-4d15-872c-6ad4c43411b3",
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
            "updated_at": parse_datetime("2023-11-03T01:42:43.733Z"),
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

## create_dms_vehiclesale

Creates a DmsVehiclesale. Provide the unified DmsVehiclesale fields in the request body; they are mapped to the provider's API. Returns the created DmsVehiclesale.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsVehiclesale" method="post" path="/dms/{connection_id}/vehiclesale" example="dms_vehiclesale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.create_dms_vehiclesale(request={
        "dms_vehiclesale": {
            "back_gross_amount": 4565.0,
            "created_at": parse_datetime("2020-04-02T08:14:56.150Z"),
            "currency": "USD",
            "down_payment_amount": 6700.0,
            "fees": [
                {
                    "cost_amount": 0.0,
                    "is_capitalized": True,
                    "name": "Documentation fee",
                    "price_amount": 499.0,
                },
                {
                    "is_capitalized": False,
                    "name": "Title and registration",
                    "price_amount": 392.0,
                },
            ],
            "finance": {
                "financed_amount": 0.0,
                "first_payment_at": parse_datetime("2022-08-16T02:28:39.768Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "e4fbdb78-a120-48db-8840-3f369b3e43ef",
            "metadata": [],
            "number": "D84591",
            "products": [
                {
                    "contract_number": "B7JN10GVB7",
                    "cost_amount": 1320.0,
                    "name": "Tire & Wheel",
                    "price_amount": 3300.0,
                    "provider": "Renner and Sons",
                    "term_months": 60.0,
                    "type": shared.DmsVehiclesaleProductType.PROTECTION,
                },
                {
                    "contract_number": "VIZU7K3VRU",
                    "cost_amount": 1115.0,
                    "deductible_amount": 100.0,
                    "name": "Platinum Vehicle Service Contract",
                    "price_amount": 3700.0,
                    "provider": "Frami, Wisozk and Gleichner",
                    "term_months": 72.0,
                    "type": shared.DmsVehiclesaleProductType.SERVICE_CONTRACT,
                },
            ],
            "rebate_amount": 500.0,
            "sold_at": parse_datetime("2022-08-14T11:13:05.481Z"),
            "source": "Website",
            "status": shared.DmsVehiclesaleStatus.SOLD,
            "tax_amount": 0.0,
            "taxes": [
                {
                    "name": "State sales tax",
                    "rate": 8.25,
                    "total_amount": 0.0,
                },
            ],
            "total_amount": 7891.0,
            "trade_ins": [],
            "type": shared.DmsVehiclesaleType.RETAIL,
            "updated_at": parse_datetime("2025-04-16T02:25:03.816Z"),
            "vehicles": [],
        },
        "connection_id": "<id>",
    })

    assert res.dms_vehiclesale is not None

    # Handle response
    print(res.dms_vehiclesale)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDmsVehiclesaleRequest](../../models/operations/createdmsvehiclesalerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDmsVehiclesaleResponse](../../models/operations/createdmsvehiclesaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_appointment

Retrieves a single DmsAppointment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsAppointment" method="get" path="/dms/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_appointment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetDmsAppointmentRequest](../../models/operations/getdmsappointmentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetDmsAppointmentResponse](../../models/operations/getdmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_opcode

Retrieves a single DmsOpcode by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsOpcode" method="get" path="/dms/{connection_id}/opcode/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_opcode(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetDmsOpcodeRequest](../../models/operations/getdmsopcoderequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetDmsOpcodeResponse](../../models/operations/getdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_part

Retrieves a single DmsPart by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsPart" method="get" path="/dms/{connection_id}/part/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_part(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_part is not None

    # Handle response
    print(res.dms_part)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetDmsPartRequest](../../models/operations/getdmspartrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetDmsPartResponse](../../models/operations/getdmspartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_partsale

Retrieves a single DmsPartsale by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsPartsale" method="get" path="/dms/{connection_id}/partsale/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_partsale(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_partsale is not None

    # Handle response
    print(res.dms_partsale)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDmsPartsaleRequest](../../models/operations/getdmspartsalerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetDmsPartsaleResponse](../../models/operations/getdmspartsaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dms_repairorder

Retrieves a single DmsRepairorder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsRepairorder" method="get" path="/dms/{connection_id}/repairorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_repairorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_repairorder is not None

    # Handle response
    print(res.dms_repairorder)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetDmsRepairorderRequest](../../models/operations/getdmsrepairorderrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetDmsRepairorderResponse](../../models/operations/getdmsrepairorderresponse.md)**

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

    res = unified_to.dms.get_dms_vehicle(request={
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

## get_dms_vehiclesale

Retrieves a single DmsVehiclesale by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsVehiclesale" method="get" path="/dms/{connection_id}/vehiclesale/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.get_dms_vehiclesale(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehiclesale is not None

    # Handle response
    print(res.dms_vehiclesale)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetDmsVehiclesaleRequest](../../models/operations/getdmsvehiclesalerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetDmsVehiclesaleResponse](../../models/operations/getdmsvehiclesaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_appointments

Returns a list of DmsAppointments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsAppointments" method="get" path="/dms/{connection_id}/appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_appointments(request={
        "connection_id": "<id>",
    })

    assert res.dms_appointments is not None

    # Handle response
    print(res.dms_appointments)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListDmsAppointmentsRequest](../../models/operations/listdmsappointmentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListDmsAppointmentsResponse](../../models/operations/listdmsappointmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_opcodes

Returns a list of DmsOpcodes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsOpcodes" method="get" path="/dms/{connection_id}/opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_opcodes(request={
        "connection_id": "<id>",
    })

    assert res.dms_opcodes is not None

    # Handle response
    print(res.dms_opcodes)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListDmsOpcodesRequest](../../models/operations/listdmsopcodesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListDmsOpcodesResponse](../../models/operations/listdmsopcodesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_parts

Returns a list of DmsParts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsParts" method="get" path="/dms/{connection_id}/part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_parts(request={
        "connection_id": "<id>",
    })

    assert res.dms_parts is not None

    # Handle response
    print(res.dms_parts)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListDmsPartsRequest](../../models/operations/listdmspartsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListDmsPartsResponse](../../models/operations/listdmspartsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_partsales

Returns a list of DmsPartsales. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsPartsales" method="get" path="/dms/{connection_id}/partsale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_partsales(request={
        "connection_id": "<id>",
    })

    assert res.dms_partsales is not None

    # Handle response
    print(res.dms_partsales)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDmsPartsalesRequest](../../models/operations/listdmspartsalesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListDmsPartsalesResponse](../../models/operations/listdmspartsalesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_dms_repairorders

Returns a list of DmsRepairorders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsRepairorders" method="get" path="/dms/{connection_id}/repairorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_repairorders(request={
        "connection_id": "<id>",
    })

    assert res.dms_repairorders is not None

    # Handle response
    print(res.dms_repairorders)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListDmsRepairordersRequest](../../models/operations/listdmsrepairordersrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListDmsRepairordersResponse](../../models/operations/listdmsrepairordersresponse.md)**

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

    res = unified_to.dms.list_dms_vehicles(request={
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

## list_dms_vehiclesales

Returns a list of DmsVehiclesales. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsVehiclesales" method="get" path="/dms/{connection_id}/vehiclesale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.list_dms_vehiclesales(request={
        "connection_id": "<id>",
    })

    assert res.dms_vehiclesales is not None

    # Handle response
    print(res.dms_vehiclesales)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListDmsVehiclesalesRequest](../../models/operations/listdmsvehiclesalesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListDmsVehiclesalesResponse](../../models/operations/listdmsvehiclesalesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_appointment

Updates the DmsAppointment identified by `id`. Provide the unified DmsAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsAppointment" method="patch" path="/dms/{connection_id}/appointment/{id}" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.631Z"),
            "id": "4adcb137-9ab5-4404-99d5-9b49a342578e",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "d7f17954-4053-4eba-a7be-f4016074238d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "52fba2cc-a29d-457d-a0d5-14d9e9481c0d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "c653de4e-1054-4fec-9696-51886b2362b2",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.631Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.998Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchDmsAppointmentRequest](../../models/operations/patchdmsappointmentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchDmsAppointmentResponse](../../models/operations/patchdmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_opcode

Updates the DmsOpcode identified by `id`. Provide the unified DmsOpcode fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsOpcode" method="patch" path="/dms/{connection_id}/opcode/{id}" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "8a3a625f-cde5-4df7-9a76-7e5d72f2508e",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T12:17:13.057Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchDmsOpcodeRequest](../../models/operations/patchdmsopcoderequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchDmsOpcodeResponse](../../models/operations/patchdmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_part

Updates the DmsPart identified by `id`. Provide the unified DmsPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsPart" method="patch" path="/dms/{connection_id}/part/{id}" example="dms_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "a76e2648-fede-463a-ae14-9b48940c3d9a",
            "last_sold_at": parse_datetime("2020-11-23T02:58:30.889Z"),
            "list_price_amount": 39.61,
            "manufacturer_code": "TOY",
            "max_stock_quantity": 21.0,
            "metadata": [],
            "min_stock_quantity": 3.0,
            "pack_quantity": 1.0,
            "part_number": "73992-IM3FI",
            "quantity_available": 13.0,
            "quantity_on_hand": 15.0,
            "quantity_on_order": 14.0,
            "source_code": "30",
            "trade_price_amount": 29.05,
            "updated_at": parse_datetime("2023-11-22T17:30:11.498Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_part is not None

    # Handle response
    print(res.dms_part)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchDmsPartRequest](../../models/operations/patchdmspartrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchDmsPartResponse](../../models/operations/patchdmspartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_partsale

Updates the DmsPartsale identified by `id`. Provide the unified DmsPartsale fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsPartsale" method="patch" path="/dms/{connection_id}/partsale/{id}" example="dms_partsale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_partsale(request={
        "dms_partsale": {
            "cost_amount": 0.0,
            "created_at": parse_datetime("2023-05-22T03:39:30.335Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "freight_amount": 0.0,
            "id": "c577212b-856c-4afa-b866-510023c35189",
            "lines": [
                {
                    "id": "95290c13-4f44-4bb9-92a2-e5dab8e5e43f",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "08f9368b-c157-4968-bdd5-4af302744207",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "8a489684-dbcc-4342-ab28-1caac8e76023",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 3.0,
                    "quantity_ordered": 3.0,
                    "total_amount": 249.54,
                    "unit_price_amount": 83.18,
                },
            ],
            "metadata": [],
            "number": "P292867",
            "pay_type": shared.DmsPartsalePayType.CUSTOMER,
            "status": shared.DmsPartsaleStatus.VOIDED,
            "subtotal_amount": 981.89,
            "tax_amount": 68.73,
            "total_amount": 1050.62,
            "type": shared.DmsPartsaleType.SALE,
            "updated_at": parse_datetime("2026-04-17T16:03:18.289Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_partsale is not None

    # Handle response
    print(res.dms_partsale)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchDmsPartsaleRequest](../../models/operations/patchdmspartsalerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchDmsPartsaleResponse](../../models/operations/patchdmspartsaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_dms_repairorder

Updates the DmsRepairorder identified by `id`. Provide the unified DmsRepairorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsRepairorder" method="patch" path="/dms/{connection_id}/repairorder/{id}" example="dms_repairorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_repairorder(request={
        "dms_repairorder": {
            "balance_amount": 3193.86,
            "completed_at": parse_datetime("2026-11-12T19:17:42.307Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "205d65d6-f300-436e-a728-71ed9ac8cb5c",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "426874d7-2e52-4162-8b6c-8639c58d18b5",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "e1009e6c-2d8d-446c-8269-bcc66c32cd67",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 213.0,
                            "sold_hours": 3.2,
                            "technician_user_ids": [],
                            "total_amount": 681.6,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "A",
                    "parts": [],
                    "parts_amount": 0.0,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.2,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 681.6,
                },
                {
                    "actual_hours": 3.0,
                    "cause": "Worn brake pads",
                    "complaint": "Vibration at highway speed",
                    "correction": "Somnus avaritia utroque vulnero ullam ancilla.",
                    "id": "7a124d15-1bb6-491d-adc1-579be2c00466",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "bf400c19-1912-4255-b38c-bdc5cb87abf6",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 144.0,
                            "sold_hours": 3.1,
                            "technician_user_ids": [],
                            "total_amount": 446.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "B",
                    "parts": [
                        {
                            "id": "5d8d7099-cdda-4146-b08c-46d84fba20a8",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "9a7d805a-b9d9-4663-86e4-0e9b32dba051",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 216.18,
                            "unit_price_amount": 108.09,
                        },
                    ],
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.1,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 1553.02,
                },
                {
                    "actual_hours": 1.5,
                    "cause": "Scheduled maintenance",
                    "complaint": "Noise when braking",
                    "correction": "Degero theca natus.",
                    "id": "8fe8640a-c7a2-4ad5-86ef-a016db57c58a",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "1e1d8015-f3f9-4d90-bede-5f2b99783e47",
                            "pay_type": shared.DmsRepairorderLaborPayType.CUSTOMER,
                            "rate_amount": 166.0,
                            "sold_hours": 1.4,
                            "technician_user_ids": [],
                            "total_amount": 232.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "C",
                    "parts": [
                        {
                            "id": "9237d282-5b87-4e09-bb1f-363fc2a6296e",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "884766ed-b7f1-4902-9a06-1a0837b87653",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 358.16,
                            "unit_price_amount": 179.08,
                        },
                    ],
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.CUSTOMER,
                    "sold_hours": 1.4,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 806.58,
                },
            ],
            "labor_amount": 1360.4,
            "metadata": [],
            "misc_amount": 35.0,
            "number": "143398",
            "odometer_in": 7776.0,
            "odometer_out": 7776.0,
            "odometer_unit": shared.DmsRepairorderOdometerUnit.MILES,
            "opened_at": parse_datetime("2025-02-07T19:13:16.353Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T03:13:16.353Z"),
            "purchase_order_number": "182743",
            "status": shared.DmsRepairorderStatus.COMPLETED,
            "sublet_amount": 0.0,
            "tag_number": "758",
            "tax_amount": 117.66,
            "technician_user_ids": [],
            "total_amount": 3193.86,
            "totals": [
                {
                    "discount_amount": 0.0,
                    "labor_amount": 232.4,
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.CUSTOMER,
                    "sublet_amount": 0.0,
                    "total_amount": 806.58,
                },
                {
                    "discount_amount": 0.0,
                    "labor_amount": 1128.0,
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.WARRANTY,
                    "sublet_amount": 0.0,
                    "total_amount": 2234.62,
                },
            ],
            "transport_type": shared.DmsRepairorderTransportType.LOANER,
            "updated_at": parse_datetime("2025-11-27T22:05:41.793Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_repairorder is not None

    # Handle response
    print(res.dms_repairorder)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchDmsRepairorderRequest](../../models/operations/patchdmsrepairorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchDmsRepairorderResponse](../../models/operations/patchdmsrepairorderresponse.md)**

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

    res = unified_to.dms.patch_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "79085b50-74a7-4f1d-8d69-d4979c6610bf",
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
            "updated_at": parse_datetime("2023-11-03T01:42:43.749Z"),
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

## patch_dms_vehiclesale

Updates the DmsVehiclesale identified by `id`. Provide the unified DmsVehiclesale fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsVehiclesale" method="patch" path="/dms/{connection_id}/vehiclesale/{id}" example="dms_vehiclesale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.patch_dms_vehiclesale(request={
        "dms_vehiclesale": {
            "back_gross_amount": 4565.0,
            "created_at": parse_datetime("2020-04-02T08:14:56.150Z"),
            "currency": "USD",
            "down_payment_amount": 6700.0,
            "fees": [
                {
                    "cost_amount": 0.0,
                    "is_capitalized": True,
                    "name": "Documentation fee",
                    "price_amount": 499.0,
                },
                {
                    "is_capitalized": False,
                    "name": "Title and registration",
                    "price_amount": 392.0,
                },
            ],
            "finance": {
                "financed_amount": 0.0,
                "first_payment_at": parse_datetime("2022-08-16T02:28:39.785Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "9cf21810-137c-43f8-9e85-5b0d7caf29db",
            "metadata": [],
            "number": "D84591",
            "products": [
                {
                    "contract_number": "B7JN10GVB7",
                    "cost_amount": 1320.0,
                    "name": "Tire & Wheel",
                    "price_amount": 3300.0,
                    "provider": "Renner and Sons",
                    "term_months": 60.0,
                    "type": shared.DmsVehiclesaleProductType.PROTECTION,
                },
                {
                    "contract_number": "VIZU7K3VRU",
                    "cost_amount": 1115.0,
                    "deductible_amount": 100.0,
                    "name": "Platinum Vehicle Service Contract",
                    "price_amount": 3700.0,
                    "provider": "Frami, Wisozk and Gleichner",
                    "term_months": 72.0,
                    "type": shared.DmsVehiclesaleProductType.SERVICE_CONTRACT,
                },
            ],
            "rebate_amount": 500.0,
            "sold_at": parse_datetime("2022-08-14T11:13:05.498Z"),
            "source": "Website",
            "status": shared.DmsVehiclesaleStatus.SOLD,
            "tax_amount": 0.0,
            "taxes": [
                {
                    "name": "State sales tax",
                    "rate": 8.25,
                    "total_amount": 0.0,
                },
            ],
            "total_amount": 7891.0,
            "trade_ins": [],
            "type": shared.DmsVehiclesaleType.RETAIL,
            "updated_at": parse_datetime("2025-04-16T02:25:03.853Z"),
            "vehicles": [],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehiclesale is not None

    # Handle response
    print(res.dms_vehiclesale)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchDmsVehiclesaleRequest](../../models/operations/patchdmsvehiclesalerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchDmsVehiclesaleResponse](../../models/operations/patchdmsvehiclesaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_dms_appointment

Deletes the DmsAppointment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDmsAppointment" method="delete" path="/dms/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.remove_dms_appointment(request={
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
| `request`                                                                                        | [operations.RemoveDmsAppointmentRequest](../../models/operations/removedmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveDmsAppointmentResponse](../../models/operations/removedmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_appointment

Updates the DmsAppointment identified by `id`. Provide the unified DmsAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsAppointment" method="put" path="/dms/{connection_id}/appointment/{id}" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.631Z"),
            "id": "4adcb137-9ab5-4404-99d5-9b49a342578e",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "d7f17954-4053-4eba-a7be-f4016074238d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "52fba2cc-a29d-457d-a0d5-14d9e9481c0d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "c653de4e-1054-4fec-9696-51886b2362b2",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.631Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.998Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateDmsAppointmentRequest](../../models/operations/updatedmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateDmsAppointmentResponse](../../models/operations/updatedmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_opcode

Updates the DmsOpcode identified by `id`. Provide the unified DmsOpcode fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsOpcode" method="put" path="/dms/{connection_id}/opcode/{id}" example="dms_opcode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_opcode(request={
        "dms_opcode": {
            "category": "Electrical",
            "code": "02AUS",
            "created_at": parse_datetime("2021-01-12T19:03:17.545Z"),
            "currency": "USD",
            "description": "Oil and filter change",
            "estimated_hours": 3.2,
            "flat_rate_hours": 3.5,
            "id": "8a3a625f-cde5-4df7-9a76-7e5d72f2508e",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T12:17:13.057Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_opcode is not None

    # Handle response
    print(res.dms_opcode)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateDmsOpcodeRequest](../../models/operations/updatedmsopcoderequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateDmsOpcodeResponse](../../models/operations/updatedmsopcoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_part

Updates the DmsPart identified by `id`. Provide the unified DmsPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsPart" method="put" path="/dms/{connection_id}/part/{id}" example="dms_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "a76e2648-fede-463a-ae14-9b48940c3d9a",
            "last_sold_at": parse_datetime("2020-11-23T02:58:30.889Z"),
            "list_price_amount": 39.61,
            "manufacturer_code": "TOY",
            "max_stock_quantity": 21.0,
            "metadata": [],
            "min_stock_quantity": 3.0,
            "pack_quantity": 1.0,
            "part_number": "73992-IM3FI",
            "quantity_available": 13.0,
            "quantity_on_hand": 15.0,
            "quantity_on_order": 14.0,
            "source_code": "30",
            "trade_price_amount": 29.05,
            "updated_at": parse_datetime("2023-11-22T17:30:11.498Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_part is not None

    # Handle response
    print(res.dms_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateDmsPartRequest](../../models/operations/updatedmspartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateDmsPartResponse](../../models/operations/updatedmspartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_partsale

Updates the DmsPartsale identified by `id`. Provide the unified DmsPartsale fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsPartsale" method="put" path="/dms/{connection_id}/partsale/{id}" example="dms_partsale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_partsale(request={
        "dms_partsale": {
            "cost_amount": 0.0,
            "created_at": parse_datetime("2023-05-22T03:39:30.335Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "freight_amount": 0.0,
            "id": "c577212b-856c-4afa-b866-510023c35189",
            "lines": [
                {
                    "id": "95290c13-4f44-4bb9-92a2-e5dab8e5e43f",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "08f9368b-c157-4968-bdd5-4af302744207",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "8a489684-dbcc-4342-ab28-1caac8e76023",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 3.0,
                    "quantity_ordered": 3.0,
                    "total_amount": 249.54,
                    "unit_price_amount": 83.18,
                },
            ],
            "metadata": [],
            "number": "P292867",
            "pay_type": shared.DmsPartsalePayType.CUSTOMER,
            "status": shared.DmsPartsaleStatus.VOIDED,
            "subtotal_amount": 981.89,
            "tax_amount": 68.73,
            "total_amount": 1050.62,
            "type": shared.DmsPartsaleType.SALE,
            "updated_at": parse_datetime("2026-04-17T16:03:18.289Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_partsale is not None

    # Handle response
    print(res.dms_partsale)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateDmsPartsaleRequest](../../models/operations/updatedmspartsalerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateDmsPartsaleResponse](../../models/operations/updatedmspartsaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dms_repairorder

Updates the DmsRepairorder identified by `id`. Provide the unified DmsRepairorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsRepairorder" method="put" path="/dms/{connection_id}/repairorder/{id}" example="dms_repairorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_repairorder(request={
        "dms_repairorder": {
            "balance_amount": 3193.86,
            "completed_at": parse_datetime("2026-11-12T19:17:42.307Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "205d65d6-f300-436e-a728-71ed9ac8cb5c",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "426874d7-2e52-4162-8b6c-8639c58d18b5",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "e1009e6c-2d8d-446c-8269-bcc66c32cd67",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 213.0,
                            "sold_hours": 3.2,
                            "technician_user_ids": [],
                            "total_amount": 681.6,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "A",
                    "parts": [],
                    "parts_amount": 0.0,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.2,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 681.6,
                },
                {
                    "actual_hours": 3.0,
                    "cause": "Worn brake pads",
                    "complaint": "Vibration at highway speed",
                    "correction": "Somnus avaritia utroque vulnero ullam ancilla.",
                    "id": "7a124d15-1bb6-491d-adc1-579be2c00466",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "bf400c19-1912-4255-b38c-bdc5cb87abf6",
                            "pay_type": shared.DmsRepairorderLaborPayType.WARRANTY,
                            "rate_amount": 144.0,
                            "sold_hours": 3.1,
                            "technician_user_ids": [],
                            "total_amount": 446.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "B",
                    "parts": [
                        {
                            "id": "5d8d7099-cdda-4146-b08c-46d84fba20a8",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "9a7d805a-b9d9-4663-86e4-0e9b32dba051",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 216.18,
                            "unit_price_amount": 108.09,
                        },
                    ],
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.WARRANTY,
                    "sold_hours": 3.1,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 1553.02,
                },
                {
                    "actual_hours": 1.5,
                    "cause": "Scheduled maintenance",
                    "complaint": "Noise when braking",
                    "correction": "Degero theca natus.",
                    "id": "8fe8640a-c7a2-4ad5-86ef-a016db57c58a",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "1e1d8015-f3f9-4d90-bede-5f2b99783e47",
                            "pay_type": shared.DmsRepairorderLaborPayType.CUSTOMER,
                            "rate_amount": 166.0,
                            "sold_hours": 1.4,
                            "technician_user_ids": [],
                            "total_amount": 232.4,
                        },
                    ],
                    "name": "Customer concern",
                    "number": "C",
                    "parts": [
                        {
                            "id": "9237d282-5b87-4e09-bb1f-363fc2a6296e",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "884766ed-b7f1-4902-9a06-1a0837b87653",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 2.0,
                            "quantity_ordered": 2.0,
                            "total_amount": 358.16,
                            "unit_price_amount": 179.08,
                        },
                    ],
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderJobPayType.CUSTOMER,
                    "sold_hours": 1.4,
                    "status": shared.DmsRepairorderJobStatus.COMPLETED,
                    "technician_user_ids": [],
                    "total_amount": 806.58,
                },
            ],
            "labor_amount": 1360.4,
            "metadata": [],
            "misc_amount": 35.0,
            "number": "143398",
            "odometer_in": 7776.0,
            "odometer_out": 7776.0,
            "odometer_unit": shared.DmsRepairorderOdometerUnit.MILES,
            "opened_at": parse_datetime("2025-02-07T19:13:16.353Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T03:13:16.353Z"),
            "purchase_order_number": "182743",
            "status": shared.DmsRepairorderStatus.COMPLETED,
            "sublet_amount": 0.0,
            "tag_number": "758",
            "tax_amount": 117.66,
            "technician_user_ids": [],
            "total_amount": 3193.86,
            "totals": [
                {
                    "discount_amount": 0.0,
                    "labor_amount": 232.4,
                    "parts_amount": 574.1800000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.CUSTOMER,
                    "sublet_amount": 0.0,
                    "total_amount": 806.58,
                },
                {
                    "discount_amount": 0.0,
                    "labor_amount": 1128.0,
                    "parts_amount": 1106.6200000000001,
                    "pay_type": shared.DmsRepairorderTotalPayType.WARRANTY,
                    "sublet_amount": 0.0,
                    "total_amount": 2234.62,
                },
            ],
            "transport_type": shared.DmsRepairorderTransportType.LOANER,
            "updated_at": parse_datetime("2025-11-27T22:05:41.793Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_repairorder is not None

    # Handle response
    print(res.dms_repairorder)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateDmsRepairorderRequest](../../models/operations/updatedmsrepairorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateDmsRepairorderResponse](../../models/operations/updatedmsrepairorderresponse.md)**

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

    res = unified_to.dms.update_dms_vehicle(request={
        "dms_vehicle": {
            "body_style": "Pickup",
            "condition": shared.Condition.NEW,
            "cost_amount": 26498.0,
            "created_at": parse_datetime("2021-02-03T08:01:58.559Z"),
            "currency": "USD",
            "description": "2023 Citroën Silverado",
            "exterior_color": "lavender",
            "fuel_type": shared.FuelType.ELECTRIC,
            "id": "79085b50-74a7-4f1d-8d69-d4979c6610bf",
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
            "updated_at": parse_datetime("2023-11-03T01:42:43.749Z"),
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

## update_dms_vehiclesale

Updates the DmsVehiclesale identified by `id`. Provide the unified DmsVehiclesale fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsVehiclesale" method="put" path="/dms/{connection_id}/vehiclesale/{id}" example="dms_vehiclesale" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.dms.update_dms_vehiclesale(request={
        "dms_vehiclesale": {
            "back_gross_amount": 4565.0,
            "created_at": parse_datetime("2020-04-02T08:14:56.150Z"),
            "currency": "USD",
            "down_payment_amount": 6700.0,
            "fees": [
                {
                    "cost_amount": 0.0,
                    "is_capitalized": True,
                    "name": "Documentation fee",
                    "price_amount": 499.0,
                },
                {
                    "is_capitalized": False,
                    "name": "Title and registration",
                    "price_amount": 392.0,
                },
            ],
            "finance": {
                "financed_amount": 0.0,
                "first_payment_at": parse_datetime("2022-08-16T02:28:39.785Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "9cf21810-137c-43f8-9e85-5b0d7caf29db",
            "metadata": [],
            "number": "D84591",
            "products": [
                {
                    "contract_number": "B7JN10GVB7",
                    "cost_amount": 1320.0,
                    "name": "Tire & Wheel",
                    "price_amount": 3300.0,
                    "provider": "Renner and Sons",
                    "term_months": 60.0,
                    "type": shared.DmsVehiclesaleProductType.PROTECTION,
                },
                {
                    "contract_number": "VIZU7K3VRU",
                    "cost_amount": 1115.0,
                    "deductible_amount": 100.0,
                    "name": "Platinum Vehicle Service Contract",
                    "price_amount": 3700.0,
                    "provider": "Frami, Wisozk and Gleichner",
                    "term_months": 72.0,
                    "type": shared.DmsVehiclesaleProductType.SERVICE_CONTRACT,
                },
            ],
            "rebate_amount": 500.0,
            "sold_at": parse_datetime("2022-08-14T11:13:05.498Z"),
            "source": "Website",
            "status": shared.DmsVehiclesaleStatus.SOLD,
            "tax_amount": 0.0,
            "taxes": [
                {
                    "name": "State sales tax",
                    "rate": 8.25,
                    "total_amount": 0.0,
                },
            ],
            "total_amount": 7891.0,
            "trade_ins": [],
            "type": shared.DmsVehiclesaleType.RETAIL,
            "updated_at": parse_datetime("2025-04-16T02:25:03.853Z"),
            "vehicles": [],
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_vehiclesale is not None

    # Handle response
    print(res.dms_vehiclesale)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateDmsVehiclesaleRequest](../../models/operations/updatedmsvehiclesalerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateDmsVehiclesaleResponse](../../models/operations/updatedmsvehiclesaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |