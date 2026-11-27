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
            "end_at": parse_datetime("2026-05-08T02:58:02.059Z"),
            "id": "eb634d17-4919-4ed3-b666-62471a3038a5",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "8e2817c1-0373-4659-b7e1-9df4a7ad7a15",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "33643f74-b310-4718-a259-8f5aee631bd6",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "4a197a15-6d7d-43d3-90e2-f73cc4675b28",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-07T19:58:02.059Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T16:40:48.866Z"),
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
            "id": "ccba54df-c730-4902-90d0-95c7ccbd59f7",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.214Z"),
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
            "id": "e9188fc4-10a1-4775-9778-47a08239064b",
            "last_sold_at": parse_datetime("2020-11-23T04:34:35.807Z"),
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
            "updated_at": parse_datetime("2023-11-23T07:17:45.648Z"),
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
            "id": "3ab4e703-0ac9-4604-ad3a-805c3f5f9c24",
            "lines": [
                {
                    "id": "2c511f11-8e5b-4999-919c-3de7cca28cae",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "8b91c82f-6dc4-4047-bb88-995bfd66340d",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "7f0ff54b-fb03-4f2b-aea4-480c598fa9c6",
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
            "updated_at": parse_datetime("2026-04-18T13:34:58.702Z"),
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
            "completed_at": parse_datetime("2026-11-13T21:06:05.397Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "dc719e46-db55-4160-946a-3f77af194de5",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "adc18f6f-7a66-4082-b11d-77d199708403",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "9cd64624-d6f6-4006-af05-04fb1e6163a8",
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
                    "id": "7756a388-77a7-4150-aaba-ed8cc9ec6b3c",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "b45ae8ab-d54c-4120-8aac-0a43c6b6af86",
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
                            "id": "18c49469-b13a-44ec-ad67-54580ebe4a44",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "5620085d-b50b-4943-a8fe-fda3ae0dfd7f",
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
                    "id": "ab68f656-72ed-4a62-8229-a91d2db58a8a",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "4809d0fd-bf7e-4757-80c5-c56a00d26455",
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
                            "id": "a59ab044-7d30-450d-a7e5-ebc11ca33c00",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "b16b8295-b596-4c55-8c76-d364ff00df0e",
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
            "opened_at": parse_datetime("2025-02-08T09:48:33.256Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T17:48:33.256Z"),
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
            "updated_at": parse_datetime("2025-11-28T17:47:49.166Z"),
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
                "first_payment_at": parse_datetime("2022-08-16T11:44:29.333Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "eecfe7bd-c241-4fe6-adc1-4d4c5bebcf3c",
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
            "sold_at": parse_datetime("2022-08-14T20:28:55.046Z"),
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
            "updated_at": parse_datetime("2025-04-16T22:08:26.493Z"),
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
            "end_at": parse_datetime("2026-05-08T02:58:02.080Z"),
            "id": "ea321acc-a42f-47f7-b41f-b1a7a3bd7ec0",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "9c4b63fd-b5b3-4719-9d10-2f5f71f62a58",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "b956367f-7aa7-4f4c-aff8-9c4cba541c4d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "0d3830ca-0d5b-4c82-98d1-1accddce0a70",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-07T19:58:02.080Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T16:40:48.878Z"),
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
            "id": "e4a94368-53be-45f0-b65c-df20583d81cf",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.217Z"),
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
            "id": "e841ec48-113a-4afa-90fa-09e888d47d9d",
            "last_sold_at": parse_datetime("2020-11-23T04:34:35.808Z"),
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
            "updated_at": parse_datetime("2023-11-23T07:17:45.658Z"),
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
            "id": "80e2a6c4-4a59-4f2f-a84a-744b6cdd9e54",
            "lines": [
                {
                    "id": "0f9f5bb6-4215-416f-ac99-8de0d19a2287",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "d27ab4d3-e8c8-4201-a6e7-facc8ecd2009",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "932bf4d7-1d06-4b7a-ba30-814a3be2be1e",
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
            "updated_at": parse_datetime("2026-04-18T13:34:58.730Z"),
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
            "completed_at": parse_datetime("2026-11-13T21:06:05.448Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "8d67956e-05e3-4060-9554-8ae10272eaac",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "341cec2f-355f-4449-9d9b-7dcdb991d0c0",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "8c7d6a5a-a065-416e-9101-a30648e6aaf4",
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
                    "id": "91d64421-8d6e-413e-8786-f32fbd2c9c42",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "fe0da275-b721-4a6f-9c92-afc08267fa24",
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
                            "id": "57047be4-d9a2-4a03-94bd-8631dfbee458",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "a7bc1a47-80e4-452a-a93b-85fbf11d6c5f",
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
                    "id": "ebd74b7b-1c48-4080-a29b-5b2cc98dd670",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "b4e0b848-1f51-4597-bcdb-0012855eaf6c",
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
                            "id": "87eb884f-e1f5-4b37-b558-748a86b6d514",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "4e2754af-f2b3-49d4-bc9f-ea6114e3f975",
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
            "opened_at": parse_datetime("2025-02-08T09:48:33.286Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T17:48:33.286Z"),
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
            "updated_at": parse_datetime("2025-11-28T17:47:49.205Z"),
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
                "first_payment_at": parse_datetime("2022-08-16T11:44:29.350Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "d64f9352-d83d-4e53-b3a1-f9ba3572be37",
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
            "sold_at": parse_datetime("2022-08-14T20:28:55.063Z"),
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
            "updated_at": parse_datetime("2025-04-16T22:08:26.529Z"),
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
            "end_at": parse_datetime("2026-05-08T02:58:02.080Z"),
            "id": "ea321acc-a42f-47f7-b41f-b1a7a3bd7ec0",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "9c4b63fd-b5b3-4719-9d10-2f5f71f62a58",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "b956367f-7aa7-4f4c-aff8-9c4cba541c4d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "0d3830ca-0d5b-4c82-98d1-1accddce0a70",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-07T19:58:02.080Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T16:40:48.878Z"),
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
            "id": "e4a94368-53be-45f0-b65c-df20583d81cf",
            "is_active": True,
            "labor_rate_amount": 216.0,
            "metadata": [],
            "oem_code": "05604A3",
            "parts": [],
            "pay_type": shared.DmsOpcodePayType.CUSTOMER,
            "skill_code": "A",
            "type": shared.DmsOpcodeType.LABOR,
            "updated_at": parse_datetime("2021-11-03T15:52:02.217Z"),
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
            "id": "e841ec48-113a-4afa-90fa-09e888d47d9d",
            "last_sold_at": parse_datetime("2020-11-23T04:34:35.808Z"),
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
            "updated_at": parse_datetime("2023-11-23T07:17:45.658Z"),
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
            "id": "80e2a6c4-4a59-4f2f-a84a-744b6cdd9e54",
            "lines": [
                {
                    "id": "0f9f5bb6-4215-416f-ac99-8de0d19a2287",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 5.0,
                    "quantity_ordered": 5.0,
                    "total_amount": 491.45,
                    "unit_price_amount": 98.29,
                },
                {
                    "id": "d27ab4d3-e8c8-4201-a6e7-facc8ecd2009",
                    "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                    "quantity": 2.0,
                    "quantity_ordered": 2.0,
                    "total_amount": 240.9,
                    "unit_price_amount": 120.45,
                },
                {
                    "id": "932bf4d7-1d06-4b7a-ba30-814a3be2be1e",
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
            "updated_at": parse_datetime("2026-04-18T13:34:58.730Z"),
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
            "completed_at": parse_datetime("2026-11-13T21:06:05.448Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "8d67956e-05e3-4060-9554-8ae10272eaac",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "341cec2f-355f-4449-9d9b-7dcdb991d0c0",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "8c7d6a5a-a065-416e-9101-a30648e6aaf4",
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
                    "id": "91d64421-8d6e-413e-8786-f32fbd2c9c42",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "fe0da275-b721-4a6f-9c92-afc08267fa24",
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
                            "id": "57047be4-d9a2-4a03-94bd-8631dfbee458",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "a7bc1a47-80e4-452a-a93b-85fbf11d6c5f",
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
                    "id": "ebd74b7b-1c48-4080-a29b-5b2cc98dd670",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "b4e0b848-1f51-4597-bcdb-0012855eaf6c",
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
                            "id": "87eb884f-e1f5-4b37-b558-748a86b6d514",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "4e2754af-f2b3-49d4-bc9f-ea6114e3f975",
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
            "opened_at": parse_datetime("2025-02-08T09:48:33.286Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-09T17:48:33.286Z"),
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
            "updated_at": parse_datetime("2025-11-28T17:47:49.205Z"),
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
                "first_payment_at": parse_datetime("2022-08-16T11:44:29.350Z"),
                "interest_rate": 6.68,
                "lender_name": "Mueller, Yundt and Murray Financial",
                "payment_amount": 339.0,
                "payment_frequency": shared.PaymentFrequency.MONTHLY,
                "term_months": 72.0,
            },
            "finance_type": shared.FinanceType.FINANCE,
            "id": "d64f9352-d83d-4e53-b3a1-f9ba3572be37",
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
            "sold_at": parse_datetime("2022-08-14T20:28:55.063Z"),
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
            "updated_at": parse_datetime("2025-04-16T22:08:26.529Z"),
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