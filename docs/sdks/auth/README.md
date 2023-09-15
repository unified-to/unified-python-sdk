# Auth

### Available Operations

* [get_unified_integration_auth_workspace_id_integration_type](#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_login_workspace_id_integration_type](#get_unified_integration_login_workspace_id_integration_type) - Sign in a user

## get_unified_integration_auth_workspace_id_integration_type

Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest(
    env='beatae',
    external_xref='aliquid',
    failure_redirect='modi',
    integration_type='optio',
    lang='voluptatibus',
    redirect=False,
    scopes=[
        operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeScopes.MARTECH_MEMBER_READ,
    ],
    state='officia',
    subdomain='libero',
    success_redirect='totam',
    workspace_id='sequi',
)

res = s.auth.get_unified_integration_auth_workspace_id_integration_type(req)

if res.get_unified_integration_auth_workspace_id_integration_type_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest](../../models/operations/getunifiedintegrationauthworkspaceidintegrationtyperequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeResponse](../../models/operations/getunifiedintegrationauthworkspaceidintegrationtyperesponse.md)**


## get_unified_integration_login_workspace_id_integration_type

Returns an authentication URL for the specified integration.  Once a successful authentication occurs, the name and emails are returned.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest(
    env='aliquid',
    failure_redirect='ea',
    integration_type='impedit',
    redirect=False,
    state='ducimus',
    success_redirect='odit',
    workspace_id='velit',
)

res = s.auth.get_unified_integration_login_workspace_id_integration_type(req)

if res.get_unified_integration_login_workspace_id_integration_type_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest](../../models/operations/getunifiedintegrationloginworkspaceidintegrationtyperequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |


### Response

**[operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeResponse](../../models/operations/getunifiedintegrationloginworkspaceidintegrationtyperesponse.md)**

