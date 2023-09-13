# unified

### Available Operations

* [delete_unified_connection_id](#delete_unified_connection_id) - Remove connection
* [delete_unified_user](#delete_unified_user) - Delete your user object
* [delete_unified_webhook_id](#delete_unified_webhook_id) - Remove webhook subscription
* [get_unified_apicall](#get_unified_apicall) - Returns API Calls
* [get_unified_apicall_id](#get_unified_apicall_id) - Retrieve specific API Call by its ID
* [get_unified_connection](#get_unified_connection) - List all connections
* [get_unified_connection_id](#get_unified_connection_id) - Retrieve connection
* [get_unified_integration](#get_unified_integration) - Returns all integrations
* [get_unified_integration_auth_workspace_id_integration_type](#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_integration_type](#get_unified_integration_integration_type) - Retrieve an integration
* [get_unified_integration_workspace_workspace_id](#get_unified_integration_workspace_workspace_id) - Returns all activated integrations in a workspace
* [get_unified_user](#get_unified_user) - Retrieve your user object
* [get_unified_user_token](#get_unified_user_token) - Retrieve your user token
* [get_unified_webhook](#get_unified_webhook) - Returns all registered webhooks
* [get_unified_webhook_id](#get_unified_webhook_id) - Retrieve webhook by its ID
* [patch_unified_connection_id](#patch_unified_connection_id) - Update connection
* [patch_unified_user](#patch_unified_user) - Updates your user object
* [post_unified_connection](#post_unified_connection) - Create connection
* [post_unified_webhook_connection_id_object](#post_unified_webhook_connection_id_object) - Create webhook subscription
* [put_unified_connection_id](#put_unified_connection_id) - Update connection
* [put_unified_user](#put_unified_user) - Updates your user object

## delete_unified_connection_id

Remove connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUnifiedConnectionIDRequest(
    id='d2a7c7d1-ea0e-479f-a9bb-e5f179f650b1',
)

res = s.unified.delete_unified_connection_id(req, operations.DeleteUnifiedConnectionIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteUnifiedConnectionIDRequest](../../models/operations/deleteunifiedconnectionidrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.DeleteUnifiedConnectionIDSecurity](../../models/operations/deleteunifiedconnectionidsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.DeleteUnifiedConnectionIDResponse](../../models/operations/deleteunifiedconnectionidresponse.md)**


## delete_unified_user

Delete your user object

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.unified.delete_unified_user(operations.DeleteUnifiedUserSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.DeleteUnifiedUserSecurity](../../models/operations/deleteunifiedusersecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.DeleteUnifiedUserResponse](../../models/operations/deleteunifieduserresponse.md)**


## delete_unified_webhook_id

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUnifiedWebhookIDRequest(
    id='e707e7e4-3967-413b-acce-072abd61918d',
)

res = s.unified.delete_unified_webhook_id(req, operations.DeleteUnifiedWebhookIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteUnifiedWebhookIDRequest](../../models/operations/deleteunifiedwebhookidrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.DeleteUnifiedWebhookIDSecurity](../../models/operations/deleteunifiedwebhookidsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.DeleteUnifiedWebhookIDResponse](../../models/operations/deleteunifiedwebhookidresponse.md)**


## get_unified_apicall

Returns API Calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallRequest(
    connection_id='magni',
    created_lte=dateutil.parser.parse('2022-05-24').date(),
    env='maxime',
    error=False,
    external_xref='vitae',
    integration_type='alias',
    limit=8070.07,
    offset=1150.28,
    order='blanditiis',
    sort='ipsam',
    updated_gte=dateutil.parser.parse('2022-08-08').date(),
)

res = s.unified.get_unified_apicall(req, operations.GetUnifiedApicallSecurity(
    jwt="",
))

if res.api_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedApicallSecurity](../../models/operations/getunifiedapicallsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**


## get_unified_apicall_id

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallIDRequest(
    id='fd78be26-2127-4262-8fa5-03962867e72b',
)

res = s.unified.get_unified_apicall_id(req, operations.GetUnifiedApicallIDSecurity(
    jwt="",
))

if res.api_call is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedApicallIDRequest](../../models/operations/getunifiedapicallidrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetUnifiedApicallIDSecurity](../../models/operations/getunifiedapicallidsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedApicallIDResponse](../../models/operations/getunifiedapicallidresponse.md)**


## get_unified_connection

List all connections

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedConnectionRequest(
    categories=[
        operations.GetUnifiedConnectionCategories.HRIS,
    ],
    env='laborum',
    external_xref='autem',
    limit=3273.73,
    offset=603.93,
    order='qui',
    sort='labore',
    updated_gte=dateutil.parser.parse('2022-11-05').date(),
)

res = s.unified.get_unified_connection(req, operations.GetUnifiedConnectionSecurity(
    jwt="",
))

if res.connections is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetUnifiedConnectionRequest](../../models/operations/getunifiedconnectionrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetUnifiedConnectionSecurity](../../models/operations/getunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetUnifiedConnectionResponse](../../models/operations/getunifiedconnectionresponse.md)**


## get_unified_connection_id

Retrieve connection

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedConnectionIDRequest(
    id='57f9bb6e-f72a-4508-b1d9-9b661a7def16',
)

res = s.unified.get_unified_connection_id(req, operations.GetUnifiedConnectionIDSecurity(
    jwt="",
))

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetUnifiedConnectionIDRequest](../../models/operations/getunifiedconnectionidrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.GetUnifiedConnectionIDSecurity](../../models/operations/getunifiedconnectionidsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetUnifiedConnectionIDResponse](../../models/operations/getunifiedconnectionidresponse.md)**


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
        operations.GetUnifiedIntegrationCategories.CRM,
    ],
    limit=7216.29,
    offset=4263.23,
    order='impedit',
    sort='optio',
    summary=False,
    updated_gte=dateutil.parser.parse('2022-09-12').date(),
)

res = s.unified.get_unified_integration(req, operations.GetUnifiedIntegrationSecurity(
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
    env='deleniti',
    external_xref='dolores',
    failure_redirect='dolores',
    integration_type='distinctio',
    lang='modi',
    redirect=False,
    scopes=[
        operations.GetUnifiedIntegrationAuthWorkspaceIDIntegrationTypeScopes.TICKETING_TICKET_READ,
    ],
    state='perspiciatis',
    subdomain='totam',
    success_redirect='ipsam',
    workspace_id='alias',
)

res = s.unified.get_unified_integration_auth_workspace_id_integration_type(req)

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
    integration_type='repudiandae',
)

res = s.unified.get_unified_integration_integration_type(req, operations.GetUnifiedIntegrationIntegrationTypeSecurity(
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
        operations.GetUnifiedIntegrationWorkspaceWorkspaceIDCategories.TICKETING,
    ],
    env='magni',
    summary=False,
    workspace_id='doloribus',
)

res = s.unified.get_unified_integration_workspace_workspace_id(req)

if res.integrations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetUnifiedIntegrationWorkspaceWorkspaceIDRequest](../../models/operations/getunifiedintegrationworkspaceworkspaceidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetUnifiedIntegrationWorkspaceWorkspaceIDResponse](../../models/operations/getunifiedintegrationworkspaceworkspaceidresponse.md)**


## get_unified_user

Retrieve your user object

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.unified.get_unified_user(operations.GetUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.GetUnifiedUserSecurity](../../models/operations/getunifiedusersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetUnifiedUserResponse](../../models/operations/getunifieduserresponse.md)**


## get_unified_user_token

Retrieve your user token

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.unified.get_unified_user_token(operations.GetUnifiedUserTokenSecurity(
    jwt="",
))

if res.get_unified_user_token_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetUnifiedUserTokenSecurity](../../models/operations/getunifiedusertokensecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedUserTokenResponse](../../models/operations/getunifiedusertokenresponse.md)**


## get_unified_webhook

Returns all registered webhooks

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookRequest(
    env='dolore',
    limit=6674.44,
    object='veritatis',
    offset=9332.28,
    order='excepturi',
    sort='eligendi',
    updated_gte=dateutil.parser.parse('2022-04-26').date(),
)

res = s.unified.get_unified_webhook(req, operations.GetUnifiedWebhookSecurity(
    jwt="",
))

if res.webhooks is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedWebhookSecurity](../../models/operations/getunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**


## get_unified_webhook_id

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookIDRequest(
    id='e55140e7-5726-4e00-bc2f-0294192518ce',
)

res = s.unified.get_unified_webhook_id(req, operations.GetUnifiedWebhookIDSecurity(
    jwt="",
))

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedWebhookIDRequest](../../models/operations/getunifiedwebhookidrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetUnifiedWebhookIDSecurity](../../models/operations/getunifiedwebhookidsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedWebhookIDResponse](../../models/operations/getunifiedwebhookidresponse.md)**


## patch_unified_connection_id

Update connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchUnifiedConnectionIDRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            access_token='accusamus',
            api_url='incidunt',
            app_id='dicta',
            authorize_url='quo',
            client_id='natus',
            client_secret='excepturi',
            consumer_key='natus',
            consumer_secret='hic',
            emails=[
                'ut',
            ],
            expires_in=3924.24,
            expiry_date=dateutil.parser.parse('2021-01-28').date(),
            key='eum',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Albert Schmidt MD',
            other_auth_info=[
                'adipisci',
            ],
            pem='a',
            refresh_token='ipsa',
            state='sed',
            token='sequi',
            token_url='minus',
        ),
        auth_aws_arn='suscipit',
        categories=[
            shared.PropertyConnectionCategories.AUTH,
        ],
        created_at=dateutil.parser.parse('2021-02-21').date(),
        environment='laboriosam',
        external_xref='harum',
        id='626012eb-a057-4988-8672-0c3103f1a40c',
        integration_type='doloremque',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.ATS_JOB_READ,
        ],
        updated_at=dateutil.parser.parse('2022-02-08').date(),
        workspace_id='quo',
    ),
    id='8688fd8e-c6fc-4031-a8f0-aaaeee004eba',
)

res = s.unified.patch_unified_connection_id(req, operations.PatchUnifiedConnectionIDSecurity(
    jwt="",
))

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchUnifiedConnectionIDRequest](../../models/operations/patchunifiedconnectionidrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.PatchUnifiedConnectionIDSecurity](../../models/operations/patchunifiedconnectionidsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.PatchUnifiedConnectionIDResponse](../../models/operations/patchunifiedconnectionidresponse.md)**


## patch_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.User(
    created_at=dateutil.parser.parse('2022-04-05').date(),
    email='Kavon12@hotmail.com',
    environment='harum',
    id='e509c508-7131-4f06-b0bc-e55a8687143c',
    meta=shared.PropertyUserMeta(),
    name='Mrs. Darryl Morar',
    updated_at=dateutil.parser.parse('2021-07-05').date(),
    workspace_id='sint',
    workspace_ids=[
        'odio',
    ],
)

res = s.unified.patch_unified_user(req, operations.PatchUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.User](../../models/shared/user.md)                                                 | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchUnifiedUserSecurity](../../models/operations/patchunifiedusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchUnifiedUserResponse](../../models/operations/patchunifieduserresponse.md)**


## post_unified_connection

Create connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.Connection(
    auth=shared.PropertyConnectionAuth(
        access_token='animi',
        api_url='exercitationem',
        app_id='repellendus',
        authorize_url='culpa',
        client_id='vel',
        client_secret='ex',
        consumer_key='non',
        consumer_secret='nobis',
        emails=[
            'in',
        ],
        expires_in=8765.83,
        expiry_date=dateutil.parser.parse('2022-07-06').date(),
        key='voluptatum',
        meta=shared.PropertyPropertyConnectionAuthMeta(),
        name='Neil Grimes',
        other_auth_info=[
            'culpa',
        ],
        pem='culpa',
        refresh_token='odit',
        state='laudantium',
        token='dolor',
        token_url='consequuntur',
    ),
    auth_aws_arn='libero',
    categories=[
        shared.PropertyConnectionCategories.MARTECH,
    ],
    created_at=dateutil.parser.parse('2022-09-06').date(),
    environment='totam',
    external_xref='laboriosam',
    id='2d2a31f9-b14a-4a6b-9ec7-f444232e9a5d',
    integration_type='eveniet',
    is_paused=False,
    permissions=[
        shared.PropertyConnectionPermissions.ATS_INTERVIEW_READ,
    ],
    updated_at=dateutil.parser.parse('2022-05-01').date(),
    workspace_id='cumque',
)

res = s.unified.post_unified_connection(req, operations.PostUnifiedConnectionSecurity(
    jwt="",
))

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.Connection](../../models/shared/connection.md)                                               | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PostUnifiedConnectionSecurity](../../models/operations/postunifiedconnectionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PostUnifiedConnectionResponse](../../models/operations/postunifiedconnectionresponse.md)**


## post_unified_webhook_connection_id_object

To maintain compatibility with the webhooks specification and Zapier webhooks, only the hook_url field is required in the payload when creating a Webhook.  When updated/new objects are found, the array of objects will be POSTed to the hook_url with the paramater hookId=<hookId>.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostUnifiedWebhookConnectionIDObjectRequest(
    webhook=shared.Webhook(
        checked_at=dateutil.parser.parse('2021-07-13').date(),
        connection_id='sed',
        created_at=dateutil.parser.parse('2021-12-08').date(),
        environment='cupiditate',
        events=[
            shared.PropertyWebhookEvents.CREATED,
        ],
        hook_url='voluptatum',
        id='1b58fe68-2e1c-42db-a23d-58e8247d122c',
        include_raw=False,
        integration_type='provident',
        interval=9868.06,
        object_type=shared.WebhookObjectType.CRM_LEAD,
        subscriptions=[
            'iusto',
        ],
        updated_at=dateutil.parser.parse('2022-07-12').date(),
        workspace_id='praesentium',
    ),
    connection_id='maiores',
    events=[
        operations.PostUnifiedWebhookConnectionIDObjectEvents.CREATED,
    ],
    object='dolores',
)

res = s.unified.post_unified_webhook_connection_id_object(req, operations.PostUnifiedWebhookConnectionIDObjectSecurity(
    jwt="",
))

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostUnifiedWebhookConnectionIDObjectRequest](../../models/operations/postunifiedwebhookconnectionidobjectrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.PostUnifiedWebhookConnectionIDObjectSecurity](../../models/operations/postunifiedwebhookconnectionidobjectsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.PostUnifiedWebhookConnectionIDObjectResponse](../../models/operations/postunifiedwebhookconnectionidobjectresponse.md)**


## put_unified_connection_id

Update connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutUnifiedConnectionIDRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            access_token='ducimus',
            api_url='occaecati',
            app_id='nostrum',
            authorize_url='atque',
            client_id='sequi',
            client_secret='commodi',
            consumer_key='quam',
            consumer_secret='dolor',
            emails=[
                'voluptas',
            ],
            expires_in=2226.69,
            expiry_date=dateutil.parser.parse('2020-12-30').date(),
            key='aut',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Velma Baumbach',
            other_auth_info=[
                'doloribus',
            ],
            pem='deserunt',
            refresh_token='officiis',
            state='nam',
            token='totam',
            token_url='ex',
        ),
        auth_aws_arn='labore',
        categories=[
            shared.PropertyConnectionCategories.CRM,
        ],
        created_at=dateutil.parser.parse('2022-07-24').date(),
        environment='adipisci',
        external_xref='voluptatem',
        id='d8f8b89d-9ca6-4075-a56f-c0ebe67155e2',
        integration_type='assumenda',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.ATS_SCORECARD_WRITE,
        ],
        updated_at=dateutil.parser.parse('2022-04-26').date(),
        workspace_id='ipsum',
    ),
    id='070d6e29-7f58-41fa-baaa-7d801088076f',
)

res = s.unified.put_unified_connection_id(req, operations.PutUnifiedConnectionIDSecurity(
    jwt="",
))

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PutUnifiedConnectionIDRequest](../../models/operations/putunifiedconnectionidrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PutUnifiedConnectionIDSecurity](../../models/operations/putunifiedconnectionidsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PutUnifiedConnectionIDResponse](../../models/operations/putunifiedconnectionidresponse.md)**


## put_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.User(
    created_at=dateutil.parser.parse('2021-12-05').date(),
    email='Gillian.Walsh62@hotmail.com',
    environment='laudantium',
    id='14088269-b6a7-40b0-9d82-f94fffbd1e1e',
    meta=shared.PropertyUserMeta(),
    name='Debra Stiedemann',
    updated_at=dateutil.parser.parse('2022-06-05').date(),
    workspace_id='doloremque',
    workspace_ids=[
        'sequi',
    ],
)

res = s.unified.put_unified_user(req, operations.PutUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.User](../../models/shared/user.md)                                             | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PutUnifiedUserSecurity](../../models/operations/putunifiedusersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PutUnifiedUserResponse](../../models/operations/putunifieduserresponse.md)**

