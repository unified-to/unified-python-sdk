# Company

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
    connection_id='eos',
    id='b9c247c8-8373-4a40-a194-2f32e5505575',
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
    connection_id='nisi',
    deal_id='tenetur',
    id='5d56d0bd-0af2-4dfe-93db-4f62cba3f894',
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
    connection_id='quasi',
    contact_id='mollitia',
    deal_id='accusamus',
    limit=6875.89,
    offset=7691.56,
    order='doloremque',
    query='expedita',
    sort='corrupti',
    updated_gte=dateutil.parser.isoparse('2022-05-11T05:34:43.056Z'),
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
    connection_id='aliquid',
    id='924d3b2e-cfcc-48f8-9501-0f5dd3d6fa18',
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
    connection_id='aperiam',
    domain='non',
    name='Derek Haag',
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
            address1='consequuntur',
            address2='maiores',
            city='South Jonathanchester',
            country='Cyprus',
            country_code='HU',
            postal_code='75542',
            region='recusandae',
            region_code='tempora',
        ),
        created_at=dateutil.parser.isoparse('2022-06-26T14:48:08.360Z'),
        deal_ids=[
            'sequi',
        ],
        emails=[
            shared.CrmEmail(
                email='Alejandrin94@yahoo.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='b8ca275a-60a0-44c4-95cc-699171b51c1b',
        name='Johnathan Braun',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'labore',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='expedita',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-11-30T08:27:41.789Z'),
        websites=[
            'officiis',
        ],
    ),
    connection_id='cum',
    id='dfc4ccca-99bc-47fc-8b2d-ce10873e42b0',
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
    connection_id='voluptatem',
    deal_id='eum',
    id='d678878b-a858-41a5-8208-c54fefa9c95f',
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
            address1='quia',
            address2='officiis',
            city='Runolfsdottirborough',
            country='Gambia',
            country_code='IR',
            postal_code='82047',
            region='asperiores',
            region_code='recusandae',
        ),
        created_at=dateutil.parser.isoparse('2021-06-25T15:44:39.144Z'),
        deal_ids=[
            'dicta',
        ],
        emails=[
            shared.CrmEmail(
                email='Albina.Hyatt53@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='3fa4a41c-480d-43f2-932a-f03102d514f4',
        name='Loren Jakubowski IV',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'expedita',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='hic',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-11-06T17:51:41.197Z'),
        websites=[
            'beatae',
        ],
    ),
    connection_id='similique',
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
            address1='ea',
            address2='animi',
            city='Fort Jeremie',
            country='Kenya',
            country_code='NG',
            postal_code='49928-2794',
            region='ipsam',
            region_code='explicabo',
        ),
        created_at=dateutil.parser.isoparse('2021-10-23T06:28:50.254Z'),
        deal_ids=[
            'quis',
        ],
        emails=[
            shared.CrmEmail(
                email='Cyril10@hotmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='e3bb91c8-d975-4e0e-8419-d8f84f144f3e',
        name='Joy Toy',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'cumque',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='aliquam',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-05-12T12:30:36.705Z'),
        websites=[
            'reiciendis',
        ],
    ),
    connection_id='sequi',
    id='cabd905a-972e-4056-b282-27b2d309470b',
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
    connection_id='sapiente',
    deal_id='quam',
    id='a4fa87cf-535a-46fa-a54e-bf60c321f023',
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

