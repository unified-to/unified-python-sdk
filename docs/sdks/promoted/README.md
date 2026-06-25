# Promoted

## Overview

### Available Operations

* [get_ads_promoted2](#get_ads_promoted2) - Retrieve a promoted
* [list_ads_promoteds2](#list_ads_promoteds2) - List all promoteds

## get_ads_promoted2

Retrieve a promoted

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsPromoted2" method="get" path="/ads/{connection_id}/promoted/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.promoted.get_ads_promoted2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_promoted is not None

    # Handle response
    print(res.ads_promoted)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAdsPromoted2Request](../../models/operations/getadspromoted2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAdsPromoted2Response](../../models/operations/getadspromoted2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_promoteds2

List all promoteds

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsPromoteds2" method="get" path="/ads/{connection_id}/promoted" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.promoted.list_ads_promoteds2(request={
        "connection_id": "<id>",
    })

    assert res.ads_promoteds is not None

    # Handle response
    print(res.ads_promoteds)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAdsPromoteds2Request](../../models/operations/listadspromoteds2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAdsPromoteds2Response](../../models/operations/listadspromoteds2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |