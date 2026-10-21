# Repo

## Overview

### Available Operations

* [create_repo_branch](#create_repo_branch) - Create a branch
* [create_repo_commit](#create_repo_commit) - Create a commit
* [create_repo_organization](#create_repo_organization) - Create an organization
* [create_repo_pullrequest](#create_repo_pullrequest) - Create a pullrequest
* [create_repo_repository](#create_repo_repository) - Create a repository
* [get_repo_branch](#get_repo_branch) - Retrieve a branch
* [get_repo_commit](#get_repo_commit) - Retrieve a commit
* [get_repo_organization](#get_repo_organization) - Retrieve an organization
* [get_repo_pullrequest](#get_repo_pullrequest) - Retrieve a pullrequest
* [get_repo_repository](#get_repo_repository) - Retrieve a repository
* [list_repo_branches](#list_repo_branches) - List all branches
* [list_repo_commits](#list_repo_commits) - List all commits
* [list_repo_organizations](#list_repo_organizations) - List all organizations
* [list_repo_pullrequests](#list_repo_pullrequests) - List all pullrequests
* [list_repo_repositories](#list_repo_repositories) - List all repositories
* [patch_repo_branch](#patch_repo_branch) - Update a branch
* [patch_repo_commit](#patch_repo_commit) - Update a commit
* [patch_repo_organization](#patch_repo_organization) - Update an organization
* [patch_repo_pullrequest](#patch_repo_pullrequest) - Update a pullrequest
* [patch_repo_repository](#patch_repo_repository) - Update a repository
* [remove_repo_branch](#remove_repo_branch) - Remove a branch
* [remove_repo_commit](#remove_repo_commit) - Remove a commit
* [remove_repo_organization](#remove_repo_organization) - Remove an organization
* [remove_repo_pullrequest](#remove_repo_pullrequest) - Remove a pullrequest
* [remove_repo_repository](#remove_repo_repository) - Remove a repository
* [update_repo_branch](#update_repo_branch) - Update a branch
* [update_repo_commit](#update_repo_commit) - Update a commit
* [update_repo_organization](#update_repo_organization) - Update an organization
* [update_repo_pullrequest](#update_repo_pullrequest) - Update a pullrequest
* [update_repo_repository](#update_repo_repository) - Update a repository

## create_repo_branch

Create a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoBranch" method="post" path="/repo/{connection_id}/branch" example="repo_branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "1977544f-f608-4b0c-95f6-93d6c8b189fc",
            "metadata": [],
            "name": "transmitter-calculate",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-07T08:02:21.811Z"),
        },
        "connection_id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateRepoBranchRequest](../../models/operations/createrepobranchrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateRepoBranchResponse](../../models/operations/createrepobranchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_commit

Create a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoCommit" method="post" path="/repo/{connection_id}/commit" example="repo_commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "ea7fc4cb-af24-4313-a099-e8898d5527b7",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-05-31T06:49:09.389Z"),
        },
        "connection_id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateRepoCommitRequest](../../models/operations/createrepocommitrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateRepoCommitResponse](../../models/operations/createrepocommitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_organization

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoOrganization" method="post" path="/repo/{connection_id}/organization" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "80e8a6fd-a1fe-49b5-9218-70e0019ddd60",
            "metadata": [],
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-21T15:07:00.136Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
        "connection_id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateRepoOrganizationRequest](../../models/operations/createrepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateRepoOrganizationResponse](../../models/operations/createrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_pullrequest

Create a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoPullrequest" method="post" path="/repo/{connection_id}/pullrequest" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-05-01T13:49:56.790Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "107e687f-47df-41e1-8207-aad4e09e6700",
            "labels": [
                "creptio",
                "tutamen",
            ],
            "metadata": [],
            "notes": "Texo advoco bibo amet. Defero coadunatio turbo curtus. Consuasor aggero veritatis suggero adeo.",
            "status": shared.RepoPullrequestStatus.APPROVED,
            "title": "reboot mobile application",
            "updated_at": parse_datetime("2026-01-17T07:02:05.496Z"),
        },
        "connection_id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateRepoPullrequestRequest](../../models/operations/createrepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateRepoPullrequestResponse](../../models/operations/createrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_repo_repository

Create a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="createRepoRepository" method="post" path="/repo/{connection_id}/repository" example="repo_repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.create_repo_repository(request={
        "repo_repository": {
            "created_at": parse_datetime("2023-06-12T09:42:00.080Z"),
            "description": "Sed somnus crastinus armarium.",
            "id": "66453156-002c-4535-9f4c-2752f08a0ce6",
            "is_private": False,
            "metadata": [],
            "name": "bah-bogus",
            "updated_at": parse_datetime("2024-03-01T02:04:01.289Z"),
            "web_url": "https://neat-birdbath.org",
        },
        "connection_id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateRepoRepositoryRequest](../../models/operations/createreporepositoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateRepoRepositoryResponse](../../models/operations/createreporepositoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_branch

Retrieve a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoBranch" method="get" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_branch(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetRepoBranchRequest](../../models/operations/getrepobranchrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetRepoBranchResponse](../../models/operations/getrepobranchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_commit

Retrieve a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoCommit" method="get" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_commit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetRepoCommitRequest](../../models/operations/getrepocommitrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetRepoCommitResponse](../../models/operations/getrepocommitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoOrganization" method="get" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetRepoOrganizationRequest](../../models/operations/getrepoorganizationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetRepoOrganizationResponse](../../models/operations/getrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_pullrequest

Retrieve a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoPullrequest" method="get" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_pullrequest(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetRepoPullrequestRequest](../../models/operations/getrepopullrequestrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetRepoPullrequestResponse](../../models/operations/getrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_repo_repository

Retrieve a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="getRepoRepository" method="get" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.get_repo_repository(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetRepoRepositoryRequest](../../models/operations/getreporepositoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetRepoRepositoryResponse](../../models/operations/getreporepositoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_branches

List all branches

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoBranches" method="get" path="/repo/{connection_id}/branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_branches(request={
        "connection_id": "<id>",
    })

    assert res.repo_branches is not None

    # Handle response
    print(res.repo_branches)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListRepoBranchesRequest](../../models/operations/listrepobranchesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListRepoBranchesResponse](../../models/operations/listrepobranchesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_commits

List all commits

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoCommits" method="get" path="/repo/{connection_id}/commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_commits(request={
        "connection_id": "<id>",
    })

    assert res.repo_commits is not None

    # Handle response
    print(res.repo_commits)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListRepoCommitsRequest](../../models/operations/listrepocommitsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListRepoCommitsResponse](../../models/operations/listrepocommitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoOrganizations" method="get" path="/repo/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_organizations(request={
        "connection_id": "<id>",
    })

    assert res.repo_organizations is not None

    # Handle response
    print(res.repo_organizations)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListRepoOrganizationsRequest](../../models/operations/listrepoorganizationsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListRepoOrganizationsResponse](../../models/operations/listrepoorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_pullrequests

List all pullrequests

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoPullrequests" method="get" path="/repo/{connection_id}/pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_pullrequests(request={
        "connection_id": "<id>",
    })

    assert res.repo_pullrequests is not None

    # Handle response
    print(res.repo_pullrequests)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListRepoPullrequestsRequest](../../models/operations/listrepopullrequestsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListRepoPullrequestsResponse](../../models/operations/listrepopullrequestsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_repo_repositories

List all repositories

### Example Usage

<!-- UsageSnippet language="python" operationID="listRepoRepositories" method="get" path="/repo/{connection_id}/repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.list_repo_repositories(request={
        "connection_id": "<id>",
    })

    assert res.repo_repositories is not None

    # Handle response
    print(res.repo_repositories)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListRepoRepositoriesRequest](../../models/operations/listreporepositoriesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListRepoRepositoriesResponse](../../models/operations/listreporepositoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_branch

Update a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoBranch" method="patch" path="/repo/{connection_id}/branch/{id}" example="repo_branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "6dc80949-6f8b-4219-b731-291c308a1a44",
            "metadata": [],
            "name": "transmitter-calculate",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-07T08:02:21.812Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_branch is not None

    # Handle response
    print(res.repo_branch)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchRepoBranchRequest](../../models/operations/patchrepobranchrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchRepoBranchResponse](../../models/operations/patchrepobranchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_commit

Update a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoCommit" method="patch" path="/repo/{connection_id}/commit/{id}" example="repo_commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "6f4cd413-c6d3-406d-aacc-2b96e1fae49a",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-05-31T06:49:09.401Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_commit is not None

    # Handle response
    print(res.repo_commit)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchRepoCommitRequest](../../models/operations/patchrepocommitrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchRepoCommitResponse](../../models/operations/patchrepocommitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoOrganization" method="patch" path="/repo/{connection_id}/organization/{id}" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "ad9a058b-873e-4876-a837-1b47d35c0e0e",
            "metadata": [],
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-21T15:07:00.140Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_organization is not None

    # Handle response
    print(res.repo_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchRepoOrganizationRequest](../../models/operations/patchrepoorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchRepoOrganizationResponse](../../models/operations/patchrepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_pullrequest

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoPullrequest" method="patch" path="/repo/{connection_id}/pullrequest/{id}" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-05-01T13:49:56.801Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "743d6e2e-ff01-4226-87e4-63e082360e6c",
            "labels": [
                "creptio",
                "tutamen",
            ],
            "metadata": [],
            "notes": "Texo advoco bibo amet. Defero coadunatio turbo curtus. Consuasor aggero veritatis suggero adeo.",
            "status": shared.RepoPullrequestStatus.APPROVED,
            "title": "reboot mobile application",
            "updated_at": parse_datetime("2026-01-17T07:02:05.510Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_pullrequest is not None

    # Handle response
    print(res.repo_pullrequest)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchRepoPullrequestRequest](../../models/operations/patchrepopullrequestrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchRepoPullrequestResponse](../../models/operations/patchrepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_repo_repository

Update a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="patchRepoRepository" method="patch" path="/repo/{connection_id}/repository/{id}" example="repo_repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.patch_repo_repository(request={
        "repo_repository": {
            "created_at": parse_datetime("2023-06-12T09:42:00.080Z"),
            "description": "Sed somnus crastinus armarium.",
            "id": "c2277c4c-e335-4cde-b578-cf33cb4ca875",
            "is_private": False,
            "metadata": [],
            "name": "bah-bogus",
            "updated_at": parse_datetime("2024-03-01T02:04:01.292Z"),
            "web_url": "https://neat-birdbath.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.repo_repository is not None

    # Handle response
    print(res.repo_repository)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchRepoRepositoryRequest](../../models/operations/patchreporepositoryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchRepoRepositoryResponse](../../models/operations/patchreporepositoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_branch

Remove a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoBranch" method="delete" path="/repo/{connection_id}/branch/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_branch(request={
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
| `request`                                                                                | [operations.RemoveRepoBranchRequest](../../models/operations/removerepobranchrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveRepoBranchResponse](../../models/operations/removerepobranchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_commit

Remove a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoCommit" method="delete" path="/repo/{connection_id}/commit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_commit(request={
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
| `request`                                                                                | [operations.RemoveRepoCommitRequest](../../models/operations/removerepocommitrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveRepoCommitResponse](../../models/operations/removerepocommitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_organization

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoOrganization" method="delete" path="/repo/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_organization(request={
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
| `request`                                                                                            | [operations.RemoveRepoOrganizationRequest](../../models/operations/removerepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveRepoOrganizationResponse](../../models/operations/removerepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_pullrequest

Remove a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoPullrequest" method="delete" path="/repo/{connection_id}/pullrequest/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_pullrequest(request={
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
| `request`                                                                                          | [operations.RemoveRepoPullrequestRequest](../../models/operations/removerepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveRepoPullrequestResponse](../../models/operations/removerepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_repo_repository

Remove a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="removeRepoRepository" method="delete" path="/repo/{connection_id}/repository/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.remove_repo_repository(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveRepoRepositoryRequest](../../models/operations/removereporepositoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveRepoRepositoryResponse](../../models/operations/removereporepositoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_branch

Update a branch

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoBranch" method="put" path="/repo/{connection_id}/branch/{id}" example="repo_branch" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "6dc80949-6f8b-4219-b731-291c308a1a44",
            "metadata": [],
            "name": "transmitter-calculate",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-07T08:02:21.812Z"),
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
| `request`                                                                                | [operations.UpdateRepoBranchRequest](../../models/operations/updaterepobranchrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateRepoBranchResponse](../../models/operations/updaterepobranchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_commit

Update a commit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoCommit" method="put" path="/repo/{connection_id}/commit/{id}" example="repo_commit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "6f4cd413-c6d3-406d-aacc-2b96e1fae49a",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-05-31T06:49:09.401Z"),
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
| `request`                                                                                | [operations.UpdateRepoCommitRequest](../../models/operations/updaterepocommitrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateRepoCommitResponse](../../models/operations/updaterepocommitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoOrganization" method="put" path="/repo/{connection_id}/organization/{id}" example="repo_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_organization(request={
        "repo_organization": {
            "avatar_url": "https://picsum.photos/seed/fGl6Lb/3157/3173",
            "created_at": parse_datetime("2022-07-07T00:18:40.748Z"),
            "description": "Trepide defendo supra testimonium ager.",
            "id": "ad9a058b-873e-4876-a837-1b47d35c0e0e",
            "metadata": [],
            "name": "Denesik - Lemke",
            "updated_at": parse_datetime("2023-08-21T15:07:00.140Z"),
            "web_url": "https://turbulent-overheard.biz",
        },
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
| `request`                                                                                            | [operations.UpdateRepoOrganizationRequest](../../models/operations/updaterepoorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateRepoOrganizationResponse](../../models/operations/updaterepoorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_pullrequest

Update a pullrequest

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoPullrequest" method="put" path="/repo/{connection_id}/pullrequest/{id}" example="repo_pullrequest" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_pullrequest(request={
        "repo_pullrequest": {
            "closed_at": parse_datetime("2025-05-01T13:49:56.801Z"),
            "created_at": parse_datetime("2023-02-27T09:37:13.663Z"),
            "id": "743d6e2e-ff01-4226-87e4-63e082360e6c",
            "labels": [
                "creptio",
                "tutamen",
            ],
            "metadata": [],
            "notes": "Texo advoco bibo amet. Defero coadunatio turbo curtus. Consuasor aggero veritatis suggero adeo.",
            "status": shared.RepoPullrequestStatus.APPROVED,
            "title": "reboot mobile application",
            "updated_at": parse_datetime("2026-01-17T07:02:05.510Z"),
        },
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
| `request`                                                                                          | [operations.UpdateRepoPullrequestRequest](../../models/operations/updaterepopullrequestrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateRepoPullrequestResponse](../../models/operations/updaterepopullrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_repo_repository

Update a repository

### Example Usage

<!-- UsageSnippet language="python" operationID="updateRepoRepository" method="put" path="/repo/{connection_id}/repository/{id}" example="repo_repository" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.repo.update_repo_repository(request={
        "repo_repository": {
            "created_at": parse_datetime("2023-06-12T09:42:00.080Z"),
            "description": "Sed somnus crastinus armarium.",
            "id": "c2277c4c-e335-4cde-b578-cf33cb4ca875",
            "is_private": False,
            "metadata": [],
            "name": "bah-bogus",
            "updated_at": parse_datetime("2024-03-01T02:04:01.292Z"),
            "web_url": "https://neat-birdbath.org",
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
| `request`                                                                                        | [operations.UpdateRepoRepositoryRequest](../../models/operations/updatereporepositoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateRepoRepositoryResponse](../../models/operations/updatereporepositoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |