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

Create a comment

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
            "id": "30d3f3cc-b753-4748-9916-96e018b1a819",
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-17T04:28:29.168Z"),
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

Create a page

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
            "id": "35025d82-bdff-4cd1-a869-f045e9573f18",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-09-13T04:14:05.570Z"),
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

Create a space

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
            "id": "fda8200a-a977-4ada-9566-fb710e734aa0",
            "is_active": False,
            "name": "into nor afore",
            "updated_at": parse_datetime("2025-12-05T21:21:09.630Z"),
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

Retrieve a comment

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

Retrieve a page

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

Retrieve a space

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

List all comments

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

List all pages

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

List all spaces

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

Update a comment

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
            "id": "dc097808-b17e-49d3-a3d7-7d3c2d3ecb3d",
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-17T04:28:29.172Z"),
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

Update a page

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
            "id": "7a66eec3-b362-49af-8737-9b08671edcb0",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-09-13T04:14:05.587Z"),
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

Update a space

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
            "id": "3ecc896e-07c6-4e0f-b3aa-4033aea9fb77",
            "is_active": False,
            "name": "into nor afore",
            "updated_at": parse_datetime("2025-12-05T21:21:09.637Z"),
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

Remove a comment

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

Remove a page

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

Remove a space

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

Update a comment

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
            "id": "dc097808-b17e-49d3-a3d7-7d3c2d3ecb3d",
            "type": shared.KmsCommentType.PAGE,
            "updated_at": parse_datetime("2023-11-17T04:28:29.172Z"),
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

Update a page

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
            "id": "7a66eec3-b362-49af-8737-9b08671edcb0",
            "is_active": True,
            "metadata": [],
            "title": "even minister extract",
            "type": shared.KmsPageType.HTML,
            "updated_at": parse_datetime("2025-09-13T04:14:05.587Z"),
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

Update a space

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
            "id": "3ecc896e-07c6-4e0f-b3aa-4033aea9fb77",
            "is_active": False,
            "name": "into nor afore",
            "updated_at": parse_datetime("2025-12-05T21:21:09.637Z"),
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