# Company
(*company*)

### Available Operations

* [create_crm_company](#create_crm_company) - Create a company
* [get_crm_company](#get_crm_company) - Retrieve a company
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_enrich_companies](#list_enrich_companies) - Retrieve enrichment information for a company
* [patch_crm_company](#patch_crm_company) - Update a company
* [remove_crm_company](#remove_crm_company) - Remove a company
* [update_crm_company](#update_crm_company) - Update a company

## create_crm_company

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

req = operations.CreateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'connecting',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'carouse',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Germany',
            ),
        ],
        websites=[
            'yippee',
        ],
    ),
    connection_id='magenta Data woot',
    fields_=[
        'payment',
    ],
)

res = s.company.create_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmCompanyRequest](../../models/operations/createcrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateCrmCompanyResponse](../../models/operations/createcrmcompanyresponse.md)**


## get_crm_company

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

req = operations.GetCrmCompanyRequest(
    connection_id='THX Strategist deposit',
    fields_=[
        'snag',
    ],
    id='<ID>',
)

res = s.company.get_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmCompanyRequest](../../models/operations/getcrmcompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetCrmCompanyResponse](../../models/operations/getcrmcompanyresponse.md)**


## list_crm_companies

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

req = operations.ListCrmCompaniesRequest(
    connection_id='Jazz solid Lamborghini',
    fields_=[
        'Sleek',
    ],
)

res = s.company.list_crm_companies(req)

if res.crm_companies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmCompaniesRequest](../../models/operations/listcrmcompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCrmCompaniesResponse](../../models/operations/listcrmcompaniesresponse.md)**


## list_enrich_companies

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

req = operations.ListEnrichCompaniesRequest(
    connection_id='Chips',
)

res = s.company.list_enrich_companies(req)

if res.enrich_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListEnrichCompaniesRequest](../../models/operations/listenrichcompaniesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListEnrichCompaniesResponse](../../models/operations/listenrichcompaniesresponse.md)**


## patch_crm_company

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

req = operations.PatchCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Producer',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'Corporate',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='haptic Phased',
            ),
        ],
        websites=[
            'Investment',
        ],
    ),
    connection_id='Trans',
    fields_=[
        'Money',
    ],
    id='<ID>',
)

res = s.company.patch_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmCompanyRequest](../../models/operations/patchcrmcompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchCrmCompanyResponse](../../models/operations/patchcrmcompanyresponse.md)**


## remove_crm_company

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

req = operations.RemoveCrmCompanyRequest(
    connection_id='Mayaguez index wireless',
    id='<ID>',
)

res = s.company.remove_crm_company(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCrmCompanyRequest](../../models/operations/removecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveCrmCompanyResponse](../../models/operations/removecrmcompanyresponse.md)**


## update_crm_company

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

req = operations.UpdateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'SMS',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'barrel',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Account alarm infrastructure',
            ),
        ],
        websites=[
            'Visionary',
        ],
    ),
    connection_id='Southeast ad',
    fields_=[
        'Practical',
    ],
    id='<ID>',
)

res = s.company.update_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmCompanyRequest](../../models/operations/updatecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateCrmCompanyResponse](../../models/operations/updatecrmcompanyresponse.md)**

