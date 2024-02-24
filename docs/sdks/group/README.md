# Group
(*group*)

### Available Operations

* [create_hris_group](#create_hris_group) - Create a group
* [get_hris_group](#get_hris_group) - Retrieve a group
* [list_hris_groups](#list_hris_groups) - List all groups
* [patch_hris_group](#patch_hris_group) - Update a group
* [remove_hris_group](#remove_hris_group) - Remove a group
* [update_hris_group](#update_hris_group) - Update a group

## create_hris_group

Create a group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateHrisGroupRequest(
    connection_id='<value>',
)

res = s.group.create_hris_group(req, operations.CreateHrisGroupSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateHrisGroupRequest](../../models/operations/createhrisgrouprequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.CreateHrisGroupSecurity](../../models/operations/createhrisgroupsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.CreateHrisGroupResponse](../../models/operations/createhrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_hris_group

Retrieve a group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisGroupRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.group.get_hris_group(req, operations.GetHrisGroupSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetHrisGroupRequest](../../models/operations/gethrisgrouprequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.GetHrisGroupSecurity](../../models/operations/gethrisgroupsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.GetHrisGroupResponse](../../models/operations/gethrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_hris_groups

List all groups

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListHrisGroupsRequest(
    connection_id='<value>',
)

res = s.group.list_hris_groups(req, operations.ListHrisGroupsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_groups is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListHrisGroupsRequest](../../models/operations/listhrisgroupsrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ListHrisGroupsSecurity](../../models/operations/listhrisgroupssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ListHrisGroupsResponse](../../models/operations/listhrisgroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_hris_group

Update a group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchHrisGroupRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.group.patch_hris_group(req, operations.PatchHrisGroupSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchHrisGroupRequest](../../models/operations/patchhrisgrouprequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PatchHrisGroupSecurity](../../models/operations/patchhrisgroupsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PatchHrisGroupResponse](../../models/operations/patchhrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_hris_group

Remove a group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveHrisGroupRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.group.remove_hris_group(req, operations.RemoveHrisGroupSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveHrisGroupRequest](../../models/operations/removehrisgrouprequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.RemoveHrisGroupSecurity](../../models/operations/removehrisgroupsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.RemoveHrisGroupResponse](../../models/operations/removehrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_hris_group

Update a group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateHrisGroupRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.group.update_hris_group(req, operations.UpdateHrisGroupSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateHrisGroupRequest](../../models/operations/updatehrisgrouprequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.UpdateHrisGroupSecurity](../../models/operations/updatehrisgroupsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.UpdateHrisGroupResponse](../../models/operations/updatehrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
