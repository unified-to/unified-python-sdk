# Genai

## Overview

### Available Operations

* [create_genai_agent](#create_genai_agent) - Create an agent
* [create_genai_embedding](#create_genai_embedding) - Create an embedding
* [create_genai_organization](#create_genai_organization) - Create an organization
* [create_genai_prompt](#create_genai_prompt) - Create a prompt
* [create_genai_task](#create_genai_task) - Create a task
* [get_genai_agent](#get_genai_agent) - Retrieve an agent
* [get_genai_model](#get_genai_model) - Retrieve a model
* [get_genai_organization](#get_genai_organization) - Retrieve an organization
* [get_genai_task](#get_genai_task) - Retrieve a task
* [list_genai_agents](#list_genai_agents) - List all agents
* [list_genai_models](#list_genai_models) - List all models
* [list_genai_organizations](#list_genai_organizations) - List all organizations
* [list_genai_tasks](#list_genai_tasks) - List all tasks
* [patch_genai_agent](#patch_genai_agent) - Update an agent
* [patch_genai_organization](#patch_genai_organization) - Update an organization
* [remove_genai_agent](#remove_genai_agent) - Remove an agent
* [remove_genai_organization](#remove_genai_organization) - Remove an organization
* [remove_genai_task](#remove_genai_task) - Remove a task
* [update_genai_agent](#update_genai_agent) - Update an agent
* [update_genai_organization](#update_genai_organization) - Update an organization

## create_genai_agent

Create an agent

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

    res = unified_to.genai.create_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "c104d9fa-c7f7-473a-9190-eb8d7db8fccd",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-09-20T11:48:23.168Z"),
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

## create_genai_embedding

Create an embedding

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiEmbedding" method="post" path="/genai/{connection_id}/embedding" example="genai_embedding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_embedding(request={
        "genai_embedding": {
            "content": [
                {
                    "text": "Utrimque temptatio pecco demulceo.",
                },
            ],
            "dimension": 423.0,
            "embeddings": "Est.",
            "enconding_format": shared.EncondingFormat.FLOAT,
            "id": "62bbaf9c-5d32-4a2e-88ba-812b77de9ed1",
            "max_tokens": 223.0,
            "tokens_used": 836.0,
            "type": "classification",
        },
        "connection_id": "<id>",
    })

    assert res.genai_embedding is not None

    # Handle response
    print(res.genai_embedding)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateGenaiEmbeddingRequest](../../models/operations/creategenaiembeddingrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateGenaiEmbeddingResponse](../../models/operations/creategenaiembeddingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_genai_organization

Create an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiOrganization" method="post" path="/genai/{connection_id}/organization" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "c6b6737d-7782-41e3-a20e-674fb9c33d86",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.003Z"),
        },
        "connection_id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateGenaiOrganizationRequest](../../models/operations/creategenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateGenaiOrganizationResponse](../../models/operations/creategenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_genai_prompt

Create a prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiPrompt" method="post" path="/genai/{connection_id}/prompt" example="genai_prompt" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_prompt(request={
        "genai_prompt": {
            "max_tokens": 0.4677782787475735,
            "mcp_authorization_token": "f45a6e93-7bed-49b4-a5c8-37a2ed2d58f4",
            "mcp_deferred_tools": [],
            "mcp_url": "https://unsung-dusk.info/",
            "messages": [
                {
                    "content": "Aegre repudiandae verecundia facere statua.",
                    "role": shared.Role.ASSISTANT,
                },
                {
                    "content": "Speciosus xiphias soleo trepide crinis.",
                    "role": shared.Role.SYSTEM,
                },
            ],
            "responses": [
                "Balbus vobis circumvenio una.",
            ],
            "temperature": 0.0,
            "tokens_used": 975.0,
        },
        "connection_id": "<id>",
    })

    assert res.genai_prompt is not None

    # Handle response
    print(res.genai_prompt)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateGenaiPromptRequest](../../models/operations/creategenaipromptrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateGenaiPromptResponse](../../models/operations/creategenaipromptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_genai_task

Create a task

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiTask" method="post" path="/genai/{connection_id}/task" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-09-06T09:18:49.674Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "586f6326-fe69-435c-8548-3150816342b0",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-03T10:13:29.849Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-02-14T12:14:43.464Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateGenaiTaskRequest](../../models/operations/creategenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateGenaiTaskResponse](../../models/operations/creategenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_agent

Retrieve an agent

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

    res = unified_to.genai.get_genai_agent(request={
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

## get_genai_model

Retrieve a model

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiModel" method="get" path="/genai/{connection_id}/model/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.get_genai_model(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_model is not None

    # Handle response
    print(res.genai_model)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetGenaiModelRequest](../../models/operations/getgenaimodelrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetGenaiModelResponse](../../models/operations/getgenaimodelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiOrganization" method="get" path="/genai/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.get_genai_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetGenaiOrganizationRequest](../../models/operations/getgenaiorganizationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetGenaiOrganizationResponse](../../models/operations/getgenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_task

Retrieve a task

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiTask" method="get" path="/genai/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.get_genai_task(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetGenaiTaskRequest](../../models/operations/getgenaitaskrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetGenaiTaskResponse](../../models/operations/getgenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_agents

List all agents

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

    res = unified_to.genai.list_genai_agents(request={
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

## list_genai_models

List all models

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiModels" method="get" path="/genai/{connection_id}/model" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.list_genai_models(request={
        "connection_id": "<id>",
    })

    assert res.genai_models is not None

    # Handle response
    print(res.genai_models)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListGenaiModelsRequest](../../models/operations/listgenaimodelsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListGenaiModelsResponse](../../models/operations/listgenaimodelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiOrganizations" method="get" path="/genai/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.list_genai_organizations(request={
        "connection_id": "<id>",
    })

    assert res.genai_organizations is not None

    # Handle response
    print(res.genai_organizations)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListGenaiOrganizationsRequest](../../models/operations/listgenaiorganizationsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListGenaiOrganizationsResponse](../../models/operations/listgenaiorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_tasks

List all tasks

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiTasks" method="get" path="/genai/{connection_id}/task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.list_genai_tasks(request={
        "connection_id": "<id>",
    })

    assert res.genai_tasks is not None

    # Handle response
    print(res.genai_tasks)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListGenaiTasksRequest](../../models/operations/listgenaitasksrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListGenaiTasksResponse](../../models/operations/listgenaitasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_agent

Update an agent

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

    res = unified_to.genai.patch_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "1c8b2286-947d-4e72-ab18-0b3a5b1e863d",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-09-20T11:48:23.176Z"),
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

## patch_genai_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiOrganization" method="patch" path="/genai/{connection_id}/organization/{id}" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.patch_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "e466e490-09c0-476e-9a38-d324960c1635",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.005Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchGenaiOrganizationRequest](../../models/operations/patchgenaiorganizationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchGenaiOrganizationResponse](../../models/operations/patchgenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_agent

Remove an agent

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

    res = unified_to.genai.remove_genai_agent(request={
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

## remove_genai_organization

Remove an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiOrganization" method="delete" path="/genai/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.remove_genai_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveGenaiOrganizationRequest](../../models/operations/removegenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveGenaiOrganizationResponse](../../models/operations/removegenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_task

Remove a task

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiTask" method="delete" path="/genai/{connection_id}/task/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.remove_genai_task(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveGenaiTaskRequest](../../models/operations/removegenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveGenaiTaskResponse](../../models/operations/removegenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_agent

Update an agent

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

    res = unified_to.genai.update_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "1c8b2286-947d-4e72-ab18-0b3a5b1e863d",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-09-20T11:48:23.176Z"),
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

## update_genai_organization

Update an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiOrganization" method="put" path="/genai/{connection_id}/organization/{id}" example="genai_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.update_genai_organization(request={
        "genai_organization": {
            "created_at": parse_datetime("2020-10-27T16:03:47.122Z"),
            "description": "Voluptates abeo subseco.",
            "id": "e466e490-09c0-476e-9a38-d324960c1635",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-15T02:14:43.005Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_organization is not None

    # Handle response
    print(res.genai_organization)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateGenaiOrganizationRequest](../../models/operations/updategenaiorganizationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateGenaiOrganizationResponse](../../models/operations/updategenaiorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |