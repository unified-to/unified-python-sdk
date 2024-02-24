# Apicall
(*apicall*)

### Available Operations

* [get_unified_apicall](#get_unified_apicall) - Retrieve specific API Call by its ID
* [list_unified_apicalls](#list_unified_apicalls) - Returns API Calls

## get_unified_apicall

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallRequest(
    id='<id>',
)

res = s.apicall.get_unified_apicall(req, operations.GetUnifiedApicallSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.api_call is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedApicallSecurity](../../models/operations/getunifiedapicallsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_apicalls

Returns API Calls

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedApicallsRequest()

res = s.apicall.list_unified_apicalls(req, operations.ListUnifiedApicallsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.api_calls is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListUnifiedApicallsRequest](../../models/operations/listunifiedapicallsrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ListUnifiedApicallsSecurity](../../models/operations/listunifiedapicallssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ListUnifiedApicallsResponse](../../models/operations/listunifiedapicallsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
