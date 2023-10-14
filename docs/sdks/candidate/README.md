# Candidate
(*candidate*)

### Available Operations

* [create_ats_candidate](#create_ats_candidate) - Create a candidate
* [get_ats_candidate](#get_ats_candidate) - Retrieve a candidate
* [list_ats_candidates](#list_ats_candidates) - List all candidates
* [patch_ats_candidate](#patch_ats_candidate) - Update a candidate
* [remove_ats_candidate](#remove_ats_candidate) - Remove a candidate
* [update_ats_candidate](#update_ats_candidate) - Update a candidate

## create_ats_candidate

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

req = operations.CreateAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Robin_Feeney@hotmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'radian',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='but Pop fluid',
            ),
        ],
    ),
    connection_id='bypass Creative Legacy',
    fields_=[
        'Bronze',
    ],
)

res = s.candidate.create_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsCandidateRequest](../../models/operations/createatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAtsCandidateResponse](../../models/operations/createatscandidateresponse.md)**


## get_ats_candidate

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

req = operations.GetAtsCandidateRequest(
    connection_id='Markets',
    fields_=[
        'payment',
    ],
    id='<ID>',
)

res = s.candidate.get_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsCandidateRequest](../../models/operations/getatscandidaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetAtsCandidateResponse](../../models/operations/getatscandidateresponse.md)**


## list_ats_candidates

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

req = operations.ListAtsCandidatesRequest(
    connection_id='mole clearly',
    fields_=[
        'Van',
    ],
)

res = s.candidate.list_ats_candidates(req)

if res.ats_candidates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsCandidatesRequest](../../models/operations/listatscandidatesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListAtsCandidatesResponse](../../models/operations/listatscandidatesresponse.md)**


## patch_ats_candidate

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

req = operations.PatchAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Tracy.Collins13@gmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'Credit',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='payment Books',
            ),
        ],
    ),
    connection_id='World Van transitional',
    fields_=[
        'green',
    ],
    id='<ID>',
)

res = s.candidate.patch_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsCandidateRequest](../../models/operations/patchatscandidaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchAtsCandidateResponse](../../models/operations/patchatscandidateresponse.md)**


## remove_ats_candidate

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

req = operations.RemoveAtsCandidateRequest(
    connection_id='Accountability Recumbent Ball',
    id='<ID>',
)

res = s.candidate.remove_ats_candidate(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsCandidateRequest](../../models/operations/removeatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsCandidateResponse](../../models/operations/removeatscandidateresponse.md)**


## update_ats_candidate

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

req = operations.UpdateAtsCandidateRequest(
    ats_candidate=shared.AtsCandidate(
        address=shared.PropertyAtsCandidateAddress(),
        emails=[
            shared.AtsEmail(
                email='Gaetano86@hotmail.com',
            ),
        ],
        raw=shared.PropertyAtsCandidateRaw(),
        tags=[
            'B2C',
        ],
        telephones=[
            shared.AtsTelephone(
                telephone='DNS monetize Dynamic',
            ),
        ],
    ),
    connection_id='Zackery male Gloves',
    fields_=[
        'threadbare',
    ],
    id='<ID>',
)

res = s.candidate.update_ats_candidate(req)

if res.ats_candidate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsCandidateRequest](../../models/operations/updateatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateAtsCandidateResponse](../../models/operations/updateatscandidateresponse.md)**

