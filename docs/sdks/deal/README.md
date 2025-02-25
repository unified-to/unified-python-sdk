# Deal
(*deal*)

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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.create_crm_deal(request={
        "crm_deal": {},
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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.patch_crm_deal(request={
        "crm_deal": {},
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

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.deal.update_crm_deal(request={
        "crm_deal": {},
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