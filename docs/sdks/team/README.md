# team

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDTeamIDRequest(
    connection_id='ab',
    id='bbf05527-1b25-411d-9606-dd1b28272bc9',
)

res = s.team.delete_crm_connection_id_team_id(req, operations.DeleteCrmConnectionIDTeamIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCrmConnectionIDTeamIDRequest](../../models/operations/deletecrmconnectionidteamidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.DeleteCrmConnectionIDTeamIDSecurity](../../models/operations/deletecrmconnectionidteamidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.DeleteCrmConnectionIDTeamIDResponse](../../models/operations/deletecrmconnectionidteamidresponse.md)**


## get_crm_connection_id_team

List all teams

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDTeamRequest(
    connection_id='placeat',
    limit=1884.9,
    offset=1694.68,
    order='sunt',
    query='vitae',
    sort='ex',
    updated_gte=dateutil.parser.parse('2022-01-05').date(),
)

res = s.team.get_crm_connection_id_team(req, operations.GetCrmConnectionIDTeamSecurity(
    jwt="",
))

if res.crm_teams is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCrmConnectionIDTeamRequest](../../models/operations/getcrmconnectionidteamrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.GetCrmConnectionIDTeamSecurity](../../models/operations/getcrmconnectionidteamsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetCrmConnectionIDTeamResponse](../../models/operations/getcrmconnectionidteamresponse.md)**


## get_crm_connection_id_team_id

Retrieve a team

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDTeamIDRequest(
    connection_id='rerum',
    id='1880fcbb-2b93-4c15-b670-bd1784831653',
)

res = s.team.get_crm_connection_id_team_id(req, operations.GetCrmConnectionIDTeamIDSecurity(
    jwt="",
))

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDTeamIDRequest](../../models/operations/getcrmconnectionidteamidrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetCrmConnectionIDTeamIDSecurity](../../models/operations/getcrmconnectionidteamidsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetCrmConnectionIDTeamIDResponse](../../models/operations/getcrmconnectionidteamidresponse.md)**


## patch_crm_connection_id_team_id

Update a team

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.parse('2020-04-24').date(),
        description='harum',
        id='3b6e241c-3109-4983-a63c-66dcbb7df6cb',
        name='Jenny Rolfson',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.parse('2022-12-14').date(),
        user_ids=[
            'praesentium',
        ],
    ),
    connection_id='recusandae',
    id='0713774d-e4fe-4e10-9d97-80a10c47b950',
)

res = s.team.patch_crm_connection_id_team_id(req, operations.PatchCrmConnectionIDTeamIDSecurity(
    jwt="",
))

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchCrmConnectionIDTeamIDRequest](../../models/operations/patchcrmconnectionidteamidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchCrmConnectionIDTeamIDSecurity](../../models/operations/patchcrmconnectionidteamidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchCrmConnectionIDTeamIDResponse](../../models/operations/patchcrmconnectionidteamidresponse.md)**


## post_crm_connection_id_team

Create a team

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostCrmConnectionIDTeamRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.parse('2022-12-18').date(),
        description='possimus',
        id='6c8b2a5f-0022-407e-8048-f90009ed2902',
        name='Brandy Tillman',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.parse('2021-02-19').date(),
        user_ids=[
            'iste',
        ],
    ),
    connection_id='pariatur',
)

res = s.team.post_crm_connection_id_team(req, operations.PostCrmConnectionIDTeamSecurity(
    jwt="",
))

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostCrmConnectionIDTeamRequest](../../models/operations/postcrmconnectionidteamrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.PostCrmConnectionIDTeamSecurity](../../models/operations/postcrmconnectionidteamsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.PostCrmConnectionIDTeamResponse](../../models/operations/postcrmconnectionidteamresponse.md)**


## put_crm_connection_id_team_id

Update a team

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.parse('2022-09-20').date(),
        description='sunt',
        id='61e91500-323b-42c0-9b92-4771f5669e5b',
        name='Tricia Sawayn',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.parse('2022-07-25').date(),
        user_ids=[
            'ea',
        ],
    ),
    connection_id='labore',
    id='9d84eb9e-4cfd-4227-ae0b-88fb87d6fa5b',
)

res = s.team.put_crm_connection_id_team_id(req, operations.PutCrmConnectionIDTeamIDSecurity(
    jwt="",
))

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCrmConnectionIDTeamIDRequest](../../models/operations/putcrmconnectionidteamidrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.PutCrmConnectionIDTeamIDSecurity](../../models/operations/putcrmconnectionidteamidsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.PutCrmConnectionIDTeamIDResponse](../../models/operations/putcrmconnectionidteamidresponse.md)**

