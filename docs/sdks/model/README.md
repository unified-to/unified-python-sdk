# Model
(*model*)

## Overview

### Available Operations

* [list_genai_models](#list_genai_models) - List all models

## list_genai_models

List all models

### Example Usage

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = unified_to.model.list_genai_models(request={
        "connection_id": "<value>",
    })

    if res.genai_models is not None:
        # handle response
        pass

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