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
    connection_id='fuga',
    id='4251904e-523c-47e0-bc71-78e4796f2a70',
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
    connection_id='porro',
    id='688282aa-4825-462f-a22e-9817ee17cbe6',
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
    connection_id='quasi',
    id='e6b7b95b-c0ab-43c2-8c4f-3789fd871f99',
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
    connection_id='pariatur',
    id='d2efd121-aa6f-41e6-b4bd-b04f15756082',
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
    connection_id='quibusdam',
    id='68ea19f1-d170-4513-b9d0-8086a1840394',
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
    candidate_id='impedit',
    connection_id='explicabo',
    job_id='voluptas',
    limit=120.36,
    offset=4910.25,
    order='dicta',
    query='maiores',
    sort='natus',
    updated_gte=dateutil.parser.isoparse('2022-01-10T09:30:55.914Z'),
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
    connection_id='voluptas',
    id='f0642dac-7af5-415c-8413-aa63aae8d678',
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
    connection_id='vel',
    limit=2870.51,
    offset=8225.6,
    order='facilis',
    query='cum',
    sort='commodi',
    updated_gte=dateutil.parser.isoparse('2022-08-22T09:37:14.602Z'),
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
    connection_id='reiciendis',
    id='d5e60b37-5ed4-4f6f-bee4-1f33317fe35b',
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
    application_id='laboriosam',
    connection_id='ipsa',
    limit=9167.27,
    offset=7307.09,
    order='vitae',
    query='accusamus',
    sort='similique',
    updated_gte=dateutil.parser.isoparse('2022-11-13T12:32:25.289Z'),
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
    connection_id='voluptas',
    id='555ba3c2-8744-4ed5-bb88-f3a8d8f5c0b2',
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
    connection_id='reiciendis',
    limit=1318.52,
    offset=9944.01,
    order='facilis',
    query='voluptate',
    sort='expedita',
    updated_gte=dateutil.parser.isoparse('2022-05-22T17:05:01.514Z'),
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
    connection_id='dolore',
    id='a276b269-16fe-41f0-8f42-94e3698f447f',
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
    application_id='ex',
    candidate_id='sit',
    connection_id='non',
    interview_id='officiis',
    limit=5058.66,
    offset=7086.09,
    order='quaerat',
    query='incidunt',
    sort='ipsam',
    updated_gte=dateutil.parser.isoparse('2021-06-05T03:46:35.414Z'),
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
    connection_id='sit',
    id='ca55efd2-0e45-47e1-858b-6a89fbe3a5aa',
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
        applied_at=dateutil.parser.isoparse('2021-03-30T03:48:24.857Z'),
        candidate_id='tempora',
        created_at=dateutil.parser.isoparse('2022-09-14T18:19:59.469Z'),
        id='4d0ab407-5088-4e51-8620-65e904f3b119',
        job_id='labore',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2021-12-03T11:25:52.746Z'),
        rejected_reason='laborum',
        source='nam',
        status=shared.AtsApplicationStatus.REJECTED,
        updated_at=dateutil.parser.isoparse('2022-12-31T00:19:10.437Z'),
    ),
    connection_id='amet',
    id='a79f9dfe-0ab7-4da8-a50c-e187f86bc173',
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
        address=shared.PropertyAtsCandidateAddress(
            address1='assumenda',
            address2='ea',
            city='Lindaside',
            country='Timor-Leste',
            country_code='TK',
            postal_code='31495-8653',
            region='repudiandae',
            region_code='atque',
        ),
        company_name='atque',
        created_at=dateutil.parser.isoparse('2022-01-28T23:50:19.904Z'),
        emails=[
            shared.AtsEmail(
                email='Richie.Grant91@hotmail.com',
                type=shared.AtsEmailType.WORK,
            ),
        ],
        external_id='accusantium',
        id='12563f94-e29e-4973-a922-a57a15be3e06',
        image_url='ipsa',
        name='Frank Krajcik',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'cum',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='iure',
                type=shared.AtsTelephoneType.MOBILE,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2021-07-27T21:33:31.354Z'),
    ),
    connection_id='voluptatum',
    id='845f0597-a60f-4f2a-94a3-1e94764a3e86',
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
        application_id='nemo',
        candidate_id='recusandae',
        created_at=dateutil.parser.isoparse('2022-05-29T21:22:23.687Z'),
        end_at=dateutil.parser.isoparse('2022-07-27T09:33:49.991Z'),
        external_event_xref='reiciendis',
        id='9251a5a9-da66-40ff-97bf-aad4f9efc1b4',
        job_id='quis',
        location='inventore',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2022-03-27T16:13:46.480Z'),
        status=shared.AtsInterviewStatus.SCHEDULED,
        updated_at=dateutil.parser.isoparse('2022-10-04T16:56:27.065Z'),
        user_ids=[
            'aspernatur',
        ],
    ),
    connection_id='eum',
    id='48dc2f61-5199-4ebf-90e9-fe6c632ca3ae',
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
            shared.AtsAddress(
                address1='nulla',
                address2='consequatur',
                city='North Jessefurt',
                country='Moldova',
                country_code='HM',
                postal_code='01988',
                region='ipsa',
                region_code='tempora',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-07-12T06:51:18.031Z'),
        compensation=[
            shared.AtsCompensation(
                currency='dicta',
                frequency=shared.AtsCompensationFrequency.YEAR,
                max=4570.59,
                min=5083.9,
                type=shared.AtsCompensationType.OTHER,
            ),
        ],
        created_at=dateutil.parser.isoparse('2021-09-24T00:59:48.564Z'),
        departments=[
            'architecto',
        ],
        description='fugiat',
        employment_type=shared.AtsJobEmploymentType.FULL_TIME,
        hiring_manager_ids=[
            'dicta',
        ],
        id='7476360a-15db-46a6-a065-9a1adeaab585',
        language_locale='vitae',
        name='Ruben Ryan',
        public_job_urls=[
            'ad',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'expedita',
        ],
        remote=False,
        status=shared.AtsJobStatus.ARCHIVED,
        updated_at=dateutil.parser.isoparse('2021-07-11T19:18:20.130Z'),
    ),
    connection_id='aliquid',
    id='1891baa0-fe1a-4de0-88e6-f8c5f350d8cd',
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
        application_id='nam',
        candidate_id='ipsam',
        created_at=dateutil.parser.isoparse('2022-07-22T07:25:32.550Z'),
        id='41814301-0421-4813-9520-8ece7e253b66',
        interview_id='voluptatum',
        interviewer_id='magnam',
        job_id='exercitationem',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.DEFINITELY_NO,
        updated_at=dateutil.parser.isoparse('2021-09-26T01:55:33.743Z'),
    ),
    connection_id='nobis',
    id='6e205e16-deab-43fe-8957-8a64584273a8',
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
        applied_at=dateutil.parser.isoparse('2022-11-26T09:57:27.688Z'),
        candidate_id='rem',
        created_at=dateutil.parser.isoparse('2022-08-25T11:14:44.041Z'),
        id='62309fb0-9299-421a-afb9-f58c4d86e68e',
        job_id='modi',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2021-03-31T11:58:23.065Z'),
        rejected_reason='voluptatem',
        source='ipsam',
        status=shared.AtsApplicationStatus.SECOND_INTERVIEW,
        updated_at=dateutil.parser.isoparse('2022-11-27T17:29:03.103Z'),
    ),
    connection_id='non',
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
        address=shared.PropertyAtsCandidateAddress(
            address1='maiores',
            address2='enim',
            city='Ryderfurt',
            country='Kenya',
            country_code='GT',
            postal_code='63587',
            region='hic',
            region_code='necessitatibus',
        ),
        company_name='asperiores',
        created_at=dateutil.parser.isoparse('2022-08-16T11:44:46.779Z'),
        emails=[
            shared.AtsEmail(
                email='Virginie_Bergnaum67@hotmail.com',
                type=shared.AtsEmailType.WORK,
            ),
        ],
        external_id='velit',
        id='83c2beb4-7737-43c8-972f-64d1db1f2c43',
        image_url='illo',
        name='Dr. Gina Jaskolski',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'eum',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='velit',
                type=shared.AtsTelephoneType.HOME,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-08-25T07:25:33.000Z'),
    ),
    connection_id='impedit',
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
        application_id='voluptatibus',
        candidate_id='iste',
        created_at=dateutil.parser.isoparse('2022-12-29T01:38:46.899Z'),
        end_at=dateutil.parser.isoparse('2022-01-26T00:00:57.040Z'),
        external_event_xref='velit',
        id='a437000a-e6b6-4bc9-b8f7-59eac55a9741',
        job_id='vero',
        location='consectetur',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2022-12-02T07:11:00.455Z'),
        status=shared.AtsInterviewStatus.SCHEDULED,
        updated_at=dateutil.parser.isoparse('2022-10-26T04:37:41.230Z'),
        user_ids=[
            'iste',
        ],
    ),
    connection_id='ex',
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
            shared.AtsAddress(
                address1='nemo',
                address2='soluta',
                city='Legroschester',
                country='Latvia',
                country_code='BZ',
                postal_code='14002',
                region='neque',
                region_code='exercitationem',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-09-26T08:50:09.615Z'),
        compensation=[
            shared.AtsCompensation(
                currency='ipsum',
                frequency=shared.AtsCompensationFrequency.HOUR,
                max=8583.38,
                min=7143.76,
                type=shared.AtsCompensationType.OTHER,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-11-03T21:52:43.365Z'),
        departments=[
            'nostrum',
        ],
        description='omnis',
        employment_type=shared.AtsJobEmploymentType.SEASONAL,
        hiring_manager_ids=[
            'dicta',
        ],
        id='abda8c07-0e10-484c-b067-2d1ad879eeb9',
        language_locale='ea',
        name='Brittany Prosacco',
        public_job_urls=[
            'officiis',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'voluptatibus',
        ],
        remote=False,
        status=shared.AtsJobStatus.OPEN,
        updated_at=dateutil.parser.isoparse('2022-12-26T08:34:47.406Z'),
    ),
    connection_id='quia',
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
        application_id='quidem',
        candidate_id='fuga',
        created_at=dateutil.parser.isoparse('2022-11-24T16:37:12.153Z'),
        id='be2d7822-59e3-4ea4-b519-7f92443da7ce',
        interview_id='corporis',
        interviewer_id='qui',
        job_id='expedita',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.YES,
        updated_at=dateutil.parser.isoparse('2022-05-07T19:45:21.246Z'),
    ),
    connection_id='placeat',
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
        applied_at=dateutil.parser.isoparse('2022-10-18T12:19:42.762Z'),
        candidate_id='in',
        created_at=dateutil.parser.isoparse('2021-09-13T18:43:27.876Z'),
        id='454efb0b-3489-46c3-8a5a-cfbe2fd57075',
        job_id='in',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2022-06-07T17:40:07.973Z'),
        rejected_reason='dolores',
        source='error',
        status=shared.AtsApplicationStatus.REVIEWING,
        updated_at=dateutil.parser.isoparse('2022-07-19T18:05:42.224Z'),
    ),
    connection_id='pariatur',
    id='eac646ec-b573-4409-a3eb-1e5a2b12eb07',
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
        address=shared.PropertyAtsCandidateAddress(
            address1='maiores',
            address2='veritatis',
            city='South Salmacester',
            country='Mayotte',
            country_code='MK',
            postal_code='33975',
            region='enim',
            region_code='hic',
        ),
        company_name='animi',
        created_at=dateutil.parser.isoparse('2021-12-19T08:26:48.749Z'),
        emails=[
            shared.AtsEmail(
                email='Jazmyne.Bechtelar55@yahoo.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='assumenda',
        id='bb30fcb3-3ea0-455b-997c-d44e2f52d82d',
        image_url='amet',
        name='Virginia Flatley',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'nisi',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='voluptatibus',
                type=shared.AtsTelephoneType.HOME,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-03-20T12:36:58.674Z'),
    ),
    connection_id='quis',
    id='6bcdb35f-f2e4-4b27-937a-8cd9e7319c17',
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
        application_id='esse',
        candidate_id='fugiat',
        created_at=dateutil.parser.isoparse('2022-11-12T18:59:18.362Z'),
        end_at=dateutil.parser.isoparse('2022-01-13T17:49:01.077Z'),
        external_event_xref='iusto',
        id='7b114eeb-52ff-4785-bc37-814d4c98e0c2',
        job_id='nam',
        location='expedita',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2021-10-26T16:10:32.283Z'),
        status=shared.AtsInterviewStatus.COMPLETE,
        updated_at=dateutil.parser.isoparse('2022-01-06T13:49:40.637Z'),
        user_ids=[
            'corporis',
        ],
    ),
    connection_id='vero',
    id='ad636c60-0503-4d8b-b311-80f739ae9e05',
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
            shared.AtsAddress(
                address1='molestiae',
                address2='itaque',
                city='Lockmanton',
                country='Micronesia',
                country_code='TK',
                postal_code='51022',
                region='sunt',
                region_code='a',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-06-02T10:52:44.468Z'),
        compensation=[
            shared.AtsCompensation(
                currency='atque',
                frequency=shared.AtsCompensationFrequency.ONE_TIME,
                max=8682.55,
                min=2875.44,
                type=shared.AtsCompensationType.EQUITY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-12-20T04:33:32.836Z'),
        departments=[
            'perferendis',
        ],
        description='rerum',
        employment_type=shared.AtsJobEmploymentType.CONSULTANT,
        hiring_manager_ids=[
            'aperiam',
        ],
        id='7f3c93c7-3b9d-4a3f-aced-a7e23f225741',
        language_locale='illo',
        name='Doug Wintheiser',
        public_job_urls=[
            'in',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'exercitationem',
        ],
        remote=False,
        status=shared.AtsJobStatus.PENDING,
        updated_at=dateutil.parser.isoparse('2022-01-29T18:21:22.366Z'),
    ),
    connection_id='modi',
    id='72e80285-7a5b-4404-a3a7-d575f1400e76',
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
        application_id='numquam',
        candidate_id='dolorum',
        created_at=dateutil.parser.isoparse('2021-08-23T14:57:18.247Z'),
        id='334ec1b7-81b3-46a0-8088-d100efada200',
        interview_id='eveniet',
        interviewer_id='hic',
        job_id='voluptatem',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.NO,
        updated_at=dateutil.parser.isoparse('2022-10-25T03:32:12.534Z'),
    ),
    connection_id='necessitatibus',
    id='b2164cf9-ab83-466c-b23f-fda9e06bee48',
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

