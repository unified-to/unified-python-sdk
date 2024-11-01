# User
(*user*)

## Overview

### Available Operations

* [create_scim_users](#create_scim_users) - Create user
* [get_scim_users](#get_scim_users) - Get user
* [list_scim_users](#list_scim_users) - List users
* [patch_scim_users](#patch_scim_users) - Update user
* [remove_scim_users](#remove_scim_users) - Delete user
* [update_scim_users](#update_scim_users) - Update user

## create_scim_users

Create user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.create_scim_users(request=operations.CreateScimUsersRequest(
    connection_id='<id>',
))

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateScimUsersRequest](../../models/operations/createscimusersrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |

### Response

**[operations.CreateScimUsersResponse](../../models/operations/createscimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_scim_users

Get user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.get_scim_users(request=operations.GetScimUsersRequest(
    connection_id='<id>',
    id='<id>',
))

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetScimUsersRequest](../../models/operations/getscimusersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |

### Response

**[operations.GetScimUsersResponse](../../models/operations/getscimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_scim_users

List users

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.list_scim_users(request=operations.ListScimUsersRequest(
    connection_id='<id>',
))

if res.users is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListScimUsersRequest](../../models/operations/listscimusersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |

### Response

**[operations.ListScimUsersResponse](../../models/operations/listscimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_scim_users

Update user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.patch_scim_users(request=operations.PatchScimUsersRequest(
    connection_id='<id>',
    id='<id>',
))

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchScimUsersRequest](../../models/operations/patchscimusersrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[operations.PatchScimUsersResponse](../../models/operations/patchscimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_scim_users

Delete user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.remove_scim_users(request=operations.RemoveScimUsersRequest(
    connection_id='<id>',
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveScimUsersRequest](../../models/operations/removescimusersrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |

### Response

**[operations.RemoveScimUsersResponse](../../models/operations/removescimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_scim_users

Update user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.update_scim_users(request=operations.UpdateScimUsersRequest(
    connection_id='<id>',
    id='<id>',
))

if res.user is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateScimUsersRequest](../../models/operations/updatescimusersrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |

### Response

**[operations.UpdateScimUsersResponse](../../models/operations/updatescimusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |