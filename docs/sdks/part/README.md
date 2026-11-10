# Part

## Overview

### Available Operations

* [create_plm_part](#create_plm_part) - Create a part
* [get_plm_part](#get_plm_part) - Retrieve a part
* [list_plm_parts](#list_plm_parts) - List all parts
* [patch_plm_part](#patch_plm_part) - Update a part
* [update_plm_part](#update_plm_part) - Update a part

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
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "8827af39-cc18-4126-9af8-b58b75a9412c",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "abb94e2c-8692-4382-a97f-7d8e3bcd140f",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T08:53:28.706Z"),
            "url": "https://inborn-independence.info",
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
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "ee03d8b5-d9b3-49b4-bf6e-ebf995f0985d",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "5b0c4d89-097f-4346-8b11-676abfc104ce",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T08:53:28.711Z"),
            "url": "https://inborn-independence.info",
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
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "ee03d8b5-d9b3-49b4-bf6e-ebf995f0985d",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "5b0c4d89-097f-4346-8b11-676abfc104ce",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T08:53:28.711Z"),
            "url": "https://inborn-independence.info",
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