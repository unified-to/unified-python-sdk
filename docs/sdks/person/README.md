# Person

## Overview

### Available Operations

* [list_enrich_people2](#list_enrich_people2) - Retrieve enrichment information for a person

## list_enrich_people2

Retrieve enrichment information for a person

### Example Usage

<!-- UsageSnippet language="python" operationID="listEnrichPeople2" method="get" path="/enrich/{connection_id}/person" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.person.list_enrich_people2(request={
        "connection_id": "<id>",
    })

    assert res.enrich_person is not None

    # Handle response
    print(res.enrich_person)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListEnrichPeople2Request](../../models/operations/listenrichpeople2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListEnrichPeople2Response](../../models/operations/listenrichpeople2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |