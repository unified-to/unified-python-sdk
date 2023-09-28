# Member
(*member*)

### Available Operations

* [delete_martech_connection_id_list_id_member_id](#delete_martech_connection_id_list_id_member_id) - Remove member from a list
* [get_martech_connection_id_list_id_member](#get_martech_connection_id_list_id_member) - List all members in a list
* [get_martech_connection_id_list_id_member_id](#get_martech_connection_id_list_id_member_id) - Retrieve a member from a list
* [patch_martech_connection_id_list_id_member_id](#patch_martech_connection_id_list_id_member_id) - Update a member in a list
* [post_martech_connection_id_list_id_member](#post_martech_connection_id_list_id_member) - Create a member in a list
* [put_martech_connection_id_list_id_member_id](#put_martech_connection_id_list_id_member_id) - Update a member in a list

## delete_martech_connection_id_list_id_member_id

Remove member from a list

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteMartechConnectionIDListIDMemberIDRequest(
    connection_id='Southwest fib',
    id='<ID>',
    list_id='pascal',
)

res = s.member.delete_martech_connection_id_list_id_member_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.DeleteMartechConnectionIDListIDMemberIDRequest](../../models/operations/deletemartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.DeleteMartechConnectionIDListIDMemberIDResponse](../../models/operations/deletemartechconnectionidlistidmemberidresponse.md)**


## get_martech_connection_id_list_id_member

List all members in a list

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

req = operations.GetMartechConnectionIDListIDMemberRequest(
    connection_id='fuchsia economics',
    limit=3725.92,
    list_id='Southwest',
    offset=1114.27,
    order='emulation',
    query='male male',
    sort='Arizona Oklahoma Land',
    updated_gte=dateutil.parser.isoparse('2021-03-19T13:12:48.332Z'),
)

res = s.member.get_martech_connection_id_list_id_member(req)

if res.marketing_members is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetMartechConnectionIDListIDMemberRequest](../../models/operations/getmartechconnectionidlistidmemberrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetMartechConnectionIDListIDMemberResponse](../../models/operations/getmartechconnectionidlistidmemberresponse.md)**


## get_martech_connection_id_list_id_member_id

Retrieve a member from a list

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetMartechConnectionIDListIDMemberIDRequest(
    connection_id='male',
    id='<ID>',
    list_id='Gasoline Home allot',
)

res = s.member.get_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetMartechConnectionIDListIDMemberIDRequest](../../models/operations/getmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetMartechConnectionIDListIDMemberIDResponse](../../models/operations/getmartechconnectionidlistidmemberidresponse.md)**


## patch_martech_connection_id_list_id_member_id

Update a member in a list

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

req = operations.PatchMartechConnectionIDListIDMemberIDRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.isoparse('2022-06-21T07:15:04.418Z'),
        emails=[
            shared.MarketingEmail(
                email='Zula_Bogan76@hotmail.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        list_ids=[
            'gadzooks',
        ],
        name='Haven Hatchback',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'mutiny',
        ],
        updated_at=dateutil.parser.isoparse('2021-08-13T23:04:27.910Z'),
    ),
    connection_id='female',
    id='<ID>',
    list_id='yellow overriding Rock',
)

res = s.member.patch_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PatchMartechConnectionIDListIDMemberIDRequest](../../models/operations/patchmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PatchMartechConnectionIDListIDMemberIDResponse](../../models/operations/patchmartechconnectionidlistidmemberidresponse.md)**


## post_martech_connection_id_list_id_member

Create a member in a list

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

req = operations.PostMartechConnectionIDListIDMemberRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.isoparse('2022-12-27T02:49:51.488Z'),
        emails=[
            shared.MarketingEmail(
                email='Esta.Dach@hotmail.com',
                type=shared.MarketingEmailType.OTHER,
            ),
        ],
        id='<ID>',
        list_ids=[
            'virtual',
        ],
        name='dolorum Wooden Granite',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'Road',
        ],
        updated_at=dateutil.parser.isoparse('2021-06-09T19:47:01.060Z'),
    ),
    connection_id='Pennsylvania leverage sheath',
    list_id='parse exercitationem',
)

res = s.member.post_martech_connection_id_list_id_member(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PostMartechConnectionIDListIDMemberRequest](../../models/operations/postmartechconnectionidlistidmemberrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PostMartechConnectionIDListIDMemberResponse](../../models/operations/postmartechconnectionidlistidmemberresponse.md)**


## put_martech_connection_id_list_id_member_id

Update a member in a list

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

req = operations.PutMartechConnectionIDListIDMemberIDRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.isoparse('2023-09-24T05:00:50.743Z'),
        emails=[
            shared.MarketingEmail(
                email='Lorenz_Kautzer@hotmail.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        list_ids=[
            'SMS',
        ],
        name='East platforms',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'Estonia',
        ],
        updated_at=dateutil.parser.isoparse('2023-01-20T05:09:32.775Z'),
    ),
    connection_id='following quia Intelligent',
    id='<ID>',
    list_id='Cab',
)

res = s.member.put_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PutMartechConnectionIDListIDMemberIDRequest](../../models/operations/putmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PutMartechConnectionIDListIDMemberIDResponse](../../models/operations/putmartechconnectionidlistidmemberidresponse.md)**

