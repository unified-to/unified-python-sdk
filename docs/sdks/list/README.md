# ListT
(*list*)

### Available Operations

* [create_martech_list](#create_martech_list) - Create a list
* [get_martech_list](#get_martech_list) - Retrieve a list
* [list_martech_lists](#list_martech_lists) - List all lists
* [patch_martech_list](#patch_martech_list) - Update a list
* [remove_martech_list](#remove_martech_list) - Remove a list
* [update_martech_list](#update_martech_list) - Update a list

## create_martech_list

Create a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateMartechListRequest(
    connection_id='<value>',
)

res = s.list.create_martech_list(req, operations.CreateMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateMartechListRequest](../../models/operations/createmartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateMartechListSecurity](../../models/operations/createmartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateMartechListResponse](../../models/operations/createmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_martech_list

Retrieve a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.list.get_martech_list(req, operations.GetMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetMartechListRequest](../../models/operations/getmartechlistrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetMartechListSecurity](../../models/operations/getmartechlistsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetMartechListResponse](../../models/operations/getmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_martech_lists

List all lists

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListMartechListsRequest(
    connection_id='<value>',
)

res = s.list.list_martech_lists(req, operations.ListMartechListsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_lists is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListMartechListsRequest](../../models/operations/listmartechlistsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListMartechListsSecurity](../../models/operations/listmartechlistssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListMartechListsResponse](../../models/operations/listmartechlistsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_martech_list

Update a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.list.patch_martech_list(req, operations.PatchMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchMartechListRequest](../../models/operations/patchmartechlistrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchMartechListSecurity](../../models/operations/patchmartechlistsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchMartechListResponse](../../models/operations/patchmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_martech_list

Remove a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.list.remove_martech_list(req, operations.RemoveMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveMartechListRequest](../../models/operations/removemartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveMartechListSecurity](../../models/operations/removemartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveMartechListResponse](../../models/operations/removemartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_martech_list

Update a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.list.update_martech_list(req, operations.UpdateMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateMartechListRequest](../../models/operations/updatemartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateMartechListSecurity](../../models/operations/updatemartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateMartechListResponse](../../models/operations/updatemartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
