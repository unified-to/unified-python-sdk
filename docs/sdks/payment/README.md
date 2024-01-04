# Payment
(*payment*)

### Available Operations

* [create_accounting_payment](#create_accounting_payment) - Create a payment
* [get_accounting_payment](#get_accounting_payment) - Retrieve a payment
* [list_accounting_payments](#list_accounting_payments) - List all payments
* [patch_accounting_payment](#patch_accounting_payment) - Update a payment
* [remove_accounting_payment](#remove_accounting_payment) - Remove a payment
* [update_accounting_payment](#update_accounting_payment) - Update a payment

## create_accounting_payment

Create a payment

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
)

res = s.payment.create_accounting_payment(req)

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingPaymentRequest](../../models/operations/createaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateAccountingPaymentResponse](../../models/operations/createaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_payment

Retrieve a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetAccountingPaymentRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.payment.get_accounting_payment(req)

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingPaymentRequest](../../models/operations/getaccountingpaymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetAccountingPaymentResponse](../../models/operations/getaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_payments

List all payments

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListAccountingPaymentsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.payment.list_accounting_payments(req)

if res.accounting_payments is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingPaymentsRequest](../../models/operations/listaccountingpaymentsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListAccountingPaymentsResponse](../../models/operations/listaccountingpaymentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_payment

Update a payment

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.payment.patch_accounting_payment(req)

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingPaymentRequest](../../models/operations/patchaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchAccountingPaymentResponse](../../models/operations/patchaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_payment

Remove a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveAccountingPaymentRequest(
    connection_id='string',
    id='<ID>',
)

res = s.payment.remove_accounting_payment(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingPaymentRequest](../../models/operations/removeaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveAccountingPaymentResponse](../../models/operations/removeaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_payment

Update a payment

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.payment.update_accounting_payment(req)

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingPaymentRequest](../../models/operations/updateaccountingpaymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateAccountingPaymentResponse](../../models/operations/updateaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
