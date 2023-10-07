# Deal
(*deal*)

### Available Operations

* [delete_crm_connection_id_deal_id](#delete_crm_connection_id_deal_id) - Remove a deal
* [get_crm_connection_id_deal](#get_crm_connection_id_deal) - List all deals
* [get_crm_connection_id_deal_id](#get_crm_connection_id_deal_id) - Retrieve a deal
* [patch_crm_connection_id_deal_id](#patch_crm_connection_id_deal_id) - Update a deal
* [post_crm_connection_id_deal](#post_crm_connection_id_deal) - Create a deal
* [put_crm_connection_id_deal_id](#put_crm_connection_id_deal_id) - Update a deal

## delete_crm_connection_id_deal_id

Remove a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDDealIDRequest(
    connection_id='Fresh',
    id='<ID>',
)

res = s.deal.delete_crm_connection_id_deal_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDDealIDRequest](../../models/operations/deletecrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDDealIDResponse](../../models/operations/deletecrmconnectioniddealidresponse.md)**


## get_crm_connection_id_deal

List all deals

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

req = operations.GetCrmConnectionIDDealRequest(
    connection_id='Tools Card copying',
)

res = s.deal.get_crm_connection_id_deal(req)

if res.crm_deals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDDealRequest](../../models/operations/getcrmconnectioniddealrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDDealResponse](../../models/operations/getcrmconnectioniddealresponse.md)**


## get_crm_connection_id_deal_id

Retrieve a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDDealIDRequest(
    connection_id='Concrete Director',
    id='<ID>',
)

res = s.deal.get_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDDealIDRequest](../../models/operations/getcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDDealIDResponse](../../models/operations/getcrmconnectioniddealidresponse.md)**


## patch_crm_connection_id_deal_id

Update a deal

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

req = operations.PatchCrmConnectionIDDealIDRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'Bicycle',
        ],
    ),
    connection_id='partnerships',
    id='<ID>',
)

res = s.deal.patch_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDDealIDRequest](../../models/operations/patchcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDDealIDResponse](../../models/operations/patchcrmconnectioniddealidresponse.md)**


## post_crm_connection_id_deal

Create a deal

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

req = operations.PostCrmConnectionIDDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'M2F',
        ],
    ),
    connection_id='Borders pfft',
)

res = s.deal.post_crm_connection_id_deal(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDDealRequest](../../models/operations/postcrmconnectioniddealrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDDealResponse](../../models/operations/postcrmconnectioniddealresponse.md)**


## put_crm_connection_id_deal_id

Update a deal

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

req = operations.PutCrmConnectionIDDealIDRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'Account',
        ],
    ),
    connection_id='payment',
    id='<ID>',
)

res = s.deal.put_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDDealIDRequest](../../models/operations/putcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDDealIDResponse](../../models/operations/putcrmconnectioniddealidresponse.md)**

