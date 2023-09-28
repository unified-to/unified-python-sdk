# Connection
(*connection*)

### Available Operations

* [delete_unified_connection_id](#delete_unified_connection_id) - Remove connection
* [get_unified_connection](#get_unified_connection) - List all connections
* [get_unified_connection_id](#get_unified_connection_id) - Retrieve connection
* [patch_unified_connection_id](#patch_unified_connection_id) - Update connection
* [post_unified_connection](#post_unified_connection) - Create connection
* [put_unified_connection_id](#put_unified_connection_id) - Update connection

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

res = s.connection.delete_unified_connection_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteUnifiedConnectionIDRequest](../../models/operations/deleteunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DeleteUnifiedConnectionIDResponse](../../models/operations/deleteunifiedconnectionidresponse.md)**


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

res = s.connection.get_unified_connection(req)

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

res = s.connection.get_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUnifiedConnectionIDRequest](../../models/operations/getunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUnifiedConnectionIDResponse](../../models/operations/getunifiedconnectionidresponse.md)**


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

res = s.connection.patch_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchUnifiedConnectionIDRequest](../../models/operations/patchunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PatchUnifiedConnectionIDResponse](../../models/operations/patchunifiedconnectionidresponse.md)**


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

res = s.connection.post_unified_connection(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.Connection](../../models/shared/connection.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.PostUnifiedConnectionResponse](../../models/operations/postunifiedconnectionresponse.md)**


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

res = s.connection.put_unified_connection_id(req)

if res.connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutUnifiedConnectionIDRequest](../../models/operations/putunifiedconnectionidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PutUnifiedConnectionIDResponse](../../models/operations/putunifiedconnectionidresponse.md)**

