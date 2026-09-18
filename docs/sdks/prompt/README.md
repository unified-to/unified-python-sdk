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