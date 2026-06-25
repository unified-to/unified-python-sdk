# Branch

## Overview

### Available Operations

* [create_repo_branch2](#create_repo_branch2) - Create a branch
* [get_repo_branch2](#get_repo_branch2) - Retrieve a branch
* [list_repo_branches2](#list_repo_branches2) - List all branches
* [patch_repo_branch2](#patch_repo_branch2) - Update a branch
* [remove_repo_branch2](#remove_repo_branch2) - Remove a branch
* [update_repo_branch2](#update_repo_branch2) - Update a branch

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

    res = unified_to.branch.create_repo_branch2(request={
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

    res = unified_to.branch.get_repo_branch2(request={
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

    res = unified_to.branch.list_repo_branches2(request={
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

    res = unified_to.branch.patch_repo_branch2(request={
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

    res = unified_to.branch.remove_repo_branch2(request={
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

    res = unified_to.branch.update_repo_branch2(request={
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