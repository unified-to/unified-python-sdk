# Ats
(*ats*)

### Available Operations

* [create_ats_application](#create_ats_application) - Create an application
* [create_ats_candidate](#create_ats_candidate) - Create a candidate
* [create_ats_interview](#create_ats_interview) - Create a interview
* [create_ats_job](#create_ats_job) - Create a job
* [create_ats_scorecard](#create_ats_scorecard) - Create a scorecard
* [get_ats_application](#get_ats_application) - Retrieve an application
* [get_ats_candidate](#get_ats_candidate) - Retrieve a candidate
* [get_ats_interview](#get_ats_interview) - Retrieve a interview
* [get_ats_job](#get_ats_job) - Retrieve a job
* [get_ats_scorecard](#get_ats_scorecard) - Retrieve a scorecard
* [list_ats_applications](#list_ats_applications) - List all applications
* [list_ats_candidates](#list_ats_candidates) - List all candidates
* [list_ats_interviews](#list_ats_interviews) - List all interviews
* [list_ats_jobs](#list_ats_jobs) - List all jobs
* [list_ats_scorecards](#list_ats_scorecards) - List all scorecards
* [patch_ats_application](#patch_ats_application) - Update an application
* [patch_ats_candidate](#patch_ats_candidate) - Update a candidate
* [patch_ats_interview](#patch_ats_interview) - Update a interview
* [patch_ats_job](#patch_ats_job) - Update a job
* [patch_ats_scorecard](#patch_ats_scorecard) - Update a scorecard
* [remove_ats_application](#remove_ats_application) - Remove an application
* [remove_ats_candidate](#remove_ats_candidate) - Remove a candidate
* [remove_ats_interview](#remove_ats_interview) - Remove a interview
* [remove_ats_job](#remove_ats_job) - Remove a job
* [remove_ats_scorecard](#remove_ats_scorecard) - Remove a scorecard
* [update_ats_application](#update_ats_application) - Update an application
* [update_ats_candidate](#update_ats_candidate) - Update a candidate
* [update_ats_interview](#update_ats_interview) - Update a interview
* [update_ats_job](#update_ats_job) - Update a job
* [update_ats_scorecard](#update_ats_scorecard) - Update a scorecard

## create_ats_application

Create an application

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

req = operations.CreateAtsApplicationRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='string',
)

res = s.ats.create_ats_application(req)

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAtsApplicationRequest](../../models/operations/createatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateAtsApplicationResponse](../../models/operations/createatsapplicationresponse.md)**


## create_ats_candidate

Create a candidate

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

req = operations.CreateAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Robin_Feeney@hotmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
)

res = s.ats.create_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsCandidateRequest](../../models/operations/createatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAtsCandidateResponse](../../models/operations/createatscandidateresponse.md)**


## create_ats_interview

Create a interview

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

req = operations.CreateAtsInterviewRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'string',
        ],
    ),
    connection_id='string',
)

res = s.ats.create_ats_interview(req)

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
            'string',
        ],
        hiring_manager_ids=[
            'string',
        ],
        public_job_urls=[
            'string',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'string',
        ],
    ),
    connection_id='string',
)

res = s.ats.create_ats_job(req)

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


## create_ats_scorecard

Create a scorecard

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

req = operations.CreateAtsScorecardRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='string',
)

res = s.ats.create_ats_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsScorecardRequest](../../models/operations/createatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAtsScorecardResponse](../../models/operations/createatsscorecardresponse.md)**


## get_ats_application

Retrieve an application

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsApplicationRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
)

res = s.ats.get_ats_application(req)

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAtsApplicationRequest](../../models/operations/getatsapplicationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetAtsApplicationResponse](../../models/operations/getatsapplicationresponse.md)**


## get_ats_candidate

Retrieve a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsCandidateRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
)

res = s.ats.get_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsCandidateRequest](../../models/operations/getatscandidaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetAtsCandidateResponse](../../models/operations/getatscandidateresponse.md)**


## get_ats_interview

Retrieve a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsInterviewRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
)

res = s.ats.get_ats_interview(req)

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
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
)

res = s.ats.get_ats_job(req)

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


## get_ats_scorecard

Retrieve a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsScorecardRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
    id='<ID>',
)

res = s.ats.get_ats_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsScorecardRequest](../../models/operations/getatsscorecardrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetAtsScorecardResponse](../../models/operations/getatsscorecardresponse.md)**


## list_ats_applications

List all applications

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

req = operations.ListAtsApplicationsRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
)

res = s.ats.list_ats_applications(req)

if res.ats_applications is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAtsApplicationsRequest](../../models/operations/listatsapplicationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListAtsApplicationsResponse](../../models/operations/listatsapplicationsresponse.md)**


## list_ats_candidates

List all candidates

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

req = operations.ListAtsCandidatesRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
)

res = s.ats.list_ats_candidates(req)

if res.ats_candidates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsCandidatesRequest](../../models/operations/listatscandidatesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListAtsCandidatesResponse](../../models/operations/listatscandidatesresponse.md)**


## list_ats_interviews

List all interviews

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

req = operations.ListAtsInterviewsRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
)

res = s.ats.list_ats_interviews(req)

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
    connection_id='string',
    fields_=[
        'string',
    ],
)

res = s.ats.list_ats_jobs(req)

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


## list_ats_scorecards

List all scorecards

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

req = operations.ListAtsScorecardsRequest(
    connection_id='string',
    fields_=[
        'string',
    ],
)

res = s.ats.list_ats_scorecards(req)

if res.ats_scorecards is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsScorecardsRequest](../../models/operations/listatsscorecardsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListAtsScorecardsResponse](../../models/operations/listatsscorecardsresponse.md)**


## patch_ats_application

Update an application

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

req = operations.PatchAtsApplicationRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.patch_ats_application(req)

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchAtsApplicationRequest](../../models/operations/patchatsapplicationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PatchAtsApplicationResponse](../../models/operations/patchatsapplicationresponse.md)**


## patch_ats_candidate

Update a candidate

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

req = operations.PatchAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Tracy.Collins13@gmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.patch_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsCandidateRequest](../../models/operations/patchatscandidaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchAtsCandidateResponse](../../models/operations/patchatscandidateresponse.md)**


## patch_ats_interview

Update a interview

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

req = operations.PatchAtsInterviewRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.patch_ats_interview(req)

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
            'string',
        ],
        hiring_manager_ids=[
            'string',
        ],
        public_job_urls=[
            'string',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.patch_ats_job(req)

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


## patch_ats_scorecard

Update a scorecard

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

req = operations.PatchAtsScorecardRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.patch_ats_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsScorecardRequest](../../models/operations/patchatsscorecardrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchAtsScorecardResponse](../../models/operations/patchatsscorecardresponse.md)**


