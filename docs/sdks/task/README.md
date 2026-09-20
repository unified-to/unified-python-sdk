# Task

## Overview

### Available Operations

* [create_task_comment](#create_task_comment) - Create a comment
* [create_task_project](#create_task_project) - Create a project
* [create_task_task](#create_task_task) - Create a task
* [get_task_change](#get_task_change) - Retrieve a change
* [get_task_comment](#get_task_comment) - Retrieve a comment
* [get_task_project](#get_task_project) - Retrieve a project
* [get_task_task](#get_task_task) - Retrieve a task
* [list_task_changes](#list_task_changes) - List all changes
* [list_task_comments](#list_task_comments) - List all comments
* [list_task_projects](#list_task_projects) - List all projects
* [list_task_tasks](#list_task_tasks) - List all tasks
* [patch_task_comment](#patch_task_comment) - Update a comment
* [patch_task_project](#patch_task_project) - Update a project
* [patch_task_task](#patch_task_task) - Update a task
* [remove_task_comment](#remove_task_comment) - Remove a comment
* [remove_task_project](#remove_task_project) - Remove a project
* [remove_task_task](#remove_task_task) - Remove a task
* [update_task_comment](#update_task_comment) - Update a comment
* [update_task_project](#update_task_project) - Update a project
* [update_task_task](#update_task_task) - Update a task

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
            "id": "dd91651e-99c7-4898-be5e-217b704012ac",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-09-24T10:05:30.314Z"),
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
            "id": "1812b40f-b8eb-4fa7-8e68-4c615664f0b3",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "1d5b3dea-f08a-41fb-be76-5267dc7f456a",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "652359a0-c809-461d-8669-27885845e4a5",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-08T17:43:47.069Z"),
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
            "completed_at": parse_datetime("2022-03-25T00:51:34.854Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-04-24T14:34:53.210Z"),
            "end_at": parse_datetime("2022-10-14T08:40:35.013Z"),
            "has_children": True,
            "id": "4af7da43-e710-49ed-9a66-871d725e4588",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-19T23:40:24.353Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-13T12:39:59.471Z"),
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
            "id": "ce156dcf-89dc-474c-b3cd-93df5762f354",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-09-24T10:05:30.315Z"),
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
            "id": "c81cf2e7-d7ae-4cd5-96c6-010f301f25b6",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "500001c1-e9e6-4bff-b28e-ff7e87e827ab",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "0d19d358-d37a-48e6-b3b2-0a48f98ccbdf",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-08T17:43:47.070Z"),
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
            "completed_at": parse_datetime("2022-03-25T00:51:34.860Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-04-24T14:34:53.223Z"),
            "end_at": parse_datetime("2022-10-14T08:40:35.020Z"),
            "has_children": True,
            "id": "ce280840-19a5-4ddf-81f3-1c423a918c05",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-19T23:40:24.358Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-13T12:39:59.472Z"),
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
            "id": "ce156dcf-89dc-474c-b3cd-93df5762f354",
            "text": "Colo ulciscor sublime tabernus.",
            "updated_at": parse_datetime("2021-09-24T10:05:30.315Z"),
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
            "id": "c81cf2e7-d7ae-4cd5-96c6-010f301f25b6",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "500001c1-e9e6-4bff-b28e-ff7e87e827ab",
                    "namespace": "custom",
                    "slug": "decens",
                    "value": "uterque",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.TaskMetadataFormat.TEXT,
                    "id": "0d19d358-d37a-48e6-b3b2-0a48f98ccbdf",
                    "namespace": "custom",
                    "slug": "benevolentia",
                    "value": "pariatur",
                },
            ],
            "name": "Garden",
            "updated_at": parse_datetime("2023-10-08T17:43:47.070Z"),
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
            "completed_at": parse_datetime("2022-03-25T00:51:34.860Z"),
            "created_at": parse_datetime("2019-01-31T08:34:55.626Z"),
            "due_at": parse_datetime("2026-04-24T14:34:53.223Z"),
            "end_at": parse_datetime("2022-10-14T08:40:35.020Z"),
            "has_children": True,
            "id": "ce280840-19a5-4ddf-81f3-1c423a918c05",
            "metadata": [],
            "name": "Direct Markets Architect",
            "notes": "Calcar vilicus audacia ut cultura argentum ventosus. Talis neque thymbra titulus absconditus peccatus crustulum tollo. Volva vacuus eos cedo spero. Utpote coadunatio denuncio adopto autus sono atrocitas vulnero.",
            "priority": "LOW",
            "progress": 2.0,
            "start_at": parse_datetime("2022-01-19T23:40:24.358Z"),
            "status": shared.TaskTaskStatus.IN_PROGRESS,
            "story_points": 0.0,
            "tags": [
                "concido",
                "rerum",
            ],
            "time_spent": 957.0,
            "time_spent_unit": "SECONDS",
            "type": "tubineus",
            "updated_at": parse_datetime("2019-07-13T12:39:59.472Z"),
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