# Query

## Overview

### Available Operations

* [create_datastore_query2](#create_datastore_query2) - Create a query

## create_datastore_query2

Create a query

### Example Usage

<!-- UsageSnippet language="python" operationID="createDatastoreQuery2" method="post" path="/datastore/{connection_id}/query" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.query.create_datastore_query2(request={
        "datastore_query": {},
        "connection_id": "<id>",
    })

    assert res.datastore_query is not None

    # Handle response
    print(res.datastore_query)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateDatastoreQuery2Request](../../models/operations/createdatastorequery2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateDatastoreQuery2Response](../../models/operations/createdatastorequery2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |