# Genai

## Overview

### Available Operations

* [create_genai_agent](#create_genai_agent) - Create an agent
* [create_genai_embedding](#create_genai_embedding) - Create an embedding
* [create_genai_memory](#create_genai_memory) - Create a memory
* [create_genai_organization](#create_genai_organization) - Create an organization
* [create_genai_prompt](#create_genai_prompt) - Create a prompt
* [create_genai_task](#create_genai_task) - Create a task
* [get_genai_agent](#get_genai_agent) - Retrieve an agent
* [get_genai_memory](#get_genai_memory) - Retrieve a memory
* [get_genai_model](#get_genai_model) - Retrieve a model
* [get_genai_organization](#get_genai_organization) - Retrieve an organization
* [get_genai_skill](#get_genai_skill) - Retrieve a skill
* [get_genai_task](#get_genai_task) - Retrieve a task
* [list_genai_agents](#list_genai_agents) - List all agents
* [list_genai_memories](#list_genai_memories) - List all memories
* [list_genai_models](#list_genai_models) - List all models
* [list_genai_organizations](#list_genai_organizations) - List all organizations
* [list_genai_skills](#list_genai_skills) - List all skills
* [list_genai_tasks](#list_genai_tasks) - List all tasks
* [patch_genai_agent](#patch_genai_agent) - Update an agent
* [patch_genai_memory](#patch_genai_memory) - Update a memory
* [patch_genai_organization](#patch_genai_organization) - Update an organization
* [patch_genai_task](#patch_genai_task) - Update a task
* [remove_genai_agent](#remove_genai_agent) - Remove an agent
* [remove_genai_memory](#remove_genai_memory) - Remove a memory
* [remove_genai_organization](#remove_genai_organization) - Remove an organization
* [remove_genai_skill](#remove_genai_skill) - Remove a skill
* [remove_genai_task](#remove_genai_task) - Remove a task
* [update_genai_agent](#update_genai_agent) - Update an agent
* [update_genai_memory](#update_genai_memory) - Update a memory
* [update_genai_organization](#update_genai_organization) - Update an organization
* [update_genai_task](#update_genai_task) - Update a task

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

    res = unified_to.genai.create_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "3f202140-2007-4217-b564-4e03200220fd",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-23T15:05:11.536Z"),
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

Creates a GenaiEmbedding. Provide the unified GenaiEmbedding fields in the request body; they are mapped to the provider's API. Returns the created GenaiEmbedding.

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
            "id": "117393d5-2829-4181-9c44-07a2e84e39f9",
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

## create_genai_memory

Creates a GenaiMemory. Provide the unified GenaiMemory fields in the request body; they are mapped to the provider's API. Returns the created GenaiMemory.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiMemory" method="post" path="/genai/{connection_id}/memory" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_memory(request={
        "genai_memory": {
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "eb69d318-519c-4142-a112-9c034efda223",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-28T21:10:36.953Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
        },
        "connection_id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateGenaiMemoryRequest](../../models/operations/creategenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateGenaiMemoryResponse](../../models/operations/creategenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_genai_organization

Creates a GenaiOrganization. Provide the unified GenaiOrganization fields in the request body; they are mapped to the provider's API. Returns the created GenaiOrganization.

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
            "id": "28945522-a885-4f2b-bd82-b1f731e7fa41",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-30T03:54:28.619Z"),
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

Creates a GenaiPrompt. Provide the unified GenaiPrompt fields in the request body; they are mapped to the provider's API. Returns the created GenaiPrompt.

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
            "answers": [
                {
                    "confidence": 0.5384309098590165,
                    "id": "TeZpueFB",
                    "probabilities": [
                        {
                            "option": "veniam",
                            "probability": 0.05683182482607663,
                        },
                        {
                            "option": "comes",
                            "probability": 0.1404057613108307,
                        },
                    ],
                    "score": 0.05974147981032729,
                    "type": shared.GenaiAnswerType.CHOICE,
                    "value": "summisse",
                },
            ],
            "max_tokens": 0.4677782787475735,
            "mcp_authorization_token": "f45a6e93-7bed-49b4-a5c8-37a2ed2d58f4",
            "mcp_deferred_tools": [],
            "mcp_url": "https://unsung-dusk.info/",
            "messages": [
                {
                    "content": "Aegre repudiandae verecundia facere statua.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
                {
                    "content": "Speciosus xiphias soleo trepide crinis.",
                    "images": [],
                    "role": shared.Role.SYSTEM,
                },
            ],
            "questions": [
                {
                    "id": "KtvbYiEq",
                    "instructions": "Admiratio cura contabesco subvenio venustas architecto vacuus summopere.",
                    "options": [
                        "vulnero",
                        "quasi",
                        "tolero",
                    ],
                    "type": shared.GenaiQuestionType.BOOLEAN,
                },
                {
                    "id": "oV6IURtv",
                    "instructions": "Celer deleniti ventus ipsam tendo odit.",
                    "options": [
                        "nulla",
                        "aspicio",
                        "tero",
                    ],
                    "type": shared.GenaiQuestionType.CHOICE,
                },
                {
                    "id": "60dBZk2K",
                    "instructions": "Decretum vesica amet repudiandae.",
                    "options": [
                        "ducimus",
                        "civis",
                        "alter",
                    ],
                    "type": shared.GenaiQuestionType.BOOLEAN,
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

Creates a GenaiTask. Provide the unified GenaiTask fields in the request body; they are mapped to the provider's API. Returns the created GenaiTask.

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
            "completed_at": parse_datetime("2025-10-09T10:25:39.225Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "ea17fe45-401f-4207-86fe-75a9dadf818a",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-27T08:09:18.318Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-02T03:59:42.281Z"),
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

## get_genai_memory

Retrieves a single GenaiMemory by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiMemory" method="get" path="/genai/{connection_id}/memory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.get_genai_memory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetGenaiMemoryRequest](../../models/operations/getgenaimemoryrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetGenaiMemoryResponse](../../models/operations/getgenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_model

Retrieves a single GenaiModel by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single GenaiOrganization by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

## get_genai_skill

Retrieves a single GenaiSkill by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiSkill" method="get" path="/genai/{connection_id}/skill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.get_genai_skill(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_skill is not None

    # Handle response
    print(res.genai_skill)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetGenaiSkillRequest](../../models/operations/getgenaiskillrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetGenaiSkillResponse](../../models/operations/getgenaiskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_task

Retrieves a single GenaiTask by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

## list_genai_memories

Returns a list of GenaiMemories. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiMemories" method="get" path="/genai/{connection_id}/memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.list_genai_memories(request={
        "connection_id": "<id>",
    })

    assert res.genai_memories is not None

    # Handle response
    print(res.genai_memories)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListGenaiMemoriesRequest](../../models/operations/listgenaimemoriesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListGenaiMemoriesResponse](../../models/operations/listgenaimemoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_models

Returns a list of GenaiModels. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of GenaiOrganizations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

## list_genai_skills

Returns a list of GenaiSkills. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiSkills" method="get" path="/genai/{connection_id}/skill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.list_genai_skills(request={
        "connection_id": "<id>",
    })

    assert res.genai_skills is not None

    # Handle response
    print(res.genai_skills)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListGenaiSkillsRequest](../../models/operations/listgenaiskillsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListGenaiSkillsResponse](../../models/operations/listgenaiskillsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_tasks

Returns a list of GenaiTasks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

    res = unified_to.genai.patch_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "bb7bb3b8-3cd0-43ea-a107-d7422e90bc51",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-23T15:05:11.540Z"),
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

## patch_genai_memory

Updates the GenaiMemory identified by `id`. Provide the unified GenaiMemory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiMemory" method="patch" path="/genai/{connection_id}/memory/{id}" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.patch_genai_memory(request={
        "genai_memory": {
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "9f1e3989-5fe5-44dc-9bf2-c23d3778b207",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-28T21:10:36.955Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchGenaiMemoryRequest](../../models/operations/patchgenaimemoryrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchGenaiMemoryResponse](../../models/operations/patchgenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_organization

Updates the GenaiOrganization identified by `id`. Provide the unified GenaiOrganization fields to change in the request body.

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
            "id": "36e6744e-81a1-4236-8254-3dd6674d680d",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-30T03:54:28.621Z"),
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

## patch_genai_task

Updates the GenaiTask identified by `id`. Provide the unified GenaiTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiTask" method="patch" path="/genai/{connection_id}/task/{id}" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.patch_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-10-09T10:25:39.242Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "3fa23590-b09b-4da3-a103-75a00bc15765",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-27T08:09:18.330Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-02T03:59:42.289Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchGenaiTaskRequest](../../models/operations/patchgenaitaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchGenaiTaskResponse](../../models/operations/patchgenaitaskresponse.md)**

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

## remove_genai_memory

Deletes the GenaiMemory identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiMemory" method="delete" path="/genai/{connection_id}/memory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.remove_genai_memory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveGenaiMemoryRequest](../../models/operations/removegenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveGenaiMemoryResponse](../../models/operations/removegenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_organization

Deletes the GenaiOrganization identified by `id`.

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

## remove_genai_skill

Deletes the GenaiSkill identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiSkill" method="delete" path="/genai/{connection_id}/skill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.remove_genai_skill(request={
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
| `request`                                                                                | [operations.RemoveGenaiSkillRequest](../../models/operations/removegenaiskillrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveGenaiSkillResponse](../../models/operations/removegenaiskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_task

Deletes the GenaiTask identified by `id`.

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

    res = unified_to.genai.update_genai_agent(request={
        "genai_agent": {
            "created_at": parse_datetime("2020-12-18T02:23:33.723Z"),
            "description": "Assentator tero sequi.",
            "id": "bb7bb3b8-3cd0-43ea-a107-d7422e90bc51",
            "instructions": "Delicate tabella addo vita ver auctus corrumpo. Conscendo auctus maiores astrum sulum aufero bis stella. Non varius sto solus admitto vado suggero theatrum.",
            "is_active": False,
            "name": "daughter with",
            "updated_at": parse_datetime("2025-10-23T15:05:11.540Z"),
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

## update_genai_memory

Updates the GenaiMemory identified by `id`. Provide the unified GenaiMemory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiMemory" method="put" path="/genai/{connection_id}/memory/{id}" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.update_genai_memory(request={
        "genai_memory": {
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "9f1e3989-5fe5-44dc-9bf2-c23d3778b207",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-28T21:10:36.955Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateGenaiMemoryRequest](../../models/operations/updategenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateGenaiMemoryResponse](../../models/operations/updategenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_organization

Updates the GenaiOrganization identified by `id`. Provide the unified GenaiOrganization fields to change in the request body.

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
            "id": "36e6744e-81a1-4236-8254-3dd6674d680d",
            "is_active": False,
            "name": "officially about",
            "updated_at": parse_datetime("2023-01-30T03:54:28.621Z"),
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

## update_genai_task

Updates the GenaiTask identified by `id`. Provide the unified GenaiTask fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiTask" method="put" path="/genai/{connection_id}/task/{id}" example="genai_task" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.update_genai_task(request={
        "genai_task": {
            "completed_at": parse_datetime("2025-10-09T10:25:39.242Z"),
            "created_at": parse_datetime("2020-10-25T20:19:33.247Z"),
            "files_changed": 19.0,
            "id": "3fa23590-b09b-4da3-a103-75a00bc15765",
            "instructions": "Benigne canonicus officiis solvo adsidue deleo angustus.",
            "lines_added": 244.0,
            "lines_deleted": 118.0,
            "messages": [
                {
                    "content": "Stultus esse cursim stabilis tenetur amet contigo tristis.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
            ],
            "name": "connect multi-byte port",
            "pullrequest_url": "https://github.com/berenice.satterfield/joshingly-ignorance/pull/383",
            "repo_url": "https://github.com/berenice.satterfield/joshingly-ignorance",
            "source_branch_identifier": "main",
            "started_at": parse_datetime("2024-05-27T08:09:18.330Z"),
            "status": shared.GenaiTaskStatus.BLOCKED,
            "summary": "Cur aeternus cogito vesper.",
            "target_branch_identifier": "agent/joshingly-ignorance",
            "tokens_used": 2165.0,
            "updated_at": parse_datetime("2023-03-02T03:59:42.289Z"),
            "web_url": "https://inexperienced-adrenalin.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_task is not None

    # Handle response
    print(res.genai_task)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateGenaiTaskRequest](../../models/operations/updategenaitaskrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateGenaiTaskResponse](../../models/operations/updategenaitaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |