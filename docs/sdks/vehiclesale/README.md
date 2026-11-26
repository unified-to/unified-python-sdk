# Vehiclesale

## Overview

### Available Operations

* [create_dms_vehiclesale](#create_dms_vehiclesale) - Create a vehiclesale
* [get_dms_vehiclesale](#get_dms_vehiclesale) - Retrieve a vehiclesale
* [list_dms_vehiclesales](#list_dms_vehiclesales) - List all vehiclesales
* [patch_dms_vehiclesale](#patch_dms_vehiclesale) - Update a vehiclesale
* [update_dms_vehiclesale](#update_dms_vehiclesale) - Update a vehiclesale

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

    res = unified_to.vehiclesale.create_dms_vehiclesale(request={
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

    res = unified_to.vehiclesale.get_dms_vehiclesale(request={
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

    res = unified_to.vehiclesale.list_dms_vehiclesales(request={
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

    res = unified_to.vehiclesale.patch_dms_vehiclesale(request={
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

    res = unified_to.vehiclesale.update_dms_vehiclesale(request={
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