# call

### Available Operations

* [get_uc_connection_id_call](#get_uc_connection_id_call) - List all calls

## get_uc_connection_id_call

List all calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDCallRequest(
    agent_id='reiciendis',
    connection_id='repellat',
    contact_id='nulla',
    limit=6711.16,
    offset=6176.57,
    order='accusamus',
    query='doloremque',
    sort='nisi',
    updated_gte=dateutil.parser.parse('2021-02-24').date(),
)

res = s.call.get_uc_connection_id_call(req, operations.GetUcConnectionIDCallSecurity(
    jwt="",
))

if res.uc_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUcConnectionIDCallRequest](../../models/operations/getucconnectionidcallrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetUcConnectionIDCallSecurity](../../models/operations/getucconnectionidcallsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetUcConnectionIDCallResponse](../../models/operations/getucconnectionidcallresponse.md)**

