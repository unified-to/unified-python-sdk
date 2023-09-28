# Document
(*document*)

### Available Operations

* [delete_ats_connection_id_scorecard_id](#delete_ats_connection_id_scorecard_id) - Remove a scorecard
* [get_ats_connection_id_scorecard](#get_ats_connection_id_scorecard) - List all scorecards
* [get_ats_connection_id_scorecard_id](#get_ats_connection_id_scorecard_id) - Retrieve a scorecard
* [patch_ats_connection_id_scorecard_id](#patch_ats_connection_id_scorecard_id) - Update a scorecard
* [post_ats_connection_id_scorecard](#post_ats_connection_id_scorecard) - Create a scorecard
* [put_ats_connection_id_scorecard_id](#put_ats_connection_id_scorecard_id) - Update a scorecard

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

res = s.document.delete_ats_connection_id_scorecard_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDScorecardIDRequest](../../models/operations/deleteatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDScorecardIDResponse](../../models/operations/deleteatsconnectionidscorecardidresponse.md)**


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

res = s.document.get_ats_connection_id_scorecard(req)

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

res = s.document.get_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDScorecardIDRequest](../../models/operations/getatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDScorecardIDResponse](../../models/operations/getatsconnectionidscorecardidresponse.md)**


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

res = s.document.patch_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDScorecardIDRequest](../../models/operations/patchatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDScorecardIDResponse](../../models/operations/patchatsconnectionidscorecardidresponse.md)**


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

res = s.document.post_ats_connection_id_scorecard(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDScorecardRequest](../../models/operations/postatsconnectionidscorecardrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDScorecardResponse](../../models/operations/postatsconnectionidscorecardresponse.md)**


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

res = s.document.put_ats_connection_id_scorecard_id(req)

if res.ats_scorecard is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDScorecardIDRequest](../../models/operations/putatsconnectionidscorecardidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDScorecardIDResponse](../../models/operations/putatsconnectionidscorecardidresponse.md)**

