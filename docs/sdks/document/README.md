# Document

## Overview

### Available Operations

* [create_ats_document](#create_ats_document) - Create a document
* [create_hris_document](#create_hris_document) - Create a document
* [create_signing_document](#create_signing_document) - Create a document
* [get_ats_document](#get_ats_document) - Retrieve a document
* [get_hris_document](#get_hris_document) - Retrieve a document
* [get_signing_document](#get_signing_document) - Retrieve a document
* [list_ats_documents](#list_ats_documents) - List all documents
* [list_hris_documents](#list_hris_documents) - List all documents
* [list_signing_documents](#list_signing_documents) - List all documents
* [patch_ats_document](#patch_ats_document) - Update a document
* [patch_hris_document](#patch_hris_document) - Update a document
* [patch_signing_document](#patch_signing_document) - Update a document
* [remove_ats_document](#remove_ats_document) - Remove a document
* [remove_hris_document](#remove_hris_document) - Remove a document
* [remove_signing_document](#remove_signing_document) - Remove a document
* [update_ats_document](#update_ats_document) - Update a document
* [update_hris_document](#update_hris_document) - Update a document
* [update_signing_document](#update_signing_document) - Update a document

## create_ats_document

Create a document

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsDocument" method="post" path="/ats/{connection_id}/document" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.create_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "bah_white_frantically.bz",
            "id": "9f225f20-6c03-4714-921f-d2f617898f4b",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-11-29T15:00:47.310Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAtsDocumentRequest](../../models/operations/createatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAtsDocumentResponse](../../models/operations/createatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_document

Create a document

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDocument" method="post" path="/hris/{connection_id}/document" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.create_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "c36ce7b1-e96d-4546-8310-2b1cd2427e9f",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-19T03:46:30.170Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisDocumentRequest](../../models/operations/createhrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisDocumentResponse](../../models/operations/createhrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_signing_document

Create a document

### Example Usage

<!-- UsageSnippet language="python" operationID="createSigningDocument" method="post" path="/signing/{connection_id}/document" example="signing_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.create_signing_document(request={
        "signing_document": {
            "created_at": parse_datetime("2021-05-02T09:35:23.679Z"),
            "expires_at": parse_datetime("2026-12-19T05:25:05.101Z"),
            "id": "c5eb1751-2c24-4374-a11d-57a0e58ba9fd",
            "name": "nam audax absens",
            "status": shared.SigningDocumentStatus.VOIDED,
            "updated_at": parse_datetime("2025-08-09T23:26:52.148Z"),
        },
        "connection_id": "<id>",
    })

    assert res.signing_document is not None

    # Handle response
    print(res.signing_document)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateSigningDocumentRequest](../../models/operations/createsigningdocumentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateSigningDocumentResponse](../../models/operations/createsigningdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_document

Retrieve a document

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsDocument" method="get" path="/ats/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.get_ats_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAtsDocumentRequest](../../models/operations/getatsdocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAtsDocumentResponse](../../models/operations/getatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_document

Retrieve a document

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDocument" method="get" path="/hris/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.get_hris_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisDocumentRequest](../../models/operations/gethrisdocumentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisDocumentResponse](../../models/operations/gethrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_signing_document

Retrieve a document

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningDocument" method="get" path="/signing/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.get_signing_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_document is not None

    # Handle response
    print(res.signing_document)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSigningDocumentRequest](../../models/operations/getsigningdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetSigningDocumentResponse](../../models/operations/getsigningdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_documents

List all documents

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsDocuments" method="get" path="/ats/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.list_ats_documents(request={
        "connection_id": "<id>",
    })

    assert res.ats_documents is not None

    # Handle response
    print(res.ats_documents)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAtsDocumentsRequest](../../models/operations/listatsdocumentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAtsDocumentsResponse](../../models/operations/listatsdocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_documents

List all documents

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDocuments" method="get" path="/hris/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.list_hris_documents(request={
        "connection_id": "<id>",
    })

    assert res.hris_documents is not None

    # Handle response
    print(res.hris_documents)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisDocumentsRequest](../../models/operations/listhrisdocumentsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisDocumentsResponse](../../models/operations/listhrisdocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_documents

List all documents

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningDocuments" method="get" path="/signing/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.list_signing_documents(request={
        "connection_id": "<id>",
    })

    assert res.signing_documents is not None

    # Handle response
    print(res.signing_documents)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListSigningDocumentsRequest](../../models/operations/listsigningdocumentsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListSigningDocumentsResponse](../../models/operations/listsigningdocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsDocument" method="patch" path="/ats/{connection_id}/document/{id}" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.patch_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "bah_white_frantically.bz",
            "id": "55958542-606c-4129-9319-a150223fc4df",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-11-29T15:00:47.312Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAtsDocumentRequest](../../models/operations/patchatsdocumentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAtsDocumentResponse](../../models/operations/patchatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDocument" method="patch" path="/hris/{connection_id}/document/{id}" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.patch_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "23391a53-5d85-4874-b27c-6cc01144df3c",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-19T03:46:30.178Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisDocumentRequest](../../models/operations/patchhrisdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisDocumentResponse](../../models/operations/patchhrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_signing_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="patchSigningDocument" method="patch" path="/signing/{connection_id}/document/{id}" example="signing_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.patch_signing_document(request={
        "signing_document": {
            "created_at": parse_datetime("2021-05-02T09:35:23.679Z"),
            "expires_at": parse_datetime("2026-12-19T05:25:05.113Z"),
            "id": "d881c945-1384-49fe-b1fd-eca616cd73b3",
            "name": "nam audax absens",
            "status": shared.SigningDocumentStatus.VOIDED,
            "updated_at": parse_datetime("2025-08-09T23:26:52.158Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_document is not None

    # Handle response
    print(res.signing_document)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchSigningDocumentRequest](../../models/operations/patchsigningdocumentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchSigningDocumentResponse](../../models/operations/patchsigningdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_document

Remove a document

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsDocument" method="delete" path="/ats/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.remove_ats_document(request={
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
| `request`                                                                                  | [operations.RemoveAtsDocumentRequest](../../models/operations/removeatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAtsDocumentResponse](../../models/operations/removeatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_document

Remove a document

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDocument" method="delete" path="/hris/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.remove_hris_document(request={
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
| `request`                                                                                    | [operations.RemoveHrisDocumentRequest](../../models/operations/removehrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisDocumentResponse](../../models/operations/removehrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_signing_document

Remove a document

### Example Usage

<!-- UsageSnippet language="python" operationID="removeSigningDocument" method="delete" path="/signing/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.remove_signing_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveSigningDocumentRequest](../../models/operations/removesigningdocumentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveSigningDocumentResponse](../../models/operations/removesigningdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsDocument" method="put" path="/ats/{connection_id}/document/{id}" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.update_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "bah_white_frantically.bz",
            "id": "55958542-606c-4129-9319-a150223fc4df",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-11-29T15:00:47.312Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAtsDocumentRequest](../../models/operations/updateatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAtsDocumentResponse](../../models/operations/updateatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDocument" method="put" path="/hris/{connection_id}/document/{id}" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.update_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "23391a53-5d85-4874-b27c-6cc01144df3c",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-19T03:46:30.178Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisDocumentRequest](../../models/operations/updatehrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisDocumentResponse](../../models/operations/updatehrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_signing_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSigningDocument" method="put" path="/signing/{connection_id}/document/{id}" example="signing_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.update_signing_document(request={
        "signing_document": {
            "created_at": parse_datetime("2021-05-02T09:35:23.679Z"),
            "expires_at": parse_datetime("2026-12-19T05:25:05.113Z"),
            "id": "d881c945-1384-49fe-b1fd-eca616cd73b3",
            "name": "nam audax absens",
            "status": shared.SigningDocumentStatus.VOIDED,
            "updated_at": parse_datetime("2025-08-09T23:26:52.158Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_document is not None

    # Handle response
    print(res.signing_document)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateSigningDocumentRequest](../../models/operations/updatesigningdocumentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateSigningDocumentResponse](../../models/operations/updatesigningdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |