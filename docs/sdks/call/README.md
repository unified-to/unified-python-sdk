# Call
(*call*)

### Available Operations

* [get_uc_connection_id_call](#get_uc_connection_id_call) - List all calls

## get_uc_connection_id_call

List all calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUcConnectionIDCallRequest(
    connection_id='Directives',
)

res = s.call.get_uc_connection_id_call(req)

if res.uc_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetUcConnectionIDCallRequest](../../models/operations/getucconnectionidcallrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetUcConnectionIDCallResponse](../../models/operations/getucconnectionidcallresponse.md)**

