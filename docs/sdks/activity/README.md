# Activity
(*activity*)

### Available Operations

* [create_ats_activity](#create_ats_activity) - Create an activity
* [get_ats_activity](#get_ats_activity) - Retrieve an activity
* [list_ats_activities](#list_ats_activities) - List all activities
* [patch_ats_activity](#patch_ats_activity) - Update an activity
* [remove_ats_activity](#remove_ats_activity) - Remove an activity
* [update_ats_activity](#update_ats_activity) - Update an activity

## create_ats_activity

Create an activity

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsActivityRequest(
    connection_id='<value>',
)

res = s.activity.create_ats_activity(req, operations.CreateAtsActivitySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsActivityRequest](../../models/operations/createatsactivityrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateAtsActivitySecurity](../../models/operations/createatsactivitysecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateAtsActivityResponse](../../models/operations/createatsactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_activity

Retrieve an activity

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsActivityRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.activity.get_ats_activity(req, operations.GetAtsActivitySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsActivityRequest](../../models/operations/getatsactivityrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetAtsActivitySecurity](../../models/operations/getatsactivitysecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetAtsActivityResponse](../../models/operations/getatsactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_activities

List all activities

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsActivitiesRequest(
    connection_id='<value>',
)

res = s.activity.list_ats_activities(req, operations.ListAtsActivitiesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_activities is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListAtsActivitiesRequest](../../models/operations/listatsactivitiesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListAtsActivitiesSecurity](../../models/operations/listatsactivitiessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListAtsActivitiesResponse](../../models/operations/listatsactivitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_activity

Update an activity

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsActivityRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.activity.patch_ats_activity(req, operations.PatchAtsActivitySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsActivityRequest](../../models/operations/patchatsactivityrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchAtsActivitySecurity](../../models/operations/patchatsactivitysecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchAtsActivityResponse](../../models/operations/patchatsactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_activity

Remove an activity

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsActivityRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.activity.remove_ats_activity(req, operations.RemoveAtsActivitySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsActivityRequest](../../models/operations/removeatsactivityrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveAtsActivitySecurity](../../models/operations/removeatsactivitysecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveAtsActivityResponse](../../models/operations/removeatsactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_activity

Update an activity

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsActivityRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.activity.update_ats_activity(req, operations.UpdateAtsActivitySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_activity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsActivityRequest](../../models/operations/updateatsactivityrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateAtsActivitySecurity](../../models/operations/updateatsactivitysecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateAtsActivityResponse](../../models/operations/updateatsactivityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
