# Job
(*job*)

## Overview

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
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.create_ats_job(request={
    "connection_id": "<value>",
})

if res.ats_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateAtsJobRequest](../../models/operations/createatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateAtsJobResponse](../../models/operations/createatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_job

Retrieve a job

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.get_ats_job(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.ats_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetAtsJobRequest](../../models/operations/getatsjobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetAtsJobResponse](../../models/operations/getatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_jobs

List all jobs

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.list_ats_jobs(request={
    "connection_id": "<value>",
})

if res.ats_jobs is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListAtsJobsRequest](../../models/operations/listatsjobsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListAtsJobsResponse](../../models/operations/listatsjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_job

Update a job

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.patch_ats_job(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.ats_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchAtsJobRequest](../../models/operations/patchatsjobrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.PatchAtsJobResponse](../../models/operations/patchatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_job

Remove a job

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.remove_ats_job(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RemoveAtsJobRequest](../../models/operations/removeatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.RemoveAtsJobResponse](../../models/operations/removeatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_job

Update a job

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.job.update_ats_job(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.ats_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateAtsJobRequest](../../models/operations/updateatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateAtsJobResponse](../../models/operations/updateatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |