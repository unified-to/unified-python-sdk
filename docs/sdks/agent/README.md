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
    connection_id='navigate',
    id='<ID>',
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
    connection_id='East Steel Frozen',
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
    connection_id='Hat gas Cisgender',
    id='<ID>',
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
    connection_id='Regional East Sedan',
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
        emails=[
            shared.TicketingEmail(
                email='Albertha.Bernier63@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='Borders parse',
            ),
        ],
    ),
    connection_id='driver',
    id='<ID>',
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
        emails=[
            shared.TicketingEmail(
                email='Adele80@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='Unbranded Sedan',
            ),
        ],
    ),
    connection_id='wireless absent',
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
        emails=[
            shared.TicketingEmail(
                email='Samara_Botsford@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='newton Coordinator Refined',
            ),
        ],
    ),
    connection_id='asynchronous',
    id='<ID>',
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

