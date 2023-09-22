# Candidate

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
    connection_id='consequuntur',
    id='defcce8f-1977-4773-a635-62a7b408f05e',
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
    connection_id='neque',
    limit=8163.65,
    offset=3071.73,
    order='quos',
    query='doloribus',
    sort='fugiat',
    updated_gte=dateutil.parser.isoparse('2021-01-28T10:50:17.967Z'),
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
    connection_id='velit',
    id='13a1f5fd-9425-49c0-b36f-25ea944f3b75',
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
            address1='ex',
            address2='minus',
            city='North Tylerview',
            country='Senegal',
            country_code='CZ',
            postal_code='63113',
            region='magni',
            region_code='incidunt',
        ),
        company_name='adipisci',
        created_at=dateutil.parser.isoparse('2022-07-24T00:20:38.347Z'),
        emails=[
            shared.AtsEmail(
                email='Melyna.Quigley36@yahoo.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='consequuntur',
        id='3a45cefc-5fde-410a-8ce2-169e510019c6',
        image_url='quibusdam',
        name='Corey Walker',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'dignissimos',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='laboriosam',
                type=shared.AtsTelephoneType.WORK,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2021-10-28T15:35:10.950Z'),
    ),
    connection_id='cum',
    id='fbbe6949-fb2b-4b4e-8ae6-c3d5db3adebd',
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
            address1='ad',
            address2='facere',
            city='Veumchester',
            country='Faroe Islands',
            country_code='SI',
            postal_code='03656',
            region='est',
            region_code='occaecati',
        ),
        company_name='labore',
        created_at=dateutil.parser.isoparse('2022-12-10T16:31:33.706Z'),
        emails=[
            shared.AtsEmail(
                email='Green75@gmail.com',
                type=shared.AtsEmailType.OTHER,
            ),
        ],
        external_id='nostrum',
        id='e9d9a457-8adc-41ac-a00d-ec001ac802e2',
        image_url='necessitatibus',
        name='Jose Mante',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'laudantium',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='maiores',
                type=shared.AtsTelephoneType.WORK,
            ),
        ],
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2022-10-06T09:51:21.294Z'),
    ),
    connection_id='suscipit',
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
            address1='earum',
            address2='doloribus',
            city='West Jade',
            country='Jersey',
            country_code='RO',
            postal_code='28501',
            region='impedit',
            region_code='beatae',
        ),
        company_name='incidunt',
        created_at=dateutil.parser.isoparse('2022-11-11T05:11:31.731Z'),
        emails=[
            shared.AtsEmail(
                email='Maybell.Abshire@yahoo.com',
                type=shared.AtsEmailType.WORK,
            ),
        ],
        external_id='id',
        id='668151a4-72af-4923-8594-9f83f350cf87',
        image_url='aliquid',
        name='Tommie Rohan Sr.',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'minus',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='commodi',
                type=shared.AtsTelephoneType.MOBILE,
            ),
        ],
        title='Miss',
        updated_at=dateutil.parser.isoparse('2021-08-12T13:33:07.290Z'),
    ),
    connection_id='modi',
    id='e243cf78-9ffa-4fed-a53e-5ae6e0ac184c',
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

