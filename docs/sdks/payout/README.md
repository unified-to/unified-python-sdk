# Payout

## Overview

### Available Operations

* [get_payment_payout2](#get_payment_payout2) - Retrieve a payout
* [list_payment_payouts2](#list_payment_payouts2) - List all payouts

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

    res = unified_to.payout.get_payment_payout2(request={
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

    res = unified_to.payout.list_payment_payouts2(request={
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