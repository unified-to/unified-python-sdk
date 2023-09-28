# Login
(*login*)

### Available Operations

* [get_unified_integration_login_workspace_id_integration_type](#get_unified_integration_login_workspace_id_integration_type) - Sign in a user

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

res = s.login.get_unified_integration_login_workspace_id_integration_type(req)

if res.get_unified_integration_login_workspace_id_integration_type_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeRequest](../../models/operations/getunifiedintegrationloginworkspaceidintegrationtyperequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |


### Response

**[operations.GetUnifiedIntegrationLoginWorkspaceIDIntegrationTypeResponse](../../models/operations/getunifiedintegrationloginworkspaceidintegrationtyperesponse.md)**

