# Ats

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDApplicationIDRequest(
    connection_id='nulla',
    id='6b144290-7474-4778-a7bd-466d28c10ab3',
)

res = s.ats.delete_ats_connection_id_application_id(req, operations.DeleteAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteAtsConnectionIDApplicationIDRequest](../../models/operations/deleteatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.DeleteAtsConnectionIDApplicationIDSecurity](../../models/operations/deleteatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.DeleteAtsConnectionIDApplicationIDResponse](../../models/operations/deleteatsconnectionidapplicationidresponse.md)**


## delete_ats_connection_id_candidate_id

Remove a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDCandidateIDRequest(
    connection_id='quo',
    id='dca42519-04e5-423c-be0b-c7178e4796f2',
)

res = s.ats.delete_ats_connection_id_candidate_id(req, operations.DeleteAtsConnectionIDCandidateIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteAtsConnectionIDCandidateIDRequest](../../models/operations/deleteatsconnectionidcandidateidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.DeleteAtsConnectionIDCandidateIDSecurity](../../models/operations/deleteatsconnectionidcandidateidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.DeleteAtsConnectionIDCandidateIDResponse](../../models/operations/deleteatsconnectionidcandidateidresponse.md)**


## delete_ats_connection_id_interview_id

Remove a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDInterviewIDRequest(
    connection_id='deserunt',
    id='70c68828-2aa4-4825-a2f2-22e9817ee17c',
)

res = s.ats.delete_ats_connection_id_interview_id(req, operations.DeleteAtsConnectionIDInterviewIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteAtsConnectionIDInterviewIDRequest](../../models/operations/deleteatsconnectionidinterviewidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.DeleteAtsConnectionIDInterviewIDSecurity](../../models/operations/deleteatsconnectionidinterviewidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.DeleteAtsConnectionIDInterviewIDResponse](../../models/operations/deleteatsconnectionidinterviewidresponse.md)**


## delete_ats_connection_id_job_id

Remove a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDJobIDRequest(
    connection_id='nam',
    id='e61e6b7b-95bc-40ab-bc20-c4f3789fd871',
)

res = s.ats.delete_ats_connection_id_job_id(req, operations.DeleteAtsConnectionIDJobIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteAtsConnectionIDJobIDRequest](../../models/operations/deleteatsconnectionidjobidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.DeleteAtsConnectionIDJobIDSecurity](../../models/operations/deleteatsconnectionidjobidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.DeleteAtsConnectionIDJobIDResponse](../../models/operations/deleteatsconnectionidjobidresponse.md)**


## delete_ats_connection_id_scorecard_id

Remove a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDScorecardIDRequest(
    connection_id='a',
    id='99dd2efd-121a-4a6f-9e67-4bdb04f15756',
)

res = s.ats.delete_ats_connection_id_scorecard_id(req, operations.DeleteAtsConnectionIDScorecardIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteAtsConnectionIDScorecardIDRequest](../../models/operations/deleteatsconnectionidscorecardidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.DeleteAtsConnectionIDScorecardIDSecurity](../../models/operations/deleteatsconnectionidscorecardidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.DeleteAtsConnectionIDScorecardIDResponse](../../models/operations/deleteatsconnectionidscorecardidresponse.md)**


## get_ats_connection_id_application

List all applications

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDApplicationRequest(
    candidate_id='aut',
    connection_id='voluptatum',
    job_id='qui',
    limit=8453.58,
    offset=4012.59,
    order='deleniti',
    query='itaque',
    sort='dolorum',
    updated_gte=dateutil.parser.isoparse('2022-05-23T15:36:15.509Z'),
)

res = s.ats.get_ats_connection_id_application(req, operations.GetAtsConnectionIDApplicationSecurity(
    jwt="",
))

if res.ats_applications is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAtsConnectionIDApplicationRequest](../../models/operations/getatsconnectionidapplicationrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetAtsConnectionIDApplicationSecurity](../../models/operations/getatsconnectionidapplicationsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetAtsConnectionIDApplicationResponse](../../models/operations/getatsconnectionidapplicationresponse.md)**


## get_ats_connection_id_application_id

Retrieve an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDApplicationIDRequest(
    connection_id='tenetur',
    id='1d170513-39d0-4808-aa18-40394c26071f',
)

res = s.ats.get_ats_connection_id_application_id(req, operations.GetAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAtsConnectionIDApplicationIDRequest](../../models/operations/getatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.GetAtsConnectionIDApplicationIDSecurity](../../models/operations/getatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.GetAtsConnectionIDApplicationIDResponse](../../models/operations/getatsconnectionidapplicationidresponse.md)**


## get_ats_connection_id_candidate

List all candidates

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDCandidateRequest(
    connection_id='natus',
    limit=2446.51,
    offset=9742.57,
    order='voluptas',
    query='asperiores',
    sort='aperiam',
    updated_gte=dateutil.parser.isoparse('2022-09-09T19:48:26.093Z'),
)

res = s.ats.get_ats_connection_id_candidate(req, operations.GetAtsConnectionIDCandidateSecurity(
    jwt="",
))

if res.ats_candidates is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAtsConnectionIDCandidateRequest](../../models/operations/getatsconnectionidcandidaterequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetAtsConnectionIDCandidateSecurity](../../models/operations/getatsconnectionidcandidatesecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetAtsConnectionIDCandidateResponse](../../models/operations/getatsconnectionidcandidateresponse.md)**


## get_ats_connection_id_candidate_id

Retrieve a candidate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDCandidateIDRequest(
    connection_id='consequuntur',
    id='dac7af51-5cc4-413a-a63a-ae8d67864dbb',
)

res = s.ats.get_ats_connection_id_candidate_id(req, operations.GetAtsConnectionIDCandidateIDSecurity(
    jwt="",
))

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAtsConnectionIDCandidateIDRequest](../../models/operations/getatsconnectionidcandidateidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetAtsConnectionIDCandidateIDSecurity](../../models/operations/getatsconnectionidcandidateidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetAtsConnectionIDCandidateIDResponse](../../models/operations/getatsconnectionidcandidateidresponse.md)**


## get_ats_connection_id_interview

List all interviews

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDInterviewRequest(
    application_id='commodi',
    connection_id='in',
    limit=3605.45,
    offset=9689.04,
    order='assumenda',
    query='nemo',
    sort='recusandae',
    updated_gte=dateutil.parser.isoparse('2022-12-15T04:58:32.488Z'),
)

res = s.ats.get_ats_connection_id_interview(req, operations.GetAtsConnectionIDInterviewSecurity(
    jwt="",
))

if res.ats_interviews is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAtsConnectionIDInterviewRequest](../../models/operations/getatsconnectionidinterviewrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetAtsConnectionIDInterviewSecurity](../../models/operations/getatsconnectionidinterviewsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetAtsConnectionIDInterviewResponse](../../models/operations/getatsconnectionidinterviewresponse.md)**


## get_ats_connection_id_interview_id

Retrieve a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDInterviewIDRequest(
    connection_id='cum',
    id='375ed4f6-fbee-441f-b331-7fe35b60eb1e',
)

res = s.ats.get_ats_connection_id_interview_id(req, operations.GetAtsConnectionIDInterviewIDSecurity(
    jwt="",
))

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAtsConnectionIDInterviewIDRequest](../../models/operations/getatsconnectionidinterviewidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetAtsConnectionIDInterviewIDSecurity](../../models/operations/getatsconnectionidinterviewidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetAtsConnectionIDInterviewIDResponse](../../models/operations/getatsconnectionidinterviewidresponse.md)**


## get_ats_connection_id_job

List all jobs

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDJobRequest(
    connection_id='similique',
    limit=2724.37,
    offset=1328.15,
    order='voluptas',
    query='voluptas',
    sort='voluptas',
    updated_gte=dateutil.parser.isoparse('2022-04-02T16:36:53.419Z'),
)

res = s.ats.get_ats_connection_id_job(req, operations.GetAtsConnectionIDJobSecurity(
    jwt="",
))

if res.ats_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAtsConnectionIDJobRequest](../../models/operations/getatsconnectionidjobrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetAtsConnectionIDJobSecurity](../../models/operations/getatsconnectionidjobsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetAtsConnectionIDJobResponse](../../models/operations/getatsconnectionidjobresponse.md)**


## get_ats_connection_id_job_id

Retrieve a job

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDJobIDRequest(
    connection_id='dolorum',
    id='3c28744e-d53b-488f-ba8d-8f5c0b2f2fb7',
)

res = s.ats.get_ats_connection_id_job_id(req, operations.GetAtsConnectionIDJobIDSecurity(
    jwt="",
))

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAtsConnectionIDJobIDRequest](../../models/operations/getatsconnectionidjobidrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.GetAtsConnectionIDJobIDSecurity](../../models/operations/getatsconnectionidjobidsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetAtsConnectionIDJobIDResponse](../../models/operations/getatsconnectionidjobidresponse.md)**


