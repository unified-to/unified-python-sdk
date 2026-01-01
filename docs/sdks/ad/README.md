# Ad

## Overview

### Available Operations

* [create_ads_ad](#create_ads_ad) - Create an ad
* [get_ads_ad](#get_ads_ad) - Retrieve an ad
* [list_ads_ads](#list_ads_ads) - List all ads
* [patch_ads_ad](#patch_ads_ad) - Update an ad
* [remove_ads_ad](#remove_ads_ad) - Remove an ad
* [update_ads_ad](#update_ads_ad) - Update an ad

## create_ads_ad

Create an ad

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsAd" method="post" path="/ads/{connection_id}/ad" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.create_ads_ad(request={
        "ads_ad": {},
        "connection_id": "<id>",
    })

    assert res.ads_ad is not None

    # Handle response
    print(res.ads_ad)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateAdsAdRequest](../../models/operations/createadsadrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CreateAdsAdResponse](../../models/operations/createadsadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_ad

Retrieve an ad

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsAd" method="get" path="/ads/{connection_id}/ad/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.get_ads_ad(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_ad is not None

    # Handle response
    print(res.ads_ad)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetAdsAdRequest](../../models/operations/getadsadrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.GetAdsAdResponse](../../models/operations/getadsadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_ads

List all ads

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsAds" method="get" path="/ads/{connection_id}/ad" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.list_ads_ads(request={
        "connection_id": "<id>",
    })

    assert res.ads_ads is not None

    # Handle response
    print(res.ads_ads)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListAdsAdsRequest](../../models/operations/listadsadsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.ListAdsAdsResponse](../../models/operations/listadsadsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_ad

Update an ad

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsAd" method="patch" path="/ads/{connection_id}/ad/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.patch_ads_ad(request={
        "ads_ad": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_ad is not None

    # Handle response
    print(res.ads_ad)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.PatchAdsAdRequest](../../models/operations/patchadsadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.PatchAdsAdResponse](../../models/operations/patchadsadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_ad

Remove an ad

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsAd" method="delete" path="/ads/{connection_id}/ad/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.remove_ads_ad(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RemoveAdsAdRequest](../../models/operations/removeadsadrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.RemoveAdsAdResponse](../../models/operations/removeadsadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_ad

Update an ad

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsAd" method="put" path="/ads/{connection_id}/ad/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ad.update_ads_ad(request={
        "ads_ad": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_ad is not None

    # Handle response
    print(res.ads_ad)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateAdsAdRequest](../../models/operations/updateadsadrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.UpdateAdsAdResponse](../../models/operations/updateadsadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |