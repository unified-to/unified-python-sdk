# Martech
(*martech*)

### Available Operations

* [create_martech_list](#create_martech_list) - Create a list
* [create_martech_member](#create_martech_member) - Create a member
* [get_martech_list](#get_martech_list) - Retrieve a list
* [get_martech_member](#get_martech_member) - Retrieve a member
* [list_martech_lists](#list_martech_lists) - List all lists
* [list_martech_members](#list_martech_members) - List all members
* [patch_martech_list](#patch_martech_list) - Update a list
* [patch_martech_member](#patch_martech_member) - Update a member
* [remove_martech_list](#remove_martech_list) - Remove a list
* [remove_martech_member](#remove_martech_member) - Remove member
* [update_martech_list](#update_martech_list) - Update a list
* [update_martech_member](#update_martech_member) - Update a member

## create_martech_list

Create a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateMartechListRequest(
    connection_id='<value>',
)

res = s.martech.create_martech_list(req, operations.CreateMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateMartechListRequest](../../models/operations/createmartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateMartechListSecurity](../../models/operations/createmartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateMartechListResponse](../../models/operations/createmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_martech_member

Create a member

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateMartechMemberRequest(
    connection_id='<value>',
)

res = s.martech.create_martech_member(req, operations.CreateMartechMemberSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateMartechMemberRequest](../../models/operations/createmartechmemberrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.CreateMartechMemberSecurity](../../models/operations/createmartechmembersecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.CreateMartechMemberResponse](../../models/operations/createmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_martech_list

Retrieve a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.get_martech_list(req, operations.GetMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetMartechListRequest](../../models/operations/getmartechlistrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetMartechListSecurity](../../models/operations/getmartechlistsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetMartechListResponse](../../models/operations/getmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_martech_member

Retrieve a member

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetMartechMemberRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.get_martech_member(req, operations.GetMartechMemberSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMartechMemberRequest](../../models/operations/getmartechmemberrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.GetMartechMemberSecurity](../../models/operations/getmartechmembersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.GetMartechMemberResponse](../../models/operations/getmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_martech_lists

List all lists

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListMartechListsRequest(
    connection_id='<value>',
)

res = s.martech.list_martech_lists(req, operations.ListMartechListsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_lists is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListMartechListsRequest](../../models/operations/listmartechlistsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListMartechListsSecurity](../../models/operations/listmartechlistssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListMartechListsResponse](../../models/operations/listmartechlistsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_martech_members

List all members

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListMartechMembersRequest(
    connection_id='<value>',
)

res = s.martech.list_martech_members(req, operations.ListMartechMembersSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_members is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListMartechMembersRequest](../../models/operations/listmartechmembersrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ListMartechMembersSecurity](../../models/operations/listmartechmemberssecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ListMartechMembersResponse](../../models/operations/listmartechmembersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_martech_list

Update a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.patch_martech_list(req, operations.PatchMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchMartechListRequest](../../models/operations/patchmartechlistrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchMartechListSecurity](../../models/operations/patchmartechlistsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchMartechListResponse](../../models/operations/patchmartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_martech_member

Update a member

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchMartechMemberRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.patch_martech_member(req, operations.PatchMartechMemberSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchMartechMemberRequest](../../models/operations/patchmartechmemberrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.PatchMartechMemberSecurity](../../models/operations/patchmartechmembersecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.PatchMartechMemberResponse](../../models/operations/patchmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_martech_list

Remove a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.remove_martech_list(req, operations.RemoveMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveMartechListRequest](../../models/operations/removemartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveMartechListSecurity](../../models/operations/removemartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveMartechListResponse](../../models/operations/removemartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_martech_member

Remove member

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveMartechMemberRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.remove_martech_member(req, operations.RemoveMartechMemberSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveMartechMemberRequest](../../models/operations/removemartechmemberrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.RemoveMartechMemberSecurity](../../models/operations/removemartechmembersecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.RemoveMartechMemberResponse](../../models/operations/removemartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_martech_list

Update a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateMartechListRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.update_martech_list(req, operations.UpdateMartechListSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateMartechListRequest](../../models/operations/updatemartechlistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateMartechListSecurity](../../models/operations/updatemartechlistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateMartechListResponse](../../models/operations/updatemartechlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_martech_member

Update a member

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateMartechMemberRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.martech.update_martech_member(req, operations.UpdateMartechMemberSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateMartechMemberRequest](../../models/operations/updatemartechmemberrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.UpdateMartechMemberSecurity](../../models/operations/updatemartechmembersecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.UpdateMartechMemberResponse](../../models/operations/updatemartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
