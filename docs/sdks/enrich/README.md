# Enrich

### Available Operations

* [get_enrich_connection_id_company](#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [get_enrich_connection_id_person](#get_enrich_connection_id_person) - Retrieve enrichment information for a person

## get_enrich_connection_id_company

Retrieve enrichment information for a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetEnrichConnectionIDCompanyRequest(
    connection_id='mollitia',
    domain='beatae',
    name='Irma Bayer',
)

res = s.enrich.get_enrich_connection_id_company(req, operations.GetEnrichConnectionIDCompanySecurity(
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


## get_enrich_connection_id_person

Retrieve enrichment information for a person

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetEnrichConnectionIDPersonRequest(
    connection_id='at',
    email='Curtis.Barrows40@hotmail.com',
    linkedin_url='cupiditate',
    name='Ms. Ivan Breitenberg IV',
    twitter='temporibus',
)

res = s.enrich.get_enrich_connection_id_person(req, operations.GetEnrichConnectionIDPersonSecurity(
    jwt="",
))

if res.enrich_person is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetEnrichConnectionIDPersonRequest](../../models/operations/getenrichconnectionidpersonrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetEnrichConnectionIDPersonSecurity](../../models/operations/getenrichconnectionidpersonsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetEnrichConnectionIDPersonResponse](../../models/operations/getenrichconnectionidpersonresponse.md)**

