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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDCompanyIDRequest(
    connection_id='maiores',
    id='eda53e5a-e6e0-4ac1-84c2-b9c247c88373',
)

res = s.company.delete_crm_connection_id_company_id(req, operations.DeleteCrmConnectionIDCompanyIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteCrmConnectionIDCompanyIDRequest](../../models/operations/deletecrmconnectionidcompanyidrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.DeleteCrmConnectionIDCompanyIDSecurity](../../models/operations/deletecrmconnectionidcompanyidsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.DeleteCrmConnectionIDCompanyIDResponse](../../models/operations/deletecrmconnectionidcompanyidresponse.md)**


## delete_crm_connection_id_company_id_deal_deal_id

Remove deal association from a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='laborum',
    deal_id='modi',
    id='0e1942f3-2e55-4055-b56f-5d56d0bd0af2',
)

res = s.company.delete_crm_connection_id_company_id_deal_deal_id(req, operations.DeleteCrmConnectionIDCompanyIDDealDealIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.DeleteCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/deletecrmconnectionidcompanyiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `security`                                                                                                                                 | [operations.DeleteCrmConnectionIDCompanyIDDealDealIDSecurity](../../models/operations/deletecrmconnectionidcompanyiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                         | The security requirements to use for the request.                                                                                          |


### Response

**[operations.DeleteCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/deletecrmconnectionidcompanyiddealdealidresponse.md)**


## get_crm_connection_id_company

List all companies

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDCompanyRequest(
    connection_id='possimus',
    contact_id='repellat',
    deal_id='repudiandae',
    limit=1002.33,
    offset=2406.96,
    order='pariatur',
    query='harum',
    sort='dolore',
    updated_gte=dateutil.parser.isoparse('2021-09-11T06:54:38.386Z'),
)

res = s.company.get_crm_connection_id_company(req, operations.GetCrmConnectionIDCompanySecurity(
    jwt="",
))

if res.crm_companies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCrmConnectionIDCompanyRequest](../../models/operations/getcrmconnectionidcompanyrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetCrmConnectionIDCompanySecurity](../../models/operations/getcrmconnectionidcompanysecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetCrmConnectionIDCompanyResponse](../../models/operations/getcrmconnectionidcompanyresponse.md)**


## get_crm_connection_id_company_id

Retrieve a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDCompanyIDRequest(
    connection_id='explicabo',
    id='cba3f894-1aeb-4c0b-80a6-924d3b2ecfcc',
)

res = s.company.get_crm_connection_id_company_id(req, operations.GetCrmConnectionIDCompanyIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetCrmConnectionIDCompanyIDRequest](../../models/operations/getcrmconnectionidcompanyidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetCrmConnectionIDCompanyIDSecurity](../../models/operations/getcrmconnectionidcompanyidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetCrmConnectionIDCompanyIDResponse](../../models/operations/getcrmconnectionidcompanyidresponse.md)**


## get_enrich_connection_id_company

Retrieve enrichment information for a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetEnrichConnectionIDCompanyRequest(
    connection_id='quos',
    domain='asperiores',
    name='Mr. Nick Hessel DVM',
)

res = s.company.get_enrich_connection_id_company(req, operations.GetEnrichConnectionIDCompanySecurity(
    jwt="",
))

if res.enrich_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetEnrichConnectionIDCompanyRequest](../../models/operations/getenrichconnectionidcompanyrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.GetEnrichConnectionIDCompanySecurity](../../models/operations/getenrichconnectionidcompanysecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.GetEnrichConnectionIDCompanyResponse](../../models/operations/getenrichconnectionidcompanyresponse.md)**


## patch_crm_connection_id_company_id

Update a company

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='nostrum',
            address2='at',
            city='Coon Rapids',
            country='Syrian Arab Republic',
            country_code='IO',
            postal_code='60502-9337',
            region='quas',
            region_code='consequuntur',
        ),
        created_at=dateutil.parser.isoparse('2022-10-03T16:02:53.877Z'),
        deal_ids=[
            'aliquid',
        ],
        emails=[
            shared.CrmEmail(
                email='Mandy.Ernser@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='8873e484-380b-41f6-b8ca-275a60a04c49',
        name='Lynne Schroeder',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'unde',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='illo',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-11T06:13:47.031Z'),
        websites=[
            'ipsam',
        ],
    ),
    connection_id='quasi',
    id='c1bdb1cf-4b88-48eb-9fc4-ccca99bc7fc0',
)

