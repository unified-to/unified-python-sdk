# Unified
(*unified*)

### Available Operations

* [create_unified_connection](#create_unified_connection) - Create connection
* [create_unified_webhook](#create_unified_webhook) - Create webhook subscription
* [get_unified_apicall](#get_unified_apicall) - Retrieve specific API Call by its ID
* [get_unified_connection](#get_unified_connection) - Retrieve connection
* [get_unified_integration_auth](#get_unified_integration_auth) - Create connection indirectly
* [get_unified_webhook](#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_apicalls](#list_unified_apicalls) - Returns API Calls
* [list_unified_connections](#list_unified_connections) - List all connections
* [list_unified_integration_workspaces](#list_unified_integration_workspaces) - Returns all activated integrations in a workspace
* [list_unified_integrations](#list_unified_integrations) - Returns all integrations
* [list_unified_issues](#list_unified_issues) - List support issues
* [list_unified_webhooks](#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_connection](#patch_unified_connection) - Update connection
* [patch_unified_webhook_trigger](#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_connection](#remove_unified_connection) - Remove connection
* [remove_unified_webhook](#remove_unified_webhook) - Remove webhook subscription
* [update_unified_connection](#update_unified_connection) - Update connection
* [update_unified_webhook_trigger](#update_unified_webhook_trigger) - Trigger webhook

## create_unified_connection

Create connection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.Connection(
    categories=[
        shared.PropertyConnectionCategories.COMMERCE,
    ],
    integration_type='<value>',
    permissions=[
        shared.PropertyConnectionPermissions.ATS_CANDIDATE_READ,
    ],
)

res = s.unified.create_unified_connection(req, operations.CreateUnifiedConnectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.Connection](../../models/shared/connection.md)                                                   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateUnifiedConnectionSecurity](../../models/operations/createunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateUnifiedConnectionResponse](../../models/operations/createunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_unified_webhook

The data payload received by your server is described at https://docs.unified.to/unified/overview. The `interval` field can be set as low as 1 minute for paid accounts, and 60 minutes for free accounts.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateUnifiedWebhookRequest()

res = s.unified.create_unified_webhook(req, operations.CreateUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateUnifiedWebhookRequest](../../models/operations/createunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.CreateUnifiedWebhookSecurity](../../models/operations/createunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.CreateUnifiedWebhookResponse](../../models/operations/createunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unified_apicall

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallRequest(
    id='<id>',
)

res = s.unified.get_unified_apicall(req, operations.GetUnifiedApicallSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.api_call is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedApicallSecurity](../../models/operations/getunifiedapicallsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unified_connection

Retrieve connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedConnectionRequest(
    id='<id>',
)

res = s.unified.get_unified_connection(req, operations.GetUnifiedConnectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetUnifiedConnectionRequest](../../models/operations/getunifiedconnectionrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetUnifiedConnectionSecurity](../../models/operations/getunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetUnifiedConnectionResponse](../../models/operations/getunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unified_integration_auth

Returns an authorization URL for the specified integration.  Once a successful authorization occurs, a new connection is created.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedIntegrationAuthRequest(
    integration_type='<value>',
    workspace_id='<value>',
)

res = s.unified.get_unified_integration_auth(req)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetUnifiedIntegrationAuthRequest](../../models/operations/getunifiedintegrationauthrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetUnifiedIntegrationAuthResponse](../../models/operations/getunifiedintegrationauthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unified_webhook

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookRequest(
    id='<id>',
)

res = s.unified.get_unified_webhook(req, operations.GetUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedWebhookSecurity](../../models/operations/getunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_apicalls

Returns API Calls

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedApicallsRequest()

res = s.unified.list_unified_apicalls(req, operations.ListUnifiedApicallsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.api_calls is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListUnifiedApicallsRequest](../../models/operations/listunifiedapicallsrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ListUnifiedApicallsSecurity](../../models/operations/listunifiedapicallssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ListUnifiedApicallsResponse](../../models/operations/listunifiedapicallsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_connections

List all connections

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedConnectionsRequest()

res = s.unified.list_unified_connections(req, operations.ListUnifiedConnectionsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.connections is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListUnifiedConnectionsRequest](../../models/operations/listunifiedconnectionsrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListUnifiedConnectionsSecurity](../../models/operations/listunifiedconnectionssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListUnifiedConnectionsResponse](../../models/operations/listunifiedconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_integration_workspaces

No authentication required as this is to be used by front-end interface

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedIntegrationWorkspacesRequest(
    workspace_id='<value>',
)

res = s.unified.list_unified_integration_workspaces(req)

if res.integrations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListUnifiedIntegrationWorkspacesRequest](../../models/operations/listunifiedintegrationworkspacesrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.ListUnifiedIntegrationWorkspacesResponse](../../models/operations/listunifiedintegrationworkspacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_integrations

Returns all integrations

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedIntegrationsRequest()

res = s.unified.list_unified_integrations(req, operations.ListUnifiedIntegrationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.integrations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListUnifiedIntegrationsRequest](../../models/operations/listunifiedintegrationsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ListUnifiedIntegrationsSecurity](../../models/operations/listunifiedintegrationssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ListUnifiedIntegrationsResponse](../../models/operations/listunifiedintegrationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_issues

List support issues

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedIssuesRequest()

res = s.unified.list_unified_issues(req, operations.ListUnifiedIssuesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.issues is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListUnifiedIssuesRequest](../../models/operations/listunifiedissuesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListUnifiedIssuesSecurity](../../models/operations/listunifiedissuessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListUnifiedIssuesResponse](../../models/operations/listunifiedissuesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_webhooks

Returns all registered webhooks

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedWebhooksRequest()

res = s.unified.list_unified_webhooks(req, operations.ListUnifiedWebhooksSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhooks is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListUnifiedWebhooksRequest](../../models/operations/listunifiedwebhooksrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ListUnifiedWebhooksSecurity](../../models/operations/listunifiedwebhookssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ListUnifiedWebhooksResponse](../../models/operations/listunifiedwebhooksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_unified_connection

Update connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchUnifiedConnectionRequest(
    id='<id>',
)

res = s.unified.patch_unified_connection(req, operations.PatchUnifiedConnectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchUnifiedConnectionRequest](../../models/operations/patchunifiedconnectionrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchUnifiedConnectionSecurity](../../models/operations/patchunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchUnifiedConnectionResponse](../../models/operations/patchunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchUnifiedWebhookTriggerRequest(
    id='<id>',
)

res = s.unified.patch_unified_webhook_trigger(req, operations.PatchUnifiedWebhookTriggerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchUnifiedWebhookTriggerRequest](../../models/operations/patchunifiedwebhooktriggerrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchUnifiedWebhookTriggerSecurity](../../models/operations/patchunifiedwebhooktriggersecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchUnifiedWebhookTriggerResponse](../../models/operations/patchunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_unified_connection

Remove connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveUnifiedConnectionRequest(
    id='<id>',
)

res = s.unified.remove_unified_connection(req, operations.RemoveUnifiedConnectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveUnifiedConnectionRequest](../../models/operations/removeunifiedconnectionrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveUnifiedConnectionSecurity](../../models/operations/removeunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveUnifiedConnectionResponse](../../models/operations/removeunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_unified_webhook

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveUnifiedWebhookRequest(
    id='<id>',
)

res = s.unified.remove_unified_webhook(req, operations.RemoveUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveUnifiedWebhookRequest](../../models/operations/removeunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.RemoveUnifiedWebhookSecurity](../../models/operations/removeunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.RemoveUnifiedWebhookResponse](../../models/operations/removeunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_unified_connection

Update connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateUnifiedConnectionRequest(
    id='<id>',
)

res = s.unified.update_unified_connection(req, operations.UpdateUnifiedConnectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateUnifiedConnectionRequest](../../models/operations/updateunifiedconnectionrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateUnifiedConnectionSecurity](../../models/operations/updateunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateUnifiedConnectionResponse](../../models/operations/updateunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateUnifiedWebhookTriggerRequest(
    id='<id>',
)

res = s.unified.update_unified_webhook_trigger(req, operations.UpdateUnifiedWebhookTriggerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateUnifiedWebhookTriggerRequest](../../models/operations/updateunifiedwebhooktriggerrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.UpdateUnifiedWebhookTriggerSecurity](../../models/operations/updateunifiedwebhooktriggersecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.UpdateUnifiedWebhookTriggerResponse](../../models/operations/updateunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
