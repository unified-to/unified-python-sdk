# Member
(*member*)

### Available Operations

* [create_martech_member](#create_martech_member) - Create a member
* [get_martech_member](#get_martech_member) - Retrieve a member
* [list_martech_members](#list_martech_members) - List all members
* [patch_martech_member](#patch_martech_member) - Update a member
* [remove_martech_member](#remove_martech_member) - Remove member
* [update_martech_member](#update_martech_member) - Update a member

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

res = s.member.create_martech_member(req, operations.CreateMartechMemberSecurity(
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

res = s.member.get_martech_member(req, operations.GetMartechMemberSecurity(
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

res = s.member.list_martech_members(req, operations.ListMartechMembersSecurity(
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

res = s.member.patch_martech_member(req, operations.PatchMartechMemberSecurity(
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

res = s.member.remove_martech_member(req, operations.RemoveMartechMemberSecurity(
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

res = s.member.update_martech_member(req, operations.UpdateMartechMemberSecurity(
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
