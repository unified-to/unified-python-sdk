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
            "completed_at": parse_datetime("2026-11-14T20:28:00.850Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "8d5cc00a-65d8-4314-bd82-be83d9464869",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "db0c3ae0-d9f6-4d5c-9711-be041cff09a8",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "556113f0-2fe8-4643-95d2-45f84db7ba3f",
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
                    "id": "4e0897e0-d574-4abd-8583-ec17102d3fd2",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "af002f65-6916-4a6d-a709-145a45d7048e",
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
                            "id": "d2566540-7721-4aa9-bb74-8a23bb9a4a60",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "bf952140-c71f-4bb0-a5f2-514360db8a29",
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
                    "id": "a23e7d1f-867f-4156-91ea-0bdd7d138fb1",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "b115a5eb-65e7-4e4a-b800-9656c3c1aa3d",
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
                            "id": "dd33432b-f266-4981-9103-3bad2b78c6ae",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "d1439ba1-7ceb-4223-8ef9-d0169de1a06c",
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
            "opened_at": parse_datetime("2025-02-08T23:01:02.624Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-10T07:01:02.624Z"),
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
            "updated_at": parse_datetime("2025-11-29T11:38:07.569Z"),
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
            "completed_at": parse_datetime("2026-11-14T20:28:00.907Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "2e4fa164-d74c-4289-afe2-7b8256d19ce2",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "525e7197-fecc-4ef6-99f4-1447ede8ff42",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "e27a1436-f9be-4bb5-9642-b41fe31cabc0",
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
                    "id": "805c1ee5-a417-4408-8983-4146ff7a0d34",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "87f53ace-31d8-47cb-ac93-590a7a775941",
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
                            "id": "95d2b874-ca0b-4b4f-87c8-e945ed3f2804",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "9dfee145-9d03-4ee4-b9ed-139857839006",
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
                    "id": "a98afe22-27a5-42ad-818b-2a637a309080",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "3104d7f2-8bd0-4b4c-bd1c-22a1581071a0",
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
                            "id": "77189727-98bc-46ee-b0ec-4b78d8285f61",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "a0de710c-7b3e-47cf-848b-68de66f10a4b",
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
            "opened_at": parse_datetime("2025-02-08T23:01:02.656Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-10T07:01:02.656Z"),
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
            "updated_at": parse_datetime("2025-11-29T11:38:07.613Z"),
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
            "completed_at": parse_datetime("2026-11-14T20:28:00.907Z"),
            "created_at": parse_datetime("2022-10-25T15:50:48.007Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "estimate_amount": 3264.0,
            "id": "2e4fa164-d74c-4289-afe2-7b8256d19ce2",
            "jobs": [
                {
                    "actual_hours": 3.6,
                    "cause": "Scheduled maintenance",
                    "complaint": "Due for service",
                    "correction": "Aufero cumque vicinus aptus assumenda quis aptus.",
                    "id": "525e7197-fecc-4ef6-99f4-1447ede8ff42",
                    "labor_amount": 681.6,
                    "labors": [
                        {
                            "id": "e27a1436-f9be-4bb5-9642-b41fe31cabc0",
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
                    "id": "805c1ee5-a417-4408-8983-4146ff7a0d34",
                    "labor_amount": 446.4,
                    "labors": [
                        {
                            "id": "87f53ace-31d8-47cb-ac93-590a7a775941",
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
                            "id": "95d2b874-ca0b-4b4f-87c8-e945ed3f2804",
                            "pay_type": shared.DmsPartlinePayType.WARRANTY,
                            "quantity": 4.0,
                            "quantity_ordered": 4.0,
                            "total_amount": 890.44,
                            "unit_price_amount": 222.61,
                        },
                        {
                            "id": "9dfee145-9d03-4ee4-b9ed-139857839006",
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
                    "id": "a98afe22-27a5-42ad-818b-2a637a309080",
                    "labor_amount": 232.4,
                    "labors": [
                        {
                            "id": "3104d7f2-8bd0-4b4c-bd1c-22a1581071a0",
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
                            "id": "77189727-98bc-46ee-b0ec-4b78d8285f61",
                            "pay_type": shared.DmsPartlinePayType.CUSTOMER,
                            "quantity": 1.0,
                            "quantity_ordered": 1.0,
                            "total_amount": 216.02,
                            "unit_price_amount": 216.02,
                        },
                        {
                            "id": "a0de710c-7b3e-47cf-848b-68de66f10a4b",
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
            "opened_at": parse_datetime("2025-02-08T23:01:02.656Z"),
            "parts_amount": 1680.8000000000002,
            "pay_type": shared.DmsRepairorderPayType.WARRANTY,
            "promised_at": parse_datetime("2025-02-10T07:01:02.656Z"),
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
            "updated_at": parse_datetime("2025-11-29T11:38:07.613Z"),
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