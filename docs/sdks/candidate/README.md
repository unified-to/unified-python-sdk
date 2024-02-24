# Candidate
(*candidate*)

### Available Operations

* [create_ats_candidate](#create_ats_candidate) - Create a candidate
* [get_ats_candidate](#get_ats_candidate) - Retrieve a candidate
* [list_ats_candidates](#list_ats_candidates) - List all candidates
* [patch_ats_candidate](#patch_ats_candidate) - Update a candidate
* [remove_ats_candidate](#remove_ats_candidate) - Remove a candidate
* [update_ats_candidate](#update_ats_candidate) - Update a candidate

## create_ats_candidate

Create a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsCandidateRequest(
    connection_id='<value>',
)

res = s.candidate.create_ats_candidate(req, operations.CreateAtsCandidateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateAtsCandidateRequest](../../models/operations/createatscandidaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateAtsCandidateSecurity](../../models/operations/createatscandidatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateAtsCandidateResponse](../../models/operations/createatscandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_candidate

Retrieve a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsCandidateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.candidate.get_ats_candidate(req, operations.GetAtsCandidateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetAtsCandidateRequest](../../models/operations/getatscandidaterequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetAtsCandidateSecurity](../../models/operations/getatscandidatesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetAtsCandidateResponse](../../models/operations/getatscandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_candidates

List all candidates

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsCandidatesRequest(
    connection_id='<value>',
)

res = s.candidate.list_ats_candidates(req, operations.ListAtsCandidatesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_candidates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListAtsCandidatesRequest](../../models/operations/listatscandidatesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListAtsCandidatesSecurity](../../models/operations/listatscandidatessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListAtsCandidatesResponse](../../models/operations/listatscandidatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_candidate

Update a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsCandidateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.candidate.patch_ats_candidate(req, operations.PatchAtsCandidateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchAtsCandidateRequest](../../models/operations/patchatscandidaterequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PatchAtsCandidateSecurity](../../models/operations/patchatscandidatesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PatchAtsCandidateResponse](../../models/operations/patchatscandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_candidate

Remove a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsCandidateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.candidate.remove_ats_candidate(req, operations.RemoveAtsCandidateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveAtsCandidateRequest](../../models/operations/removeatscandidaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.RemoveAtsCandidateSecurity](../../models/operations/removeatscandidatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.RemoveAtsCandidateResponse](../../models/operations/removeatscandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_candidate

Update a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsCandidateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.candidate.update_ats_candidate(req, operations.UpdateAtsCandidateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateAtsCandidateRequest](../../models/operations/updateatscandidaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateAtsCandidateSecurity](../../models/operations/updateatscandidatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateAtsCandidateResponse](../../models/operations/updateatscandidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
