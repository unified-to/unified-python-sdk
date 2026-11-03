# Goal

## Overview

### Available Operations

* [create_performance_goal](#create_performance_goal) - Create a goal
* [get_healthcare_goal](#get_healthcare_goal) - Retrieve a goal
* [get_performance_goal](#get_performance_goal) - Retrieve a goal
* [list_healthcare_goals](#list_healthcare_goals) - List all goals
* [list_performance_goals](#list_performance_goals) - List all goals
* [patch_performance_goal](#patch_performance_goal) - Update a goal
* [remove_performance_goal](#remove_performance_goal) - Remove a goal
* [update_performance_goal](#update_performance_goal) - Update a goal

## create_performance_goal

Creates a PerformanceGoal. Provide the unified PerformanceGoal fields in the request body; they are mapped to the provider's API. Returns the created PerformanceGoal.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPerformanceGoal" method="post" path="/performance/{connection_id}/goal" example="performance_goal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.create_performance_goal(request={
        "performance_goal": {
            "created_at": parse_datetime("2020-01-09T20:43:07.380Z"),
            "description": "Suscipit suspendo vulnero vel facere valeo vallum degero.",
            "due_at": parse_datetime("2026-08-11T07:26:35.545Z"),
            "id": "76c81667-1ff1-460c-9196-7c195b068726",
            "metadata": [],
            "milestones": [
                {
                    "current_value": 10.0,
                    "due_at": parse_datetime("2026-06-16T03:06:35.438Z"),
                    "id": "c41c97c4-3b50-47fc-8b7d-c23540b63fd9",
                    "is_completed": True,
                    "name": "Team-oriented secondary matrix",
                    "target_value": 32.0,
                    "unit": "%",
                    "weight": 7.0,
                },
                {
                    "current_value": 0.0,
                    "due_at": parse_datetime("2026-08-21T01:30:37.661Z"),
                    "id": "c8b10dc5-cb6c-4be6-acf3-f22206f9cfca",
                    "is_completed": True,
                    "name": "Exclusive client-server conglomeration",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
                {
                    "current_value": 31.0,
                    "description": "Hic explicabo odit.",
                    "due_at": parse_datetime("2026-10-23T08:15:47.527Z"),
                    "id": "7feafe27-a142-4ed5-a596-6896ef3e3409",
                    "is_completed": True,
                    "name": "Synchronised immersive success",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
            ],
            "name": "Proactive national protocol",
            "progress": 3.0,
            "start_at": parse_datetime("2025-08-02T23:30:28.432Z"),
            "status": shared.PerformanceGoalStatus.CLOSED,
            "type": shared.PerformanceGoalSchemasType.COMPANY,
            "updated_at": parse_datetime("2022-09-18T04:25:03.405Z"),
            "weight": 5.0,
        },
        "connection_id": "<id>",
    })

    assert res.performance_goal is not None

    # Handle response
    print(res.performance_goal)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePerformanceGoalRequest](../../models/operations/createperformancegoalrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreatePerformanceGoalResponse](../../models/operations/createperformancegoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_healthcare_goal

Retrieves a single HealthcareGoal by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareGoal" method="get" path="/healthcare/{connection_id}/goal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.get_healthcare_goal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_goal is not None

    # Handle response
    print(res.healthcare_goal)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetHealthcareGoalRequest](../../models/operations/gethealthcaregoalrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetHealthcareGoalResponse](../../models/operations/gethealthcaregoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_performance_goal

Retrieves a single PerformanceGoal by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPerformanceGoal" method="get" path="/performance/{connection_id}/goal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.get_performance_goal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.performance_goal is not None

    # Handle response
    print(res.performance_goal)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetPerformanceGoalRequest](../../models/operations/getperformancegoalrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetPerformanceGoalResponse](../../models/operations/getperformancegoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_goals

Returns a list of HealthcareGoals. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareGoals" method="get" path="/healthcare/{connection_id}/goal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.list_healthcare_goals(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_goals is not None

    # Handle response
    print(res.healthcare_goals)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListHealthcareGoalsRequest](../../models/operations/listhealthcaregoalsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListHealthcareGoalsResponse](../../models/operations/listhealthcaregoalsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_performance_goals

Returns a list of PerformanceGoals. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPerformanceGoals" method="get" path="/performance/{connection_id}/goal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.list_performance_goals(request={
        "connection_id": "<id>",
    })

    assert res.performance_goals is not None

    # Handle response
    print(res.performance_goals)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListPerformanceGoalsRequest](../../models/operations/listperformancegoalsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListPerformanceGoalsResponse](../../models/operations/listperformancegoalsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_performance_goal

Updates the PerformanceGoal identified by `id`. Provide the unified PerformanceGoal fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPerformanceGoal" method="patch" path="/performance/{connection_id}/goal/{id}" example="performance_goal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.patch_performance_goal(request={
        "performance_goal": {
            "created_at": parse_datetime("2020-01-09T20:43:07.380Z"),
            "description": "Suscipit suspendo vulnero vel facere valeo vallum degero.",
            "due_at": parse_datetime("2026-08-11T07:26:35.571Z"),
            "id": "4dcaa805-9ce1-4407-952b-cfaf7bee84ec",
            "metadata": [],
            "milestones": [
                {
                    "current_value": 10.0,
                    "due_at": parse_datetime("2026-06-16T03:06:35.463Z"),
                    "id": "b0f6f2ae-3f19-41fa-858b-f3722c8de94e",
                    "is_completed": True,
                    "name": "Team-oriented secondary matrix",
                    "target_value": 32.0,
                    "unit": "%",
                    "weight": 7.0,
                },
                {
                    "current_value": 0.0,
                    "due_at": parse_datetime("2026-08-21T01:30:37.686Z"),
                    "id": "7eff3c8d-d7ae-4997-8fcb-f36c2f4e1fd4",
                    "is_completed": True,
                    "name": "Exclusive client-server conglomeration",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
                {
                    "current_value": 31.0,
                    "description": "Hic explicabo odit.",
                    "due_at": parse_datetime("2026-10-23T08:15:47.554Z"),
                    "id": "43a6223b-b079-4021-ab03-f3cc1195a67b",
                    "is_completed": True,
                    "name": "Synchronised immersive success",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
            ],
            "name": "Proactive national protocol",
            "progress": 3.0,
            "start_at": parse_datetime("2025-08-02T23:30:28.454Z"),
            "status": shared.PerformanceGoalStatus.CLOSED,
            "type": shared.PerformanceGoalSchemasType.COMPANY,
            "updated_at": parse_datetime("2022-09-18T04:25:03.416Z"),
            "weight": 5.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.performance_goal is not None

    # Handle response
    print(res.performance_goal)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchPerformanceGoalRequest](../../models/operations/patchperformancegoalrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchPerformanceGoalResponse](../../models/operations/patchperformancegoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_performance_goal

Deletes the PerformanceGoal identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePerformanceGoal" method="delete" path="/performance/{connection_id}/goal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.remove_performance_goal(request={
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
| `request`                                                                                          | [operations.RemovePerformanceGoalRequest](../../models/operations/removeperformancegoalrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemovePerformanceGoalResponse](../../models/operations/removeperformancegoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_performance_goal

Updates the PerformanceGoal identified by `id`. Provide the unified PerformanceGoal fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePerformanceGoal" method="put" path="/performance/{connection_id}/goal/{id}" example="performance_goal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.goal.update_performance_goal(request={
        "performance_goal": {
            "created_at": parse_datetime("2020-01-09T20:43:07.380Z"),
            "description": "Suscipit suspendo vulnero vel facere valeo vallum degero.",
            "due_at": parse_datetime("2026-08-11T07:26:35.571Z"),
            "id": "4dcaa805-9ce1-4407-952b-cfaf7bee84ec",
            "metadata": [],
            "milestones": [
                {
                    "current_value": 10.0,
                    "due_at": parse_datetime("2026-06-16T03:06:35.463Z"),
                    "id": "b0f6f2ae-3f19-41fa-858b-f3722c8de94e",
                    "is_completed": True,
                    "name": "Team-oriented secondary matrix",
                    "target_value": 32.0,
                    "unit": "%",
                    "weight": 7.0,
                },
                {
                    "current_value": 0.0,
                    "due_at": parse_datetime("2026-08-21T01:30:37.686Z"),
                    "id": "7eff3c8d-d7ae-4997-8fcb-f36c2f4e1fd4",
                    "is_completed": True,
                    "name": "Exclusive client-server conglomeration",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
                {
                    "current_value": 31.0,
                    "description": "Hic explicabo odit.",
                    "due_at": parse_datetime("2026-10-23T08:15:47.554Z"),
                    "id": "43a6223b-b079-4021-ab03-f3cc1195a67b",
                    "is_completed": True,
                    "name": "Synchronised immersive success",
                    "target_value": 32.0,
                    "weight": 5.0,
                },
            ],
            "name": "Proactive national protocol",
            "progress": 3.0,
            "start_at": parse_datetime("2025-08-02T23:30:28.454Z"),
            "status": shared.PerformanceGoalStatus.CLOSED,
            "type": shared.PerformanceGoalSchemasType.COMPANY,
            "updated_at": parse_datetime("2022-09-18T04:25:03.416Z"),
            "weight": 5.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.performance_goal is not None

    # Handle response
    print(res.performance_goal)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePerformanceGoalRequest](../../models/operations/updateperformancegoalrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdatePerformanceGoalResponse](../../models/operations/updateperformancegoalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |