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

    res = unified_to.subscription.create_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "c8ba9aa2-99bc-4fad-b552-e40187ecfd6d",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T04:14:48.596Z"),
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

    res = unified_to.subscription.patch_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "5ca4bf16-3050-4007-b334-35743853164b",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T04:14:48.599Z"),
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

    res = unified_to.subscription.update_payment_subscription(request={
        "payment_subscription": {
            "created_at": parse_datetime("2023-05-08T10:11:03.414Z"),
            "currency": "WST",
            "current_period_end_at": parse_datetime("2023-06-03T04:20:29.157Z"),
            "current_period_start_at": parse_datetime("2023-05-21T03:55:58.846Z"),
            "day_of_month": 1.0,
            "description": "Innovative Mouse featuring important technology and Bamboo construction",
            "end_at": parse_datetime("2023-05-21T12:36:09.234Z"),
            "id": "5ca4bf16-3050-4007-b334-35743853164b",
            "interval": 1.0,
            "interval_unit": shared.IntervalUnit.MONTH,
            "lineitems": [],
            "start_at": parse_datetime("2023-05-29T06:04:51.030Z"),
            "status": shared.PaymentSubscriptionStatus.ACTIVE,
            "total_amount": 75616.0,
            "updated_at": parse_datetime("2023-12-16T04:14:48.599Z"),
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