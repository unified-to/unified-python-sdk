# Repo
(*repo*)

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.create_repo_branch(request={
        "connection_id": "<id>",
    })

    if res.repo_branch is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.create_repo_commit(request={
        "connection_id": "<id>",
    })

    if res.repo_commit is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.create_repo_organization(request={
        "connection_id": "<id>",
    })

    if res.repo_organization is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.create_repo_pullrequest(request={
        "connection_id": "<id>",
    })

    if res.repo_pullrequest is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.create_repo_repository(request={
        "connection_id": "<id>",
    })

    if res.repo_repository is not None:
        # handle response
        pass

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

    if res.repo_branch is not None:
        # handle response
        pass

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

    if res.repo_commit is not None:
        # handle response
        pass

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

    if res.repo_organization is not None:
        # handle response
        pass

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

    if res.repo_pullrequest is not None:
        # handle response
        pass

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

    if res.repo_repository is not None:
        # handle response
        pass

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

    if res.repo_branches is not None:
        # handle response
        pass

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

    if res.repo_commits is not None:
        # handle response
        pass

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

    if res.repo_organizations is not None:
        # handle response
        pass

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

    if res.repo_pullrequests is not None:
        # handle response
        pass

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

    if res.repo_repositories is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.patch_repo_branch(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_branch is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.patch_repo_commit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_commit is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.patch_repo_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_organization is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.patch_repo_pullrequest(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_pullrequest is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.patch_repo_repository(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_repository is not None:
        # handle response
        pass

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

    if res is not None:
        # handle response
        pass

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

    if res is not None:
        # handle response
        pass

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

    if res is not None:
        # handle response
        pass

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

    if res is not None:
        # handle response
        pass

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

    if res is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.update_repo_branch(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_branch is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.update_repo_commit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_commit is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.update_repo_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_organization is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.update_repo_pullrequest(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_pullrequest is not None:
        # handle response
        pass

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.repo.update_repo_repository(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    if res.repo_repository is not None:
        # handle response
        pass

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