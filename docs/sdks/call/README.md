# Call

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
    agent_id='a',
    connection_id='iste',
    contact_id='dicta',
    limit=5524.39,
    offset=3563.15,
    order='dolore',
    query='modi',
    sort='itaque',
    updated_gte=dateutil.parser.isoparse('2022-03-15T19:59:59.350Z'),
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

