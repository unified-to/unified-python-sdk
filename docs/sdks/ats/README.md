# Ats
(*ats*)

### Available Operations

* [delete_ats_connection_id_application_id](#delete_ats_connection_id_application_id) - Remove an application
* [delete_ats_connection_id_candidate_id](#delete_ats_connection_id_candidate_id) - Remove a candidate
* [delete_ats_connection_id_interview_id](#delete_ats_connection_id_interview_id) - Remove a interview
* [delete_ats_connection_id_job_id](#delete_ats_connection_id_job_id) - Remove a job
* [delete_ats_connection_id_scorecard_id](#delete_ats_connection_id_scorecard_id) - Remove a scorecard
* [get_ats_connection_id_application](#get_ats_connection_id_application) - List all applications
* [get_ats_connection_id_application_id](#get_ats_connection_id_application_id) - Retrieve an application
* [get_ats_connection_id_candidate](#get_ats_connection_id_candidate) - List all candidates
* [get_ats_connection_id_candidate_id](#get_ats_connection_id_candidate_id) - Retrieve a candidate
* [get_ats_connection_id_interview](#get_ats_connection_id_interview) - List all interviews
* [get_ats_connection_id_interview_id](#get_ats_connection_id_interview_id) - Retrieve a interview
* [get_ats_connection_id_job](#get_ats_connection_id_job) - List all jobs
* [get_ats_connection_id_job_id](#get_ats_connection_id_job_id) - Retrieve a job
* [get_ats_connection_id_scorecard](#get_ats_connection_id_scorecard) - List all scorecards
* [get_ats_connection_id_scorecard_id](#get_ats_connection_id_scorecard_id) - Retrieve a scorecard
* [patch_ats_connection_id_application_id](#patch_ats_connection_id_application_id) - Update an application
* [patch_ats_connection_id_candidate_id](#patch_ats_connection_id_candidate_id) - Update a candidate
* [patch_ats_connection_id_interview_id](#patch_ats_connection_id_interview_id) - Update a interview
* [patch_ats_connection_id_job_id](#patch_ats_connection_id_job_id) - Update a job
* [patch_ats_connection_id_scorecard_id](#patch_ats_connection_id_scorecard_id) - Update a scorecard
* [post_ats_connection_id_application](#post_ats_connection_id_application) - Create an application
* [post_ats_connection_id_candidate](#post_ats_connection_id_candidate) - Create a candidate
* [post_ats_connection_id_interview](#post_ats_connection_id_interview) - Create a interview
* [post_ats_connection_id_job](#post_ats_connection_id_job) - Create a job
* [post_ats_connection_id_scorecard](#post_ats_connection_id_scorecard) - Create a scorecard
* [put_ats_connection_id_application_id](#put_ats_connection_id_application_id) - Update an application
* [put_ats_connection_id_candidate_id](#put_ats_connection_id_candidate_id) - Update a candidate
* [put_ats_connection_id_interview_id](#put_ats_connection_id_interview_id) - Update a interview
* [put_ats_connection_id_job_id](#put_ats_connection_id_job_id) - Update a job
* [put_ats_connection_id_scorecard_id](#put_ats_connection_id_scorecard_id) - Update a scorecard

## delete_ats_connection_id_application_id

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

req = operations.DeleteAtsConnectionIDApplicationIDRequest(
    connection_id='markets sievert meh',
    id='<ID>',
)

res = s.ats.delete_ats_connection_id_application_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.DeleteAtsConnectionIDApplicationIDRequest](../../models/operations/deleteatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.DeleteAtsConnectionIDApplicationIDResponse](../../models/operations/deleteatsconnectionidapplicationidresponse.md)**


## delete_ats_connection_id_candidate_id

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

req = operations.DeleteAtsConnectionIDCandidateIDRequest(
    connection_id='multimedia',
    id='<ID>',
)

res = s.ats.delete_ats_connection_id_candidate_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDCandidateIDRequest](../../models/operations/deleteatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDCandidateIDResponse](../../models/operations/deleteatsconnectionidcandidateidresponse.md)**


## delete_ats_connection_id_interview_id

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

req = operations.DeleteAtsConnectionIDInterviewIDRequest(
    connection_id='redundant Health Hayes',
    id='<ID>',
)

res = s.ats.delete_ats_connection_id_interview_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDInterviewIDRequest](../../models/operations/deleteatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDInterviewIDResponse](../../models/operations/deleteatsconnectionidinterviewidresponse.md)**


## delete_ats_connection_id_job_id

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

req = operations.DeleteAtsConnectionIDJobIDRequest(
    connection_id='Sedan Bedfordshire Hybrid',
    id='<ID>',
)

res = s.ats.delete_ats_connection_id_job_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteAtsConnectionIDJobIDRequest](../../models/operations/deleteatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.DeleteAtsConnectionIDJobIDResponse](../../models/operations/deleteatsconnectionidjobidresponse.md)**


## delete_ats_connection_id_scorecard_id

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

req = operations.DeleteAtsConnectionIDScorecardIDRequest(
    connection_id='Agent intrepid',
    id='<ID>',
)

res = s.ats.delete_ats_connection_id_scorecard_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDScorecardIDRequest](../../models/operations/deleteatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDScorecardIDResponse](../../models/operations/deleteatsconnectionidscorecardidresponse.md)**


## get_ats_connection_id_application

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

req = operations.GetAtsConnectionIDApplicationRequest(
    connection_id='turquoise',
)

res = s.ats.get_ats_connection_id_application(req)

if res.ats_applications is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDApplicationRequest](../../models/operations/getatsconnectionidapplicationrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDApplicationResponse](../../models/operations/getatsconnectionidapplicationresponse.md)**


## get_ats_connection_id_application_id

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

req = operations.GetAtsConnectionIDApplicationIDRequest(
    connection_id='Buckinghamshire functionalities',
    id='<ID>',
)

res = s.ats.get_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetAtsConnectionIDApplicationIDRequest](../../models/operations/getatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetAtsConnectionIDApplicationIDResponse](../../models/operations/getatsconnectionidapplicationidresponse.md)**


## get_ats_connection_id_candidate

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

req = operations.GetAtsConnectionIDCandidateRequest(
    connection_id='Northwest forceful Moore',
)

res = s.ats.get_ats_connection_id_candidate(req)

if res.ats_candidates is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAtsConnectionIDCandidateRequest](../../models/operations/getatsconnectionidcandidaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetAtsConnectionIDCandidateResponse](../../models/operations/getatsconnectionidcandidateresponse.md)**


## get_ats_connection_id_candidate_id

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

req = operations.GetAtsConnectionIDCandidateIDRequest(
    connection_id='ha Loan',
    id='<ID>',
)

res = s.ats.get_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDCandidateIDRequest](../../models/operations/getatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDCandidateIDResponse](../../models/operations/getatsconnectionidcandidateidresponse.md)**


## get_ats_connection_id_interview

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

req = operations.GetAtsConnectionIDInterviewRequest(
    connection_id='Fresh Pickup converse',
)

res = s.ats.get_ats_connection_id_interview(req)

if res.ats_interviews is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAtsConnectionIDInterviewRequest](../../models/operations/getatsconnectionidinterviewrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetAtsConnectionIDInterviewResponse](../../models/operations/getatsconnectionidinterviewresponse.md)**


## get_ats_connection_id_interview_id

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

req = operations.GetAtsConnectionIDInterviewIDRequest(
    connection_id='Loan Gorgeous lux',
    id='<ID>',
)

res = s.ats.get_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDInterviewIDRequest](../../models/operations/getatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDInterviewIDResponse](../../models/operations/getatsconnectionidinterviewidresponse.md)**


## get_ats_connection_id_job

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

req = operations.GetAtsConnectionIDJobRequest(
    connection_id='City katal',
)

res = s.ats.get_ats_connection_id_job(req)

if res.ats_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAtsConnectionIDJobRequest](../../models/operations/getatsconnectionidjobrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAtsConnectionIDJobResponse](../../models/operations/getatsconnectionidjobresponse.md)**


## get_ats_connection_id_job_id

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

req = operations.GetAtsConnectionIDJobIDRequest(
    connection_id='Jazz',
    id='<ID>',
)

res = s.ats.get_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAtsConnectionIDJobIDRequest](../../models/operations/getatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetAtsConnectionIDJobIDResponse](../../models/operations/getatsconnectionidjobidresponse.md)**


## get_ats_connection_id_scorecard

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

req = operations.GetAtsConnectionIDScorecardRequest(
    connection_id='Licensed deep',
)

res = s.ats.get_ats_connection_id_scorecard(req)

if res.ats_scorecards is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAtsConnectionIDScorecardRequest](../../models/operations/getatsconnectionidscorecardrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetAtsConnectionIDScorecardResponse](../../models/operations/getatsconnectionidscorecardresponse.md)**


## get_ats_connection_id_scorecard_id

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

req = operations.GetAtsConnectionIDScorecardIDRequest(
    connection_id='East mobile Mini',
    id='<ID>',
)

res = s.ats.get_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDScorecardIDRequest](../../models/operations/getatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDScorecardIDResponse](../../models/operations/getatsconnectionidscorecardidresponse.md)**


## patch_ats_connection_id_application_id

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

req = operations.PatchAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='mole Northeast Southwest',
    id='<ID>',
)

res = s.ats.patch_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PatchAtsConnectionIDApplicationIDRequest](../../models/operations/patchatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PatchAtsConnectionIDApplicationIDResponse](../../models/operations/patchatsconnectionidapplicationidresponse.md)**


## patch_ats_connection_id_candidate_id

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

req = operations.PatchAtsConnectionIDCandidateIDRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Stella57@hotmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'Chips',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='culpa',
            ),
        ],
    ),
    connection_id='Unbranded Country',
    id='<ID>',
)

res = s.ats.patch_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDCandidateIDRequest](../../models/operations/patchatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDCandidateIDResponse](../../models/operations/patchatsconnectionidcandidateidresponse.md)**


## patch_ats_connection_id_interview_id

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

req = operations.PatchAtsConnectionIDInterviewIDRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'coulomb',
        ],
    ),
    connection_id='green pascal illo',
    id='<ID>',
)

res = s.ats.patch_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDInterviewIDRequest](../../models/operations/patchatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDInterviewIDResponse](../../models/operations/patchatsconnectionidinterviewidresponse.md)**


## patch_ats_connection_id_job_id

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

req = operations.PatchAtsConnectionIDJobIDRequest(
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
            'Transexual',
        ],
        hiring_manager_ids=[
            'leach',
        ],
        public_job_urls=[
            'national',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'Kia',
        ],
    ),
    connection_id='Ferrari Facilitator',
    id='<ID>',
)

res = s.ats.patch_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAtsConnectionIDJobIDRequest](../../models/operations/patchatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PatchAtsConnectionIDJobIDResponse](../../models/operations/patchatsconnectionidjobidresponse.md)**


## patch_ats_connection_id_scorecard_id

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

req = operations.PatchAtsConnectionIDScorecardIDRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='Carter Hatchback functionalities',
    id='<ID>',
)

res = s.ats.patch_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDScorecardIDRequest](../../models/operations/patchatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDScorecardIDResponse](../../models/operations/patchatsconnectionidscorecardidresponse.md)**


## post_ats_connection_id_application

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

req = operations.PostAtsConnectionIDApplicationRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='Berkshire',
)

res = s.ats.post_ats_connection_id_application(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostAtsConnectionIDApplicationRequest](../../models/operations/postatsconnectionidapplicationrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostAtsConnectionIDApplicationResponse](../../models/operations/postatsconnectionidapplicationresponse.md)**


## post_ats_connection_id_candidate

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

req = operations.PostAtsConnectionIDCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Elmore.Mante@gmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'than',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='Wooden siemens Wooden',
            ),
        ],
    ),
    connection_id='Jazz Ball',
)

res = s.ats.post_ats_connection_id_candidate(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDCandidateRequest](../../models/operations/postatsconnectionidcandidaterequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDCandidateResponse](../../models/operations/postatsconnectionidcandidateresponse.md)**


## post_ats_connection_id_interview

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

req = operations.PostAtsConnectionIDInterviewRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'Tricycle',
        ],
    ),
    connection_id='Hat Savings Electronic',
)

res = s.ats.post_ats_connection_id_interview(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDInterviewRequest](../../models/operations/postatsconnectionidinterviewrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDInterviewResponse](../../models/operations/postatsconnectionidinterviewresponse.md)**