res = s.company.patch_crm_connection_id_company_id(req, operations.PatchCrmConnectionIDCompanyIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchCrmConnectionIDCompanyIDRequest](../../models/operations/patchcrmconnectionidcompanyidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PatchCrmConnectionIDCompanyIDSecurity](../../models/operations/patchcrmconnectionidcompanyidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PatchCrmConnectionIDCompanyIDResponse](../../models/operations/patchcrmconnectionidcompanyidresponse.md)**


## patch_crm_connection_id_company_id_deal_deal_id

Associate a deal with a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='soluta',
    deal_id='fugit',
    id='dce10873-e42b-4006-9678-878ba8581a58',
)

res = s.company.patch_crm_connection_id_company_id_deal_deal_id(req, operations.PatchCrmConnectionIDCompanyIDDealDealIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PatchCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/patchcrmconnectionidcompanyiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `security`                                                                                                                               | [operations.PatchCrmConnectionIDCompanyIDDealDealIDSecurity](../../models/operations/patchcrmconnectionidcompanyiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                       | The security requirements to use for the request.                                                                                        |


### Response

**[operations.PatchCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/patchcrmconnectionidcompanyiddealdealidresponse.md)**


## post_crm_connection_id_company

Create a company

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostCrmConnectionIDCompanyRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='magni',
            address2='quae',
            city='Randalborough',
            country='Fiji',
            country_code='VG',
            postal_code='96676-3918',
            region='mollitia',
            region_code='cumque',
        ),
        created_at=dateutil.parser.isoparse('2022-09-08T12:56:45.780Z'),
        deal_ids=[
            'eum',
        ],
        emails=[
            shared.CrmEmail(
                email='Roslyn48@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='fee81206-e281-43fa-8a41-c480d3f2132a',
        name='Mr. Matthew Ebert',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'nulla',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='enim',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-01-14T22:16:14.005Z'),
        websites=[
            'numquam',
        ],
    ),
    connection_id='optio',
)

res = s.company.post_crm_connection_id_company(req, operations.PostCrmConnectionIDCompanySecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostCrmConnectionIDCompanyRequest](../../models/operations/postcrmconnectionidcompanyrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PostCrmConnectionIDCompanySecurity](../../models/operations/postcrmconnectionidcompanysecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PostCrmConnectionIDCompanyResponse](../../models/operations/postcrmconnectionidcompanyresponse.md)**


## put_crm_connection_id_company_id

Update a company

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='nobis',
            address2='ex',
            city='Beavercreek',
            country='Malaysia',
            country_code='PK',
            postal_code='53116-4629',
            region='dignissimos',
            region_code='esse',
        ),
        created_at=dateutil.parser.isoparse('2021-12-22T21:12:12.654Z'),
        deal_ids=[
            'esse',
        ],
        emails=[
            shared.CrmEmail(
                email='Travon.Franecki70@hotmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='752c65b3-4418-4e3b-b91c-8d975e0e8419',
        name='Wallace Wiegand',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'earum',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='architecto',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-01-07T01:07:05.981Z'),
        websites=[
            'sequi',
        ],
    ),
    connection_id='saepe',
    id='07edcc4a-a5f3-4cab-9905-a972e0567282',
)

res = s.company.put_crm_connection_id_company_id(req, operations.PutCrmConnectionIDCompanyIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutCrmConnectionIDCompanyIDRequest](../../models/operations/putcrmconnectionidcompanyidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.PutCrmConnectionIDCompanyIDSecurity](../../models/operations/putcrmconnectionidcompanyidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.PutCrmConnectionIDCompanyIDResponse](../../models/operations/putcrmconnectionidcompanyidresponse.md)**


## put_crm_connection_id_company_id_deal_deal_id

Associate a deal with a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDCompanyIDDealDealIDRequest(
    connection_id='odit',
    deal_id='iusto',
    id='b2d30947-0bf7-4a4f-a87c-f535a6fae54e',
)

res = s.company.put_crm_connection_id_company_id_deal_deal_id(req, operations.PutCrmConnectionIDCompanyIDDealDealIDSecurity(
    jwt="",
))

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PutCrmConnectionIDCompanyIDDealDealIDRequest](../../models/operations/putcrmconnectionidcompanyiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.PutCrmConnectionIDCompanyIDDealDealIDSecurity](../../models/operations/putcrmconnectionidcompanyiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.PutCrmConnectionIDCompanyIDDealDealIDResponse](../../models/operations/putcrmconnectionidcompanyiddealdealidresponse.md)**

