# Plm

## Overview

### Available Operations

* [create_plm_bomline](#create_plm_bomline) - Create a bomline
* [create_plm_change](#create_plm_change) - Create a change
* [create_plm_document](#create_plm_document) - Create a document
* [create_plm_part](#create_plm_part) - Create a part
* [get_plm_bomline](#get_plm_bomline) - Retrieve a bomline
* [get_plm_category](#get_plm_category) - Retrieve a category
* [get_plm_change](#get_plm_change) - Retrieve a change
* [get_plm_document](#get_plm_document) - Retrieve a document
* [get_plm_part](#get_plm_part) - Retrieve a part
* [list_plm_bomlines](#list_plm_bomlines) - List all bomlines
* [list_plm_categories](#list_plm_categories) - List all categories
* [list_plm_changes](#list_plm_changes) - List all changes
* [list_plm_documents](#list_plm_documents) - List all documents
* [list_plm_parts](#list_plm_parts) - List all parts
* [patch_plm_bomline](#patch_plm_bomline) - Update a bomline
* [patch_plm_change](#patch_plm_change) - Update a change
* [patch_plm_document](#patch_plm_document) - Update a document
* [patch_plm_part](#patch_plm_part) - Update a part
* [remove_plm_bomline](#remove_plm_bomline) - Remove a bomline
* [update_plm_bomline](#update_plm_bomline) - Update a bomline
* [update_plm_change](#update_plm_change) - Update a change
* [update_plm_document](#update_plm_document) - Update a document
* [update_plm_part](#update_plm_part) - Update a part

## create_plm_bomline

Creates a PlmBomline. Provide the unified PlmBomline fields in the request body; they are mapped to the provider's API. Returns the created PlmBomline.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmBomline" method="post" path="/plm/{connection_id}/bomline" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.create_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "65169d61-4bde-4d5a-9a76-52f3303e416a",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-19T11:24:47.265Z"),
        },
        "connection_id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreatePlmBomlineRequest](../../models/operations/createplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreatePlmBomlineResponse](../../models/operations/createplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_plm_change

Creates a PlmChange. Provide the unified PlmChange fields in the request body; they are mapped to the provider's API. Returns the created PlmChange.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmChange" method="post" path="/plm/{connection_id}/change" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.create_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "be14cec1-7986-493b-9e07-d0c14abd673c",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-25T06:48:23.466Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePlmChangeRequest](../../models/operations/createplmchangerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreatePlmChangeResponse](../../models/operations/createplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_plm_document

Creates a PlmDocument. Provide the unified PlmDocument fields in the request body; they are mapped to the provider's API. Returns the created PlmDocument.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmDocument" method="post" path="/plm/{connection_id}/document" example="plm_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.create_plm_document(request={
        "plm_document": {
            "created_at": parse_datetime("2020-10-16T01:44:30.293Z"),
            "file_ids": [],
            "id": "45511ca2-86d9-41da-9a1a-15f9a8868993",
            "lifecycle_state": "Under Review",
            "master_identifier": "0c59b0d3-c1d6-4710-8880-42837a488951",
            "metadata": [],
            "name": "Procedure taxicab",
            "number": "DOC-086886",
            "original_type": "Procedure",
            "revision": "C",
            "status": shared.PlmDocumentStatus.IN_REVIEW,
            "type": shared.PlmDocumentType.PROCEDURE,
            "updated_at": parse_datetime("2026-09-06T00:31:45.146Z"),
            "url": "https://uncommon-guide.info/",
        },
        "connection_id": "<id>",
    })

    assert res.plm_document is not None

    # Handle response
    print(res.plm_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePlmDocumentRequest](../../models/operations/createplmdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreatePlmDocumentResponse](../../models/operations/createplmdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_plm_part

Creates a PlmPart. Provide the unified PlmPart fields in the request body; they are mapped to the provider's API. Returns the created PlmPart.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlmPart" method="post" path="/plm/{connection_id}/part" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.create_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "67a58332-7e9a-4e37-8136-e3471f3305f4",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "4f750190-7628-4930-91fb-f82252ea6c5c",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T20:25:22.392Z"),
            "url": "https://inborn-independence.info",
        },
        "connection_id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreatePlmPartRequest](../../models/operations/createplmpartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreatePlmPartResponse](../../models/operations/createplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_bomline

Retrieves a single PlmBomline by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmBomline" method="get" path="/plm/{connection_id}/bomline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.get_plm_bomline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetPlmBomlineRequest](../../models/operations/getplmbomlinerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetPlmBomlineResponse](../../models/operations/getplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_category

Retrieves a single PlmCategory by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmCategory" method="get" path="/plm/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.get_plm_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_category is not None

    # Handle response
    print(res.plm_category)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPlmCategoryRequest](../../models/operations/getplmcategoryrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetPlmCategoryResponse](../../models/operations/getplmcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_change

Retrieves a single PlmChange by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmChange" method="get" path="/plm/{connection_id}/change/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.get_plm_change(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetPlmChangeRequest](../../models/operations/getplmchangerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetPlmChangeResponse](../../models/operations/getplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_document

Retrieves a single PlmDocument by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmDocument" method="get" path="/plm/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.get_plm_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_document is not None

    # Handle response
    print(res.plm_document)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPlmDocumentRequest](../../models/operations/getplmdocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetPlmDocumentResponse](../../models/operations/getplmdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_plm_part

Retrieves a single PlmPart by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlmPart" method="get" path="/plm/{connection_id}/part/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.get_plm_part(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetPlmPartRequest](../../models/operations/getplmpartrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetPlmPartResponse](../../models/operations/getplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_bomlines

Returns a list of PlmBomlines. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmBomlines" method="get" path="/plm/{connection_id}/bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.list_plm_bomlines(request={
        "connection_id": "<id>",
    })

    assert res.plm_bomlines is not None

    # Handle response
    print(res.plm_bomlines)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListPlmBomlinesRequest](../../models/operations/listplmbomlinesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListPlmBomlinesResponse](../../models/operations/listplmbomlinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_categories

Returns a list of PlmCategories. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmCategories" method="get" path="/plm/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.list_plm_categories(request={
        "connection_id": "<id>",
    })

    assert res.plm_categories is not None

    # Handle response
    print(res.plm_categories)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPlmCategoriesRequest](../../models/operations/listplmcategoriesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListPlmCategoriesResponse](../../models/operations/listplmcategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_changes

Returns a list of PlmChanges. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmChanges" method="get" path="/plm/{connection_id}/change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.list_plm_changes(request={
        "connection_id": "<id>",
    })

    assert res.plm_changes is not None

    # Handle response
    print(res.plm_changes)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListPlmChangesRequest](../../models/operations/listplmchangesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListPlmChangesResponse](../../models/operations/listplmchangesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_documents

Returns a list of PlmDocuments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmDocuments" method="get" path="/plm/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.list_plm_documents(request={
        "connection_id": "<id>",
    })

    assert res.plm_documents is not None

    # Handle response
    print(res.plm_documents)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListPlmDocumentsRequest](../../models/operations/listplmdocumentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListPlmDocumentsResponse](../../models/operations/listplmdocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_plm_parts

Returns a list of PlmParts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPlmParts" method="get" path="/plm/{connection_id}/part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.list_plm_parts(request={
        "connection_id": "<id>",
    })

    assert res.plm_parts is not None

    # Handle response
    print(res.plm_parts)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPlmPartsRequest](../../models/operations/listplmpartsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListPlmPartsResponse](../../models/operations/listplmpartsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_bomline

Updates the PlmBomline identified by `id`. Provide the unified PlmBomline fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmBomline" method="patch" path="/plm/{connection_id}/bomline/{id}" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.patch_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "0f0665e8-5cf9-4f22-89a3-043b1be81ada",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-19T11:24:47.267Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchPlmBomlineRequest](../../models/operations/patchplmbomlinerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchPlmBomlineResponse](../../models/operations/patchplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_change

Updates the PlmChange identified by `id`. Provide the unified PlmChange fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmChange" method="patch" path="/plm/{connection_id}/change/{id}" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.patch_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "cdc2f535-fd0d-476d-ab8a-9d10f418d6e8",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-25T06:48:23.482Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchPlmChangeRequest](../../models/operations/patchplmchangerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchPlmChangeResponse](../../models/operations/patchplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_document

Updates the PlmDocument identified by `id`. Provide the unified PlmDocument fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmDocument" method="patch" path="/plm/{connection_id}/document/{id}" example="plm_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.patch_plm_document(request={
        "plm_document": {
            "created_at": parse_datetime("2020-10-16T01:44:30.293Z"),
            "file_ids": [],
            "id": "984d14c7-bb6c-4a30-bbdf-a59be599f733",
            "lifecycle_state": "Under Review",
            "master_identifier": "2fe40ece-190e-4b28-adc7-13ea03d10c7f",
            "metadata": [],
            "name": "Procedure taxicab",
            "number": "DOC-086886",
            "original_type": "Procedure",
            "revision": "C",
            "status": shared.PlmDocumentStatus.IN_REVIEW,
            "type": shared.PlmDocumentType.PROCEDURE,
            "updated_at": parse_datetime("2026-09-06T00:31:45.163Z"),
            "url": "https://uncommon-guide.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_document is not None

    # Handle response
    print(res.plm_document)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchPlmDocumentRequest](../../models/operations/patchplmdocumentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchPlmDocumentResponse](../../models/operations/patchplmdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_plm_part

Updates the PlmPart identified by `id`. Provide the unified PlmPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPlmPart" method="patch" path="/plm/{connection_id}/part/{id}" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.patch_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "4c938a15-c13c-4fea-8737-3829eac9fbd2",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "a50aba23-6cf9-4204-bc51-1e84590cd580",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T20:25:22.396Z"),
            "url": "https://inborn-independence.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchPlmPartRequest](../../models/operations/patchplmpartrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchPlmPartResponse](../../models/operations/patchplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_plm_bomline

Deletes the PlmBomline identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePlmBomline" method="delete" path="/plm/{connection_id}/bomline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.remove_plm_bomline(request={
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
| `request`                                                                                | [operations.RemovePlmBomlineRequest](../../models/operations/removeplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemovePlmBomlineResponse](../../models/operations/removeplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_bomline

Updates the PlmBomline identified by `id`. Provide the unified PlmBomline fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmBomline" method="put" path="/plm/{connection_id}/bomline/{id}" example="plm_bomline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.update_plm_bomline(request={
        "plm_bomline": {
            "created_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "effective_at": parse_datetime("2022-04-02T07:09:29.598Z"),
            "id": "0f0665e8-5cf9-4f22-89a3-043b1be81ada",
            "quantity": 7.0,
            "reference_designators": [],
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2023-04-19T11:24:47.267Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_bomline is not None

    # Handle response
    print(res.plm_bomline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdatePlmBomlineRequest](../../models/operations/updateplmbomlinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdatePlmBomlineResponse](../../models/operations/updateplmbomlineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_change

Updates the PlmChange identified by `id`. Provide the unified PlmChange fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmChange" method="put" path="/plm/{connection_id}/change/{id}" example="plm_change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.update_plm_change(request={
        "plm_change": {
            "affected_items": [],
            "created_at": parse_datetime("2021-08-02T05:58:32.287Z"),
            "description": "Vorago spiculum avaritia adipiscor callide.",
            "id": "cdc2f535-fd0d-476d-ab8a-9d10f418d6e8",
            "metadata": [],
            "name": "Update goodwill",
            "number": "ECO-6591",
            "priority": "Medium",
            "status": shared.PlmChangeStatus.IN_REVIEW,
            "type": shared.PlmChangeType.ORDER,
            "updated_at": parse_datetime("2026-09-25T06:48:23.482Z"),
            "url": "https://warmhearted-fraudster.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_change is not None

    # Handle response
    print(res.plm_change)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdatePlmChangeRequest](../../models/operations/updateplmchangerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdatePlmChangeResponse](../../models/operations/updateplmchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_document

Updates the PlmDocument identified by `id`. Provide the unified PlmDocument fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmDocument" method="put" path="/plm/{connection_id}/document/{id}" example="plm_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.update_plm_document(request={
        "plm_document": {
            "created_at": parse_datetime("2020-10-16T01:44:30.293Z"),
            "file_ids": [],
            "id": "984d14c7-bb6c-4a30-bbdf-a59be599f733",
            "lifecycle_state": "Under Review",
            "master_identifier": "2fe40ece-190e-4b28-adc7-13ea03d10c7f",
            "metadata": [],
            "name": "Procedure taxicab",
            "number": "DOC-086886",
            "original_type": "Procedure",
            "revision": "C",
            "status": shared.PlmDocumentStatus.IN_REVIEW,
            "type": shared.PlmDocumentType.PROCEDURE,
            "updated_at": parse_datetime("2026-09-06T00:31:45.163Z"),
            "url": "https://uncommon-guide.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_document is not None

    # Handle response
    print(res.plm_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdatePlmDocumentRequest](../../models/operations/updateplmdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdatePlmDocumentResponse](../../models/operations/updateplmdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_plm_part

Updates the PlmPart identified by `id`. Provide the unified PlmPart fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePlmPart" method="put" path="/plm/{connection_id}/part/{id}" example="plm_part" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.plm.update_plm_part(request={
        "plm_part": {
            "created_at": parse_datetime("2019-04-13T06:25:34.770Z"),
            "description": "Pectus tero ulterius aestivus talis tero ullam cruciamentum.",
            "document_ids": [],
            "file_ids": [],
            "id": "4c938a15-c13c-4fea-8737-3829eac9fbd2",
            "is_assembly": False,
            "lifecycle_state": "Design",
            "master_identifier": "a50aba23-6cf9-4204-bc51-1e84590cd580",
            "metadata": [],
            "name": "grumpy PCB",
            "number": "PRT-009154",
            "original_type": "Software",
            "revision": "B",
            "source": shared.Source.MAKE,
            "status": shared.PlmPartStatus.IN_WORK,
            "type": shared.PlmPartType.SOFTWARE,
            "unit_of_measure": "EA",
            "updated_at": parse_datetime("2021-04-11T20:25:22.396Z"),
            "url": "https://inborn-independence.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.plm_part is not None

    # Handle response
    print(res.plm_part)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdatePlmPartRequest](../../models/operations/updateplmpartrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdatePlmPartResponse](../../models/operations/updateplmpartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |