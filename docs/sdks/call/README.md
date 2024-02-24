# Call
(*call*)

### Available Operations

* [list_uc_calls](#list_uc_calls) - List all calls

## list_uc_calls

List all calls

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUcCallsRequest(
    connection_id='<value>',
)

res = s.call.list_uc_calls(req, operations.ListUcCallsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_calls is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListUcCallsRequest](../../models/operations/listuccallsrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ListUcCallsSecurity](../../models/operations/listuccallssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ListUcCallsResponse](../../models/operations/listuccallsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
