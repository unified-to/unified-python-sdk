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
    connection_id='expedita',
    id='855e889d-9ef9-432e-9000-a13ad8124208',
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
    connection_id='voluptates',
    id='fd234118-98e7-4387-9efb-e8baebabb794',
    list_id='voluptas',
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
    connection_id='neque',
    limit=4300.03,
    offset=9186.14,
    order='excepturi',
    query='ipsa',
    sort='velit',
    updated_gte=dateutil.parser.isoparse('2022-12-03T21:28:14.776Z'),
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
    connection_id='harum',
    id='b9763172-0b77-4a5a-9365-a79f15271f01',
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
    connection_id='quo',
    limit=34.09,
    list_id='illum',
    offset=2078.87,
    order='commodi',
    query='veritatis',
    sort='reiciendis',
    updated_gte=dateutil.parser.isoparse('2020-05-30T08:39:08.252Z'),
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
    connection_id='blanditiis',
    id='dc5effb4-53e9-4089-a871-fdb4d697bdd9',
    list_id='quisquam',
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
        created_at='molestias',
        id='85e43734-a5d7-42d9-add7-85be5e7afe55',
        name='Kristina Kozey',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2022-11-15T19:44:05.359Z'),
    ),
    connection_id='laudantium',
    id='1f44e3a2-3394-4a68-8c80-d30ff72164d0',
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
        created_at=dateutil.parser.isoparse('2021-11-04T00:39:44.335Z'),
        emails=[
            shared.MarketingEmail(
                email='Zora_Volkman@gmail.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='6553b89e-0009-4c66-92de-7b3562201a6a',
        list_ids=[
            'error',
        ],
        name='Ray O'Connell',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'harum',
        ],
        updated_at=dateutil.parser.isoparse('2022-04-25T11:53:38.687Z'),
    ),
    connection_id='ipsam',
    id='b908d4e3-0491-4aa3-9d4a-839f03bab77b',
    list_id='occaecati',
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
        created_at='quasi',
        id='8f031398-4507-4e0e-b9c7-e23ecb060465',
        name='Kate Cummerata',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2022-02-21T18:28:51.367Z'),
    ),
    connection_id='autem',
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
        created_at=dateutil.parser.isoparse('2021-11-13T23:02:04.436Z'),
        emails=[
            shared.MarketingEmail(
                email='Ines_Swift@yahoo.com',
                type=shared.MarketingEmailType.OTHER,
            ),
        ],
        id='8f7f002d-1986-4aa9-9d3a-1d32329e4583',
        list_ids=[
            'voluptate',
        ],
        name='Alberto Wisozk',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'fugiat',
        ],
        updated_at=dateutil.parser.isoparse('2022-04-07T09:46:27.417Z'),
    ),
    connection_id='harum',
    list_id='inventore',
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
        created_at='aut',
        id='e255fdc4-80d6-4e33-8867-5cbf186856a7',
        name='Jaime Conroy',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2021-03-04T08:28:08.196Z'),
    ),
    connection_id='assumenda',
    id='0fc282c6-66af-43c3-b558-9bea5d264e41',
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
        created_at=dateutil.parser.isoparse('2022-06-10T00:17:48.769Z'),
        emails=[
            shared.MarketingEmail(
                email='Mark54@hotmail.com',
                type=shared.MarketingEmailType.WORK,
            ),
        ],
        id='2e513f6d-9d2a-4d37-8309-9077c10b6879',
        list_ids=[
            'sed',
        ],
        name='Lucy Fahey',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'nihil',
        ],
        updated_at=dateutil.parser.isoparse('2022-03-31T07:19:18.789Z'),
    ),
    connection_id='rem',
    id='860543c0-a304-49c3-8f6c-0276e7b21bad',
    list_id='provident',
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

