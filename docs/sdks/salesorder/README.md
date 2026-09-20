# Salesorder

## Overview

### Available Operations

* [create_accounting_salesorder](#create_accounting_salesorder) - Create a salesorder
* [get_accounting_salesorder](#get_accounting_salesorder) - Retrieve a salesorder
* [list_accounting_salesorders](#list_accounting_salesorders) - List all salesorders
* [patch_accounting_salesorder](#patch_accounting_salesorder) - Update a salesorder
* [remove_accounting_salesorder](#remove_accounting_salesorder) - Remove a salesorder
* [update_accounting_salesorder](#update_accounting_salesorder) - Update a salesorder

## create_accounting_salesorder

Create a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingSalesorder" method="post" path="/accounting/{connection_id}/salesorder" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.create_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-08-17T08:27:51.628Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "2bf17771-4216-47dd-8874-501dd599bcd4",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-01-12T05:07:19.769Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-10T19:15:56.399Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingSalesorderRequest](../../models/operations/createaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateAccountingSalesorderResponse](../../models/operations/createaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_salesorder

Retrieve a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingSalesorder" method="get" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.get_accounting_salesorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingSalesorderRequest](../../models/operations/getaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingSalesorderResponse](../../models/operations/getaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_salesorders

List all salesorders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingSalesorders" method="get" path="/accounting/{connection_id}/salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.list_accounting_salesorders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_salesorders is not None

    # Handle response
    print(res.accounting_salesorders)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListAccountingSalesordersRequest](../../models/operations/listaccountingsalesordersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListAccountingSalesordersResponse](../../models/operations/listaccountingsalesordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_salesorder

Update a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingSalesorder" method="patch" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.patch_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-08-17T08:27:51.642Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "1e14878f-9d6c-4963-a124-d4426a301545",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-01-12T05:07:19.804Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-10T19:15:56.399Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAccountingSalesorderRequest](../../models/operations/patchaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchAccountingSalesorderResponse](../../models/operations/patchaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_salesorder

Remove a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingSalesorder" method="delete" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.remove_accounting_salesorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.RemoveAccountingSalesorderRequest](../../models/operations/removeaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveAccountingSalesorderResponse](../../models/operations/removeaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_salesorder

Update a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingSalesorder" method="put" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.update_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-08-17T08:27:51.642Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "1e14878f-9d6c-4963-a124-d4426a301545",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-01-12T05:07:19.804Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-10T19:15:56.399Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateAccountingSalesorderRequest](../../models/operations/updateaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateAccountingSalesorderResponse](../../models/operations/updateaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |