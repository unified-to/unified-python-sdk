# Document

## Overview

### Available Operations

* [create_ats_document](#create_ats_document) - Create a document
* [create_healthcare_document](#create_healthcare_document) - Create a document
* [create_hris_document](#create_hris_document) - Create a document
* [create_signing_document](#create_signing_document) - Create a document
* [get_ats_document](#get_ats_document) - Retrieve a document
* [get_healthcare_document](#get_healthcare_document) - Retrieve a document
* [get_hris_document](#get_hris_document) - Retrieve a document
* [get_signing_document](#get_signing_document) - Retrieve a document
* [list_ats_documents](#list_ats_documents) - List all documents
* [list_healthcare_documents](#list_healthcare_documents) - List all documents
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

Creates a AtsDocument. Provide the unified AtsDocument fields in the request body; they are mapped to the provider's API. Returns the created AtsDocument.

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
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "bcbfcfef-289c-4401-b483-9bce5c194d2f",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-09T11:26:35.968Z"),
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

## create_healthcare_document

Creates a HealthcareDocument. Provide the unified HealthcareDocument fields in the request body; they are mapped to the provider's API. Returns the created HealthcareDocument.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHealthcareDocument" method="post" path="/healthcare/{connection_id}/document" example="healthcare_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.create_healthcare_document(request={
        "healthcare_document": {
            "authored_at": parse_datetime("2023-07-16T04:00:25.853Z"),
            "codes": [
                {
                    "code": "23671711",
                    "display": "History and physical",
                    "system": "http://loinc.org",
                },
            ],
            "created_at": parse_datetime("2023-07-16T04:00:25.853Z"),
            "document_url": "https://overcooked-yogurt.org",
            "filename": "ugh_after.elc",
            "id": "9f31f1f8-bba9-4f65-a6b5-ec78e2effe61",
            "metadata": [],
            "mime_type": "application/pdf",
            "name": "History and physical",
            "status": shared.HealthcareDocumentStatus.SUPERSEDED,
            "type": shared.HealthcareDocumentType.CONSULTATION_NOTE,
            "updated_at": parse_datetime("2024-12-30T18:48:28.483Z"),
        },
        "connection_id": "<id>",
    })

    assert res.healthcare_document is not None

    # Handle response
    print(res.healthcare_document)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateHealthcareDocumentRequest](../../models/operations/createhealthcaredocumentrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateHealthcareDocumentResponse](../../models/operations/createhealthcaredocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_document

Creates a HrisDocument. Provide the unified HrisDocument fields in the request body; they are mapped to the provider's API. Returns the created HrisDocument.

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
            "id": "8c618430-40f5-4aa0-b4f6-14ff27c84bd8",
            "metadata": [],
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-10-18T07:09:10.496Z"),
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

Creates a SigningDocument. Provide the unified SigningDocument fields in the request body; they are mapped to the provider's API. Returns the created SigningDocument.

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
            "description": "Aer asporto caste umbra coerceo anser color allatus aestas perspiciatis.",
            "expires_at": parse_datetime("2021-06-04T01:21:34.949Z"),
            "id": "e0d43f49-dcf7-4a03-836c-62ed385844c4",
            "metadata": [],
            "name": "Denesik Group NDA",
            "sent_at": parse_datetime("2022-07-01T10:02:09.383Z"),
            "status": shared.SigningDocumentStatus.DRAFT,
            "updated_at": parse_datetime("2025-09-10T02:30:46.339Z"),
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

Retrieves a single AtsDocument by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

## get_healthcare_document

Retrieves a single HealthcareDocument by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareDocument" method="get" path="/healthcare/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.get_healthcare_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_document is not None

    # Handle response
    print(res.healthcare_document)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetHealthcareDocumentRequest](../../models/operations/gethealthcaredocumentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetHealthcareDocumentResponse](../../models/operations/gethealthcaredocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_document

Retrieves a single HrisDocument by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single SigningDocument by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AtsDocuments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

## list_healthcare_documents

Returns a list of HealthcareDocuments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareDocuments" method="get" path="/healthcare/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.document.list_healthcare_documents(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_documents is not None

    # Handle response
    print(res.healthcare_documents)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListHealthcareDocumentsRequest](../../models/operations/listhealthcaredocumentsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListHealthcareDocumentsResponse](../../models/operations/listhealthcaredocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_documents

Returns a list of HrisDocuments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of SigningDocuments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AtsDocument identified by `id`. Provide the unified AtsDocument fields to change in the request body.

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
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "2478154c-c3c3-432c-9c7d-ffec06ebbe77",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-09T11:26:35.973Z"),
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

Updates the HrisDocument identified by `id`. Provide the unified HrisDocument fields to change in the request body.

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
            "id": "3113d3f0-cefb-4c89-b9bc-9c25fc0e3ca3",
            "metadata": [],
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-10-18T07:09:10.508Z"),
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

Updates the SigningDocument identified by `id`. Provide the unified SigningDocument fields to change in the request body.

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
            "description": "Aer asporto caste umbra coerceo anser color allatus aestas perspiciatis.",
            "expires_at": parse_datetime("2021-06-04T01:21:34.949Z"),
            "id": "8475d973-3b71-4bba-abd0-5efcc34276fa",
            "metadata": [],
            "name": "Denesik Group NDA",
            "sent_at": parse_datetime("2022-07-01T10:02:09.385Z"),
            "status": shared.SigningDocumentStatus.DRAFT,
            "updated_at": parse_datetime("2025-09-10T02:30:46.348Z"),
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

Deletes the AtsDocument identified by `id`.

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

Deletes the HrisDocument identified by `id`.

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

Deletes the SigningDocument identified by `id`.

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

Updates the AtsDocument identified by `id`. Provide the unified AtsDocument fields to change in the request body.

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
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "2478154c-c3c3-432c-9c7d-ffec06ebbe77",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-09T11:26:35.973Z"),
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

Updates the HrisDocument identified by `id`. Provide the unified HrisDocument fields to change in the request body.

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
            "id": "3113d3f0-cefb-4c89-b9bc-9c25fc0e3ca3",
            "metadata": [],
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-10-18T07:09:10.508Z"),
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

Updates the SigningDocument identified by `id`. Provide the unified SigningDocument fields to change in the request body.

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
            "description": "Aer asporto caste umbra coerceo anser color allatus aestas perspiciatis.",
            "expires_at": parse_datetime("2021-06-04T01:21:34.949Z"),
            "id": "8475d973-3b71-4bba-abd0-5efcc34276fa",
            "metadata": [],
            "name": "Denesik Group NDA",
            "sent_at": parse_datetime("2022-07-01T10:02:09.385Z"),
            "status": shared.SigningDocumentStatus.DRAFT,
            "updated_at": parse_datetime("2025-09-10T02:30:46.348Z"),
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