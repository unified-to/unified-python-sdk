# Agent
(*agent*)

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='esse',
    id='39205929-396f-4ea7-996e-b10faaa2352c',
)

res = s.agent.delete_ticketing_connection_id_agent_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.DeleteTicketingConnectionIDAgentIDRequest](../../models/operations/deleteticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.DeleteTicketingConnectionIDAgentIDResponse](../../models/operations/deleteticketingconnectionidagentidresponse.md)**


## get_ticketing_connection_id_agent

List all agents

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

req = operations.GetTicketingConnectionIDAgentRequest(
    connection_id='enim',
    limit=6078.31,
    offset=3637.11,
    order='minima',
    query='excepturi',
    sort='accusantium',
    updated_gte=dateutil.parser.isoparse('2022-05-14T11:45:33.094Z'),
)

res = s.agent.get_ticketing_connection_id_agent(req)

if res.ticketing_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetTicketingConnectionIDAgentRequest](../../models/operations/getticketingconnectionidagentrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetTicketingConnectionIDAgentResponse](../../models/operations/getticketingconnectionidagentresponse.md)**


## get_ticketing_connection_id_agent_id

Retrieve a agent

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDAgentIDRequest(
    connection_id='doloribus',
    id='f1a3a2fa-9467-4739-a51a-a52c3f5ad019',
)

res = s.agent.get_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetTicketingConnectionIDAgentIDRequest](../../models/operations/getticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetTicketingConnectionIDAgentIDResponse](../../models/operations/getticketingconnectionidagentidresponse.md)**


## get_uc_connection_id_agent

List all agents

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

req = operations.GetUcConnectionIDAgentRequest(
    connection_id='temporibus',
    contact_id='laborum',
    limit=960.98,
    offset=9719.45,
    order='voluptatibus',
    query='vero',
    sort='nihil',
    updated_gte=dateutil.parser.isoparse('2021-01-17T23:08:44.457Z'),
)

res = s.agent.get_uc_connection_id_agent(req)

if res.uc_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUcConnectionIDAgentRequest](../../models/operations/getucconnectionidagentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUcConnectionIDAgentResponse](../../models/operations/getucconnectionidagentresponse.md)**


## patch_ticketing_connection_id_agent_id

Update a agent

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

req = operations.PatchTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-05-25T05:33:11.349Z'),
        emails=[
            shared.TicketingEmail(
                email='Myrtis44@yahoo.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='f15471b5-e6e1-43b9-9d48-8e1e91e450ad',
        name='Joanna Rau',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='modi',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-05-31T22:08:47.731Z'),
    ),
    connection_id='quos',
    id='02d502a9-4bb4-4f63-8969-e9a3efa77dfb',
)

res = s.agent.patch_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PatchTicketingConnectionIDAgentIDRequest](../../models/operations/patchticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PatchTicketingConnectionIDAgentIDResponse](../../models/operations/patchticketingconnectionidagentidresponse.md)**


## post_ticketing_connection_id_agent

Create a agent

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

req = operations.PostTicketingConnectionIDAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2022-09-14T10:27:07.590Z'),
        emails=[
            shared.TicketingEmail(
                email='Raquel_Jenkins@hotmail.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='395efb9b-a88f-43a6-a997-074ba4469b6e',
        name='Ms. Julie Gusikowski',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='provident',
                type=shared.TicketingTelephoneType.OTHER,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-12-07T10:53:17.121Z'),
    ),
    connection_id='mollitia',
)

res = s.agent.post_ticketing_connection_id_agent(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostTicketingConnectionIDAgentRequest](../../models/operations/postticketingconnectionidagentrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostTicketingConnectionIDAgentResponse](../../models/operations/postticketingconnectionidagentresponse.md)**


## put_ticketing_connection_id_agent_id

Update a agent

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

req = operations.PutTicketingConnectionIDAgentIDRequest(
    ticketing_agent=shared.TicketingAgent(
        created_at=dateutil.parser.isoparse('2021-01-16T22:43:33.071Z'),
        emails=[
            shared.TicketingEmail(
                email='Holden.Ernser36@gmail.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='6fe4c8b7-11e5-4b7f-92ed-028921cddc69',
        name='Dr. Rosemary Bartoletti',
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='ipsam',
                type=shared.TicketingTelephoneType.OTHER,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-12T10:47:34.158Z'),
    ),
    connection_id='eaque',
    id='d5f0d30c-5fbb-4258-b053-202c73d5fe9b',
)

res = s.agent.put_ticketing_connection_id_agent_id(req)

if res.ticketing_agent is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PutTicketingConnectionIDAgentIDRequest](../../models/operations/putticketingconnectionidagentidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PutTicketingConnectionIDAgentIDResponse](../../models/operations/putticketingconnectionidagentidresponse.md)**

