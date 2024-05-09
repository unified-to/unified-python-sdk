# Model
(*model*)

### Available Operations

* [list_genai_models](#list_genai_models) - List all models

## list_genai_models

List all models

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.model.list_genai_models(request=operations.ListGenaiModelsRequest(
    connection_id='<value>',
))

if res.genai_models is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListGenaiModelsRequest](../../models/operations/listgenaimodelsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListGenaiModelsResponse](../../models/operations/listgenaimodelsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
