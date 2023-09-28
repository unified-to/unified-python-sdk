# Company
(*company*)

### Available Operations

* [delete_crm_connection_id_company_id](#delete_crm_connection_id_company_id) - Remove a company
* [delete_crm_connection_id_company_id_deal_deal_id](#delete_crm_connection_id_company_id_deal_deal_id) - Remove deal association from a company
* [get_crm_connection_id_company](#get_crm_connection_id_company) - List all companies
* [get_crm_connection_id_company_id](#get_crm_connection_id_company_id) - Retrieve a company
* [get_enrich_connection_id_company](#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [patch_crm_connection_id_company_id](#patch_crm_connection_id_company_id) - Update a company
* [patch_crm_connection_id_company_id_deal_deal_id](#patch_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company
* [post_crm_connection_id_company](#post_crm_connection_id_company) - Create a company
* [put_crm_connection_id_company_id](#put_crm_connection_id_company_id) - Update a company
* [put_crm_connection_id_company_id_deal_deal_id](#put_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company

## delete_crm_connection_id_company_id

Remove a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDCompanyIDRequest(
    connection_id='hertz morph',
    id='<ID>',
)

res = s.company.delete_crm_connection_id_company_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteCrmConnectionIDCompanyIDRequest](../../models/operations/deletecrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteCrmConnectionIDCompanyIDResponse](../../models/operations/deletecrmconnectionidcompanyidresponse.md)**


## delete_crm_connection_id_company_id_deal_deal_id

Remove deal association from a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='Carolina',
    deal_id='Technician',
    id='<ID>',
)

res = s.company.delete_crm_connection_id_company_id_deal_deal_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.DeleteCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/deletecrmconnectionidcompanyiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.DeleteCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/deletecrmconnectionidcompanyiddealdealidresponse.md)**


## get_crm_connection_id_company

List all companies

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

req = operations.GetCrmConnectionIDCompanyRequest(
    connection_id='indexing',
    contact_id='Porsche firewall',
    deal_id='Hafnium Computers',
    limit=902.85,
    offset=2893.88,
    order='Interactions relationships juxtapose',
    query='newton Luxembourg',
    sort='Dakota quantifying Actinium',
    updated_gte=dateutil.parser.isoparse('2022-09-27T07:42:48.074Z'),
)

res = s.company.get_crm_connection_id_company(req)

if res.crm_companies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDCompanyRequest](../../models/operations/getcrmconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCrmConnectionIDCompanyResponse](../../models/operations/getcrmconnectionidcompanyresponse.md)**


## get_crm_connection_id_company_id

Retrieve a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDCompanyIDRequest(
    connection_id='Netherlands',
    id='<ID>',
)

res = s.company.get_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCrmConnectionIDCompanyIDRequest](../../models/operations/getcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCrmConnectionIDCompanyIDResponse](../../models/operations/getcrmconnectionidcompanyidresponse.md)**


## get_enrich_connection_id_company

Retrieve enrichment information for a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetEnrichConnectionIDCompanyRequest(
    connection_id='female Computers Central',
    domain='scientific-facet.biz',
    name='Outdoors embrace interface',
)

res = s.company.get_enrich_connection_id_company(req)

if res.enrich_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetEnrichConnectionIDCompanyRequest](../../models/operations/getenrichconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetEnrichConnectionIDCompanyResponse](../../models/operations/getenrichconnectionidcompanyresponse.md)**


## patch_crm_connection_id_company_id

Update a company

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

req = operations.PatchCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='invoice',
            address2='indexing Ford',
            city='McAllen',
            country='Netherlands',
            country_code='PF',
            postal_code='93486',
            region='Steel impactful',
            region_code='Dong',
        ),
        created_at=dateutil.parser.isoparse('2023-07-25T08:43:38.995Z'),
        deal_ids=[
            'usefully',
        ],
        emails=[
            shared.CrmEmail(
                email='Annabel31@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        name='Toys Vermont Astatine',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'Trigender',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='female',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-12-22T11:39:56.432Z'),
        websites=[
            'Latin',
        ],
    ),
    connection_id='North kilogram connecting',
    id='<ID>',
)

res = s.company.patch_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchCrmConnectionIDCompanyIDRequest](../../models/operations/patchcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PatchCrmConnectionIDCompanyIDResponse](../../models/operations/patchcrmconnectionidcompanyidresponse.md)**


## patch_crm_connection_id_company_id_deal_deal_id

Associate a deal with a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='virtual BMX Tuna',
    deal_id='frightened quia generating',
    id='<ID>',
)

res = s.company.patch_crm_connection_id_company_id_deal_deal_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.PatchCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/patchcrmconnectionidcompanyiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.PatchCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/patchcrmconnectionidcompanyiddealdealidresponse.md)**


## post_crm_connection_id_company

Create a company

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

req = operations.PostCrmConnectionIDCompanyRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='consequently gosh',
            address2='phooey',
            city='Antonettaville',
            country='Lebanon',
            country_code='SI',
            postal_code='79462',
            region='orchid Oxygen Kids',
            region_code='Electric utilisation',
        ),
        created_at=dateutil.parser.isoparse('2021-10-01T08:46:18.197Z'),
        deal_ids=[
            'Tennessee',
        ],
        emails=[
            shared.CrmEmail(
                email='Jaida.McDermott26@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='Hydrogen Wooden',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'CSS',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Account invoice',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-09-12T17:31:24.634Z'),
        websites=[
            'Intuitive',
        ],
    ),
    connection_id='Gasoline',
)

res = s.company.post_crm_connection_id_company(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostCrmConnectionIDCompanyRequest](../../models/operations/postcrmconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostCrmConnectionIDCompanyResponse](../../models/operations/postcrmconnectionidcompanyresponse.md)**


## put_crm_connection_id_company_id

Update a company

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

req = operations.PutCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='Northwest Northwest',
            address2='portals Diesel',
            city='Azusa',
            country='Qatar',
            country_code='CG',
            postal_code='52396',
            region='Tuna sticky lest',
            region_code='Soft boo Missoula',
        ),
        created_at=dateutil.parser.isoparse('2022-05-14T19:17:30.970Z'),
        deal_ids=[
            'Hybrid',
        ],
        emails=[
            shared.CrmEmail(
                email='Vance_Cruickshank93@gmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='lest Northwest',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'East',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Bronze round',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-02-21T09:41:36.696Z'),
        websites=[
            'Keyboard',
        ],
    ),
    connection_id='orange Bespoke',
    id='<ID>',
)

res = s.company.put_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutCrmConnectionIDCompanyIDRequest](../../models/operations/putcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutCrmConnectionIDCompanyIDResponse](../../models/operations/putcrmconnectionidcompanyidresponse.md)**


## put_crm_connection_id_company_id_deal_deal_id

Associate a deal with a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='Hybrid Mississippi Savings',
    deal_id='West Hill Woman',
    id='<ID>',
)

res = s.company.put_crm_connection_id_company_id_deal_deal_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PutCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/putcrmconnectionidcompanyiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PutCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/putcrmconnectionidcompanyiddealdealidresponse.md)**

