# File

## Overview

### Available Operations

* [create_storage_file2](#create_storage_file2) - Create a file
* [get_storage_file2](#get_storage_file2) - Retrieve a file
* [list_storage_files2](#list_storage_files2) - List all files
* [patch_storage_file2](#patch_storage_file2) - Update a file
* [remove_storage_file2](#remove_storage_file2) - Remove a file
* [update_storage_file2](#update_storage_file2) - Update a file

## create_storage_file2

Create a file

### Example Usage

<!-- UsageSnippet language="python" operationID="createStorageFile2" method="post" path="/storage/{connection_id}/file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.create_storage_file2(request={
        "storage_file": {},
        "connection_id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateStorageFile2Request](../../models/operations/createstoragefile2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateStorageFile2Response](../../models/operations/createstoragefile2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_storage_file2

Retrieve a file

### Example Usage

<!-- UsageSnippet language="python" operationID="getStorageFile2" method="get" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.get_storage_file2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetStorageFile2Request](../../models/operations/getstoragefile2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetStorageFile2Response](../../models/operations/getstoragefile2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_storage_files2

List all files

### Example Usage

<!-- UsageSnippet language="python" operationID="listStorageFiles2" method="get" path="/storage/{connection_id}/file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.list_storage_files2(request={
        "connection_id": "<id>",
    })

    assert res.storage_files is not None

    # Handle response
    print(res.storage_files)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListStorageFiles2Request](../../models/operations/liststoragefiles2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListStorageFiles2Response](../../models/operations/liststoragefiles2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_storage_file2

Update a file

### Example Usage

<!-- UsageSnippet language="python" operationID="patchStorageFile2" method="patch" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.patch_storage_file2(request={
        "storage_file": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchStorageFile2Request](../../models/operations/patchstoragefile2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchStorageFile2Response](../../models/operations/patchstoragefile2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_storage_file2

Remove a file

### Example Usage

<!-- UsageSnippet language="python" operationID="removeStorageFile2" method="delete" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.remove_storage_file2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveStorageFile2Request](../../models/operations/removestoragefile2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveStorageFile2Response](../../models/operations/removestoragefile2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_storage_file2

Update a file

### Example Usage

<!-- UsageSnippet language="python" operationID="updateStorageFile2" method="put" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.update_storage_file2(request={
        "storage_file": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateStorageFile2Request](../../models/operations/updatestoragefile2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateStorageFile2Response](../../models/operations/updatestoragefile2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |