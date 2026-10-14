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
            "currency": "BOB",
            "customer_defined_code": "quo",
            "description": "Spoliatio comedo vilitas harum cupiditate.",
            "id": "bcedab85-6b1d-4e1c-b18a-4a02c8b38289",
            "is_payable": True,
            "name": "Electronic Aluminum Tuna",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vesper",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "iste",
                },
                {
                    "original_type": "adamo",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "peccatus",
                },
            ],
            "type": shared.Type.BANK,
            "updated_at": parse_datetime("2023-01-06T05:16:44.338Z"),
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
            "account_id": "baa0e9a4-65e9-4bf5-856a-ce46fc36ebb1",
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 90358.0,
            "bank_name": "Weissnat Inc",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "SSP",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "81a79ff7-4cfa-4305-bfe7-e6f932a8edc0",
            "name": "Corwin, Donnelly and Connelly Savings",
            "routing_number": "667753156",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-21T04:15:03.213Z"),
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
            "account_id": "b7dc4175-1368-4b89-a700-d621b6666648",
            "amount": 60889.0,
            "bank_category": "Games",
            "bankfeedaccount_id": "34c1d05f-5b62-4bcd-9121-3be8b720941f",
            "category_ids": [],
            "contact_id": "1ef58ebe-f9c9-46f6-9d9c-2df2658503be",
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "SRD",
            "description": "payment transaction at McLaughlin - Schaden using card ending with ****8233 for DOP 574.03 in account ***9523.",
            "id": "6e656ff0-fd11-4bd4-b222-5f37dd96b362",
            "is_pending": True,
            "merchant_name": "Reichert, Erdman and Tillman",
            "posted_at": parse_datetime("2025-04-10T01:40:14.162Z"),
            "reference": "93642593",
            "transaction_at": parse_datetime("2022-07-29T19:08:12.792Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-24T19:29:33.908Z"),
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
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "084a27dc-db89-48af-89f9-f2148f065168",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-21T06:00:58.879Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-17T23:16:18.166Z"),
            "url": "https://coarse-interviewer.biz/",
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
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "5e3ba882-f95b-47af-a6db-b9554ff85bca",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-09-06T16:58:55.411Z"),
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
            "associated_contacts": [
                {
                    "id": "01827bf9-e87d-4ae6-a690-0971eba26a4c",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "2c84d544-063f-4126-af85-f289b4dfd93f",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "c342a755-ec47-4967-90d6-d6e7fe5c766c",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "239bd770-002b-4231-b161-a5bb855705c4",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-16T15:28:50.197Z"),
            "website": "https://noxious-advertisement.org",
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
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "5506de63-2029-4dca-8cb4-b2a6a9199df3",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "9e19f7ec-0489-4b68-a4b7-8dd9ea1ef880",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-12-04T02:04:50.609Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-25T13:24:34.132Z"),
            "url": "https://lighthearted-bandwidth.net/",
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
            "approved_at": parse_datetime("2026-06-03T03:51:40.838Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "51777b32-446a-4925-b2ac-4996fad19dc9",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "fcf74eb5-9ea2-45cd-983b-6c9abb6fbe01",
            "lineitems": [
                {
                    "id": "f39af1b6-9a5a-48aa-8b5e-80cc6c0689a8",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-08T06:10:48.698Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "type": shared.AccountingExpenseType.USER,
            "updated_at": parse_datetime("2026-06-03T03:51:40.838Z"),
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
            "approved_at": parse_datetime("2025-04-08T14:17:56.562Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "f4551530-294a-45c3-bcf3-8ac5d9cfe1f5",
            "lineitems": [
                {
                    "id": "ef024226-2cab-43cb-8321-92f69bb0c325",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "a387e30b-5922-4a35-9ac1-aa0547c66192",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-10-31T08:51:10.898Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-08T14:17:56.562Z"),
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
                    "id": "950a9348-f93f-4c44-93df-fa01d5635ad9",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "dba911f0-0502-49dc-a1d9-0d5769ab863a",
            "invoice_number": "vinco",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-04-18T14:46:04.006Z"),
            "reference": "adinventitias",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-07T22:44:49.776Z"),
            "url": "https://gifted-yarmulke.info/",
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
            "currency": "RUB",
            "description": "Solum commemoro conor nemo ultio.",
            "exchange_rate": 1.0625,
            "id": "af95aa5b-8e47-4897-8265-3250346d9cc6",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "posted_at": parse_datetime("2023-11-02T11:30:33.236Z"),
            "reference": "82523039",
            "source": "amplitudo",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-08T19:13:50.072Z"),
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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "aefcd32c-9065-47b5-b54e-65b9e685af19",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-11T02:25:41.352Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-20T11:54:33.393Z"),
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
            "id": "d6d73ae7-0716-4f8a-8b83-7fd8fb0b894b",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-02T10:06:26.168Z"),
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
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "1a7e6862-4e84-487f-9b78-f6b677346e7a",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-05-14T17:55:03.781Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-27T01:40:48.245Z"),
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
            "closed_at": parse_datetime("2023-08-25T15:46:30.031Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "925de6d3-7e9f-43ce-a244-f70b43a8c71a",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-02-02T04:11:00.928Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-11T03:36:16.933Z"),
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
                    "name": "cogo",
                    "rate": 53.0,
                },
            ],
            "country": "BY",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Atrox tricesimus creator.",
            "effective_rate": 53.0,
            "id": "85b33467-6768-4ad7-9d03-97b4ea48bd78",
            "is_active": False,
            "is_compound": True,
            "metadata": [],
            "name": "villa",
            "rate": 53.0,
            "region": "TX",
            "total_rate": 53.0,
            "type": shared.AccountingTaxrateType.OTHER,
            "updated_at": parse_datetime("2022-04-21T03:47:18.487Z"),
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
            "exchange_rate": 0.5674,
            "id": "f2edd48a-1282-4926-920d-44b0ff14e89f",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The Nikolas Table is the latest in a series of downright products from Beier and Sons",
                    "id": "f58f78a4-d974-4f40-b27b-35b8ab8e86e5",
                    "name": "Salad",
                    "object_type": "delicate",
                    "total_amount": 58531.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 91.0,
                },
            ],
            "memo": "withdrawal of USD 873.18 at Harber and Sons charged to account ending in 1804 using card ending in ****7022.",
            "status": shared.AccountingTransactionStatus.VOID,
            "tax_amount": 0.0,
            "total_amount": 94452.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2021-09-17T08:56:13.533Z"),
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
            "apply_amount": 1.0,
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "KGS",
            "due_at": parse_datetime("2023-05-06T20:38:46.775Z"),
            "id": "42a36e6a-cd20-4bce-b19a-43246cf46477",
            "lineitems": [],
            "metadata": [],
            "notes": "Conatus cruciamentum decor avaritia tantum.",
            "posted_at": parse_datetime("2023-10-02T03:02:21.445Z"),
            "status": shared.AccountingVendorcreditStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-12-01T06:09:05.693Z"),
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
            "currency": "BOB",
            "customer_defined_code": "quo",
            "description": "Spoliatio comedo vilitas harum cupiditate.",
            "id": "4ab11124-4d00-4688-a8df-80fd55c3f83f",
            "is_payable": True,
            "name": "Electronic Aluminum Tuna",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vesper",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "iste",
                },
                {
                    "original_type": "adamo",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "peccatus",
                },
            ],
            "type": shared.Type.BANK,
            "updated_at": parse_datetime("2023-01-06T05:16:44.340Z"),
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
            "account_id": "baa0e9a4-65e9-4bf5-856a-ce46fc36ebb1",
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 90358.0,
            "bank_name": "Weissnat Inc",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "SSP",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "29905cbb-8fd6-4d85-82ac-b05cd3c84ea1",
            "name": "Corwin, Donnelly and Connelly Savings",
            "routing_number": "667753156",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-21T04:15:03.216Z"),
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
            "account_id": "b7dc4175-1368-4b89-a700-d621b6666648",
            "amount": 60889.0,
            "bank_category": "Games",
            "bankfeedaccount_id": "34c1d05f-5b62-4bcd-9121-3be8b720941f",
            "category_ids": [],
            "contact_id": "1ef58ebe-f9c9-46f6-9d9c-2df2658503be",
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "SRD",
            "description": "payment transaction at McLaughlin - Schaden using card ending with ****8233 for DOP 574.03 in account ***9523.",
            "id": "7d03bc49-7c51-472b-9834-638dbe81463d",
            "is_pending": True,
            "merchant_name": "Reichert, Erdman and Tillman",
            "posted_at": parse_datetime("2025-04-10T01:40:14.168Z"),
            "reference": "93642593",
            "transaction_at": parse_datetime("2022-07-29T19:08:12.792Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-24T19:29:33.909Z"),
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
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "c9cfde20-e90a-4854-a816-ea3c8cf42a96",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-21T06:00:58.916Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-17T23:16:18.209Z"),
            "url": "https://coarse-interviewer.biz/",
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
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "d59af4a4-c2a5-4e09-b9e7-f7e332152535",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-09-06T16:58:55.418Z"),
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
            "associated_contacts": [
                {
                    "id": "a9b3ac12-37c9-479f-a12b-cf2493de4002",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "d32e70f5-f8da-4ff5-bf25-181e8c234be5",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "f5579091-17dc-4fc8-bdb0-34803a431f4f",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "8d92f002-5967-4aa2-8667-ef69e1ab53c7",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-16T15:28:50.213Z"),
            "website": "https://noxious-advertisement.org",
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
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "319514e5-8c4f-4090-ac33-24ffe610be0a",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "748537ea-d4a1-4989-b81e-649a81f2e5d6",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-12-04T02:04:50.634Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-25T13:24:34.145Z"),
            "url": "https://lighthearted-bandwidth.net/",
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
            "approved_at": parse_datetime("2026-06-03T03:51:40.880Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "342c80a9-949e-4b3b-9145-d259c985c6cb",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "df68d4df-993d-43a4-b60b-f257edf44272",
            "lineitems": [
                {
                    "id": "5df7f6a5-3389-4e02-b6fe-e505cb61091d",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-08T06:10:48.705Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "type": shared.AccountingExpenseType.USER,
            "updated_at": parse_datetime("2026-06-03T03:51:40.880Z"),
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
            "approved_at": parse_datetime("2025-04-08T14:17:56.587Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "aa77e25e-455e-4d93-ac21-3807fd9e8568",
            "lineitems": [
                {
                    "id": "bf0949fd-f92d-4524-8ac0-3756355d5c6f",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "5baf512b-8bf1-4c0c-90f6-58060c68a2b5",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-10-31T08:51:10.911Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-08T14:17:56.587Z"),
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
                    "id": "3e912774-9769-44d4-9a52-0d0c1b241500",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "cc544b8e-6882-4ae3-9856-acfc13577130",
            "invoice_number": "vinco",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-04-18T14:46:04.055Z"),
            "reference": "adinventitias",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-07T22:44:49.779Z"),
            "url": "https://gifted-yarmulke.info/",
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
            "currency": "RUB",
            "description": "Solum commemoro conor nemo ultio.",
            "exchange_rate": 1.0625,
            "id": "99f4610b-9d7c-4d39-abe5-8964e1e1aff6",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "posted_at": parse_datetime("2023-11-02T11:30:33.247Z"),
            "reference": "82523039",
            "source": "amplitudo",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-08T19:13:50.078Z"),
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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "42809cae-207d-4265-a7c5-5329d8b1b068",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-11T02:25:41.361Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-20T11:54:33.397Z"),
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
            "id": "7ebb882f-8673-4ed3-88f7-d5e99ae3fdad",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-02T10:06:26.179Z"),
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
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "6ab61c43-3f6b-42af-877d-e174801f584a",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-05-14T17:55:03.809Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-27T01:40:48.246Z"),
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
            "closed_at": parse_datetime("2023-08-25T15:46:30.050Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "024f8e1e-f388-4d21-96ff-8160c1ae733d",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-02-02T04:11:00.975Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-11T03:36:16.933Z"),
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
                    "name": "cogo",
                    "rate": 53.0,
                },
            ],
            "country": "BY",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Atrox tricesimus creator.",
            "effective_rate": 53.0,
            "id": "7c0bb142-c068-450a-92ac-c0a4424264c8",
            "is_active": False,
            "is_compound": True,
            "metadata": [],
            "name": "villa",
            "rate": 53.0,
            "region": "TX",
            "total_rate": 53.0,
            "type": shared.AccountingTaxrateType.OTHER,
            "updated_at": parse_datetime("2022-04-21T03:47:18.491Z"),
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
            "exchange_rate": 0.5674,
            "id": "f1eab3b8-f50a-42e7-b3f6-0ba92d4e7982",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The Nikolas Table is the latest in a series of downright products from Beier and Sons",
                    "id": "154a7889-68f2-4f05-9304-50df411cb4b8",
                    "name": "Salad",
                    "object_type": "delicate",
                    "total_amount": 58531.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 91.0,
                },
            ],
            "memo": "withdrawal of USD 873.18 at Harber and Sons charged to account ending in 1804 using card ending in ****7022.",
            "status": shared.AccountingTransactionStatus.VOID,
            "tax_amount": 0.0,
            "total_amount": 94452.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2021-09-17T08:56:13.538Z"),
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
            "apply_amount": 1.0,
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "KGS",
            "due_at": parse_datetime("2023-05-06T20:38:46.775Z"),
            "id": "1d87dfbe-b01f-4c89-8077-a1268242ca50",
            "lineitems": [],
            "metadata": [],
            "notes": "Conatus cruciamentum decor avaritia tantum.",
            "posted_at": parse_datetime("2023-10-02T03:02:21.449Z"),
            "status": shared.AccountingVendorcreditStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-12-01T06:09:05.698Z"),
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
            "currency": "BOB",
            "customer_defined_code": "quo",
            "description": "Spoliatio comedo vilitas harum cupiditate.",
            "id": "4ab11124-4d00-4688-a8df-80fd55c3f83f",
            "is_payable": True,
            "name": "Electronic Aluminum Tuna",
            "status": shared.Status.ARCHIVED,
            "taxonomy": [
                {
                    "original_type": "vesper",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "iste",
                },
                {
                    "original_type": "adamo",
                    "type": shared.AccountingAccountTaxonomyType.SUBGROUP,
                    "value": "peccatus",
                },
            ],
            "type": shared.Type.BANK,
            "updated_at": parse_datetime("2023-01-06T05:16:44.340Z"),
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
            "account_id": "baa0e9a4-65e9-4bf5-856a-ce46fc36ebb1",
            "account_number": "30369722",
            "account_number_last4": "9722",
            "account_type": shared.AccountType.LOAN,
            "balance": 90358.0,
            "bank_name": "Weissnat Inc",
            "created_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "currency": "SSP",
            "feed_start_at": parse_datetime("2022-10-31T16:42:19.277Z"),
            "id": "29905cbb-8fd6-4d85-82ac-b05cd3c84ea1",
            "name": "Corwin, Donnelly and Connelly Savings",
            "routing_number": "667753156",
            "status": shared.AccountingBankfeedaccountStatus.ACTIVE,
            "updated_at": parse_datetime("2024-04-21T04:15:03.216Z"),
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
            "account_id": "b7dc4175-1368-4b89-a700-d621b6666648",
            "amount": 60889.0,
            "bank_category": "Games",
            "bankfeedaccount_id": "34c1d05f-5b62-4bcd-9121-3be8b720941f",
            "category_ids": [],
            "contact_id": "1ef58ebe-f9c9-46f6-9d9c-2df2658503be",
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "SRD",
            "description": "payment transaction at McLaughlin - Schaden using card ending with ****8233 for DOP 574.03 in account ***9523.",
            "id": "7d03bc49-7c51-472b-9834-638dbe81463d",
            "is_pending": True,
            "merchant_name": "Reichert, Erdman and Tillman",
            "posted_at": parse_datetime("2025-04-10T01:40:14.168Z"),
            "reference": "93642593",
            "transaction_at": parse_datetime("2022-07-29T19:08:12.792Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-24T19:29:33.909Z"),
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
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "c9cfde20-e90a-4854-a816-ea3c8cf42a96",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-21T06:00:58.916Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-17T23:16:18.209Z"),
            "url": "https://coarse-interviewer.biz/",
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
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "d59af4a4-c2a5-4e09-b9e7-f7e332152535",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-09-06T16:58:55.418Z"),
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
            "associated_contacts": [
                {
                    "id": "a9b3ac12-37c9-479f-a12b-cf2493de4002",
                    "name": "Delores Reynolds",
                },
                {
                    "id": "d32e70f5-f8da-4ff5-bf25-181e8c234be5",
                    "name": "Delores Reynolds",
                },
            ],
            "billing_address": {
                "address1": "2633 Stoney Lane",
                "address2": "Suite 176",
                "city": "Ladariusboro",
                "country_code": "US",
                "postal_code": "70131-2908",
                "region": "Illinois",
                "region_code": "NV",
            },
            "company_name": "Marquardt Inc",
            "created_at": parse_datetime("2021-08-15T14:56:50.258Z"),
            "currency": "ISK",
            "emails": [
                {
                    "email": "Delores.Reynolds10@hotmail.com",
                    "type": shared.AccountingEmailType.HOME,
                },
            ],
            "first_name": "Delores",
            "id": "f5579091-17dc-4fc8-bdb0-34803a431f4f",
            "identification": "amicitia",
            "is_active": True,
            "is_customer": True,
            "last_name": "Reynolds",
            "name": "Delores Reynolds",
            "notes": "Caput accusamus et videlicet.",
            "payment_methods": [
                {
                    "default": True,
                    "id": "8d92f002-5967-4aa2-8667-ef69e1ab53c7",
                    "name": "Visa 1234",
                    "type": shared.AccountingContactPaymentMethodType.CARD,
                },
            ],
            "portal_url": "https://scented-t-shirt.info/",
            "shipping_address": {
                "address1": "786 Renner Stream",
                "address2": "Apt. 555",
                "city": "Roanoke",
                "country_code": "US",
                "postal_code": "80686-7556",
                "region": "Vermont",
                "region_code": "NE",
            },
            "tax_exemption": shared.TaxExemption.RESALE,
            "tax_number": "amplexus",
            "telephones": [
                {
                    "telephone": "(427) 701-7160",
                    "type": shared.AccountingTelephoneType.HOME,
                },
                {
                    "telephone": "(540) 913-9171",
                    "type": shared.AccountingTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2023-12-16T15:28:50.213Z"),
            "website": "https://noxious-advertisement.org",
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
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "319514e5-8c4f-4090-ac33-24ffe610be0a",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "748537ea-d4a1-4989-b81e-649a81f2e5d6",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-12-04T02:04:50.634Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-25T13:24:34.145Z"),
            "url": "https://lighthearted-bandwidth.net/",
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
            "approved_at": parse_datetime("2026-06-03T03:51:40.880Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "342c80a9-949e-4b3b-9145-d259c985c6cb",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "df68d4df-993d-43a4-b60b-f257edf44272",
            "lineitems": [
                {
                    "id": "5df7f6a5-3389-4e02-b6fe-e505cb61091d",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-08T06:10:48.705Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "type": shared.AccountingExpenseType.USER,
            "updated_at": parse_datetime("2026-06-03T03:51:40.880Z"),
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
            "approved_at": parse_datetime("2025-04-08T14:17:56.587Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "aa77e25e-455e-4d93-ac21-3807fd9e8568",
            "lineitems": [
                {
                    "id": "bf0949fd-f92d-4524-8ac0-3756355d5c6f",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "5baf512b-8bf1-4c0c-90f6-58060c68a2b5",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-10-31T08:51:10.911Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-08T14:17:56.587Z"),
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
                    "id": "3e912774-9769-44d4-9a52-0d0c1b241500",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "cc544b8e-6882-4ae3-9856-acfc13577130",
            "invoice_number": "vinco",
            "is_inclusive_of_tax": True,
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-04-18T14:46:04.055Z"),
            "reference": "adinventitias",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-07T22:44:49.779Z"),
            "url": "https://gifted-yarmulke.info/",
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
            "currency": "RUB",
            "description": "Solum commemoro conor nemo ultio.",
            "exchange_rate": 1.0625,
            "id": "99f4610b-9d7c-4d39-abe5-8964e1e1aff6",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "posted_at": parse_datetime("2023-11-02T11:30:33.247Z"),
            "reference": "82523039",
            "source": "amplitudo",
            "status": shared.AccountingJournalStatus.VOID,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-01-08T19:13:50.078Z"),
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
                "address1": "802 Bechtelar Park",
                "address2": "Apt. 436",
                "city": "Daniellaville",
                "country_code": "US",
                "postal_code": "36947",
                "region": "Wisconsin",
                "region_code": "NY",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "USD",
            "id": "42809cae-207d-4265-a7c5-5329d8b1b068",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2022-04-11T02:25:41.361Z"),
            "shipping_address": {
                "address1": "9745 Betty Shore",
                "city": "South Alainaland",
                "country_code": "US",
                "postal_code": "25274-7654",
                "region": "New Hampshire",
                "region_code": "LA",
            },
            "status": shared.AccountingOrderStatus.SUBMITTED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.PURCHASE,
            "updated_at": parse_datetime("2021-06-20T11:54:33.397Z"),
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
            "id": "7ebb882f-8673-4ed3-88f7-d5e99ae3fdad",
            "is_active": False,
            "metadata": [],
            "name": "Net 30",
            "type": shared.AccountingPaymenttermType.NET_15,
            "updated_at": parse_datetime("2026-01-02T10:06:26.179Z"),
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
                "address1": "37214 Tanya Walks",
                "city": "South Annabelleton",
                "country_code": "US",
                "postal_code": "30337",
                "region": "Nevada",
                "region_code": "MA",
            },
            "category_ids": [],
            "created_at": parse_datetime("2020-12-12T07:17:47.021Z"),
            "currency": "ZMW",
            "id": "6ab61c43-3f6b-42af-877d-e174801f584a",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2025-05-14T17:55:03.809Z"),
            "shipping_address": {
                "address1": "649 Maggio Overpass",
                "city": "Lake Jaylan",
                "country_code": "US",
                "postal_code": "99211-6547",
                "region": "North Carolina",
                "region_code": "ID",
            },
            "status": shared.AccountingPurchaseorderStatus.PARTIALLY_REFUNDED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2021-02-27T01:40:48.246Z"),
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
            "closed_at": parse_datetime("2023-08-25T15:46:30.050Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "ANG",
            "discount_amount": 99.0,
            "employee_user_id": "4a6b8990-c85a-499f-82d0-5011c3c95a0b",
            "fees": [
                {
                    "amount": 519.0,
                    "currency": "XCD",
                    "type": shared.AccountingFeeType.PROMOTION,
                },
            ],
            "fulfillment_type": shared.FulfillmentType.TAKEOUT,
            "guest_count": 8.0,
            "id": "024f8e1e-f388-4d21-96ff-8160c1ae733d",
            "lineitems": [],
            "metadata": [],
            "order_number": "988187",
            "payments": [],
            "posted_at": parse_datetime("2026-02-02T04:11:00.975Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Harvey, Collier and Weimann",
            "service_charge_amount": 63.0,
            "shipping_address": {
                "address1": "9878 Bradley Mill",
                "address2": "Apt. 215",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.REFUNDED,
            "subtotal_amount": 0.0,
            "tax_amount": 63.0,
            "tip_amount": 34.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2022-02-11T03:36:16.933Z"),
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
                    "name": "cogo",
                    "rate": 53.0,
                },
            ],
            "country": "BY",
            "created_at": parse_datetime("2020-01-04T10:37:56.894Z"),
            "description": "Atrox tricesimus creator.",
            "effective_rate": 53.0,
            "id": "7c0bb142-c068-450a-92ac-c0a4424264c8",
            "is_active": False,
            "is_compound": True,
            "metadata": [],
            "name": "villa",
            "rate": 53.0,
            "region": "TX",
            "total_rate": 53.0,
            "type": shared.AccountingTaxrateType.OTHER,
            "updated_at": parse_datetime("2022-04-21T03:47:18.491Z"),
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
            "exchange_rate": 0.5674,
            "id": "f1eab3b8-f50a-42e7-b3f6-0ba92d4e7982",
            "lineitems": [
                {
                    "category_ids": [],
                    "description": "The Nikolas Table is the latest in a series of downright products from Beier and Sons",
                    "id": "154a7889-68f2-4f05-9304-50df411cb4b8",
                    "name": "Salad",
                    "object_type": "delicate",
                    "total_amount": 58531.0,
                    "unit_amount": 536.0,
                    "unit_quantity": 91.0,
                },
            ],
            "memo": "withdrawal of USD 873.18 at Harber and Sons charged to account ending in 1804 using card ending in ****7022.",
            "status": shared.AccountingTransactionStatus.VOID,
            "tax_amount": 0.0,
            "total_amount": 94452.0,
            "transaction_at": parse_datetime("2019-09-25T11:40:42.574Z"),
            "updated_at": parse_datetime("2021-09-17T08:56:13.538Z"),
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
            "apply_amount": 1.0,
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "KGS",
            "due_at": parse_datetime("2023-05-06T20:38:46.775Z"),
            "id": "1d87dfbe-b01f-4c89-8077-a1268242ca50",
            "lineitems": [],
            "metadata": [],
            "notes": "Conatus cruciamentum decor avaritia tantum.",
            "posted_at": parse_datetime("2023-10-02T03:02:21.449Z"),
            "status": shared.AccountingVendorcreditStatus.SUBMITTED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-12-01T06:09:05.698Z"),
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