## post_ats_connection_id_job

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

req = operations.PostAtsConnectionIDJobRequest(
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
            'Forward',
        ],
        hiring_manager_ids=[
            'Americium',
        ],
        public_job_urls=[
            'shiny',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'yellow',
        ],
    ),
    connection_id='neatly Diesel virtual',
)

res = s.ats.post_ats_connection_id_job(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PostAtsConnectionIDJobRequest](../../models/operations/postatsconnectionidjobrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PostAtsConnectionIDJobResponse](../../models/operations/postatsconnectionidjobresponse.md)**


## post_ats_connection_id_scorecard

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

req = operations.PostAtsConnectionIDScorecardRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='female bah',
)

res = s.ats.post_ats_connection_id_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDScorecardRequest](../../models/operations/postatsconnectionidscorecardrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDScorecardResponse](../../models/operations/postatsconnectionidscorecardresponse.md)**


## put_ats_connection_id_application_id

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

req = operations.PutAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        raw=shared.PropertyAtsApplicationRaw(),
    ),
    connection_id='input Electric',
    id='<ID>',
)

res = s.ats.put_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PutAtsConnectionIDApplicationIDRequest](../../models/operations/putatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PutAtsConnectionIDApplicationIDResponse](../../models/operations/putatsconnectionidapplicationidresponse.md)**


