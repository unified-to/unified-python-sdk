# List

### Available Operations

* [delete_martech_connection_id_list_id](#delete_martech_connection_id_list_id) - Remove a list
* [get_martech_connection_id_list](#get_martech_connection_id_list) - List all lists
* [get_martech_connection_id_list_id](#get_martech_connection_id_list_id) - Retrieve a list
* [patch_martech_connection_id_list_id](#patch_martech_connection_id_list_id) - Update a list
* [post_martech_connection_id_list](#post_martech_connection_id_list) - Create a list
* [put_martech_connection_id_list_id](#put_martech_connection_id_list_id) - Update a list

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
    connection_id='molestiae',
    id='866db8a7-49e3-4984-911c-c75e4f0c004b',
)

res = s.list_.delete_martech_connection_id_list_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteMartechConnectionIDListIDRequest](../../models/operations/deletemartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.DeleteMartechConnectionIDListIDResponse](../../models/operations/deletemartechconnectionidlistidresponse.md)**


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
    connection_id='minima',
    limit=7315.15,
    offset=6991.28,
    order='molestiae',
    query='ipsam',
    sort='quos',
    updated_gte=dateutil.parser.isoparse('2020-09-30T08:18:10.798Z'),
)

res = s.list_.get_martech_connection_id_list(req)

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
    connection_id='cupiditate',
    id='4562f006-9685-4fcd-9a17-3d84bbe24f29',
)

res = s.list_.get_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetMartechConnectionIDListIDRequest](../../models/operations/getmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetMartechConnectionIDListIDResponse](../../models/operations/getmartechconnectionidlistidresponse.md)**


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
        created_at='praesentium',
        id='34afb073-5cb6-4285-94a2-9aaa1e169156',
        name='Adrian Schuster',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2022-06-17T09:25:28.057Z'),
    ),
    connection_id='perferendis',
    id='9505bf03-a93e-4944-80ca-37fb10789032',
)

res = s.list_.patch_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchMartechConnectionIDListIDRequest](../../models/operations/patchmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PatchMartechConnectionIDListIDResponse](../../models/operations/patchmartechconnectionidlistidresponse.md)**


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
        created_at='deserunt',
        id='c333172e-2dd7-49ec-b4ba-7e88ddb36fd1',
        name='Lucas Schneider',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2022-03-20T02:47:07.461Z'),
    ),
    connection_id='quas',
)

res = s.list_.post_martech_connection_id_list(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostMartechConnectionIDListRequest](../../models/operations/postmartechconnectionidlistrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostMartechConnectionIDListResponse](../../models/operations/postmartechconnectionidlistresponse.md)**


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
        created_at='autem',
        id='573474f0-a740-4fb4-ab44-1c3a09e76399',
        name='Ms. Eula Leffler',
        raw=shared.PropertyMarketingListRaw(),
        updated_at=dateutil.parser.isoparse('2021-03-29T15:45:25.588Z'),
    ),
    connection_id='odio',
    id='94455ebc-550a-41c4-a6b5-9c8366fdcc13',
)

res = s.list_.put_martech_connection_id_list_id(req)

if res.marketing_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutMartechConnectionIDListIDRequest](../../models/operations/putmartechconnectionidlistidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PutMartechConnectionIDListIDResponse](../../models/operations/putmartechconnectionidlistidresponse.md)**

