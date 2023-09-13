# interview

### Available Operations

* [delete_ats_connection_id_interview_id](#delete_ats_connection_id_interview_id) - Remove a interview
* [get_ats_connection_id_interview](#get_ats_connection_id_interview) - List all interviews
* [get_ats_connection_id_interview_id](#get_ats_connection_id_interview_id) - Retrieve a interview
* [patch_ats_connection_id_interview_id](#patch_ats_connection_id_interview_id) - Update a interview
* [post_ats_connection_id_interview](#post_ats_connection_id_interview) - Create a interview
* [put_ats_connection_id_interview_id](#put_ats_connection_id_interview_id) - Update a interview

## delete_ats_connection_id_interview_id

Remove a interview

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDInterviewIDRequest(
    connection_id='minus',
    id='7dda70ec-60e6-4075-894d-61c14cd90227',
)

res = s.interview.delete_ats_connection_id_interview_id(req, operations.DeleteAtsConnectionIDInterviewIDSecurity(
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


## get_ats_connection_id_interview

List all interviews

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDInterviewRequest(
    application_id='recusandae',
    connection_id='neque',
    limit=4704,
    offset=7513.92,
    order='eaque',
    query='facere',
    sort='iste',
    updated_gte=dateutil.parser.parse('2022-07-18').date(),
)

res = s.interview.get_ats_connection_id_interview(req, operations.GetAtsConnectionIDInterviewSecurity(
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
    connection_id='reiciendis',
    id='1a5491ab-e975-41b1-86d2-3e03e69815aa',
)

res = s.interview.get_ats_connection_id_interview_id(req, operations.GetAtsConnectionIDInterviewIDSecurity(
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
        application_id='officiis',
        candidate_id='omnis',
        created_at=dateutil.parser.parse('2021-02-14').date(),
        end_at=dateutil.parser.parse('2020-07-04').date(),
        external_event_xref='necessitatibus',
        id='9e729c9d-4f2d-48a4-8640-ca60db73a2f9',
        job_id='dolorem',
        location='maiores',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.parse('2022-07-30').date(),
        status=shared.AtsInterviewStatus.AWAITING_FEEDBACK,
        updated_at=dateutil.parser.parse('2020-08-23').date(),
        user_ids=[
            'quae',
        ],
    ),
    connection_id='possimus',
    id='8da56122-026a-4b8f-a774-85c1976af980',
)

res = s.interview.patch_ats_connection_id_interview_id(req, operations.PatchAtsConnectionIDInterviewIDSecurity(
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
        application_id='nulla',
        candidate_id='culpa',
        created_at=dateutil.parser.parse('2022-05-03').date(),
        end_at=dateutil.parser.parse('2022-07-01').date(),
        external_event_xref='unde',
        id='fc44db27-4530-4e5c-87c6-d0cbcfdcd334',
        job_id='facilis',
        location='autem',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.parse('2021-10-11').date(),
        status=shared.AtsInterviewStatus.SCHEDULED,
        updated_at=dateutil.parser.parse('2022-04-07').date(),
        user_ids=[
            'minus',
        ],
    ),
    connection_id='repudiandae',
)

res = s.interview.post_ats_connection_id_interview(req, operations.PostAtsConnectionIDInterviewSecurity(
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
        application_id='quisquam',
        candidate_id='mollitia',
        created_at=dateutil.parser.parse('2022-04-26').date(),
        end_at=dateutil.parser.parse('2022-04-30').date(),
        external_event_xref='voluptates',
        id='e5e0da8b-9af6-4ad0-9486-e7b413cbe2d1',
        job_id='molestiae',
        location='ea',
        raw=shared.PropertyAtsInterviewRaw(),
        start_at=dateutil.parser.parse('2020-07-27').date(),
        status=shared.AtsInterviewStatus.SCHEDULED,
        updated_at=dateutil.parser.parse('2022-03-28').date(),
        user_ids=[
            'adipisci',
        ],
    ),
    connection_id='pariatur',
    id='40f61d17-1157-4cbe-9ee4-f7211840772f',
)

res = s.interview.put_ats_connection_id_interview_id(req, operations.PutAtsConnectionIDInterviewIDSecurity(
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

