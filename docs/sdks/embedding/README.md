# Embedding

## Overview

### Available Operations

* [create_genai_embedding](#create_genai_embedding) - Create an embedding

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

    res = unified_to.embedding.create_genai_embedding(request={
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