## get_ats_connection_id_scorecard

List all scorecards

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDScorecardRequest(
    application_id='expedita',
    candidate_id='ab',
    connection_id='iste',
    interview_id='dolore',
    limit=6719.07,
    offset=1523.54,
    order='in',
    query='commodi',
    sort='quidem',
    updated_gte=dateutil.parser.isoparse('2022-08-15T21:51:46.128Z'),
)

res = s.ats.get_ats_connection_id_scorecard(req, operations.GetAtsConnectionIDScorecardSecurity(
    jwt="",
))

if res.ats_scorecards is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAtsConnectionIDScorecardRequest](../../models/operations/getatsconnectionidscorecardrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetAtsConnectionIDScorecardSecurity](../../models/operations/getatsconnectionidscorecardsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetAtsConnectionIDScorecardResponse](../../models/operations/getatsconnectionidscorecardresponse.md)**


## get_ats_connection_id_scorecard_id

Retrieve a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDScorecardIDRequest(
    connection_id='unde',
    id='16fe1f08-f429-44e3-a98f-447f603e8b44',
)

res = s.ats.get_ats_connection_id_scorecard_id(req, operations.GetAtsConnectionIDScorecardIDSecurity(
    jwt="",
))

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAtsConnectionIDScorecardIDRequest](../../models/operations/getatsconnectionidscorecardidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetAtsConnectionIDScorecardIDSecurity](../../models/operations/getatsconnectionidscorecardidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetAtsConnectionIDScorecardIDResponse](../../models/operations/getatsconnectionidscorecardidresponse.md)**


## patch_ats_connection_id_application_id

Update an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2022-02-08T08:59:54.184Z'),
        candidate_id='rem',
        created_at=dateutil.parser.isoparse('2022-04-02T00:47:15.232Z'),
        id='a55efd20-e457-4e18-98b6-a89fbe3a5aa8',
        job_id='accusamus',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2022-06-16T13:22:48.429Z'),
        rejected_reason='fugit',
        source='ut',
        status=shared.AtsApplicationStatus.HIRED,
        updated_at=dateutil.parser.isoparse('2022-05-14T04:54:08.545Z'),
    ),
    connection_id='expedita',
    id='4075088e-5186-4206-9e90-4f3b1194b8ab',
)

res = s.ats.patch_ats_connection_id_application_id(req, operations.PatchAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchAtsConnectionIDApplicationIDRequest](../../models/operations/patchatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PatchAtsConnectionIDApplicationIDSecurity](../../models/operations/patchatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PatchAtsConnectionIDApplicationIDResponse](../../models/operations/patchatsconnectionidapplicationidresponse.md)**


## patch_ats_connection_id_candidate_id

Update a candidate

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDCandidateIDRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(
            address1='tenetur',
            address2='laboriosam',
            city='East Lutherport',
            country='Morocco',
            country_code='WF',
            postal_code='89906-6486',
            region='praesentium',
            region_code='mollitia',
        ),
        company_name='veniam',
        created_at=dateutil.parser.isoparse('2022-03-18T08:14:24.399Z'),
        emails=[
            shared.AtsEmail(
                email='Avis_Littel@hotmail.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='suscipit',
        id='bc173d68-9eee-4952-af8d-986e881ead4f',
        image_url='doloremque',
        name='Mr. Keith Bashirian',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'laboriosam',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='velit',
                type=shared.AtsTelephoneType.MOBILE,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-02-04T04:20:12.809Z'),
    ),
    connection_id='consequuntur',
    id='9e973e92-2a57-4a15-be3e-060807e2b6e3',
)

res = s.ats.patch_ats_connection_id_candidate_id(req, operations.PatchAtsConnectionIDCandidateIDSecurity(
    jwt="",
))

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchAtsConnectionIDCandidateIDRequest](../../models/operations/patchatsconnectionidcandidateidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PatchAtsConnectionIDCandidateIDSecurity](../../models/operations/patchatsconnectionidcandidateidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PatchAtsConnectionIDCandidateIDResponse](../../models/operations/patchatsconnectionidcandidateidresponse.md)**


## patch_ats_connection_id_interview_id

Update a interview

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDInterviewIDRequest(
    ats_interview=shared.AtsInterview(
        application_id='laborum',
        candidate_id='distinctio',
        created_at=dateutil.parser.isoparse('2021-12-15T04:55:40.282Z'),
        end_at=dateutil.parser.isoparse('2022-09-05T23:50:51.335Z'),
        external_event_xref='repellat',
        id='0597a60f-f2a5-44a3-9e94-764a3e865e79',
        job_id='quis',
        location='eum',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2021-03-22T21:44:03.640Z'),
        status=shared.AtsInterviewStatus.SCHEDULED,
        updated_at=dateutil.parser.isoparse('2022-11-26T15:59:49.659Z'),
        user_ids=[
            'animi',
        ],
    ),
    connection_id='nostrum',
    id='a9da660f-f57b-4faa-94f9-efc1b4512c10',
)

res = s.ats.patch_ats_connection_id_interview_id(req, operations.PatchAtsConnectionIDInterviewIDSecurity(
    jwt="",
))

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchAtsConnectionIDInterviewIDRequest](../../models/operations/patchatsconnectionidinterviewidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PatchAtsConnectionIDInterviewIDSecurity](../../models/operations/patchatsconnectionidinterviewidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PatchAtsConnectionIDInterviewIDResponse](../../models/operations/patchatsconnectionidinterviewidresponse.md)**


## patch_ats_connection_id_job_id

Update a job

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDJobIDRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='velit',
                address2='aspernatur',
                city='Devenstad',
                country='Taiwan',
                country_code='SA',
                postal_code='94131',
                region='cupiditate',
                region_code='provident',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2020-10-06T18:56:18.922Z'),
        compensation=[
            shared.AtsCompensation(
                currency='hic',
                frequency=shared.AtsCompensationFrequency.MONTH,
                max=525.08,
                min=9358.33,
                type=shared.AtsCompensationType.STOCK_OPTIONS,
            ),
        ],
        created_at=dateutil.parser.isoparse('2020-04-29T11:28:14.354Z'),
        departments=[
            'aliquid',
        ],
        description='porro',
        employment_type=shared.AtsJobEmploymentType.INTERN,
        hiring_manager_ids=[
            'dolorem',
        ],
        id='2ca3aed0-1179-4963-92fd-e04771778ff6',
        language_locale='architecto',
        name='Brian Carroll',
        public_job_urls=[
            'esse',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'ex',
        ],
        remote=False,
        status=shared.AtsJobStatus.PENDING,
        updated_at=dateutil.parser.isoparse('2022-12-10T12:17:45.772Z'),
    ),
    connection_id='laborum',
    id='15db6a66-0659-4a1a-9eaa-b5851d6c645b',
)

res = s.ats.patch_ats_connection_id_job_id(req, operations.PatchAtsConnectionIDJobIDSecurity(
    jwt="",
))

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAtsConnectionIDJobIDRequest](../../models/operations/patchatsconnectionidjobidrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.PatchAtsConnectionIDJobIDSecurity](../../models/operations/patchatsconnectionidjobidsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.PatchAtsConnectionIDJobIDResponse](../../models/operations/patchatsconnectionidjobidresponse.md)**


## patch_ats_connection_id_scorecard_id

Update a scorecard

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDScorecardIDRequest(
    ats_scorecard=shared.AtsScorecard(
        application_id='voluptatem',
        candidate_id='molestias',
        created_at=dateutil.parser.isoparse('2022-03-15T05:57:22.639Z'),
        id='1891baa0-fe1a-4de0-88e6-f8c5f350d8cd',
        interview_id='nam',
        interviewer_id='ipsam',
        job_id='culpa',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.DEFINITELY_NO,
        updated_at=dateutil.parser.isoparse('2022-12-02T14:32:21.843Z'),
    ),
    connection_id='deleniti',
    id='14301042-1813-4d52-88ec-e7e253b66845',
)

res = s.ats.patch_ats_connection_id_scorecard_id(req, operations.PatchAtsConnectionIDScorecardIDSecurity(
    jwt="",
))

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchAtsConnectionIDScorecardIDRequest](../../models/operations/patchatsconnectionidscorecardidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PatchAtsConnectionIDScorecardIDSecurity](../../models/operations/patchatsconnectionidscorecardidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PatchAtsConnectionIDScorecardIDResponse](../../models/operations/patchatsconnectionidscorecardidresponse.md)**


## post_ats_connection_id_application

