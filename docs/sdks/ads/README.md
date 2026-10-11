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

Create an ad

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
            "id": "260e56bb-d295-4f90-81c6-b63eecdb3201",
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-14T11:49:54.627Z"),
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

Create an asset

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
            "id": "0b48e2f9-2d4a-4a30-ba2d-2e6cc12ae4b0",
            "mime_type": "IMAGE_PNG",
            "name": "Lockman - DuBuque",
            "type": shared.AdsAssetType.IMAGE,
            "updated_at": parse_datetime("2022-03-22T03:53:44.624Z"),
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

Create a campaign

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
            "end_at": parse_datetime("2025-05-25T02:59:49.820Z"),
            "id": "a54c81b7-2d80-4802-bc73-60534c462125",
            "labels": [
                "comedo",
            ],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T01:45:31.358Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2025-12-24T09:43:01.805Z"),
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

Create a creative

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
            "id": "92c5c536-991c-4ba6-880c-349f9b390888",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-25T17:27:05.688Z"),
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

Create a group

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
            "end_at": parse_datetime("2026-06-15T12:32:26.945Z"),
            "id": "c12fdd91-a24b-4d8d-8ebc-b4d394c5cb30",
            "language_locale": "fr-FR",
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2025-12-31T09:06:45.660Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-10T08:26:25.470Z"),
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

Create an insertionorder

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
            "id": "13b4831e-e8b3-4cf5-a620-2c12e8322b5a",
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T17:35:24.669Z"),
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

Create an organization

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
            "id": "b2e8806e-2361-427a-804d-dd4221087617",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-20T00:51:22.274Z"),
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

Retrieve an asset

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

Retrieve a campaign

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

Retrieve a creative

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

Retrieve a group

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

Retrieve an insertionorder

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

Retrieve an organization

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

Retrieve a target

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

List all assets

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

List all campaigns

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

List all creatives

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

List all groups

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

List all insertionorders

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

List all organizations

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

List all reports

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

List all targets

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

Update an ad

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
            "id": "f9915792-eeea-445e-808f-aa05183da6b5",
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-14T11:49:54.635Z"),
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

Update a campaign

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
            "end_at": parse_datetime("2025-05-25T02:59:49.928Z"),
            "id": "4b2f33cf-6d7a-48cb-a04f-5f336236c28f",
            "labels": [
                "comedo",
            ],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T01:45:31.364Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2025-12-24T09:43:01.933Z"),
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

Update a creative

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
            "id": "14bf089e-f5ef-498d-aa1e-2e14dbbf7bb6",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-25T17:27:05.692Z"),
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

Update a group

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
            "end_at": parse_datetime("2026-06-15T12:32:27.043Z"),
            "id": "fb1c3be7-5f34-4017-9b5b-eabdc7de25e1",
            "language_locale": "fr-FR",
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2025-12-31T09:06:45.751Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-10T08:26:25.504Z"),
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

Update an insertionorder

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
            "id": "e070e85d-64f6-489e-9e85-5dfafc957e4b",
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T17:35:24.669Z"),
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

Update an organization

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
            "id": "f683ccba-8b2e-4b81-b011-5fa9cfbe0db0",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-20T00:51:22.284Z"),
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

Remove a campaign

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

Remove a creative

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

Remove a group

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

Remove an insertionorder

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

Remove an organization

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

Update an ad

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
            "id": "f9915792-eeea-445e-808f-aa05183da6b5",
            "name": "Hermiston Group",
            "status": shared.AdsAdStatus.ARCHIVED,
            "updated_at": parse_datetime("2024-06-14T11:49:54.635Z"),
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

Update a campaign

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
            "end_at": parse_datetime("2025-05-25T02:59:49.928Z"),
            "id": "4b2f33cf-6d7a-48cb-a04f-5f336236c28f",
            "labels": [
                "comedo",
            ],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T01:45:31.364Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2025-12-24T09:43:01.933Z"),
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

Update a creative

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
            "id": "14bf089e-f5ef-498d-aa1e-2e14dbbf7bb6",
            "labels": [
                "coma",
                "accedo",
                "termes",
            ],
            "name": "Brekke, Bradtke and Robel",
            "status": shared.AdsCreativeStatus.PAUSED,
            "updated_at": parse_datetime("2021-06-25T17:27:05.692Z"),
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

Update a group

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
            "end_at": parse_datetime("2026-06-15T12:32:27.043Z"),
            "id": "fb1c3be7-5f34-4017-9b5b-eabdc7de25e1",
            "language_locale": "fr-FR",
            "name": "Stark - Baumbach",
            "start_at": parse_datetime("2025-12-31T09:06:45.751Z"),
            "status": shared.AdsGroupStatus.PROCESSING,
            "targeting": {},
            "updated_at": parse_datetime("2022-01-10T08:26:25.504Z"),
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

Update an insertionorder

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
            "id": "e070e85d-64f6-489e-9e85-5dfafc957e4b",
            "name": "Kunde, Smith and Reinger",
            "status": shared.AdsInsertionorderStatus.UNSPECIFIED,
            "updated_at": parse_datetime("2021-04-28T17:35:24.669Z"),
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

Update an organization

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
            "id": "f683ccba-8b2e-4b81-b011-5fa9cfbe0db0",
            "managers": [
                {
                    "id": "e4fd87df-9f8b-4fa0-a77b-b7d18669e350",
                    "name": "Parker, Leannon and Gibson",
                },
            ],
            "name": "Ankunding Inc",
            "status": shared.AdsOrganizationStatus.PROCESSING,
            "timezone": "Europe/Chisinau",
            "updated_at": parse_datetime("2026-03-20T00:51:22.284Z"),
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