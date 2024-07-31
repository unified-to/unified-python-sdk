# Refund
(*refund*)

### Available Operations

* [get_payment_refund](#get_payment_refund) - Retrieve a refund
* [list_payment_refunds](#list_payment_refunds) - List all refunds

## get_payment_refund

Retrieve a refund

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.refund.get_payment_refund(request=operations.GetPaymentRefundRequest(
    connection_id='<value>',
    id='<id>',
))

if res.payment_refund is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPaymentRefundRequest](../../models/operations/getpaymentrefundrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetPaymentRefundResponse](../../models/operations/getpaymentrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_payment_refunds

List all refunds

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.refund.list_payment_refunds(request=operations.ListPaymentRefundsRequest(
    connection_id='<value>',
))

if res.payment_refunds is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPaymentRefundsRequest](../../models/operations/listpaymentrefundsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.ListPaymentRefundsResponse](../../models/operations/listpaymentrefundsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
