# Subscription

## Overview

### Available Operations

* [create_payment_subscription2](#create_payment_subscription2) - Create a subscription
* [get_payment_subscription2](#get_payment_subscription2) - Retrieve a subscription
* [list_payment_subscriptions2](#list_payment_subscriptions2) - List all subscriptions
* [patch_payment_subscription2](#patch_payment_subscription2) - Update a subscription
* [remove_payment_subscription2](#remove_payment_subscription2) - Remove a subscription
* [update_payment_subscription2](#update_payment_subscription2) - Update a subscription

## create_payment_subscription2

Create a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentSubscription2" method="post" path="/payment/{connection_id}/subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.create_payment_subscription2(request={
        "payment_subscription": {},
        "connection_id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreatePaymentSubscription2Request](../../models/operations/createpaymentsubscription2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreatePaymentSubscription2Response](../../models/operations/createpaymentsubscription2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_subscription2

Retrieve a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentSubscription2" method="get" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.get_payment_subscription2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetPaymentSubscription2Request](../../models/operations/getpaymentsubscription2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetPaymentSubscription2Response](../../models/operations/getpaymentsubscription2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_subscriptions2

List all subscriptions

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentSubscriptions2" method="get" path="/payment/{connection_id}/subscription" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.list_payment_subscriptions2(request={
        "connection_id": "<id>",
    })

    assert res.payment_subscriptions is not None

    # Handle response
    print(res.payment_subscriptions)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListPaymentSubscriptions2Request](../../models/operations/listpaymentsubscriptions2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListPaymentSubscriptions2Response](../../models/operations/listpaymentsubscriptions2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_subscription2

Update a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentSubscription2" method="patch" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.patch_payment_subscription2(request={
        "payment_subscription": {},
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
| `request`                                                                                                  | [operations.PatchPaymentSubscription2Request](../../models/operations/patchpaymentsubscription2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchPaymentSubscription2Response](../../models/operations/patchpaymentsubscription2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_subscription2

Remove a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentSubscription2" method="delete" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.remove_payment_subscription2(request={
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
| `request`                                                                                                    | [operations.RemovePaymentSubscription2Request](../../models/operations/removepaymentsubscription2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemovePaymentSubscription2Response](../../models/operations/removepaymentsubscription2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_subscription2

Update a subscription

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentSubscription2" method="put" path="/payment/{connection_id}/subscription/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.subscription.update_payment_subscription2(request={
        "payment_subscription": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_subscription is not None

    # Handle response
    print(res.payment_subscription)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdatePaymentSubscription2Request](../../models/operations/updatepaymentsubscription2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdatePaymentSubscription2Response](../../models/operations/updatepaymentsubscription2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |