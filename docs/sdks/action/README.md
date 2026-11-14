# Action

## Overview

### Available Operations

* [create_qms_action](#create_qms_action) - Create an action
* [get_qms_action](#get_qms_action) - Retrieve an action
* [list_qms_actions](#list_qms_actions) - List all actions
* [patch_qms_action](#patch_qms_action) - Update an action
* [update_qms_action](#update_qms_action) - Update an action

## create_qms_action

Creates a QmsAction. Provide the unified QmsAction fields in the request body; they are mapped to the provider's API. Returns the created QmsAction.

### Example Usage

<!-- UsageSnippet language="python" operationID="createQmsAction" method="post" path="/qms/{connection_id}/action" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.action.create_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "3fc477f2-2e9e-4b41-baf1-07b71958e121",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.971Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateQmsActionRequest](../../models/operations/createqmsactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateQmsActionResponse](../../models/operations/createqmsactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_qms_action

Retrieves a single QmsAction by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getQmsAction" method="get" path="/qms/{connection_id}/action/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.action.get_qms_action(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetQmsActionRequest](../../models/operations/getqmsactionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetQmsActionResponse](../../models/operations/getqmsactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_qms_actions

Returns a list of QmsActions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listQmsActions" method="get" path="/qms/{connection_id}/action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.action.list_qms_actions(request={
        "connection_id": "<id>",
    })

    assert res.qms_actions is not None

    # Handle response
    print(res.qms_actions)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListQmsActionsRequest](../../models/operations/listqmsactionsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListQmsActionsResponse](../../models/operations/listqmsactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_qms_action

Updates the QmsAction identified by `id`. Provide the unified QmsAction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchQmsAction" method="patch" path="/qms/{connection_id}/action/{id}" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.action.patch_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "5836bb23-031c-4200-bd54-c19e0895874a",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.987Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchQmsActionRequest](../../models/operations/patchqmsactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchQmsActionResponse](../../models/operations/patchqmsactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_qms_action

Updates the QmsAction identified by `id`. Provide the unified QmsAction fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateQmsAction" method="put" path="/qms/{connection_id}/action/{id}" example="qms_action" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.action.update_qms_action(request={
        "qms_action": {
            "affected_items": [],
            "created_at": parse_datetime("2022-03-07T03:01:29.933Z"),
            "description": "Auditor sunt tego apparatus aegre ascisco.",
            "due_at": parse_datetime("2022-04-04T03:42:01.290Z"),
            "file_ids": [],
            "id": "5836bb23-031c-4200-bd54-c19e0895874a",
            "issue_ids": [],
            "lifecycle_state": "Cancelled",
            "metadata": [],
            "name": "Add inspection step",
            "number": "CAPA-6268",
            "original_type": "Corrective Action",
            "priority": "Medium",
            "root_cause": "Worn tooling",
            "status": shared.QmsActionStatus.CANCELLED,
            "type": shared.QmsActionType.CORRECTIVE,
            "updated_at": parse_datetime("2025-02-17T01:04:17.987Z"),
            "url": "https://incomplete-conservation.org",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.qms_action is not None

    # Handle response
    print(res.qms_action)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateQmsActionRequest](../../models/operations/updateqmsactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateQmsActionResponse](../../models/operations/updateqmsactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |