# Call
(*.call*)

### Available Operations

* [list_uc_calls](#list_uc_calls) - List all calls

## list_uc_calls

List all calls

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListUcCallsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.call.list_uc_calls(req)

if res.uc_calls is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcCallsRequest](../../models/operations/listuccallsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListUcCallsResponse](../../models/operations/listuccallsresponse.md)**

