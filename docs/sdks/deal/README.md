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
            "closed_at": parse_datetime("2024-03-08T22:37:52.437Z"),
            "closing_at": parse_datetime("2025-08-26T20:36:41.042Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "7e6c12b9-0d7e-4fff-9baa-791736127e88",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "f7ebd73a-055e-4c46-a0c8-e05633dbef5b",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "27975d06-0060-4f2c-8248-789b92a90604",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "b012ca63-f323-4b10-a196-aa5b6c46a1b9",
                    "name": "tubineus",
                },
                {
                    "id": "05c62317-d945-4ac4-9d1e-5dd613154bc0",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-09T03:08:47.009Z"),
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
            "closed_at": parse_datetime("2024-03-08T22:37:52.441Z"),
            "closing_at": parse_datetime("2025-08-26T20:36:41.054Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "819c0b52-617b-4400-b660-5a426f5ac6c1",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "b5b924ce-765c-46ed-b9f6-f65d192f2336",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "74af7eef-f16b-4f73-8fd4-7388abb1486f",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "f3dba15a-165e-4f84-acff-9492ef75d924",
                    "name": "tubineus",
                },
                {
                    "id": "85553304-6e70-4e10-8cd6-cd41143c7249",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-09T03:08:47.016Z"),
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
            "closed_at": parse_datetime("2024-03-08T22:37:52.441Z"),
            "closing_at": parse_datetime("2025-08-26T20:36:41.054Z"),
            "created_at": parse_datetime("2023-07-04T12:48:48.470Z"),
            "currency": "IQD",
            "description": "Tabula cicuta sophismata comis tepidus sit cavus.",
            "id": "819c0b52-617b-4400-b660-5a426f5ac6c1",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.CrmMetadataFormat.TEXT,
                    "id": "b5b924ce-765c-46ed-b9f6-f65d192f2336",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "conatus",
                },
            ],
            "name": "Frozen Silk Chicken",
            "pipelines": [
                {
                    "id": "74af7eef-f16b-4f73-8fd4-7388abb1486f",
                    "name": "trans",
                },
            ],
            "probability": 65.0,
            "source": "cubo",
            "stages": [
                {
                    "id": "f3dba15a-165e-4f84-acff-9492ef75d924",
                    "name": "tubineus",
                },
                {
                    "id": "85553304-6e70-4e10-8cd6-cd41143c7249",
                    "name": "adfectus",
                },
            ],
            "tags": [
                "causa",
                "suus",
            ],
            "updated_at": parse_datetime("2024-10-09T03:08:47.016Z"),
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