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
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateMartechMemberRequest(
    marketing_member=shared.MarketingMember(
        emails=[
            shared.MarketingEmail(
                email='Eldridge.Marvin@gmail.com',
            ),
        ],
        list_ids=[
            'string',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
)

res = s.member.create_martech_member(req)

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateMartechMemberRequest](../../models/operations/createmartechmemberrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreateMartechMemberResponse](../../models/operations/createmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_martech_member

Retrieve a member

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetMartechMemberRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.member.get_martech_member(req)

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetMartechMemberRequest](../../models/operations/getmartechmemberrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetMartechMemberResponse](../../models/operations/getmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_martech_members

List all members

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListMartechMembersRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.member.list_martech_members(req)

if res.marketing_members is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListMartechMembersRequest](../../models/operations/listmartechmembersrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListMartechMembersResponse](../../models/operations/listmartechmembersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_martech_member

Update a member

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchMartechMemberRequest(
    marketing_member=shared.MarketingMember(
        emails=[
            shared.MarketingEmail(
                email='Shana_Boyle@yahoo.com',
            ),
        ],
        list_ids=[
            'string',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.member.patch_martech_member(req)

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchMartechMemberRequest](../../models/operations/patchmartechmemberrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PatchMartechMemberResponse](../../models/operations/patchmartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_martech_member

Remove member

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveMartechMemberRequest(
    connection_id='string',
    id='<ID>',
)

res = s.member.remove_martech_member(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveMartechMemberRequest](../../models/operations/removemartechmemberrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.RemoveMartechMemberResponse](../../models/operations/removemartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_martech_member

Update a member

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateMartechMemberRequest(
    marketing_member=shared.MarketingMember(
        emails=[
            shared.MarketingEmail(
                email='Antonette.Kerluke@hotmail.com',
            ),
        ],
        list_ids=[
            'string',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.member.update_martech_member(req)

if res.marketing_member is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateMartechMemberRequest](../../models/operations/updatemartechmemberrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.UpdateMartechMemberResponse](../../models/operations/updatemartechmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