Create an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDApplicationRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2022-03-21T18:14:19.097Z'),
        candidate_id='autem',
        created_at=dateutil.parser.isoparse('2021-11-01T18:57:38.460Z'),
        id='e205e16d-eab3-4fec-9578-a64584273a84',
        job_id='quasi',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2021-04-19T03:31:22.925Z'),
        rejected_reason='dicta',
        source='nisi',
        status=shared.AtsApplicationStatus.REVIEWING,
        updated_at=dateutil.parser.isoparse('2022-12-14T21:58:33.872Z'),
    ),
    connection_id='cupiditate',
)

res = s.ats.post_ats_connection_id_application(req, operations.PostAtsConnectionIDApplicationSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostAtsConnectionIDApplicationRequest](../../models/operations/postatsconnectionidapplicationrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.PostAtsConnectionIDApplicationSecurity](../../models/operations/postatsconnectionidapplicationsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostAtsConnectionIDApplicationResponse](../../models/operations/postatsconnectionidapplicationresponse.md)**


## post_ats_connection_id_candidate

Create a candidate

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(
            address1='reiciendis',
            address2='soluta',
            city='New Chaunceystead',
            country='Namibia',
            country_code='CH',
            postal_code='68976',
            region='delectus',
            region_code='minima',
        ),
        company_name='praesentium',
        created_at=dateutil.parser.isoparse('2022-02-06T01:23:27.992Z'),
        emails=[
            shared.AtsEmail(
                email='Katheryn.Johns52@hotmail.com',
                type=shared.AtsEmailType.OTHER,
            ),
        ],
        external_id='modi',
        id='be056013-f59d-4a75-ba59-ecfef66ef1ca',
        image_url='laborum',
        name='Shannon Lind',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'magni',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='soluta',
                type=shared.AtsTelephoneType.MOBILE,
            ),
        ],
        title='Miss',
        updated_at=dateutil.parser.isoparse('2022-07-08T17:52:09.255Z'),
    ),
    connection_id='voluptate',
)

res = s.ats.post_ats_connection_id_candidate(req, operations.PostAtsConnectionIDCandidateSecurity(
    jwt="",
))

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostAtsConnectionIDCandidateRequest](../../models/operations/postatsconnectionidcandidaterequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PostAtsConnectionIDCandidateSecurity](../../models/operations/postatsconnectionidcandidatesecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PostAtsConnectionIDCandidateResponse](../../models/operations/postatsconnectionidcandidateresponse.md)**


## post_ats_connection_id_interview

Create a interview

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDInterviewRequest(
    ats_interview=shared.AtsInterview(
        application_id='sequi',
        candidate_id='dignissimos',
        created_at=dateutil.parser.isoparse('2022-03-22T23:13:00.381Z'),
        end_at=dateutil.parser.isoparse('2021-04-24T17:00:12.334Z'),
        external_event_xref='iure',
        id='2f64d1db-1f2c-4431-8661-e96349e1cf9e',
        job_id='alias',
        location='nisi',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2022-04-10T19:32:47.130Z'),
        status=shared.AtsInterviewStatus.COMPLETE,
        updated_at=dateutil.parser.isoparse('2022-10-11T01:40:09.903Z'),
        user_ids=[
            'iusto',
        ],
    ),
    connection_id='sit',
)

res = s.ats.post_ats_connection_id_interview(req, operations.PostAtsConnectionIDInterviewSecurity(
    jwt="",
))

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostAtsConnectionIDInterviewRequest](../../models/operations/postatsconnectionidinterviewrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PostAtsConnectionIDInterviewSecurity](../../models/operations/postatsconnectionidinterviewsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PostAtsConnectionIDInterviewResponse](../../models/operations/postatsconnectionidinterviewresponse.md)**


## post_ats_connection_id_job

Create a job

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDJobRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='doloremque',
                address2='consequatur',
                city='Walterview',
                country='Paraguay',
                country_code='GY',
                postal_code='85759-4368',
                region='animi',
                region_code='impedit',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-08-23T12:57:35.673Z'),
        compensation=[
            shared.AtsCompensation(
                currency='est',
                frequency=shared.AtsCompensationFrequency.HOUR,
                max=4568.85,
                min=2885.7,
                type=shared.AtsCompensationType.SALARY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-04-20T16:11:36.555Z'),
        departments=[
            'vitae',
        ],
        description='inventore',
        employment_type=shared.AtsJobEmploymentType.CONTRACTOR,
        hiring_manager_ids=[
            'ad',
        ],
        id='2965bb8a-7202-4611-835e-139dbc2259b1',
        language_locale='id',
        name='Laurence Nienow',
        public_job_urls=[
            'sit',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'iusto',
        ],
        remote=False,
        status=shared.AtsJobStatus.ARCHIVED,
        updated_at=dateutil.parser.isoparse('2022-10-05T07:59:39.108Z'),
    ),
    connection_id='aperiam',
)

