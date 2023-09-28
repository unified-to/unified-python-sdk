# Group
(*group*)

### Available Operations

* [delete_hris_connection_id_group_id](#delete_hris_connection_id_group_id) - Remove a Group
* [get_hris_connection_id_group](#get_hris_connection_id_group) - List all Groups
* [get_hris_connection_id_group_id](#get_hris_connection_id_group_id) - Retrieve a Group
* [patch_hris_connection_id_group_id](#patch_hris_connection_id_group_id) - Update a Group
* [post_hris_connection_id_group](#post_hris_connection_id_group) - Create a Group
* [put_hris_connection_id_group_id](#put_hris_connection_id_group_id) - Update a Group

## delete_hris_connection_id_group_id

Remove a Group

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

List all Groups

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
    limit=3486.96,
    offset=9705.73,
    order='Coordinator',
    query='World',
    sort='Dollar',
    updated_gte=dateutil.parser.isoparse('2021-01-15T16:06:13.340Z'),
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

Retrieve a Group

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

Update a Group

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
        created_at=dateutil.parser.isoparse('2023-10-19T05:30:26.390Z'),
        description='Stand-alone asymmetric orchestration',
        employee_ids=[
            'shootdown',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            '24/7',
        ],
        name='Agender trainer',
        parent_id='Configuration Kids Sedan',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DIVISION,
        updated_at=dateutil.parser.isoparse('2021-08-18T16:48:12.885Z'),
    ),
    connection_id='Intersex',
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

Create a Group

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
        created_at=dateutil.parser.isoparse('2021-02-23T15:35:38.483Z'),
        description='Configurable stable product',
        employee_ids=[
            'Auto',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            'JSON',
        ],
        name='whereas Usability transmitting',
        parent_id='invoice Cyclocross Electric',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.GROUP,
        updated_at=dateutil.parser.isoparse('2021-04-30T12:40:50.129Z'),
    ),
    connection_id='Hybrid Schenectady',
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

Update a Group

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
        created_at=dateutil.parser.isoparse('2022-08-10T12:11:42.375Z'),
        description='Decentralized methodical projection',
        employee_ids=[
            'Credit',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            'South',
        ],
        name='Jeep brr Northwest',
        parent_id='quickly Licensed',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.BUSINESS_UNIT,
        updated_at=dateutil.parser.isoparse('2021-11-08T00:11:45.458Z'),
    ),
    connection_id='vortals interface Gasoline',
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

