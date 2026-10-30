# Kms

## Overview

### Available Operations

* [create_kms_comment](#create_kms_comment) - Create a comment
* [create_kms_page](#create_kms_page) - Create a page
* [create_kms_space](#create_kms_space) - Create a space
* [get_kms_comment](#get_kms_comment) - Retrieve a comment
* [get_kms_page](#get_kms_page) - Retrieve a page
* [get_kms_space](#get_kms_space) - Retrieve a space
* [list_kms_comments](#list_kms_comments) - List all comments
* [list_kms_pages](#list_kms_pages) - List all pages
* [list_kms_spaces](#list_kms_spaces) - List all spaces
* [patch_kms_comment](#patch_kms_comment) - Update a comment
* [patch_kms_page](#patch_kms_page) - Update a page
* [patch_kms_space](#patch_kms_space) - Update a space
* [remove_kms_comment](#remove_kms_comment) - Remove a comment
* [remove_kms_page](#remove_kms_page) - Remove a page
* [remove_kms_space](#remove_kms_space) - Remove a space
* [update_kms_comment](#update_kms_comment) - Update a comment
* [update_kms_page](#update_kms_page) - Update a page
* [update_kms_space](#update_kms_space) - Update a space

## create_kms_comment

Creates a KmsComment. Provide the unified KmsComment fields in the request body; they are mapped to the provider's API. Returns the created KmsComment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createKmsComment" method="post" path="/kms/{connection_id}/comment" example="kms_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.create_kms_comment(request={
        "kms_comment": {
            "content": "Decimus tolero viriliter usque.",
            "content_type": shared.ContentType.HTML,
            "created_at": parse_datetime("2022-08-26T14:40:49.732Z"),
            "id": "16f85d7a-e59d-4f58-9761-033e7ee10a59",
            "metadata": [],
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-29T00:06:33.190Z"),
        },
        "connection_id": "<id>",
    })

    assert res.kms_comment is not None

    # Handle response
    print(res.kms_comment)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateKmsCommentRequest](../../models/operations/createkmscommentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateKmsCommentResponse](../../models/operations/createkmscommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_kms_page

Creates a KmsPage. Provide the unified KmsPage fields in the request body; they are mapped to the provider's API. Returns the created KmsPage.

### Example Usage

<!-- UsageSnippet language="python" operationID="createKmsPage" method="post" path="/kms/{connection_id}/page" example="kms_page" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.create_kms_page(request={
        "kms_page": {
            "created_at": parse_datetime("2019-05-20T18:06:50.749Z"),
            "download_url": "https://agitated-validity.info",
            "has_children": True,
            "id": "8dfe87aa-4192-4f7a-a749-16e172485d20",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-10-16T23:06:06.468Z"),
            "web_url": "https://another-petticoat.info",
        },
        "connection_id": "<id>",
    })

    assert res.kms_page is not None

    # Handle response
    print(res.kms_page)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateKmsPageRequest](../../models/operations/createkmspagerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateKmsPageResponse](../../models/operations/createkmspageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_kms_space

Creates a KmsSpace. Provide the unified KmsSpace fields in the request body; they are mapped to the provider's API. Returns the created KmsSpace.

### Example Usage

<!-- UsageSnippet language="python" operationID="createKmsSpace" method="post" path="/kms/{connection_id}/space" example="kms_space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.create_kms_space(request={
        "kms_space": {
            "created_at": parse_datetime("2022-10-31T00:56:54.246Z"),
            "description": "Acer.",
            "id": "756a9d7c-bb4b-4709-8a23-97c901c73368",
            "is_active": False,
            "metadata": [],
            "name": "into nor afore",
            "updated_at": parse_datetime("2026-01-06T03:39:13.485Z"),
        },
        "connection_id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateKmsSpaceRequest](../../models/operations/createkmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateKmsSpaceResponse](../../models/operations/createkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_kms_comment

Retrieves a single KmsComment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getKmsComment" method="get" path="/kms/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.get_kms_comment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_comment is not None

    # Handle response
    print(res.kms_comment)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetKmsCommentRequest](../../models/operations/getkmscommentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetKmsCommentResponse](../../models/operations/getkmscommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_kms_page

Retrieves a single KmsPage by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getKmsPage" method="get" path="/kms/{connection_id}/page/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.get_kms_page(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_page is not None

    # Handle response
    print(res.kms_page)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetKmsPageRequest](../../models/operations/getkmspagerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetKmsPageResponse](../../models/operations/getkmspageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_kms_space

Retrieves a single KmsSpace by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getKmsSpace" method="get" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.get_kms_space(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetKmsSpaceRequest](../../models/operations/getkmsspacerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetKmsSpaceResponse](../../models/operations/getkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_kms_comments

Returns a list of KmsComments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listKmsComments" method="get" path="/kms/{connection_id}/comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.list_kms_comments(request={
        "connection_id": "<id>",
    })

    assert res.kms_comments is not None

    # Handle response
    print(res.kms_comments)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListKmsCommentsRequest](../../models/operations/listkmscommentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListKmsCommentsResponse](../../models/operations/listkmscommentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_kms_pages

Returns a list of KmsPages. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listKmsPages" method="get" path="/kms/{connection_id}/page" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.list_kms_pages(request={
        "connection_id": "<id>",
    })

    assert res.kms_pages is not None

    # Handle response
    print(res.kms_pages)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListKmsPagesRequest](../../models/operations/listkmspagesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListKmsPagesResponse](../../models/operations/listkmspagesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_kms_spaces

Returns a list of KmsSpaces. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listKmsSpaces" method="get" path="/kms/{connection_id}/space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.list_kms_spaces(request={
        "connection_id": "<id>",
    })

    assert res.kms_spaces is not None

    # Handle response
    print(res.kms_spaces)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListKmsSpacesRequest](../../models/operations/listkmsspacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListKmsSpacesResponse](../../models/operations/listkmsspacesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_kms_comment

Updates the KmsComment identified by `id`. Provide the unified KmsComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchKmsComment" method="patch" path="/kms/{connection_id}/comment/{id}" example="kms_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.patch_kms_comment(request={
        "kms_comment": {
            "content": "Decimus tolero viriliter usque.",
            "content_type": shared.ContentType.HTML,
            "created_at": parse_datetime("2022-08-26T14:40:49.732Z"),
            "id": "e8cef14d-3762-4ee7-98b7-e89a23a1aa12",
            "metadata": [],
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-29T00:06:33.194Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_comment is not None

    # Handle response
    print(res.kms_comment)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchKmsCommentRequest](../../models/operations/patchkmscommentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchKmsCommentResponse](../../models/operations/patchkmscommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_kms_page

Updates the KmsPage identified by `id`. Provide the unified KmsPage fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchKmsPage" method="patch" path="/kms/{connection_id}/page/{id}" example="kms_page" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.patch_kms_page(request={
        "kms_page": {
            "created_at": parse_datetime("2019-05-20T18:06:50.749Z"),
            "download_url": "https://agitated-validity.info",
            "has_children": True,
            "id": "362b8f69-320d-4855-9e55-a868c0b7e66e",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-10-16T23:06:06.484Z"),
            "web_url": "https://another-petticoat.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_page is not None

    # Handle response
    print(res.kms_page)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchKmsPageRequest](../../models/operations/patchkmspagerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchKmsPageResponse](../../models/operations/patchkmspageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_kms_space

Updates the KmsSpace identified by `id`. Provide the unified KmsSpace fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchKmsSpace" method="patch" path="/kms/{connection_id}/space/{id}" example="kms_space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.patch_kms_space(request={
        "kms_space": {
            "created_at": parse_datetime("2022-10-31T00:56:54.246Z"),
            "description": "Acer.",
            "id": "77719217-9fb0-4a1f-9f25-584dc869c855",
            "is_active": False,
            "metadata": [],
            "name": "into nor afore",
            "updated_at": parse_datetime("2026-01-06T03:39:13.492Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchKmsSpaceRequest](../../models/operations/patchkmsspacerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchKmsSpaceResponse](../../models/operations/patchkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_kms_comment

Deletes the KmsComment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeKmsComment" method="delete" path="/kms/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.remove_kms_comment(request={
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
| `request`                                                                                | [operations.RemoveKmsCommentRequest](../../models/operations/removekmscommentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveKmsCommentResponse](../../models/operations/removekmscommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_kms_page

Deletes the KmsPage identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeKmsPage" method="delete" path="/kms/{connection_id}/page/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.remove_kms_page(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveKmsPageRequest](../../models/operations/removekmspagerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemoveKmsPageResponse](../../models/operations/removekmspageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_kms_space

Deletes the KmsSpace identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeKmsSpace" method="delete" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.remove_kms_space(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveKmsSpaceRequest](../../models/operations/removekmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveKmsSpaceResponse](../../models/operations/removekmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_kms_comment

Updates the KmsComment identified by `id`. Provide the unified KmsComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateKmsComment" method="put" path="/kms/{connection_id}/comment/{id}" example="kms_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.update_kms_comment(request={
        "kms_comment": {
            "content": "Decimus tolero viriliter usque.",
            "content_type": shared.ContentType.HTML,
            "created_at": parse_datetime("2022-08-26T14:40:49.732Z"),
            "id": "e8cef14d-3762-4ee7-98b7-e89a23a1aa12",
            "metadata": [],
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-29T00:06:33.194Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_comment is not None

    # Handle response
    print(res.kms_comment)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateKmsCommentRequest](../../models/operations/updatekmscommentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateKmsCommentResponse](../../models/operations/updatekmscommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_kms_page

Updates the KmsPage identified by `id`. Provide the unified KmsPage fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateKmsPage" method="put" path="/kms/{connection_id}/page/{id}" example="kms_page" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.update_kms_page(request={
        "kms_page": {
            "created_at": parse_datetime("2019-05-20T18:06:50.749Z"),
            "download_url": "https://agitated-validity.info",
            "has_children": True,
            "id": "362b8f69-320d-4855-9e55-a868c0b7e66e",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-10-16T23:06:06.484Z"),
            "web_url": "https://another-petticoat.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_page is not None

    # Handle response
    print(res.kms_page)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateKmsPageRequest](../../models/operations/updatekmspagerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateKmsPageResponse](../../models/operations/updatekmspageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_kms_space

Updates the KmsSpace identified by `id`. Provide the unified KmsSpace fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateKmsSpace" method="put" path="/kms/{connection_id}/space/{id}" example="kms_space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.kms.update_kms_space(request={
        "kms_space": {
            "created_at": parse_datetime("2022-10-31T00:56:54.246Z"),
            "description": "Acer.",
            "id": "77719217-9fb0-4a1f-9f25-584dc869c855",
            "is_active": False,
            "metadata": [],
            "name": "into nor afore",
            "updated_at": parse_datetime("2026-01-06T03:39:13.492Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateKmsSpaceRequest](../../models/operations/updatekmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateKmsSpaceResponse](../../models/operations/updatekmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |