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
    pass
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
)

res = s.team.get_crm_connection_id_team(req)

if res.crm_teams is not None:
    # handle response
    pass
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
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Arizona',
        ],
    ),
    connection_id='Internal experiences',
    id='<ID>',
)

res = s.team.patch_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'local',
        ],
    ),
    connection_id='pascal male bandwidth',
)

res = s.team.post_crm_connection_id_team(req)

if res.crm_team is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'immense',
        ],
    ),
    connection_id='duh Indonesia',
    id='<ID>',
)

res = s.team.put_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDTeamIDRequest](../../models/operations/putcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDTeamIDResponse](../../models/operations/putcrmconnectionidteamidresponse.md)**

