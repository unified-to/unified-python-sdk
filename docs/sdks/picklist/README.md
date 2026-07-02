# Picklist

## Overview

### Available Operations

* [list_crm_picklists](#list_crm_picklists) - List all picklists

## list_crm_picklists

List all picklists

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmPicklists" method="get" path="/crm/{connection_id}/picklist" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.picklist.list_crm_picklists(request={
        "connection_id": "<id>",
    })

    assert res.crm_picklists is not None

    # Handle response
    print(res.crm_picklists)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmPicklistsRequest](../../models/operations/listcrmpicklistsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCrmPicklistsResponse](../../models/operations/listcrmpicklistsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |