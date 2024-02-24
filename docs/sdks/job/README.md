# Job
(*job*)

### Available Operations

* [create_ats_job](#create_ats_job) - Create a job
* [get_ats_job](#get_ats_job) - Retrieve a job
* [list_ats_jobs](#list_ats_jobs) - List all jobs
* [patch_ats_job](#patch_ats_job) - Update a job
* [remove_ats_job](#remove_ats_job) - Remove a job
* [update_ats_job](#update_ats_job) - Update a job

## create_ats_job

Create a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsJobRequest(
    connection_id='<value>',
)

res = s.job.create_ats_job(req, operations.CreateAtsJobSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateAtsJobRequest](../../models/operations/createatsjobrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.CreateAtsJobSecurity](../../models/operations/createatsjobsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.CreateAtsJobResponse](../../models/operations/createatsjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_job

Retrieve a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsJobRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.job.get_ats_job(req, operations.GetAtsJobSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAtsJobRequest](../../models/operations/getatsjobrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetAtsJobSecurity](../../models/operations/getatsjobsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetAtsJobResponse](../../models/operations/getatsjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_jobs

List all jobs

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsJobsRequest(
    connection_id='<value>',
)

res = s.job.list_ats_jobs(req, operations.ListAtsJobsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListAtsJobsRequest](../../models/operations/listatsjobsrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ListAtsJobsSecurity](../../models/operations/listatsjobssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ListAtsJobsResponse](../../models/operations/listatsjobsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_job

Update a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsJobRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.job.patch_ats_job(req, operations.PatchAtsJobSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchAtsJobRequest](../../models/operations/patchatsjobrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.PatchAtsJobSecurity](../../models/operations/patchatsjobsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.PatchAtsJobResponse](../../models/operations/patchatsjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_job

Remove a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsJobRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.job.remove_ats_job(req, operations.RemoveAtsJobSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveAtsJobRequest](../../models/operations/removeatsjobrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.RemoveAtsJobSecurity](../../models/operations/removeatsjobsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.RemoveAtsJobResponse](../../models/operations/removeatsjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_job

Update a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsJobRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.job.update_ats_job(req, operations.UpdateAtsJobSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateAtsJobRequest](../../models/operations/updateatsjobrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.UpdateAtsJobSecurity](../../models/operations/updateatsjobsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.UpdateAtsJobResponse](../../models/operations/updateatsjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
