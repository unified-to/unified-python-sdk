# Promoted

## Overview

### Available Operations

* [list_ads_promotedes](#list_ads_promotedes) - List all promotedes

## list_ads_promotedes

List all promotedes

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsPromotedes" method="get" path="/ads/{connection_id}/promoted" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.promoted.list_ads_promotedes(request={
        "connection_id": "<id>",
    })

    assert res.ads_promotedes is not None

    # Handle response
    print(res.ads_promotedes)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAdsPromotedesRequest](../../models/operations/listadspromotedesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAdsPromotedesResponse](../../models/operations/listadspromotedesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |