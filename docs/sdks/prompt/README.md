# Prompt
(*prompt*)

### Available Operations

* [create_genai_prompt](#create_genai_prompt) - Create a prompt

## create_genai_prompt

Create a prompt

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.prompt.create_genai_prompt(request=operations.CreateGenaiPromptRequest(
    connection_id='<value>',
))

if res.genai_prompt is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateGenaiPromptRequest](../../models/operations/creategenaipromptrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateGenaiPromptResponse](../../models/operations/creategenaipromptresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
