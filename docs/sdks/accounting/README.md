# Accounting
(*accounting*)

### Available Operations

* [create_accounting_account](#create_accounting_account) - Create an account
* [create_accounting_contact](#create_accounting_contact) - Create a contact
* [create_accounting_invoice](#create_accounting_invoice) - Create a invoice
* [create_accounting_payment](#create_accounting_payment) - Create a payment
* [create_accounting_taxrate](#create_accounting_taxrate) - Create a taxrate
* [create_accounting_transaction](#create_accounting_transaction) - Create a transaction
* [get_accounting_account](#get_accounting_account) - Retrieve an account
* [get_accounting_contact](#get_accounting_contact) - Retrieve a contact
* [get_accounting_invoice](#get_accounting_invoice) - Retrieve a invoice
* [get_accounting_organization](#get_accounting_organization) - Retrieve an organization
* [get_accounting_payment](#get_accounting_payment) - Retrieve a payment
* [get_accounting_payout](#get_accounting_payout) - Retrieve a payout
* [get_accounting_refund](#get_accounting_refund) - Retrieve a refund
* [get_accounting_taxrate](#get_accounting_taxrate) - Retrieve a taxrate
* [get_accounting_transaction](#get_accounting_transaction) - Retrieve a transaction
* [list_accounting_accounts](#list_accounting_accounts) - List all accounts
* [list_accounting_contacts](#list_accounting_contacts) - List all contacts
* [list_accounting_invoices](#list_accounting_invoices) - List all invoices
* [list_accounting_organizations](#list_accounting_organizations) - List all organizations
* [list_accounting_payments](#list_accounting_payments) - List all payments
* [list_accounting_payouts](#list_accounting_payouts) - List all payouts
* [list_accounting_refunds](#list_accounting_refunds) - List all refunds
* [list_accounting_taxrates](#list_accounting_taxrates) - List all taxrates
* [list_accounting_transactions](#list_accounting_transactions) - List all transactions
* [patch_accounting_account](#patch_accounting_account) - Update an account
* [patch_accounting_contact](#patch_accounting_contact) - Update a contact
* [patch_accounting_invoice](#patch_accounting_invoice) - Update a invoice
* [patch_accounting_payment](#patch_accounting_payment) - Update a payment
* [patch_accounting_taxrate](#patch_accounting_taxrate) - Update a taxrate
* [patch_accounting_transaction](#patch_accounting_transaction) - Update a transaction
* [remove_accounting_account](#remove_accounting_account) - Remove an account
* [remove_accounting_contact](#remove_accounting_contact) - Remove a contact
* [remove_accounting_invoice](#remove_accounting_invoice) - Remove a invoice
* [remove_accounting_payment](#remove_accounting_payment) - Remove a payment
* [remove_accounting_taxrate](#remove_accounting_taxrate) - Remove a taxrate
* [remove_accounting_transaction](#remove_accounting_transaction) - Remove a transaction
* [update_accounting_account](#update_accounting_account) - Update an account
* [update_accounting_contact](#update_accounting_contact) - Update a contact
* [update_accounting_invoice](#update_accounting_invoice) - Update a invoice
* [update_accounting_payment](#update_accounting_payment) - Update a payment
* [update_accounting_taxrate](#update_accounting_taxrate) - Update a taxrate
* [update_accounting_transaction](#update_accounting_transaction) - Update a transaction

## create_accounting_account

Create an account

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingAccountRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_account(req, operations.CreateAccountingAccountSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingAccountRequest](../../models/operations/createaccountingaccountrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingAccountSecurity](../../models/operations/createaccountingaccountsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingAccountResponse](../../models/operations/createaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_accounting_contact

Create a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingContactRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_contact(req, operations.CreateAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingContactRequest](../../models/operations/createaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingContactSecurity](../../models/operations/createaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingContactResponse](../../models/operations/createaccountingcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_accounting_invoice

Create a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingInvoiceRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_invoice(req, operations.CreateAccountingInvoiceSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingInvoiceSecurity](../../models/operations/createaccountinginvoicesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_accounting_payment

Create a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingPaymentRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_payment(req, operations.CreateAccountingPaymentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingPaymentRequest](../../models/operations/createaccountingpaymentrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingPaymentSecurity](../../models/operations/createaccountingpaymentsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingPaymentResponse](../../models/operations/createaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_accounting_taxrate

Create a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingTaxrateRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_taxrate(req, operations.CreateAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingTaxrateRequest](../../models/operations/createaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingTaxrateSecurity](../../models/operations/createaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingTaxrateResponse](../../models/operations/createaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_accounting_transaction

Create a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingTransactionRequest(
    connection_id='<value>',
)

res = s.accounting.create_accounting_transaction(req, operations.CreateAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingTransactionRequest](../../models/operations/createaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.CreateAccountingTransactionSecurity](../../models/operations/createaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.CreateAccountingTransactionResponse](../../models/operations/createaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_account

Retrieve an account

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingAccountRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_account(req, operations.GetAccountingAccountSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingAccountRequest](../../models/operations/getaccountingaccountrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingAccountSecurity](../../models/operations/getaccountingaccountsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingAccountResponse](../../models/operations/getaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_contact(req, operations.GetAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingContactRequest](../../models/operations/getaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingContactSecurity](../../models/operations/getaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingContactResponse](../../models/operations/getaccountingcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_invoice

Retrieve a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingInvoiceRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_invoice(req, operations.GetAccountingInvoiceSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingInvoiceRequest](../../models/operations/getaccountinginvoicerequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingInvoiceSecurity](../../models/operations/getaccountinginvoicesecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingInvoiceResponse](../../models/operations/getaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_organization

Retrieve an organization

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingOrganizationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_organization(req, operations.GetAccountingOrganizationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_organization is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingOrganizationRequest](../../models/operations/getaccountingorganizationrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetAccountingOrganizationSecurity](../../models/operations/getaccountingorganizationsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetAccountingOrganizationResponse](../../models/operations/getaccountingorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_payment

Retrieve a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingPaymentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_payment(req, operations.GetAccountingPaymentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingPaymentRequest](../../models/operations/getaccountingpaymentrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingPaymentSecurity](../../models/operations/getaccountingpaymentsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingPaymentResponse](../../models/operations/getaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_payout

Retrieve a payout

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingPayoutRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_payout(req, operations.GetAccountingPayoutSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payout is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingPayoutRequest](../../models/operations/getaccountingpayoutrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetAccountingPayoutSecurity](../../models/operations/getaccountingpayoutsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAccountingPayoutResponse](../../models/operations/getaccountingpayoutresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_refund

Retrieve a refund

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingRefundRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_refund(req, operations.GetAccountingRefundSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_refund is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingRefundRequest](../../models/operations/getaccountingrefundrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetAccountingRefundSecurity](../../models/operations/getaccountingrefundsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAccountingRefundResponse](../../models/operations/getaccountingrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_taxrate

Retrieve a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_taxrate(req, operations.GetAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingTaxrateRequest](../../models/operations/getaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingTaxrateSecurity](../../models/operations/getaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingTaxrateResponse](../../models/operations/getaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_transaction

Retrieve a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.get_accounting_transaction(req, operations.GetAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingTransactionRequest](../../models/operations/getaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetAccountingTransactionSecurity](../../models/operations/getaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetAccountingTransactionResponse](../../models/operations/getaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_accounts

List all accounts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingAccountsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_accounts(req, operations.ListAccountingAccountsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_accounts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingAccountsRequest](../../models/operations/listaccountingaccountsrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingAccountsSecurity](../../models/operations/listaccountingaccountssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingAccountsResponse](../../models/operations/listaccountingaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_contacts

List all contacts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingContactsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_contacts(req, operations.ListAccountingContactsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingContactsRequest](../../models/operations/listaccountingcontactsrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingContactsSecurity](../../models/operations/listaccountingcontactssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingContactsResponse](../../models/operations/listaccountingcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_invoices

List all invoices

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingInvoicesRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_invoices(req, operations.ListAccountingInvoicesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_invoices is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingInvoicesRequest](../../models/operations/listaccountinginvoicesrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingInvoicesSecurity](../../models/operations/listaccountinginvoicessecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingInvoicesResponse](../../models/operations/listaccountinginvoicesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_organizations

List all organizations

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingOrganizationsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_organizations(req, operations.ListAccountingOrganizationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_organizations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingOrganizationsRequest](../../models/operations/listaccountingorganizationsrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.ListAccountingOrganizationsSecurity](../../models/operations/listaccountingorganizationssecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.ListAccountingOrganizationsResponse](../../models/operations/listaccountingorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_payments

List all payments

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingPaymentsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_payments(req, operations.ListAccountingPaymentsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payments is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingPaymentsRequest](../../models/operations/listaccountingpaymentsrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingPaymentsSecurity](../../models/operations/listaccountingpaymentssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingPaymentsResponse](../../models/operations/listaccountingpaymentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_payouts

List all payouts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingPayoutsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_payouts(req, operations.ListAccountingPayoutsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payouts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingPayoutsRequest](../../models/operations/listaccountingpayoutsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListAccountingPayoutsSecurity](../../models/operations/listaccountingpayoutssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListAccountingPayoutsResponse](../../models/operations/listaccountingpayoutsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_refunds

List all refunds

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingRefundsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_refunds(req, operations.ListAccountingRefundsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_refunds is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingRefundsRequest](../../models/operations/listaccountingrefundsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListAccountingRefundsSecurity](../../models/operations/listaccountingrefundssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListAccountingRefundsResponse](../../models/operations/listaccountingrefundsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_taxrates

List all taxrates

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingTaxratesRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_taxrates(req, operations.ListAccountingTaxratesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrates is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingTaxratesRequest](../../models/operations/listaccountingtaxratesrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingTaxratesSecurity](../../models/operations/listaccountingtaxratessecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingTaxratesResponse](../../models/operations/listaccountingtaxratesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_transactions

List all transactions

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingTransactionsRequest(
    connection_id='<value>',
)

res = s.accounting.list_accounting_transactions(req, operations.ListAccountingTransactionsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transactions is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingTransactionsRequest](../../models/operations/listaccountingtransactionsrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.ListAccountingTransactionsSecurity](../../models/operations/listaccountingtransactionssecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.ListAccountingTransactionsResponse](../../models/operations/listaccountingtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_account

Update an account

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingAccountRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_account(req, operations.PatchAccountingAccountSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingAccountRequest](../../models/operations/patchaccountingaccountrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingAccountSecurity](../../models/operations/patchaccountingaccountsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingAccountResponse](../../models/operations/patchaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_contact(req, operations.PatchAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingContactRequest](../../models/operations/patchaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingContactSecurity](../../models/operations/patchaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingContactResponse](../../models/operations/patchaccountingcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_invoice

Update a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingInvoiceRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_invoice(req, operations.PatchAccountingInvoiceSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingInvoiceRequest](../../models/operations/patchaccountinginvoicerequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingInvoiceSecurity](../../models/operations/patchaccountinginvoicesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingInvoiceResponse](../../models/operations/patchaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_payment

Update a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingPaymentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_payment(req, operations.PatchAccountingPaymentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingPaymentRequest](../../models/operations/patchaccountingpaymentrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingPaymentSecurity](../../models/operations/patchaccountingpaymentsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingPaymentResponse](../../models/operations/patchaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_taxrate

Update a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_taxrate(req, operations.PatchAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingTaxrateRequest](../../models/operations/patchaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingTaxrateSecurity](../../models/operations/patchaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingTaxrateResponse](../../models/operations/patchaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.patch_accounting_transaction(req, operations.PatchAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchAccountingTransactionRequest](../../models/operations/patchaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchAccountingTransactionSecurity](../../models/operations/patchaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchAccountingTransactionResponse](../../models/operations/patchaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_account

Remove an account

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingAccountRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_account(req, operations.RemoveAccountingAccountSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingAccountRequest](../../models/operations/removeaccountingaccountrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingAccountSecurity](../../models/operations/removeaccountingaccountsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingAccountResponse](../../models/operations/removeaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_contact(req, operations.RemoveAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingContactRequest](../../models/operations/removeaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingContactSecurity](../../models/operations/removeaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingContactResponse](../../models/operations/removeaccountingcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_invoice

Remove a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingInvoiceRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_invoice(req, operations.RemoveAccountingInvoiceSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingInvoiceRequest](../../models/operations/removeaccountinginvoicerequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingInvoiceSecurity](../../models/operations/removeaccountinginvoicesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingInvoiceResponse](../../models/operations/removeaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_payment

Remove a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingPaymentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_payment(req, operations.RemoveAccountingPaymentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingPaymentRequest](../../models/operations/removeaccountingpaymentrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingPaymentSecurity](../../models/operations/removeaccountingpaymentsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingPaymentResponse](../../models/operations/removeaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_taxrate

Remove a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_taxrate(req, operations.RemoveAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingTaxrateRequest](../../models/operations/removeaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingTaxrateSecurity](../../models/operations/removeaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingTaxrateResponse](../../models/operations/removeaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_transaction

Remove a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.remove_accounting_transaction(req, operations.RemoveAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.RemoveAccountingTransactionRequest](../../models/operations/removeaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.RemoveAccountingTransactionSecurity](../../models/operations/removeaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.RemoveAccountingTransactionResponse](../../models/operations/removeaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_account

Update an account

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingAccountRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_account(req, operations.UpdateAccountingAccountSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingAccountRequest](../../models/operations/updateaccountingaccountrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingAccountSecurity](../../models/operations/updateaccountingaccountsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingAccountResponse](../../models/operations/updateaccountingaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_contact(req, operations.UpdateAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingContactRequest](../../models/operations/updateaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingContactSecurity](../../models/operations/updateaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingContactResponse](../../models/operations/updateaccountingcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_invoice

Update a invoice

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingInvoiceRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_invoice(req, operations.UpdateAccountingInvoiceSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingInvoiceRequest](../../models/operations/updateaccountinginvoicerequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingInvoiceSecurity](../../models/operations/updateaccountinginvoicesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingInvoiceResponse](../../models/operations/updateaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_payment

Update a payment

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingPaymentRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_payment(req, operations.UpdateAccountingPaymentSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingPaymentRequest](../../models/operations/updateaccountingpaymentrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingPaymentSecurity](../../models/operations/updateaccountingpaymentsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingPaymentResponse](../../models/operations/updateaccountingpaymentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_taxrate

Update a taxrate

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingTaxrateRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_taxrate(req, operations.UpdateAccountingTaxrateSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_taxrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingTaxrateRequest](../../models/operations/updateaccountingtaxraterequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingTaxrateSecurity](../../models/operations/updateaccountingtaxratesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingTaxrateResponse](../../models/operations/updateaccountingtaxrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_transaction

Update a transaction

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingTransactionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.accounting.update_accounting_transaction(req, operations.UpdateAccountingTransactionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_transaction is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateAccountingTransactionRequest](../../models/operations/updateaccountingtransactionrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.UpdateAccountingTransactionSecurity](../../models/operations/updateaccountingtransactionsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.UpdateAccountingTransactionResponse](../../models/operations/updateaccountingtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
