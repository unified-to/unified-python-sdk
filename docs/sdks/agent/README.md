# agent

### Available Operations

* [delete_ticketing_connection_id_agent_id](#delete_ticketing_connection_id_agent_id) - Remove a agent
* [get_ticketing_connection_id_agent](#get_ticketing_connection_id_agent) - List all agents
* [get_ticketing_connection_id_agent_id](#get_ticketing_connection_id_agent_id) - Retrieve a agent
* [get_uc_connection_id_agent](#get_uc_connection_id_agent) - List all agents
* [patch_ticketing_connection_id_agent_id](#patch_ticketing_connection_id_agent_id) - Update a agent
* [post_ticketing_connection_id_agent](#post_ticketing_connection_id_agent) - Create a agent
* [put_ticketing_connection_id_agent_id](#put_ticketing_connection_id_agent_id) - Update a agent

## delete_ticketing_connection_id_agent_id

Remove a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='perferendis',
    id='5dfc2ddf-7cc7-48ca-9ba9-28fc816742cb',
)

res = s.agent.delete_ticketing_connection_id_agent_id(req, operations.DeleteTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTicketingConnectionIDAgentIDRequest](../../models/operations/deleteticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.DeleteTicketingConnectionIDAgentIDSecurity](../../models/operations/deleteticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.DeleteTicketingConnectionIDAgentIDResponse](../../models/operations/deleteticketingconnectionidagentidresponse.md)**


## get_ticketing_connection_id_agent

List all agents

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDAgentRequest(
    connection_id='esse',
    limit=2165.5,
    offset=5684.34,
    order='aspernatur',
    query='perferendis',
    sort='ad',
    updated_gte=dateutil.parser.isoparse('2022-09-13T17:41:46.141Z'),
)

res = s.agent.get_ticketing_connection_id_agent(req, operations.GetTicketingConnectionIDAgentSecurity(
    jwt="",
))

if res.ticketing_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetTicketingConnectionIDAgentRequest](../../models/operations/getticketingconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetTicketingConnectionIDAgentSecurity](../../models/operations/getticketingconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetTicketingConnectionIDAgentResponse](../../models/operations/getticketingconnectionidagentresponse.md)**


## get_ticketing_connection_id_agent_id

Retrieve a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDAgentIDRequest(
    connection_id='iste',
    id='396fea75-96eb-410f-aaa2-352c5955907a',
)

res = s.agent.get_ticketing_connection_id_agent_id(req, operations.GetTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDAgentIDRequest](../../models/operations/getticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.GetTicketingConnectionIDAgentIDSecurity](../../models/operations/getticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.GetTicketingConnectionIDAgentIDResponse](../../models/operations/getticketingconnectionidagentidresponse.md)**


## get_uc_connection_id_agent

List all agents

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDAgentRequest(
    connection_id='doloribus',
    contact_id='sapiente',
    limit=1020.44,
    offset=6527.9,
    order='dolorem',
    query='culpa',
    sort='consequuntur',
    updated_gte=dateutil.parser.isoparse('2021-01-15T20:18:47.519Z'),
)

res = s.agent.get_uc_connection_id_agent(req, operations.GetUcConnectionIDAgentSecurity(
    jwt="",
))

if res.uc_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetUcConnectionIDAgentRequest](../../models/operations/getucconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.GetUcConnectionIDAgentSecurity](../../models/operations/getucconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetUcConnectionIDAgentResponse](../../models/operations/getucconnectionidagentresponse.md)**


## patch_ticketing_connection_id_agent_id

Update a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-06-30T02:19:51.375Z'),
        emails=[
            shared.TicketingEmail(
                email='Jamil62@yahoo.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='51aa52c3-f5ad-4019-9a1f-fe78f097b007',
        name='Shawna Carter',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='iusto',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-05-13T20:56:04.612Z'),
    ),
    connection_id='accusamus',
    id='6e13b99d-488e-41e9-9e45-0ad2abd44269',
)

res = s.agent.patch_ticketing_connection_id_agent_id(req, operations.PatchTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchTicketingConnectionIDAgentIDRequest](../../models/operations/patchticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PatchTicketingConnectionIDAgentIDSecurity](../../models/operations/patchticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PatchTicketingConnectionIDAgentIDResponse](../../models/operations/patchticketingconnectionidagentidresponse.md)**


## post_ticketing_connection_id_agent

Create a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-12-17T07:42:55.593Z'),
        emails=[
            shared.TicketingEmail(
                email='Rhoda14@gmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='94bb4f63-c969-4e9a-befa-77dfb14cd66a',
        name='Alfred McClure',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='delectus',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-07-20T13:32:41.687Z'),
    ),
    connection_id='id',
)

res = s.agent.post_ticketing_connection_id_agent(req, operations.PostTicketingConnectionIDAgentSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostTicketingConnectionIDAgentRequest](../../models/operations/postticketingconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.PostTicketingConnectionIDAgentSecurity](../../models/operations/postticketingconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostTicketingConnectionIDAgentResponse](../../models/operations/postticketingconnectionidagentresponse.md)**


## put_ticketing_connection_id_agent_id

Update a agent

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2021-12-07T18:13:34.827Z'),
        emails=[
            shared.TicketingEmail(
                email='Daren.Nolan@hotmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='97074ba4-469b-46e2-9419-59890afa563e',
        name='Vivian Boyle',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='debitis',
                type=shared.TicketingTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-05-22T23:02:53.221Z'),
    ),
    connection_id='facilis',
    id='711e5b7f-d2ed-4028-921c-ddc692601fb5',
)

res = s.agent.put_ticketing_connection_id_agent_id(req, operations.PutTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTicketingConnectionIDAgentIDRequest](../../models/operations/putticketingconnectionidagentidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PutTicketingConnectionIDAgentIDSecurity](../../models/operations/putticketingconnectionidagentidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PutTicketingConnectionIDAgentIDResponse](../../models/operations/putticketingconnectionidagentidresponse.md)**

