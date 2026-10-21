# Campaign

## Overview

### Available Operations

* [create_ads_campaign](#create_ads_campaign) - Create a campaign
* [create_martech_campaign](#create_martech_campaign) - Create a campaign
* [get_ads_campaign](#get_ads_campaign) - Retrieve a campaign
* [get_martech_campaign](#get_martech_campaign) - Retrieve a campaign
* [list_ads_campaigns](#list_ads_campaigns) - List all campaigns
* [list_martech_campaigns](#list_martech_campaigns) - List all campaigns
* [patch_ads_campaign](#patch_ads_campaign) - Update a campaign
* [patch_martech_campaign](#patch_martech_campaign) - Update a campaign
* [remove_ads_campaign](#remove_ads_campaign) - Remove a campaign
* [remove_martech_campaign](#remove_martech_campaign) - Remove a campaign
* [update_ads_campaign](#update_ads_campaign) - Update a campaign
* [update_martech_campaign](#update_martech_campaign) - Update a campaign

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

    res = unified_to.campaign.create_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-05-31T23:26:56.615Z"),
            "id": "4d2fc8a6-0125-4929-8012-2e17b706b5bd",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T10:50:09.909Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-01T14:03:42.719Z"),
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

## create_martech_campaign

Create a campaign

### Example Usage

<!-- UsageSnippet language="python" operationID="createMartechCampaign" method="post" path="/martech/{connection_id}/campaign" example="martech_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.create_martech_campaign(request={
        "marketing_campaign": {
            "created_at": parse_datetime("2019-05-19T11:18:15.589Z"),
            "from_email": "graham.mertz@gmail.com",
            "from_name": "Graham Mertz",
            "id": "f70a1360-e5df-471c-83ac-71222f0ab7c2",
            "metadata": [],
            "name": "Consequatur atqui sustineo.",
            "preview_text": "Auctus votum ver umbra corroboro turpis spoliatio tamen strues auxilium benigne tempus error eaque suasoria.",
            "reply_to_email": "graham.mertz@icloud.com",
            "send_at": parse_datetime("2024-01-23T21:19:26.708Z"),
            "status": shared.MarketingCampaignStatus.SCHEDULED,
            "subject_line": "Trepide utpote conculco tibi solio supplanto peior tibi.",
            "type": "absplit",
            "updated_at": parse_datetime("2022-06-22T02:48:16.946Z"),
        },
        "connection_id": "<id>",
    })

    assert res.marketing_campaign is not None

    # Handle response
    print(res.marketing_campaign)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateMartechCampaignRequest](../../models/operations/createmartechcampaignrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateMartechCampaignResponse](../../models/operations/createmartechcampaignresponse.md)**

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

    res = unified_to.campaign.get_ads_campaign(request={
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

## get_martech_campaign

Retrieve a campaign

### Example Usage

<!-- UsageSnippet language="python" operationID="getMartechCampaign" method="get" path="/martech/{connection_id}/campaign/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.get_martech_campaign(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_campaign is not None

    # Handle response
    print(res.marketing_campaign)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetMartechCampaignRequest](../../models/operations/getmartechcampaignrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetMartechCampaignResponse](../../models/operations/getmartechcampaignresponse.md)**

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

    res = unified_to.campaign.list_ads_campaigns(request={
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

## list_martech_campaigns

List all campaigns

### Example Usage

<!-- UsageSnippet language="python" operationID="listMartechCampaigns" method="get" path="/martech/{connection_id}/campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.list_martech_campaigns(request={
        "connection_id": "<id>",
    })

    assert res.marketing_campaigns is not None

    # Handle response
    print(res.marketing_campaigns)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListMartechCampaignsRequest](../../models/operations/listmartechcampaignsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListMartechCampaignsResponse](../../models/operations/listmartechcampaignsresponse.md)**

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

    res = unified_to.campaign.patch_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-05-31T23:26:56.734Z"),
            "id": "15dd6daf-7978-40b5-b066-11670d6a948b",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T10:50:09.916Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-01T14:03:42.861Z"),
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

## patch_martech_campaign

Update a campaign

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMartechCampaign" method="patch" path="/martech/{connection_id}/campaign/{id}" example="martech_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.patch_martech_campaign(request={
        "marketing_campaign": {
            "created_at": parse_datetime("2019-05-19T11:18:15.589Z"),
            "from_email": "graham.mertz@gmail.com",
            "from_name": "Graham Mertz",
            "id": "56b0a145-4a67-48a0-a319-0aa1c1bc69b0",
            "metadata": [],
            "name": "Consequatur atqui sustineo.",
            "preview_text": "Auctus votum ver umbra corroboro turpis spoliatio tamen strues auxilium benigne tempus error eaque suasoria.",
            "reply_to_email": "graham.mertz@icloud.com",
            "send_at": parse_datetime("2024-01-23T21:19:26.708Z"),
            "status": shared.MarketingCampaignStatus.SCHEDULED,
            "subject_line": "Trepide utpote conculco tibi solio supplanto peior tibi.",
            "type": "absplit",
            "updated_at": parse_datetime("2022-06-22T02:48:16.953Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_campaign is not None

    # Handle response
    print(res.marketing_campaign)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchMartechCampaignRequest](../../models/operations/patchmartechcampaignrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchMartechCampaignResponse](../../models/operations/patchmartechcampaignresponse.md)**

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

    res = unified_to.campaign.remove_ads_campaign(request={
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

## remove_martech_campaign

Remove a campaign

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMartechCampaign" method="delete" path="/martech/{connection_id}/campaign/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.remove_martech_campaign(request={
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
| `request`                                                                                          | [operations.RemoveMartechCampaignRequest](../../models/operations/removemartechcampaignrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveMartechCampaignResponse](../../models/operations/removemartechcampaignresponse.md)**

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

    res = unified_to.campaign.update_ads_campaign(request={
        "ads_campaign": {
            "budget_amount": 8743.179536121897,
            "budget_period": shared.BudgetPeriod.MONTHLY,
            "category": "CREDIT",
            "created_at": parse_datetime("2022-05-21T08:51:41.868Z"),
            "currency": "USD",
            "effective_status": shared.EffectiveStatus.NOT_ELIGIBLE,
            "end_at": parse_datetime("2025-05-31T23:26:56.734Z"),
            "id": "15dd6daf-7978-40b5-b066-11670d6a948b",
            "labels": [
                "comedo",
            ],
            "metadata": [],
            "name": "Emard Inc",
            "start_at": parse_datetime("2022-07-21T10:50:09.916Z"),
            "status": shared.AdsCampaignStatus.PROCESSING_FAILED,
            "targeting": {},
            "total_spend_amount": 2349.8642875347286,
            "updated_at": parse_datetime("2026-01-01T14:03:42.861Z"),
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

## update_martech_campaign

Update a campaign

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMartechCampaign" method="put" path="/martech/{connection_id}/campaign/{id}" example="martech_campaign" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.campaign.update_martech_campaign(request={
        "marketing_campaign": {
            "created_at": parse_datetime("2019-05-19T11:18:15.589Z"),
            "from_email": "graham.mertz@gmail.com",
            "from_name": "Graham Mertz",
            "id": "56b0a145-4a67-48a0-a319-0aa1c1bc69b0",
            "metadata": [],
            "name": "Consequatur atqui sustineo.",
            "preview_text": "Auctus votum ver umbra corroboro turpis spoliatio tamen strues auxilium benigne tempus error eaque suasoria.",
            "reply_to_email": "graham.mertz@icloud.com",
            "send_at": parse_datetime("2024-01-23T21:19:26.708Z"),
            "status": shared.MarketingCampaignStatus.SCHEDULED,
            "subject_line": "Trepide utpote conculco tibi solio supplanto peior tibi.",
            "type": "absplit",
            "updated_at": parse_datetime("2022-06-22T02:48:16.953Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_campaign is not None

    # Handle response
    print(res.marketing_campaign)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateMartechCampaignRequest](../../models/operations/updatemartechcampaignrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateMartechCampaignResponse](../../models/operations/updatemartechcampaignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |