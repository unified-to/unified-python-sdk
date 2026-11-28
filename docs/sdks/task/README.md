# Task

## Overview

### Available Operations

* [create_genai_task](#create_genai_task) - Create a task
* [create_task_comment](#create_task_comment) - Create a comment
* [create_task_project](#create_task_project) - Create a project
* [create_task_task](#create_task_task) - Create a task
* [get_genai_task](#get_genai_task) - Retrieve a task
* [get_task_change](#get_task_change) - Retrieve a change
* [get_task_comment](#get_task_comment) - Retrieve a comment
* [get_task_project](#get_task_project) - Retrieve a project
* [get_task_task](#get_task_task) - Retrieve a task
* [list_genai_tasks](#list_genai_tasks) - List all tasks
* [list_task_changes](#list_task_changes) - List all changes
* [list_task_comments](#list_task_comments) - List all comments
* [list_task_projects](#list_task_projects) - List all projects
* [list_task_tasks](#list_task_tasks) - List all tasks
* [patch_genai_task](#patch_genai_task) - Update a task
* [patch_task_comment](#patch_task_comment) - Update a comment
* [patch_task_project](#patch_task_project) - Update a project
* [patch_task_task](#patch_task_task) - Update a task
* [remove_genai_task](#remove_genai_task) - Remove a task
* [remove_task_comment](#remove_task_comment) - Remove a comment
* [remove_task_project](#remove_task_project) - Remove a project
* [remove_task_task](#remove_task_task) - Remove a task
* [update_genai_task](#update_genai_task) - Update a task
* [update_task_comment](#update_task_comment) - Update a comment
* [update_task_project](#update_task_project) - Update a project
* [update_task_task](#update_task_task) - Update a task

## create_genai_task

Creates a GenaiTask. Provide the unified GenaiTask fields in the request body; they are mapped to the provider's API. Returns the created GenaiTask.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiTask" method="post" path="/genai/{connection_id}/task" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.create_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-11-01T14:28:03.779Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "4dfde77e-1045-4fff-83e7-0bc6dd8ef8e9",
            "instructions": "Angustus cubo cupio abundans admoveo sumptus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Amet contigo tristis deripio auxilium cur aeternus cogito.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect online monitor",
            "pullrequest_url": "https://github.com/felicity.rowe61/eek-save/pull/383",
            "repo_url": "https://github.com/felicity.rowe61/eek-save",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-06-13T02:31:43.993Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Tenus via tamisium denego teres adsidue cura crur. Coma defungo magnam delicate confero amaritudo varius.",
            "target_branch_identifier": "agent/eek-save",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-13T03:25:39.115Z"),
            "web_url": "https://monstrous-honesty.net",
        },
        "connection_id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateGenaiTaskRequest](../../models/operations/creategenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateGenaiTaskResponse](../../models/operations/creategenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_task_comment

Creates a TaskComment. Provide the unified TaskComment fields in the request body; they are mapped to the provider's API. Returns the created TaskComment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTaskComment" method="post" path="/task/{connection_id}/comment" example="task_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.create_task_comment(request={
        "task_comment": {
            "created_at": parse_datetime("2019-10-12T20:33:37.879Z"),
            "has_children": False,
            "id": "7a805ab4-5ac8-437a-bb92-d49ff46846d9",
            "metadata": [],
            "text": "Tabernus circumvenio demens placeat.",
            "updated_at": parse_datetime("2021-10-14T00:36:09.183Z"),
        },
        "connection_id": "<id>",
    })

    assert res.task_comment is not None

    # Handle response
    print(res.task_comment)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTaskCommentRequest](../../models/operations/createtaskcommentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateTaskCommentResponse](../../models/operations/createtaskcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_task_project

Creates a TaskProject. Provide the unified TaskProject fields in the request body; they are mapped to the provider's API. Returns the created TaskProject.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTaskProject" method="post" path="/task/{connection_id}/project" example="task_project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.create_task_project(request={
        "task_project": {
            "created_at": parse_datetime("2023-06-23T16:39:40.446Z"),
            "description": "Curiositas.",
            "has_children": False,
            "has_tasks": False,
            "id": "84ea887c-2be9-47ab-910e-486a5d93b188",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "0938d2eb-78ab-45e0-b343-52c1cca85ae4",
                    "namespace": "custom",
                    "slug": "vox",
                    "value": "decens",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "d3f99a37-3081-4284-b583-054868f017b4",
                    "namespace": "custom",
                    "slug": "uterque",
                    "value": "benevolentia",
                },
            ],
            "name": "Baby",
            "updated_at": parse_datetime("2023-10-15T01:01:16.653Z"),
        },
        "connection_id": "<id>",
    })

    assert res.task_project is not None

    # Handle response
    print(res.task_project)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTaskProjectRequest](../../models/operations/createtaskprojectrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateTaskProjectResponse](../../models/operations/createtaskprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_task_task

Creates a TaskTask. Provide the unified TaskTask fields in the request body; they are mapped to the provider's API. Returns the created TaskTask.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTaskTask" method="post" path="/task/{connection_id}/task" example="task_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.create_task_task(request={
        "task_task": {
            "attachment_ids": [],
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2025-10-13T22:29:12.035Z"),
            "has_children": True,
            "id": "ac0c63be-7041-459e-a082-b822f858d630",
            "metadata": [],
            "name": "We need to connect the bluetooth IP sensor!",
            "notes": "Neque thymbra titulus absconditus peccatus crustulum tollo cometes. Vacuus eos cedo spero somnus utpote coadunatio denuncio adopto autus. Atrocitas vulnero concido rerum cura aveho torqueo tempore. Vomer tempore suscipit tutis clibanus valetudo vulnero pauper caput.",
            "priority": "MEDIUM",
            "progress": 33.0,
            "start_at": parse_datetime("2025-09-15T12:37:43.073Z"),
            "status": shared.TaskTaskStatus.OPENED,
            "story_points": 0.0,
            "tags": [
                "absorbeo",
                "correptius",
            ],
            "time_spent": 5359.0,
            "time_spent_unit": "SECONDS",
            "type": "antiquus",
            "updated_at": parse_datetime("2022-04-22T18:06:05.279Z"),
            "url": "https://knotty-heroine.info",
        },
        "connection_id": "<id>",
    })

    assert res.task_task is not None

    # Handle response
    print(res.task_task)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateTaskTaskRequest](../../models/operations/createtasktaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateTaskTaskResponse](../../models/operations/createtasktaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_task

Retrieves a single GenaiTask by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiTask" method="get" path="/genai/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.get_genai_task(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetGenaiTaskRequest](../../models/operations/getgenaitaskrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetGenaiTaskResponse](../../models/operations/getgenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_task_change

Retrieves a single TaskChange by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskChange" method="get" path="/task/{connection_id}/change/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.get_task_change(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_change is not None

    # Handle response
    print(res.task_change)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetTaskChangeRequest](../../models/operations/gettaskchangerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetTaskChangeResponse](../../models/operations/gettaskchangeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_task_comment

Retrieves a single TaskComment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskComment" method="get" path="/task/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.get_task_comment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_comment is not None

    # Handle response
    print(res.task_comment)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTaskCommentRequest](../../models/operations/gettaskcommentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetTaskCommentResponse](../../models/operations/gettaskcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_task_project

Retrieves a single TaskProject by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskProject" method="get" path="/task/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.get_task_project(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_project is not None

    # Handle response
    print(res.task_project)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTaskProjectRequest](../../models/operations/gettaskprojectrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetTaskProjectResponse](../../models/operations/gettaskprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_task_task

Retrieves a single TaskTask by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTaskTask" method="get" path="/task/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.get_task_task(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_task is not None

    # Handle response
    print(res.task_task)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetTaskTaskRequest](../../models/operations/gettasktaskrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetTaskTaskResponse](../../models/operations/gettasktaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_tasks

Returns a list of GenaiTasks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiTasks" method="get" path="/genai/{connection_id}/task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.list_genai_tasks(request={
        "connection_id": "<id>",
    })

    assert res.genai_tasks is not None

    # Handle response
    print(res.genai_tasks)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListGenaiTasksRequest](../../models/operations/listgenaitasksrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListGenaiTasksResponse](../../models/operations/listgenaitasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_changes

Returns a list of TaskChanges. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskChanges" method="get" path="/task/{connection_id}/change" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.list_task_changes(request={
        "connection_id": "<id>",
    })

    assert res.task_changes is not None

    # Handle response
    print(res.task_changes)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListTaskChangesRequest](../../models/operations/listtaskchangesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListTaskChangesResponse](../../models/operations/listtaskchangesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_comments

Returns a list of TaskComments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskComments" method="get" path="/task/{connection_id}/comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.list_task_comments(request={
        "connection_id": "<id>",
    })

    assert res.task_comments is not None

    # Handle response
    print(res.task_comments)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTaskCommentsRequest](../../models/operations/listtaskcommentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListTaskCommentsResponse](../../models/operations/listtaskcommentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_projects

Returns a list of TaskProjects. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskProjects" method="get" path="/task/{connection_id}/project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.list_task_projects(request={
        "connection_id": "<id>",
    })

    assert res.task_projects is not None

    # Handle response
    print(res.task_projects)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTaskProjectsRequest](../../models/operations/listtaskprojectsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListTaskProjectsResponse](../../models/operations/listtaskprojectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_task_tasks

Returns a list of TaskTasks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTaskTasks" method="get" path="/task/{connection_id}/task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.list_task_tasks(request={
        "connection_id": "<id>",
    })

    assert res.task_tasks is not None

    # Handle response
    print(res.task_tasks)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListTaskTasksRequest](../../models/operations/listtasktasksrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListTaskTasksResponse](../../models/operations/listtasktasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_task

Updates the GenaiTask identified by `id`. Provide the unified GenaiTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiTask" method="patch" path="/genai/{connection_id}/task/{id}" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.patch_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-11-01T14:28:03.795Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "d7626b7b-f0cf-4133-9553-34b468ca5544",
            "instructions": "Angustus cubo cupio abundans admoveo sumptus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Amet contigo tristis deripio auxilium cur aeternus cogito.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect online monitor",
            "pullrequest_url": "https://github.com/felicity.rowe61/eek-save/pull/383",
            "repo_url": "https://github.com/felicity.rowe61/eek-save",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-06-13T02:31:44.004Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Tenus via tamisium denego teres adsidue cura crur. Coma defungo magnam delicate confero amaritudo varius.",
            "target_branch_identifier": "agent/eek-save",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-13T03:25:39.123Z"),
            "web_url": "https://monstrous-honesty.net",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchGenaiTaskRequest](../../models/operations/patchgenaitaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchGenaiTaskResponse](../../models/operations/patchgenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_task_comment

Updates the TaskComment identified by `id`. Provide the unified TaskComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTaskComment" method="patch" path="/task/{connection_id}/comment/{id}" example="task_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.patch_task_comment(request={
        "task_comment": {
            "created_at": parse_datetime("2019-10-12T20:33:37.879Z"),
            "has_children": False,
            "id": "a51782cf-b839-4c7c-b1d6-dbd2deca29e0",
            "metadata": [],
            "text": "Tabernus circumvenio demens placeat.",
            "updated_at": parse_datetime("2021-10-14T00:36:09.187Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_comment is not None

    # Handle response
    print(res.task_comment)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchTaskCommentRequest](../../models/operations/patchtaskcommentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchTaskCommentResponse](../../models/operations/patchtaskcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_task_project

Updates the TaskProject identified by `id`. Provide the unified TaskProject fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTaskProject" method="patch" path="/task/{connection_id}/project/{id}" example="task_project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.patch_task_project(request={
        "task_project": {
            "created_at": parse_datetime("2023-06-23T16:39:40.446Z"),
            "description": "Curiositas.",
            "has_children": False,
            "has_tasks": False,
            "id": "0ab2b66d-f487-4bd6-9274-8e62519ad9ee",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "6154a499-7b88-477e-83dd-db98e2a9bba2",
                    "namespace": "custom",
                    "slug": "vox",
                    "value": "decens",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "be3a8318-2fbd-42fe-b1e9-c1c0dd2e9fdb",
                    "namespace": "custom",
                    "slug": "uterque",
                    "value": "benevolentia",
                },
            ],
            "name": "Baby",
            "updated_at": parse_datetime("2023-10-15T01:01:16.654Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_project is not None

    # Handle response
    print(res.task_project)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchTaskProjectRequest](../../models/operations/patchtaskprojectrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchTaskProjectResponse](../../models/operations/patchtaskprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_task_task

Updates the TaskTask identified by `id`. Provide the unified TaskTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTaskTask" method="patch" path="/task/{connection_id}/task/{id}" example="task_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.patch_task_task(request={
        "task_task": {
            "attachment_ids": [],
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2025-10-13T22:29:12.049Z"),
            "has_children": True,
            "id": "e91b4d7b-48ce-4d9c-8a7e-e8eaa5f92cb5",
            "metadata": [],
            "name": "We need to connect the bluetooth IP sensor!",
            "notes": "Neque thymbra titulus absconditus peccatus crustulum tollo cometes. Vacuus eos cedo spero somnus utpote coadunatio denuncio adopto autus. Atrocitas vulnero concido rerum cura aveho torqueo tempore. Vomer tempore suscipit tutis clibanus valetudo vulnero pauper caput.",
            "priority": "MEDIUM",
            "progress": 33.0,
            "start_at": parse_datetime("2025-09-15T12:37:43.087Z"),
            "status": shared.TaskTaskStatus.OPENED,
            "story_points": 0.0,
            "tags": [
                "absorbeo",
                "correptius",
            ],
            "time_spent": 5359.0,
            "time_spent_unit": "SECONDS",
            "type": "antiquus",
            "updated_at": parse_datetime("2022-04-22T18:06:05.286Z"),
            "url": "https://knotty-heroine.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_task is not None

    # Handle response
    print(res.task_task)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchTaskTaskRequest](../../models/operations/patchtasktaskrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchTaskTaskResponse](../../models/operations/patchtasktaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_task

Deletes the GenaiTask identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiTask" method="delete" path="/genai/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.remove_genai_task(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveGenaiTaskRequest](../../models/operations/removegenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveGenaiTaskResponse](../../models/operations/removegenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_task_comment

Deletes the TaskComment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTaskComment" method="delete" path="/task/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.remove_task_comment(request={
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
| `request`                                                                                  | [operations.RemoveTaskCommentRequest](../../models/operations/removetaskcommentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveTaskCommentResponse](../../models/operations/removetaskcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_task_project

Deletes the TaskProject identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTaskProject" method="delete" path="/task/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.remove_task_project(request={
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
| `request`                                                                                  | [operations.RemoveTaskProjectRequest](../../models/operations/removetaskprojectrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveTaskProjectResponse](../../models/operations/removetaskprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_task_task

Deletes the TaskTask identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTaskTask" method="delete" path="/task/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.remove_task_task(request={
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
| `request`                                                                            | [operations.RemoveTaskTaskRequest](../../models/operations/removetasktaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveTaskTaskResponse](../../models/operations/removetasktaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_task

Updates the GenaiTask identified by `id`. Provide the unified GenaiTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiTask" method="put" path="/genai/{connection_id}/task/{id}" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.update_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-11-01T14:28:03.795Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "d7626b7b-f0cf-4133-9553-34b468ca5544",
            "instructions": "Angustus cubo cupio abundans admoveo sumptus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Amet contigo tristis deripio auxilium cur aeternus cogito.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect online monitor",
            "pullrequest_url": "https://github.com/felicity.rowe61/eek-save/pull/383",
            "repo_url": "https://github.com/felicity.rowe61/eek-save",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-06-13T02:31:44.004Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Tenus via tamisium denego teres adsidue cura crur. Coma defungo magnam delicate confero amaritudo varius.",
            "target_branch_identifier": "agent/eek-save",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-13T03:25:39.123Z"),
            "web_url": "https://monstrous-honesty.net",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateGenaiTaskRequest](../../models/operations/updategenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateGenaiTaskResponse](../../models/operations/updategenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_task_comment

Updates the TaskComment identified by `id`. Provide the unified TaskComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTaskComment" method="put" path="/task/{connection_id}/comment/{id}" example="task_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.update_task_comment(request={
        "task_comment": {
            "created_at": parse_datetime("2019-10-12T20:33:37.879Z"),
            "has_children": False,
            "id": "a51782cf-b839-4c7c-b1d6-dbd2deca29e0",
            "metadata": [],
            "text": "Tabernus circumvenio demens placeat.",
            "updated_at": parse_datetime("2021-10-14T00:36:09.187Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_comment is not None

    # Handle response
    print(res.task_comment)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateTaskCommentRequest](../../models/operations/updatetaskcommentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateTaskCommentResponse](../../models/operations/updatetaskcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_task_project

Updates the TaskProject identified by `id`. Provide the unified TaskProject fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTaskProject" method="put" path="/task/{connection_id}/project/{id}" example="task_project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.update_task_project(request={
        "task_project": {
            "created_at": parse_datetime("2023-06-23T16:39:40.446Z"),
            "description": "Curiositas.",
            "has_children": False,
            "has_tasks": False,
            "id": "0ab2b66d-f487-4bd6-9274-8e62519ad9ee",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "6154a499-7b88-477e-83dd-db98e2a9bba2",
                    "namespace": "custom",
                    "slug": "vox",
                    "value": "decens",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "be3a8318-2fbd-42fe-b1e9-c1c0dd2e9fdb",
                    "namespace": "custom",
                    "slug": "uterque",
                    "value": "benevolentia",
                },
            ],
            "name": "Baby",
            "updated_at": parse_datetime("2023-10-15T01:01:16.654Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_project is not None

    # Handle response
    print(res.task_project)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateTaskProjectRequest](../../models/operations/updatetaskprojectrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateTaskProjectResponse](../../models/operations/updatetaskprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_task_task

Updates the TaskTask identified by `id`. Provide the unified TaskTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTaskTask" method="put" path="/task/{connection_id}/task/{id}" example="task_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.task.update_task_task(request={
        "task_task": {
            "attachment_ids": [],
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2025-10-13T22:29:12.049Z"),
            "has_children": True,
            "id": "e91b4d7b-48ce-4d9c-8a7e-e8eaa5f92cb5",
            "metadata": [],
            "name": "We need to connect the bluetooth IP sensor!",
            "notes": "Neque thymbra titulus absconditus peccatus crustulum tollo cometes. Vacuus eos cedo spero somnus utpote coadunatio denuncio adopto autus. Atrocitas vulnero concido rerum cura aveho torqueo tempore. Vomer tempore suscipit tutis clibanus valetudo vulnero pauper caput.",
            "priority": "MEDIUM",
            "progress": 33.0,
            "start_at": parse_datetime("2025-09-15T12:37:43.087Z"),
            "status": shared.TaskTaskStatus.OPENED,
            "story_points": 0.0,
            "tags": [
                "absorbeo",
                "correptius",
            ],
            "time_spent": 5359.0,
            "time_spent_unit": "SECONDS",
            "type": "antiquus",
            "updated_at": parse_datetime("2022-04-22T18:06:05.286Z"),
            "url": "https://knotty-heroine.info",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.task_task is not None

    # Handle response
    print(res.task_task)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateTaskTaskRequest](../../models/operations/updatetasktaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateTaskTaskResponse](../../models/operations/updatetasktaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |