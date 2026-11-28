# Part

## Overview

### Available Operations

* [create_dms_part](#create_dms_part) - Create a part
* [create_plm_part](#create_plm_part) - Create a part
* [get_dms_part](#get_dms_part) - Retrieve a part
* [get_plm_part](#get_plm_part) - Retrieve a part
* [list_dms_parts](#list_dms_parts) - List all parts
* [list_plm_parts](#list_plm_parts) - List all parts
* [patch_dms_part](#patch_dms_part) - Update a part
* [patch_plm_part](#patch_plm_part) - Update a part
* [remove_plm_part](#remove_plm_part) - Remove a part
* [update_dms_part](#update_dms_part) - Update a part
* [update_plm_part](#update_plm_part) - Update a part

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

    res = unified_to.part.create_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "079260f7-b327-4360-8ed9-82225b5fcca4",
            "last_sold_at": parse_datetime("2020-11-23T06:01:35.424Z"),
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
            "updated_at": parse_datetime("2023-11-23T19:47:03.034Z"),
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

## create_plm_part

Creates a PlmPart. Provide the unified PlmPart fields in the request body; they are mapped to the provider's API. Returns the created PlmPart.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmPart" method="post" path="/plm/{connection_id}/part" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.create_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Aestivus talis tero ullam cruciamentum voluptatibus cumque degusto cui.",
            "document_ids": [],
            "file_ids": [],
            "id": "6487f488-6bf7-4d00-937c-fef536bbb629",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "1166eb46-7bf0-4954-b604-38f6b9cfe74f",
            "metadata": [],
            "name": "speedy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-16T02:51:09.630Z"),
            "url": "https://digital-pop.com",
        },
        "connection_id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreatePlmPartRequest](../../models/operations/createplmpartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreatePlmPartResponse](../../models/operations/createplmpartresponse.md)**

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

    res = unified_to.part.get_dms_part(request={
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

## get_plm_part

Retrieves a single PlmPart by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmPart" method="get" path="/plm/{connection_id}/part/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.get_plm_part(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPlmPartRequest](../../models/operations/getplmpartrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetPlmPartResponse](../../models/operations/getplmpartresponse.md)**

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

    res = unified_to.part.list_dms_parts(request={
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

## list_plm_parts

Returns a list of PlmParts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmParts" method="get" path="/plm/{connection_id}/part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.list_plm_parts(request={
        "connection_id": "<id>",
    })

    assert res.plm_parts is not None

    # Handle response
    print(res.plm_parts)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPlmPartsRequest](../../models/operations/listplmpartsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListPlmPartsResponse](../../models/operations/listplmpartsresponse.md)**

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

    res = unified_to.part.patch_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "7280e3f5-8add-4cf8-acbd-1ee1f9af6d90",
            "last_sold_at": parse_datetime("2020-11-23T06:01:35.425Z"),
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
            "updated_at": parse_datetime("2023-11-23T19:47:03.044Z"),
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

## patch_plm_part

Updates the PlmPart identified by `id`. Provide the unified PlmPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmPart" method="patch" path="/plm/{connection_id}/part/{id}" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.patch_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Aestivus talis tero ullam cruciamentum voluptatibus cumque degusto cui.",
            "document_ids": [],
            "file_ids": [],
            "id": "262ba127-b360-4de3-bdf1-eac70bfbbe60",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "14f37939-699a-41ad-9360-e58f1c19021d",
            "metadata": [],
            "name": "speedy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-16T02:51:09.633Z"),
            "url": "https://digital-pop.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchPlmPartRequest](../../models/operations/patchplmpartrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchPlmPartResponse](../../models/operations/patchplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_plm_part

Deletes the PlmPart identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePlmPart" method="delete" path="/plm/{connection_id}/part/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.remove_plm_part(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemovePlmPartRequest](../../models/operations/removeplmpartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemovePlmPartResponse](../../models/operations/removeplmpartresponse.md)**

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

    res = unified_to.part.update_dms_part(request={
        "dms_part": {
            "bin_locations": [
                "S18-6",
            ],
            "category": "Ignition",
            "cost_amount": 25.26,
            "created_at": parse_datetime("2020-07-02T08:18:03.858Z"),
            "currency": "USD",
            "description": "Cabin filter",
            "id": "7280e3f5-8add-4cf8-acbd-1ee1f9af6d90",
            "last_sold_at": parse_datetime("2020-11-23T06:01:35.425Z"),
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
            "updated_at": parse_datetime("2023-11-23T19:47:03.044Z"),
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

## update_plm_part

Updates the PlmPart identified by `id`. Provide the unified PlmPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmPart" method="put" path="/plm/{connection_id}/part/{id}" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.part.update_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Aestivus talis tero ullam cruciamentum voluptatibus cumque degusto cui.",
            "document_ids": [],
            "file_ids": [],
            "id": "262ba127-b360-4de3-bdf1-eac70bfbbe60",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "14f37939-699a-41ad-9360-e58f1c19021d",
            "metadata": [],
            "name": "speedy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-16T02:51:09.633Z"),
            "url": "https://digital-pop.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdatePlmPartRequest](../../models/operations/updateplmpartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdatePlmPartResponse](../../models/operations/updateplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |