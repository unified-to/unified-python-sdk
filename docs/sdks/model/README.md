# Model

## Overview

### Available Operations

* [get_genai_model2](#get_genai_model2) - Retrieve a model
* [list_genai_models2](#list_genai_models2) - List all models

## get_genai_model2

Retrieve a model

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiModel2" method="get" path="/genai/{connection_id}/model/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.model.get_genai_model2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_model is not None

    # Handle response
    print(res.genai_model)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetGenaiModel2Request](../../models/operations/getgenaimodel2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetGenaiModel2Response](../../models/operations/getgenaimodel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_models2

List all models

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiModels2" method="get" path="/genai/{connection_id}/model" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.model.list_genai_models2(request={
        "connection_id": "<id>",
    })

    assert res.genai_models is not None

    # Handle response
    print(res.genai_models)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListGenaiModels2Request](../../models/operations/listgenaimodels2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListGenaiModels2Response](../../models/operations/listgenaimodels2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |