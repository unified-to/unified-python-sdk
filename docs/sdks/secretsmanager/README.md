# Secretsmanager

## Overview

### Available Operations

* [create_unified_secretsmanager](#create_unified_secretsmanager) - Create secrets manager
* [get_unified_secretsmanager](#get_unified_secretsmanager) - Retrieve secrets manager
* [list_unified_secretsmanager_instructions](#list_unified_secretsmanager_instructions) - List secrets manager setup instructions
* [list_unified_secretsmanager_secrets](#list_unified_secretsmanager_secrets) - List secrets in a secrets manager
* [list_unified_secretsmanagers](#list_unified_secretsmanagers) - List secrets managers
* [remove_unified_secretsmanager](#remove_unified_secretsmanager) - Remove secrets manager

## create_unified_secretsmanager

Create secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="createUnifiedSecretsmanager" method="post" path="/unified/secretsmanager" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.create_unified_secretsmanager(request={
        "auth": {
            "key": "<value>",
            "key1": "<value>",
        },
        "name": "<value>",
        "type": shared.SecretsManagerType.AKEYLESS,
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

**[operations.CreateUnifiedSecretsmanagerResponse](../../models/operations/createunifiedsecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_secretsmanager

Retrieve secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedSecretsmanager" method="get" path="/unified/secretsmanager/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.get_unified_secretsmanager(request={
        "id": "<id>",
    })

    assert res.secrets_manager is not None

    # Handle response
    print(res.secrets_manager)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetUnifiedSecretsmanagerRequest](../../models/operations/getunifiedsecretsmanagerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetUnifiedSecretsmanagerResponse](../../models/operations/getunifiedsecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_secretsmanager_instructions

List secrets manager setup instructions

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedSecretsmanagerInstructions" method="get" path="/unified/secretsmanager/instructions" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.list_unified_secretsmanager_instructions()

    assert res.secrets_manager_instructions_list is not None

    # Handle response
    print(res.secrets_manager_instructions_list)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListUnifiedSecretsmanagerInstructionsResponse](../../models/operations/listunifiedsecretsmanagerinstructionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_secretsmanager_secrets

List secrets in a secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedSecretsmanagerSecrets" method="get" path="/unified/secretsmanager/secrets" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.list_unified_secretsmanager_secrets(request={
        "secretsmanager_id": "<id>",
    })

    assert res.secrets_manager_secrets is not None

    # Handle response
    print(res.secrets_manager_secrets)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListUnifiedSecretsmanagerSecretsRequest](../../models/operations/listunifiedsecretsmanagersecretsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.ListUnifiedSecretsmanagerSecretsResponse](../../models/operations/listunifiedsecretsmanagersecretsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_secretsmanagers

List secrets managers

### Example Usage

<!-- UsageSnippet language="python" operationID="listUnifiedSecretsmanagers" method="get" path="/unified/secretsmanager" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.list_unified_secretsmanagers(request={})

    assert res.secrets_managers is not None

    # Handle response
    print(res.secrets_managers)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListUnifiedSecretsmanagersRequest](../../models/operations/listunifiedsecretsmanagersrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListUnifiedSecretsmanagersResponse](../../models/operations/listunifiedsecretsmanagersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_unified_secretsmanager

Remove secrets manager

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUnifiedSecretsmanager" method="delete" path="/unified/secretsmanager/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.secretsmanager.remove_unified_secretsmanager(request={
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveUnifiedSecretsmanagerRequest](../../models/operations/removeunifiedsecretsmanagerrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveUnifiedSecretsmanagerResponse](../../models/operations/removeunifiedsecretsmanagerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |