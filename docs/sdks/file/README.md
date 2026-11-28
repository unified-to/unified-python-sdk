# File

## Overview

### Available Operations

* [create_printing_file](#create_printing_file) - Create a file
* [create_storage_file](#create_storage_file) - Create a file
* [get_printing_file](#get_printing_file) - Retrieve a file
* [get_storage_file](#get_storage_file) - Retrieve a file
* [list_printing_files](#list_printing_files) - List all files
* [list_storage_files](#list_storage_files) - List all files
* [patch_storage_file](#patch_storage_file) - Update a file
* [remove_storage_file](#remove_storage_file) - Remove a file
* [update_storage_file](#update_storage_file) - Update a file

## create_printing_file

Creates a PrintingFile. Provide the unified PrintingFile fields in the request body; they are mapped to the provider's API. Returns the created PrintingFile.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPrintingFile" method="post" path="/printing/{connection_id}/file" example="printing_file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.create_printing_file(request={
        "printing_file": {
            "created_at": parse_datetime("2020-10-22T04:25:39.825Z"),
            "dpi": 300.0,
            "height": 5400.0,
            "id": "5f03fbd1-3c23-4de5-8d6d-69e250180672",
            "metadata": [],
            "mime_type": "image/jpeg",
            "name": "blond-ecliptic.jpg",
            "preview_url": "https://picsum.photos/seed/aATvhmNA/400/400",
            "size": 1956654.0,
            "status": shared.PrintingFileStatus.READY,
            "updated_at": parse_datetime("2020-10-22T04:25:39.825Z"),
            "url": "https://picsum.photos/seed/XBj97B/2783/172",
            "width": 4500.0,
        },
        "connection_id": "<id>",
    })

    assert res.printing_file is not None

    # Handle response
    print(res.printing_file)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreatePrintingFileRequest](../../models/operations/createprintingfilerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreatePrintingFileResponse](../../models/operations/createprintingfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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
            "description": "Debilito cimentarius virgo acidus thymbra.",
            "download_url": "https://messy-clamp.net/",
            "hash": "9d88dda7bc0acaa8472fdef2307f94a1fc355cef",
            "id": "93d64c2e-b84c-432e-8277-308ba9e58045",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "joshingly.pdf",
            "size": 1134456.0,
            "tags": [
                "derelinquo",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-15T23:00:05.136Z"),
            "version": "1",
            "web_url": "https://likable-widow.org/",
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

## get_printing_file

Retrieves a single PrintingFile by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrintingFile" method="get" path="/printing/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.get_printing_file(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_file is not None

    # Handle response
    print(res.printing_file)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPrintingFileRequest](../../models/operations/getprintingfilerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetPrintingFileResponse](../../models/operations/getprintingfileresponse.md)**

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

## list_printing_files

Returns a list of PrintingFiles. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPrintingFiles" method="get" path="/printing/{connection_id}/file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.file.list_printing_files(request={
        "connection_id": "<id>",
    })

    assert res.printing_files is not None

    # Handle response
    print(res.printing_files)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPrintingFilesRequest](../../models/operations/listprintingfilesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListPrintingFilesResponse](../../models/operations/listprintingfilesresponse.md)**

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
            "description": "Debilito cimentarius virgo acidus thymbra.",
            "download_url": "https://messy-clamp.net/",
            "hash": "9d88dda7bc0acaa8472fdef2307f94a1fc355cef",
            "id": "26e2fecf-6dc2-4871-bcdd-a7573401a174",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "joshingly.pdf",
            "size": 1134456.0,
            "tags": [
                "derelinquo",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-15T23:00:05.143Z"),
            "version": "1",
            "web_url": "https://likable-widow.org/",
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
            "description": "Debilito cimentarius virgo acidus thymbra.",
            "download_url": "https://messy-clamp.net/",
            "hash": "9d88dda7bc0acaa8472fdef2307f94a1fc355cef",
            "id": "26e2fecf-6dc2-4871-bcdd-a7573401a174",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "joshingly.pdf",
            "size": 1134456.0,
            "tags": [
                "derelinquo",
            ],
            "type": shared.StorageFileType.FOLDER,
            "updated_at": parse_datetime("2023-02-15T23:00:05.143Z"),
            "version": "1",
            "web_url": "https://likable-widow.org/",
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