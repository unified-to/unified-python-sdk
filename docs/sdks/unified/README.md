# Unified
(*unified*)

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteUnifiedConnectionIDRequest(
    id='<ID>',
)

res = s.unified.delete_unified_connection_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteUnifiedConnectionIDRequest](../../models/operations/deleteunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DeleteUnifiedConnectionIDResponse](../../models/operations/deleteunifiedconnectionidresponse.md)**


## delete_unified_user

Delete your user object

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.unified.delete_unified_user()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.DeleteUnifiedUserResponse](../../models/operations/deleteunifieduserresponse.md)**


## delete_unified_webhook_id

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteUnifiedWebhookIDRequest(
    id='<ID>',
)

res = s.unified.delete_unified_webhook_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteUnifiedWebhookIDRequest](../../models/operations/deleteunifiedwebhookidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteUnifiedWebhookIDResponse](../../models/operations/deleteunifiedwebhookidresponse.md)**


## get_unified_apicall

Returns API Calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedApicallRequest(
    connection_id='delectus green Hybrid',
    created_lte=dateutil.parser.isoparse('2021-04-02T21:36:49.952Z'),
    env='Fantastic Iodine indexing',
    error=False,
    external_xref='Music',
    integration_type='Soft',
    limit=2390.64,
    offset=3757.34,
    order='mobile envisioneer',
    sort='North payment opposite',
    updated_gte=dateutil.parser.isoparse('2021-08-11T16:18:13.644Z'),
)

res = s.unified.get_unified_apicall(req)

if res.api_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**


## get_unified_apicall_id

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedApicallIDRequest(
    id='<ID>',
)

res = s.unified.get_unified_apicall_id(req)

if res.api_call is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetUnifiedApicallIDRequest](../../models/operations/getunifiedapicallidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetUnifiedApicallIDResponse](../../models/operations/getunifiedapicallidresponse.md)**


## get_unified_connection

List all connections

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedConnectionRequest(
    categories=[
        operations.GetUnifiedConnectionCategories.ATS,
    ],
    env='copying invoice coulomb',
    external_xref='Islands West',
    limit=7809.21,
    offset=2750.2,
    order='Volkswagen architect',
    sort='consequently synthesizing Technician',
    updated_gte=dateutil.parser.isoparse('2021-11-09T20:41:53.442Z'),
)

res = s.unified.get_unified_connection(req)

if res.connections is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedConnectionRequest](../../models/operations/getunifiedconnectionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetUnifiedConnectionResponse](../../models/operations/getunifiedconnectionresponse.md)**


## get_unified_connection_id

Retrieve connection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedConnectionIDRequest(
    id='<ID>',
)

res = s.unified.get_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUnifiedConnectionIDRequest](../../models/operations/getunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUnifiedConnectionIDResponse](../../models/operations/getunifiedconnectionidresponse.md)**


## get_unified_integration

Returns all integrations

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedIntegrationRequest(
    active=False,
    categories=[
        operations.GetUnifiedIntegrationCategories.ENRICH,
    ],
    limit=7363.95,
    offset=8214.4,
    order='Nelda Implemented',
    sort='cabinet',
    summary=False,
    updated_gte=dateutil.parser.isoparse('2022-02-05T00:16:37.455Z'),
)

res = s.unified.get_unified_integration(req)

if res.integrations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetUnifiedIntegrationRequest](../../models/operations/getunifiedintegrationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetUnifiedIntegrationResponse](../../models/operations/getunifiedintegrationresponse.md)**


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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedIntegrationIntegrationTypeRequest(
    integration_type='Pizza Electric',
)

res = s.unified.get_unified_integration_integration_type(req)

if res.integration is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetUnifiedIntegrationIntegrationTypeRequest](../../models/operations/getunifiedintegrationintegrationtyperequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetUnifiedIntegrationIntegrationTypeResponse](../../models/operations/getunifiedintegrationintegrationtyperesponse.md)**


## get_unified_integration_workspace_workspace_id

