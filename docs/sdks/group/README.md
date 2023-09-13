# group

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteHrisConnectionIDGroupIDRequest(
    connection_id='ipsam',
    id='8aaeacae-323a-431b-b7ba-1cc97716c802',
)

res = s.group.delete_hris_connection_id_group_id(req, operations.DeleteHrisConnectionIDGroupIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteHrisConnectionIDGroupIDRequest](../../models/operations/deletehrisconnectionidgroupidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.DeleteHrisConnectionIDGroupIDSecurity](../../models/operations/deletehrisconnectionidgroupidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.DeleteHrisConnectionIDGroupIDResponse](../../models/operations/deletehrisconnectionidgroupidresponse.md)**


## get_hris_connection_id_group

List all Groups

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisConnectionIDGroupRequest(
    connection_id='minus',
    limit=7864.46,
    offset=5742.21,
    order='voluptates',
    query='alias',
    sort='placeat',
    updated_gte=dateutil.parser.parse('2022-03-07').date(),
)

res = s.group.get_hris_connection_id_group(req, operations.GetHrisConnectionIDGroupSecurity(
    jwt="",
))

if res.hris_groups is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetHrisConnectionIDGroupRequest](../../models/operations/gethrisconnectionidgrouprequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetHrisConnectionIDGroupSecurity](../../models/operations/gethrisconnectionidgroupsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetHrisConnectionIDGroupResponse](../../models/operations/gethrisconnectionidgroupresponse.md)**


## get_hris_connection_id_group_id

Retrieve a Group

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisConnectionIDGroupIDRequest(
    connection_id='iste',
    id='d323f1aa-63ed-49cf-9c85-6bcba51ef245',
)

res = s.group.get_hris_connection_id_group_id(req, operations.GetHrisConnectionIDGroupIDSecurity(
    jwt="",
))

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetHrisConnectionIDGroupIDRequest](../../models/operations/gethrisconnectionidgroupidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.GetHrisConnectionIDGroupIDSecurity](../../models/operations/gethrisconnectionidgroupidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.GetHrisConnectionIDGroupIDResponse](../../models/operations/gethrisconnectionidgroupidresponse.md)**


## patch_hris_connection_id_group_id

Update a Group

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.parse('2022-05-13').date(),
        description='aliquam',
        employee_ids=[
            'iusto',
        ],
        id='facf116c-dd54-444a-b562-873c7dd9efaf',
        is_active=False,
        manager_ids=[
            'labore',
        ],
        name='Cristina Russel',
        parent_id='consectetur',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DEPARTMENT,
        updated_at=dateutil.parser.parse('2022-12-28').date(),
    ),
    connection_id='delectus',
    id='3138f30d-f3db-4022-baa5-65fb8f652ebb',
)

res = s.group.patch_hris_connection_id_group_id(req, operations.PatchHrisConnectionIDGroupIDSecurity(
    jwt="",
))

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchHrisConnectionIDGroupIDRequest](../../models/operations/patchhrisconnectionidgroupidrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PatchHrisConnectionIDGroupIDSecurity](../../models/operations/patchhrisconnectionidgroupidsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PatchHrisConnectionIDGroupIDResponse](../../models/operations/patchhrisconnectionidgroupidresponse.md)**


## post_hris_connection_id_group

Create a Group

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostHrisConnectionIDGroupRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.parse('2021-04-22').date(),
        description='dolor',
        employee_ids=[
            'praesentium',
        ],
        id='38387902-43b2-493d-ab30-e917f50fda04',
        is_active=False,
        manager_ids=[
            'porro',
        ],
        name='Wm Boyer',
        parent_id='exercitationem',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DEPARTMENT,
        updated_at=dateutil.parser.parse('2022-08-30').date(),
    ),
    connection_id='unde',
)

res = s.group.post_hris_connection_id_group(req, operations.PostHrisConnectionIDGroupSecurity(
    jwt="",
))

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostHrisConnectionIDGroupRequest](../../models/operations/posthrisconnectionidgrouprequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.PostHrisConnectionIDGroupSecurity](../../models/operations/posthrisconnectionidgroupsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.PostHrisConnectionIDGroupResponse](../../models/operations/posthrisconnectionidgroupresponse.md)**


## put_hris_connection_id_group_id

Update a Group

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.parse('2022-04-06').date(),
        description='aut',
        employee_ids=[
            'expedita',
        ],
        id='c3bb7446-64eb-41d0-b388-b0d1bb17afee',
        is_active=False,
        manager_ids=[
            'reprehenderit',
        ],
        name='Latoya Hodkiewicz',
        parent_id='quidem',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.BUSINESS_UNIT,
        updated_at=dateutil.parser.parse('2022-08-19').date(),
    ),
    connection_id='voluptate',
    id='c7edaf39-d16f-4bf7-afd1-62b303e3023b',
)

res = s.group.put_hris_connection_id_group_id(req, operations.PutHrisConnectionIDGroupIDSecurity(
    jwt="",
))

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutHrisConnectionIDGroupIDRequest](../../models/operations/puthrisconnectionidgroupidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PutHrisConnectionIDGroupIDSecurity](../../models/operations/puthrisconnectionidgroupidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PutHrisConnectionIDGroupIDResponse](../../models/operations/puthrisconnectionidgroupidresponse.md)**

