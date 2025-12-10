# Auth

## Overview

### Available Operations

* [get_unified_integration_auth](#get_unified_integration_auth) - Authorize new connection
* [get_unified_integration_login](#get_unified_integration_login) - Sign in a user

## get_unified_integration_auth

Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedIntegrationAuth" method="get" path="/unified/integration/auth/{workspace_id}/{integration_type}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.auth.get_unified_integration_auth(request={
        "integration_type": "<value>",
        "workspace_id": "<id>",
    })

    assert res.res is not None

    # Handle response
    print(res.res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetUnifiedIntegrationAuthRequest](../../models/operations/getunifiedintegrationauthrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetUnifiedIntegrationAuthResponse](../../models/operations/getunifiedintegrationauthresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_unified_integration_login

Returns an authentication URL for the specified integration.  Once a successful authentication occurs, the name and email are returned inside a jwt parameter, which is a JSON web token that is base-64 encoded.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUnifiedIntegrationLogin" method="get" path="/unified/integration/login/{workspace_id}/{integration_type}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.auth.get_unified_integration_login(request={
        "integration_type": "<value>",
        "workspace_id": "<id>",
    })

    assert res.res is not None

    # Handle response
    print(res.res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetUnifiedIntegrationLoginRequest](../../models/operations/getunifiedintegrationloginrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetUnifiedIntegrationLoginResponse](../../models/operations/getunifiedintegrationloginresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |