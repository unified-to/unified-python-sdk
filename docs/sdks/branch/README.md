# Branch

## Overview

### Available Operations

* [create_repo_branch](#create_repo_branch) - Create a branch
* [get_repo_branch](#get_repo_branch) - Retrieve a branch
* [list_repo_branches](#list_repo_branches) - List all branches
* [patch_repo_branch](#patch_repo_branch) - Update a branch
* [remove_repo_branch](#remove_repo_branch) - Remove a branch
* [update_repo_branch](#update_repo_branch) - Update a branch

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

    res = unified_to.branch.create_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "b23f2c76-54a4-4eb5-8868-c14999ec82bc",
            "name": "voluptas",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-03T17:49:49.232Z"),
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

    res = unified_to.branch.get_repo_branch(request={
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

    res = unified_to.branch.list_repo_branches(request={
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

    res = unified_to.branch.patch_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "f43b6486-07f1-4d4c-b5e4-a37a08a3c975",
            "name": "voluptas",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-03T17:49:49.233Z"),
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

    res = unified_to.branch.remove_repo_branch(request={
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

    res = unified_to.branch.update_repo_branch(request={
        "repo_branch": {
            "created_at": parse_datetime("2019-02-24T09:33:48.540Z"),
            "id": "f43b6486-07f1-4d4c-b5e4-a37a08a3c975",
            "name": "voluptas",
            "repo_id": "<id>",
            "updated_at": parse_datetime("2020-01-03T17:49:49.233Z"),
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