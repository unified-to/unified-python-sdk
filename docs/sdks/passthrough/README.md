# Passthrough
(*passthrough*)

### Available Operations

* [create_passthrough](#create_passthrough) - Passthrough POST
* [list_passthroughs](#list_passthroughs) - Passthrough GET
* [patch_passthrough](#patch_passthrough) - Passthrough PUT
* [remove_passthrough](#remove_passthrough) - Passthrough DELETE
* [update_passthrough](#update_passthrough) - Passthrough PUT

## create_passthrough

Passthrough POST

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreatePassthroughRequest(
    connection_id='<value>',
    path='/etc/periodic',
)

res = s.passthrough.create_passthrough(req, operations.CreatePassthroughSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreatePassthroughRequest](../../models/operations/createpassthroughrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreatePassthroughSecurity](../../models/operations/createpassthroughsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreatePassthroughResponse](../../models/operations/createpassthroughresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_passthroughs

Passthrough GET

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListPassthroughsRequest(
    connection_id='<value>',
    path='/selinux',
)

res = s.passthrough.list_passthroughs(req, operations.ListPassthroughsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPassthroughsRequest](../../models/operations/listpassthroughsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListPassthroughsSecurity](../../models/operations/listpassthroughssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListPassthroughsResponse](../../models/operations/listpassthroughsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_passthrough

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchPassthroughRequest(
    connection_id='<value>',
    path='/mnt',
)

res = s.passthrough.patch_passthrough(req, operations.PatchPassthroughSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchPassthroughRequest](../../models/operations/patchpassthroughrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchPassthroughSecurity](../../models/operations/patchpassthroughsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchPassthroughResponse](../../models/operations/patchpassthroughresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_passthrough

Passthrough DELETE

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemovePassthroughRequest(
    connection_id='<value>',
    path='/Applications',
)

res = s.passthrough.remove_passthrough(req, operations.RemovePassthroughSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemovePassthroughRequest](../../models/operations/removepassthroughrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemovePassthroughSecurity](../../models/operations/removepassthroughsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemovePassthroughResponse](../../models/operations/removepassthroughresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_passthrough

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdatePassthroughRequest(
    connection_id='<value>',
    path='/dev',
)

res = s.passthrough.update_passthrough(req, operations.UpdatePassthroughSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdatePassthroughRequest](../../models/operations/updatepassthroughrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdatePassthroughSecurity](../../models/operations/updatepassthroughsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdatePassthroughResponse](../../models/operations/updatepassthroughresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
