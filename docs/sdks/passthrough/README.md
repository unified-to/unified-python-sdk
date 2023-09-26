# Passthrough
(*passthrough*)

### Available Operations

* [delete_passthrough_connection_id_path](#delete_passthrough_connection_id_path) - Passthrough DELETE
* [get_passthrough_connection_id_path](#get_passthrough_connection_id_path) - Passthrough GET
* [patch_passthrough_connection_id_path](#patch_passthrough_connection_id_path) - Passthrough PUT
* [post_passthrough_connection_id_path](#post_passthrough_connection_id_path) - Passthrough POST
* [put_passthrough_connection_id_path](#put_passthrough_connection_id_path) - Passthrough PUT

## delete_passthrough_connection_id_path

Passthrough DELETE

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeletePassthroughConnectionIDPathRequest(
    connection_id='fugiat',
    path='debitis',
)

res = s.passthrough.delete_passthrough_connection_id_path(req)

if res.undefined is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeletePassthroughConnectionIDPathRequest](../../models/operations/deletepassthroughconnectionidpathrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.DeletePassthroughConnectionIDPathResponse](../../models/operations/deletepassthroughconnectionidpathresponse.md)**


## get_passthrough_connection_id_path

Passthrough GET

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetPassthroughConnectionIDPathRequest(
    connection_id='minima',
    path='ducimus',
)

res = s.passthrough.get_passthrough_connection_id_path(req)

if res.undefined is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetPassthroughConnectionIDPathRequest](../../models/operations/getpassthroughconnectionidpathrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetPassthroughConnectionIDPathResponse](../../models/operations/getpassthroughconnectionidpathresponse.md)**


## patch_passthrough_connection_id_path

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchPassthroughConnectionIDPathRequest(
    connection_id='est',
    path='dicta',
    undefined=shared.Undefined(),
)

res = s.passthrough.patch_passthrough_connection_id_path(req)

if res.undefined is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchPassthroughConnectionIDPathRequest](../../models/operations/patchpassthroughconnectionidpathrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PatchPassthroughConnectionIDPathResponse](../../models/operations/patchpassthroughconnectionidpathresponse.md)**


## post_passthrough_connection_id_path

Passthrough POST

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PostPassthroughConnectionIDPathRequest(
    connection_id='architecto',
    path='fugiat',
    undefined=shared.Undefined(),
)

res = s.passthrough.post_passthrough_connection_id_path(req)

if res.undefined is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostPassthroughConnectionIDPathRequest](../../models/operations/postpassthroughconnectionidpathrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PostPassthroughConnectionIDPathResponse](../../models/operations/postpassthroughconnectionidpathresponse.md)**


## put_passthrough_connection_id_path

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutPassthroughConnectionIDPathRequest(
    connection_id='eum',
    path='vitae',
    undefined=shared.Undefined(),
)

res = s.passthrough.put_passthrough_connection_id_path(req)

if res.undefined is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutPassthroughConnectionIDPathRequest](../../models/operations/putpassthroughconnectionidpathrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PutPassthroughConnectionIDPathResponse](../../models/operations/putpassthroughconnectionidpathresponse.md)**

