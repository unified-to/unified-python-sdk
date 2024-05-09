# Scorecard
(*scorecard*)

### Available Operations

* [create_ats_scorecard](#create_ats_scorecard) - Create a scorecard
* [get_ats_scorecard](#get_ats_scorecard) - Retrieve a scorecard
* [list_ats_scorecards](#list_ats_scorecards) - List all scorecards
* [patch_ats_scorecard](#patch_ats_scorecard) - Update a scorecard
* [remove_ats_scorecard](#remove_ats_scorecard) - Remove a scorecard
* [update_ats_scorecard](#update_ats_scorecard) - Update a scorecard

## create_ats_scorecard

Create a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.create_ats_scorecard(request=operations.CreateAtsScorecardRequest(
    connection_id='<value>',
))

if res.ats_scorecard is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsScorecardRequest](../../models/operations/createatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateAtsScorecardResponse](../../models/operations/createatsscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ats_scorecard

Retrieve a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.get_ats_scorecard(request=operations.GetAtsScorecardRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_scorecard is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsScorecardRequest](../../models/operations/getatsscorecardrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetAtsScorecardResponse](../../models/operations/getatsscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_ats_scorecards

List all scorecards

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.list_ats_scorecards(request=operations.ListAtsScorecardsRequest(
    connection_id='<value>',
))

if res.ats_scorecards is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsScorecardsRequest](../../models/operations/listatsscorecardsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListAtsScorecardsResponse](../../models/operations/listatsscorecardsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_ats_scorecard

Update a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.patch_ats_scorecard(request=operations.PatchAtsScorecardRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_scorecard is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsScorecardRequest](../../models/operations/patchatsscorecardrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchAtsScorecardResponse](../../models/operations/patchatsscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## remove_ats_scorecard

Remove a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.remove_ats_scorecard(request=operations.RemoveAtsScorecardRequest(
    connection_id='<value>',
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsScorecardRequest](../../models/operations/removeatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveAtsScorecardResponse](../../models/operations/removeatsscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_ats_scorecard

Update a scorecard

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.scorecard.update_ats_scorecard(request=operations.UpdateAtsScorecardRequest(
    connection_id='<value>',
    id='<id>',
))

if res.ats_scorecard is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsScorecardRequest](../../models/operations/updateatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateAtsScorecardResponse](../../models/operations/updateatsscorecardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
