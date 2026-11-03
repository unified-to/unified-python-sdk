# Bomline

## Overview

### Available Operations

* [create_plm_bomline](#create_plm_bomline) - Create a bomline
* [get_plm_bomline](#get_plm_bomline) - Retrieve a bomline
* [list_plm_bomlines](#list_plm_bomlines) - List all bomlines
* [patch_plm_bomline](#patch_plm_bomline) - Update a bomline
* [remove_plm_bomline](#remove_plm_bomline) - Remove a bomline
* [update_plm_bomline](#update_plm_bomline) - Update a bomline

## create_plm_bomline

Creates a PlmBomline. Provide the unified PlmBomline fields in the request body; they are mapped to the provider's API. Returns the created PlmBomline.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmBomline" method="post" path="/plm/{connection_id}/bomline" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.create_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "0c304df1-acda-4074-8e74-5f0e52e30631",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-17T11:18:38.125Z"),
        },
        "connection_id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreatePlmBomlineRequest](../../models/operations/createplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreatePlmBomlineResponse](../../models/operations/createplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_bomline

Retrieves a single PlmBomline by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmBomline" method="get" path="/plm/{connection_id}/bomline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.get_plm_bomline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetPlmBomlineRequest](../../models/operations/getplmbomlinerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetPlmBomlineResponse](../../models/operations/getplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_bomlines

Returns a list of PlmBomlines. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmBomlines" method="get" path="/plm/{connection_id}/bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.list_plm_bomlines(request={
        "connection_id": "<id>",
    })

    assert res.plm_bomlines is not None

    # Handle response
    print(res.plm_bomlines)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListPlmBomlinesRequest](../../models/operations/listplmbomlinesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListPlmBomlinesResponse](../../models/operations/listplmbomlinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_bomline

Updates the PlmBomline identified by `id`. Provide the unified PlmBomline fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmBomline" method="patch" path="/plm/{connection_id}/bomline/{id}" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.patch_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "4055607b-b1e9-49a2-863d-9904c4f314f8",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-17T11:18:38.127Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchPlmBomlineRequest](../../models/operations/patchplmbomlinerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchPlmBomlineResponse](../../models/operations/patchplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_plm_bomline

Deletes the PlmBomline identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePlmBomline" method="delete" path="/plm/{connection_id}/bomline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.remove_plm_bomline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemovePlmBomlineRequest](../../models/operations/removeplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemovePlmBomlineResponse](../../models/operations/removeplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_bomline

Updates the PlmBomline identified by `id`. Provide the unified PlmBomline fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmBomline" method="put" path="/plm/{connection_id}/bomline/{id}" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bomline.update_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "4055607b-b1e9-49a2-863d-9904c4f314f8",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-17T11:18:38.127Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdatePlmBomlineRequest](../../models/operations/updateplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdatePlmBomlineResponse](../../models/operations/updateplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |