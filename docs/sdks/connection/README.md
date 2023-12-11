# Connection
(*connection*)

### Available Operations

* [create_unified_connection](#create_unified_connection) - Create connection
* [get_unified_connection](#get_unified_connection) - Retrieve connection
* [list_unified_connections](#list_unified_connections) - List all connections
* [patch_unified_connection](#patch_unified_connection) - Update connection
* [remove_unified_connection](#remove_unified_connection) - Remove connection
* [update_unified_connection](#update_unified_connection) - Update connection

## create_unified_connection

Create connection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.Connection(
    auth=shared.PropertyConnectionAuth(
        emails=[
            'string',
        ],
        meta=shared.PropertyPropertyConnectionAuthMeta(),
        other_auth_info=[
            'string',
        ],
    ),
    categories=[
        shared.PropertyConnectionCategories.ACCOUNTING,
    ],
    cursors_cache=[
        shared.Undefined(),
    ],
    integration_type='string',
    permissions=[
        shared.PropertyConnectionPermissions.ATS_DOCUMENT_WRITE,
    ],
)

res = s.connection.create_unified_connection(req)

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.Connection](../../models/shared/connection.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateUnifiedConnectionResponse](../../models/operations/createunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_unified_connection

Retrieve connection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetUnifiedConnectionRequest(
    id='<ID>',
)

res = s.connection.get_unified_connection(req)

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedConnectionRequest](../../models/operations/getunifiedconnectionrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetUnifiedConnectionResponse](../../models/operations/getunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_unified_connections

List all connections

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListUnifiedConnectionsRequest(
    categories=[
        operations.Categories.ENRICH,
    ],
)

res = s.connection.list_unified_connections(req)

if res.connections is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListUnifiedConnectionsRequest](../../models/operations/listunifiedconnectionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListUnifiedConnectionsResponse](../../models/operations/listunifiedconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_unified_connection

Update connection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchUnifiedConnectionRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            emails=[
                'string',
            ],
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            other_auth_info=[
                'string',
            ],
        ),
        categories=[
            shared.PropertyConnectionCategories.MARTECH,
        ],
        cursors_cache=[
            shared.Undefined(),
        ],
        integration_type='string',
        permissions=[
            shared.PropertyConnectionPermissions.MARTECH_LIST_READ,
        ],
    ),
    id='<ID>',
)

res = s.connection.patch_unified_connection(req)

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchUnifiedConnectionRequest](../../models/operations/patchunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchUnifiedConnectionResponse](../../models/operations/patchunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_unified_connection

Remove connection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveUnifiedConnectionRequest(
    id='<ID>',
)

res = s.connection.remove_unified_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveUnifiedConnectionRequest](../../models/operations/removeunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveUnifiedConnectionResponse](../../models/operations/removeunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_unified_connection

Update connection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateUnifiedConnectionRequest(
    connection=shared.Connection(
        auth=shared.PropertyConnectionAuth(
            emails=[
                'string',
            ],
            meta=shared.PropertyPropertyConnectionAuthMeta(),
            other_auth_info=[
                'string',
            ],
        ),
        categories=[
            shared.PropertyConnectionCategories.TICKETING,
        ],
        cursors_cache=[
            shared.Undefined(),
        ],
        integration_type='string',
        permissions=[
            shared.PropertyConnectionPermissions.CRM_DEAL_READ,
        ],
    ),
    id='<ID>',
)

res = s.connection.update_unified_connection(req)

if res.connection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateUnifiedConnectionRequest](../../models/operations/updateunifiedconnectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateUnifiedConnectionResponse](../../models/operations/updateunifiedconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
