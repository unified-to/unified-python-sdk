# Ads

## Overview

### Available Operations

* [create_ads_ad](#create_ads_ad) - Create an ad
* [create_ads_asset](#create_ads_asset) - Create an asset
* [create_ads_campaign](#create_ads_campaign) - Create a campaign
* [create_ads_creative](#create_ads_creative) - Create a creative
* [create_ads_group](#create_ads_group) - Create a group
* [create_ads_insertionorder](#create_ads_insertionorder) - Create an insertionorder
* [create_ads_organization](#create_ads_organization) - Create an organization
* [get_ads_ad](#get_ads_ad) - Retrieve an ad
* [get_ads_asset](#get_ads_asset) - Retrieve an asset
* [get_ads_campaign](#get_ads_campaign) - Retrieve a campaign
* [get_ads_creative](#get_ads_creative) - Retrieve a creative
* [get_ads_group](#get_ads_group) - Retrieve a group
* [get_ads_insertionorder](#get_ads_insertionorder) - Retrieve an insertionorder
* [get_ads_organization](#get_ads_organization) - Retrieve an organization
* [get_ads_promoted](#get_ads_promoted) - Retrieve a promoted
* [get_ads_target](#get_ads_target) - Retrieve a target
* [list_ads_ads](#list_ads_ads) - List all ads
* [list_ads_assets](#list_ads_assets) - List all assets
* [list_ads_campaigns](#list_ads_campaigns) - List all campaigns
* [list_ads_creatives](#list_ads_creatives) - List all creatives
* [list_ads_groups](#list_ads_groups) - List all groups
* [list_ads_insertionorders](#list_ads_insertionorders) - List all insertionorders
* [list_ads_organizations](#list_ads_organizations) - List all organizations
* [list_ads_promoteds](#list_ads_promoteds) - List all promoteds
* [list_ads_reports](#list_ads_reports) - List all reports
* [list_ads_targets](#list_ads_targets) - List all targets
* [patch_ads_ad](#patch_ads_ad) - Update an ad
* [patch_ads_campaign](#patch_ads_campaign) - Update a campaign
* [patch_ads_creative](#patch_ads_creative) - Update a creative
* [patch_ads_group](#patch_ads_group) - Update a group
* [patch_ads_insertionorder](#patch_ads_insertionorder) - Update an insertionorder
* [patch_ads_organization](#patch_ads_organization) - Update an organization
* [remove_ads_ad](#remove_ads_ad) - Remove an ad
* [remove_ads_campaign](#remove_ads_campaign) - Remove a campaign
* [remove_ads_creative](#remove_ads_creative) - Remove a creative
* [remove_ads_group](#remove_ads_group) - Remove a group
* [remove_ads_insertionorder](#remove_ads_insertionorder) - Remove an insertionorder
* [remove_ads_organization](#remove_ads_organization) - Remove an organization
* [update_ads_ad](#update_ads_ad) - Update an ad
* [update_ads_campaign](#update_ads_campaign) - Update a campaign
* [update_ads_creative](#update_ads_creative) - Update a creative
* [update_ads_group](#update_ads_group) - Update a group
* [update_ads_insertionorder](#update_ads_insertionorder) - Update an insertionorder
* [update_ads_organization](#update_ads_organization) - Update an organization

## create_ads_ad

Creates a AdsAd. Provide the unified AdsAd fields in the request body; they are mapped to the provider's API. Returns the created AdsAd.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsAd" method="post" path="/ads/{connection_id}/ad" example="ads_ad" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_ad(request={
        "ads_ad": {
            "ad_copy": "Ascisco tolero caute sapiente. Valens unde comedo cursus crinis nobis thema. Cohaero nisi ullam tum unde ultio vilicus auditor capio.",
            "ad_type": shared.AdType.SOCIAL,
            "advertiser_name": "Robel, Nader and Rau",
            "created_at": parse_datetime("2022-11-08T03:38:20.978Z"),
            "creative_asset_url": "https://picsum.photos/seed/LwOzrpr9/948/2793",
            "description": "Accedo vespillo carpo dolor decet stillicidium comptus tenuis.",
            "final_url": "https://improbable-sanity.com",
            "id": "19b51d94-4826-44bc-9a26-3bc7a44646fe",
            "metadata": [],
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-22T06:06:26.922Z"),
        },
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

## create_ads_asset

Creates a AdsAsset. Provide the unified AdsAsset fields in the request body; they are mapped to the provider's API. Returns the created AdsAsset.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsAsset" method="post" path="/ads/{connection_id}/asset" example="ads_asset" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_asset(request={
        "ads_asset": {
            "created_at": parse_datetime("2020-03-27T20:14:38.603Z"),
            "height": 400.0,
            "id": "6e4c08c6-ab7f-4720-9ef8-f0ea175026cf",
            "metadata": [],
            "mime_type": "IMAGE_PNG",
            "name": "Lockman - DuBuque",
            "type": shared.AdsAssetType.IMAGE,
            "updated_at": parse_datetime("2022-03-27T22:25:46.061Z"),
            "url": "https://informal-perfection.com/",
            "width": 600.0,
        },
        "connection_id": "<id>",
    })

    assert res.ads_asset is not None

    # Handle response
    print(res.ads_asset)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateAdsAssetRequest](../../models/operations/createadsassetrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateAdsAssetResponse](../../models/operations/createadsassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ads_campaign

Creates a AdsCampaign. Provide the unified AdsCampaign fields in the request body; they are mapped to the provider's API. Returns the created AdsCampaign.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsCampaign" method="post" path="/ads/{connection_id}/campaign" example="ads_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-06-07T04:14:23.987Z"),
            "id": "ae603529-f22f-4c87-ba72-d6eaecdefa69",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T19:02:56.443Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-08T23:42:30.322Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_campaign is not None

    # Handle response
    print(res.ads_campaign)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAdsCampaignRequest](../../models/operations/createadscampaignrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAdsCampaignResponse](../../models/operations/createadscampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ads_creative

Creates a AdsCreative. Provide the unified AdsCreative fields in the request body; they are mapped to the provider's API. Returns the created AdsCreative.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsCreative" method="post" path="/ads/{connection_id}/creative" example="ads_creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_creative(request={
        "ads_creative": {
            "created_at": parse_datetime("2020-02-17T11:24:51.093Z"),
            "id": "fff77e7c-392c-4a18-9e85-a731f97ee30e",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "metadata": [],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-29T14:26:57.980Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAdsCreativeRequest](../../models/operations/createadscreativerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAdsCreativeResponse](../../models/operations/createadscreativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ads_group

Creates a AdsGroup. Provide the unified AdsGroup fields in the request body; they are mapped to the provider's API. Returns the created AdsGroup.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsGroup" method="post" path="/ads/{connection_id}/group" example="ads_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_group(request={
        "ads_group": {
            "bid_amount": 26.16030164062977,
            "budget_amount": 5099.175239447504,
            "budget_period": shared.AdsGroupBudgetPeriod.MONTHLY,
            "created_at": parse_datetime("2019-08-29T17:59:41.045Z"),
            "currency": "USD",
            "effective_status": shared.AdsGroupEffectiveStatus.PAUSED,
            "end_at": parse_datetime("2026-07-03T16:39:25.785Z"),
            "id": "b0e4e101-556d-4ea2-89f8-99816e02423c",
            "language_locale": "fr-FR",
            "metadata": [],
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2026-01-17T08:01:59.234Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-16T16:22:29.843Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_group is not None

    # Handle response
    print(res.ads_group)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateAdsGroupRequest](../../models/operations/createadsgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateAdsGroupResponse](../../models/operations/createadsgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ads_insertionorder

Creates a AdsInsertionorder. Provide the unified AdsInsertionorder fields in the request body; they are mapped to the provider's API. Returns the created AdsInsertionorder.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsInsertionorder" method="post" path="/ads/{connection_id}/insertionorder" example="ads_insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_insertionorder(request={
        "ads_insertionorder": {
            "created_at": parse_datetime("2021-04-10T06:57:36.611Z"),
            "id": "bbff8487-f749-4442-9d58-77ff4208ed12",
            "metadata": [],
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T21:46:54.612Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAdsInsertionorderRequest](../../models/operations/createadsinsertionorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAdsInsertionorderResponse](../../models/operations/createadsinsertionorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ads_organization

Creates a AdsOrganization. Provide the unified AdsOrganization fields in the request body; they are mapped to the provider's API. Returns the created AdsOrganization.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsOrganization" method="post" path="/ads/{connection_id}/organization" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.create_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "0fca8576-a59c-4822-9650-ae8e3a50869a",
            "managers": [],
            "metadata": [],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-04-06T08:22:34.713Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAdsOrganizationRequest](../../models/operations/createadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAdsOrganizationResponse](../../models/operations/createadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_ad

Retrieves a single AdsAd by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

    res = unified_to.ads.get_ads_ad(request={
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

## get_ads_asset

Retrieves a single AdsAsset by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsAsset" method="get" path="/ads/{connection_id}/asset/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_asset(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_asset is not None

    # Handle response
    print(res.ads_asset)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetAdsAssetRequest](../../models/operations/getadsassetrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetAdsAssetResponse](../../models/operations/getadsassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_campaign

Retrieves a single AdsCampaign by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsCampaign" method="get" path="/ads/{connection_id}/campaign/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_campaign(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_campaign is not None

    # Handle response
    print(res.ads_campaign)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAdsCampaignRequest](../../models/operations/getadscampaignrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAdsCampaignResponse](../../models/operations/getadscampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_creative

Retrieves a single AdsCreative by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsCreative" method="get" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_creative(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAdsCreativeRequest](../../models/operations/getadscreativerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAdsCreativeResponse](../../models/operations/getadscreativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_group

Retrieves a single AdsGroup by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsGroup" method="get" path="/ads/{connection_id}/group/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_group(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_group is not None

    # Handle response
    print(res.ads_group)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetAdsGroupRequest](../../models/operations/getadsgrouprequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetAdsGroupResponse](../../models/operations/getadsgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_insertionorder

Retrieves a single AdsInsertionorder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsInsertionorder" method="get" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_insertionorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAdsInsertionorderRequest](../../models/operations/getadsinsertionorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAdsInsertionorderResponse](../../models/operations/getadsinsertionorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_organization

Retrieves a single AdsOrganization by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsOrganization" method="get" path="/ads/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAdsOrganizationRequest](../../models/operations/getadsorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAdsOrganizationResponse](../../models/operations/getadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_promoted

Retrieves a single AdsPromoted by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

    res = unified_to.ads.get_ads_promoted(request={
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

## get_ads_target

Retrieves a single AdsTarget by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsTarget" method="get" path="/ads/{connection_id}/target/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.get_ads_target(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_target is not None

    # Handle response
    print(res.ads_target)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetAdsTargetRequest](../../models/operations/getadstargetrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetAdsTargetResponse](../../models/operations/getadstargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_ads

Returns a list of AdsAds. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

    res = unified_to.ads.list_ads_ads(request={
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

## list_ads_assets

Returns a list of AdsAssets. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsAssets" method="get" path="/ads/{connection_id}/asset" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_assets(request={
        "connection_id": "<id>",
    })

    assert res.ads_assets is not None

    # Handle response
    print(res.ads_assets)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListAdsAssetsRequest](../../models/operations/listadsassetsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListAdsAssetsResponse](../../models/operations/listadsassetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_campaigns

Returns a list of AdsCampaigns. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsCampaigns" method="get" path="/ads/{connection_id}/campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_campaigns(request={
        "connection_id": "<id>",
    })

    assert res.ads_campaigns is not None

    # Handle response
    print(res.ads_campaigns)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAdsCampaignsRequest](../../models/operations/listadscampaignsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAdsCampaignsResponse](../../models/operations/listadscampaignsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_creatives

Returns a list of AdsCreatives. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsCreatives" method="get" path="/ads/{connection_id}/creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_creatives(request={
        "connection_id": "<id>",
    })

    assert res.ads_creatives is not None

    # Handle response
    print(res.ads_creatives)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAdsCreativesRequest](../../models/operations/listadscreativesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAdsCreativesResponse](../../models/operations/listadscreativesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_groups

Returns a list of AdsGroups. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsGroups" method="get" path="/ads/{connection_id}/group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_groups(request={
        "connection_id": "<id>",
    })

    assert res.ads_groups is not None

    # Handle response
    print(res.ads_groups)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListAdsGroupsRequest](../../models/operations/listadsgroupsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListAdsGroupsResponse](../../models/operations/listadsgroupsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_insertionorders

Returns a list of AdsInsertionorders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsInsertionorders" method="get" path="/ads/{connection_id}/insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_insertionorders(request={
        "connection_id": "<id>",
    })

    assert res.ads_insertionorders is not None

    # Handle response
    print(res.ads_insertionorders)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAdsInsertionordersRequest](../../models/operations/listadsinsertionordersrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAdsInsertionordersResponse](../../models/operations/listadsinsertionordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_organizations

Returns a list of AdsOrganizations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsOrganizations" method="get" path="/ads/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_organizations(request={
        "connection_id": "<id>",
    })

    assert res.ads_organizations is not None

    # Handle response
    print(res.ads_organizations)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAdsOrganizationsRequest](../../models/operations/listadsorganizationsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAdsOrganizationsResponse](../../models/operations/listadsorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_promoteds

Returns a list of AdsPromoteds. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

    res = unified_to.ads.list_ads_promoteds(request={
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

## list_ads_reports

Returns a list of AdsReports. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsReports" method="get" path="/ads/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_reports(request={
        "connection_id": "<id>",
    })

    assert res.ads_reports is not None

    # Handle response
    print(res.ads_reports)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListAdsReportsRequest](../../models/operations/listadsreportsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListAdsReportsResponse](../../models/operations/listadsreportsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_targets

Returns a list of AdsTargets. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsTargets" method="get" path="/ads/{connection_id}/target" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.list_ads_targets(request={
        "connection_id": "<id>",
    })

    assert res.ads_targets is not None

    # Handle response
    print(res.ads_targets)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListAdsTargetsRequest](../../models/operations/listadstargetsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListAdsTargetsResponse](../../models/operations/listadstargetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_ad

Updates the AdsAd identified by `id`. Provide the unified AdsAd fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsAd" method="patch" path="/ads/{connection_id}/ad/{id}" example="ads_ad" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_ad(request={
        "ads_ad": {
            "ad_copy": "Ascisco tolero caute sapiente. Valens unde comedo cursus crinis nobis thema. Cohaero nisi ullam tum unde ultio vilicus auditor capio.",
            "ad_type": shared.AdType.SOCIAL,
            "advertiser_name": "Robel, Nader and Rau",
            "created_at": parse_datetime("2022-11-08T03:38:20.978Z"),
            "creative_asset_url": "https://picsum.photos/seed/LwOzrpr9/948/2793",
            "description": "Accedo vespillo carpo dolor decet stillicidium comptus tenuis.",
            "final_url": "https://improbable-sanity.com",
            "id": "023ba780-e0be-4809-bce4-b442b1ea90fe",
            "metadata": [],
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-22T06:06:26.931Z"),
        },
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

## patch_ads_campaign

Updates the AdsCampaign identified by `id`. Provide the unified AdsCampaign fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsCampaign" method="patch" path="/ads/{connection_id}/campaign/{id}" example="ads_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-06-07T04:14:24.086Z"),
            "id": "c78f2f65-b84c-43fe-8afe-7e695f7ee21f",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T19:02:56.448Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-08T23:42:30.440Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_campaign is not None

    # Handle response
    print(res.ads_campaign)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAdsCampaignRequest](../../models/operations/patchadscampaignrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAdsCampaignResponse](../../models/operations/patchadscampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_creative

Updates the AdsCreative identified by `id`. Provide the unified AdsCreative fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsCreative" method="patch" path="/ads/{connection_id}/creative/{id}" example="ads_creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_creative(request={
        "ads_creative": {
            "created_at": parse_datetime("2020-02-17T11:24:51.093Z"),
            "id": "b506821e-3241-4862-902f-cc4130dc8dd6",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "metadata": [],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-29T14:26:57.990Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_creative is not None

    # Handle response
    print(res.ads_creative)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAdsCreativeRequest](../../models/operations/patchadscreativerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAdsCreativeResponse](../../models/operations/patchadscreativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_group

Updates the AdsGroup identified by `id`. Provide the unified AdsGroup fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsGroup" method="patch" path="/ads/{connection_id}/group/{id}" example="ads_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_group(request={
        "ads_group": {
            "bid_amount": 26.16030164062977,
            "budget_amount": 5099.175239447504,
            "budget_period": shared.AdsGroupBudgetPeriod.MONTHLY,
            "created_at": parse_datetime("2019-08-29T17:59:41.045Z"),
            "currency": "USD",
            "effective_status": shared.AdsGroupEffectiveStatus.PAUSED,
            "end_at": parse_datetime("2026-07-03T16:39:25.925Z"),
            "id": "41657731-df09-49f6-81b2-6ecf6d6e638d",
            "language_locale": "fr-FR",
            "metadata": [],
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2026-01-17T08:01:59.364Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-16T16:22:29.891Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_group is not None

    # Handle response
    print(res.ads_group)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchAdsGroupRequest](../../models/operations/patchadsgrouprequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchAdsGroupResponse](../../models/operations/patchadsgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_insertionorder

Updates the AdsInsertionorder identified by `id`. Provide the unified AdsInsertionorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsInsertionorder" method="patch" path="/ads/{connection_id}/insertionorder/{id}" example="ads_insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_insertionorder(request={
        "ads_insertionorder": {
            "created_at": parse_datetime("2021-04-10T06:57:36.611Z"),
            "id": "5b58360d-99ef-4656-a040-67745ad066f2",
            "metadata": [],
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T21:46:54.612Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAdsInsertionorderRequest](../../models/operations/patchadsinsertionorderrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAdsInsertionorderResponse](../../models/operations/patchadsinsertionorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_organization

Updates the AdsOrganization identified by `id`. Provide the unified AdsOrganization fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsOrganization" method="patch" path="/ads/{connection_id}/organization/{id}" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.patch_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "871959de-4e11-4c66-81e1-417e96e66607",
            "managers": [],
            "metadata": [],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-04-06T08:22:34.735Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAdsOrganizationRequest](../../models/operations/patchadsorganizationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAdsOrganizationResponse](../../models/operations/patchadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_ad

Deletes the AdsAd identified by `id`.

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

    res = unified_to.ads.remove_ads_ad(request={
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

## remove_ads_campaign

Deletes the AdsCampaign identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsCampaign" method="delete" path="/ads/{connection_id}/campaign/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.remove_ads_campaign(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveAdsCampaignRequest](../../models/operations/removeadscampaignrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAdsCampaignResponse](../../models/operations/removeadscampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_creative

Deletes the AdsCreative identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsCreative" method="delete" path="/ads/{connection_id}/creative/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.remove_ads_creative(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveAdsCreativeRequest](../../models/operations/removeadscreativerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAdsCreativeResponse](../../models/operations/removeadscreativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_group

Deletes the AdsGroup identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsGroup" method="delete" path="/ads/{connection_id}/group/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.remove_ads_group(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveAdsGroupRequest](../../models/operations/removeadsgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveAdsGroupResponse](../../models/operations/removeadsgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_insertionorder

Deletes the AdsInsertionorder identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsInsertionorder" method="delete" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.remove_ads_insertionorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAdsInsertionorderRequest](../../models/operations/removeadsinsertionorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAdsInsertionorderResponse](../../models/operations/removeadsinsertionorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_organization

Deletes the AdsOrganization identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsOrganization" method="delete" path="/ads/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.remove_ads_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAdsOrganizationRequest](../../models/operations/removeadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAdsOrganizationResponse](../../models/operations/removeadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_ad

Updates the AdsAd identified by `id`. Provide the unified AdsAd fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsAd" method="put" path="/ads/{connection_id}/ad/{id}" example="ads_ad" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_ad(request={
        "ads_ad": {
            "ad_copy": "Ascisco tolero caute sapiente. Valens unde comedo cursus crinis nobis thema. Cohaero nisi ullam tum unde ultio vilicus auditor capio.",
            "ad_type": shared.AdType.SOCIAL,
            "advertiser_name": "Robel, Nader and Rau",
            "created_at": parse_datetime("2022-11-08T03:38:20.978Z"),
            "creative_asset_url": "https://picsum.photos/seed/LwOzrpr9/948/2793",
            "description": "Accedo vespillo carpo dolor decet stillicidium comptus tenuis.",
            "final_url": "https://improbable-sanity.com",
            "id": "023ba780-e0be-4809-bce4-b442b1ea90fe",
            "metadata": [],
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-22T06:06:26.931Z"),
        },
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

## update_ads_campaign

Updates the AdsCampaign identified by `id`. Provide the unified AdsCampaign fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsCampaign" method="put" path="/ads/{connection_id}/campaign/{id}" example="ads_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-06-07T04:14:24.086Z"),
            "id": "c78f2f65-b84c-43fe-8afe-7e695f7ee21f",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T19:02:56.448Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-08T23:42:30.440Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_campaign is not None

    # Handle response
    print(res.ads_campaign)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAdsCampaignRequest](../../models/operations/updateadscampaignrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAdsCampaignResponse](../../models/operations/updateadscampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_creative

Updates the AdsCreative identified by `id`. Provide the unified AdsCreative fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsCreative" method="put" path="/ads/{connection_id}/creative/{id}" example="ads_creative" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_creative(request={
        "ads_creative": {
            "created_at": parse_datetime("2020-02-17T11:24:51.093Z"),
            "id": "b506821e-3241-4862-902f-cc4130dc8dd6",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "metadata": [],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-29T14:26:57.990Z"),
        },
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
| `request`                                                                                  | [operations.UpdateAdsCreativeRequest](../../models/operations/updateadscreativerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAdsCreativeResponse](../../models/operations/updateadscreativeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_group

Updates the AdsGroup identified by `id`. Provide the unified AdsGroup fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsGroup" method="put" path="/ads/{connection_id}/group/{id}" example="ads_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_group(request={
        "ads_group": {
            "bid_amount": 26.16030164062977,
            "budget_amount": 5099.175239447504,
            "budget_period": shared.AdsGroupBudgetPeriod.MONTHLY,
            "created_at": parse_datetime("2019-08-29T17:59:41.045Z"),
            "currency": "USD",
            "effective_status": shared.AdsGroupEffectiveStatus.PAUSED,
            "end_at": parse_datetime("2026-07-03T16:39:25.925Z"),
            "id": "41657731-df09-49f6-81b2-6ecf6d6e638d",
            "language_locale": "fr-FR",
            "metadata": [],
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2026-01-17T08:01:59.364Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-16T16:22:29.891Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_group is not None

    # Handle response
    print(res.ads_group)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateAdsGroupRequest](../../models/operations/updateadsgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateAdsGroupResponse](../../models/operations/updateadsgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_insertionorder

Updates the AdsInsertionorder identified by `id`. Provide the unified AdsInsertionorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsInsertionorder" method="put" path="/ads/{connection_id}/insertionorder/{id}" example="ads_insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_insertionorder(request={
        "ads_insertionorder": {
            "created_at": parse_datetime("2021-04-10T06:57:36.611Z"),
            "id": "5b58360d-99ef-4656-a040-67745ad066f2",
            "metadata": [],
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T21:46:54.612Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAdsInsertionorderRequest](../../models/operations/updateadsinsertionorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAdsInsertionorderResponse](../../models/operations/updateadsinsertionorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_organization

Updates the AdsOrganization identified by `id`. Provide the unified AdsOrganization fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsOrganization" method="put" path="/ads/{connection_id}/organization/{id}" example="ads_organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ads.update_ads_organization(request={
        "ads_organization": {
            "account_number": "LQUJx8zQBW",
            "created_at": parse_datetime("2020-07-23T21:47:11.440Z"),
            "currency": "USD",
            "id": "871959de-4e11-4c66-81e1-417e96e66607",
            "managers": [],
            "metadata": [],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-04-06T08:22:34.735Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_organization is not None

    # Handle response
    print(res.ads_organization)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAdsOrganizationRequest](../../models/operations/updateadsorganizationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAdsOrganizationResponse](../../models/operations/updateadsorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |