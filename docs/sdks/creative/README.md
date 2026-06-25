# Creative

## Overview

### Available Operations

* [create_ads_creative2](#create_ads_creative2) - Create a creative
* [get_ads_creative2](#get_ads_creative2) - Retrieve a creative
* [list_ads_creatives2](#list_ads_creatives2) - List all creatives
* [patch_ads_creative2](#patch_ads_creative2) - Update a creative
* [remove_ads_creative2](#remove_ads_creative2) - Remove a creative
* [update_ads_creative2](#update_ads_creative2) - Update a creative

## create_ads_creative2

Create a creative

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsCreative2" method="post" path="/ads/{connection_id}/creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.create_ads_creative2(request={
        "ads_creative": {},
        "connection_id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAdsCreative2Request](../../models/operations/createadscreative2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAdsCreative2Response](../../models/operations/createadscreative2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_creative2

Retrieve a creative

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsCreative2" method="get" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.get_ads_creative2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAdsCreative2Request](../../models/operations/getadscreative2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAdsCreative2Response](../../models/operations/getadscreative2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_creatives2

List all creatives

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsCreatives2" method="get" path="/ads/{connection_id}/creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.list_ads_creatives2(request={
        "connection_id": "<id>",
    })

    assert res.ads_creatives is not None

    # Handle response
    print(res.ads_creatives)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAdsCreatives2Request](../../models/operations/listadscreatives2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAdsCreatives2Response](../../models/operations/listadscreatives2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_creative2

Update a creative

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsCreative2" method="patch" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.patch_ads_creative2(request={
        "ads_creative": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAdsCreative2Request](../../models/operations/patchadscreative2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAdsCreative2Response](../../models/operations/patchadscreative2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_creative2

Remove a creative

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsCreative2" method="delete" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.remove_ads_creative2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAdsCreative2Request](../../models/operations/removeadscreative2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAdsCreative2Response](../../models/operations/removeadscreative2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_creative2

Update a creative

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsCreative2" method="put" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creative.update_ads_creative2(request={
        "ads_creative": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAdsCreative2Request](../../models/operations/updateadscreative2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAdsCreative2Response](../../models/operations/updateadscreative2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |