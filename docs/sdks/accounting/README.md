# Accounting

## Overview

### Available Operations

* [create_accounting_account](#create_accounting_account) - Create an account
* [create_accounting_bankfeedaccount](#create_accounting_bankfeedaccount) - Create a bankfeedaccount
* [create_accounting_bankfeedtransaction](#create_accounting_bankfeedtransaction) - Create a bankfeedtransaction
* [create_accounting_bill](#create_accounting_bill) - Create a bill
* [create_accounting_category](#create_accounting_category) - Create a category
* [create_accounting_contact](#create_accounting_contact) - Create a contact
* [create_accounting_creditmemo](#create_accounting_creditmemo) - Create a creditmemo
* [create_accounting_expense](#create_accounting_expense) - Create an expense
* [create_accounting_expensereport](#create_accounting_expensereport) - Create an expensereport
* [create_accounting_invoice](#create_accounting_invoice) - Create an invoice
* [create_accounting_journal](#create_accounting_journal) - Create a journal
* [create_accounting_order](#create_accounting_order) - Create an order
* [create_accounting_paymentterm](#create_accounting_paymentterm) - Create a paymentterm
* [create_accounting_project](#create_accounting_project) - Create a project
* [create_accounting_purchaseorder](#create_accounting_purchaseorder) - Create a purchaseorder
* [create_accounting_quote](#create_accounting_quote) - Create a quote
* [create_accounting_salesorder](#create_accounting_salesorder) - Create a salesorder
* [create_accounting_taxrate](#create_accounting_taxrate) - Create a taxrate
* [create_accounting_transaction](#create_accounting_transaction) - Create a transaction
* [create_accounting_vendorcredit](#create_accounting_vendorcredit) - Create a vendorcredit
* [get_accounting_account](#get_accounting_account) - Retrieve an account
* [get_accounting_agedpayable](#get_accounting_agedpayable) - Retrieve an agedpayable
* [get_accounting_agedreceivable](#get_accounting_agedreceivable) - Retrieve an agedreceivable
* [get_accounting_balancesheet](#get_accounting_balancesheet) - Retrieve a balancesheet
* [get_accounting_bankfeedaccount](#get_accounting_bankfeedaccount) - Retrieve a bankfeedaccount
* [get_accounting_bankfeedtransaction](#get_accounting_bankfeedtransaction) - Retrieve a bankfeedtransaction
* [get_accounting_bill](#get_accounting_bill) - Retrieve a bill
* [get_accounting_cashflow](#get_accounting_cashflow) - Retrieve a cashflow
* [get_accounting_category](#get_accounting_category) - Retrieve a category
* [get_accounting_contact](#get_accounting_contact) - Retrieve a contact
* [get_accounting_creditmemo](#get_accounting_creditmemo) - Retrieve a creditmemo
* [get_accounting_expense](#get_accounting_expense) - Retrieve an expense
* [get_accounting_expensereport](#get_accounting_expensereport) - Retrieve an expensereport
* [get_accounting_invoice](#get_accounting_invoice) - Retrieve an invoice
* [get_accounting_journal](#get_accounting_journal) - Retrieve a journal
* [get_accounting_order](#get_accounting_order) - Retrieve an order
* [get_accounting_organization](#get_accounting_organization) - Retrieve an organization
* [get_accounting_paymentterm](#get_accounting_paymentterm) - Retrieve a paymentterm
* [get_accounting_profitloss](#get_accounting_profitloss) - Retrieve a profitloss
* [get_accounting_project](#get_accounting_project) - Retrieve a project
* [get_accounting_purchaseorder](#get_accounting_purchaseorder) - Retrieve a purchaseorder
* [get_accounting_purchasereceipt](#get_accounting_purchasereceipt) - Retrieve a purchasereceipt
* [get_accounting_quote](#get_accounting_quote) - Retrieve a quote
* [get_accounting_salesorder](#get_accounting_salesorder) - Retrieve a salesorder
* [get_accounting_salesreceipt](#get_accounting_salesreceipt) - Retrieve a salesreceipt
* [get_accounting_taxrate](#get_accounting_taxrate) - Retrieve a taxrate
* [get_accounting_transaction](#get_accounting_transaction) - Retrieve a transaction
* [get_accounting_trialbalance](#get_accounting_trialbalance) - Retrieve a trialbalance
* [get_accounting_vendorcredit](#get_accounting_vendorcredit) - Retrieve a vendorcredit
* [list_accounting_accounts](#list_accounting_accounts) - List all accounts
* [list_accounting_agedpayables](#list_accounting_agedpayables) - List all agedpayables
* [list_accounting_agedreceivables](#list_accounting_agedreceivables) - List all agedreceivables
* [list_accounting_balancesheets](#list_accounting_balancesheets) - List all balancesheets
* [list_accounting_bankfeedaccounts](#list_accounting_bankfeedaccounts) - List all bankfeedaccounts
* [list_accounting_bankfeedtransactions](#list_accounting_bankfeedtransactions) - List all bankfeedtransactions
* [list_accounting_bills](#list_accounting_bills) - List all bills
* [list_accounting_cashflows](#list_accounting_cashflows) - List all cashflows
* [list_accounting_categories](#list_accounting_categories) - List all categories
* [list_accounting_contacts](#list_accounting_contacts) - List all contacts
* [list_accounting_creditmemoes](#list_accounting_creditmemoes) - List all creditmemoes
* [list_accounting_expensereports](#list_accounting_expensereports) - List all expensereports
* [list_accounting_expenses](#list_accounting_expenses) - List all expenses
* [list_accounting_invoices](#list_accounting_invoices) - List all invoices
* [list_accounting_journals](#list_accounting_journals) - List all journals
* [list_accounting_orders](#list_accounting_orders) - List all orders
* [list_accounting_organizations](#list_accounting_organizations) - List all organizations
* [list_accounting_paymentterms](#list_accounting_paymentterms) - List all paymentterms
* [list_accounting_profitlosses](#list_accounting_profitlosses) - List all profitlosses
* [list_accounting_projects](#list_accounting_projects) - List all projects
* [list_accounting_purchaseorders](#list_accounting_purchaseorders) - List all purchaseorders
* [list_accounting_purchasereceipts](#list_accounting_purchasereceipts) - List all purchasereceipts
* [list_accounting_quotes](#list_accounting_quotes) - List all quotes
* [list_accounting_salesorders](#list_accounting_salesorders) - List all salesorders
* [list_accounting_salesreceipts](#list_accounting_salesreceipts) - List all salesreceipts
* [list_accounting_taxrates](#list_accounting_taxrates) - List all taxrates
* [list_accounting_transactions](#list_accounting_transactions) - List all transactions
* [list_accounting_trialbalances](#list_accounting_trialbalances) - List all trialbalances
* [list_accounting_vendorcredits](#list_accounting_vendorcredits) - List all vendorcredits
* [patch_accounting_account](#patch_accounting_account) - Update an account
* [patch_accounting_bankfeedaccount](#patch_accounting_bankfeedaccount) - Update a bankfeedaccount
* [patch_accounting_bankfeedtransaction](#patch_accounting_bankfeedtransaction) - Update a bankfeedtransaction
* [patch_accounting_bill](#patch_accounting_bill) - Update a bill
* [patch_accounting_category](#patch_accounting_category) - Update a category
* [patch_accounting_contact](#patch_accounting_contact) - Update a contact
* [patch_accounting_creditmemo](#patch_accounting_creditmemo) - Update a creditmemo
* [patch_accounting_expense](#patch_accounting_expense) - Update an expense
* [patch_accounting_expensereport](#patch_accounting_expensereport) - Update an expensereport
* [patch_accounting_invoice](#patch_accounting_invoice) - Update an invoice
* [patch_accounting_journal](#patch_accounting_journal) - Update a journal
* [patch_accounting_order](#patch_accounting_order) - Update an order
* [patch_accounting_paymentterm](#patch_accounting_paymentterm) - Update a paymentterm
* [patch_accounting_project](#patch_accounting_project) - Update a project
* [patch_accounting_purchaseorder](#patch_accounting_purchaseorder) - Update a purchaseorder
* [patch_accounting_quote](#patch_accounting_quote) - Update a quote
* [patch_accounting_salesorder](#patch_accounting_salesorder) - Update a salesorder
* [patch_accounting_taxrate](#patch_accounting_taxrate) - Update a taxrate
* [patch_accounting_transaction](#patch_accounting_transaction) - Update a transaction
* [patch_accounting_vendorcredit](#patch_accounting_vendorcredit) - Update a vendorcredit
* [remove_accounting_account](#remove_accounting_account) - Remove an account
* [remove_accounting_bankfeedaccount](#remove_accounting_bankfeedaccount) - Remove a bankfeedaccount
* [remove_accounting_bankfeedtransaction](#remove_accounting_bankfeedtransaction) - Remove a bankfeedtransaction
* [remove_accounting_bill](#remove_accounting_bill) - Remove a bill
* [remove_accounting_category](#remove_accounting_category) - Remove a category
* [remove_accounting_contact](#remove_accounting_contact) - Remove a contact
* [remove_accounting_creditmemo](#remove_accounting_creditmemo) - Remove a creditmemo
* [remove_accounting_expense](#remove_accounting_expense) - Remove an expense
* [remove_accounting_expensereport](#remove_accounting_expensereport) - Remove an expensereport
* [remove_accounting_invoice](#remove_accounting_invoice) - Remove an invoice
* [remove_accounting_journal](#remove_accounting_journal) - Remove a journal
* [remove_accounting_order](#remove_accounting_order) - Remove an order
* [remove_accounting_paymentterm](#remove_accounting_paymentterm) - Remove a paymentterm
* [remove_accounting_project](#remove_accounting_project) - Remove a project
* [remove_accounting_purchaseorder](#remove_accounting_purchaseorder) - Remove a purchaseorder
* [remove_accounting_quote](#remove_accounting_quote) - Remove a quote
* [remove_accounting_salesorder](#remove_accounting_salesorder) - Remove a salesorder
* [remove_accounting_taxrate](#remove_accounting_taxrate) - Remove a taxrate
* [remove_accounting_transaction](#remove_accounting_transaction) - Remove a transaction
* [remove_accounting_vendorcredit](#remove_accounting_vendorcredit) - Remove a vendorcredit
* [update_accounting_account](#update_accounting_account) - Update an account
* [update_accounting_bankfeedaccount](#update_accounting_bankfeedaccount) - Update a bankfeedaccount
* [update_accounting_bankfeedtransaction](#update_accounting_bankfeedtransaction) - Update a bankfeedtransaction
* [update_accounting_bill](#update_accounting_bill) - Update a bill
* [update_accounting_category](#update_accounting_category) - Update a category
* [update_accounting_contact](#update_accounting_contact) - Update a contact
* [update_accounting_creditmemo](#update_accounting_creditmemo) - Update a creditmemo
* [update_accounting_expense](#update_accounting_expense) - Update an expense
* [update_accounting_expensereport](#update_accounting_expensereport) - Update an expensereport
* [update_accounting_invoice](#update_accounting_invoice) - Update an invoice
* [update_accounting_journal](#update_accounting_journal) - Update a journal
* [update_accounting_order](#update_accounting_order) - Update an order
* [update_accounting_paymentterm](#update_accounting_paymentterm) - Update a paymentterm
* [update_accounting_project](#update_accounting_project) - Update a project
* [update_accounting_purchaseorder](#update_accounting_purchaseorder) - Update a purchaseorder
* [update_accounting_quote](#update_accounting_quote) - Update a quote
* [update_accounting_salesorder](#update_accounting_salesorder) - Update a salesorder
* [update_accounting_taxrate](#update_accounting_taxrate) - Update a taxrate
* [update_accounting_transaction](#update_accounting_transaction) - Update a transaction
* [update_accounting_vendorcredit](#update_accounting_vendorcredit) - Update a vendorcredit

## create_accounting_account

Create an account

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingAccount" method="post" path="/accounting/{connection_id}/account" example="accounting_account" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {
            "balance": 12092.0,
            "created_at": parse_datetime("2022-07-03T17:57:07.391Z"),
            "currency": "CAD",
            "customer_defined_code": "6170",
            "description": "Voluptatibus valde spoliatio.",
            "id": "71a0c5e2-8579-4ed0-9615-d3a139f92492",
            "is_payable": False,
            "metadata": [],
            "name": "Auto Loan Account",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vilitas",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "comedo",
                },
            ],
            "type": shared.Type.ACCOUNTS_RECEIVABLE,
            "updated_at": parse_datetime("2023-08-06T14:16:21.001Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingAccountRequest](../../models/operations/createaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingAccountResponse](../../models/operations/createaccountingaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_bankfeedaccount

Create a bankfeedaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingBankfeedaccount" method="post" path="/accounting/{connection_id}/bankfeedaccount" example="accounting_bankfeedaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_bankfeedaccount(request={
        "accounting_bankfeedaccount": {
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 49437.0,
            "bank_name": "Wells Fargo",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "AUD",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "7d62fb0f-fa04-43d1-a1ff-2ac21b1267ef",
            "metadata": [],
            "name": "Corwin, Donnelly and Connelly Checking",
            "routing_number": "694667752",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-23T09:05:03.284Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedaccount is not None

    # Handle response
    print(res.accounting_bankfeedaccount)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.CreateAccountingBankfeedaccountRequest](../../models/operations/createaccountingbankfeedaccountrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.CreateAccountingBankfeedaccountResponse](../../models/operations/createaccountingbankfeedaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_bankfeedtransaction

Create a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingBankfeedtransaction" method="post" path="/accounting/{connection_id}/bankfeedtransaction" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "c6bdb45f-7fa5-4b9b-a480-4727f873f723",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T00:29:08.607Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T05:56:55.059Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T00:40:43.175Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.CreateAccountingBankfeedtransactionRequest](../../models/operations/createaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.CreateAccountingBankfeedtransactionResponse](../../models/operations/createaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_bill

Create a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingBill" method="post" path="/accounting/{connection_id}/bill" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_bill(request={
        "accounting_bill": {
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "04c13eb7-cd1f-4936-aa4b-adbd5c83e662",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "d65d8bf1-438a-4e6f-ab11-522eb801c7e4",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "de88207b-3a11-4be6-b544-eae219cd137a",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T02:34:30.089Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAccountingBillRequest](../../models/operations/createaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAccountingBillResponse](../../models/operations/createaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_category

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCategory" method="post" path="/accounting/{connection_id}/category" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Textus ab thymum labore basium.",
            "id": "ebf1d96b-aa3b-48e3-b941-4d6c9300c2dc",
            "is_active": False,
            "metadata": [],
            "name": "Beauty",
            "updated_at": parse_datetime("2025-09-10T16:32:55.222Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingCategoryRequest](../../models/operations/createaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateAccountingCategoryResponse](../../models/operations/createaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_contact

Create a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingContact" method="post" path="/accounting/{connection_id}/contact" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "4b985b9a-65ff-4d96-bbf2-afb487afe6e6",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "888a5045-1b70-4854-ae2d-221aceaac24a",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.518Z"),
            "website": "https://kertzmanngroup.com",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingContactRequest](../../models/operations/createaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingContactResponse](../../models/operations/createaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_creditmemo

Create a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCreditmemo" method="post" path="/accounting/{connection_id}/creditmemo" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "CM-99537",
            "currency": "AUD",
            "discount_amount": 0.0,
            "id": "780e4fca-7630-41ec-ac30-f7051968a67f",
            "lineitems": [],
            "metadata": [],
            "notes": "Hic vorax dedecor amo adfero torqueo quas victoria.",
            "posted_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "send": True,
            "status": shared.AccountingCreditmemoStatus.AUTHORIZED,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-09-10T13:16:31.890Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingCreditmemoRequest](../../models/operations/createaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateAccountingCreditmemoResponse](../../models/operations/createaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_expense

Create an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingExpense" method="post" path="/accounting/{connection_id}/expense" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_expense(request={
        "accounting_expense": {
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "5f8b1c03-3bc6-44f8-aea5-9ae8e8f4d547",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "ff8ffede-aa95-4bee-8ce3-e67d9ddae0af",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "605bea72-d349-47ad-9eb7-7f03b244f9b8",
            "lineitems": [
                {
                    "id": "287307d7-dbd2-4eba-a195-866acd80f0e3",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "0610f264-59c1-4af3-9d29-0bd9aa685f99",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "7948b977-1003-4617-91c2-ab82b9105793",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "9dbd88b4-ea80-4d49-96de-7a204373ab4a",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "b2eb0efd-ec3c-4275-a913-8c9d20cee3de",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-02T06:14:35.954Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingExpenseRequest](../../models/operations/createaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingExpenseResponse](../../models/operations/createaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_expensereport

Create an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingExpensereport" method="post" path="/accounting/{connection_id}/expensereport" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T07:25:37.091Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "05f2b20b-9164-4958-a57c-53d5fd5670dc",
            "lineitems": [
                {
                    "id": "fb1362dc-9143-4314-8c15-0c49ba4d4608",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "13de6f70-bef8-4fcb-91a0-e374cf87ab34",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "bb047b18-5efd-4aa2-9764-10829e994c3e",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "68be3e94-844e-49df-804c-db7752ceaccd",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T07:25:37.091Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T07:25:37.091Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateAccountingExpensereportRequest](../../models/operations/createaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateAccountingExpensereportResponse](../../models/operations/createaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_invoice

Create an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingInvoice" method="post" path="/accounting/{connection_id}/invoice" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "3f7cf848-2892-424b-9e13-aa4f7812f4c3",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "7b1b2543-630b-470b-84d3-f4a5a60727fc",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "adbee18c-c92e-4da5-9a3e-db0f23245eaf",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-22T11:33:30.917Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_journal

Create a journal

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingJournal" method="post" path="/accounting/{connection_id}/journal" example="accounting_journal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_journal(request={
        "accounting_journal": {
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-02-20T15:14:55.881Z"),
            "currency": "CAD",
            "description": "Cilicium minima calco constans adipisci.",
            "id": "8accebf6-8c59-442a-bebd-5ab5155ba22a",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2023-11-05T18:27:35.613Z"),
            "reference": "JE-78884",
            "source": "crustulum",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-10T11:27:02.604Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_journal is not None

    # Handle response
    print(res.accounting_journal)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingJournalRequest](../../models/operations/createaccountingjournalrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingJournalResponse](../../models/operations/createaccountingjournalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_order

Create an order

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingOrder" method="post" path="/accounting/{connection_id}/order" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "f25850f6-9e75-447a-8577-6d78d4580209",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T01:18:36.550Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccountingOrderRequest](../../models/operations/createaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAccountingOrderResponse](../../models/operations/createaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_paymentterm

Create a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingPaymentterm" method="post" path="/accounting/{connection_id}/paymentterm" example="accounting_paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_paymentterm(request={
        "accounting_paymentterm": {
            "category": shared.Category.STANDARD,
            "created_at": parse_datetime("2021-08-22T22:42:42.265Z"),
            "day_of_month_due": 4.0,
            "description": "Cogito pecco eos cultura.",
            "discount_day_of_month": 13.0,
            "discount_days": 4.0,
            "discount_percent": 5.0,
            "due_days": 57.0,
            "due_next_month_days": 9.0,
            "id": "6144e8d3-6b06-4b5a-96a6-94a2d6e6fdc4",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-07T10:28:50.046Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAccountingPaymenttermRequest](../../models/operations/createaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateAccountingPaymenttermResponse](../../models/operations/createaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_project

Create a project

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingProject" method="post" path="/accounting/{connection_id}/project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_project(request={
        "accounting_project": {},
        "connection_id": "<id>",
    })

    assert res.accounting_project is not None

    # Handle response
    print(res.accounting_project)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingProjectRequest](../../models/operations/createaccountingprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingProjectResponse](../../models/operations/createaccountingprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_purchaseorder

Create a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingPurchaseorder" method="post" path="/accounting/{connection_id}/purchaseorder" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "attachments": [],
            "billing_address": {
                "address1": "72142 Willow Street",
                "address2": "Apt. 967",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "FL",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "EUR",
            "id": "5575d5ba-6d1e-4539-9b09-b44fe251285c",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "shipping_address": {
                "address1": "76494 Medhurst Club",
                "city": "Kshlerinfurt",
                "country_code": "US",
                "postal_code": "92116-5474",
                "region": "Oregon",
                "region_code": "WY",
            },
            "status": shared.AccountingPurchaseorderStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-08-11T02:42:33.395Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateAccountingPurchaseorderRequest](../../models/operations/createaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateAccountingPurchaseorderResponse](../../models/operations/createaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_quote

Create a quote

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingQuote" method="post" path="/accounting/{connection_id}/quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccountingQuoteRequest](../../models/operations/createaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAccountingQuoteResponse](../../models/operations/createaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_salesorder

Create a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingSalesorder" method="post" path="/accounting/{connection_id}/salesorder" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T05:42:39.589Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "c0fba8a7-b802-4168-bfb0-e0cf355e598c",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T05:42:39.589Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingSalesorderRequest](../../models/operations/createaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateAccountingSalesorderResponse](../../models/operations/createaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_taxrate

Create a taxrate

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingTaxrate" method="post" path="/accounting/{connection_id}/taxrate" example="accounting_taxrate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_taxrate(request={
        "accounting_taxrate": {
            "components": [
                {
                    "is_compound": False,
                    "name": "Exempt",
                    "rate": 0.0,
                },
            ],
            "country": "US",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Exempt (0%)",
            "effective_rate": 0.0,
            "id": "674f0f5c-42e2-4c45-9603-93ce5ae013a6",
            "is_active": False,
            "is_compound": False,
            "metadata": [],
            "name": "Exempt",
            "rate": 0.0,
            "region": "KS",
            "total_rate": 0.0,
            "type": shared.AccountingTaxrateType.SALES,
            "updated_at": parse_datetime("2020-02-13T04:41:49.452Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_taxrate is not None

    # Handle response
    print(res.accounting_taxrate)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingTaxrateRequest](../../models/operations/createaccountingtaxraterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingTaxrateResponse](../../models/operations/createaccountingtaxrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_transaction

Create a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingTransaction" method="post" path="/accounting/{connection_id}/transaction" example="accounting_transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_transaction(request={
        "accounting_transaction": {
            "created_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "id": "cc99b400-3dbd-4276-addd-9ea38dfa0938",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The turquoise Hat combines Wallis and Futuna aesthetics with Potassium-based durability",
                    "id": "a7db9c15-d6b3-47f3-af5d-32d0f2afc3d0",
                    "name": "Shirt",
                    "total_amount": 10184.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 19.0,
                },
            ],
            "memo": "deposit of ISK 792.81 at Fritsch - Dooley charged to account ending in 7879 using card ending in ****3230.",
            "status": shared.AccountingTransactionStatus.PENDING,
            "tax_amount": 0.0,
            "total_amount": 10184.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2019-10-14T05:55:46.797Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAccountingTransactionRequest](../../models/operations/createaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateAccountingTransactionResponse](../../models/operations/createaccountingtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_accounting_vendorcredit

Create a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingVendorcredit" method="post" path="/accounting/{connection_id}/vendorcredit" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "b96d11b4-1858-4dd6-bc6e-93ab44f0b4c2",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-02T21:50:25.784Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingVendorcreditRequest](../../models/operations/createaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.CreateAccountingVendorcreditResponse](../../models/operations/createaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_account

Retrieve an account

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingAccount" method="get" path="/accounting/{connection_id}/account/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_account(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingAccountRequest](../../models/operations/getaccountingaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingAccountResponse](../../models/operations/getaccountingaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_agedpayable

Retrieve an agedpayable

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingAgedpayable" method="get" path="/accounting/{connection_id}/agedpayable/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_agedpayable(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_agedpayable is not None

    # Handle response
    print(res.accounting_agedpayable)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingAgedpayableRequest](../../models/operations/getaccountingagedpayablerequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingAgedpayableResponse](../../models/operations/getaccountingagedpayableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_agedreceivable

Retrieve an agedreceivable

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingAgedreceivable" method="get" path="/accounting/{connection_id}/agedreceivable/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_agedreceivable(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_agedreceivable is not None

    # Handle response
    print(res.accounting_agedreceivable)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAccountingAgedreceivableRequest](../../models/operations/getaccountingagedreceivablerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.GetAccountingAgedreceivableResponse](../../models/operations/getaccountingagedreceivableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_balancesheet

Retrieve a balancesheet

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBalancesheet" method="get" path="/accounting/{connection_id}/balancesheet/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_balancesheet(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_balancesheet is not None

    # Handle response
    print(res.accounting_balancesheet)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingBalancesheetRequest](../../models/operations/getaccountingbalancesheetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingBalancesheetResponse](../../models/operations/getaccountingbalancesheetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_bankfeedaccount

Retrieve a bankfeedaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBankfeedaccount" method="get" path="/accounting/{connection_id}/bankfeedaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_bankfeedaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedaccount is not None

    # Handle response
    print(res.accounting_bankfeedaccount)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAccountingBankfeedaccountRequest](../../models/operations/getaccountingbankfeedaccountrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.GetAccountingBankfeedaccountResponse](../../models/operations/getaccountingbankfeedaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_bankfeedtransaction

Retrieve a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBankfeedtransaction" method="get" path="/accounting/{connection_id}/bankfeedtransaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_bankfeedtransaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAccountingBankfeedtransactionRequest](../../models/operations/getaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.GetAccountingBankfeedtransactionResponse](../../models/operations/getaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_bill

Retrieve a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBill" method="get" path="/accounting/{connection_id}/bill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_bill(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAccountingBillRequest](../../models/operations/getaccountingbillrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAccountingBillResponse](../../models/operations/getaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_cashflow

Retrieve a cashflow

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCashflow" method="get" path="/accounting/{connection_id}/cashflow/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_cashflow(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_cashflow is not None

    # Handle response
    print(res.accounting_cashflow)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingCashflowRequest](../../models/operations/getaccountingcashflowrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAccountingCashflowResponse](../../models/operations/getaccountingcashflowresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_category

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCategory" method="get" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingCategoryRequest](../../models/operations/getaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAccountingCategoryResponse](../../models/operations/getaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_contact

Retrieve a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingContact" method="get" path="/accounting/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingContactRequest](../../models/operations/getaccountingcontactrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingContactResponse](../../models/operations/getaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_creditmemo

Retrieve a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCreditmemo" method="get" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_creditmemo(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingCreditmemoRequest](../../models/operations/getaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingCreditmemoResponse](../../models/operations/getaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_expense

Retrieve an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingExpense" method="get" path="/accounting/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingExpenseRequest](../../models/operations/getaccountingexpenserequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingExpenseResponse](../../models/operations/getaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_expensereport

Retrieve an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingExpensereport" method="get" path="/accounting/{connection_id}/expensereport/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_expensereport(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingExpensereportRequest](../../models/operations/getaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetAccountingExpensereportResponse](../../models/operations/getaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_invoice

Retrieve an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingInvoice" method="get" path="/accounting/{connection_id}/invoice/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_invoice(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingInvoiceRequest](../../models/operations/getaccountinginvoicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingInvoiceResponse](../../models/operations/getaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_journal

Retrieve a journal

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingJournal" method="get" path="/accounting/{connection_id}/journal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_journal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_journal is not None

    # Handle response
    print(res.accounting_journal)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingJournalRequest](../../models/operations/getaccountingjournalrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingJournalResponse](../../models/operations/getaccountingjournalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_order

Retrieve an order

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrder" method="get" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountingOrderRequest](../../models/operations/getaccountingorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountingOrderResponse](../../models/operations/getaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_organization

Retrieve an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrganization" method="get" path="/accounting/{connection_id}/organization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_organization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_organization is not None

    # Handle response
    print(res.accounting_organization)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingOrganizationRequest](../../models/operations/getaccountingorganizationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingOrganizationResponse](../../models/operations/getaccountingorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_paymentterm

Retrieve a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingPaymentterm" method="get" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_paymentterm(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingPaymenttermRequest](../../models/operations/getaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingPaymenttermResponse](../../models/operations/getaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_profitloss

Retrieve a profitloss

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingProfitloss" method="get" path="/accounting/{connection_id}/profitloss/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_profitloss(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_profitloss is not None

    # Handle response
    print(res.accounting_profitloss)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingProfitlossRequest](../../models/operations/getaccountingprofitlossrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingProfitlossResponse](../../models/operations/getaccountingprofitlossresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_project

Retrieve a project

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingProject" method="get" path="/accounting/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_project(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_project is not None

    # Handle response
    print(res.accounting_project)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingProjectRequest](../../models/operations/getaccountingprojectrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingProjectResponse](../../models/operations/getaccountingprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_purchaseorder

Retrieve a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingPurchaseorder" method="get" path="/accounting/{connection_id}/purchaseorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_purchaseorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingPurchaseorderRequest](../../models/operations/getaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetAccountingPurchaseorderResponse](../../models/operations/getaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_purchasereceipt

Retrieve a purchasereceipt

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingPurchasereceipt" method="get" path="/accounting/{connection_id}/purchasereceipt/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_purchasereceipt(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchasereceipt is not None

    # Handle response
    print(res.accounting_purchasereceipt)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAccountingPurchasereceiptRequest](../../models/operations/getaccountingpurchasereceiptrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.GetAccountingPurchasereceiptResponse](../../models/operations/getaccountingpurchasereceiptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_quote

Retrieve a quote

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingQuote" method="get" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_quote(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountingQuoteRequest](../../models/operations/getaccountingquoterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountingQuoteResponse](../../models/operations/getaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_salesorder

Retrieve a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingSalesorder" method="get" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_salesorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingSalesorderRequest](../../models/operations/getaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingSalesorderResponse](../../models/operations/getaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_salesreceipt

Retrieve a salesreceipt

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingSalesreceipt" method="get" path="/accounting/{connection_id}/salesreceipt/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_salesreceipt(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesreceipt is not None

    # Handle response
    print(res.accounting_salesreceipt)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingSalesreceiptRequest](../../models/operations/getaccountingsalesreceiptrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingSalesreceiptResponse](../../models/operations/getaccountingsalesreceiptresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_taxrate

Retrieve a taxrate

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingTaxrate" method="get" path="/accounting/{connection_id}/taxrate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_taxrate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_taxrate is not None

    # Handle response
    print(res.accounting_taxrate)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingTaxrateRequest](../../models/operations/getaccountingtaxraterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingTaxrateResponse](../../models/operations/getaccountingtaxrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_transaction

Retrieve a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingTransaction" method="get" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_transaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingTransactionRequest](../../models/operations/getaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingTransactionResponse](../../models/operations/getaccountingtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_trialbalance

Retrieve a trialbalance

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingTrialbalance" method="get" path="/accounting/{connection_id}/trialbalance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_trialbalance(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_trialbalance is not None

    # Handle response
    print(res.accounting_trialbalance)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingTrialbalanceRequest](../../models/operations/getaccountingtrialbalancerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingTrialbalanceResponse](../../models/operations/getaccountingtrialbalanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_vendorcredit

Retrieve a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingVendorcredit" method="get" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.get_accounting_vendorcredit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingVendorcreditRequest](../../models/operations/getaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingVendorcreditResponse](../../models/operations/getaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_accounts

List all accounts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingAccounts" method="get" path="/accounting/{connection_id}/account" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_accounts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_accounts is not None

    # Handle response
    print(res.accounting_accounts)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingAccountsRequest](../../models/operations/listaccountingaccountsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingAccountsResponse](../../models/operations/listaccountingaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_agedpayables

List all agedpayables

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingAgedpayables" method="get" path="/accounting/{connection_id}/agedpayable" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_agedpayables(request={
        "connection_id": "<id>",
    })

    assert res.accounting_agedpayables is not None

    # Handle response
    print(res.accounting_agedpayables)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingAgedpayablesRequest](../../models/operations/listaccountingagedpayablesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingAgedpayablesResponse](../../models/operations/listaccountingagedpayablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_agedreceivables

List all agedreceivables

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingAgedreceivables" method="get" path="/accounting/{connection_id}/agedreceivable" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_agedreceivables(request={
        "connection_id": "<id>",
    })

    assert res.accounting_agedreceivables is not None

    # Handle response
    print(res.accounting_agedreceivables)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.ListAccountingAgedreceivablesRequest](../../models/operations/listaccountingagedreceivablesrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.ListAccountingAgedreceivablesResponse](../../models/operations/listaccountingagedreceivablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_balancesheets

List all balancesheets

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBalancesheets" method="get" path="/accounting/{connection_id}/balancesheet" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_balancesheets(request={
        "connection_id": "<id>",
    })

    assert res.accounting_balancesheets is not None

    # Handle response
    print(res.accounting_balancesheets)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingBalancesheetsRequest](../../models/operations/listaccountingbalancesheetsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingBalancesheetsResponse](../../models/operations/listaccountingbalancesheetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_bankfeedaccounts

List all bankfeedaccounts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBankfeedaccounts" method="get" path="/accounting/{connection_id}/bankfeedaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_bankfeedaccounts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedaccounts is not None

    # Handle response
    print(res.accounting_bankfeedaccounts)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.ListAccountingBankfeedaccountsRequest](../../models/operations/listaccountingbankfeedaccountsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.ListAccountingBankfeedaccountsResponse](../../models/operations/listaccountingbankfeedaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_bankfeedtransactions

List all bankfeedtransactions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBankfeedtransactions" method="get" path="/accounting/{connection_id}/bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_bankfeedtransactions(request={
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedtransactions is not None

    # Handle response
    print(res.accounting_bankfeedtransactions)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.ListAccountingBankfeedtransactionsRequest](../../models/operations/listaccountingbankfeedtransactionsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.ListAccountingBankfeedtransactionsResponse](../../models/operations/listaccountingbankfeedtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_bills

List all bills

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBills" method="get" path="/accounting/{connection_id}/bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_bills(request={
        "connection_id": "<id>",
    })

    assert res.accounting_bills is not None

    # Handle response
    print(res.accounting_bills)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAccountingBillsRequest](../../models/operations/listaccountingbillsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAccountingBillsResponse](../../models/operations/listaccountingbillsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_cashflows

List all cashflows

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCashflows" method="get" path="/accounting/{connection_id}/cashflow" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_cashflows(request={
        "connection_id": "<id>",
    })

    assert res.accounting_cashflows is not None

    # Handle response
    print(res.accounting_cashflows)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingCashflowsRequest](../../models/operations/listaccountingcashflowsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAccountingCashflowsResponse](../../models/operations/listaccountingcashflowsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_categories

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCategories" method="get" path="/accounting/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_categories(request={
        "connection_id": "<id>",
    })

    assert res.accounting_categories is not None

    # Handle response
    print(res.accounting_categories)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListAccountingCategoriesRequest](../../models/operations/listaccountingcategoriesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListAccountingCategoriesResponse](../../models/operations/listaccountingcategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_contacts

List all contacts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingContacts" method="get" path="/accounting/{connection_id}/contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_contacts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_contacts is not None

    # Handle response
    print(res.accounting_contacts)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingContactsRequest](../../models/operations/listaccountingcontactsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingContactsResponse](../../models/operations/listaccountingcontactsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_creditmemoes

List all creditmemoes

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCreditmemoes" method="get" path="/accounting/{connection_id}/creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_creditmemoes(request={
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemoes is not None

    # Handle response
    print(res.accounting_creditmemoes)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingCreditmemoesRequest](../../models/operations/listaccountingcreditmemoesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingCreditmemoesResponse](../../models/operations/listaccountingcreditmemoesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_expensereports

List all expensereports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingExpensereports" method="get" path="/accounting/{connection_id}/expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_expensereports(request={
        "connection_id": "<id>",
    })

    assert res.accounting_expensereports is not None

    # Handle response
    print(res.accounting_expensereports)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingExpensereportsRequest](../../models/operations/listaccountingexpensereportsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.ListAccountingExpensereportsResponse](../../models/operations/listaccountingexpensereportsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_expenses

List all expenses

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingExpenses" method="get" path="/accounting/{connection_id}/expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_expenses(request={
        "connection_id": "<id>",
    })

    assert res.accounting_expenses is not None

    # Handle response
    print(res.accounting_expenses)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingExpensesRequest](../../models/operations/listaccountingexpensesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingExpensesResponse](../../models/operations/listaccountingexpensesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_invoices

List all invoices

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingInvoices" method="get" path="/accounting/{connection_id}/invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_invoices(request={
        "connection_id": "<id>",
    })

    assert res.accounting_invoices is not None

    # Handle response
    print(res.accounting_invoices)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingInvoicesRequest](../../models/operations/listaccountinginvoicesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingInvoicesResponse](../../models/operations/listaccountinginvoicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_journals

List all journals

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingJournals" method="get" path="/accounting/{connection_id}/journal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_journals(request={
        "connection_id": "<id>",
    })

    assert res.accounting_journals is not None

    # Handle response
    print(res.accounting_journals)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingJournalsRequest](../../models/operations/listaccountingjournalsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingJournalsResponse](../../models/operations/listaccountingjournalsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_orders

List all orders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrders" method="get" path="/accounting/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_orders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_orders is not None

    # Handle response
    print(res.accounting_orders)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAccountingOrdersRequest](../../models/operations/listaccountingordersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAccountingOrdersResponse](../../models/operations/listaccountingordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_organizations

List all organizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrganizations" method="get" path="/accounting/{connection_id}/organization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_organizations(request={
        "connection_id": "<id>",
    })

    assert res.accounting_organizations is not None

    # Handle response
    print(res.accounting_organizations)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingOrganizationsRequest](../../models/operations/listaccountingorganizationsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingOrganizationsResponse](../../models/operations/listaccountingorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_paymentterms

List all paymentterms

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingPaymentterms" method="get" path="/accounting/{connection_id}/paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_paymentterms(request={
        "connection_id": "<id>",
    })

    assert res.accounting_paymentterms is not None

    # Handle response
    print(res.accounting_paymentterms)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingPaymenttermsRequest](../../models/operations/listaccountingpaymenttermsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingPaymenttermsResponse](../../models/operations/listaccountingpaymenttermsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_profitlosses

List all profitlosses

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingProfitlosses" method="get" path="/accounting/{connection_id}/profitloss" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_profitlosses(request={
        "connection_id": "<id>",
    })

    assert res.accounting_profitlosses is not None

    # Handle response
    print(res.accounting_profitlosses)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingProfitlossesRequest](../../models/operations/listaccountingprofitlossesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingProfitlossesResponse](../../models/operations/listaccountingprofitlossesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_projects

List all projects

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingProjects" method="get" path="/accounting/{connection_id}/project" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_projects(request={
        "connection_id": "<id>",
    })

    assert res.accounting_projects is not None

    # Handle response
    print(res.accounting_projects)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingProjectsRequest](../../models/operations/listaccountingprojectsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingProjectsResponse](../../models/operations/listaccountingprojectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_purchaseorders

List all purchaseorders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingPurchaseorders" method="get" path="/accounting/{connection_id}/purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_purchaseorders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_purchaseorders is not None

    # Handle response
    print(res.accounting_purchaseorders)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingPurchaseordersRequest](../../models/operations/listaccountingpurchaseordersrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.ListAccountingPurchaseordersResponse](../../models/operations/listaccountingpurchaseordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_purchasereceipts

List all purchasereceipts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingPurchasereceipts" method="get" path="/accounting/{connection_id}/purchasereceipt" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_purchasereceipts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_purchasereceipts is not None

    # Handle response
    print(res.accounting_purchasereceipts)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.ListAccountingPurchasereceiptsRequest](../../models/operations/listaccountingpurchasereceiptsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.ListAccountingPurchasereceiptsResponse](../../models/operations/listaccountingpurchasereceiptsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_quotes

List all quotes

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingQuotes" method="get" path="/accounting/{connection_id}/quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_quotes(request={
        "connection_id": "<id>",
    })

    assert res.accounting_quotes is not None

    # Handle response
    print(res.accounting_quotes)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAccountingQuotesRequest](../../models/operations/listaccountingquotesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAccountingQuotesResponse](../../models/operations/listaccountingquotesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_salesorders

List all salesorders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingSalesorders" method="get" path="/accounting/{connection_id}/salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_salesorders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_salesorders is not None

    # Handle response
    print(res.accounting_salesorders)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListAccountingSalesordersRequest](../../models/operations/listaccountingsalesordersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListAccountingSalesordersResponse](../../models/operations/listaccountingsalesordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_salesreceipts

List all salesreceipts

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingSalesreceipts" method="get" path="/accounting/{connection_id}/salesreceipt" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_salesreceipts(request={
        "connection_id": "<id>",
    })

    assert res.accounting_salesreceipts is not None

    # Handle response
    print(res.accounting_salesreceipts)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingSalesreceiptsRequest](../../models/operations/listaccountingsalesreceiptsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingSalesreceiptsResponse](../../models/operations/listaccountingsalesreceiptsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_taxrates

List all taxrates

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingTaxrates" method="get" path="/accounting/{connection_id}/taxrate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_taxrates(request={
        "connection_id": "<id>",
    })

    assert res.accounting_taxrates is not None

    # Handle response
    print(res.accounting_taxrates)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingTaxratesRequest](../../models/operations/listaccountingtaxratesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingTaxratesResponse](../../models/operations/listaccountingtaxratesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_transactions

List all transactions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingTransactions" method="get" path="/accounting/{connection_id}/transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_transactions(request={
        "connection_id": "<id>",
    })

    assert res.accounting_transactions is not None

    # Handle response
    print(res.accounting_transactions)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingTransactionsRequest](../../models/operations/listaccountingtransactionsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingTransactionsResponse](../../models/operations/listaccountingtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_trialbalances

List all trialbalances

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingTrialbalances" method="get" path="/accounting/{connection_id}/trialbalance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_trialbalances(request={
        "connection_id": "<id>",
    })

    assert res.accounting_trialbalances is not None

    # Handle response
    print(res.accounting_trialbalances)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingTrialbalancesRequest](../../models/operations/listaccountingtrialbalancesrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingTrialbalancesResponse](../../models/operations/listaccountingtrialbalancesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_vendorcredits

List all vendorcredits

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingVendorcredits" method="get" path="/accounting/{connection_id}/vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.list_accounting_vendorcredits(request={
        "connection_id": "<id>",
    })

    assert res.accounting_vendorcredits is not None

    # Handle response
    print(res.accounting_vendorcredits)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingVendorcreditsRequest](../../models/operations/listaccountingvendorcreditsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingVendorcreditsResponse](../../models/operations/listaccountingvendorcreditsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_account

Update an account

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingAccount" method="patch" path="/accounting/{connection_id}/account/{id}" example="accounting_account" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_account(request={
        "accounting_account": {
            "balance": 12092.0,
            "created_at": parse_datetime("2022-07-03T17:57:07.391Z"),
            "currency": "CAD",
            "customer_defined_code": "6170",
            "description": "Voluptatibus valde spoliatio.",
            "id": "13be529a-44a9-4a3f-8475-76174d49f7c6",
            "is_payable": False,
            "metadata": [],
            "name": "Auto Loan Account",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vilitas",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "comedo",
                },
            ],
            "type": shared.Type.ACCOUNTS_RECEIVABLE,
            "updated_at": parse_datetime("2023-08-06T14:16:21.006Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingAccountRequest](../../models/operations/patchaccountingaccountrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingAccountResponse](../../models/operations/patchaccountingaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_bankfeedaccount

Update a bankfeedaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingBankfeedaccount" method="patch" path="/accounting/{connection_id}/bankfeedaccount/{id}" example="accounting_bankfeedaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_bankfeedaccount(request={
        "accounting_bankfeedaccount": {
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 49437.0,
            "bank_name": "Wells Fargo",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "AUD",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "70525a7d-7350-4eea-b656-95e1dfe49102",
            "metadata": [],
            "name": "Corwin, Donnelly and Connelly Checking",
            "routing_number": "694667752",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-23T09:05:03.291Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedaccount is not None

    # Handle response
    print(res.accounting_bankfeedaccount)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchAccountingBankfeedaccountRequest](../../models/operations/patchaccountingbankfeedaccountrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.PatchAccountingBankfeedaccountResponse](../../models/operations/patchaccountingbankfeedaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_bankfeedtransaction

Update a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingBankfeedtransaction" method="patch" path="/accounting/{connection_id}/bankfeedtransaction/{id}" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "aa56f908-811c-48fc-915b-6c8d0452b7c6",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T00:29:08.620Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T05:56:55.061Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T00:40:43.176Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchAccountingBankfeedtransactionRequest](../../models/operations/patchaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.PatchAccountingBankfeedtransactionResponse](../../models/operations/patchaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_bill

Update a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingBill" method="patch" path="/accounting/{connection_id}/bill/{id}" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_bill(request={
        "accounting_bill": {
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "42f3ac3e-f2a1-4575-ab78-43217258a0a0",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "71d10b5f-2cb9-4a88-971b-f4544b40760e",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "70dbb13d-e258-4e51-9ea6-934bcc65b8e9",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T02:34:30.096Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchAccountingBillRequest](../../models/operations/patchaccountingbillrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchAccountingBillResponse](../../models/operations/patchaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCategory" method="patch" path="/accounting/{connection_id}/category/{id}" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Textus ab thymum labore basium.",
            "id": "89d2a833-46c0-4d58-8a7e-962b786f409f",
            "is_active": False,
            "metadata": [],
            "name": "Beauty",
            "updated_at": parse_datetime("2025-09-10T16:32:55.231Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingCategoryRequest](../../models/operations/patchaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchAccountingCategoryResponse](../../models/operations/patchaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingContact" method="patch" path="/accounting/{connection_id}/contact/{id}" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "c68927a3-7321-4c55-9a75-c9e203870e52",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "57d6ffc5-f8d4-40da-8c97-5568f8253ff7",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.543Z"),
            "website": "https://kertzmanngroup.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingContactRequest](../../models/operations/patchaccountingcontactrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingContactResponse](../../models/operations/patchaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_creditmemo

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCreditmemo" method="patch" path="/accounting/{connection_id}/creditmemo/{id}" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "CM-99537",
            "currency": "AUD",
            "discount_amount": 0.0,
            "id": "7980681f-d8b6-48c2-aeab-8cf43c995426",
            "lineitems": [],
            "metadata": [],
            "notes": "Hic vorax dedecor amo adfero torqueo quas victoria.",
            "posted_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "send": True,
            "status": shared.AccountingCreditmemoStatus.AUTHORIZED,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-09-10T13:16:31.922Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAccountingCreditmemoRequest](../../models/operations/patchaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchAccountingCreditmemoResponse](../../models/operations/patchaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingExpense" method="patch" path="/accounting/{connection_id}/expense/{id}" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_expense(request={
        "accounting_expense": {
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "d9d99770-2edb-47a1-ac05-67cfa16f1b38",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "a14ba52a-ed88-4798-952c-f4fc425cd0a6",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "1f9bf42d-dc72-48e3-ab6a-0d7556f21ccb",
            "lineitems": [
                {
                    "id": "1dbd0778-6dc3-41a9-aa2c-fc8468dae2fa",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "ad08ef21-7355-4b7f-9c15-4652bb9e12b1",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "58d1ee89-4b77-4267-8567-946af153bbd6",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "c02af0d6-46f6-462b-a69f-1ac89f81c97c",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "64d7bebe-a45b-45f0-835c-cee30f03a25c",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-02T06:14:35.956Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingExpenseRequest](../../models/operations/patchaccountingexpenserequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingExpenseResponse](../../models/operations/patchaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_expensereport

Update an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingExpensereport" method="patch" path="/accounting/{connection_id}/expensereport/{id}" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T07:25:37.097Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "72bbbb02-bf43-48b3-a69d-b7d1cee6711a",
            "lineitems": [
                {
                    "id": "03097e5a-aa7c-4d29-b4d7-ce3dd19e2f22",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "7f86c87e-6aa7-405f-b495-b787c3f56085",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "6a160452-4868-4785-8b62-b6d408639126",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "d3ba215c-aa2e-4b50-9f62-797b2bf9411e",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T07:25:37.097Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T07:25:37.097Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchAccountingExpensereportRequest](../../models/operations/patchaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.PatchAccountingExpensereportResponse](../../models/operations/patchaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_invoice

Update an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingInvoice" method="patch" path="/accounting/{connection_id}/invoice/{id}" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "006151f7-80b7-4518-b99e-e80b04371d6c",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "573d811c-1568-474b-91c0-933d15fbc79b",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "3574403c-70e2-4b2d-aa22-fee93ea54fb9",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-22T11:33:30.972Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingInvoiceRequest](../../models/operations/patchaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingInvoiceResponse](../../models/operations/patchaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_journal

Update a journal

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingJournal" method="patch" path="/accounting/{connection_id}/journal/{id}" example="accounting_journal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_journal(request={
        "accounting_journal": {
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-02-20T15:14:55.881Z"),
            "currency": "CAD",
            "description": "Cilicium minima calco constans adipisci.",
            "id": "4e3db2c0-346e-494d-b2b9-5e710ea2d464",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2023-11-05T18:27:35.629Z"),
            "reference": "JE-78884",
            "source": "crustulum",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-10T11:27:02.612Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_journal is not None

    # Handle response
    print(res.accounting_journal)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingJournalRequest](../../models/operations/patchaccountingjournalrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingJournalResponse](../../models/operations/patchaccountingjournalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_order

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingOrder" method="patch" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "9cfbbc55-852e-40c0-bcf8-0ce527e203b5",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T01:18:36.560Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAccountingOrderRequest](../../models/operations/patchaccountingorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAccountingOrderResponse](../../models/operations/patchaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_paymentterm

Update a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingPaymentterm" method="patch" path="/accounting/{connection_id}/paymentterm/{id}" example="accounting_paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_paymentterm(request={
        "accounting_paymentterm": {
            "category": shared.Category.STANDARD,
            "created_at": parse_datetime("2021-08-22T22:42:42.265Z"),
            "day_of_month_due": 4.0,
            "description": "Cogito pecco eos cultura.",
            "discount_day_of_month": 13.0,
            "discount_days": 4.0,
            "discount_percent": 5.0,
            "due_days": 57.0,
            "due_next_month_days": 9.0,
            "id": "4400719a-265b-483c-a655-f757d7bcc8d4",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-07T10:28:50.062Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAccountingPaymenttermRequest](../../models/operations/patchaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.PatchAccountingPaymenttermResponse](../../models/operations/patchaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_project

Update a project

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingProject" method="patch" path="/accounting/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_project(request={
        "accounting_project": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_project is not None

    # Handle response
    print(res.accounting_project)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingProjectRequest](../../models/operations/patchaccountingprojectrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingProjectResponse](../../models/operations/patchaccountingprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_purchaseorder

Update a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingPurchaseorder" method="patch" path="/accounting/{connection_id}/purchaseorder/{id}" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "attachments": [],
            "billing_address": {
                "address1": "72142 Willow Street",
                "address2": "Apt. 967",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "FL",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "EUR",
            "id": "277cf34b-95f2-4480-8c9b-7f6628222ac6",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "shipping_address": {
                "address1": "76494 Medhurst Club",
                "city": "Kshlerinfurt",
                "country_code": "US",
                "postal_code": "92116-5474",
                "region": "Oregon",
                "region_code": "WY",
            },
            "status": shared.AccountingPurchaseorderStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-08-11T02:42:33.400Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchAccountingPurchaseorderRequest](../../models/operations/patchaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.PatchAccountingPurchaseorderResponse](../../models/operations/patchaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_quote

Update a quote

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingQuote" method="patch" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAccountingQuoteRequest](../../models/operations/patchaccountingquoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAccountingQuoteResponse](../../models/operations/patchaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_salesorder

Update a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingSalesorder" method="patch" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T05:42:39.602Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "08ce3fda-9749-4d82-b421-52c25901ae51",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T05:42:39.602Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAccountingSalesorderRequest](../../models/operations/patchaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchAccountingSalesorderResponse](../../models/operations/patchaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_taxrate

Update a taxrate

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingTaxrate" method="patch" path="/accounting/{connection_id}/taxrate/{id}" example="accounting_taxrate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_taxrate(request={
        "accounting_taxrate": {
            "components": [
                {
                    "is_compound": False,
                    "name": "Exempt",
                    "rate": 0.0,
                },
            ],
            "country": "US",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Exempt (0%)",
            "effective_rate": 0.0,
            "id": "f4b92b54-4f02-49c5-a56b-a7901ca117b5",
            "is_active": False,
            "is_compound": False,
            "metadata": [],
            "name": "Exempt",
            "rate": 0.0,
            "region": "KS",
            "total_rate": 0.0,
            "type": shared.AccountingTaxrateType.SALES,
            "updated_at": parse_datetime("2020-02-13T04:41:49.452Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_taxrate is not None

    # Handle response
    print(res.accounting_taxrate)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingTaxrateRequest](../../models/operations/patchaccountingtaxraterequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingTaxrateResponse](../../models/operations/patchaccountingtaxrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_transaction

Update a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingTransaction" method="patch" path="/accounting/{connection_id}/transaction/{id}" example="accounting_transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_transaction(request={
        "accounting_transaction": {
            "created_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "id": "750d5e43-7689-42b0-9976-ec929d1a3e48",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The turquoise Hat combines Wallis and Futuna aesthetics with Potassium-based durability",
                    "id": "d04fc8a8-3ba8-4ccb-9501-86287c8a50a3",
                    "name": "Shirt",
                    "total_amount": 10184.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 19.0,
                },
            ],
            "memo": "deposit of ISK 792.81 at Fritsch - Dooley charged to account ending in 7879 using card ending in ****3230.",
            "status": shared.AccountingTransactionStatus.PENDING,
            "tax_amount": 0.0,
            "total_amount": 10184.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2019-10-14T05:55:46.797Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAccountingTransactionRequest](../../models/operations/patchaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.PatchAccountingTransactionResponse](../../models/operations/patchaccountingtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_vendorcredit

Update a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingVendorcredit" method="patch" path="/accounting/{connection_id}/vendorcredit/{id}" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.patch_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "cbc5956d-066c-435a-a65a-2f6e9f858d97",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-02T21:50:25.789Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchAccountingVendorcreditRequest](../../models/operations/patchaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.PatchAccountingVendorcreditResponse](../../models/operations/patchaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_account

Remove an account

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingAccount" method="delete" path="/accounting/{connection_id}/account/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_account(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingAccountRequest](../../models/operations/removeaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingAccountResponse](../../models/operations/removeaccountingaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_bankfeedaccount

Remove a bankfeedaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingBankfeedaccount" method="delete" path="/accounting/{connection_id}/bankfeedaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_bankfeedaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.RemoveAccountingBankfeedaccountRequest](../../models/operations/removeaccountingbankfeedaccountrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.RemoveAccountingBankfeedaccountResponse](../../models/operations/removeaccountingbankfeedaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_bankfeedtransaction

Remove a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingBankfeedtransaction" method="delete" path="/accounting/{connection_id}/bankfeedtransaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_bankfeedtransaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.RemoveAccountingBankfeedtransactionRequest](../../models/operations/removeaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.RemoveAccountingBankfeedtransactionResponse](../../models/operations/removeaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_bill

Remove a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingBill" method="delete" path="/accounting/{connection_id}/bill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_bill(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveAccountingBillRequest](../../models/operations/removeaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveAccountingBillResponse](../../models/operations/removeaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_category

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCategory" method="delete" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingCategoryRequest](../../models/operations/removeaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveAccountingCategoryResponse](../../models/operations/removeaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_contact

Remove a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingContact" method="delete" path="/accounting/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingContactRequest](../../models/operations/removeaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingContactResponse](../../models/operations/removeaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_creditmemo

Remove a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCreditmemo" method="delete" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_creditmemo(request={
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
| `request`                                                                                                    | [operations.RemoveAccountingCreditmemoRequest](../../models/operations/removeaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveAccountingCreditmemoResponse](../../models/operations/removeaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_expense

Remove an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingExpense" method="delete" path="/accounting/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingExpenseRequest](../../models/operations/removeaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingExpenseResponse](../../models/operations/removeaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_expensereport

Remove an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingExpensereport" method="delete" path="/accounting/{connection_id}/expensereport/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_expensereport(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.RemoveAccountingExpensereportRequest](../../models/operations/removeaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.RemoveAccountingExpensereportResponse](../../models/operations/removeaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_invoice

Remove an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingInvoice" method="delete" path="/accounting/{connection_id}/invoice/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_invoice(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingInvoiceRequest](../../models/operations/removeaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingInvoiceResponse](../../models/operations/removeaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_journal

Remove a journal

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingJournal" method="delete" path="/accounting/{connection_id}/journal/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_journal(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingJournalRequest](../../models/operations/removeaccountingjournalrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingJournalResponse](../../models/operations/removeaccountingjournalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_order

Remove an order

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingOrder" method="delete" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_order(request={
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
| `request`                                                                                          | [operations.RemoveAccountingOrderRequest](../../models/operations/removeaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountingOrderResponse](../../models/operations/removeaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_paymentterm

Remove a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingPaymentterm" method="delete" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_paymentterm(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveAccountingPaymenttermRequest](../../models/operations/removeaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveAccountingPaymenttermResponse](../../models/operations/removeaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_project

Remove a project

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingProject" method="delete" path="/accounting/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_project(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingProjectRequest](../../models/operations/removeaccountingprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingProjectResponse](../../models/operations/removeaccountingprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_purchaseorder

Remove a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingPurchaseorder" method="delete" path="/accounting/{connection_id}/purchaseorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_purchaseorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.RemoveAccountingPurchaseorderRequest](../../models/operations/removeaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.RemoveAccountingPurchaseorderResponse](../../models/operations/removeaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_quote

Remove a quote

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingQuote" method="delete" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_quote(request={
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
| `request`                                                                                          | [operations.RemoveAccountingQuoteRequest](../../models/operations/removeaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountingQuoteResponse](../../models/operations/removeaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_salesorder

Remove a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingSalesorder" method="delete" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_salesorder(request={
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
| `request`                                                                                                    | [operations.RemoveAccountingSalesorderRequest](../../models/operations/removeaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveAccountingSalesorderResponse](../../models/operations/removeaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_taxrate

Remove a taxrate

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingTaxrate" method="delete" path="/accounting/{connection_id}/taxrate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_taxrate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingTaxrateRequest](../../models/operations/removeaccountingtaxraterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingTaxrateResponse](../../models/operations/removeaccountingtaxrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_transaction

Remove a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingTransaction" method="delete" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_transaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveAccountingTransactionRequest](../../models/operations/removeaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveAccountingTransactionResponse](../../models/operations/removeaccountingtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_vendorcredit

Remove a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingVendorcredit" method="delete" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.remove_accounting_vendorcredit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.RemoveAccountingVendorcreditRequest](../../models/operations/removeaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.RemoveAccountingVendorcreditResponse](../../models/operations/removeaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_account

Update an account

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingAccount" method="put" path="/accounting/{connection_id}/account/{id}" example="accounting_account" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_account(request={
        "accounting_account": {
            "balance": 12092.0,
            "created_at": parse_datetime("2022-07-03T17:57:07.391Z"),
            "currency": "CAD",
            "customer_defined_code": "6170",
            "description": "Voluptatibus valde spoliatio.",
            "id": "13be529a-44a9-4a3f-8475-76174d49f7c6",
            "is_payable": False,
            "metadata": [],
            "name": "Auto Loan Account",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vilitas",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "comedo",
                },
            ],
            "type": shared.Type.ACCOUNTS_RECEIVABLE,
            "updated_at": parse_datetime("2023-08-06T14:16:21.006Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingAccountRequest](../../models/operations/updateaccountingaccountrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingAccountResponse](../../models/operations/updateaccountingaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_bankfeedaccount

Update a bankfeedaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingBankfeedaccount" method="put" path="/accounting/{connection_id}/bankfeedaccount/{id}" example="accounting_bankfeedaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_bankfeedaccount(request={
        "accounting_bankfeedaccount": {
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 49437.0,
            "bank_name": "Wells Fargo",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "AUD",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "70525a7d-7350-4eea-b656-95e1dfe49102",
            "metadata": [],
            "name": "Corwin, Donnelly and Connelly Checking",
            "routing_number": "694667752",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-23T09:05:03.291Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedaccount is not None

    # Handle response
    print(res.accounting_bankfeedaccount)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.UpdateAccountingBankfeedaccountRequest](../../models/operations/updateaccountingbankfeedaccountrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.UpdateAccountingBankfeedaccountResponse](../../models/operations/updateaccountingbankfeedaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_bankfeedtransaction

Update a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingBankfeedtransaction" method="put" path="/accounting/{connection_id}/bankfeedtransaction/{id}" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "aa56f908-811c-48fc-915b-6c8d0452b7c6",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T00:29:08.620Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T05:56:55.061Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T00:40:43.176Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.UpdateAccountingBankfeedtransactionRequest](../../models/operations/updateaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.UpdateAccountingBankfeedtransactionResponse](../../models/operations/updateaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_bill

Update a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingBill" method="put" path="/accounting/{connection_id}/bill/{id}" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_bill(request={
        "accounting_bill": {
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "42f3ac3e-f2a1-4575-ab78-43217258a0a0",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "71d10b5f-2cb9-4a88-971b-f4544b40760e",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "70dbb13d-e258-4e51-9ea6-934bcc65b8e9",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T02:34:30.096Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateAccountingBillRequest](../../models/operations/updateaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateAccountingBillResponse](../../models/operations/updateaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCategory" method="put" path="/accounting/{connection_id}/category/{id}" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Textus ab thymum labore basium.",
            "id": "89d2a833-46c0-4d58-8a7e-962b786f409f",
            "is_active": False,
            "metadata": [],
            "name": "Beauty",
            "updated_at": parse_datetime("2025-09-10T16:32:55.231Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingCategoryRequest](../../models/operations/updateaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateAccountingCategoryResponse](../../models/operations/updateaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_contact

Update a contact

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingContact" method="put" path="/accounting/{connection_id}/contact/{id}" example="accounting_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_contact(request={
        "accounting_contact": {
            "associated_contacts": [],
            "balance_amount": 55574.0,
            "billing_address": {
                "address1": "4091 Tromp Coves",
                "city": "Lake Emmybury",
                "country_code": "US",
                "postal_code": "50764-5226",
                "region": "Washington",
                "region_code": "CA",
            },
            "company_name": "Kertzmann Group",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "AUD",
            "emails": [
                {
                    "email": "delores.reynolds@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.WORK,
                },
                {
                    "email": "accounts@kertzmanngroup.com",
                    "type": shared.AccountingEmailType.OTHER,
                },
            ],
            "first_name": "Delores",
            "id": "c68927a3-7321-4c55-9a75-c9e203870e52",
            "identification": "531850872",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "metadata": [],
            "name": "Kertzmann Group",
            "notes": "Et videlicet pauci.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "57d6ffc5-f8d4-40da-8c97-5568f8253ff7",
                    "name": "Visa 7844",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://kertzmanngroup.com/billing",
            "shipping_address": {
                "address1": "23129 Rebekah Mews",
                "city": "Mortimerhaven",
                "country_code": "US",
                "postal_code": "55878-6806",
                "region": "Florida",
                "region_code": "OK",
            },
            "tax_exemption": shared.TaxExemption.FOREIGN,
            "tax_number": "867556410",
            "telephones": [
                {
                    "telephone": "(432) 760-1716",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-19T07:40:07.543Z"),
            "website": "https://kertzmanngroup.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_contact is not None

    # Handle response
    print(res.accounting_contact)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingContactRequest](../../models/operations/updateaccountingcontactrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingContactResponse](../../models/operations/updateaccountingcontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_creditmemo

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCreditmemo" method="put" path="/accounting/{connection_id}/creditmemo/{id}" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "CM-99537",
            "currency": "AUD",
            "discount_amount": 0.0,
            "id": "7980681f-d8b6-48c2-aeab-8cf43c995426",
            "lineitems": [],
            "metadata": [],
            "notes": "Hic vorax dedecor amo adfero torqueo quas victoria.",
            "posted_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "send": True,
            "status": shared.AccountingCreditmemoStatus.AUTHORIZED,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-09-10T13:16:31.922Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateAccountingCreditmemoRequest](../../models/operations/updateaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateAccountingCreditmemoResponse](../../models/operations/updateaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingExpense" method="put" path="/accounting/{connection_id}/expense/{id}" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_expense(request={
        "accounting_expense": {
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "d9d99770-2edb-47a1-ac05-67cfa16f1b38",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "a14ba52a-ed88-4798-952c-f4fc425cd0a6",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "1f9bf42d-dc72-48e3-ab6a-0d7556f21ccb",
            "lineitems": [
                {
                    "id": "1dbd0778-6dc3-41a9-aa2c-fc8468dae2fa",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "ad08ef21-7355-4b7f-9c15-4652bb9e12b1",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "58d1ee89-4b77-4267-8567-946af153bbd6",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "c02af0d6-46f6-462b-a69f-1ac89f81c97c",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "64d7bebe-a45b-45f0-835c-cee30f03a25c",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-02T06:14:35.956Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingExpenseRequest](../../models/operations/updateaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingExpenseResponse](../../models/operations/updateaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_expensereport

Update an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingExpensereport" method="put" path="/accounting/{connection_id}/expensereport/{id}" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T07:25:37.097Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "72bbbb02-bf43-48b3-a69d-b7d1cee6711a",
            "lineitems": [
                {
                    "id": "03097e5a-aa7c-4d29-b4d7-ce3dd19e2f22",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "7f86c87e-6aa7-405f-b495-b787c3f56085",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "6a160452-4868-4785-8b62-b6d408639126",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "d3ba215c-aa2e-4b50-9f62-797b2bf9411e",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T07:25:37.097Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T07:25:37.097Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateAccountingExpensereportRequest](../../models/operations/updateaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.UpdateAccountingExpensereportResponse](../../models/operations/updateaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_invoice

Update an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingInvoice" method="put" path="/accounting/{connection_id}/invoice/{id}" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "006151f7-80b7-4518-b99e-e80b04371d6c",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "573d811c-1568-474b-91c0-933d15fbc79b",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "3574403c-70e2-4b2d-aa22-fee93ea54fb9",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-22T11:33:30.972Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingInvoiceRequest](../../models/operations/updateaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingInvoiceResponse](../../models/operations/updateaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_journal

Update a journal

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingJournal" method="put" path="/accounting/{connection_id}/journal/{id}" example="accounting_journal" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_journal(request={
        "accounting_journal": {
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-02-20T15:14:55.881Z"),
            "currency": "CAD",
            "description": "Cilicium minima calco constans adipisci.",
            "id": "4e3db2c0-346e-494d-b2b9-5e710ea2d464",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2023-11-05T18:27:35.629Z"),
            "reference": "JE-78884",
            "source": "crustulum",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-10T11:27:02.612Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_journal is not None

    # Handle response
    print(res.accounting_journal)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingJournalRequest](../../models/operations/updateaccountingjournalrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingJournalResponse](../../models/operations/updateaccountingjournalresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_order

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingOrder" method="put" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "7654 Treutel Square",
                "city": "Forrestport",
                "country_code": "US",
                "postal_code": "42190-3694",
                "region": "Maine",
                "region_code": "OR",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "9cfbbc55-852e-40c0-bcf8-0ce527e203b5",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "4974 Beatty Corners",
                "city": "Alizeport",
                "country_code": "US",
                "postal_code": "56252",
                "region": "Alaska",
                "region_code": "VT",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-08T01:18:36.560Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountingOrderRequest](../../models/operations/updateaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAccountingOrderResponse](../../models/operations/updateaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_paymentterm

Update a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingPaymentterm" method="put" path="/accounting/{connection_id}/paymentterm/{id}" example="accounting_paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_paymentterm(request={
        "accounting_paymentterm": {
            "category": shared.Category.STANDARD,
            "created_at": parse_datetime("2021-08-22T22:42:42.265Z"),
            "day_of_month_due": 4.0,
            "description": "Cogito pecco eos cultura.",
            "discount_day_of_month": 13.0,
            "discount_days": 4.0,
            "discount_percent": 5.0,
            "due_days": 57.0,
            "due_next_month_days": 9.0,
            "id": "4400719a-265b-483c-a655-f757d7bcc8d4",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-07T10:28:50.062Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateAccountingPaymenttermRequest](../../models/operations/updateaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.UpdateAccountingPaymenttermResponse](../../models/operations/updateaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_project

Update a project

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingProject" method="put" path="/accounting/{connection_id}/project/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_project(request={
        "accounting_project": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_project is not None

    # Handle response
    print(res.accounting_project)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingProjectRequest](../../models/operations/updateaccountingprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingProjectResponse](../../models/operations/updateaccountingprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_purchaseorder

Update a purchaseorder

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingPurchaseorder" method="put" path="/accounting/{connection_id}/purchaseorder/{id}" example="accounting_purchaseorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_purchaseorder(request={
        "accounting_purchaseorder": {
            "attachments": [],
            "billing_address": {
                "address1": "72142 Willow Street",
                "address2": "Apt. 967",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "FL",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "EUR",
            "id": "277cf34b-95f2-4480-8c9b-7f6628222ac6",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "shipping_address": {
                "address1": "76494 Medhurst Club",
                "city": "Kshlerinfurt",
                "country_code": "US",
                "postal_code": "92116-5474",
                "region": "Oregon",
                "region_code": "WY",
            },
            "status": shared.AccountingPurchaseorderStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-08-11T02:42:33.400Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_purchaseorder is not None

    # Handle response
    print(res.accounting_purchaseorder)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateAccountingPurchaseorderRequest](../../models/operations/updateaccountingpurchaseorderrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.UpdateAccountingPurchaseorderResponse](../../models/operations/updateaccountingpurchaseorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_quote

Update a quote

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingQuote" method="put" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountingQuoteRequest](../../models/operations/updateaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAccountingQuoteResponse](../../models/operations/updateaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_salesorder

Update a salesorder

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingSalesorder" method="put" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T05:42:39.602Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "08ce3fda-9749-4d82-b421-52c25901ae51",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T05:42:39.602Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateAccountingSalesorderRequest](../../models/operations/updateaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateAccountingSalesorderResponse](../../models/operations/updateaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_taxrate

Update a taxrate

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingTaxrate" method="put" path="/accounting/{connection_id}/taxrate/{id}" example="accounting_taxrate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_taxrate(request={
        "accounting_taxrate": {
            "components": [
                {
                    "is_compound": False,
                    "name": "Exempt",
                    "rate": 0.0,
                },
            ],
            "country": "US",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Exempt (0%)",
            "effective_rate": 0.0,
            "id": "f4b92b54-4f02-49c5-a56b-a7901ca117b5",
            "is_active": False,
            "is_compound": False,
            "metadata": [],
            "name": "Exempt",
            "rate": 0.0,
            "region": "KS",
            "total_rate": 0.0,
            "type": shared.AccountingTaxrateType.SALES,
            "updated_at": parse_datetime("2020-02-13T04:41:49.452Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_taxrate is not None

    # Handle response
    print(res.accounting_taxrate)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingTaxrateRequest](../../models/operations/updateaccountingtaxraterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingTaxrateResponse](../../models/operations/updateaccountingtaxrateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_transaction

Update a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingTransaction" method="put" path="/accounting/{connection_id}/transaction/{id}" example="accounting_transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_transaction(request={
        "accounting_transaction": {
            "created_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "id": "750d5e43-7689-42b0-9976-ec929d1a3e48",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The turquoise Hat combines Wallis and Futuna aesthetics with Potassium-based durability",
                    "id": "d04fc8a8-3ba8-4ccb-9501-86287c8a50a3",
                    "name": "Shirt",
                    "total_amount": 10184.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 19.0,
                },
            ],
            "memo": "deposit of ISK 792.81 at Fritsch - Dooley charged to account ending in 7879 using card ending in ****3230.",
            "status": shared.AccountingTransactionStatus.PENDING,
            "tax_amount": 0.0,
            "total_amount": 10184.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2019-10-14T05:55:46.797Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateAccountingTransactionRequest](../../models/operations/updateaccountingtransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.UpdateAccountingTransactionResponse](../../models/operations/updateaccountingtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_vendorcredit

Update a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingVendorcredit" method="put" path="/accounting/{connection_id}/vendorcredit/{id}" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.update_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "cbc5956d-066c-435a-a65a-2f6e9f858d97",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-02T21:50:25.789Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateAccountingVendorcreditRequest](../../models/operations/updateaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.UpdateAccountingVendorcreditResponse](../../models/operations/updateaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |