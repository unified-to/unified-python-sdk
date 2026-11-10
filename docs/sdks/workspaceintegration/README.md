# Workspaceintegration

## Overview

### Available Operations

* [create_unified_workspaceintegration](#create_unified_workspaceintegration) - Create workspace integration
* [get_unified_workspaceintegration](#get_unified_workspaceintegration) - Retrieve workspace integration
* [list_unified_workspaceintegrations](#list_unified_workspaceintegrations) - List workspace integrations
* [patch_unified_workspaceintegration](#patch_unified_workspaceintegration) - Update workspace integration
* [remove_unified_workspaceintegration](#remove_unified_workspaceintegration) - Remove workspace integration
* [update_unified_workspaceintegration](#update_unified_workspaceintegration) - Update workspace integration

## create_unified_workspaceintegration

Create workspace integration

### Example Usage

<!-- UsageSnippet language="python" operationID="createUnifiedWorkspaceintegration" method="post" path="/unified/workspaceintegration" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.create_unified_workspaceintegration(request={
        "integration_type": "<value>",
        "is_active": True,
    })

    assert res.workspace_integration is not None

    # Handle response
    print(res.workspace_integration)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.WorkspaceIntegration](../../models/shared/workspaceintegration.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.CreateUnifiedWorkspaceintegrationResponse](../../models/operations/createunifiedworkspaceintegrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_workspaceintegration

Retrieve workspace integration

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedWorkspaceintegration" method="get" path="/unified/workspaceintegration/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.get_unified_workspaceintegration(request={
        "id": "<id>",
    })

    assert res.workspace_integration is not None

    # Handle response
    print(res.workspace_integration)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetUnifiedWorkspaceintegrationRequest](../../models/operations/getunifiedworkspaceintegrationrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.GetUnifiedWorkspaceintegrationResponse](../../models/operations/getunifiedworkspaceintegrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_workspaceintegrations

List workspace integrations

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedWorkspaceintegrations" method="get" path="/unified/workspaceintegration" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.list_unified_workspaceintegrations(request={})

    assert res.workspace_integrations is not None

    # Handle response
    print(res.workspace_integrations)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListUnifiedWorkspaceintegrationsRequest](../../models/operations/listunifiedworkspaceintegrationsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.ListUnifiedWorkspaceintegrationsResponse](../../models/operations/listunifiedworkspaceintegrationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_unified_workspaceintegration

Update workspace integration

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUnifiedWorkspaceintegration" method="patch" path="/unified/workspaceintegration/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.patch_unified_workspaceintegration(request={
        "workspace_integration_patch": {},
        "id": "<id>",
    })

    assert res.workspace_integration is not None

    # Handle response
    print(res.workspace_integration)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchUnifiedWorkspaceintegrationRequest](../../models/operations/patchunifiedworkspaceintegrationrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.PatchUnifiedWorkspaceintegrationResponse](../../models/operations/patchunifiedworkspaceintegrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_unified_workspaceintegration

Remove workspace integration

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUnifiedWorkspaceintegration" method="delete" path="/unified/workspaceintegration/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.remove_unified_workspaceintegration(request={
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.RemoveUnifiedWorkspaceintegrationRequest](../../models/operations/removeunifiedworkspaceintegrationrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.RemoveUnifiedWorkspaceintegrationResponse](../../models/operations/removeunifiedworkspaceintegrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_unified_workspaceintegration

Update workspace integration

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUnifiedWorkspaceintegration" method="put" path="/unified/workspaceintegration/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.workspaceintegration.update_unified_workspaceintegration(request={
        "workspace_integration": {
            "integration_type": "<value>",
            "is_active": False,
        },
        "id": "<id>",
    })

    assert res.workspace_integration is not None

    # Handle response
    print(res.workspace_integration)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.UpdateUnifiedWorkspaceintegrationRequest](../../models/operations/updateunifiedworkspaceintegrationrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.UpdateUnifiedWorkspaceintegrationResponse](../../models/operations/updateunifiedworkspaceintegrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |