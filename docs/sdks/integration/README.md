# integration

### Available Operations

* [get_unified_integration](#get_unified_integration) - Returns all integrations
* [get_unified_integration_auth_workspace_id_integration_type](#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_integration_type](#get_unified_integration_integration_type) - Retrieve an integration
* [get_unified_integration_workspace_workspace_id](#get_unified_integration_workspace_workspace_id) - Returns all activated integrations in a workspace

## get_unified_integration

Returns all integrations

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationRequest(
    active=False,
    categories=[
        operations.GetUnifiedIntegrationCategories.HRIS,
    ],
    limit=2394.27,
    offset=8487.85,
    order='ea',
    sort='veniam',
    summary=False,
    updated_gte=dateutil.parser.isoparse('2021-01-26T22:48:04.970Z'),
)

res = s.integration.get_unified_integration(req, operations.GetUnifiedIntegrationSecurity(
    jwt="",
))

if res.integrations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUnifiedIntegrationRequest](../../models/operations/getunifiedintegrationrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetUnifiedIntegrationSecurity](../../models/operations/getunifiedintegrationsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetUnifiedIntegrationResponse](../../models/operations/getunifiedintegrationresponse.md)**


## get_unified_integration_auth_workspace_id_integration_type

Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest(
    env='earum',
    external_xref='placeat',
    failure_redirect='saepe',
    integration_type='quod',
    lang='odit',
    redirect=False,
    scopes=[
        operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeScopes.HRIS_GROUP_WRITE,
    ],
    state='at',
    subdomain='ea',
    success_redirect='provident',
    workspace_id='inventore',
)

res = s.integration.get_unified_integration_auth_workspace_id_integration_type(req)

if res.get_unified_integration_auth_workspace_id_integration_type_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeRequest](../../models/operations/getunifiedintegrationauthworkspaceidintegrationtyperequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeResponse](../../models/operations/getunifiedintegrationauthworkspaceidintegrationtyperesponse.md)**


## get_unified_integration_integration_type

Retrieve an integration

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationIntegrationTypeRequest(
    integration_type='ea',
)

res = s.integration.get_unified_integration_integration_type(req, operations.GetUnifiedIntegrationIntegrationTypeSecurity(
    jwt="",
))

if res.integration is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetUnifiedIntegrationIntegrationTypeRequest](../../models/operations/getunifiedintegrationintegrationtyperequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.GetUnifiedIntegrationIntegrationTypeSecurity](../../models/operations/getunifiedintegrationintegrationtypesecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.GetUnifiedIntegrationIntegrationTypeResponse](../../models/operations/getunifiedintegrationintegrationtyperesponse.md)**


## get_unified_integration_workspace_workspace_id

No authentication required as this is to be used by front-end interface

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationWorkspaceWorkspaceIDRequest(
    active=False,
    categories=[
        operations.GetUnifiedIntegrationWorkspaceWorkspaceIDCategories.UC,
    ],
    env='quam',
    summary=False,
    workspace_id='delectus',
)

res = s.integration.get_unified_integration_workspace_workspace_id(req)

if res.integrations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetUnifiedIntegrationWorkspaceWorkspaceIDRequest](../../models/operations/getunifiedintegrationworkspaceworkspaceidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetUnifiedIntegrationWorkspaceWorkspaceIDResponse](../../models/operations/getunifiedintegrationworkspaceworkspaceidresponse.md)**

