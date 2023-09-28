# Apicall
(*apicall*)

### Available Operations

* [get_unified_apicall](#get_unified_apicall) - Returns API Calls
* [get_unified_apicall_id](#get_unified_apicall_id) - Retrieve specific API Call by its ID

## get_unified_apicall

Returns API Calls

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

req = operations.GetUnifiedApicallRequest(
    connection_id='delectus green Hybrid',
    created_lte=dateutil.parser.isoparse('2021-04-02T21:36:49.952Z'),
    env='Fantastic Iodine indexing',
    error=False,
    external_xref='Music',
    integration_type='Soft',
    limit=2390.64,
    offset=3757.34,
    order='mobile envisioneer',
    sort='North payment opposite',
    updated_gte=dateutil.parser.isoparse('2021-08-11T16:18:13.644Z'),
)

res = s.apicall.get_unified_apicall(req)

if res.api_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetUnifiedApicallRequest](../../models/operations/getunifiedapicallrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetUnifiedApicallResponse](../../models/operations/getunifiedapicallresponse.md)**


## get_unified_apicall_id

Retrieve specific API Call by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedApicallIDRequest(
    id='<ID>',
)

res = s.apicall.get_unified_apicall_id(req)

if res.api_call is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetUnifiedApicallIDRequest](../../models/operations/getunifiedapicallidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetUnifiedApicallIDResponse](../../models/operations/getunifiedapicallidresponse.md)**