## put_ats_connection_id_candidate_id

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

req = operations.PutAtsConnectionIDCandidateIDRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Giovanny_Botsford@gmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'deploy',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='knowledge officiis',
            ),
        ],
    ),
    connection_id='Personal Madagascar',
    id='<ID>',
)

res = s.ats.put_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDCandidateIDRequest](../../models/operations/putatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDCandidateIDResponse](../../models/operations/putatsconnectionidcandidateidresponse.md)**


## put_ats_connection_id_interview_id

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

req = operations.PutAtsConnectionIDInterviewIDRequest(
    ats_interview=shared.AtsInterview(
        raw=shared.PropertyAtsInterviewRaw(),
        user_ids=[
            'amet',
        ],
    ),
    connection_id='capacitor Auto',
    id='<ID>',
)

res = s.ats.put_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDInterviewIDRequest](../../models/operations/putatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDInterviewIDResponse](../../models/operations/putatsconnectionidinterviewidresponse.md)**


## put_ats_connection_id_job_id

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

req = operations.PutAtsConnectionIDJobIDRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(),
        ],
        compensation=[
            shared.AtsCompensation(
                type=shared.AtsCompensationType.STOCK_OPTIONS,
            ),
        ],
        departments=[
            'cotton',
        ],
        hiring_manager_ids=[
            'Washington',
        ],
        public_job_urls=[
            'Hybrid',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'henry',
        ],
    ),
    connection_id='male Intelligent',
    id='<ID>',
)

res = s.ats.put_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PutAtsConnectionIDJobIDRequest](../../models/operations/putatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PutAtsConnectionIDJobIDResponse](../../models/operations/putatsconnectionidjobidresponse.md)**


## put_ats_connection_id_scorecard_id

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

req = operations.PutAtsConnectionIDScorecardIDRequest(
    ats_scorecard=shared.AtsScorecard(
        raw=shared.PropertyAtsScorecardRaw(),
    ),
    connection_id='East Granite',
    id='<ID>',
)

res = s.ats.put_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDScorecardIDRequest](../../models/operations/putatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDScorecardIDResponse](../../models/operations/putatsconnectionidscorecardidresponse.md)**

