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
    agent_id='Directives',
    connection_id='female than',
    contact_id='reintermediate Enid Applications',
    limit=1980.39,
    offset=3478,
    order='white Oklahoma Functionality',
    query='pricing whether Hillsboro',
    sort='Wooden desensitize SCSI',
    updated_gte=dateutil.parser.isoparse('2021-11-03T12:40:46.997Z'),
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

