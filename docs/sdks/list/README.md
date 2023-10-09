# List
(*list_*)

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
    connection_id='Minivan',
    id='<ID>',
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
    connection_id='silver DeKalb',
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
    connection_id='Jewelery orange',
    id='<ID>',
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
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='Funk',
    id='<ID>',
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
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='synergistic Transexual Steel',
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
        raw=shared.PropertyMarketingListRaw(),
    ),
    connection_id='Underpass initiatives',
    id='<ID>',
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

