# Envvar

## Overview

### Available Operations

* [create_compute_envvar](#create_compute_envvar) - Create an envvar
* [get_compute_envvar](#get_compute_envvar) - Retrieve an envvar
* [list_compute_envvars](#list_compute_envvars) - List all envvars
* [patch_compute_envvar](#patch_compute_envvar) - Update an envvar
* [remove_compute_envvar](#remove_compute_envvar) - Remove an envvar
* [update_compute_envvar](#update_compute_envvar) - Update an envvar

## create_compute_envvar

Creates a ComputeEnvvar. Provide the unified ComputeEnvvar fields in the request body; they are mapped to the provider's API. Returns the created ComputeEnvvar.

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeEnvvar" method="post" path="/compute/{connection_id}/envvar" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.create_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "b34e00c9-07a2-42c3-a306-41447f6807c4",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-10T08:51:28.382Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateComputeEnvvarRequest](../../models/operations/createcomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateComputeEnvvarResponse](../../models/operations/createcomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_envvar

Retrieves a single ComputeEnvvar by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeEnvvar" method="get" path="/compute/{connection_id}/envvar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.get_compute_envvar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeEnvvarRequest](../../models/operations/getcomputeenvvarrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeEnvvarResponse](../../models/operations/getcomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_envvars

Returns a list of ComputeEnvvars. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeEnvvars" method="get" path="/compute/{connection_id}/envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.list_compute_envvars(request={
        "connection_id": "<id>",
    })

    assert res.compute_envvars is not None

    # Handle response
    print(res.compute_envvars)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeEnvvarsRequest](../../models/operations/listcomputeenvvarsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeEnvvarsResponse](../../models/operations/listcomputeenvvarsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_envvar

Updates the ComputeEnvvar identified by `id`. Provide the unified ComputeEnvvar fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeEnvvar" method="patch" path="/compute/{connection_id}/envvar/{id}" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.patch_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "40be57fe-4256-49b2-82ef-a5ce6ff93ffd",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-10T08:51:28.391Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchComputeEnvvarRequest](../../models/operations/patchcomputeenvvarrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchComputeEnvvarResponse](../../models/operations/patchcomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_envvar

Deletes the ComputeEnvvar identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeEnvvar" method="delete" path="/compute/{connection_id}/envvar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.remove_compute_envvar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveComputeEnvvarRequest](../../models/operations/removecomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveComputeEnvvarResponse](../../models/operations/removecomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_envvar

Updates the ComputeEnvvar identified by `id`. Provide the unified ComputeEnvvar fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeEnvvar" method="put" path="/compute/{connection_id}/envvar/{id}" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.envvar.update_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "40be57fe-4256-49b2-82ef-a5ce6ff93ffd",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-10T08:51:28.391Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateComputeEnvvarRequest](../../models/operations/updatecomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateComputeEnvvarResponse](../../models/operations/updatecomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |