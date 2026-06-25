# Target

## Overview

### Available Operations

* [get_ads_target2](#get_ads_target2) - Retrieve a target
* [list_ads_targets2](#list_ads_targets2) - List all targets

## get_ads_target2

Retrieve a target

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsTarget2" method="get" path="/ads/{connection_id}/target/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.target.get_ads_target2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_target is not None

    # Handle response
    print(res.ads_target)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAdsTarget2Request](../../models/operations/getadstarget2request.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetAdsTarget2Response](../../models/operations/getadstarget2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_targets2

List all targets

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsTargets2" method="get" path="/ads/{connection_id}/target" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.target.list_ads_targets2(request={
        "connection_id": "<id>",
    })

    assert res.ads_targets is not None

    # Handle response
    print(res.ads_targets)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListAdsTargets2Request](../../models/operations/listadstargets2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListAdsTargets2Response](../../models/operations/listadstargets2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |