# Document
(*document*)

### Available Operations

* [create_ats_document](#create_ats_document) - Create a document
* [get_ats_document](#get_ats_document) - Retrieve a document
* [list_ats_documents](#list_ats_documents) - List all documents
* [patch_ats_document](#patch_ats_document) - Update a document
* [remove_ats_document](#remove_ats_document) - Remove a document
* [update_ats_document](#update_ats_document) - Update a document

## create_ats_document

Create a document

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsDocumentRequest(
    connection_id='<value>',
)

res = s.document.create_ats_document(req, operations.CreateAtsDocumentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_document is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsDocumentRequest](../../models/operations/createatsdocumentrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateAtsDocumentSecurity](../../models/operations/createatsdocumentsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateAtsDocumentResponse](../../models/operations/createatsdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_document

Retrieve a document

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsDocumentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.document.get_ats_document(req, operations.GetAtsDocumentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_document is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsDocumentRequest](../../models/operations/getatsdocumentrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetAtsDocumentSecurity](../../models/operations/getatsdocumentsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetAtsDocumentResponse](../../models/operations/getatsdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_documents

List all documents

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsDocumentsRequest(
    connection_id='<value>',
)

res = s.document.list_ats_documents(req, operations.ListAtsDocumentsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_documents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsDocumentsRequest](../../models/operations/listatsdocumentsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListAtsDocumentsSecurity](../../models/operations/listatsdocumentssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListAtsDocumentsResponse](../../models/operations/listatsdocumentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_document

Update a document

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsDocumentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.document.patch_ats_document(req, operations.PatchAtsDocumentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_document is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsDocumentRequest](../../models/operations/patchatsdocumentrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchAtsDocumentSecurity](../../models/operations/patchatsdocumentsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchAtsDocumentResponse](../../models/operations/patchatsdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_document

Remove a document

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsDocumentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.document.remove_ats_document(req, operations.RemoveAtsDocumentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsDocumentRequest](../../models/operations/removeatsdocumentrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveAtsDocumentSecurity](../../models/operations/removeatsdocumentsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveAtsDocumentResponse](../../models/operations/removeatsdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_document

Update a document

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsDocumentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.document.update_ats_document(req, operations.UpdateAtsDocumentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_document is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsDocumentRequest](../../models/operations/updateatsdocumentrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateAtsDocumentSecurity](../../models/operations/updateatsdocumentsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateAtsDocumentResponse](../../models/operations/updateatsdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