res = s.ats.post_ats_connection_id_job(req, operations.PostAtsConnectionIDJobSecurity(
    jwt="",
))

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostAtsConnectionIDJobRequest](../../models/operations/postatsconnectionidjobrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PostAtsConnectionIDJobSecurity](../../models/operations/postatsconnectionidjobsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PostAtsConnectionIDJobResponse](../../models/operations/postatsconnectionidjobresponse.md)**


## post_ats_connection_id_scorecard

Create a scorecard

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDScorecardRequest(
    ats_scorecard=shared.AtsScorecard(
        application_id='totam',
        candidate_id='dolore',
        created_at=dateutil.parser.isoparse('2020-11-09T00:25:03.486Z'),
        id='0672d1ad-879e-4eb9-a65b-85efbd02bae0',
        interview_id='expedita',
        interviewer_id='officiis',
        job_id='eos',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.STRONG_YES,
        updated_at=dateutil.parser.isoparse('2022-06-28T19:16:42.798Z'),
    ),
    connection_id='odit',
)

res = s.ats.post_ats_connection_id_scorecard(req, operations.PostAtsConnectionIDScorecardSecurity(
    jwt="",
))

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostAtsConnectionIDScorecardRequest](../../models/operations/postatsconnectionidscorecardrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PostAtsConnectionIDScorecardSecurity](../../models/operations/postatsconnectionidscorecardsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PostAtsConnectionIDScorecardResponse](../../models/operations/postatsconnectionidscorecardresponse.md)**


## put_ats_connection_id_application_id

Update an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2022-08-22T23:12:04.283Z'),
        candidate_id='error',
        created_at=dateutil.parser.isoparse('2022-04-13T22:13:24.007Z'),
        id='ea4b5197-f924-443d-a7ce-52b895c537c6',
        job_id='modi',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2022-09-14T03:12:12.516Z'),
        rejected_reason='voluptates',
        source='maiores',
        status=shared.AtsApplicationStatus.OFFERED,
        updated_at=dateutil.parser.isoparse('2022-04-10T10:41:17.662Z'),
    ),
    connection_id='ratione',
    id='4896c3ca-5acf-4be2-bd57-07577929177d',
)

res = s.ats.put_ats_connection_id_application_id(req, operations.PutAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutAtsConnectionIDApplicationIDRequest](../../models/operations/putatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PutAtsConnectionIDApplicationIDSecurity](../../models/operations/putatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PutAtsConnectionIDApplicationIDResponse](../../models/operations/putatsconnectionidapplicationidresponse.md)**


## put_ats_connection_id_candidate_id

Update a candidate

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDCandidateIDRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(
            address1='itaque',
            address2='similique',
            city='Jacobsborough',
            country='Iraq',
            country_code='TM',
            postal_code='63422-0581',
            region='repudiandae',
            region_code='cum',
        ),
        company_name='dicta',
        created_at=dateutil.parser.isoparse('2021-12-30T18:01:47.888Z'),
        emails=[
            shared.AtsEmail(
                email='Chanel16@yahoo.com',
                type=shared.AtsEmailType.OTHER,
            ),
        ],
        external_id='nobis',
        id='07f116db-9954-45fc-95fa-88970e189dbb',
        image_url='velit',
        name='Lucia Rutherford',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'adipisci',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='saepe',
                type=shared.AtsTelephoneType.FAX,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2022-09-01T10:17:19.810Z'),
    ),
    connection_id='libero',
    id='197cd44e-2f52-4d82-9351-3bb6f48b656b',
)

res = s.ats.put_ats_connection_id_candidate_id(req, operations.PutAtsConnectionIDCandidateIDSecurity(
    jwt="",
))

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutAtsConnectionIDCandidateIDRequest](../../models/operations/putatsconnectionidcandidateidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PutAtsConnectionIDCandidateIDSecurity](../../models/operations/putatsconnectionidcandidateidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PutAtsConnectionIDCandidateIDResponse](../../models/operations/putatsconnectionidcandidateidresponse.md)**


