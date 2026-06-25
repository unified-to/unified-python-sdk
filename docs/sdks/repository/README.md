# Repository

## Overview

### Available Operations

* [create_repo_repository2](#create_repo_repository2) - Create a repository
* [get_repo_repository2](#get_repo_repository2) - Retrieve a repository
* [list_repo_repositories2](#list_repo_repositories2) - List all repositories
* [patch_repo_repository2](#patch_repo_repository2) - Update a repository
* [remove_repo_repository2](#remove_repo_repository2) - Remove a repository
* [update_repo_repository2](#update_repo_repository2) - Update a repository

## create_repo_repository2

Create a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoRepository2" method="post" path="/repo/{connection_id}/repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.create_repo_repository2(request={
        "repo_repository": {
            "name": "<value>",
        },
        "connection_id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateRepoRepository2Request](../../models/operations/createreporepository2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateRepoRepository2Response](../../models/operations/createreporepository2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_repository2

Retrieve a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoRepository2" method="get" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.get_repo_repository2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetRepoRepository2Request](../../models/operations/getreporepository2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetRepoRepository2Response](../../models/operations/getreporepository2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_repositories2

List all repositories

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoRepositories2" method="get" path="/repo/{connection_id}/repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.list_repo_repositories2(request={
        "connection_id": "<id>",
    })

    assert res.repo_repositories is not None

    # Handle response
    print(res.repo_repositories)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListRepoRepositories2Request](../../models/operations/listreporepositories2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListRepoRepositories2Response](../../models/operations/listreporepositories2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_repository2

Update a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoRepository2" method="patch" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.patch_repo_repository2(request={
        "repo_repository": {
            "name": "<value>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchRepoRepository2Request](../../models/operations/patchreporepository2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchRepoRepository2Response](../../models/operations/patchreporepository2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_repository2

Remove a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoRepository2" method="delete" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.remove_repo_repository2(request={
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
| `request`                                                                                          | [operations.RemoveRepoRepository2Request](../../models/operations/removereporepository2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveRepoRepository2Response](../../models/operations/removereporepository2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_repository2

Update a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoRepository2" method="put" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repository.update_repo_repository2(request={
        "repo_repository": {
            "name": "<value>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateRepoRepository2Request](../../models/operations/updatereporepository2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateRepoRepository2Response](../../models/operations/updatereporepository2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |