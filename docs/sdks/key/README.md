# Key

## Overview

### Available Operations

* [create_compute_key](#create_compute_key) - Create a key
* [get_compute_key](#get_compute_key) - Retrieve a key
* [list_compute_keys](#list_compute_keys) - List all keys
* [patch_compute_key](#patch_compute_key) - Update a key
* [remove_compute_key](#remove_compute_key) - Remove a key
* [update_compute_key](#update_compute_key) - Update a key

## create_compute_key

Create a key

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeKey" method="post" path="/compute/{connection_id}/key" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.create_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "20afd750-fcf7-4406-83e5-a2621eb61518",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.588Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateComputeKeyRequest](../../models/operations/createcomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateComputeKeyResponse](../../models/operations/createcomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_key

Retrieve a key

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeKey" method="get" path="/compute/{connection_id}/key/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.get_compute_key(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetComputeKeyRequest](../../models/operations/getcomputekeyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetComputeKeyResponse](../../models/operations/getcomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_keys

List all keys

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeKeys" method="get" path="/compute/{connection_id}/key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.list_compute_keys(request={
        "connection_id": "<id>",
    })

    assert res.compute_keys is not None

    # Handle response
    print(res.compute_keys)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListComputeKeysRequest](../../models/operations/listcomputekeysrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListComputeKeysResponse](../../models/operations/listcomputekeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_key

Update a key

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeKey" method="patch" path="/compute/{connection_id}/key/{id}" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.patch_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "ef7eede9-a69b-4e48-931b-1a2db7a2d8c8",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.593Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchComputeKeyRequest](../../models/operations/patchcomputekeyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchComputeKeyResponse](../../models/operations/patchcomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_key

Remove a key

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeKey" method="delete" path="/compute/{connection_id}/key/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.remove_compute_key(request={
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
| `request`                                                                                | [operations.RemoveComputeKeyRequest](../../models/operations/removecomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveComputeKeyResponse](../../models/operations/removecomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_key

Update a key

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeKey" method="put" path="/compute/{connection_id}/key/{id}" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.key.update_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "ef7eede9-a69b-4e48-931b-1a2db7a2d8c8",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.593Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateComputeKeyRequest](../../models/operations/updatecomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateComputeKeyResponse](../../models/operations/updatecomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |