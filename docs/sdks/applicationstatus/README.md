# Applicationstatus
(*applicationstatus*)

### Available Operations

* [list_ats_applicationstatuses](#list_ats_applicationstatuses) - List all application statuses

## list_ats_applicationstatuses

List all application statuses

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsApplicationstatusesRequest(
    connection_id='<value>',
)

res = s.applicationstatus.list_ats_applicationstatuses(req, operations.ListAtsApplicationstatusesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_statuses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAtsApplicationstatusesRequest](../../models/operations/listatsapplicationstatusesrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.ListAtsApplicationstatusesSecurity](../../models/operations/listatsapplicationstatusessecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.ListAtsApplicationstatusesResponse](../../models/operations/listatsapplicationstatusesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
