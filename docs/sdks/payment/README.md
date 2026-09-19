# Payment

## Overview

### Available Operations

* [create_payment_link](#create_payment_link) - Create a link
* [create_payment_payment](#create_payment_payment) - Create a payment
* [create_payment_subscription](#create_payment_subscription) - Create a subscription
* [get_payment_link](#get_payment_link) - Retrieve a link
* [get_payment_payment](#get_payment_payment) - Retrieve a payment
* [get_payment_payout](#get_payment_payout) - Retrieve a payout
* [get_payment_refund](#get_payment_refund) - Retrieve a refund
* [get_payment_subscription](#get_payment_subscription) - Retrieve a subscription
* [list_payment_links](#list_payment_links) - List all links
* [list_payment_payments](#list_payment_payments) - List all payments
* [list_payment_payouts](#list_payment_payouts) - List all payouts
* [list_payment_refunds](#list_payment_refunds) - List all refunds
* [list_payment_subscriptions](#list_payment_subscriptions) - List all subscriptions
* [patch_payment_link](#patch_payment_link) - Update a link
* [patch_payment_payment](#patch_payment_payment) - Update a payment
* [patch_payment_subscription](#patch_payment_subscription) - Update a subscription
* [remove_payment_link](#remove_payment_link) - Remove a link
* [remove_payment_payment](#remove_payment_payment) - Remove a payment
* [remove_payment_subscription](#remove_payment_subscription) - Remove a subscription
* [update_payment_link](#update_payment_link) - Update a link
* [update_payment_payment](#update_payment_payment) - Update a payment
* [update_payment_subscription](#update_payment_subscription) - Update a subscription

## create_payment_link

Create a link

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentLink" method="post" path="/payment/{connection_id}/link" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.create_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "a8f5322d-eaac-4317-8c71-09d28989af2e",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "5a041525-0801-434a-879a-d2fb8293a705",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "a653c1ab-4dc1-484c-8063-1a8c8d4201eb",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "f014f633-30c0-4ead-9a12-257a38e4f149",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "e705d74b-e8cb-44fc-9a28-3f95c3dfe1dc",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "b2d01b6a-0634-4b5e-9bea-b5178de33322",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T12:09:34.258Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePaymentLinkRequest](../../models/operations/createpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreatePaymentLinkResponse](../../models/operations/createpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_payment_payment

Create a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentPayment" method="post" path="/payment/{connection_id}/payment" example="payment_payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.create_payment_payment(request={
        "payment_payment": {
            "allocations": [],
            "card_brand": "AMEX",
            "card_last4": "0819",
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "BIF",
            "fee_amount": 3.0,
            "id": "33f66de0-db4c-4251-b842-4c8b581a4e46",
            "location_id": "94f7c68e-07de-40d1-9d6f-a0896363913f",
            "notes": "Tactus vilicus.",
            "payment_method": "BANK_TRANSFER",
            "reference": "auctus",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CHECK,
            "tip_amount": 2.0,
            "total_amount": 44219.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-05-25T07:01:25.989Z"),
        },
        "connection_id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreatePaymentPaymentRequest](../../models/operations/createpaymentpaymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreatePaymentPaymentResponse](../../models/operations/createpaymentpaymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_payment_subscription

Create a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentSubscription" method="post" path="/payment/{connection_id}/subscription" example="payment_subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.create_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "257b14c7-1585-4b05-9087-4a9ed8815b97",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T02:35:12.652Z"),
        },
        "connection_id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreatePaymentSubscriptionRequest](../../models/operations/createpaymentsubscriptionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreatePaymentSubscriptionResponse](../../models/operations/createpaymentsubscriptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_link

Retrieve a link

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentLink" method="get" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPaymentLinkRequest](../../models/operations/getpaymentlinkrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetPaymentLinkResponse](../../models/operations/getpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_payment

Retrieve a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentPayment" method="get" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_payment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPaymentPaymentRequest](../../models/operations/getpaymentpaymentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetPaymentPaymentResponse](../../models/operations/getpaymentpaymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_payout

Retrieve a payout

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentPayout" method="get" path="/payment/{connection_id}/payout/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_payout(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payout is not None

    # Handle response
    print(res.payment_payout)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPaymentPayoutRequest](../../models/operations/getpaymentpayoutrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetPaymentPayoutResponse](../../models/operations/getpaymentpayoutresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_refund

Retrieve a refund

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentRefund" method="get" path="/payment/{connection_id}/refund/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_refund(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_refund is not None

    # Handle response
    print(res.payment_refund)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPaymentRefundRequest](../../models/operations/getpaymentrefundrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetPaymentRefundResponse](../../models/operations/getpaymentrefundresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_subscription

Retrieve a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentSubscription" method="get" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_subscription(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetPaymentSubscriptionRequest](../../models/operations/getpaymentsubscriptionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetPaymentSubscriptionResponse](../../models/operations/getpaymentsubscriptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_links

List all links

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentLinks" method="get" path="/payment/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_links(request={
        "connection_id": "<id>",
    })

    assert res.payment_links is not None

    # Handle response
    print(res.payment_links)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListPaymentLinksRequest](../../models/operations/listpaymentlinksrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListPaymentLinksResponse](../../models/operations/listpaymentlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_payments

List all payments

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentPayments" method="get" path="/payment/{connection_id}/payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_payments(request={
        "connection_id": "<id>",
    })

    assert res.payment_payments is not None

    # Handle response
    print(res.payment_payments)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListPaymentPaymentsRequest](../../models/operations/listpaymentpaymentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListPaymentPaymentsResponse](../../models/operations/listpaymentpaymentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_payouts

List all payouts

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentPayouts" method="get" path="/payment/{connection_id}/payout" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_payouts(request={
        "connection_id": "<id>",
    })

    assert res.payment_payouts is not None

    # Handle response
    print(res.payment_payouts)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPaymentPayoutsRequest](../../models/operations/listpaymentpayoutsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListPaymentPayoutsResponse](../../models/operations/listpaymentpayoutsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_refunds

List all refunds

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentRefunds" method="get" path="/payment/{connection_id}/refund" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_refunds(request={
        "connection_id": "<id>",
    })

    assert res.payment_refunds is not None

    # Handle response
    print(res.payment_refunds)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPaymentRefundsRequest](../../models/operations/listpaymentrefundsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListPaymentRefundsResponse](../../models/operations/listpaymentrefundsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_subscriptions

List all subscriptions

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentSubscriptions" method="get" path="/payment/{connection_id}/subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_subscriptions(request={
        "connection_id": "<id>",
    })

    assert res.payment_subscriptions is not None

    # Handle response
    print(res.payment_subscriptions)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListPaymentSubscriptionsRequest](../../models/operations/listpaymentsubscriptionsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListPaymentSubscriptionsResponse](../../models/operations/listpaymentsubscriptionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentLink" method="patch" path="/payment/{connection_id}/link/{id}" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.patch_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "572d6790-70ac-41ca-b4d2-8dee83ac6303",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "8faeb0e8-f090-442b-9a1c-b551290d2207",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "a900ad8b-784e-447b-a6bd-3673245f0494",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "859b6741-bdce-475c-8855-e64444bf7017",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "186bf115-1506-4902-9da2-3dfd31015db1",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "bec30fae-971d-4a64-9599-f28801bcf427",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T12:09:34.274Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchPaymentLinkRequest](../../models/operations/patchpaymentlinkrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchPaymentLinkResponse](../../models/operations/patchpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_payment

Update a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentPayment" method="patch" path="/payment/{connection_id}/payment/{id}" example="payment_payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.patch_payment_payment(request={
        "payment_payment": {
            "allocations": [],
            "card_brand": "AMEX",
            "card_last4": "0819",
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "BIF",
            "fee_amount": 3.0,
            "id": "4567e0e8-5d04-4eba-8bc1-cdc86b9a053e",
            "location_id": "94f7c68e-07de-40d1-9d6f-a0896363913f",
            "notes": "Tactus vilicus.",
            "payment_method": "BANK_TRANSFER",
            "reference": "auctus",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CHECK,
            "tip_amount": 2.0,
            "total_amount": 44219.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-05-25T07:01:26.007Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchPaymentPaymentRequest](../../models/operations/patchpaymentpaymentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchPaymentPaymentResponse](../../models/operations/patchpaymentpaymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_subscription

Update a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentSubscription" method="patch" path="/payment/{connection_id}/subscription/{id}" example="payment_subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.patch_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "6056e89c-e4ea-431e-8e84-440bf932f86c",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T02:35:12.657Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchPaymentSubscriptionRequest](../../models/operations/patchpaymentsubscriptionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PatchPaymentSubscriptionResponse](../../models/operations/patchpaymentsubscriptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_link

Remove a link

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentLink" method="delete" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.remove_payment_link(request={
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
| `request`                                                                                  | [operations.RemovePaymentLinkRequest](../../models/operations/removepaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemovePaymentLinkResponse](../../models/operations/removepaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_payment

Remove a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentPayment" method="delete" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.remove_payment_payment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemovePaymentPaymentRequest](../../models/operations/removepaymentpaymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemovePaymentPaymentResponse](../../models/operations/removepaymentpaymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_subscription

Remove a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentSubscription" method="delete" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.remove_payment_subscription(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemovePaymentSubscriptionRequest](../../models/operations/removepaymentsubscriptionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.RemovePaymentSubscriptionResponse](../../models/operations/removepaymentsubscriptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentLink" method="put" path="/payment/{connection_id}/link/{id}" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.update_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "572d6790-70ac-41ca-b4d2-8dee83ac6303",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "8faeb0e8-f090-442b-9a1c-b551290d2207",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "a900ad8b-784e-447b-a6bd-3673245f0494",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "859b6741-bdce-475c-8855-e64444bf7017",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "186bf115-1506-4902-9da2-3dfd31015db1",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "bec30fae-971d-4a64-9599-f28801bcf427",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T12:09:34.274Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdatePaymentLinkRequest](../../models/operations/updatepaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdatePaymentLinkResponse](../../models/operations/updatepaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_payment

Update a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentPayment" method="put" path="/payment/{connection_id}/payment/{id}" example="payment_payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.update_payment_payment(request={
        "payment_payment": {
            "allocations": [],
            "card_brand": "AMEX",
            "card_last4": "0819",
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "BIF",
            "fee_amount": 3.0,
            "id": "4567e0e8-5d04-4eba-8bc1-cdc86b9a053e",
            "location_id": "94f7c68e-07de-40d1-9d6f-a0896363913f",
            "notes": "Tactus vilicus.",
            "payment_method": "BANK_TRANSFER",
            "reference": "auctus",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CHECK,
            "tip_amount": 2.0,
            "total_amount": 44219.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-05-25T07:01:26.007Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdatePaymentPaymentRequest](../../models/operations/updatepaymentpaymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdatePaymentPaymentResponse](../../models/operations/updatepaymentpaymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_subscription

Update a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentSubscription" method="put" path="/payment/{connection_id}/subscription/{id}" example="payment_subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.update_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "6056e89c-e4ea-431e-8e84-440bf932f86c",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T02:35:12.657Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdatePaymentSubscriptionRequest](../../models/operations/updatepaymentsubscriptionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdatePaymentSubscriptionResponse](../../models/operations/updatepaymentsubscriptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |