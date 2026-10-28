# Subscription

## Overview

### Available Operations

* [create_payment_subscription](#create_payment_subscription) - Create a subscription
* [get_payment_subscription](#get_payment_subscription) - Retrieve a subscription
* [list_payment_subscriptions](#list_payment_subscriptions) - List all subscriptions
* [patch_payment_subscription](#patch_payment_subscription) - Update a subscription
* [remove_payment_subscription](#remove_payment_subscription) - Remove a subscription
* [update_payment_subscription](#update_payment_subscription) - Update a subscription

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

    res = unified_to.subscription.create_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "7e99bbc5-5aec-4c2b-bae1-875d5a0f81a5",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-05T08:50:11.773Z"),
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

    res = unified_to.subscription.get_payment_subscription(request={
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

    res = unified_to.subscription.list_payment_subscriptions(request={
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

    res = unified_to.subscription.patch_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "757ed7c9-22a4-4537-9e6e-fb5f6f19f111",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-05T08:50:11.776Z"),
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

    res = unified_to.subscription.remove_payment_subscription(request={
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

    res = unified_to.subscription.update_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "USD",
            "current_period_end_at": parse_datetime("2024-02-08T10:05:22.912Z"),
            "current_period_start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "day_of_month": 8.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "id": "757ed7c9-22a4-4537-9e6e-fb5f6f19f111",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.YEAR,
            "lineitems": [],
            "metadata": [],
            "month": 5.0,
            "start_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-05T08:50:11.776Z"),
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