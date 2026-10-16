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

Create a task

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
            "completed_at": parse_datetime("2025-09-27T01:15:18.106Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "3cfa7dd8-8cf5-44d5-bb6e-16f8cbfa0fe0",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-18T09:06:31.229Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-02-24T07:12:18.305Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
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

Create a comment

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
            "has_children": True,
            "id": "78a4b519-d824-475f-adcf-fcd360172056",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-10-01T21:22:35.257Z"),
            "user_name": "Santina Abbott",
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

Create a project

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
            "description": "Valetudo aggredior accommodo curiositas vox.",
            "has_children": False,
            "has_tasks": False,
            "id": "6a91fca9-3ebb-457a-b771-6dc9b3ee39a9",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "07d58012-a2dd-438b-9e78-0566e9b813d2",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "e27e9aed-7472-49f4-b4ec-c5d7b061bf32",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-11T03:22:41.816Z"),
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

Create a task

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
            "completed_at": parse_datetime("2022-04-04T23:29:24.840Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-05-19T18:14:26.718Z"),
            "end_at": parse_datetime("2022-10-27T05:47:41.129Z"),
            "has_children": True,
            "id": "88dd2a4a-d3f8-4180-842a-d993b46ff1d1",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-30T07:39:35.649Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-15T01:58:23.845Z"),
            "url": "https://dismal-silk.net/",
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

Retrieve a task

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

Retrieve a change

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

Retrieve a comment

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

Retrieve a project

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

Retrieve a task

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

List all tasks

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

List all changes

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

List all comments

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

List all projects

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

List all tasks

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

Update a task

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
            "completed_at": parse_datetime("2025-09-27T01:15:18.123Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "1ceef6b8-57dc-4a36-aa3d-eb6a14f6888c",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-18T09:06:31.241Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-02-24T07:12:18.313Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
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

Update a comment

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
            "has_children": True,
            "id": "3072d279-3576-4350-9bf0-3ba0692e276e",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-10-01T21:22:35.259Z"),
            "user_name": "Santina Abbott",
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

Update a project

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
            "description": "Valetudo aggredior accommodo curiositas vox.",
            "has_children": False,
            "has_tasks": False,
            "id": "2d11dd26-a2db-4cdf-aaca-fc472ec0502a",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "ade7e799-e768-409c-810d-272cb2ee95f0",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "c18b84b0-40e7-4d98-a779-89a80c636f55",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-11T03:22:41.818Z"),
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

Update a task

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
            "completed_at": parse_datetime("2022-04-04T23:29:24.851Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-05-19T18:14:26.743Z"),
            "end_at": parse_datetime("2022-10-27T05:47:41.141Z"),
            "has_children": True,
            "id": "190d45ec-165d-44b5-a9da-8395ad0c0975",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-30T07:39:35.659Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-15T01:58:23.847Z"),
            "url": "https://dismal-silk.net/",
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

Remove a task

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

Remove a comment

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

Remove a project

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

Remove a task

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

Update a task

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
            "completed_at": parse_datetime("2025-09-27T01:15:18.123Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "1ceef6b8-57dc-4a36-aa3d-eb6a14f6888c",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-18T09:06:31.241Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-02-24T07:12:18.313Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
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

Update a comment

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
            "has_children": True,
            "id": "3072d279-3576-4350-9bf0-3ba0692e276e",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-10-01T21:22:35.259Z"),
            "user_name": "Santina Abbott",
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

Update a project

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
            "description": "Valetudo aggredior accommodo curiositas vox.",
            "has_children": False,
            "has_tasks": False,
            "id": "2d11dd26-a2db-4cdf-aaca-fc472ec0502a",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "ade7e799-e768-409c-810d-272cb2ee95f0",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "c18b84b0-40e7-4d98-a779-89a80c636f55",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-11T03:22:41.818Z"),
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

Update a task

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
            "completed_at": parse_datetime("2022-04-04T23:29:24.851Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-05-19T18:14:26.743Z"),
            "end_at": parse_datetime("2022-10-27T05:47:41.141Z"),
            "has_children": True,
            "id": "190d45ec-165d-44b5-a9da-8395ad0c0975",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-30T07:39:35.659Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-15T01:58:23.847Z"),
            "url": "https://dismal-silk.net/",
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