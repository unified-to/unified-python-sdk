# Group
(*group*)

### Available Operations

* [delete_hris_connection_id_group_id](#delete_hris_connection_id_group_id) - Remove a group
* [get_hris_connection_id_group](#get_hris_connection_id_group) - List all groups
* [get_hris_connection_id_group_id](#get_hris_connection_id_group_id) - Retrieve a group
* [patch_hris_connection_id_group_id](#patch_hris_connection_id_group_id) - Update a group
* [post_hris_connection_id_group](#post_hris_connection_id_group) - Create a group
* [put_hris_connection_id_group_id](#put_hris_connection_id_group_id) - Update a group

## delete_hris_connection_id_group_id

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

req = operations.DeleteHrisConnectionIDGroupIDRequest(
    connection_id='consequently platforms Metal',
    id='<ID>',
)

res = s.group.delete_hris_connection_id_group_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteHrisConnectionIDGroupIDRequest](../../models/operations/deletehrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteHrisConnectionIDGroupIDResponse](../../models/operations/deletehrisconnectionidgroupidresponse.md)**


## get_hris_connection_id_group

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

req = operations.GetHrisConnectionIDGroupRequest(
    connection_id='Loan',
)

res = s.group.get_hris_connection_id_group(req)

if res.hris_groups is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetHrisConnectionIDGroupRequest](../../models/operations/gethrisconnectionidgrouprequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetHrisConnectionIDGroupResponse](../../models/operations/gethrisconnectionidgroupresponse.md)**


## get_hris_connection_id_group_id

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

req = operations.GetHrisConnectionIDGroupIDRequest(
    connection_id='behind',
    id='<ID>',
)

res = s.group.get_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetHrisConnectionIDGroupIDRequest](../../models/operations/gethrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetHrisConnectionIDGroupIDResponse](../../models/operations/gethrisconnectionidgroupidresponse.md)**


## patch_hris_connection_id_group_id

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

req = operations.PatchHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'gosh',
        ],
        manager_ids=[
            'Northwest',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='grey East Agender',
    id='<ID>',
)

res = s.group.patch_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchHrisConnectionIDGroupIDRequest](../../models/operations/patchhrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchHrisConnectionIDGroupIDResponse](../../models/operations/patchhrisconnectionidgroupidresponse.md)**


## post_hris_connection_id_group

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

req = operations.PostHrisConnectionIDGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'Bhutan',
        ],
        manager_ids=[
            'Polestar',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='Cab XSS',
)

res = s.group.post_hris_connection_id_group(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostHrisConnectionIDGroupRequest](../../models/operations/posthrisconnectionidgrouprequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PostHrisConnectionIDGroupResponse](../../models/operations/posthrisconnectionidgroupresponse.md)**


## put_hris_connection_id_group_id

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

req = operations.PutHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'panel',
        ],
        manager_ids=[
            'And',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='Small woman solid',
    id='<ID>',
)

res = s.group.put_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutHrisConnectionIDGroupIDRequest](../../models/operations/puthrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutHrisConnectionIDGroupIDResponse](../../models/operations/puthrisconnectionidgroupidresponse.md)**