## put_ats_connection_id_interview_id

Update a interview

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDInterviewIDRequest(
    ats_interview=shared.AtsInterview(
        application_id='minus',
        candidate_id='facere',
        created_at=dateutil.parser.isoparse('2022-07-26T02:32:48.491Z'),
        end_at=dateutil.parser.isoparse('2022-01-10T13:20:53.595Z'),
        external_event_xref='voluptatibus',
        id='2e4b2753-7a8c-4d9e-b319-c177d525f77b',
        job_id='illo',
        location='ab',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2022-02-14T02:26:29.574Z'),
        status=shared.AtsInterviewStatus.COMPLETE,
        updated_at=dateutil.parser.isoparse('2022-05-02T04:00:18.906Z'),
        user_ids=[
            'eos',
        ],
    ),
    connection_id='reiciendis',
    id='f785fc37-814d-44c9-8e0c-2bb89eb75dad',
)

res = s.ats.put_ats_connection_id_interview_id(req, operations.PutAtsConnectionIDInterviewIDSecurity(
    jwt="",
))

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutAtsConnectionIDInterviewIDRequest](../../models/operations/putatsconnectionidinterviewidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PutAtsConnectionIDInterviewIDSecurity](../../models/operations/putatsconnectionidinterviewidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PutAtsConnectionIDInterviewIDResponse](../../models/operations/putatsconnectionidinterviewidresponse.md)**


## put_ats_connection_id_job_id

Update a job

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDJobIDRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='iure',
                address2='dolorem',
                city='Olenview',
                country='Algeria',
                country_code='AO',
                postal_code='02856',
                region='cum',
                region_code='amet',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-11-18T21:12:35.377Z'),
        compensation=[
            shared.AtsCompensation(
                currency='laudantium',
                frequency=shared.AtsCompensationFrequency.ONE_TIME,
                max=9384.12,
                min=4797.07,
                type=shared.AtsCompensationType.BONUS,
            ),
        ],
        created_at=dateutil.parser.isoparse('2021-08-24T16:29:13.432Z'),
        departments=[
            'necessitatibus',
        ],
        description='provident',
        employment_type=shared.AtsJobEmploymentType.OTHER,
        hiring_manager_ids=[
            'consequatur',
        ],
        id='57eb809e-2810-4331-b398-1d4c700b607f',
        language_locale='velit',
        name='Rene Feeney',
        public_job_urls=[
            'consectetur',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'soluta',
        ],
        remote=False,
        status=shared.AtsJobStatus.OPEN,
        updated_at=dateutil.parser.isoparse('2021-01-30T14:43:38.066Z'),
    ),
    connection_id='amet',
    id='f2ceda7e-23f2-4257-811f-af4b7544e472',
)

res = s.ats.put_ats_connection_id_job_id(req, operations.PutAtsConnectionIDJobIDSecurity(
    jwt="",
))

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutAtsConnectionIDJobIDRequest](../../models/operations/putatsconnectionidjobidrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.PutAtsConnectionIDJobIDSecurity](../../models/operations/putatsconnectionidjobidsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.PutAtsConnectionIDJobIDResponse](../../models/operations/putatsconnectionidjobidresponse.md)**


## put_ats_connection_id_scorecard_id

Update a scorecard

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDScorecardIDRequest(
    ats_scorecard=shared.AtsScorecard(
        application_id='accusamus',
        candidate_id='rem',
        created_at=dateutil.parser.isoparse('2022-11-10T05:40:49.537Z'),
        id='857a5b40-463a-47d5-b5f1-400e764ad733',
        interview_id='quaerat',
        interviewer_id='itaque',
        job_id='minus',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.DEFINITELY_NO,
        updated_at=dateutil.parser.isoparse('2022-01-14T14:18:21.018Z'),
    ),
    connection_id='quas',
    id='1b36a080-88d1-400e-bada-200ef0422eb2',
)

res = s.ats.put_ats_connection_id_scorecard_id(req, operations.PutAtsConnectionIDScorecardIDSecurity(
    jwt="",
))

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutAtsConnectionIDScorecardIDRequest](../../models/operations/putatsconnectionidscorecardidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PutAtsConnectionIDScorecardIDSecurity](../../models/operations/putatsconnectionidscorecardidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PutAtsConnectionIDScorecardIDResponse](../../models/operations/putatsconnectionidscorecardidresponse.md)**

