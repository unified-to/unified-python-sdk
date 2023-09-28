# Martech
(*martech*)

### Available Operations

* [delete_martech_connection_id_list_id](#delete_martech_connection_id_list_id) - Remove a list
* [delete_martech_connection_id_list_id_member_id](#delete_martech_connection_id_list_id_member_id) - Remove member from a list
* [get_martech_connection_id_list](#get_martech_connection_id_list) - List all lists
* [get_martech_connection_id_list_id](#get_martech_connection_id_list_id) - Retrieve a list
* [get_martech_connection_id_list_id_member](#get_martech_connection_id_list_id_member) - List all members in a list
* [get_martech_connection_id_list_id_member_id](#get_martech_connection_id_list_id_member_id) - Retrieve a member from a list
* [patch_martech_connection_id_list_id](#patch_martech_connection_id_list_id) - Update a list
* [patch_martech_connection_id_list_id_member_id](#patch_martech_connection_id_list_id_member_id) - Update a member in a list
* [post_martech_connection_id_list](#post_martech_connection_id_list) - Create a list
* [post_martech_connection_id_list_id_member](#post_martech_connection_id_list_id_member) - Create a member in a list
* [put_martech_connection_id_list_id](#put_martech_connection_id_list_id) - Update a list
* [put_martech_connection_id_list_id_member_id](#put_martech_connection_id_list_id_member_id) - Update a member in a list

## delete_martech_connection_id_list_id

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

req = operations.DeleteMartechConnectionIDListIDRequest(
    connection_id='Minivan',
    id='<ID>',
)

res = s.martech.delete_martech_connection_id_list_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteMartechConnectionIDListIDRequest](../../models/operations/deletemartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.DeleteMartechConnectionIDListIDResponse](../../models/operations/deletemartechconnectionidlistidresponse.md)**


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

res = s.martech.delete_martech_connection_id_list_id_member_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.DeleteMartechConnectionIDListIDMemberIDRequest](../../models/operations/deletemartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.DeleteMartechConnectionIDListIDMemberIDResponse](../../models/operations/deletemartechconnectionidlistidmemberidresponse.md)**


## get_martech_connection_id_list

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

req = operations.GetMartechConnectionIDListRequest(
    connection_id='silver DeKalb',
    limit=9799.48,
    offset=4800.63,
    order='Bedfordshire',
    query='Hip Pass',
    sort='since',
    updated_gte=dateutil.parser.isoparse('2022-03-26T19:40:00.770Z'),
)

res = s.martech.get_martech_connection_id_list(req)

if res.marketing_lists is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetMartechConnectionIDListRequest](../../models/operations/getmartechconnectionidlistrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetMartechConnectionIDListResponse](../../models/operations/getmartechconnectionidlistresponse.md)**


## get_martech_connection_id_list_id

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

req = operations.GetMartechConnectionIDListIDRequest(
    connection_id='Jewelery orange',
    id='<ID>',
)

res = s.martech.get_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetMartechConnectionIDListIDRequest](../../models/operations/getmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetMartechConnectionIDListIDResponse](../../models/operations/getmartechconnectionidlistidresponse.md)**


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

res = s.martech.get_martech_connection_id_list_id_member(req)

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

res = s.martech.get_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetMartechConnectionIDListIDMemberIDRequest](../../models/operations/getmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetMartechConnectionIDListIDMemberIDResponse](../../models/operations/getmartechconnectionidlistidmemberidresponse.md)**


## patch_martech_connection_id_list_id

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

req = operations.PatchMartechConnectionIDListIDRequest(
    marketing_list=shared.MarketingList(
        created_at='Funk',
        id='<ID>',
        name='lime Fiat',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2021-01-15T20:51:24.192Z'),
    ),
    connection_id='male sheepishly Intelligent',
    id='<ID>',
)

res = s.martech.patch_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchMartechConnectionIDListIDRequest](../../models/operations/patchmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PatchMartechConnectionIDListIDResponse](../../models/operations/patchmartechconnectionidlistidresponse.md)**


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

res = s.martech.patch_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PatchMartechConnectionIDListIDMemberIDRequest](../../models/operations/patchmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PatchMartechConnectionIDListIDMemberIDResponse](../../models/operations/patchmartechconnectionidlistidmemberidresponse.md)**


## post_martech_connection_id_list

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

req = operations.PostMartechConnectionIDListRequest(
    marketing_list=shared.MarketingList(
        created_at='synergistic Transexual Steel',
        id='<ID>',
        name='Virginia whoever Bicycle',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2023-04-27T09:56:39.589Z'),
    ),
    connection_id='Hybrid',
)

res = s.martech.post_martech_connection_id_list(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostMartechConnectionIDListRequest](../../models/operations/postmartechconnectionidlistrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostMartechConnectionIDListResponse](../../models/operations/postmartechconnectionidlistresponse.md)**


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

res = s.martech.post_martech_connection_id_list_id_member(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PostMartechConnectionIDListIDMemberRequest](../../models/operations/postmartechconnectionidlistidmemberrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PostMartechConnectionIDListIDMemberResponse](../../models/operations/postmartechconnectionidlistidmemberresponse.md)**


## put_martech_connection_id_list_id

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

req = operations.PutMartechConnectionIDListIDRequest(
    marketing_list=shared.MarketingList(
        created_at='Underpass initiatives',
        id='<ID>',
        name='North Progressive Assistant',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2023-10-03T22:31:39.028Z'),
    ),
    connection_id='Security Legacy onto',
    id='<ID>',
)

res = s.martech.put_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutMartechConnectionIDListIDRequest](../../models/operations/putmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PutMartechConnectionIDListIDResponse](../../models/operations/putmartechconnectionidlistidresponse.md)**


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

res = s.martech.put_martech_connection_id_list_id_member_id(req)

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PutMartechConnectionIDListIDMemberIDRequest](../../models/operations/putmartechconnectionidlistidmemberidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PutMartechConnectionIDListIDMemberIDResponse](../../models/operations/putmartechconnectionidlistidmemberidresponse.md)**

