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
    id='b75d2367-fe1a-40cc-8df7-9f0a396d90c3',
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
        operations.GetUnifiedConnectionCategories.AUTH,
    ],
    env='labore',
    external_xref='expedita',
    limit=4467.37,
    offset=7898.7,
    order='sunt',
    sort='enim',
    updated_gte=dateutil.parser.isoparse('2020-01-24T16:46:41.592Z'),
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
    id='bace188b-1c4e-4e2c-8c6c-e611feeb1c7c',
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
            access_token='distinctio',
            api_url='possimus',
            app_id='cum',
            authorize_url='suscipit',
            client_id='saepe',
            client_secret='earum',
            consumer_key='quod',
            consumer_secret='nihil',
            emails=[
                'quaerat',
            ],
            expires_in=2159.59,
            expiry_date=dateutil.parser.isoparse('2022-06-27T03:53:09.176Z'),
            key='rerum',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Harry Hammes IV',
            other_auth_info=[
                'esse',
            ],
            pem='magnam',
            refresh_token='odio',
            state='nulla',
            token='impedit',
            token_url='cupiditate',
        ),
        auth_aws_arn='illo',
        categories=[
            shared.PropertyConnectionCategories.AUTH,
        ],
        created_at=dateutil.parser.isoparse('2021-04-21T08:26:42.931Z'),
        environment='fugit',
        external_xref='maxime',
        id='af5dd672-3dc0-4f5a-a2f3-a6b700878756',
        integration_type='ab',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.CRM_USER_WRITE,
        ],
        updated_at=dateutil.parser.isoparse('2022-01-16T17:11:29.866Z'),
        workspace_id='corporis',
    ),
    id='a6c98b55-5540-480d-80bc-acc6cbd6b5f3',
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
        access_token='necessitatibus',
        api_url='maxime',
        app_id='cupiditate',
        authorize_url='voluptatem',
        client_id='provident',
        client_secret='adipisci',
        consumer_key='accusantium',
        consumer_secret='magnam',
        emails=[
            'repellat',
        ],
        expires_in=6076.31,
        expiry_date=dateutil.parser.isoparse('2022-07-29T13:50:17.340Z'),
        key='cum',
        meta=shared.PropertyPropertyConnectionAuthMeta(),
        name='Rufus Conroy',
        other_auth_info=[
            'sequi',
        ],
        pem='voluptatum',
        refresh_token='quasi',
        state='error',
        token='nobis',
        token_url='tempora',
    ),
    auth_aws_arn='voluptate',
    categories=[
        shared.PropertyConnectionCategories.ATS,
    ],
    created_at=dateutil.parser.isoparse('2022-11-28T03:21:08.707Z'),
    environment='voluptates',
    external_xref='possimus',
    id='20e56248-fff6-439a-910a-bdcab6267669',
    integration_type='laboriosam',
    is_paused=False,
    permissions=[
        shared.PropertyConnectionPermissions.ATS_CANDIDATE_WRITE,
    ],
    updated_at=dateutil.parser.isoparse('2022-01-26T21:22:49.757Z'),
    workspace_id='quisquam',
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
            access_token='eaque',
            api_url='alias',
            app_id='qui',
            authorize_url='consequuntur',
            client_id='vitae',
            client_secret='quidem',
            consumer_key='sequi',
            consumer_secret='amet',
            emails=[
                'exercitationem',
            ],
            expires_in=8470.18,
            expiry_date=dateutil.parser.isoparse('2021-10-18T19:31:06.005Z'),
            key='similique',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Garry Fahey',
            other_auth_info=[
                'asperiores',
            ],
            pem='temporibus',
            refresh_token='id',
            state='atque',
            token='quibusdam',
            token_url='sit',
        ),
        auth_aws_arn='quo',
        categories=[
            shared.PropertyConnectionCategories.ATS,
        ],
        created_at=dateutil.parser.isoparse('2022-05-30T05:35:32.331Z'),
        environment='vero',
        external_xref='earum',
        id='03004978-a61f-4a1c-b206-88f77c1ffc71',
        integration_type='facere',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.HRIS_GROUP_READ,
        ],
        updated_at=dateutil.parser.isoparse('2022-11-13T09:13:55.156Z'),
        workspace_id='ex',
    ),
    id='3f2a3c80-a97f-4f33-8cdd-f857a9e61876',
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

