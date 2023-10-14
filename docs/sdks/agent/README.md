# Agent
(*agent*)

### Available Operations

* [create_ticketing_agent](#create_ticketing_agent) - Create a agent
* [get_ticketing_agent](#get_ticketing_agent) - Retrieve a agent
* [list_ticketing_agents](#list_ticketing_agents) - List all agents
* [list_uc_agents](#list_uc_agents) - List all agents
* [patch_ticketing_agent](#patch_ticketing_agent) - Update a agent
* [remove_ticketing_agent](#remove_ticketing_agent) - Remove a agent
* [update_ticketing_agent](#update_ticketing_agent) - Update a agent

## create_ticketing_agent

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

req = operations.CreateTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Paolo.Cole8@yahoo.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='scarcely Soap navigating',
            ),
        ],
    ),
    connection_id='smoothly Algeria',
    fields_=[
        'payment',
    ],
)

res = s.agent.create_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateTicketingAgentRequest](../../models/operations/createticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateTicketingAgentResponse](../../models/operations/createticketingagentresponse.md)**


## get_ticketing_agent

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

req = operations.GetTicketingAgentRequest(
    connection_id='Lamborghini',
    fields_=[
        'SAS',
    ],
    id='<ID>',
)

res = s.agent.get_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTicketingAgentRequest](../../models/operations/getticketingagentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetTicketingAgentResponse](../../models/operations/getticketingagentresponse.md)**


## list_ticketing_agents

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

req = operations.ListTicketingAgentsRequest(
    connection_id='Mazda',
    fields_=[
        'Home',
    ],
)

res = s.agent.list_ticketing_agents(req)

if res.ticketing_agents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListTicketingAgentsRequest](../../models/operations/listticketingagentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListTicketingAgentsResponse](../../models/operations/listticketingagentsresponse.md)**


## list_uc_agents

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

req = operations.ListUcAgentsRequest(
    connection_id='Representative',
    fields_=[
        'olive',
    ],
)

res = s.agent.list_uc_agents(req)

if res.uc_agents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListUcAgentsRequest](../../models/operations/listucagentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListUcAgentsResponse](../../models/operations/listucagentsresponse.md)**


## patch_ticketing_agent

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

req = operations.PatchTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Danyka87@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='envious',
            ),
        ],
    ),
    connection_id='by',
    fields_=[
        'Bedfordshire',
    ],
    id='<ID>',
)

res = s.agent.patch_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchTicketingAgentRequest](../../models/operations/patchticketingagentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PatchTicketingAgentResponse](../../models/operations/patchticketingagentresponse.md)**


## remove_ticketing_agent

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

req = operations.RemoveTicketingAgentRequest(
    connection_id='monitor',
    id='<ID>',
)

res = s.agent.remove_ticketing_agent(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveTicketingAgentRequest](../../models/operations/removeticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RemoveTicketingAgentResponse](../../models/operations/removeticketingagentresponse.md)**


## update_ticketing_agent

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

req = operations.UpdateTicketingAgentRequest(
    ticketing_agent=shared.TicketingAgent(
        emails=[
            shared.TicketingEmail(
                email='Lorenz39@hotmail.com',
            ),
        ],
        raw=shared.PropertyTicketingAgentRaw(),
        telephones=[
            shared.TicketingTelephone(
                telephone='female',
            ),
        ],
    ),
    connection_id='beside Usability Bedfordshire',
    fields_=[
        'SSD',
    ],
    id='<ID>',
)

res = s.agent.update_ticketing_agent(req)

if res.ticketing_agent is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateTicketingAgentRequest](../../models/operations/updateticketingagentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateTicketingAgentResponse](../../models/operations/updateticketingagentresponse.md)**

