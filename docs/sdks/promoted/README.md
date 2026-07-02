# Promoted

## Overview

### Available Operations

* [get_ads_promoted](#get_ads_promoted) - Retrieve a promoted
* [list_ads_promoteds](#list_ads_promoteds) - List all promoteds

## get_ads_promoted

Retrieve a promoted

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsPromoted" method="get" path="/ads/{connection_id}/promoted/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.promoted.get_ads_promoted(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_promoted is not None

    # Handle response
    print(res.ads_promoted)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAdsPromotedRequest](../../models/operations/getadspromotedrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAdsPromotedResponse](../../models/operations/getadspromotedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_promoteds

List all promoteds

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsPromoteds" method="get" path="/ads/{connection_id}/promoted" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.promoted.list_ads_promoteds(request={
        "connection_id": "<id>",
    })

    assert res.ads_promoteds is not None

    # Handle response
    print(res.ads_promoteds)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAdsPromotedsRequest](../../models/operations/listadspromotedsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAdsPromotedsResponse](../../models/operations/listadspromotedsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |