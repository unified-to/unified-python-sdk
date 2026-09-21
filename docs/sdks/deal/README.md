# Deal

## Overview

### Available Operations

* [create_crm_deal](#create_crm_deal) - Create a deal
* [get_crm_deal](#get_crm_deal) - Retrieve a deal
* [list_crm_deals](#list_crm_deals) - List all deals
* [patch_crm_deal](#patch_crm_deal) - Update a deal
* [remove_crm_deal](#remove_crm_deal) - Remove a deal
* [update_crm_deal](#update_crm_deal) - Update a deal

## create_crm_deal

Create a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmDeal" method="post" path="/crm/{connection_id}/deal" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.create_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-04T03:42:33.293Z"),
            "closing_at": parse_datetime("2025-08-11T17:45:27.374Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "e77492f0-b53c-4d4d-b3ef-85d2d39be486",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "e1c225b7-8757-4f46-8c4d-ee1d832af116",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "8922651b-a8c6-4754-a2fc-da9720b7ce19",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "0c4358bb-e675-499a-9912-7251e4ede38c",
                    "name": "tubineus",
                },
                {
                    "id": "ef1f5757-5d28-46e5-bbbc-0efde5730f83",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-30T05:08:02.851Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmDealRequest](../../models/operations/createcrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateCrmDealResponse](../../models/operations/createcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_deal

Retrieve a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmDeal" method="get" path="/crm/{connection_id}/deal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.get_crm_deal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmDealRequest](../../models/operations/getcrmdealrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetCrmDealResponse](../../models/operations/getcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_deals

List all deals

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmDeals" method="get" path="/crm/{connection_id}/deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.list_crm_deals(request={
        "connection_id": "<id>",
    })

    assert res.crm_deals is not None

    # Handle response
    print(res.crm_deals)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmDealsRequest](../../models/operations/listcrmdealsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListCrmDealsResponse](../../models/operations/listcrmdealsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_deal

Update a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmDeal" method="patch" path="/crm/{connection_id}/deal/{id}" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.patch_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-04T03:42:33.297Z"),
            "closing_at": parse_datetime("2025-08-11T17:45:27.385Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "a6dd5bf7-ba96-4e40-a0a0-9e3d65c59226",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "464a8175-f552-4506-9788-c870b7a0cb49",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "ffafefa5-2e31-4297-94a4-77985a194477",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "e574073c-430c-424c-a2ef-cad6abbbe0a4",
                    "name": "tubineus",
                },
                {
                    "id": "e0b01341-4d13-4d8b-9014-191221d8348c",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-30T05:08:02.858Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmDealRequest](../../models/operations/patchcrmdealrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchCrmDealResponse](../../models/operations/patchcrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_deal

Remove a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmDeal" method="delete" path="/crm/{connection_id}/deal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.remove_crm_deal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmDealRequest](../../models/operations/removecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemoveCrmDealResponse](../../models/operations/removecrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_deal

Update a deal

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmDeal" method="put" path="/crm/{connection_id}/deal/{id}" example="crm_deal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.update_crm_deal(request={
        "crm_deal": {
            "amount": 98162.0,
            "closed_at": parse_datetime("2024-03-04T03:42:33.297Z"),
            "closing_at": parse_datetime("2025-08-11T17:45:27.385Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "a6dd5bf7-ba96-4e40-a0a0-9e3d65c59226",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "464a8175-f552-4506-9788-c870b7a0cb49",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "ffafefa5-2e31-4297-94a4-77985a194477",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "e574073c-430c-424c-a2ef-cad6abbbe0a4",
                    "name": "tubineus",
                },
                {
                    "id": "e0b01341-4d13-4d8b-9014-191221d8348c",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-09-30T05:08:02.858Z"),
            "won_reason": "Usque libero soleo.",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_deal is not None

    # Handle response
    print(res.crm_deal)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmDealRequest](../../models/operations/updatecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateCrmDealResponse](../../models/operations/updatecrmdealresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |