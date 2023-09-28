# Interview
(*interview*)

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

res = s.interview.delete_ats_connection_id_interview_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDInterviewIDRequest](../../models/operations/deleteatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDInterviewIDResponse](../../models/operations/deleteatsconnectionidinterviewidresponse.md)**


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

res = s.interview.get_ats_connection_id_interview(req)

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

res = s.interview.get_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDInterviewIDRequest](../../models/operations/getatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDInterviewIDResponse](../../models/operations/getatsconnectionidinterviewidresponse.md)**


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

res = s.interview.patch_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDInterviewIDRequest](../../models/operations/patchatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDInterviewIDResponse](../../models/operations/patchatsconnectionidinterviewidresponse.md)**


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

res = s.interview.post_ats_connection_id_interview(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDInterviewRequest](../../models/operations/postatsconnectionidinterviewrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDInterviewResponse](../../models/operations/postatsconnectionidinterviewresponse.md)**


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

res = s.interview.put_ats_connection_id_interview_id(req)

if res.ats_interview is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDInterviewIDRequest](../../models/operations/putatsconnectionidinterviewidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDInterviewIDResponse](../../models/operations/putatsconnectionidinterviewidresponse.md)**

