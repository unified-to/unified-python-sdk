# apicall

### Available Operations

* [get_unified_apicall](#get_unified_apicall) - Returns API Calls
* [get_unified_apicall_id](#get_unified_apicall_id) - Retrieve specific API Call by its ID

## get_unified_apicall

Returns API Calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallRequest(
    connection_id='voluptate',
    created_lte=dateutil.parser.parse('2022-04-12').date(),
    env='eaque',
    error=False,
    external_xref='pariatur',
    integration_type='nemo',
    limit=9755.22,
    offset=166.27,
    order='fugiat',
    sort='amet',
    updated_gte=dateutil.parser.parse('2022-03-27').date(),
)

res = s.apicall.get_unified_apicall(req, operations.GetUnifiedApicallSecurity(
    jwt="",
))

if res.api_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedApicallSecurity](../../models/operations/getunifiedapicallsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**


## get_unified_apicall_id

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedApicallIDRequest(
    id='5fbb2587-0532-402c-b3d5-fe9b90c28909',
)

res = s.apicall.get_unified_apicall_id(req, operations.GetUnifiedApicallIDSecurity(
    jwt="",
))

if res.api_call is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedApicallIDRequest](../../models/operations/getunifiedapicallidrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetUnifiedApicallIDSecurity](../../models/operations/getunifiedapicallidsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedApicallIDResponse](../../models/operations/getunifiedapicallidresponse.md)**

