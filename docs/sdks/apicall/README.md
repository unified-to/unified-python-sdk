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
    connection_id='perspiciatis',
    created_lte=dateutil.parser.isoparse('2022-03-20T23:16:34.777Z'),
    env='consequuntur',
    error=False,
    external_xref='blanditiis',
    integration_type='error',
    limit=503.7,
    offset=5772.29,
    order='rerum',
    sort='adipisci',
    updated_gte=dateutil.parser.isoparse('2020-03-14T00:51:21.656Z'),
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
    id='49a8d9cb-f486-4333-a3f9-b77f3a410067',
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

