# Genai

## Overview

### Available Operations

* [create_genai_embedding](#create_genai_embedding) - Create an embedding
* [create_genai_prompt](#create_genai_prompt) - Create a prompt
* [get_genai_model](#get_genai_model) - Retrieve a model
* [list_genai_models](#list_genai_models) - List all models

## create_genai_embedding

Create an embedding

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiEmbedding" method="post" path="/genai/{connection_id}/embedding" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_embedding(request={
        "genai_embedding": {},
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

## create_genai_prompt

Create a prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiPrompt" method="post" path="/genai/{connection_id}/prompt" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.genai.create_genai_prompt(request={
        "genai_prompt": {},
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