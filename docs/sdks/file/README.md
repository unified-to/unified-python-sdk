# File

## Overview

### Available Operations

* [create_storage_file](#create_storage_file) - Create a file
* [get_storage_file](#get_storage_file) - Retrieve a file
* [list_storage_files](#list_storage_files) - List all files
* [patch_storage_file](#patch_storage_file) - Update a file
* [remove_storage_file](#remove_storage_file) - Remove a file
* [update_storage_file](#update_storage_file) - Update a file

## create_storage_file

Creates a StorageFile. Provide the unified StorageFile fields in the request body; they are mapped to the provider's API. Returns the created StorageFile.

### Example Usage

<!-- UsageSnippet language="python" operationID="createStorageFile" method="post" path="/storage/{connection_id}/file" example="storage_file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.create_storage_file(request={
        "storage_file": {
            "created_at": parse_datetime("2021-09-12T16:48:23.774Z"),
            "description": "Deprimo crastinus cupiditate debilito cimentarius virgo acidus.",
            "download_url": "https://clueless-laughter.biz",
            "hash": "d9d88dda7bc0acaa8472fdef2307f94a1fc355ce",
            "id": "88c42218-c3b7-4e09-ae2d-3dd49be1e532",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "softly.pdf",
            "size": 1134456.0,
            "tags": [
                "suasoria",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-07T15:23:09.732Z"),
            "version": "1",
            "web_url": "https://faraway-inspection.org",
        },
        "connection_id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateStorageFileRequest](../../models/operations/createstoragefilerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateStorageFileResponse](../../models/operations/createstoragefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_storage_file

Retrieves a single StorageFile by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getStorageFile" method="get" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.get_storage_file(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetStorageFileRequest](../../models/operations/getstoragefilerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetStorageFileResponse](../../models/operations/getstoragefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_storage_files

Returns a list of StorageFiles. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listStorageFiles" method="get" path="/storage/{connection_id}/file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.list_storage_files(request={
        "connection_id": "<id>",
    })

    assert res.storage_files is not None

    # Handle response
    print(res.storage_files)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListStorageFilesRequest](../../models/operations/liststoragefilesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListStorageFilesResponse](../../models/operations/liststoragefilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_storage_file

Updates the StorageFile identified by `id`. Provide the unified StorageFile fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchStorageFile" method="patch" path="/storage/{connection_id}/file/{id}" example="storage_file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.patch_storage_file(request={
        "storage_file": {
            "created_at": parse_datetime("2021-09-12T16:48:23.774Z"),
            "description": "Deprimo crastinus cupiditate debilito cimentarius virgo acidus.",
            "download_url": "https://clueless-laughter.biz",
            "hash": "d9d88dda7bc0acaa8472fdef2307f94a1fc355ce",
            "id": "9e1e8724-3300-48b1-8e60-05d231cad958",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "softly.pdf",
            "size": 1134456.0,
            "tags": [
                "suasoria",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-07T15:23:09.738Z"),
            "version": "1",
            "web_url": "https://faraway-inspection.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.storage_file is not None

    # Handle response
    print(res.storage_file)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchStorageFileRequest](../../models/operations/patchstoragefilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchStorageFileResponse](../../models/operations/patchstoragefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_storage_file

Deletes the StorageFile identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeStorageFile" method="delete" path="/storage/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.remove_storage_file(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveStorageFileRequest](../../models/operations/removestoragefilerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveStorageFileResponse](../../models/operations/removestoragefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_storage_file

Updates the StorageFile identified by `id`. Provide the unified StorageFile fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateStorageFile" method="put" path="/storage/{connection_id}/file/{id}" example="storage_file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.update_storage_file(request={
        "storage_file": {
            "created_at": parse_datetime("2021-09-12T16:48:23.774Z"),
            "description": "Deprimo crastinus cupiditate debilito cimentarius virgo acidus.",
            "download_url": "https://clueless-laughter.biz",
            "hash": "d9d88dda7bc0acaa8472fdef2307f94a1fc355ce",
            "id": "9e1e8724-3300-48b1-8e60-05d231cad958",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "softly.pdf",
            "size": 1134456.0,
            "tags": [
                "suasoria",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-07T15:23:09.738Z"),
            "version": "1",
            "web_url": "https://faraway-inspection.org",
        },
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
| `request`                                                                                  | [operations.UpdateStorageFileRequest](../../models/operations/updatestoragefilerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateStorageFileResponse](../../models/operations/updatestoragefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |