# Commit

## Overview

### Available Operations

* [create_repo_commit](#create_repo_commit) - Create a commit
* [get_repo_commit](#get_repo_commit) - Retrieve a commit
* [list_repo_commits](#list_repo_commits) - List all commits
* [patch_repo_commit](#patch_repo_commit) - Update a commit
* [remove_repo_commit](#remove_repo_commit) - Remove a commit
* [update_repo_commit](#update_repo_commit) - Update a commit

## create_repo_commit

Creates a RepoCommit. Provide the unified RepoCommit fields in the request body; they are mapped to the provider's API. Returns the created RepoCommit.

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

    res = unified_to.commit.create_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "6ec7848b-e61e-41af-9fdc-1d35759ff404",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-06-04T10:29:21.433Z"),
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

## get_repo_commit

Retrieves a single RepoCommit by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

    res = unified_to.commit.get_repo_commit(request={
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

## list_repo_commits

Returns a list of RepoCommits. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

    res = unified_to.commit.list_repo_commits(request={
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

## patch_repo_commit

Updates the RepoCommit identified by `id`. Provide the unified RepoCommit fields to change in the request body.

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

    res = unified_to.commit.patch_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "e13d1a41-49b4-4424-b2d8-f32eb135dd92",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-06-04T10:29:21.441Z"),
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

## remove_repo_commit

Deletes the RepoCommit identified by `id`.

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

    res = unified_to.commit.remove_repo_commit(request={
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

## update_repo_commit

Updates the RepoCommit identified by `id`. Provide the unified RepoCommit fields to change in the request body.

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

    res = unified_to.commit.update_repo_commit(request={
        "repo_commit": {
            "created_at": parse_datetime("2020-07-12T16:20:42.520Z"),
            "id": "e13d1a41-49b4-4424-b2d8-f32eb135dd92",
            "lines_added": 313.0,
            "lines_changed": 659.0,
            "lines_deleted": 482.0,
            "message": "quantify bluetooth bandwidth",
            "metadata": [],
            "repo_id": "<id>",
            "updated_at": parse_datetime("2023-06-04T10:29:21.441Z"),
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