# Prompt

## Overview

### Available Operations

* [create_genai_prompt](#create_genai_prompt) - Create a prompt

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

    res = unified_to.prompt.create_genai_prompt(request={
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