# Applicationstatus
(*applicationstatus*)

### Available Operations

* [list_ats_applicationstatuses](#list_ats_applicationstatuses) - List all application statuses

## list_ats_applicationstatuses

List all application statuses

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListAtsApplicationstatusesRequest(
    connection_id='string',
)

res = s.applicationstatus.list_ats_applicationstatuses(req)

if res.ats_statuses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAtsApplicationstatusesRequest](../../models/operations/listatsapplicationstatusesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.ListAtsApplicationstatusesResponse](../../models/operations/listatsapplicationstatusesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
