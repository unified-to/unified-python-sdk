# Purchaseorder

## Overview

### Available Operations

* [create_accounting_purchaseorder](#create_accounting_purchaseorder) - Create a purchaseorder
* [get_accounting_purchaseorder](#get_accounting_purchaseorder) - Retrieve a purchaseorder
* [list_accounting_purchaseorders](#list_accounting_purchaseorders) - List all purchaseorders
* [patch_accounting_purchaseorder](#patch_accounting_purchaseorder) - Update a purchaseorder
* [remove_accounting_purchaseorder](#remove_accounting_purchaseorder) - Remove a purchaseorder
* [update_accounting_purchaseorder](#update_accounting_purchaseorder) - Update a purchaseorder

## create_accounting_purchaseorder

Create a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingPurchaseorder" method="post" path="/accounting/{connection_id}/purchaseorder" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.create_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "billing_address": {
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "e4b77728-8330-459c-9a39-260ab69e315c",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-04-25T20:27:36.971Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-26T04:07:06.164Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateAccountingPurchaseorderRequest](../../models/operations/createaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateAccountingPurchaseorderResponse](../../models/operations/createaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_purchaseorder

Retrieve a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingPurchaseorder" method="get" path="/accounting/{connection_id}/purchaseorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.get_accounting_purchaseorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingPurchaseorderRequest](../../models/operations/getaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetAccountingPurchaseorderResponse](../../models/operations/getaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_purchaseorders

List all purchaseorders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingPurchaseorders" method="get" path="/accounting/{connection_id}/purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.list_accounting_purchaseorders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_purchaseorders is not None

    # Handle response
    print(res.accounting_purchaseorders)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingPurchaseordersRequest](../../models/operations/listaccountingpurchaseordersrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.ListAccountingPurchaseordersResponse](../../models/operations/listaccountingpurchaseordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_purchaseorder

Update a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingPurchaseorder" method="patch" path="/accounting/{connection_id}/purchaseorder/{id}" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.patch_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "billing_address": {
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "607bbb4e-9c94-4a95-ab51-72578207bf03",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-04-25T20:27:37.016Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-26T04:07:06.167Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchAccountingPurchaseorderRequest](../../models/operations/patchaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.PatchAccountingPurchaseorderResponse](../../models/operations/patchaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_purchaseorder

Remove a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingPurchaseorder" method="delete" path="/accounting/{connection_id}/purchaseorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.remove_accounting_purchaseorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.RemoveAccountingPurchaseorderRequest](../../models/operations/removeaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.RemoveAccountingPurchaseorderResponse](../../models/operations/removeaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_purchaseorder

Update a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingPurchaseorder" method="put" path="/accounting/{connection_id}/purchaseorder/{id}" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.purchaseorder.update_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "billing_address": {
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "607bbb4e-9c94-4a95-ab51-72578207bf03",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-04-25T20:27:37.016Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-26T04:07:06.167Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateAccountingPurchaseorderRequest](../../models/operations/updateaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.UpdateAccountingPurchaseorderResponse](../../models/operations/updateaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |