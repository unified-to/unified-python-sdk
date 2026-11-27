# Prompt

## Overview

### Available Operations

* [create_genai_prompt](#create_genai_prompt) - Create a prompt

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

    res = unified_to.prompt.create_genai_prompt(request={
        "genai_prompt": {
            "answers": [
                {
                    "confidence": 0.5384309098590165,
                    "id": "DiYHdUlr",
                    "probabilities": [
                        {
                            "option": "ulterius",
                            "probability": 0.05683182482607663,
                        },
                        {
                            "option": "spiculum",
                            "probability": 0.1404057613108307,
                        },
                    ],
                    "score": 0.05974147981032729,
                    "type": shared.GenaiAnswerType.CHOICE,
                    "value": "vilicus",
                },
            ],
            "has_thread": False,
            "id": "lGiOgAB6MLc1sMVUZnBJtXQG",
            "max_tokens": 0.4677782787475735,
            "mcp_authorization_token": "45c837a2-ed2d-458f-b4bc-782f4a6b065b",
            "mcp_deferred_tools": [],
            "mcp_url": "https://svelte-offset.net",
            "messages": [
                {
                    "content": "Facere statua depulso speciosus xiphias soleo trepide crinis crapula balbus.",
                    "images": [],
                    "role": shared.Role.ASSISTANT,
                },
                {
                    "content": "Circumvenio una demitto ventito chirographum culpo vos cohibeo complectus speciosus.",
                    "images": [],
                    "role": shared.Role.SYSTEM,
                },
            ],
            "questions": [
                {
                    "id": "9SIZCOoV",
                    "instructions": "Supellex verbera universe.",
                    "options": [
                        "dens",
                        "doloribus",
                        "degusto",
                    ],
                    "type": shared.GenaiQuestionType.BOOLEAN,
                },
                {
                    "id": "gsUyLAAa",
                    "instructions": "Amplexus abundans caelestis patrocinor vulgivagus condico adduco tego apostolus.",
                    "options": [
                        "decretum",
                        "vesica",
                        "amet",
                    ],
                    "type": shared.GenaiQuestionType.CHOICE,
                },
                {
                    "id": "Dwh6TeZp",
                    "instructions": "Capio somnus pauper summisse veniam comes.",
                    "options": [
                        "depulso",
                        "deficio",
                        "sustineo",
                    ],
                    "type": shared.GenaiQuestionType.BOOLEAN,
                },
            ],
            "responses": [
                "Vereor pecco avarus derideo sumptus.",
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