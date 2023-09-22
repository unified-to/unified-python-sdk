# Deal

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
    connection_id='ducimus',
    id='ed565076-21c5-48f4-9739-6564c20a0711',
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
    company_id='similique',
    connection_id='omnis',
    contact_id='commodi',
    limit=1166.35,
    offset=8489.26,
    order='aspernatur',
    query='ut',
    sort='deserunt',
    updated_gte=dateutil.parser.isoparse('2022-02-20T22:48:15.284Z'),
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
    connection_id='facilis',
    id='b8f532d8-92cf-4781-acb5-12c878240bf5',
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
        amount=2743.68,
        closed_at=dateutil.parser.isoparse('2021-02-04T20:36:14.764Z'),
        created_at=dateutil.parser.isoparse('2021-12-30T15:49:38.515Z'),
        currency='hic',
        id='8f1bf0bc-8e1f-4206-95d8-31d0081090f6',
        lost_reason='nihil',
        name='Loretta Howe',
        pipeline='doloribus',
        probability=1877.7,
        raw=shared.PropertyCrmDealRaw(),
        source='id',
        stage='ex',
        tags=[
            'quos',
        ],
        updated_at=dateutil.parser.isoparse('2022-03-17T20:43:59.276Z'),
        won_reason='exercitationem',
    ),
    connection_id='molestiae',
    id='68dce742-409a-4215-a086-01489a5f63e3',
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
        amount=6489.85,
        closed_at=dateutil.parser.isoparse('2022-04-04T11:17:39.742Z'),
        created_at=dateutil.parser.isoparse('2020-05-19T07:26:52.477Z'),
        currency='natus',
        id='dda33dcd-6348-43e4-a7a9-8e4df37e45b8',
        lost_reason='omnis',
        name='Bernice Schultz I',
        pipeline='recusandae',
        probability=784.86,
        raw=shared.PropertyCrmDealRaw(),
        source='ipsum',
        stage='error',
        tags=[
            'numquam',
        ],
        updated_at=dateutil.parser.isoparse('2022-08-25T17:34:42.796Z'),
        won_reason='consectetur',
    ),
    connection_id='dicta',
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
        amount=551.24,
        closed_at=dateutil.parser.isoparse('2022-12-18T04:51:10.637Z'),
        created_at=dateutil.parser.isoparse('2022-04-06T10:46:32.109Z'),
        currency='facere',
        id='354c092b-d734-4f02-849d-86f4bb20fe5d',
        lost_reason='provident',
        name='Ashley Schmeler',
        pipeline='itaque',
        probability=4920.7,
        raw=shared.PropertyCrmDealRaw(),
        source='magnam',
        stage='excepturi',
        tags=[
            'placeat',
        ],
        updated_at=dateutil.parser.isoparse('2021-01-19T07:13:22.442Z'),
        won_reason='modi',
    ),
    connection_id='enim',
    id='a27f69e2-c9e6-4d10-a9db-3ad4c6b03108',
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

