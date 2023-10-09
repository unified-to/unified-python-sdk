# Company
(*company*)

### Available Operations

* [delete_crm_connection_id_company_id](#delete_crm_connection_id_company_id) - Remove a company
* [get_crm_connection_id_company](#get_crm_connection_id_company) - List all companies
* [get_crm_connection_id_company_id](#get_crm_connection_id_company_id) - Retrieve a company
* [get_enrich_connection_id_company](#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [patch_crm_connection_id_company_id](#patch_crm_connection_id_company_id) - Update a company
* [post_crm_connection_id_company](#post_crm_connection_id_company) - Create a company
* [put_crm_connection_id_company_id](#put_crm_connection_id_company_id) - Update a company

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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Soft',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'invoice',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='miniature Quality',
            ),
        ],
        websites=[
            'redefine',
        ],
    ),
    connection_id='invoice National',
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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Personal',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'gosh',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='phooey',
            ),
        ],
        websites=[
            'primary',
        ],
    ),
    connection_id='neural',
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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'dicta',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'background',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='veniam secondary',
            ),
        ],
        websites=[
            'Southwest',
        ],
    ),
    connection_id='Calcium',
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

