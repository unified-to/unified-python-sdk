# Interview
(*interview*)

### Available Operations

* [create_ats_interview](#create_ats_interview) - Create an interview
* [get_ats_interview](#get_ats_interview) - Retrieve an interview
* [list_ats_interviews](#list_ats_interviews) - List all interviews
* [patch_ats_interview](#patch_ats_interview) - Update an interview
* [remove_ats_interview](#remove_ats_interview) - Remove an interview
* [update_ats_interview](#update_ats_interview) - Update an interview

## create_ats_interview

Create an interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.create_ats_interview(request=operations.CreateAtsInterviewRequest(
    connection_id='<value>',
))

if res.ats_interview is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsInterviewRequest](../../models/operations/createatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAtsInterviewResponse](../../models/operations/createatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ats_interview

Retrieve an interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.get_ats_interview(request=operations.GetAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_interview is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsInterviewRequest](../../models/operations/getatsinterviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetAtsInterviewResponse](../../models/operations/getatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_ats_interviews

List all interviews

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.list_ats_interviews(request=operations.ListAtsInterviewsRequest(
    connection_id='<value>',
))

if res.ats_interviews is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsInterviewsRequest](../../models/operations/listatsinterviewsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListAtsInterviewsResponse](../../models/operations/listatsinterviewsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_ats_interview

Update an interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.patch_ats_interview(request=operations.PatchAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_interview is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsInterviewRequest](../../models/operations/patchatsinterviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchAtsInterviewResponse](../../models/operations/patchatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## remove_ats_interview

Remove an interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.remove_ats_interview(request=operations.RemoveAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsInterviewRequest](../../models/operations/removeatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsInterviewResponse](../../models/operations/removeatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_ats_interview

Update an interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)


res = s.interview.update_ats_interview(request=operations.UpdateAtsInterviewRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_interview is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsInterviewRequest](../../models/operations/updateatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateAtsInterviewResponse](../../models/operations/updateatsinterviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
