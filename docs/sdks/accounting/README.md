# Accounting
(*accounting*)

### Available Operations

* [create_accounting_account](#create_accounting_account) - Create an account
* [create_accounting_customer](#create_accounting_customer) - Create a customer
* [create_accounting_invoice](#create_accounting_invoice) - Create a invoice
* [create_accounting_payment](#create_accounting_payment) - Create a payment
* [create_accounting_transaction](#create_accounting_transaction) - Create a transaction
* [get_accounting_account](#get_accounting_account) - Retrieve an account
* [get_accounting_customer](#get_accounting_customer) - Retrieve a customer
* [get_accounting_invoice](#get_accounting_invoice) - Retrieve a invoice
* [get_accounting_payment](#get_accounting_payment) - Retrieve a payment
* [get_accounting_transaction](#get_accounting_transaction) - Retrieve a transaction
* [list_accounting_accounts](#list_accounting_accounts) - List all accounts
* [list_accounting_customers](#list_accounting_customers) - List all customers
* [list_accounting_invoices](#list_accounting_invoices) - List all invoices
* [list_accounting_payments](#list_accounting_payments) - List all payments
* [list_accounting_transactions](#list_accounting_transactions) - List all transactions
* [patch_accounting_account](#patch_accounting_account) - Update an account
* [patch_accounting_customer](#patch_accounting_customer) - Update a customer
* [patch_accounting_invoice](#patch_accounting_invoice) - Update a invoice
* [patch_accounting_payment](#patch_accounting_payment) - Update a payment
* [patch_accounting_transaction](#patch_accounting_transaction) - Update a transaction
* [remove_accounting_account](#remove_accounting_account) - Remove an account
* [remove_accounting_customer](#remove_accounting_customer) - Remove a customer
* [remove_accounting_invoice](#remove_accounting_invoice) - Remove a invoice
* [remove_accounting_payment](#remove_accounting_payment) - Remove a payment
* [remove_accounting_transaction](#remove_accounting_transaction) - Remove a transaction
* [update_accounting_account](#update_accounting_account) - Update an account
* [update_accounting_customer](#update_accounting_customer) - Update a customer
* [update_accounting_invoice](#update_accounting_invoice) - Update a invoice
* [update_accounting_payment](#update_accounting_payment) - Update a payment
* [update_accounting_transaction](#update_accounting_transaction) - Update a transaction

## create_accounting_account

Create an account

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

req = operations.CreateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        name='string',
        raw=shared.PropertyAccountingAccountRaw(),
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingAccountRequest](../../models/operations/createaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateAccountingAccountResponse](../../models/operations/createaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_accounting_customer

Create a customer

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_accounting_invoice

Create a invoice

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_accounting_transaction

Create a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateAccountingTransactionRequest(
    accounting_transaction=shared.AccountingTransaction(
        account_id='string',
        id='<ID>',
        line_items=[
            shared.AccountingTransactionLineitem(
                id='<ID>',
                total_amount=4969.62,
            ),
        ],
        raw=shared.PropertyAccountingTransactionRaw(),
        total_amount=6267.93,
        type=shared.AccountingTransactionType.SPEND,
    ),
    connection_id='string',
)

res = s.accounting.create_accounting_transaction(req)

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAccountingTransactionRequest](../../models/operations/createaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.CreateAccountingTransactionResponse](../../models/operations/createaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_accounting_account

Retrieve an account

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetAccountingAccountRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.accounting.get_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingAccountRequest](../../models/operations/getaccountingaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetAccountingAccountResponse](../../models/operations/getaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_accounting_customer

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_accounting_invoice

Retrieve a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_accounting_transaction

Retrieve a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetAccountingTransactionRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.accounting.get_accounting_transaction(req)

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingTransactionRequest](../../models/operations/getaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetAccountingTransactionResponse](../../models/operations/getaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_accounting_accounts

List all accounts

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

req = operations.ListAccountingAccountsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.accounting.list_accounting_accounts(req)

if res.accounting_accounts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingAccountsRequest](../../models/operations/listaccountingaccountsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListAccountingAccountsResponse](../../models/operations/listaccountingaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_accounting_customers

List all customers

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_accounting_invoices

List all invoices

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_accounting_transactions

List all transactions

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

req = operations.ListAccountingTransactionsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.accounting.list_accounting_transactions(req)

if res.accounting_transactions is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingTransactionsRequest](../../models/operations/listaccountingtransactionsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.ListAccountingTransactionsResponse](../../models/operations/listaccountingtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_accounting_account

Update an account

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

req = operations.PatchAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        name='string',
        raw=shared.PropertyAccountingAccountRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.patch_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingAccountRequest](../../models/operations/patchaccountingaccountrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchAccountingAccountResponse](../../models/operations/patchaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_accounting_customer

Update a customer

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_accounting_invoice

Update a invoice

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchAccountingTransactionRequest(
    accounting_transaction=shared.AccountingTransaction(
        account_id='string',
        id='<ID>',
        line_items=[
            shared.AccountingTransactionLineitem(
                id='<ID>',
                total_amount=5633.69,
            ),
        ],
        raw=shared.PropertyAccountingTransactionRaw(),
        total_amount=4558.63,
        type=shared.AccountingTransactionType.SPEND,
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.patch_accounting_transaction(req)

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAccountingTransactionRequest](../../models/operations/patchaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchAccountingTransactionResponse](../../models/operations/patchaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_accounting_account

Remove an account

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveAccountingAccountRequest(
    connection_id='string',
    id='<ID>',
)

res = s.accounting.remove_accounting_account(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingAccountRequest](../../models/operations/removeaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveAccountingAccountResponse](../../models/operations/removeaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_accounting_customer

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_accounting_invoice

Remove a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_accounting_transaction

Remove a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveAccountingTransactionRequest(
    connection_id='string',
    id='<ID>',
)

res = s.accounting.remove_accounting_transaction(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveAccountingTransactionRequest](../../models/operations/removeaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.RemoveAccountingTransactionResponse](../../models/operations/removeaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_accounting_account

Update an account

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

req = operations.UpdateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        name='string',
        raw=shared.PropertyAccountingAccountRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.update_accounting_account(req)

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingAccountRequest](../../models/operations/updateaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateAccountingAccountResponse](../../models/operations/updateaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_accounting_customer

Update a customer

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_accounting_invoice

Update a invoice

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateAccountingTransactionRequest(
    accounting_transaction=shared.AccountingTransaction(
        account_id='string',
        id='<ID>',
        line_items=[
            shared.AccountingTransactionLineitem(
                id='<ID>',
                total_amount=6498.37,
            ),
        ],
        raw=shared.PropertyAccountingTransactionRaw(),
        total_amount=5659.17,
        type=shared.AccountingTransactionType.SPEND,
    ),
    connection_id='string',
    id='<ID>',
)

res = s.accounting.update_accounting_transaction(req)

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateAccountingTransactionRequest](../../models/operations/updateaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.UpdateAccountingTransactionResponse](../../models/operations/updateaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
