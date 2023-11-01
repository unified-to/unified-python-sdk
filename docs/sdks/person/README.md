# Person
(*.person*)

### Available Operations

* [list_enrich_people](#list_enrich_people) - Retrieve enrichment information for a person

## list_enrich_people

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

req = operations.ListEnrichPeopleRequest(
    connection_id='string',
)

res = s.person.list_enrich_people(req)

if res.enrich_person is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListEnrichPeopleRequest](../../models/operations/listenrichpeoplerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListEnrichPeopleResponse](../../models/operations/listenrichpeopleresponse.md)**

