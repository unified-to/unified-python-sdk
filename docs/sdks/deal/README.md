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
    company_id='Tools Card copying',
    connection_id='Renminbi',
    contact_id='till payment World',
    limit=8656.16,
    offset=4455.8,
    order='global',
    query='Program Bespoke Wisconsin',
    sort='Netherlands under',
    updated_gte=dateutil.parser.isoparse('2022-12-23T01:47:21.816Z'),
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
        amount=7725.78,
        closed_at=dateutil.parser.isoparse('2021-10-28T08:42:49.591Z'),
        created_at=dateutil.parser.isoparse('2023-04-23T15:03:53.999Z'),
        currency='Afghani',
        id='<ID>',
        lost_reason='North',
        name='midnight',
        pipeline='envisioneer Functionality Loan',
        probability=7051.73,
        raw=shared.PropertyCrmDealRaw(),
        source='Krone',
        stage='pascal aliquam gripping',
        tags=[
            'where',
        ],
        updated_at=dateutil.parser.isoparse('2022-04-05T10:21:22.505Z'),
        won_reason='Savings kilogram',
    ),
    connection_id='Chair weber silver',
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
        amount=6144.41,
        closed_at=dateutil.parser.isoparse('2022-07-10T09:55:59.977Z'),
        created_at=dateutil.parser.isoparse('2022-01-20T07:28:03.436Z'),
        currency='Convertible Marks',
        id='<ID>',
        lost_reason='pfft female',
        name='Expressway',
        pipeline='withdrawal Extended busily',
        probability=7998.22,
        raw=shared.PropertyCrmDealRaw(),
        source='spiffy sometimes',
        stage='transmitter',
        tags=[
            'intermediate',
        ],
        updated_at=dateutil.parser.isoparse('2022-10-06T18:34:11.762Z'),
        won_reason='Cisgender input HTTP',
    ),
    connection_id='accusantium Checking',
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
        amount=4050.98,
        closed_at=dateutil.parser.isoparse('2022-01-15T04:05:31.641Z'),
        created_at=dateutil.parser.isoparse('2023-06-04T01:28:32.466Z'),
        currency='Bermudian Dollar (customarily known as Bermuda Dollar)',
        id='<ID>',
        lost_reason='laudantium Southwest',
        name='wail Developer',
        pipeline='male Samarium Gourde',
        probability=6728.74,
        raw=shared.PropertyCrmDealRaw(),
        source='Stage Gasoline Metal',
        stage='Corporate withdrawal Tasty',
        tags=[
            'extranet',
        ],
        updated_at=dateutil.parser.isoparse('2021-10-16T22:38:02.052Z'),
        won_reason='phooey',
    ),
    connection_id='Jazz',
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

