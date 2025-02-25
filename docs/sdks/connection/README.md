# Connection
(*connection*)

## Overview

### Available Operations

* [create_unified_connection](#create_unified_connection) - Create connection
* [get_unified_connection](#get_unified_connection) - Retrieve connection
* [list_unified_connections](#list_unified_connections) - List all connections
* [patch_unified_connection](#patch_unified_connection) - Update connection
* [remove_unified_connection](#remove_unified_connection) - Remove connection
* [update_unified_connection](#update_unified_connection) - Update connection

## create_unified_connection

Used only to import existing customer credentials; use "Create connection indirectly" instead

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.create_unified_connection(request={
        "categories": [
            shared.PropertyConnectionCategories.ACCOUNTING,
            shared.PropertyConnectionCategories.MARTECH,
            shared.PropertyConnectionCategories.MARTECH,
        ],
        "integration_type": "<value>",
        "permissions": [
            shared.PropertyConnectionPermissions.LMS_COURSE_READ,
            shared.PropertyConnectionPermissions.SCIM_USERS_READ,
        ],
        "environment": "Production",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Connection](../../models/shared/connection.md)              | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateUnifiedConnectionResponse](../../models/operations/createunifiedconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_connection

Retrieve connection

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.get_unified_connection(request={
        "id": "<id>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedConnectionRequest](../../models/operations/getunifiedconnectionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetUnifiedConnectionResponse](../../models/operations/getunifiedconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_unified_connections

List all connections

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.list_unified_connections(request={})

    assert res.connections is not None

    # Handle response
    print(res.connections)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListUnifiedConnectionsRequest](../../models/operations/listunifiedconnectionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListUnifiedConnectionsResponse](../../models/operations/listunifiedconnectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_unified_connection

Update connection

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.patch_unified_connection(request={
        "connection": {
            "categories": [
                shared.PropertyConnectionCategories.METADATA,
                shared.PropertyConnectionCategories.CRM,
            ],
            "integration_type": "<value>",
            "permissions": [

            ],
            "environment": "Production",
        },
        "id": "<id>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchUnifiedConnectionRequest](../../models/operations/patchunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchUnifiedConnectionResponse](../../models/operations/patchunifiedconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_unified_connection

Remove connection

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.remove_unified_connection(request={
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveUnifiedConnectionRequest](../../models/operations/removeunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveUnifiedConnectionResponse](../../models/operations/removeunifiedconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_unified_connection

Update connection

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.connection.update_unified_connection(request={
        "connection": {
            "categories": [
                shared.PropertyConnectionCategories.METADATA,
                shared.PropertyConnectionCategories.ACCOUNTING,
                shared.PropertyConnectionCategories.METADATA,
            ],
            "integration_type": "<value>",
            "permissions": [

            ],
            "environment": "Production",
        },
        "id": "<id>",
    })

    assert res.connection is not None

    # Handle response
    print(res.connection)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateUnifiedConnectionRequest](../../models/operations/updateunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateUnifiedConnectionResponse](../../models/operations/updateunifiedconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |