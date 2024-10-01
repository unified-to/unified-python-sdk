# Payout
(*payout*)

## Overview

### Available Operations

* [get_payment_payout](#get_payment_payout) - Retrieve a payout
* [list_payment_payouts](#list_payment_payouts) - List all payouts

## get_payment_payout

Retrieve a payout

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.payout.get_payment_payout(request=operations.GetPaymentPayoutRequest(
    connection_id='<value>',
    id='<id>',
))

if res.payment_payout is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPaymentPayoutRequest](../../models/operations/getpaymentpayoutrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |

### Response

**[operations.GetPaymentPayoutResponse](../../models/operations/getpaymentpayoutresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_payouts

List all payouts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.payout.list_payment_payouts(request=operations.ListPaymentPayoutsRequest(
    connection_id='<value>',
))

if res.payment_payouts is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPaymentPayoutsRequest](../../models/operations/listpaymentpayoutsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |

### Response

**[operations.ListPaymentPayoutsResponse](../../models/operations/listpaymentpayoutsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |