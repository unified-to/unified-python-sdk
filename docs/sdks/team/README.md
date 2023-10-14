# Team
(*team*)

### Available Operations

* [create_crm_team](#create_crm_team) - Create a team
* [get_crm_team](#get_crm_team) - Retrieve a team
* [list_crm_teams](#list_crm_teams) - List all teams
* [patch_crm_team](#patch_crm_team) - Update a team
* [remove_crm_team](#remove_crm_team) - Remove a team
* [update_crm_team](#update_crm_team) - Update a team

## create_crm_team

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

req = operations.CreateCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'exercitationem',
        ],
    ),
    connection_id='as New Senior',
    fields_=[
        'Buckinghamshire',
    ],
)

res = s.team.create_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmTeamRequest](../../models/operations/createcrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmTeamResponse](../../models/operations/createcrmteamresponse.md)**


## get_crm_team

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

req = operations.GetCrmTeamRequest(
    connection_id='digital awful',
    fields_=[
        'Peru',
    ],
    id='<ID>',
)

res = s.team.get_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmTeamRequest](../../models/operations/getcrmteamrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmTeamResponse](../../models/operations/getcrmteamresponse.md)**


## list_crm_teams

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

req = operations.ListCrmTeamsRequest(
    connection_id='Classical microchip Wooden',
    fields_=[
        'Lutetium',
    ],
)

res = s.team.list_crm_teams(req)

if res.crm_teams is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmTeamsRequest](../../models/operations/listcrmteamsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmTeamsResponse](../../models/operations/listcrmteamsresponse.md)**


## patch_crm_team

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

req = operations.PatchCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Account',
        ],
    ),
    connection_id='Transexual compress redefine',
    fields_=[
        'gold',
    ],
    id='<ID>',
)

res = s.team.patch_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmTeamRequest](../../models/operations/patchcrmteamrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmTeamResponse](../../models/operations/patchcrmteamresponse.md)**


## remove_crm_team

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

req = operations.RemoveCrmTeamRequest(
    connection_id='Sol',
    id='<ID>',
)

res = s.team.remove_crm_team(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmTeamRequest](../../models/operations/removecrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmTeamResponse](../../models/operations/removecrmteamresponse.md)**


## update_crm_team

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

req = operations.UpdateCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Carbon',
        ],
    ),
    connection_id='Dakota',
    fields_=[
        'female',
    ],
    id='<ID>',
)

res = s.team.update_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmTeamRequest](../../models/operations/updatecrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmTeamResponse](../../models/operations/updatecrmteamresponse.md)**

