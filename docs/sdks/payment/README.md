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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "9988d285-8a8b-492c-b519-91eb97b4434a",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "a0ea8ec7-9586-414e-8a3c-41394c0edce3",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "16391344-6eff-4bf0-a791-c9fdf417d676",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "e1e74115-cbff-4c2d-aec4-f3e177ae4e93",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-13T02:06:57.205Z"),
            "url": "https://pay.example.com/9988d285-8a8b-492c-b519-91eb97b4434a",
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
            "card_brand": "MASTERCARD",
            "card_last4": "1529",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "df7aa2ed-41dc-4e83-a3b5-b1047eff12a1",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Bibo tactus vilicus.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-10-07T01:58:58.488Z"),
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
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "d87cb8a5-1980-45e6-a727-3ef0282bccde",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-04T09:26:11.103Z"),
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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "d37151f8-22a5-4b03-9d6b-b29ebc640e6e",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "9d154a84-75af-428b-8440-8d19f7e695dd",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "bb4a92da-9baf-4a58-8054-17b8512df02a",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "07eb7360-62d2-41b8-b068-73b82783ba9b",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-13T02:06:57.208Z"),
            "url": "https://pay.example.com/d37151f8-22a5-4b03-9d6b-b29ebc640e6e",
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
            "card_brand": "MASTERCARD",
            "card_last4": "1529",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "ebddd02d-1132-4f3d-b4c7-b662761052ea",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Bibo tactus vilicus.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-10-07T01:58:58.503Z"),
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
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "162c5860-54da-4eba-8df1-d1ee49f33de0",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-04T09:26:11.105Z"),
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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "d37151f8-22a5-4b03-9d6b-b29ebc640e6e",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "9d154a84-75af-428b-8440-8d19f7e695dd",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "bb4a92da-9baf-4a58-8054-17b8512df02a",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "07eb7360-62d2-41b8-b068-73b82783ba9b",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-13T02:06:57.208Z"),
            "url": "https://pay.example.com/d37151f8-22a5-4b03-9d6b-b29ebc640e6e",
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
            "card_brand": "MASTERCARD",
            "card_last4": "1529",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "ebddd02d-1132-4f3d-b4c7-b662761052ea",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Bibo tactus vilicus.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-10-07T01:58:58.503Z"),
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
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "162c5860-54da-4eba-8df1-d1ee49f33de0",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-04T09:26:11.105Z"),
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