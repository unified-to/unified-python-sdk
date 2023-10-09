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
    list_id='Bronze cackle',
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
        emails=[
            shared.MarketingEmail(
                email='Otto93@yahoo.com',
            ),
        ],
        list_ids=[
            'Accounts',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'capacitor',
        ],
    ),
    connection_id='yowza online',
    id='<ID>',
    list_id='to XSS',
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
        emails=[
            shared.MarketingEmail(
                email='Tomas37@yahoo.com',
            ),
        ],
        list_ids=[
            'drive',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'virtual',
        ],
    ),
    connection_id='dolorum Wooden Granite',
    list_id='Green Convertible newton',
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
        emails=[
            shared.MarketingEmail(
                email='Mikayla_Nader@hotmail.com',
            ),
        ],
        list_ids=[
            'octave',
        ],
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'SMS',
        ],
    ),
    connection_id='East platforms',
    id='<ID>',
    list_id='Frozen',
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

