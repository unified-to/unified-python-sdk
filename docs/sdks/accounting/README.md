# Accounting
(*.accounting*)

### Available Operations

* [create_accounting_customer](#create_accounting_customer) - Create a customer
* [create_accounting_invoice](#create_accounting_invoice) - Create a invoice
* [create_accounting_payment](#create_accounting_payment) - Create a payment
* [get_accounting_customer](#get_accounting_customer) - Retrieve a customer
* [get_accounting_invoice](#get_accounting_invoice) - Retrieve a invoice
* [get_accounting_payment](#get_accounting_payment) - Retrieve a payment
* [list_accounting_customers](#list_accounting_customers) - List all customers
* [list_accounting_invoices](#list_accounting_invoices) - List all invoices
* [list_accounting_payments](#list_accounting_payments) - List all payments
* [patch_accounting_customer](#patch_accounting_customer) - Update a customer
* [patch_accounting_invoice](#patch_accounting_invoice) - Update a invoice
* [patch_accounting_payment](#patch_accounting_payment) - Update a payment
* [remove_accounting_customer](#remove_accounting_customer) - Remove a customer
* [remove_accounting_invoice](#remove_accounting_invoice) - Remove a invoice
* [remove_accounting_payment](#remove_accounting_payment) - Remove a payment
* [update_accounting_customer](#update_accounting_customer) - Update a customer
* [update_accounting_invoice](#update_accounting_invoice) - Update a invoice
* [update_accounting_payment](#update_accounting_payment) - Update a payment

## create_accounting_customer

Create a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateAccountingCustomerRequest(
    accounting_customer=shared.AccountingCustomer(
        billing_address=shared.PropertyAccountingCustomerBillingAddress(),
        emails=[
            shared.AccountingEmail(
                email='Kevon_Schultz42@gmail.com',
            ),
        ],
        raw=shared.PropertyAccountingCustomerRaw(),
        shipping_address=shared.PropertyAccountingCustomerShippingAddress(),
        telephones=[
            shared.AccountingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_customer(req)

if res.accounting_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingCustomerRequest](../../models/operations/createaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CreateAccountingCustomerResponse](../../models/operations/createaccountingcustomerresponse.md)**


## create_accounting_invoice

Create a invoice

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateAccountingInvoiceRequest(
    accounting_invoice=shared.AccountingInvoice(
        lineitems=[
            shared.AccountingLineitem(
                total_amount=6736.06,
            ),
        ],
        raw=shared.PropertyAccountingInvoiceRaw(),
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_invoice(req)

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**


## create_accounting_payment

Create a payment

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        invoice_ids=[
            'string',
        ],
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_payment(req)

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


## get_accounting_customer

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAccountingCustomerRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.accounting.get_accounting_customer(req)

if res.accounting_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingCustomerRequest](../../models/operations/getaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAccountingCustomerResponse](../../models/operations/getaccountingcustomerresponse.md)**


## get_accounting_invoice

Retrieve a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAccountingInvoiceRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.accounting.get_accounting_invoice(req)

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingInvoiceRequest](../../models/operations/getaccountinginvoicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetAccountingInvoiceResponse](../../models/operations/getaccountinginvoiceresponse.md)**


## get_accounting_payment

Retrieve a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAccountingPaymentRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.accounting.get_accounting_payment(req)

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


## list_accounting_customers

List all customers

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListAccountingCustomersRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.accounting.list_accounting_customers(req)

if res.accounting_customers is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingCustomersRequest](../../models/operations/listaccountingcustomersrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListAccountingCustomersResponse](../../models/operations/listaccountingcustomersresponse.md)**


## list_accounting_invoices

List all invoices

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListAccountingInvoicesRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.accounting.list_accounting_invoices(req)

if res.accounting_invoices is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingInvoicesRequest](../../models/operations/listaccountinginvoicesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListAccountingInvoicesResponse](../../models/operations/listaccountinginvoicesresponse.md)**


## list_accounting_payments

List all payments

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListAccountingPaymentsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.accounting.list_accounting_payments(req)

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


## patch_accounting_customer

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchAccountingCustomerRequest(
    accounting_customer=shared.AccountingCustomer(
        billing_address=shared.PropertyAccountingCustomerBillingAddress(),
        emails=[
            shared.AccountingEmail(
                email='Trever_Orn@hotmail.com',
            ),
        ],
        raw=shared.PropertyAccountingCustomerRaw(),
        shipping_address=shared.PropertyAccountingCustomerShippingAddress(),
        telephones=[
            shared.AccountingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.patch_accounting_customer(req)

if res.accounting_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingCustomerRequest](../../models/operations/patchaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PatchAccountingCustomerResponse](../../models/operations/patchaccountingcustomerresponse.md)**


## patch_accounting_invoice

Update a invoice

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchAccountingInvoiceRequest(
    accounting_invoice=shared.AccountingInvoice(
        lineitems=[
            shared.AccountingLineitem(
                total_amount=7374.1,
            ),
        ],
        raw=shared.PropertyAccountingInvoiceRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.patch_accounting_invoice(req)

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingInvoiceRequest](../../models/operations/patchaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchAccountingInvoiceResponse](../../models/operations/patchaccountinginvoiceresponse.md)**


## patch_accounting_payment

Update a payment

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        invoice_ids=[
            'string',
        ],
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.patch_accounting_payment(req)

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


## remove_accounting_customer

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAccountingCustomerRequest(
    connection_id='string',
    id='<ID>',
)

res = s.accounting.remove_accounting_customer(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingCustomerRequest](../../models/operations/removeaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RemoveAccountingCustomerResponse](../../models/operations/removeaccountingcustomerresponse.md)**


## remove_accounting_invoice

Remove a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAccountingInvoiceRequest(
    connection_id='string',
    id='<ID>',
)

res = s.accounting.remove_accounting_invoice(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingInvoiceRequest](../../models/operations/removeaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveAccountingInvoiceResponse](../../models/operations/removeaccountinginvoiceresponse.md)**


## remove_accounting_payment

Remove a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveAccountingPaymentRequest(
    connection_id='string',
    id='<ID>',
)

res = s.accounting.remove_accounting_payment(req)

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


## update_accounting_customer

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.UpdateAccountingCustomerRequest(
    accounting_customer=shared.AccountingCustomer(
        billing_address=shared.PropertyAccountingCustomerBillingAddress(),
        emails=[
            shared.AccountingEmail(
                email='Myrtice_Jacobi77@hotmail.com',
            ),
        ],
        raw=shared.PropertyAccountingCustomerRaw(),
        shipping_address=shared.PropertyAccountingCustomerShippingAddress(),
        telephones=[
            shared.AccountingTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.update_accounting_customer(req)

if res.accounting_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingCustomerRequest](../../models/operations/updateaccountingcustomerrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.UpdateAccountingCustomerResponse](../../models/operations/updateaccountingcustomerresponse.md)**


## update_accounting_invoice

Update a invoice

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.UpdateAccountingInvoiceRequest(
    accounting_invoice=shared.AccountingInvoice(
        lineitems=[
            shared.AccountingLineitem(
                total_amount=6974.28,
            ),
        ],
        raw=shared.PropertyAccountingInvoiceRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.update_accounting_invoice(req)

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingInvoiceRequest](../../models/operations/updateaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateAccountingInvoiceResponse](../../models/operations/updateaccountinginvoiceresponse.md)**


## update_accounting_payment

Update a payment

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.UpdateAccountingPaymentRequest(
    accounting_payment=shared.AccountingPayment(
        invoice_ids=[
            'string',
        ],
        raw=shared.PropertyAccountingPaymentRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.update_accounting_payment(req)

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

