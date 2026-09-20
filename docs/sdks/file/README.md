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

Create a file

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
            "data": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgYmFzZVByb2ZpbGU9ImZ1bGwiIHdpZHRoPSI4MzIiIGhlaWdodD0iMTg2MSI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0iIzFmYzM1NSIvPjx0ZXh0IHg9IjQxNiIgeT0iOTMwLjUiIGZvbnQtc2l6ZT0iMjAiIGFsaWdubWVudC1iYXNlbGluZT0ibWlkZGxlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJ3aGl0ZSI+ODMyeDE4NjE8L3RleHQ+PC9zdmc+",
            "description": "Crastinus cupiditate debilito cimentarius virgo.",
            "download_url": "https://stingy-casement.name/",
            "hash": "fe6a659e-75cd-4079-9b76-351f9af2205a",
            "id": "92ef580a-4364-4668-99f2-c6459312f74b",
            "mime_type": "FOLDER",
            "name": "softly.tiff",
            "references": [
                {
                    "id": "ab705f3b-e368-4a94-8b22-d5f693c14a76",
                    "name": "tamisium viduo odio cauda",
                    "type": "accounting_bill",
                },
                {
                    "id": "9f0f694e-b6f4-4c12-b5f6-ab08d4e81140",
                    "name": "quia",
                    "type": "accounting_expense",
                },
            ],
            "size": 10276.0,
            "tags": [
                "spoliatio",
            ],
            "type": shared.StorageFileType.FILE,
            "updated_at": parse_datetime("2023-01-27T20:36:58.761Z"),
            "version": "1",
            "web_url": "https://sandy-distinction.info/",
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

Retrieve a file

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

List all files

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

Update a file

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
            "data": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgYmFzZVByb2ZpbGU9ImZ1bGwiIHdpZHRoPSI4MzIiIGhlaWdodD0iMTg2MSI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0iIzFmYzM1NSIvPjx0ZXh0IHg9IjQxNiIgeT0iOTMwLjUiIGZvbnQtc2l6ZT0iMjAiIGFsaWdubWVudC1iYXNlbGluZT0ibWlkZGxlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJ3aGl0ZSI+ODMyeDE4NjE8L3RleHQ+PC9zdmc+",
            "description": "Crastinus cupiditate debilito cimentarius virgo.",
            "download_url": "https://stingy-casement.name/",
            "hash": "fe6a659e-75cd-4079-9b76-351f9af2205a",
            "id": "bd190a3d-1339-4697-b98f-efa45b923142",
            "mime_type": "FOLDER",
            "name": "softly.tiff",
            "references": [
                {
                    "id": "ab705f3b-e368-4a94-8b22-d5f693c14a76",
                    "name": "tamisium viduo odio cauda",
                    "type": "accounting_bill",
                },
                {
                    "id": "9f0f694e-b6f4-4c12-b5f6-ab08d4e81140",
                    "name": "quia",
                    "type": "accounting_expense",
                },
            ],
            "size": 10276.0,
            "tags": [
                "spoliatio",
            ],
            "type": shared.StorageFileType.FILE,
            "updated_at": parse_datetime("2023-01-27T20:36:58.764Z"),
            "version": "1",
            "web_url": "https://sandy-distinction.info/",
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

Remove a file

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

Update a file

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
            "data": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgYmFzZVByb2ZpbGU9ImZ1bGwiIHdpZHRoPSI4MzIiIGhlaWdodD0iMTg2MSI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0iIzFmYzM1NSIvPjx0ZXh0IHg9IjQxNiIgeT0iOTMwLjUiIGZvbnQtc2l6ZT0iMjAiIGFsaWdubWVudC1iYXNlbGluZT0ibWlkZGxlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJ3aGl0ZSI+ODMyeDE4NjE8L3RleHQ+PC9zdmc+",
            "description": "Crastinus cupiditate debilito cimentarius virgo.",
            "download_url": "https://stingy-casement.name/",
            "hash": "fe6a659e-75cd-4079-9b76-351f9af2205a",
            "id": "bd190a3d-1339-4697-b98f-efa45b923142",
            "mime_type": "FOLDER",
            "name": "softly.tiff",
            "references": [
                {
                    "id": "ab705f3b-e368-4a94-8b22-d5f693c14a76",
                    "name": "tamisium viduo odio cauda",
                    "type": "accounting_bill",
                },
                {
                    "id": "9f0f694e-b6f4-4c12-b5f6-ab08d4e81140",
                    "name": "quia",
                    "type": "accounting_expense",
                },
            ],
            "size": 10276.0,
            "tags": [
                "spoliatio",
            ],
            "type": shared.StorageFileType.FILE,
            "updated_at": parse_datetime("2023-01-27T20:36:58.764Z"),
            "version": "1",
            "web_url": "https://sandy-distinction.info/",
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