## remove_ats_application

Remove an application

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAtsApplicationRequest(
    connection_id='string',
    id='<ID>',
)

res = s.ats.remove_ats_application(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveAtsApplicationRequest](../../models/operations/removeatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RemoveAtsApplicationResponse](../../models/operations/removeatsapplicationresponse.md)**


## remove_ats_candidate

Remove a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAtsCandidateRequest(
    connection_id='string',
    id='<ID>',
)

res = s.ats.remove_ats_candidate(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsCandidateRequest](../../models/operations/removeatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsCandidateResponse](../../models/operations/removeatscandidateresponse.md)**


## remove_ats_interview

Remove a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAtsInterviewRequest(
    connection_id='string',
    id='<ID>',
)

res = s.ats.remove_ats_interview(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsInterviewRequest](../../models/operations/removeatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsInterviewResponse](../../models/operations/removeatsinterviewresponse.md)**


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
    connection_id='string',
    id='<ID>',
)

res = s.ats.remove_ats_job(req)

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


## remove_ats_scorecard

Remove a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAtsScorecardRequest(
    connection_id='string',
    id='<ID>',
)

res = s.ats.remove_ats_scorecard(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsScorecardRequest](../../models/operations/removeatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsScorecardResponse](../../models/operations/removeatsscorecardresponse.md)**


## update_ats_application

Update an application

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

req = operations.UpdateAtsApplicationRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.update_ats_application(req)

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateAtsApplicationRequest](../../models/operations/updateatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateAtsApplicationResponse](../../models/operations/updateatsapplicationresponse.md)**


## update_ats_candidate

Update a candidate

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

req = operations.UpdateAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Gaetano86@hotmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.update_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsCandidateRequest](../../models/operations/updateatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateAtsCandidateResponse](../../models/operations/updateatscandidateresponse.md)**


## update_ats_interview

Update a interview

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

req = operations.UpdateAtsInterviewRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.update_ats_interview(req)

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
            'string',
        ],
        hiring_manager_ids=[
            'string',
        ],
        public_job_urls=[
            'string',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.update_ats_job(req)

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


## update_ats_scorecard

Update a scorecard

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

req = operations.UpdateAtsScorecardRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.ats.update_ats_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsScorecardRequest](../../models/operations/updateatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateAtsScorecardResponse](../../models/operations/updateatsscorecardresponse.md)**

