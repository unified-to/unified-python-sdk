# Application
(*application*)

### Available Operations

* [create_ats_application](#create_ats_application) - Create an application
* [get_ats_application](#get_ats_application) - Retrieve an application
* [list_ats_applications](#list_ats_applications) - List all applications
* [patch_ats_application](#patch_ats_application) - Update an application
* [remove_ats_application](#remove_ats_application) - Remove an application
* [update_ats_application](#update_ats_application) - Update an application

## create_ats_application

Create an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAtsApplicationRequest(
    connection_id='<value>',
)

res = s.application.create_ats_application(req, operations.CreateAtsApplicationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAtsApplicationRequest](../../models/operations/createatsapplicationrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.CreateAtsApplicationSecurity](../../models/operations/createatsapplicationsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.CreateAtsApplicationResponse](../../models/operations/createatsapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ats_application

Retrieve an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsApplicationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.application.get_ats_application(req, operations.GetAtsApplicationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAtsApplicationRequest](../../models/operations/getatsapplicationrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetAtsApplicationSecurity](../../models/operations/getatsapplicationsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetAtsApplicationResponse](../../models/operations/getatsapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ats_applications

List all applications

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAtsApplicationsRequest(
    connection_id='<value>',
)

res = s.application.list_ats_applications(req, operations.ListAtsApplicationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_applications is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAtsApplicationsRequest](../../models/operations/listatsapplicationsrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ListAtsApplicationsSecurity](../../models/operations/listatsapplicationssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ListAtsApplicationsResponse](../../models/operations/listatsapplicationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ats_application

Update an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAtsApplicationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.application.patch_ats_application(req, operations.PatchAtsApplicationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAtsApplicationRequest](../../models/operations/patchatsapplicationrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.PatchAtsApplicationSecurity](../../models/operations/patchatsapplicationsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.PatchAtsApplicationResponse](../../models/operations/patchatsapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ats_application

Remove an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAtsApplicationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.application.remove_ats_application(req, operations.RemoveAtsApplicationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAtsApplicationRequest](../../models/operations/removeatsapplicationrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.RemoveAtsApplicationSecurity](../../models/operations/removeatsapplicationsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.RemoveAtsApplicationResponse](../../models/operations/removeatsapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ats_application

Update an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAtsApplicationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.application.update_ats_application(req, operations.UpdateAtsApplicationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ats_application is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAtsApplicationRequest](../../models/operations/updateatsapplicationrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.UpdateAtsApplicationSecurity](../../models/operations/updateatsapplicationsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.UpdateAtsApplicationResponse](../../models/operations/updateatsapplicationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
