# member

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteMartechConnectionIDListIDMemberIDRequest(
    connection_id='alias',
    id='d2743fd6-c2a1-40e6-8297-8ec256a5b092',
    list_id='magni',
)

res = s.member.delete_martech_connection_id_list_id_member_id(req, operations.DeleteMartechConnectionIDListIDMemberIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.DeleteMartechConnectionIDListIDMemberIDRequest](../../models/operations/deletemartechconnectionidlistidmemberidrequest.md)   | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `security`                                                                                                                               | [operations.DeleteMartechConnectionIDListIDMemberIDSecurity](../../models/operations/deletemartechconnectionidlistidmemberidsecurity.md) | :heavy_check_mark:                                                                                                                       | The security requirements to use for the request.                                                                                        |


### Response

**[operations.DeleteMartechConnectionIDListIDMemberIDResponse](../../models/operations/deletemartechconnectionidlistidmemberidresponse.md)**


## get_martech_connection_id_list_id_member

List all members in a list

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetMartechConnectionIDListIDMemberRequest(
    connection_id='iure',
    limit=9859.05,
    list_id='quod',
    offset=8111.96,
    order='numquam',
    query='dignissimos',
    sort='natus',
    updated_gte=dateutil.parser.parse('2022-03-19').date(),
)

res = s.member.get_martech_connection_id_list_id_member(req, operations.GetMartechConnectionIDListIDMemberSecurity(
    jwt="",
))

if res.marketing_members is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetMartechConnectionIDListIDMemberRequest](../../models/operations/getmartechconnectionidlistidmemberrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.GetMartechConnectionIDListIDMemberSecurity](../../models/operations/getmartechconnectionidlistidmembersecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.GetMartechConnectionIDListIDMemberResponse](../../models/operations/getmartechconnectionidlistidmemberresponse.md)**


## get_martech_connection_id_list_id_member_id

Retrieve a member from a list

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetMartechConnectionIDListIDMemberIDRequest(
    connection_id='optio',
    id='977bbc57-f389-428a-8600-c58d67d63e4a',
    list_id='officia',
)

res = s.member.get_martech_connection_id_list_id_member_id(req, operations.GetMartechConnectionIDListIDMemberIDSecurity(
    jwt="",
))

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetMartechConnectionIDListIDMemberIDRequest](../../models/operations/getmartechconnectionidlistidmemberidrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.GetMartechConnectionIDListIDMemberIDSecurity](../../models/operations/getmartechconnectionidlistidmemberidsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.GetMartechConnectionIDListIDMemberIDResponse](../../models/operations/getmartechconnectionidlistidmemberidresponse.md)**


## patch_martech_connection_id_list_id_member_id

Update a member in a list

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchMartechConnectionIDListIDMemberIDRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.parse('2022-08-11').date(),
        emails=[
            shared.MarketingEmail(
                email='Ella32@yahoo.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='9cfc6c0e-503f-4568-b1f1-d8ed87b28e8a',
        list_ids=[
            'a',
        ],
        name='Felipe Schmeler',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'nisi',
        ],
        updated_at=dateutil.parser.parse('2022-07-05').date(),
    ),
    connection_id='aliquam',
    id='1e43b234-2417-4d13-a3f6-2aa9ae4ae8ab',
    list_id='numquam',
)

res = s.member.patch_martech_connection_id_list_id_member_id(req, operations.PatchMartechConnectionIDListIDMemberIDSecurity(
    jwt="",
))

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.PatchMartechConnectionIDListIDMemberIDRequest](../../models/operations/patchmartechconnectionidlistidmemberidrequest.md)   | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `security`                                                                                                                             | [operations.PatchMartechConnectionIDListIDMemberIDSecurity](../../models/operations/patchmartechconnectionidlistidmemberidsecurity.md) | :heavy_check_mark:                                                                                                                     | The security requirements to use for the request.                                                                                      |


### Response

**[operations.PatchMartechConnectionIDListIDMemberIDResponse](../../models/operations/patchmartechconnectionidlistidmemberidresponse.md)**


## post_martech_connection_id_list_id_member

Create a member in a list

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostMartechConnectionIDListIDMemberRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.parse('2021-10-26').date(),
        emails=[
            shared.MarketingEmail(
                email='Elena80@hotmail.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='e8ba5d4a-a4a5-408b-9380-c29aa8dd71bd',
        list_ids=[
            'repellendus',
        ],
        name='Miss Hubert Emard',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'cum',
        ],
        updated_at=dateutil.parser.parse('2022-10-14').date(),
    ),
    connection_id='labore',
    list_id='modi',
)

res = s.member.post_martech_connection_id_list_id_member(req, operations.PostMartechConnectionIDListIDMemberSecurity(
    jwt="",
))

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PostMartechConnectionIDListIDMemberRequest](../../models/operations/postmartechconnectionidlistidmemberrequest.md)   | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `security`                                                                                                                       | [operations.PostMartechConnectionIDListIDMemberSecurity](../../models/operations/postmartechconnectionidlistidmembersecurity.md) | :heavy_check_mark:                                                                                                               | The security requirements to use for the request.                                                                                |


### Response

**[operations.PostMartechConnectionIDListIDMemberResponse](../../models/operations/postmartechconnectionidlistidmemberresponse.md)**


## put_martech_connection_id_list_id_member_id

Update a member in a list

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutMartechConnectionIDListIDMemberIDRequest(
    marketing_member=shared.MarketingMember(
        created_at=dateutil.parser.parse('2021-09-21').date(),
        emails=[
            shared.MarketingEmail(
                email='Geoffrey.Mitchell53@hotmail.com',
                type=shared.MarketingEmailType.HOME,
            ),
        ],
        id='d418bb71-804f-4423-9543-935f377ac5c9',
        list_ids=[
            'nam',
        ],
        name='Gretchen Moore',
        raw=shared.PropertyMarketingMemberRaw(),
        tags=[
            'suscipit',
        ],
        updated_at=dateutil.parser.parse('2022-08-12').date(),
    ),
    connection_id='optio',
    id='523105e7-c34c-4ab0-acb8-12a66148944a',
    list_id='voluptatum',
)

res = s.member.put_martech_connection_id_list_id_member_id(req, operations.PutMartechConnectionIDListIDMemberIDSecurity(
    jwt="",
))

if res.marketing_member is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PutMartechConnectionIDListIDMemberIDRequest](../../models/operations/putmartechconnectionidlistidmemberidrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.PutMartechConnectionIDListIDMemberIDSecurity](../../models/operations/putmartechconnectionidlistidmemberidsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.PutMartechConnectionIDListIDMemberIDResponse](../../models/operations/putmartechconnectionidlistidmemberidresponse.md)**

