# Candidate
(*candidate*)

### Available Operations

* [delete_ats_connection_id_candidate_id](#delete_ats_connection_id_candidate_id) - Remove a candidate
* [get_ats_connection_id_candidate](#get_ats_connection_id_candidate) - List all candidates
* [get_ats_connection_id_candidate_id](#get_ats_connection_id_candidate_id) - Retrieve a candidate
* [patch_ats_connection_id_candidate_id](#patch_ats_connection_id_candidate_id) - Update a candidate
* [post_ats_connection_id_candidate](#post_ats_connection_id_candidate) - Create a candidate
* [put_ats_connection_id_candidate_id](#put_ats_connection_id_candidate_id) - Update a candidate

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

res = s.candidate.delete_ats_connection_id_candidate_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteAtsConnectionIDCandidateIDRequest](../../models/operations/deleteatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteAtsConnectionIDCandidateIDResponse](../../models/operations/deleteatsconnectionidcandidateidresponse.md)**


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

res = s.candidate.get_ats_connection_id_candidate(req)

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

res = s.candidate.get_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDCandidateIDRequest](../../models/operations/getatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDCandidateIDResponse](../../models/operations/getatsconnectionidcandidateidresponse.md)**


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

res = s.candidate.patch_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchAtsConnectionIDCandidateIDRequest](../../models/operations/patchatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchAtsConnectionIDCandidateIDResponse](../../models/operations/patchatsconnectionidcandidateidresponse.md)**


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

res = s.candidate.post_ats_connection_id_candidate(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAtsConnectionIDCandidateRequest](../../models/operations/postatsconnectionidcandidaterequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAtsConnectionIDCandidateResponse](../../models/operations/postatsconnectionidcandidateresponse.md)**


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

res = s.candidate.put_ats_connection_id_candidate_id(req)

if res.ats_candidate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutAtsConnectionIDCandidateIDRequest](../../models/operations/putatsconnectionidcandidateidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutAtsConnectionIDCandidateIDResponse](../../models/operations/putatsconnectionidcandidateidresponse.md)**

