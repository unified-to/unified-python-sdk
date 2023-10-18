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
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateAtsJobRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(),
        ],
        compensation=[
            shared.AtsCompensation(
                type=shared.AtsCompensationType.SALARY,
            ),
        ],
        departments=[
            'Loan',
        ],
        hiring_manager_ids=[
            'driver',
        ],
        public_job_urls=[
            'Transmasculine',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'Mini',
        ],
    ),
    connection_id='health',
)

res = s.job.create_ats_job(req)

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateAtsJobRequest](../../models/operations/createatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateAtsJobResponse](../../models/operations/createatsjobresponse.md)**


## get_ats_job

Retrieve a job

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsJobRequest(
    connection_id='Southwest',
    fields_=[
        'panel',
    ],
    id='<ID>',
)

res = s.job.get_ats_job(req)

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetAtsJobRequest](../../models/operations/getatsjobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetAtsJobResponse](../../models/operations/getatsjobresponse.md)**


## list_ats_jobs

List all jobs

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

req = operations.ListAtsJobsRequest(
    connection_id='firmware',
    fields_=[
        'Praseodymium',
    ],
)

res = s.job.list_ats_jobs(req)

if res.ats_jobs is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListAtsJobsRequest](../../models/operations/listatsjobsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListAtsJobsResponse](../../models/operations/listatsjobsresponse.md)**


## patch_ats_job

Update a job

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

req = operations.PatchAtsJobRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(),
        ],
        compensation=[
            shared.AtsCompensation(
                type=shared.AtsCompensationType.BONUS,
            ),
        ],
        departments=[
            'indigo',
        ],
        hiring_manager_ids=[
            'Bedfordshire',
        ],
        public_job_urls=[
            'North',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'mainland',
        ],
    ),
    connection_id='microchip',
    id='<ID>',
)

res = s.job.patch_ats_job(req)

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchAtsJobRequest](../../models/operations/patchatsjobrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchAtsJobResponse](../../models/operations/patchatsjobresponse.md)**


## remove_ats_job

Remove a job

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAtsJobRequest(
    connection_id='Northeast',
    id='<ID>',
)

res = s.job.remove_ats_job(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RemoveAtsJobRequest](../../models/operations/removeatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.RemoveAtsJobResponse](../../models/operations/removeatsjobresponse.md)**


## update_ats_job

Update a job

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

req = operations.UpdateAtsJobRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(),
        ],
        compensation=[
            shared.AtsCompensation(
                type=shared.AtsCompensationType.EQUITY,
            ),
        ],
        departments=[
            'Plastic',
        ],
        hiring_manager_ids=[
            'West',
        ],
        public_job_urls=[
            'Direct',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'SMS',
        ],
    ),
    connection_id='asperiores',
    id='<ID>',
)

res = s.job.update_ats_job(req)

if res.ats_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateAtsJobRequest](../../models/operations/updateatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateAtsJobResponse](../../models/operations/updateatsjobresponse.md)**

