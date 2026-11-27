# Partsale

## Overview

### Available Operations

* [create_dms_partsale](#create_dms_partsale) - Create a partsale
* [get_dms_partsale](#get_dms_partsale) - Retrieve a partsale
* [list_dms_partsales](#list_dms_partsales) - List all partsales
* [patch_dms_partsale](#patch_dms_partsale) - Update a partsale
* [update_dms_partsale](#update_dms_partsale) - Update a partsale

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

    res = unified_to.partsale.create_dms_partsale(request={
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

    res = unified_to.partsale.get_dms_partsale(request={
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

    res = unified_to.partsale.list_dms_partsales(request={
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

    res = unified_to.partsale.patch_dms_partsale(request={
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

    res = unified_to.partsale.update_dms_partsale(request={
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