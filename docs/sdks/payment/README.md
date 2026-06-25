# Payment

## Overview

### Available Operations

* [create_payment_link2](#create_payment_link2) - Create a link
* [create_payment_payment2](#create_payment_payment2) - Create a payment
* [create_payment_subscription2](#create_payment_subscription2) - Create a subscription
* [get_payment_link2](#get_payment_link2) - Retrieve a link
* [get_payment_payment2](#get_payment_payment2) - Retrieve a payment
* [get_payment_payout2](#get_payment_payout2) - Retrieve a payout
* [get_payment_refund2](#get_payment_refund2) - Retrieve a refund
* [get_payment_subscription2](#get_payment_subscription2) - Retrieve a subscription
* [list_payment_links2](#list_payment_links2) - List all links
* [list_payment_payments2](#list_payment_payments2) - List all payments
* [list_payment_payouts2](#list_payment_payouts2) - List all payouts
* [list_payment_refunds2](#list_payment_refunds2) - List all refunds
* [list_payment_subscriptions2](#list_payment_subscriptions2) - List all subscriptions
* [patch_payment_link2](#patch_payment_link2) - Update a link
* [patch_payment_payment2](#patch_payment_payment2) - Update a payment
* [patch_payment_subscription2](#patch_payment_subscription2) - Update a subscription
* [remove_payment_link2](#remove_payment_link2) - Remove a link
* [remove_payment_payment2](#remove_payment_payment2) - Remove a payment
* [remove_payment_subscription2](#remove_payment_subscription2) - Remove a subscription
* [update_payment_link2](#update_payment_link2) - Update a link
* [update_payment_payment2](#update_payment_payment2) - Update a payment
* [update_payment_subscription2](#update_payment_subscription2) - Update a subscription

## create_payment_link2

Create a link

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentLink2" method="post" path="/payment/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.create_payment_link2(request={
        "payment_link": {},
        "connection_id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreatePaymentLink2Request](../../models/operations/createpaymentlink2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreatePaymentLink2Response](../../models/operations/createpaymentlink2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_payment_payment2

Create a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentPayment2" method="post" path="/payment/{connection_id}/payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.create_payment_payment2(request={
        "payment_payment": {},
        "connection_id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePaymentPayment2Request](../../models/operations/createpaymentpayment2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreatePaymentPayment2Response](../../models/operations/createpaymentpayment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.payment.create_payment_subscription2(request={
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

## get_payment_link2

Retrieve a link

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentLink2" method="get" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_link2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPaymentLink2Request](../../models/operations/getpaymentlink2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetPaymentLink2Response](../../models/operations/getpaymentlink2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_payment2

Retrieve a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentPayment2" method="get" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_payment2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetPaymentPayment2Request](../../models/operations/getpaymentpayment2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetPaymentPayment2Response](../../models/operations/getpaymentpayment2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_payout2

Retrieve a payout

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentPayout2" method="get" path="/payment/{connection_id}/payout/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_payout2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payout is not None

    # Handle response
    print(res.payment_payout)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPaymentPayout2Request](../../models/operations/getpaymentpayout2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetPaymentPayout2Response](../../models/operations/getpaymentpayout2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_refund2

Retrieve a refund

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentRefund2" method="get" path="/payment/{connection_id}/refund/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.get_payment_refund2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_refund is not None

    # Handle response
    print(res.payment_refund)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPaymentRefund2Request](../../models/operations/getpaymentrefund2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetPaymentRefund2Response](../../models/operations/getpaymentrefund2response.md)**

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

    res = unified_to.payment.get_payment_subscription2(request={
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

## list_payment_links2

List all links

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentLinks2" method="get" path="/payment/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_links2(request={
        "connection_id": "<id>",
    })

    assert res.payment_links is not None

    # Handle response
    print(res.payment_links)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPaymentLinks2Request](../../models/operations/listpaymentlinks2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListPaymentLinks2Response](../../models/operations/listpaymentlinks2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_payments2

List all payments

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentPayments2" method="get" path="/payment/{connection_id}/payment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_payments2(request={
        "connection_id": "<id>",
    })

    assert res.payment_payments is not None

    # Handle response
    print(res.payment_payments)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListPaymentPayments2Request](../../models/operations/listpaymentpayments2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListPaymentPayments2Response](../../models/operations/listpaymentpayments2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_payouts2

List all payouts

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentPayouts2" method="get" path="/payment/{connection_id}/payout" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_payouts2(request={
        "connection_id": "<id>",
    })

    assert res.payment_payouts is not None

    # Handle response
    print(res.payment_payouts)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListPaymentPayouts2Request](../../models/operations/listpaymentpayouts2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListPaymentPayouts2Response](../../models/operations/listpaymentpayouts2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_refunds2

List all refunds

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentRefunds2" method="get" path="/payment/{connection_id}/refund" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.list_payment_refunds2(request={
        "connection_id": "<id>",
    })

    assert res.payment_refunds is not None

    # Handle response
    print(res.payment_refunds)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListPaymentRefunds2Request](../../models/operations/listpaymentrefunds2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListPaymentRefunds2Response](../../models/operations/listpaymentrefunds2response.md)**

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

    res = unified_to.payment.list_payment_subscriptions2(request={
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

## patch_payment_link2

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentLink2" method="patch" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.patch_payment_link2(request={
        "payment_link": {},
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
| `request`                                                                                  | [operations.PatchPaymentLink2Request](../../models/operations/patchpaymentlink2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchPaymentLink2Response](../../models/operations/patchpaymentlink2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_payment2

Update a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentPayment2" method="patch" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.patch_payment_payment2(request={
        "payment_payment": {},
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
| `request`                                                                                        | [operations.PatchPaymentPayment2Request](../../models/operations/patchpaymentpayment2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchPaymentPayment2Response](../../models/operations/patchpaymentpayment2response.md)**

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

    res = unified_to.payment.patch_payment_subscription2(request={
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

## remove_payment_link2

Remove a link

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentLink2" method="delete" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.remove_payment_link2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemovePaymentLink2Request](../../models/operations/removepaymentlink2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemovePaymentLink2Response](../../models/operations/removepaymentlink2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_payment2

Remove a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentPayment2" method="delete" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.remove_payment_payment2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemovePaymentPayment2Request](../../models/operations/removepaymentpayment2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemovePaymentPayment2Response](../../models/operations/removepaymentpayment2response.md)**

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

    res = unified_to.payment.remove_payment_subscription2(request={
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

## update_payment_link2

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentLink2" method="put" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.update_payment_link2(request={
        "payment_link": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdatePaymentLink2Request](../../models/operations/updatepaymentlink2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdatePaymentLink2Response](../../models/operations/updatepaymentlink2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_payment2

Update a payment

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentPayment2" method="put" path="/payment/{connection_id}/payment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payment.update_payment_payment2(request={
        "payment_payment": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_payment is not None

    # Handle response
    print(res.payment_payment)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePaymentPayment2Request](../../models/operations/updatepaymentpayment2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdatePaymentPayment2Response](../../models/operations/updatepaymentpayment2response.md)**

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

    res = unified_to.payment.update_payment_subscription2(request={
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