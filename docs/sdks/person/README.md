# person

### Available Operations

* [get_enrich_connection_id_person](#get_enrich_connection_id_person) - Retrieve enrichment information for a person

## get_enrich_connection_id_person

Retrieve enrichment information for a person

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetEnrichConnectionIDPersonRequest(
    connection_id='numquam',
    email='Donna44@yahoo.com',
    linkedin_url='laboriosam',
    name='Phillip Waelchi',
    twitter='totam',
)

res = s.person.get_enrich_connection_id_person(req, operations.GetEnrichConnectionIDPersonSecurity(
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

