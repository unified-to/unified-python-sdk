# Repo

## Overview

### Available Operations

* [create_repo_branch2](#create_repo_branch2) - Create a branch
* [create_repo_commit2](#create_repo_commit2) - Create a commit
* [create_repo_organization2](#create_repo_organization2) - Create an organization
* [create_repo_pullrequest2](#create_repo_pullrequest2) - Create a pullrequest
* [create_repo_repository2](#create_repo_repository2) - Create a repository
* [get_repo_branch2](#get_repo_branch2) - Retrieve a branch
* [get_repo_commit2](#get_repo_commit2) - Retrieve a commit
* [get_repo_organization2](#get_repo_organization2) - Retrieve an organization
* [get_repo_pullrequest2](#get_repo_pullrequest2) - Retrieve a pullrequest
* [get_repo_repository2](#get_repo_repository2) - Retrieve a repository
* [list_repo_branches2](#list_repo_branches2) - List all branches
* [list_repo_commits2](#list_repo_commits2) - List all commits
* [list_repo_organizations2](#list_repo_organizations2) - List all organizations
* [list_repo_pullrequests2](#list_repo_pullrequests2) - List all pullrequests
* [list_repo_repositories2](#list_repo_repositories2) - List all repositories
* [patch_repo_branch2](#patch_repo_branch2) - Update a branch
* [patch_repo_commit2](#patch_repo_commit2) - Update a commit
* [patch_repo_organization2](#patch_repo_organization2) - Update an organization
* [patch_repo_pullrequest2](#patch_repo_pullrequest2) - Update a pullrequest
* [patch_repo_repository2](#patch_repo_repository2) - Update a repository
* [remove_repo_branch2](#remove_repo_branch2) - Remove a branch
* [remove_repo_commit2](#remove_repo_commit2) - Remove a commit
* [remove_repo_organization2](#remove_repo_organization2) - Remove an organization
* [remove_repo_pullrequest2](#remove_repo_pullrequest2) - Remove a pullrequest
* [remove_repo_repository2](#remove_repo_repository2) - Remove a repository
* [update_repo_branch2](#update_repo_branch2) - Update a branch
* [update_repo_commit2](#update_repo_commit2) - Update a commit
* [update_repo_organization2](#update_repo_organization2) - Update an organization
* [update_repo_pullrequest2](#update_repo_pullrequest2) - Update a pullrequest
* [update_repo_repository2](#update_repo_repository2) - Update a repository

## create_repo_branch2

Create a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoBranch2" method="post" path="/repo/{connection_id}/branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_branch2(request={
        "repo_branch": {
            "name": "<value>",
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateRepoBranch2Request](../../models/operations/createrepobranch2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateRepoBranch2Response](../../models/operations/createrepobranch2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_commit2

Create a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoCommit2" method="post" path="/repo/{connection_id}/commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_commit2(request={
        "repo_commit": {
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateRepoCommit2Request](../../models/operations/createrepocommit2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateRepoCommit2Response](../../models/operations/createrepocommit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_organization2

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoOrganization2" method="post" path="/repo/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_organization2(request={
        "repo_organization": {},
        "connection_id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateRepoOrganization2Request](../../models/operations/createrepoorganization2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateRepoOrganization2Response](../../models/operations/createrepoorganization2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_pullrequest2

Create a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoPullrequest2" method="post" path="/repo/{connection_id}/pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_pullrequest2(request={
        "repo_pullrequest": {},
        "connection_id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateRepoPullrequest2Request](../../models/operations/createrepopullrequest2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateRepoPullrequest2Response](../../models/operations/createrepopullrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.repo.create_repo_repository2(request={
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

## get_repo_branch2

Retrieve a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoBranch2" method="get" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_branch2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRepoBranch2Request](../../models/operations/getrepobranch2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetRepoBranch2Response](../../models/operations/getrepobranch2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_commit2

Retrieve a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoCommit2" method="get" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_commit2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRepoCommit2Request](../../models/operations/getrepocommit2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetRepoCommit2Response](../../models/operations/getrepocommit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_organization2

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoOrganization2" method="get" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_organization2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetRepoOrganization2Request](../../models/operations/getrepoorganization2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetRepoOrganization2Response](../../models/operations/getrepoorganization2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_pullrequest2

Retrieve a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoPullrequest2" method="get" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_pullrequest2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetRepoPullrequest2Request](../../models/operations/getrepopullrequest2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetRepoPullrequest2Response](../../models/operations/getrepopullrequest2response.md)**

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

    res = unified_to.repo.get_repo_repository2(request={
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

## list_repo_branches2

List all branches

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoBranches2" method="get" path="/repo/{connection_id}/branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_branches2(request={
        "connection_id": "<id>",
    })

    assert res.repo_branches is not None

    # Handle response
    print(res.repo_branches)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListRepoBranches2Request](../../models/operations/listrepobranches2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListRepoBranches2Response](../../models/operations/listrepobranches2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_commits2

List all commits

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoCommits2" method="get" path="/repo/{connection_id}/commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_commits2(request={
        "connection_id": "<id>",
    })

    assert res.repo_commits is not None

    # Handle response
    print(res.repo_commits)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListRepoCommits2Request](../../models/operations/listrepocommits2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListRepoCommits2Response](../../models/operations/listrepocommits2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_organizations2

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoOrganizations2" method="get" path="/repo/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_organizations2(request={
        "connection_id": "<id>",
    })

    assert res.repo_organizations is not None

    # Handle response
    print(res.repo_organizations)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListRepoOrganizations2Request](../../models/operations/listrepoorganizations2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListRepoOrganizations2Response](../../models/operations/listrepoorganizations2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_pullrequests2

List all pullrequests

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoPullrequests2" method="get" path="/repo/{connection_id}/pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_pullrequests2(request={
        "connection_id": "<id>",
    })

    assert res.repo_pullrequests is not None

    # Handle response
    print(res.repo_pullrequests)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListRepoPullrequests2Request](../../models/operations/listrepopullrequests2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListRepoPullrequests2Response](../../models/operations/listrepopullrequests2response.md)**

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

    res = unified_to.repo.list_repo_repositories2(request={
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

## patch_repo_branch2

Update a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoBranch2" method="patch" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_branch2(request={
        "repo_branch": {
            "name": "<value>",
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchRepoBranch2Request](../../models/operations/patchrepobranch2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchRepoBranch2Response](../../models/operations/patchrepobranch2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_commit2

Update a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoCommit2" method="patch" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_commit2(request={
        "repo_commit": {
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchRepoCommit2Request](../../models/operations/patchrepocommit2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchRepoCommit2Response](../../models/operations/patchrepocommit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_organization2

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoOrganization2" method="patch" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_organization2(request={
        "repo_organization": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchRepoOrganization2Request](../../models/operations/patchrepoorganization2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchRepoOrganization2Response](../../models/operations/patchrepoorganization2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_pullrequest2

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoPullrequest2" method="patch" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_pullrequest2(request={
        "repo_pullrequest": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchRepoPullrequest2Request](../../models/operations/patchrepopullrequest2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchRepoPullrequest2Response](../../models/operations/patchrepopullrequest2response.md)**

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

    res = unified_to.repo.patch_repo_repository2(request={
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

## remove_repo_branch2

Remove a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoBranch2" method="delete" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_branch2(request={
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
| `request`                                                                                  | [operations.RemoveRepoBranch2Request](../../models/operations/removerepobranch2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveRepoBranch2Response](../../models/operations/removerepobranch2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_commit2

Remove a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoCommit2" method="delete" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_commit2(request={
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
| `request`                                                                                  | [operations.RemoveRepoCommit2Request](../../models/operations/removerepocommit2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveRepoCommit2Response](../../models/operations/removerepocommit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_organization2

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoOrganization2" method="delete" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_organization2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveRepoOrganization2Request](../../models/operations/removerepoorganization2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveRepoOrganization2Response](../../models/operations/removerepoorganization2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_pullrequest2

Remove a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoPullrequest2" method="delete" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_pullrequest2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveRepoPullrequest2Request](../../models/operations/removerepopullrequest2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveRepoPullrequest2Response](../../models/operations/removerepopullrequest2response.md)**

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

    res = unified_to.repo.remove_repo_repository2(request={
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

## update_repo_branch2

Update a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoBranch2" method="put" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_branch2(request={
        "repo_branch": {
            "name": "<value>",
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateRepoBranch2Request](../../models/operations/updaterepobranch2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateRepoBranch2Response](../../models/operations/updaterepobranch2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_commit2

Update a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoCommit2" method="put" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_commit2(request={
        "repo_commit": {
            "repo_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateRepoCommit2Request](../../models/operations/updaterepocommit2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateRepoCommit2Response](../../models/operations/updaterepocommit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_organization2

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoOrganization2" method="put" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_organization2(request={
        "repo_organization": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateRepoOrganization2Request](../../models/operations/updaterepoorganization2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateRepoOrganization2Response](../../models/operations/updaterepoorganization2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_pullrequest2

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoPullrequest2" method="put" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_pullrequest2(request={
        "repo_pullrequest": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateRepoPullrequest2Request](../../models/operations/updaterepopullrequest2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateRepoPullrequest2Response](../../models/operations/updaterepopullrequest2response.md)**

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

    res = unified_to.repo.update_repo_repository2(request={
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