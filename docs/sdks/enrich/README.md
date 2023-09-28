# Enrich
(*enrich*)

### Available Operations

* [get_enrich_connection_id_company](#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [get_enrich_connection_id_person](#get_enrich_connection_id_person) - Retrieve enrichment information for a person

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

res = s.enrich.get_enrich_connection_id_company(req)

if res.enrich_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetEnrichConnectionIDCompanyRequest](../../models/operations/getenrichconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetEnrichConnectionIDCompanyResponse](../../models/operations/getenrichconnectionidcompanyresponse.md)**


## get_enrich_connection_id_person

Retrieve enrichment information for a person

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetEnrichConnectionIDPersonRequest(
    connection_id='Iowa Account',
    email='Jaiden_Weimann24@gmail.com',
    linkedin_url='paradigms integrate Creative',
    name='Investment',
    twitter='Hills',
)

res = s.enrich.get_enrich_connection_id_person(req)

if res.enrich_person is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetEnrichConnectionIDPersonRequest](../../models/operations/getenrichconnectionidpersonrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetEnrichConnectionIDPersonResponse](../../models/operations/getenrichconnectionidpersonresponse.md)**

