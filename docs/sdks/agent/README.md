# Agent

## Overview

### Available Operations

* [create_genai_agent](#create_genai_agent) - Create an agent
* [get_genai_agent](#get_genai_agent) - Retrieve an agent
* [list_genai_agents](#list_genai_agents) - List all agents
* [patch_genai_agent](#patch_genai_agent) - Update an agent
* [remove_genai_agent](#remove_genai_agent) - Remove an agent
* [update_genai_agent](#update_genai_agent) - Update an agent

## create_genai_agent

Creates a GenaiAgent. Provide the unified GenaiAgent fields in the request body; they are mapped to the provider's API. Returns the created GenaiAgent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiAgent" method="post" path="/genai/{connection_id}/agent" example="genai_agent" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.create_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "3fcfbef2-df27-47d9-887f-56f456c614a9",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-19T14:35:14.617Z"),
        },
        "connection_id": "<id>",
    })

    assert res.genai_agent is not None

    # Handle response
    print(res.genai_agent)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateGenaiAgentRequest](../../models/operations/creategenaiagentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateGenaiAgentResponse](../../models/operations/creategenaiagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_agent

Retrieves a single GenaiAgent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiAgent" method="get" path="/genai/{connection_id}/agent/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.get_genai_agent(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_agent is not None

    # Handle response
    print(res.genai_agent)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetGenaiAgentRequest](../../models/operations/getgenaiagentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetGenaiAgentResponse](../../models/operations/getgenaiagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_agents

Returns a list of GenaiAgents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiAgents" method="get" path="/genai/{connection_id}/agent" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.list_genai_agents(request={
        "connection_id": "<id>",
    })

    assert res.genai_agents is not None

    # Handle response
    print(res.genai_agents)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListGenaiAgentsRequest](../../models/operations/listgenaiagentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListGenaiAgentsResponse](../../models/operations/listgenaiagentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_agent

Updates the GenaiAgent identified by `id`. Provide the unified GenaiAgent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiAgent" method="patch" path="/genai/{connection_id}/agent/{id}" example="genai_agent" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.patch_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "5a8935ff-dff2-48e1-a641-13586be1c966",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-19T14:35:14.621Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_agent is not None

    # Handle response
    print(res.genai_agent)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchGenaiAgentRequest](../../models/operations/patchgenaiagentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchGenaiAgentResponse](../../models/operations/patchgenaiagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_agent

Deletes the GenaiAgent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiAgent" method="delete" path="/genai/{connection_id}/agent/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.remove_genai_agent(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveGenaiAgentRequest](../../models/operations/removegenaiagentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveGenaiAgentResponse](../../models/operations/removegenaiagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_agent

Updates the GenaiAgent identified by `id`. Provide the unified GenaiAgent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiAgent" method="put" path="/genai/{connection_id}/agent/{id}" example="genai_agent" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agent.update_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "5a8935ff-dff2-48e1-a641-13586be1c966",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-19T14:35:14.621Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_agent is not None

    # Handle response
    print(res.genai_agent)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateGenaiAgentRequest](../../models/operations/updategenaiagentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateGenaiAgentResponse](../../models/operations/updategenaiagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |