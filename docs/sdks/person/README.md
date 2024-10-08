# Person
(*person*)

## Overview

### Available Operations

* [list_enrich_people](#list_enrich_people) - Retrieve enrichment information for a person

## list_enrich_people

Retrieve enrichment information for a person

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.person.list_enrich_people(request=operations.ListEnrichPeopleRequest(
    connection_id='<value>',
))

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

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |