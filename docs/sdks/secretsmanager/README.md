# Secretsmanager

## Overview

### Available Operations

* [create_unified_workspace_secretsmanager](#create_unified_workspace_secretsmanager) - Create secrets manager
* [get_unified_workspace_secretsmanager](#get_unified_workspace_secretsmanager) - Retrieve secrets manager
* [list_unified_workspace_secretsmanagers](#list_unified_workspace_secretsmanagers) - List secrets managers
* [remove_unified_workspace_secretsmanager](#remove_unified_workspace_secretsmanager) - Remove secrets manager

## create_unified_workspace_secretsmanager

Create secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="createUnifiedWorkspaceSecretsmanager" method="post" path="/unified/workspace/secretsmanager" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.create_unified_workspace_secretsmanager(request={
        "auth": {

        },
        "name": "<value>",
        "type": shared.SecretsManagerType.HASHICORP,
    })

    assert res.secrets_manager is not None

    # Handle response
    print(res.secrets_manager)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.SecretsManager](../../models/shared/secretsmanager.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateUnifiedWorkspaceSecretsmanagerResponse](../../models/operations/createunifiedworkspacesecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_workspace_secretsmanager

Retrieve secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedWorkspaceSecretsmanager" method="get" path="/unified/workspace/secretsmanager/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.get_unified_workspace_secretsmanager(request={
        "id": "<id>",
    })

    assert res.secrets_manager is not None

    # Handle response
    print(res.secrets_manager)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetUnifiedWorkspaceSecretsmanagerRequest](../../models/operations/getunifiedworkspacesecretsmanagerrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.GetUnifiedWorkspaceSecretsmanagerResponse](../../models/operations/getunifiedworkspacesecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_workspace_secretsmanagers

List secrets managers

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedWorkspaceSecretsmanagers" method="get" path="/unified/workspace/secretsmanager" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.list_unified_workspace_secretsmanagers(request={})

    assert res.secrets_managers is not None

    # Handle response
    print(res.secrets_managers)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.ListUnifiedWorkspaceSecretsmanagersRequest](../../models/operations/listunifiedworkspacesecretsmanagersrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.ListUnifiedWorkspaceSecretsmanagersResponse](../../models/operations/listunifiedworkspacesecretsmanagersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_unified_workspace_secretsmanager

Remove secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUnifiedWorkspaceSecretsmanager" method="delete" path="/unified/workspace/secretsmanager/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.remove_unified_workspace_secretsmanager(request={
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.RemoveUnifiedWorkspaceSecretsmanagerRequest](../../models/operations/removeunifiedworkspacesecretsmanagerrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.RemoveUnifiedWorkspaceSecretsmanagerResponse](../../models/operations/removeunifiedworkspacesecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |