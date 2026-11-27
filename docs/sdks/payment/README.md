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

Creates a PaymentLink. Provide the unified PaymentLink fields in the request body; they are mapped to the provider's API. Returns the created PaymentLink.

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
            "contact_email": "Clovis8@yahoo.com",
            "contact_name": "Lilliana Dibbert",
            "contact_phone": "963-764-0961",
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "The Daron Sausages is the latest in a series of informal products from Dach, Beatty and Moen",
            "id": "b9ca3dc1-8725-47db-b2bf-a06e0b684d0d",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "fda1a52c-a3c3-4e8c-af70-05808c1a84dc",
                    "item_description": "Introducing the Syrian Arab Republic-inspired Chips, blending neat style with local craftsmanship",
                    "item_name": "Electronic Metal Tuna",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "34df5f21-349e-45bc-8e6d-71ec18955e65",
                    "item_description": "Soft Computer designed with Bronze for junior performance",
                    "item_name": "Rustic Concrete Shoes",
                    "notes": "Doloremque appositus cito cursim bellicus rerum ubi voluptatibus.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "dbba01ea-6fa8-4a9c-8738-aff0f5a9fcb2",
                    "item_description": "The Donnie Shirt is the latest in a series of tinted products from Nitzsche and Sons",
                    "item_name": "Intelligent Marble Keyboard",
                    "notes": "Damnatio aut bene.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://finished-retention.com",
            "updated_at": parse_datetime("2024-04-22T19:25:17.836Z"),
            "url": "https://pay.example.com/b9ca3dc1-8725-47db-b2bf-a06e0b684d0d",
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

Creates a PaymentPayment. Provide the unified PaymentPayment fields in the request body; they are mapped to the provider's API. Returns the created PaymentPayment.

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
            "card_last4": "8048",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "6c759574-3596-4b66-857a-b33070596e34",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Auctus patruus causa vulnus decet thymum curvo eligendi.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-11-05T18:07:26.757Z"),
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

Creates a PaymentSubscription. Provide the unified PaymentSubscription fields in the request body; they are mapped to the provider's API. Returns the created PaymentSubscription.

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
            "description": "New Bike model with 94 GB RAM, 813 GB storage, and narrow features",
            "id": "4c410c34-fce2-41dd-8b25-61463be1e4db",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-08T21:55:53.637Z"),
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

Retrieves a single PaymentLink by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PaymentPayment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PaymentPayout by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PaymentRefund by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PaymentSubscription by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of PaymentLinks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PaymentPayments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PaymentPayouts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PaymentRefunds. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PaymentSubscriptions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the PaymentLink identified by `id`. Provide the unified PaymentLink fields to change in the request body.

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
            "contact_email": "Clovis8@yahoo.com",
            "contact_name": "Lilliana Dibbert",
            "contact_phone": "963-764-0961",
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "The Daron Sausages is the latest in a series of informal products from Dach, Beatty and Moen",
            "id": "5d33b3dc-d3a7-4735-a393-445e5ec3526b",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "ebcb66d1-043e-46e2-b17b-adac8ee28e85",
                    "item_description": "Introducing the Syrian Arab Republic-inspired Chips, blending neat style with local craftsmanship",
                    "item_name": "Electronic Metal Tuna",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "b9049468-b0db-42b7-8a26-70e91b5ad671",
                    "item_description": "Soft Computer designed with Bronze for junior performance",
                    "item_name": "Rustic Concrete Shoes",
                    "notes": "Doloremque appositus cito cursim bellicus rerum ubi voluptatibus.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "4ba16d5a-8610-4421-b3c1-a3f55eefb883",
                    "item_description": "The Donnie Shirt is the latest in a series of tinted products from Nitzsche and Sons",
                    "item_name": "Intelligent Marble Keyboard",
                    "notes": "Damnatio aut bene.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://finished-retention.com",
            "updated_at": parse_datetime("2024-04-22T19:25:17.840Z"),
            "url": "https://pay.example.com/5d33b3dc-d3a7-4735-a393-445e5ec3526b",
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

Updates the PaymentPayment identified by `id`. Provide the unified PaymentPayment fields to change in the request body.

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
            "card_last4": "8048",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "db8ceb59-2062-4fbb-8e26-658fc393f337",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Auctus patruus causa vulnus decet thymum curvo eligendi.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-11-05T18:07:26.775Z"),
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

Updates the PaymentSubscription identified by `id`. Provide the unified PaymentSubscription fields to change in the request body.

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
            "description": "New Bike model with 94 GB RAM, 813 GB storage, and narrow features",
            "id": "4c65d692-9057-4f66-b009-4ff37b97ba83",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-08T21:55:53.640Z"),
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

Deletes the PaymentLink identified by `id`.

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

Deletes the PaymentPayment identified by `id`.

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

Deletes the PaymentSubscription identified by `id`.

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

Updates the PaymentLink identified by `id`. Provide the unified PaymentLink fields to change in the request body.

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
            "contact_email": "Clovis8@yahoo.com",
            "contact_name": "Lilliana Dibbert",
            "contact_phone": "963-764-0961",
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "The Daron Sausages is the latest in a series of informal products from Dach, Beatty and Moen",
            "id": "5d33b3dc-d3a7-4735-a393-445e5ec3526b",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "ebcb66d1-043e-46e2-b17b-adac8ee28e85",
                    "item_description": "Introducing the Syrian Arab Republic-inspired Chips, blending neat style with local craftsmanship",
                    "item_name": "Electronic Metal Tuna",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "b9049468-b0db-42b7-8a26-70e91b5ad671",
                    "item_description": "Soft Computer designed with Bronze for junior performance",
                    "item_name": "Rustic Concrete Shoes",
                    "notes": "Doloremque appositus cito cursim bellicus rerum ubi voluptatibus.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "4ba16d5a-8610-4421-b3c1-a3f55eefb883",
                    "item_description": "The Donnie Shirt is the latest in a series of tinted products from Nitzsche and Sons",
                    "item_name": "Intelligent Marble Keyboard",
                    "notes": "Damnatio aut bene.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://finished-retention.com",
            "updated_at": parse_datetime("2024-04-22T19:25:17.840Z"),
            "url": "https://pay.example.com/5d33b3dc-d3a7-4735-a393-445e5ec3526b",
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

Updates the PaymentPayment identified by `id`. Provide the unified PaymentPayment fields to change in the request body.

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
            "card_last4": "8048",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "currency": "EUR",
            "fee_amount": 2055.82,
            "id": "db8ceb59-2062-4fbb-8e26-658fc393f337",
            "metadata": [],
            "net_amount": 68824.18,
            "notes": "Auctus patruus causa vulnus decet thymum curvo eligendi.",
            "paid_at": parse_datetime("2022-03-10T00:19:42.086Z"),
            "payment_method": "CASH",
            "reference": "PMT-119080",
            "status": shared.PaymentPaymentStatus.SUCCEEDED,
            "tender_type": shared.TenderType.CASH,
            "tip_amount": 0.0,
            "total_amount": 70880.0,
            "type": shared.PaymentPaymentType.INVOICE,
            "updated_at": parse_datetime("2025-11-05T18:07:26.775Z"),
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

Updates the PaymentSubscription identified by `id`. Provide the unified PaymentSubscription fields to change in the request body.

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
            "description": "New Bike model with 94 GB RAM, 813 GB storage, and narrow features",
            "id": "4c65d692-9057-4f66-b009-4ff37b97ba83",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-08T21:55:53.640Z"),
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