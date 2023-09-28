# Team
(*team*)

### Available Operations

* [delete_crm_connection_id_team_id](#delete_crm_connection_id_team_id) - Remove a team
* [get_crm_connection_id_team](#get_crm_connection_id_team) - List all teams
* [get_crm_connection_id_team_id](#get_crm_connection_id_team_id) - Retrieve a team
* [patch_crm_connection_id_team_id](#patch_crm_connection_id_team_id) - Update a team
* [post_crm_connection_id_team](#post_crm_connection_id_team) - Create a team
* [put_crm_connection_id_team_id](#put_crm_connection_id_team_id) - Update a team

## delete_crm_connection_id_team_id

Remove a team

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDTeamIDRequest(
    connection_id='Diverse',
    id='<ID>',
)

res = s.team.delete_crm_connection_id_team_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDTeamIDRequest](../../models/operations/deletecrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDTeamIDResponse](../../models/operations/deletecrmconnectionidteamidresponse.md)**


## get_crm_connection_id_team

List all teams

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

req = operations.GetCrmConnectionIDTeamRequest(
    connection_id='bath Lamborghini',
    limit=1042.31,
    offset=1586.42,
    order='Diesel Bike virtual',
    query='bakery',
    sort='Senior',
    updated_gte=dateutil.parser.isoparse('2021-12-04T23:56:00.028Z'),
)

res = s.team.get_crm_connection_id_team(req)

if res.crm_teams is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDTeamRequest](../../models/operations/getcrmconnectionidteamrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDTeamResponse](../../models/operations/getcrmconnectionidteamresponse.md)**


## get_crm_connection_id_team_id

Retrieve a team

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDTeamIDRequest(
    connection_id='Intelligent invoice Tesla',
    id='<ID>',
)

res = s.team.get_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDTeamIDRequest](../../models/operations/getcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDTeamIDResponse](../../models/operations/getcrmconnectionidteamidresponse.md)**


## patch_crm_connection_id_team_id

Update a team

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

req = operations.PatchCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2021-05-20T12:47:48.451Z'),
        description='Automated executive emulation',
        id='<ID>',
        name='Internal experiences',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-05-22T09:41:53.599Z'),
        user_ids=[
            'lumen',
        ],
    ),
    connection_id='up Candace',
    id='<ID>',
)

res = s.team.patch_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDTeamIDRequest](../../models/operations/patchcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDTeamIDResponse](../../models/operations/patchcrmconnectionidteamidresponse.md)**


## post_crm_connection_id_team

Create a team

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

req = operations.PostCrmConnectionIDTeamRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2022-02-12T08:57:03.070Z'),
        description='Organic transitional portal',
        id='<ID>',
        name='male bandwidth',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-12-29T15:50:04.365Z'),
        user_ids=[
            'meter',
        ],
    ),
    connection_id='Guaynabo AGP East',
)

res = s.team.post_crm_connection_id_team(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDTeamRequest](../../models/operations/postcrmconnectionidteamrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDTeamResponse](../../models/operations/postcrmconnectionidteamresponse.md)**


## put_crm_connection_id_team_id

Update a team

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

req = operations.PutCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2023-08-14T23:28:53.515Z'),
        description='Inverse multi-tasking task-force',
        id='<ID>',
        name='Indonesia Orchestrator Division',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-10-23T23:13:25.973Z'),
        user_ids=[
            'thoroughly',
        ],
    ),
    connection_id='delectus',
    id='<ID>',
)

res = s.team.put_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDTeamIDRequest](../../models/operations/putcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDTeamIDResponse](../../models/operations/putcrmconnectionidteamidresponse.md)**

