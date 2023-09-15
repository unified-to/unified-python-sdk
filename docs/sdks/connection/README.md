# Connection

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUnifiedConnectionIDRequest(
    id='bf60c321-f023-4b75-9236-7fe1a0cc8df7',
)

res = s.connection.delete_unified_connection_id(req, operations.DeleteUnifiedConnectionIDSecurity(
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
        operations.GetUnifiedConnectionCategories.ENRICH,
    ],
    env='sapiente',
    external_xref='aperiam',
    limit=6277.17,
    offset=1979.82,
    order='provident',
    sort='ex',
    updated_gte=dateutil.parser.isoparse('2021-03-13T14:26:08.551Z'),
)

res = s.connection.get_unified_connection(req, operations.GetUnifiedConnectionSecurity(
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
    id='0c364b7c-15df-4bac-a188-b1c4ee2c8c6c',
)

res = s.connection.get_unified_connection_id(req, operations.GetUnifiedConnectionIDSecurity(
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
            access_token='recusandae',
            api_url='ex',
            app_id='beatae',
            authorize_url='veritatis',
            client_id='maiores',
            client_secret='itaque',
            consumer_key='vero',
            consumer_secret='quidem',
            emails=[
                'illo',
            ],
            expires_in=7782.42,
            expiry_date=dateutil.parser.isoparse('2022-03-18T01:27:23.704Z'),
            key='distinctio',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Felipe Homenick',
            other_auth_info=[
                'quod',
            ],
            pem='nihil',
            refresh_token='quaerat',
            state='ipsum',
            token='ducimus',
            token_url='laudantium',
        ),
        auth_aws_arn='rerum',
        categories=[
            shared.PropertyConnectionCategories.ENRICH,
        ],
        created_at=dateutil.parser.isoparse('2022-09-06T09:53:00.602Z'),
        environment='sequi',
        external_xref='beatae',
        id='7747dc91-5ad2-4caf-9dd6-723dc0f5ae2f',
        integration_type='neque',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.TICKETING_CUSTOMER_READ,
        ],
        updated_at=dateutil.parser.isoparse('2022-04-24T15:26:26.341Z'),
        workspace_id='ducimus',
    ),
    id='00878756-143f-45a6-898b-55554080d40b',
)

res = s.connection.patch_unified_connection_id(req, operations.PatchUnifiedConnectionIDSecurity(
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
        access_token='nobis',
        api_url='similique',
        app_id='porro',
        authorize_url='impedit',
        client_id='nisi',
        client_secret='cumque',
        consumer_key='soluta',
        consumer_secret='fugiat',
        emails=[
            'laboriosam',
        ],
        expires_in=7203.19,
        expiry_date=dateutil.parser.isoparse('2022-01-08T15:51:51.663Z'),
        key='consectetur',
        meta=shared.PropertyPropertyConnectionAuthMeta(),
        name='Ms. Wilbert McGlynn',
        other_auth_info=[
            'accusantium',
        ],
        pem='magnam',
        refresh_token='repellat',
        state='omnis',
        token='explicabo',
        token_url='vel',
    ),
    auth_aws_arn='cum',
    categories=[
        shared.PropertyConnectionCategories.ENRICH,
    ],
    created_at=dateutil.parser.isoparse('2022-07-28T08:20:43.554Z'),
    environment='ipsam',
    external_xref='nostrum',
    id='3819b474-b0ed-420e-9624-8fff639a910a',
    integration_type='nam',
    is_paused=False,
    permissions=[
        shared.PropertyConnectionPermissions.HRIS_GROUP_WRITE,
    ],
    updated_at=dateutil.parser.isoparse('2020-12-12T11:22:41.690Z'),
    workspace_id='tempore',
)

res = s.connection.post_unified_connection(req, operations.PostUnifiedConnectionSecurity(
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
            access_token='commodi',
            api_url='fugit',
            app_id='suscipit',
            authorize_url='voluptate',
            client_id='nisi',
            client_secret='aliquid',
            consumer_key='provident',
            consumer_secret='laboriosam',
            emails=[
                'accusamus',
            ],
            expires_in=682.92,
            expiry_date=dateutil.parser.isoparse('2020-08-18T14:47:31.331Z'),
            key='eaque',
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            name='Miss Lois Cruickshank',
            other_auth_info=[
                'amet',
            ],
            pem='exercitationem',
            refresh_token='illum',
            state='praesentium',
            token='unde',
            token_url='similique',
        ),
        auth_aws_arn='eligendi',
        categories=[
            shared.PropertyConnectionCategories.MARTECH,
        ],
        created_at=dateutil.parser.isoparse('2022-02-10T02:37:22.453Z'),
        environment='nobis',
        external_xref='asperiores',
        id='da8d0c54-9ef0-4300-8978-a61fa1cf2068',
        integration_type='totam',
        is_paused=False,
        permissions=[
            shared.PropertyConnectionPermissions.ATS_JOB_READ,
        ],
        updated_at=dateutil.parser.isoparse('2022-07-16T11:02:07.974Z'),
        workspace_id='quod',
    ),
    id='1ffc71dc-a163-4f2a-bc80-a97ff334cddf',
)

res = s.connection.put_unified_connection_id(req, operations.PutUnifiedConnectionIDSecurity(
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

