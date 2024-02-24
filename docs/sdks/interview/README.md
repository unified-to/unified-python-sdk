# Interview
(*interview*)

### Available Operations

* [create_ats_interview](#create_ats_interview) - Create a interview
* [get_ats_interview](#get_ats_interview) - Retrieve a interview
* [list_ats_interviews](#list_ats_interviews) - List all interviews
* [patch_ats_interview](#patch_ats_interview) - Update a interview
* [remove_ats_interview](#remove_ats_interview) - Remove a interview
* [update_ats_interview](#update_ats_interview) - Update a interview

## create_ats_interview

Create a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsInterviewRequest(
    connection_id='<value>',
)

res = s.interview.create_ats_interview(req, operations.CreateAtsInterviewSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_interview is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateAtsInterviewRequest](../../models/operations/createatsinterviewrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateAtsInterviewSecurity](../../models/operations/createatsinterviewsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateAtsInterviewResponse](../../models/operations/createatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_interview

Retrieve a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.interview.get_ats_interview(req, operations.GetAtsInterviewSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_interview is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetAtsInterviewRequest](../../models/operations/getatsinterviewrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetAtsInterviewSecurity](../../models/operations/getatsinterviewsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetAtsInterviewResponse](../../models/operations/getatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_interviews

List all interviews

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsInterviewsRequest(
    connection_id='<value>',
)

res = s.interview.list_ats_interviews(req, operations.ListAtsInterviewsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_interviews is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListAtsInterviewsRequest](../../models/operations/listatsinterviewsrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListAtsInterviewsSecurity](../../models/operations/listatsinterviewssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListAtsInterviewsResponse](../../models/operations/listatsinterviewsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_interview

Update a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.interview.patch_ats_interview(req, operations.PatchAtsInterviewSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_interview is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchAtsInterviewRequest](../../models/operations/patchatsinterviewrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PatchAtsInterviewSecurity](../../models/operations/patchatsinterviewsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PatchAtsInterviewResponse](../../models/operations/patchatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_interview

Remove a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.interview.remove_ats_interview(req, operations.RemoveAtsInterviewSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveAtsInterviewRequest](../../models/operations/removeatsinterviewrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.RemoveAtsInterviewSecurity](../../models/operations/removeatsinterviewsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.RemoveAtsInterviewResponse](../../models/operations/removeatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_interview

Update a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.interview.update_ats_interview(req, operations.UpdateAtsInterviewSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_interview is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateAtsInterviewRequest](../../models/operations/updateatsinterviewrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateAtsInterviewSecurity](../../models/operations/updateatsinterviewsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateAtsInterviewResponse](../../models/operations/updateatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
