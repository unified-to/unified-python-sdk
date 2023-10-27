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
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateMartechListRequest(
    marketing_list=shared.MarketingList(
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='string',
)

res = s.martech.create_martech_list(req)

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateMartechListRequest](../../models/operations/createmartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateMartechListResponse](../../models/operations/createmartechlistresponse.md)**


## create_martech_member

Create a member

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

res = s.martech.create_martech_member(req)

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


## get_martech_list

Retrieve a list

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetMartechListRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.martech.get_martech_list(req)

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetMartechListRequest](../../models/operations/getmartechlistrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetMartechListResponse](../../models/operations/getmartechlistresponse.md)**


## get_martech_member

Retrieve a member

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetMartechMemberRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.martech.get_martech_member(req)

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


## list_martech_lists

List all lists

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

req = operations.ListMartechListsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.martech.list_martech_lists(req)

if res.marketing_lists is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListMartechListsRequest](../../models/operations/listmartechlistsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListMartechListsResponse](../../models/operations/listmartechlistsresponse.md)**


## list_martech_members

List all members

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

req = operations.ListMartechMembersRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.martech.list_martech_members(req)

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


## patch_martech_list

Update a list

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

req = operations.PatchMartechListRequest(
    marketing_list=shared.MarketingList(
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.martech.patch_martech_list(req)

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchMartechListRequest](../../models/operations/patchmartechlistrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchMartechListResponse](../../models/operations/patchmartechlistresponse.md)**


## patch_martech_member

Update a member

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

res = s.martech.patch_martech_member(req)

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


## remove_martech_list

Remove a list

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveMartechListRequest(
    connection_id='string',
    id='<ID>',
)

res = s.martech.remove_martech_list(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveMartechListRequest](../../models/operations/removemartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RemoveMartechListResponse](../../models/operations/removemartechlistresponse.md)**


## remove_martech_member

Remove member

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveMartechMemberRequest(
    connection_id='string',
    id='<ID>',
)

res = s.martech.remove_martech_member(req)

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


## update_martech_list

Update a list

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

req = operations.UpdateMartechListRequest(
    marketing_list=shared.MarketingList(
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.martech.update_martech_list(req)

if res.marketing_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateMartechListRequest](../../models/operations/updatemartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateMartechListResponse](../../models/operations/updatemartechlistresponse.md)**


## update_martech_member

Update a member

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

res = s.martech.update_martech_member(req)

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

