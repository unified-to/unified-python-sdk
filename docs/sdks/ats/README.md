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
    candidate_id='turquoise',
    connection_id='Regional Bedfordshire',
    job_id='Northwest portal Electric',
    limit=576.8,
    offset=7467.13,
    order='Architect',
    query='loosely contingency',
    sort='female',
    updated_gte=dateutil.parser.isoparse('2023-09-05T13:59:23.348Z'),
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
    limit=2623.89,
    offset=7811.91,
    order='Mouse whether deploy',
    query='pink',
    sort='huzzah thistle',
    updated_gte=dateutil.parser.isoparse('2022-03-13T15:14:03.645Z'),
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
    application_id='Fresh Pickup converse',
    connection_id='vortals',
    limit=5167.08,
    offset=6488.61,
    order='Oregon Metal',
    query='Account',
    sort='haptic',
    updated_gte=dateutil.parser.isoparse('2021-09-23T19:46:35.825Z'),
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
    limit=3542.62,
    offset=5417.97,
    order='publisher',
    query='Folding',
    sort='Kip gross recontextualize',
    updated_gte=dateutil.parser.isoparse('2022-10-12T03:36:20.050Z'),
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
    application_id='Licensed deep',
    candidate_id='happily',
    connection_id='lunch accusamus',
    interview_id='for famously Southwest',
    limit=950.05,
    offset=6133.23,
    order='withdrawal',
    query='Bicycle copy Bronze',
    sort='ouch non ut',
    updated_gte=dateutil.parser.isoparse('2021-06-01T09:53:52.927Z'),
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
        applied_at=dateutil.parser.isoparse('2023-10-17T09:51:42.165Z'),
        candidate_id='North et beyond',
        created_at=dateutil.parser.isoparse('2023-01-08T08:26:22.845Z'),
        id='<ID>',
        job_id='ick Sausages Bronze',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2023-10-18T00:47:25.469Z'),
        rejected_reason='Avon Sum quis',
        source='Carolina Wooden Pop',
        status=shared.AtsApplicationStatus.HIRED,
        updated_at=dateutil.parser.isoparse('2021-07-20T22:05:46.009Z'),
    ),
    connection_id='Baby Paucek',
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
        address=shared.PropertyAtsCandidateAddress(
            address1='closely Goyette plus',
            address2='culpa',
            city='Darrinshire',
            country='Mongolia',
            country_code='GW',
            postal_code='05275',
            region='TLS calculating',
            region_code='up Argon Internal',
        ),
        company_name='Fadel, Schulist and Koss',
        created_at=dateutil.parser.isoparse('2022-12-09T07:16:54.728Z'),
        emails=[
            shared.AtsEmail(
                email='Gregory63@gmail.com',
                type=shared.AtsEmailType.OTHER,
            ),
        ],
        external_id='Elegant',
        id='<ID>',
        image_url='Tricycle Yttrium Hybrid',
        name='ornery whether',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'Cadillac',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='Marketing Cotton',
                type=shared.AtsTelephoneType.HOME,
            ),
        ],
        title='East',
        updated_at=dateutil.parser.isoparse('2023-10-31T11:53:36.953Z'),
    ),
    connection_id='redundant Tricycle unloose',
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
        application_id='SSD green pascal',
        candidate_id='Buckinghamshire example',
        created_at=dateutil.parser.isoparse('2021-08-24T08:30:07.073Z'),
        end_at=dateutil.parser.isoparse('2021-06-27T04:06:46.373Z'),
        external_event_xref='apropos Gadolinium',
        id='<ID>',
        job_id='transgender transmitting',
        location='Investor synthesizing',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2021-01-19T01:51:02.213Z'),
        status=shared.AtsInterviewStatus.AWAITING_FEEDBACK,
        updated_at=dateutil.parser.isoparse('2022-01-21T17:38:09.113Z'),
        user_ids=[
            'Honda',
        ],
    ),
    connection_id='Myrl Dram Trail',
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
            shared.AtsAddress(
                address1='Transexual',
                address2='Planner redundant Towels',
                city='Starkboro',
                country='Chad',
                country_code='NU',
                postal_code='22603',
                region='Cambridgeshire',
                region_code='Account Copernicium at',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2023-01-02T09:14:26.844Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Metical',
                frequency=shared.AtsCompensationFrequency.HOUR,
                max=1424.24,
                min=3626.17,
                type=shared.AtsCompensationType.SALARY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-03-16T15:29:37.822Z'),
        departments=[
            'Sports',
        ],
        description='Operative bi-directional capability',
        employment_type=shared.AtsJobEmploymentType.INTERN,
        hiring_manager_ids=[
            'Hop',
        ],
        id='<ID>',
        language_locale='hence gracefully invoice',
        name='Southeast vacantly Uranium',
        public_job_urls=[
            'Keith',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'happily',
        ],
        remote=False,
        status=shared.AtsJobStatus.OPEN,
        updated_at=dateutil.parser.isoparse('2023-08-04T07:33:03.088Z'),
    ),
    connection_id='Cis benchmark',
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
        application_id='Carter Hatchback functionalities',
        candidate_id='disagree gold New',
        created_at=dateutil.parser.isoparse('2023-05-08T15:11:07.692Z'),
        id='<ID>',
        interview_id='blue',
        interviewer_id='North Buckinghamshire blur',
        job_id='kelvin hack Fantastic',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.DEFINITELY_NO,
        updated_at=dateutil.parser.isoparse('2022-11-18T04:49:38.005Z'),
    ),
    connection_id='hacking meter',
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
        applied_at=dateutil.parser.isoparse('2021-10-26T15:24:28.979Z'),
        candidate_id='solid',
        created_at=dateutil.parser.isoparse('2022-09-13T17:17:33.049Z'),
        id='<ID>',
        job_id='Gloves Pizza virtual',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2023-12-27T18:41:56.821Z'),
        rejected_reason='Northwest Kids',
        source='Human Tasty Loan',
        status=shared.AtsApplicationStatus.NEW,
        updated_at=dateutil.parser.isoparse('2022-11-01T21:08:50.319Z'),
    ),
    connection_id='Jazz',
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
            address1='incubate',
            address2='azure Trans',
            city='Port Rory',
            country='El Salvador',
            country_code='CX',
            postal_code='54222-0235',
            region='modi fooey',
            region_code='Metal TCP incidunt',
        ),
        company_name='McCullough, Rosenbaum and Daugherty',
        created_at=dateutil.parser.isoparse('2023-02-07T05:55:59.357Z'),
        emails=[
            shared.AtsEmail(
                email='Eleanora.Rogahn44@hotmail.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='South though',
        id='<ID>',
        image_url='Pants',
        name='Raleigh',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'morph',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='lavender Sedan Folk',
                type=shared.AtsTelephoneType.OTHER,
            ),
        ],
        title='Savings panel',
        updated_at=dateutil.parser.isoparse('2022-02-09T15:32:35.578Z'),
    ),
    connection_id='Ngultrum red glean',
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
        application_id='round Hat Savings',
        candidate_id='Northeast',
        created_at=dateutil.parser.isoparse('2022-12-27T10:33:09.160Z'),
        end_at=dateutil.parser.isoparse('2021-11-12T23:57:19.974Z'),
        external_event_xref='platforms',
        id='<ID>',
        job_id='payment panel Identity',
        location='Northwest Buckinghamshire',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2022-11-02T05:07:18.592Z'),
        status=shared.AtsInterviewStatus.COMPLETE,
        updated_at=dateutil.parser.isoparse('2023-07-13T16:35:04.177Z'),
        user_ids=[
            'Chevrolet',
        ],
    ),
    connection_id='Shoes Northeast SMTP',
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
                address1='Forward',
                address2='Electric fuchsia kelvin',
                city='Fort Sibylmouth',
                country='Solomon Islands',
                country_code='DO',
                postal_code='39037',
                region='Rockford',
                region_code='Trafficway eaque athwart',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-04-22T19:01:40.265Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Gourde',
                frequency=shared.AtsCompensationFrequency.YEAR,
                max=5349.62,
                min=526.63,
                type=shared.AtsCompensationType.EQUITY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2021-04-02T18:44:02.642Z'),
        departments=[
            'Polonium',
        ],
        description='Progressive disintermediate matrix',
        employment_type=shared.AtsJobEmploymentType.INTERN,
        hiring_manager_ids=[
            'itaque',
        ],
        id='<ID>',
        language_locale='the joyfully',
        name='Other because harbor',
        public_job_urls=[
            'coil',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'JSON',
        ],
        remote=False,
        status=shared.AtsJobStatus.ARCHIVED,
        updated_at=dateutil.parser.isoparse('2022-05-24T04:21:24.567Z'),
    ),
    connection_id='Coordinator applications',
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
        application_id='female bah',
        candidate_id='if since',
        created_at=dateutil.parser.isoparse('2022-02-26T00:06:29.981Z'),
        id='<ID>',
        interview_id='invoice',
        interviewer_id='male',
        job_id='Accountability',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.STRONG_YES,
        updated_at=dateutil.parser.isoparse('2023-10-04T17:15:51.015Z'),
    ),
    connection_id='Legacy tan',
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
        applied_at=dateutil.parser.isoparse('2022-06-15T22:25:51.833Z'),
        candidate_id='farad Indianapolis',
        created_at=dateutil.parser.isoparse('2022-04-01T21:03:58.880Z'),
        id='<ID>',
        job_id='enable foreground',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2022-11-06T11:41:30.414Z'),
        rejected_reason='virtual North plum',
        source='Fort solid',
        status=shared.AtsApplicationStatus.SUBMITTED,
        updated_at=dateutil.parser.isoparse('2021-02-21T04:47:57.079Z'),
    ),
    connection_id='Southeast',
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
        address=shared.PropertyAtsCandidateAddress(
            address1='archive',
            address2='Specialist Kyat',
            city='New Dennis',
            country='Mauritius',
            country_code='TL',
            postal_code='49105-9909',
            region='copy olive',
            region_code='withdrawal cumque person',
        ),
        company_name='Kuhn and Sons',
        created_at=dateutil.parser.isoparse('2022-01-28T10:51:00.922Z'),
        emails=[
            shared.AtsEmail(
                email='Hester.Jenkins@gmail.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='Loan EXE',
        id='<ID>',
        image_url='deliver executive RSS',
        name='because aha black',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'program',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='empower exit Pangender',
                type=shared.AtsTelephoneType.MOBILE,
            ),
        ],
        title='Corporate anenst Electronic',
        updated_at=dateutil.parser.isoparse('2022-03-30T08:00:53.284Z'),
    ),
    connection_id='Flerovium azure',
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
        application_id='Generic capacitor',
        candidate_id='Road disbelieve',
        created_at=dateutil.parser.isoparse('2022-06-22T01:57:06.573Z'),
        end_at=dateutil.parser.isoparse('2022-05-28T02:29:32.144Z'),
        external_event_xref='architectures',
        id='<ID>',
        job_id='Casper 1080p South',
        location='program siemens Cis',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.isoparse('2021-03-14T15:20:41.084Z'),
        status=shared.AtsInterviewStatus.AWAITING_FEEDBACK,
        updated_at=dateutil.parser.isoparse('2023-07-14T19:59:39.905Z'),
        user_ids=[
            'East',
        ],
    ),
    connection_id='ASCII yet Hybrid',
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
            shared.AtsAddress(
                address1='cotton Washington',
                address2='rosin meanwhile male',
                city='East Sierra',
                country='Somalia',
                country_code='BQ',
                postal_code='63475-6123',
                region='lighthearted online Bicycle',
                region_code='robust',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2021-05-06T11:53:52.940Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Iranian Rial',
                frequency=shared.AtsCompensationFrequency.YEAR,
                max=5965.42,
                min=5273.81,
                type=shared.AtsCompensationType.BONUS,
            ),
        ],
        created_at=dateutil.parser.isoparse('2023-07-19T02:36:00.215Z'),
        departments=[
            'embrace',
        ],
        description='Programmable tertiary benchmark',
        employment_type=shared.AtsJobEmploymentType.CONTRACTOR,
        hiring_manager_ids=[
            'New',
        ],
        id='<ID>',
        language_locale='Facilitator Gasoline application',
        name='North impractical',
        public_job_urls=[
            'clamber',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'West',
        ],
        remote=False,
        status=shared.AtsJobStatus.CLOSED,
        updated_at=dateutil.parser.isoparse('2023-02-01T04:41:47.094Z'),
    ),
    connection_id='North',
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
        application_id='East Granite',
        candidate_id='South',
        created_at=dateutil.parser.isoparse('2022-03-02T12:33:41.490Z'),
        id='<ID>',
        interview_id='Texas Technetium hack',
        interviewer_id='Adventure Kyrgyz Organic',
        job_id='Home Dynamic Integration',
        raw=shared.PropertyAtsScorecardRaw(),
        recommendation=shared.AtsScorecardRecommendation.NO,
        updated_at=dateutil.parser.isoparse('2023-11-13T03:01:57.066Z'),
    ),
    connection_id='Transexual Manager Rap',
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

