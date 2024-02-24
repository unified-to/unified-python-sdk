# Storage
(*storage*)

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

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateStorageFileRequest(
    connection_id='<value>',
)

res = s.storage.create_storage_file(req, operations.CreateStorageFileSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.storage_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateStorageFileRequest](../../models/operations/createstoragefilerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateStorageFileSecurity](../../models/operations/createstoragefilesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateStorageFileResponse](../../models/operations/createstoragefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_storage_file

Retrieve a file

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetStorageFileRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.storage.get_storage_file(req, operations.GetStorageFileSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.storage_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetStorageFileRequest](../../models/operations/getstoragefilerequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetStorageFileSecurity](../../models/operations/getstoragefilesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetStorageFileResponse](../../models/operations/getstoragefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_storage_files

List all files

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListStorageFilesRequest(
    connection_id='<value>',
)

res = s.storage.list_storage_files(req, operations.ListStorageFilesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.storage_files is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListStorageFilesRequest](../../models/operations/liststoragefilesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListStorageFilesSecurity](../../models/operations/liststoragefilessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListStorageFilesResponse](../../models/operations/liststoragefilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_storage_file

Update a file

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchStorageFileRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.storage.patch_storage_file(req, operations.PatchStorageFileSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.storage_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchStorageFileRequest](../../models/operations/patchstoragefilerequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchStorageFileSecurity](../../models/operations/patchstoragefilesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchStorageFileResponse](../../models/operations/patchstoragefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_storage_file

Remove a file

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveStorageFileRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.storage.remove_storage_file(req, operations.RemoveStorageFileSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveStorageFileRequest](../../models/operations/removestoragefilerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveStorageFileSecurity](../../models/operations/removestoragefilesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveStorageFileResponse](../../models/operations/removestoragefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_storage_file

Update a file

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateStorageFileRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.storage.update_storage_file(req, operations.UpdateStorageFileSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.storage_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateStorageFileRequest](../../models/operations/updatestoragefilerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateStorageFileSecurity](../../models/operations/updatestoragefilesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateStorageFileResponse](../../models/operations/updatestoragefileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