No authentication required as this is to be used by front-end interface

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedIntegrationWorkspaceWorkspaceIDRequest(
    active=False,
    categories=[
        operations.GetUnifiedIntegrationWorkspaceWorkspaceIDCategories.HRIS,
    ],
    env='North Southeast exercitationem',
    summary=False,
    workspace_id='Bronze Plastic',
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
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.unified.get_unified_user()

if res.user is not None:
    # handle response
```


### Response

**[operations.GetUnifiedUserResponse](../../models/operations/getunifieduserresponse.md)**


## get_unified_user_token

Retrieve your user token

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.unified.get_unified_user_token()

if res.get_unified_user_token_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.GetUnifiedUserTokenResponse](../../models/operations/getunifiedusertokenresponse.md)**


## get_unified_webhook

Returns all registered webhooks

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedWebhookRequest(
    env='Investor methodical Fitness',
    limit=8087.22,
    object='Franc past salmon',
    offset=5240.75,
    order='program',
    sort='below JSON',
    updated_gte=dateutil.parser.isoparse('2022-05-29T13:22:55.562Z'),
)

res = s.unified.get_unified_webhook(req)

if res.webhooks is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**


## get_unified_webhook_id

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedWebhookIDRequest(
    id='<ID>',
)

res = s.unified.get_unified_webhook_id(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetUnifiedWebhookIDRequest](../../models/operations/getunifiedwebhookidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetUnifiedWebhookIDResponse](../../models/operations/getunifiedwebhookidresponse.md)**


## patch_unified_connection_id

Update connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchUnifiedConnectionIDRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            access_token='Northwest Cupertino',
            api_url='Center Curium Electric',
            app_id='female fragrant',
            authorize_url='Electric Bicycle payment',
            client_id='transmitting North',
            client_secret='mole Gasoline morph',
            consumer_key='Keyboard Antimony primary',
            consumer_secret='yearly',
            emails=[
                'athwart',
            ],
            expires_in=3185.09,
            expiry_date=dateutil.parser.isoparse('2022-08-12T13:21:47.977Z'),
            key='<key>',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='inside Rupee',
            other_auth_info=[
                'Future',
            ],
            pem='guard Internal',
            refresh_token='Diesel',
            state='copy Cotton Bicycle',
            token='drive gold',
            token_url='now',
        ),
        auth_aws_arn='yum',
        categories=[
            shared.PropertyConnectionCategories.HRIS,
        ],
        created_at=dateutil.parser.isoparse('2021-06-18T22:02:30.822Z'),
        environment='Northwest Balanced',
        external_xref='boo',
        id='<ID>',
        integration_type='Soft',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.CRM_LEAD_READ,
        ],
        updated_at=dateutil.parser.isoparse('2022-07-27T15:43:44.767Z'),
        workspace_id='extend',
    ),
    id='<ID>',
)

res = s.unified.patch_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchUnifiedConnectionIDRequest](../../models/operations/patchunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PatchUnifiedConnectionIDResponse](../../models/operations/patchunifiedconnectionidresponse.md)**


## patch_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = shared.User(
    created_at=dateutil.parser.isoparse('2022-04-24T15:25:24.483Z'),
    email='Emmalee.Quitzon@yahoo.com',
    environment='Bicycle',
    id='<ID>',
    meta=shared.PropertyUserMeta(),
    name='vice compressing',
    updated_at=dateutil.parser.isoparse('2023-05-05T16:52:20.023Z'),
    workspace_id='Hybrid methodologies',
    workspace_ids=[
        'Potassium',
    ],
)

res = s.unified.patch_unified_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PatchUnifiedUserResponse](../../models/operations/patchunifieduserresponse.md)**


## post_unified_connection

Create connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = shared.Connection(
    auth=shared.PropertyConnectionAuth(
        access_token='asperiores indexing',
        api_url='plus pace global',
        app_id='And port',
        authorize_url='West whiteboard',
        client_id='Folk',
        client_secret='Northwest Modern',
        consumer_key='Southeast deposit',
        consumer_secret='Falls irritating up',
        emails=[
            'intuitive',
        ],
        expires_in=4121.5,
        expiry_date=dateutil.parser.isoparse('2021-01-21T03:25:42.786Z'),
        key='<key>',
        meta=shared.PropertyPropertyConnectionAuthMeta(),
        name='membership Classical schnitzel',
        other_auth_info=[
            'Convertible',
        ],
        pem='magenta Riel bolívar',
        refresh_token='Pula',
        state='white',
        token='Northwest',
        token_url='unbutton',
    ),
    auth_aws_arn='Investor circuit',
    categories=[
        shared.PropertyConnectionCategories.ATS,
    ],
    created_at=dateutil.parser.isoparse('2023-01-25T14:37:40.202Z'),
    environment='Hat watt',
    external_xref='Sausages tan',
    id='<ID>',
    integration_type='Principal Extended velit',
    is_paused=False,
    permissions=[
        shared.PropertyConnectionPermissions.CRM_FILE_WRITE,
    ],
    updated_at=dateutil.parser.isoparse('2021-09-22T05:13:05.778Z'),
    workspace_id='Auto',
)

res = s.unified.post_unified_connection(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.Connection](../../models/shared/connection.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.PostUnifiedConnectionResponse](../../models/operations/postunifiedconnectionresponse.md)**


## post_unified_webhook_connection_id_object

To maintain compatibility with the webhooks specification and Zapier webhooks, only the hook_url field is required in the payload when creating a Webhook.  When updated/new objects are found, the array of objects will be POSTed to the hook_url with the paramater hookId=<hookId>.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PostUnifiedWebhookConnectionIDObjectRequest(
    webhook=shared.Webhook(
        checked_at=dateutil.parser.isoparse('2021-02-25T07:12:08.980Z'),
        connection_id='deposit 1080p Passenger',
        created_at=dateutil.parser.isoparse('2023-02-21T14:58:56.193Z'),
        environment='Minnesota Soap',
        events=[
            shared.PropertyWebhookEvents.UPDATED,
        ],
        hook_url='Table female ken',
        id='<ID>',
        include_raw=False,
        integration_type='chocolate',
        interval=1710.16,
        object_type=shared.WebhookObjectType.ENRICH_COMPANY,
        subscriptions=[
            'female',
        ],
        updated_at=dateutil.parser.isoparse('2022-08-02T17:13:06.397Z'),
        workspace_id='hertz',
    ),
    connection_id='Borders',
    events=[
        operations.PostUnifiedWebhookConnectionIDObjectEvents.CREATED,
    ],
    object='scalable',
)

res = s.unified.post_unified_webhook_connection_id_object(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PostUnifiedWebhookConnectionIDObjectRequest](../../models/operations/postunifiedwebhookconnectionidobjectrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PostUnifiedWebhookConnectionIDObjectResponse](../../models/operations/postunifiedwebhookconnectionidobjectresponse.md)**


## put_unified_connection_id

Update connection

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutUnifiedConnectionIDRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            access_token='female Buckinghamshire',
            api_url='Web',
            app_id='pumpkin Account',
            authorize_url='dolorem Hybrid white',
            client_id='ohm',
            client_secret='Pennsylvania Executive',
            consumer_key='silver Account Accountability',
            consumer_secret='Mouse',
            emails=[
                'oh',
            ],
            expires_in=8946.31,
            expiry_date=dateutil.parser.isoparse('2022-01-29T12:35:08.478Z'),
            key='<key>',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='incidentally shrimp bypass',
            other_auth_info=[
                'invoice',
            ],
            pem='recent midst Northeast',
            refresh_token='Product',
            state='circuit precious',
            token='gee collaborative withdrawal',
            token_url='Platinum',
        ),
        auth_aws_arn='suddenly Fiat',
        categories=[
            shared.PropertyConnectionCategories.UC,
        ],
        created_at=dateutil.parser.isoparse('2022-09-20T19:51:21.025Z'),
        environment='redundant Southeast Camren',
        external_xref='firewall',
        id='<ID>',
        integration_type='Beauty',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.WEBHOOK,
        ],
        updated_at=dateutil.parser.isoparse('2023-12-30T14:20:47.994Z'),
        workspace_id='parse Peso Investment',
    ),
    id='<ID>',
)

res = s.unified.put_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutUnifiedConnectionIDRequest](../../models/operations/putunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PutUnifiedConnectionIDResponse](../../models/operations/putunifiedconnectionidresponse.md)**


## put_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = shared.User(
    created_at=dateutil.parser.isoparse('2023-07-31T04:46:29.769Z'),
    email='Selena59@yahoo.com',
    environment='Bedfordshire Lucia',
    id='<ID>',
    meta=shared.PropertyUserMeta(),
    name='Bicycle hacking South',
    updated_at=dateutil.parser.isoparse('2023-03-15T15:08:26.238Z'),
    workspace_id='Card defect',
    workspace_ids=[
        'repudiandae',
    ],
)

res = s.unified.put_unified_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PutUnifiedUserResponse](../../models/operations/putunifieduserresponse.md)**

