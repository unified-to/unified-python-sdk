# candidate

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDCandidateIDRequest(
    connection_id='voluptates',
    id='4825c1fc-0e11-45c8-8bff-918544ec42de',
)

res = s.candidate.delete_ats_connection_id_candidate_id(req, operations.DeleteAtsConnectionIDCandidateIDSecurity(
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


## get_ats_connection_id_candidate

List all candidates

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDCandidateRequest(
    connection_id='doloribus',
    limit=7737.11,
    offset=7833.97,
    order='accusamus',
    query='totam',
    sort='reiciendis',
    updated_gte=dateutil.parser.isoparse('2022-06-05T16:37:51.499Z'),
)

res = s.candidate.get_ats_connection_id_candidate(req, operations.GetAtsConnectionIDCandidateSecurity(
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
    connection_id='nihil',
    id='7773e635-62a7-4b40-8f05-e3d48fdaf313',
)

res = s.candidate.get_ats_connection_id_candidate_id(req, operations.GetAtsConnectionIDCandidateIDSecurity(
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
            address1='similique',
            address2='illo',
            city='Greeley',
            country='Yemen',
            country_code='SO',
            postal_code='21357-0614',
            region='sapiente',
            region_code='consequuntur',
        ),
        company_name='veniam',
        created_at=dateutil.parser.isoparse('2021-01-31T23:06:28.366Z'),
        emails=[
            shared.AtsEmail(
                email='Dylan.Gerhold72@yahoo.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='minima',
        id='6c11f6c3-7a51-4262-8383-5bbc05a23a45',
        image_url='quod',
        name='Tommie Schamberger',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'assumenda',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='officiis',
                type=shared.AtsTelephoneType.WORK,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2022-11-17T22:55:28.189Z'),
    ),
    connection_id='nobis',
    id='e2169e51-0019-4c6d-85e3-4762799bfbbe',
)

res = s.candidate.patch_ats_connection_id_candidate_id(req, operations.PatchAtsConnectionIDCandidateIDSecurity(
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
            address1='laboriosam',
            address2='unde',
            city='New Tyrel',
            country='Russian Federation',
            country_code='BV',
            postal_code='72976-9471',
            region='illum',
            region_code='nemo',
        ),
        company_name='illum',
        created_at=dateutil.parser.isoparse('2022-07-04T05:44:09.732Z'),
        emails=[
            shared.AtsEmail(
                email='Reynold_Walter32@yahoo.com',
                type=shared.AtsEmailType.OTHER,
            ),
        ],
        external_id='laborum',
        id='ea4c506a-8aa9-44c0-a644-cf5e9d9a4578',
        image_url='fuga',
        name='Edmund Boyle',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'laboriosam',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='doloremque',
                type=shared.AtsTelephoneType.WORK,
            ),
        ],
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2020-07-30T17:13:23.320Z'),
    ),
    connection_id='consequatur',
)

res = s.candidate.post_ats_connection_id_candidate(req, operations.PostAtsConnectionIDCandidateSecurity(
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
            address1='eaque',
            address2='architecto',
            city='Sawaynmouth',
            country='Azerbaijan',
            country_code='CH',
            postal_code='18705-9959',
            region='alias',
            region_code='asperiores',
        ),
        company_name='rem',
        created_at=dateutil.parser.isoparse('2022-08-15T01:59:03.683Z'),
        emails=[
            shared.AtsEmail(
                email='Winona45@hotmail.com',
                type=shared.AtsEmailType.HOME,
            ),
        ],
        external_id='eligendi',
        id='13e902c1-4125-4b09-a0a6-68151a472af9',
        image_url='sed',
        name='Kendra Hauck',
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'excepturi',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='maiores',
                type=shared.AtsTelephoneType.OTHER,
            ),
        ],
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-04-23T19:34:08.217Z'),
    ),
    connection_id='nemo',
    id='0cf876ff-b901-4c6e-8bb4-e243cf789ffa',
)

res = s.candidate.put_ats_connection_id_candidate_id(req, operations.PutAtsConnectionIDCandidateIDSecurity(
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

