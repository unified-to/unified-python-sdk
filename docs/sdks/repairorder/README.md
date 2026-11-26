# Repairorder

## Overview

### Available Operations

* [create_dms_repairorder](#create_dms_repairorder) - Create a repairorder
* [get_dms_repairorder](#get_dms_repairorder) - Retrieve a repairorder
* [list_dms_repairorders](#list_dms_repairorders) - List all repairorders
* [patch_dms_repairorder](#patch_dms_repairorder) - Update a repairorder
* [update_dms_repairorder](#update_dms_repairorder) - Update a repairorder

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

    res = unified_to.repairorder.create_dms_repairorder(request={
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

    res = unified_to.repairorder.get_dms_repairorder(request={
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

    res = unified_to.repairorder.list_dms_repairorders(request={
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

    res = unified_to.repairorder.patch_dms_repairorder(request={
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

    res = unified_to.repairorder.update_dms_repairorder(request={
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