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
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'transmitter',
        ],
        manager_ids=[
            'dependable',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='Technetium',
    fields_=[
        'Tactics',
    ],
)

res = s.group.create_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateHrisGroupRequest](../../models/operations/createhrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateHrisGroupResponse](../../models/operations/createhrisgroupresponse.md)**


## get_hris_group

Retrieve a group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetHrisGroupRequest(
    connection_id='Cedi state Cadillac',
    fields_=[
        'optical',
    ],
    id='<ID>',
)

res = s.group.get_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetHrisGroupRequest](../../models/operations/gethrisgrouprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetHrisGroupResponse](../../models/operations/gethrisgroupresponse.md)**


## list_hris_groups

List all groups

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

req = operations.ListHrisGroupsRequest(
    connection_id='Bronze Rubber',
    fields_=[
        'feel',
    ],
)

res = s.group.list_hris_groups(req)

if res.hris_groups is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListHrisGroupsRequest](../../models/operations/listhrisgroupsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ListHrisGroupsResponse](../../models/operations/listhrisgroupsresponse.md)**


## patch_hris_group

Update a group

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

req = operations.PatchHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'scalable',
        ],
        manager_ids=[
            'Bespoke',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='bluetooth West',
    fields_=[
        'Intersex',
    ],
    id='<ID>',
)

res = s.group.patch_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchHrisGroupRequest](../../models/operations/patchhrisgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PatchHrisGroupResponse](../../models/operations/patchhrisgroupresponse.md)**


## remove_hris_group

Remove a group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveHrisGroupRequest(
    connection_id='Human Soft Unbranded',
    id='<ID>',
)

res = s.group.remove_hris_group(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveHrisGroupRequest](../../models/operations/removehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RemoveHrisGroupResponse](../../models/operations/removehrisgroupresponse.md)**


## update_hris_group

Update a group

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

req = operations.UpdateHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'disintermediate',
        ],
        manager_ids=[
            'schemas',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='bashfully',
    fields_=[
        'Avon',
    ],
    id='<ID>',
)

res = s.group.update_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateHrisGroupRequest](../../models/operations/updatehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateHrisGroupResponse](../../models/operations/updatehrisgroupresponse.md)**

