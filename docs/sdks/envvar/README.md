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

Create an envvar

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
            "id": "1683b32e-438e-4f90-b41c-841bc720c291",
            "is_secret": True,
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-01T07:24:25.741Z"),
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

Retrieve an envvar

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

List all envvars

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

Update an envvar

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
            "id": "7f78313a-14d4-49bf-87bf-18c6e9ee0775",
            "is_secret": True,
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-01T07:24:25.747Z"),
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

Remove an envvar

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

Update an envvar

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
            "id": "7f78313a-14d4-49bf-87bf-18c6e9ee0775",
            "is_secret": True,
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-01T07:24:25.747Z"),
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