# Auth
(*auth*)

### Available Operations

* [get_unified_integration_auth_workspace_id_integration_type](#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_login_workspace_id_integration_type](#get_unified_integration_login_workspace_id_integration_type) - Sign in a user

## get_unified_integration_auth_workspace_id_integration_type

Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest(
    env='Algerian',
    external_xref='Cambridgeshire Surinam',
    failure_redirect='Designer Drive',
    integration_type='program Home',
    lang='Plastic program',
    redirect=False,
    scopes=[
        operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeScopes.CRM_FILE_READ,
    ],
    state='Functionality Product',
    subdomain='payment Developer Dynamic',
    success_redirect='Northeast',
    workspace_id='duh empower Kwanza',
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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest(
    env='Rubber',
    failure_redirect='gold Cambridgeshire',
    integration_type='Plastic services pixel',
    redirect=False,
    state='Volkswagen Southwest',
    success_redirect='drive integrated Bicycle',
    workspace_id='Fantastic recontextualize Frozen',
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

