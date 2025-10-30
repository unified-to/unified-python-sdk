<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/unified-to/unified-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/unified-to/unified-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start Summary [summary] -->
## Summary

Unified.to API: One API to Rule Them All
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add Unified-python-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install Unified-python-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add Unified-python-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from Unified-python-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "Unified-python-sdk",
# ]
# ///

from unified_python_sdk import UnifiedTo

sdk = UnifiedTo(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared

async def main():

    async with UnifiedTo(
        security=shared.Security(
            jwt="<YOUR_API_KEY_HERE>",
        ),
    ) as unified_to:

        res = await unified_to.accounting.create_accounting_account_async(request={
            "accounting_account": {},
            "connection_id": "<id>",
        })

        assert res.accounting_account is not None

        # Handle response
        print(res.accounting_account)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account](docs/sdks/account/README.md)

* [create_accounting_account](docs/sdks/account/README.md#create_accounting_account) - Create an account
* [get_accounting_account](docs/sdks/account/README.md#get_accounting_account) - Retrieve an account
* [list_accounting_accounts](docs/sdks/account/README.md#list_accounting_accounts) - List all accounts
* [patch_accounting_account](docs/sdks/account/README.md#patch_accounting_account) - Update an account
* [remove_accounting_account](docs/sdks/account/README.md#remove_accounting_account) - Remove an account
* [update_accounting_account](docs/sdks/account/README.md#update_accounting_account) - Update an account

### [accounting](docs/sdks/accounting/README.md)

* [create_accounting_account](docs/sdks/accounting/README.md#create_accounting_account) - Create an account
* [create_accounting_bill](docs/sdks/accounting/README.md#create_accounting_bill) - Create a bill
* [create_accounting_category](docs/sdks/accounting/README.md#create_accounting_category) - Create a category
* [create_accounting_contact](docs/sdks/accounting/README.md#create_accounting_contact) - Create a contact
* [create_accounting_creditmemo](docs/sdks/accounting/README.md#create_accounting_creditmemo) - Create a creditmemo
* [create_accounting_expense](docs/sdks/accounting/README.md#create_accounting_expense) - Create an expense
* [create_accounting_invoice](docs/sdks/accounting/README.md#create_accounting_invoice) - Create an invoice
* [create_accounting_journal](docs/sdks/accounting/README.md#create_accounting_journal) - Create a journal
* [create_accounting_order](docs/sdks/accounting/README.md#create_accounting_order) - Create an order
* [create_accounting_purchaseorder](docs/sdks/accounting/README.md#create_accounting_purchaseorder) - Create a purchaseorder
* [create_accounting_salesorder](docs/sdks/accounting/README.md#create_accounting_salesorder) - Create a salesorder
* [create_accounting_taxrate](docs/sdks/accounting/README.md#create_accounting_taxrate) - Create a taxrate
* [create_accounting_transaction](docs/sdks/accounting/README.md#create_accounting_transaction) - Create a transaction
* [get_accounting_account](docs/sdks/accounting/README.md#get_accounting_account) - Retrieve an account
* [get_accounting_balancesheet](docs/sdks/accounting/README.md#get_accounting_balancesheet) - Retrieve a balancesheet
* [get_accounting_bill](docs/sdks/accounting/README.md#get_accounting_bill) - Retrieve a bill
* [get_accounting_cashflow](docs/sdks/accounting/README.md#get_accounting_cashflow) - Retrieve a cashflow
* [get_accounting_category](docs/sdks/accounting/README.md#get_accounting_category) - Retrieve a category
* [get_accounting_contact](docs/sdks/accounting/README.md#get_accounting_contact) - Retrieve a contact
* [get_accounting_creditmemo](docs/sdks/accounting/README.md#get_accounting_creditmemo) - Retrieve a creditmemo
* [get_accounting_expense](docs/sdks/accounting/README.md#get_accounting_expense) - Retrieve an expense
* [get_accounting_invoice](docs/sdks/accounting/README.md#get_accounting_invoice) - Retrieve an invoice
* [get_accounting_journal](docs/sdks/accounting/README.md#get_accounting_journal) - Retrieve a journal
* [get_accounting_order](docs/sdks/accounting/README.md#get_accounting_order) - Retrieve an order
* [get_accounting_organization](docs/sdks/accounting/README.md#get_accounting_organization) - Retrieve an organization
* [get_accounting_profitloss](docs/sdks/accounting/README.md#get_accounting_profitloss) - Retrieve a profitloss
* [get_accounting_purchaseorder](docs/sdks/accounting/README.md#get_accounting_purchaseorder) - Retrieve a purchaseorder
* [get_accounting_report](docs/sdks/accounting/README.md#get_accounting_report) - Retrieve a report
* [get_accounting_salesorder](docs/sdks/accounting/README.md#get_accounting_salesorder) - Retrieve a salesorder
* [get_accounting_taxrate](docs/sdks/accounting/README.md#get_accounting_taxrate) - Retrieve a taxrate
* [get_accounting_transaction](docs/sdks/accounting/README.md#get_accounting_transaction) - Retrieve a transaction
* [get_accounting_trialbalance](docs/sdks/accounting/README.md#get_accounting_trialbalance) - Retrieve a trialbalance
* [list_accounting_accounts](docs/sdks/accounting/README.md#list_accounting_accounts) - List all accounts
* [list_accounting_balancesheets](docs/sdks/accounting/README.md#list_accounting_balancesheets) - List all balancesheets
* [list_accounting_bills](docs/sdks/accounting/README.md#list_accounting_bills) - List all bills
* [list_accounting_cashflows](docs/sdks/accounting/README.md#list_accounting_cashflows) - List all cashflows
* [list_accounting_categories](docs/sdks/accounting/README.md#list_accounting_categories) - List all categories
* [list_accounting_contacts](docs/sdks/accounting/README.md#list_accounting_contacts) - List all contacts
* [list_accounting_creditmemoes](docs/sdks/accounting/README.md#list_accounting_creditmemoes) - List all creditmemoes
* [list_accounting_expenses](docs/sdks/accounting/README.md#list_accounting_expenses) - List all expenses
* [list_accounting_invoices](docs/sdks/accounting/README.md#list_accounting_invoices) - List all invoices
* [list_accounting_journals](docs/sdks/accounting/README.md#list_accounting_journals) - List all journals
* [list_accounting_orders](docs/sdks/accounting/README.md#list_accounting_orders) - List all orders
* [list_accounting_organizations](docs/sdks/accounting/README.md#list_accounting_organizations) - List all organizations
* [list_accounting_profitlosses](docs/sdks/accounting/README.md#list_accounting_profitlosses) - List all profitlosses
* [list_accounting_purchaseorders](docs/sdks/accounting/README.md#list_accounting_purchaseorders) - List all purchaseorders
* [list_accounting_reports](docs/sdks/accounting/README.md#list_accounting_reports) - List all reports
* [list_accounting_salesorders](docs/sdks/accounting/README.md#list_accounting_salesorders) - List all salesorders
* [list_accounting_taxrates](docs/sdks/accounting/README.md#list_accounting_taxrates) - List all taxrates
* [list_accounting_transactions](docs/sdks/accounting/README.md#list_accounting_transactions) - List all transactions
* [list_accounting_trialbalances](docs/sdks/accounting/README.md#list_accounting_trialbalances) - List all trialbalances
* [patch_accounting_account](docs/sdks/accounting/README.md#patch_accounting_account) - Update an account
* [patch_accounting_bill](docs/sdks/accounting/README.md#patch_accounting_bill) - Update a bill
* [patch_accounting_category](docs/sdks/accounting/README.md#patch_accounting_category) - Update a category
* [patch_accounting_contact](docs/sdks/accounting/README.md#patch_accounting_contact) - Update a contact
* [patch_accounting_creditmemo](docs/sdks/accounting/README.md#patch_accounting_creditmemo) - Update a creditmemo
* [patch_accounting_expense](docs/sdks/accounting/README.md#patch_accounting_expense) - Update an expense
* [patch_accounting_invoice](docs/sdks/accounting/README.md#patch_accounting_invoice) - Update an invoice
* [patch_accounting_journal](docs/sdks/accounting/README.md#patch_accounting_journal) - Update a journal
* [patch_accounting_order](docs/sdks/accounting/README.md#patch_accounting_order) - Update an order
* [patch_accounting_purchaseorder](docs/sdks/accounting/README.md#patch_accounting_purchaseorder) - Update a purchaseorder
* [patch_accounting_salesorder](docs/sdks/accounting/README.md#patch_accounting_salesorder) - Update a salesorder
* [patch_accounting_taxrate](docs/sdks/accounting/README.md#patch_accounting_taxrate) - Update a taxrate
* [patch_accounting_transaction](docs/sdks/accounting/README.md#patch_accounting_transaction) - Update a transaction
* [remove_accounting_account](docs/sdks/accounting/README.md#remove_accounting_account) - Remove an account
* [remove_accounting_bill](docs/sdks/accounting/README.md#remove_accounting_bill) - Remove a bill
* [remove_accounting_category](docs/sdks/accounting/README.md#remove_accounting_category) - Remove a category
* [remove_accounting_contact](docs/sdks/accounting/README.md#remove_accounting_contact) - Remove a contact
* [remove_accounting_creditmemo](docs/sdks/accounting/README.md#remove_accounting_creditmemo) - Remove a creditmemo
* [remove_accounting_expense](docs/sdks/accounting/README.md#remove_accounting_expense) - Remove an expense
* [remove_accounting_invoice](docs/sdks/accounting/README.md#remove_accounting_invoice) - Remove an invoice
* [remove_accounting_journal](docs/sdks/accounting/README.md#remove_accounting_journal) - Remove a journal
* [remove_accounting_order](docs/sdks/accounting/README.md#remove_accounting_order) - Remove an order
* [remove_accounting_purchaseorder](docs/sdks/accounting/README.md#remove_accounting_purchaseorder) - Remove a purchaseorder
* [remove_accounting_salesorder](docs/sdks/accounting/README.md#remove_accounting_salesorder) - Remove a salesorder
* [remove_accounting_taxrate](docs/sdks/accounting/README.md#remove_accounting_taxrate) - Remove a taxrate
* [remove_accounting_transaction](docs/sdks/accounting/README.md#remove_accounting_transaction) - Remove a transaction
* [update_accounting_account](docs/sdks/accounting/README.md#update_accounting_account) - Update an account
* [update_accounting_bill](docs/sdks/accounting/README.md#update_accounting_bill) - Update a bill
* [update_accounting_category](docs/sdks/accounting/README.md#update_accounting_category) - Update a category
* [update_accounting_contact](docs/sdks/accounting/README.md#update_accounting_contact) - Update a contact
* [update_accounting_creditmemo](docs/sdks/accounting/README.md#update_accounting_creditmemo) - Update a creditmemo
* [update_accounting_expense](docs/sdks/accounting/README.md#update_accounting_expense) - Update an expense
* [update_accounting_invoice](docs/sdks/accounting/README.md#update_accounting_invoice) - Update an invoice
* [update_accounting_journal](docs/sdks/accounting/README.md#update_accounting_journal) - Update a journal
* [update_accounting_order](docs/sdks/accounting/README.md#update_accounting_order) - Update an order
* [update_accounting_purchaseorder](docs/sdks/accounting/README.md#update_accounting_purchaseorder) - Update a purchaseorder
* [update_accounting_salesorder](docs/sdks/accounting/README.md#update_accounting_salesorder) - Update a salesorder
* [update_accounting_taxrate](docs/sdks/accounting/README.md#update_accounting_taxrate) - Update a taxrate
* [update_accounting_transaction](docs/sdks/accounting/README.md#update_accounting_transaction) - Update a transaction

### [activity](docs/sdks/activity/README.md)

* [create_ats_activity](docs/sdks/activity/README.md#create_ats_activity) - Create an activity
* [get_ats_activity](docs/sdks/activity/README.md#get_ats_activity) - Retrieve an activity
* [list_ats_activities](docs/sdks/activity/README.md#list_ats_activities) - List all activities
* [patch_ats_activity](docs/sdks/activity/README.md#patch_ats_activity) - Update an activity
* [remove_ats_activity](docs/sdks/activity/README.md#remove_ats_activity) - Remove an activity
* [update_ats_activity](docs/sdks/activity/README.md#update_ats_activity) - Update an activity

### [apicall](docs/sdks/apicall/README.md)

* [get_unified_apicall](docs/sdks/apicall/README.md#get_unified_apicall) - Retrieve specific API Call by its ID
* [list_unified_apicalls](docs/sdks/apicall/README.md#list_unified_apicalls) - Returns API Calls

### [application](docs/sdks/application/README.md)

* [create_ats_application](docs/sdks/application/README.md#create_ats_application) - Create an application
* [get_ats_application](docs/sdks/application/README.md#get_ats_application) - Retrieve an application
* [list_ats_applications](docs/sdks/application/README.md#list_ats_applications) - List all applications
* [patch_ats_application](docs/sdks/application/README.md#patch_ats_application) - Update an application
* [remove_ats_application](docs/sdks/application/README.md#remove_ats_application) - Remove an application
* [update_ats_application](docs/sdks/application/README.md#update_ats_application) - Update an application

### [applicationstatus](docs/sdks/applicationstatus/README.md)

* [list_ats_applicationstatuses](docs/sdks/applicationstatus/README.md#list_ats_applicationstatuses) - List all applicationstatuses

### [ats](docs/sdks/ats/README.md)

* [create_ats_activity](docs/sdks/ats/README.md#create_ats_activity) - Create an activity
* [create_ats_application](docs/sdks/ats/README.md#create_ats_application) - Create an application
* [create_ats_candidate](docs/sdks/ats/README.md#create_ats_candidate) - Create a candidate
* [create_ats_company](docs/sdks/ats/README.md#create_ats_company) - Create a company
* [create_ats_document](docs/sdks/ats/README.md#create_ats_document) - Create a document
* [create_ats_interview](docs/sdks/ats/README.md#create_ats_interview) - Create an interview
* [create_ats_job](docs/sdks/ats/README.md#create_ats_job) - Create a job
* [create_ats_scorecard](docs/sdks/ats/README.md#create_ats_scorecard) - Create a scorecard
* [get_ats_activity](docs/sdks/ats/README.md#get_ats_activity) - Retrieve an activity
* [get_ats_application](docs/sdks/ats/README.md#get_ats_application) - Retrieve an application
* [get_ats_candidate](docs/sdks/ats/README.md#get_ats_candidate) - Retrieve a candidate
* [get_ats_company](docs/sdks/ats/README.md#get_ats_company) - Retrieve a company
* [get_ats_document](docs/sdks/ats/README.md#get_ats_document) - Retrieve a document
* [get_ats_interview](docs/sdks/ats/README.md#get_ats_interview) - Retrieve an interview
* [get_ats_job](docs/sdks/ats/README.md#get_ats_job) - Retrieve a job
* [get_ats_scorecard](docs/sdks/ats/README.md#get_ats_scorecard) - Retrieve a scorecard
* [list_ats_activities](docs/sdks/ats/README.md#list_ats_activities) - List all activities
* [list_ats_applications](docs/sdks/ats/README.md#list_ats_applications) - List all applications
* [list_ats_applicationstatuses](docs/sdks/ats/README.md#list_ats_applicationstatuses) - List all applicationstatuses
* [list_ats_candidates](docs/sdks/ats/README.md#list_ats_candidates) - List all candidates
* [list_ats_companies](docs/sdks/ats/README.md#list_ats_companies) - List all companies
* [list_ats_documents](docs/sdks/ats/README.md#list_ats_documents) - List all documents
* [list_ats_interviews](docs/sdks/ats/README.md#list_ats_interviews) - List all interviews
* [list_ats_jobs](docs/sdks/ats/README.md#list_ats_jobs) - List all jobs
* [list_ats_scorecards](docs/sdks/ats/README.md#list_ats_scorecards) - List all scorecards
* [patch_ats_activity](docs/sdks/ats/README.md#patch_ats_activity) - Update an activity
* [patch_ats_application](docs/sdks/ats/README.md#patch_ats_application) - Update an application
* [patch_ats_candidate](docs/sdks/ats/README.md#patch_ats_candidate) - Update a candidate
* [patch_ats_company](docs/sdks/ats/README.md#patch_ats_company) - Update a company
* [patch_ats_document](docs/sdks/ats/README.md#patch_ats_document) - Update a document
* [patch_ats_interview](docs/sdks/ats/README.md#patch_ats_interview) - Update an interview
* [patch_ats_job](docs/sdks/ats/README.md#patch_ats_job) - Update a job
* [patch_ats_scorecard](docs/sdks/ats/README.md#patch_ats_scorecard) - Update a scorecard
* [remove_ats_activity](docs/sdks/ats/README.md#remove_ats_activity) - Remove an activity
* [remove_ats_application](docs/sdks/ats/README.md#remove_ats_application) - Remove an application
* [remove_ats_candidate](docs/sdks/ats/README.md#remove_ats_candidate) - Remove a candidate
* [remove_ats_company](docs/sdks/ats/README.md#remove_ats_company) - Remove a company
* [remove_ats_document](docs/sdks/ats/README.md#remove_ats_document) - Remove a document
* [remove_ats_interview](docs/sdks/ats/README.md#remove_ats_interview) - Remove an interview
* [remove_ats_job](docs/sdks/ats/README.md#remove_ats_job) - Remove a job
* [remove_ats_scorecard](docs/sdks/ats/README.md#remove_ats_scorecard) - Remove a scorecard
* [update_ats_activity](docs/sdks/ats/README.md#update_ats_activity) - Update an activity
* [update_ats_application](docs/sdks/ats/README.md#update_ats_application) - Update an application
* [update_ats_candidate](docs/sdks/ats/README.md#update_ats_candidate) - Update a candidate
* [update_ats_company](docs/sdks/ats/README.md#update_ats_company) - Update a company
* [update_ats_document](docs/sdks/ats/README.md#update_ats_document) - Update a document
* [update_ats_interview](docs/sdks/ats/README.md#update_ats_interview) - Update an interview
* [update_ats_job](docs/sdks/ats/README.md#update_ats_job) - Update a job
* [update_ats_scorecard](docs/sdks/ats/README.md#update_ats_scorecard) - Update a scorecard

### [auth](docs/sdks/auth/README.md)

* [get_unified_integration_auth](docs/sdks/auth/README.md#get_unified_integration_auth) - Authorize new connection
* [get_unified_integration_login](docs/sdks/auth/README.md#get_unified_integration_login) - Sign in a user

### [balancesheet](docs/sdks/balancesheet/README.md)

* [get_accounting_balancesheet](docs/sdks/balancesheet/README.md#get_accounting_balancesheet) - Retrieve a balancesheet
* [list_accounting_balancesheets](docs/sdks/balancesheet/README.md#list_accounting_balancesheets) - List all balancesheets

### [bill](docs/sdks/bill/README.md)

* [create_accounting_bill](docs/sdks/bill/README.md#create_accounting_bill) - Create a bill
* [get_accounting_bill](docs/sdks/bill/README.md#get_accounting_bill) - Retrieve a bill
* [list_accounting_bills](docs/sdks/bill/README.md#list_accounting_bills) - List all bills
* [patch_accounting_bill](docs/sdks/bill/README.md#patch_accounting_bill) - Update a bill
* [remove_accounting_bill](docs/sdks/bill/README.md#remove_accounting_bill) - Remove a bill
* [update_accounting_bill](docs/sdks/bill/README.md#update_accounting_bill) - Update a bill

### [branch](docs/sdks/branch/README.md)

* [create_repo_branch](docs/sdks/branch/README.md#create_repo_branch) - Create a branch
* [get_repo_branch](docs/sdks/branch/README.md#get_repo_branch) - Retrieve a branch
* [list_repo_branches](docs/sdks/branch/README.md#list_repo_branches) - List all branches
* [patch_repo_branch](docs/sdks/branch/README.md#patch_repo_branch) - Update a branch
* [remove_repo_branch](docs/sdks/branch/README.md#remove_repo_branch) - Remove a branch
* [update_repo_branch](docs/sdks/branch/README.md#update_repo_branch) - Update a branch

### [busy](docs/sdks/busy/README.md)

* [list_calendar_busies](docs/sdks/busy/README.md#list_calendar_busies) - List all busies

### [calendar](docs/sdks/calendar/README.md)

* [create_calendar_calendar](docs/sdks/calendar/README.md#create_calendar_calendar) - Create a calendar
* [create_calendar_event](docs/sdks/calendar/README.md#create_calendar_event) - Create an event
* [create_calendar_link](docs/sdks/calendar/README.md#create_calendar_link) - Create a link
* [get_calendar_calendar](docs/sdks/calendar/README.md#get_calendar_calendar) - Retrieve a calendar
* [get_calendar_event](docs/sdks/calendar/README.md#get_calendar_event) - Retrieve an event
* [get_calendar_link](docs/sdks/calendar/README.md#get_calendar_link) - Retrieve a link
* [get_calendar_recording](docs/sdks/calendar/README.md#get_calendar_recording) - Retrieve a recording
* [list_calendar_busies](docs/sdks/calendar/README.md#list_calendar_busies) - List all busies
* [list_calendar_calendars](docs/sdks/calendar/README.md#list_calendar_calendars) - List all calendars
* [list_calendar_events](docs/sdks/calendar/README.md#list_calendar_events) - List all events
* [list_calendar_links](docs/sdks/calendar/README.md#list_calendar_links) - List all links
* [list_calendar_recordings](docs/sdks/calendar/README.md#list_calendar_recordings) - List all recordings
* [patch_calendar_calendar](docs/sdks/calendar/README.md#patch_calendar_calendar) - Update a calendar
* [patch_calendar_event](docs/sdks/calendar/README.md#patch_calendar_event) - Update an event
* [patch_calendar_link](docs/sdks/calendar/README.md#patch_calendar_link) - Update a link
* [remove_calendar_calendar](docs/sdks/calendar/README.md#remove_calendar_calendar) - Remove a calendar
* [remove_calendar_event](docs/sdks/calendar/README.md#remove_calendar_event) - Remove an event
* [remove_calendar_link](docs/sdks/calendar/README.md#remove_calendar_link) - Remove a link
* [update_calendar_calendar](docs/sdks/calendar/README.md#update_calendar_calendar) - Update a calendar
* [update_calendar_event](docs/sdks/calendar/README.md#update_calendar_event) - Update an event
* [update_calendar_link](docs/sdks/calendar/README.md#update_calendar_link) - Update a link

### [call](docs/sdks/call/README.md)

* [list_uc_calls](docs/sdks/call/README.md#list_uc_calls) - List all calls

### [candidate](docs/sdks/candidate/README.md)

* [create_ats_candidate](docs/sdks/candidate/README.md#create_ats_candidate) - Create a candidate
* [get_ats_candidate](docs/sdks/candidate/README.md#get_ats_candidate) - Retrieve a candidate
* [list_ats_candidates](docs/sdks/candidate/README.md#list_ats_candidates) - List all candidates
* [patch_ats_candidate](docs/sdks/candidate/README.md#patch_ats_candidate) - Update a candidate
* [remove_ats_candidate](docs/sdks/candidate/README.md#remove_ats_candidate) - Remove a candidate
* [update_ats_candidate](docs/sdks/candidate/README.md#update_ats_candidate) - Update a candidate

### [cashflow](docs/sdks/cashflow/README.md)

* [get_accounting_cashflow](docs/sdks/cashflow/README.md#get_accounting_cashflow) - Retrieve a cashflow
* [list_accounting_cashflows](docs/sdks/cashflow/README.md#list_accounting_cashflows) - List all cashflows

### [category](docs/sdks/category/README.md)

* [create_accounting_category](docs/sdks/category/README.md#create_accounting_category) - Create a category
* [create_ticketing_category](docs/sdks/category/README.md#create_ticketing_category) - Create a category
* [get_accounting_category](docs/sdks/category/README.md#get_accounting_category) - Retrieve a category
* [get_ticketing_category](docs/sdks/category/README.md#get_ticketing_category) - Retrieve a category
* [list_accounting_categories](docs/sdks/category/README.md#list_accounting_categories) - List all categories
* [list_ticketing_categories](docs/sdks/category/README.md#list_ticketing_categories) - List all categories
* [patch_accounting_category](docs/sdks/category/README.md#patch_accounting_category) - Update a category
* [patch_ticketing_category](docs/sdks/category/README.md#patch_ticketing_category) - Update a category
* [remove_accounting_category](docs/sdks/category/README.md#remove_accounting_category) - Remove a category
* [remove_ticketing_category](docs/sdks/category/README.md#remove_ticketing_category) - Remove a category
* [update_accounting_category](docs/sdks/category/README.md#update_accounting_category) - Update a category
* [update_ticketing_category](docs/sdks/category/README.md#update_ticketing_category) - Update a category

### [change](docs/sdks/change/README.md)

* [get_task_change](docs/sdks/change/README.md#get_task_change) - Retrieve a change
* [list_task_changes](docs/sdks/change/README.md#list_task_changes) - List all changes

### [channel](docs/sdks/channel/README.md)

* [get_messaging_channel](docs/sdks/channel/README.md#get_messaging_channel) - Retrieve a channel
* [list_messaging_channels](docs/sdks/channel/README.md#list_messaging_channels) - List all channels

### [class_](docs/sdks/class/README.md)

* [create_lms_class](docs/sdks/class/README.md#create_lms_class) - Create a class
* [get_lms_class](docs/sdks/class/README.md#get_lms_class) - Retrieve a class
* [list_lms_classes](docs/sdks/class/README.md#list_lms_classes) - List all classes
* [patch_lms_class](docs/sdks/class/README.md#patch_lms_class) - Update a class
* [remove_lms_class](docs/sdks/class/README.md#remove_lms_class) - Remove a class
* [update_lms_class](docs/sdks/class/README.md#update_lms_class) - Update a class

### [collection](docs/sdks/collection/README.md)

* [create_commerce_collection](docs/sdks/collection/README.md#create_commerce_collection) - Create a collection
* [get_commerce_collection](docs/sdks/collection/README.md#get_commerce_collection) - Retrieve a collection
* [list_commerce_collections](docs/sdks/collection/README.md#list_commerce_collections) - List all collections
* [patch_commerce_collection](docs/sdks/collection/README.md#patch_commerce_collection) - Update a collection
* [remove_commerce_collection](docs/sdks/collection/README.md#remove_commerce_collection) - Remove a collection
* [update_commerce_collection](docs/sdks/collection/README.md#update_commerce_collection) - Update a collection

### [comment](docs/sdks/comment/README.md)

* [create_kms_comment](docs/sdks/comment/README.md#create_kms_comment) - Create a comment
* [create_task_comment](docs/sdks/comment/README.md#create_task_comment) - Create a comment
* [create_uc_comment](docs/sdks/comment/README.md#create_uc_comment) - Create a comment
* [get_kms_comment](docs/sdks/comment/README.md#get_kms_comment) - Retrieve a comment
* [get_task_comment](docs/sdks/comment/README.md#get_task_comment) - Retrieve a comment
* [get_uc_comment](docs/sdks/comment/README.md#get_uc_comment) - Retrieve a comment
* [list_kms_comments](docs/sdks/comment/README.md#list_kms_comments) - List all comments
* [list_task_comments](docs/sdks/comment/README.md#list_task_comments) - List all comments
* [list_uc_comments](docs/sdks/comment/README.md#list_uc_comments) - List all comments
* [patch_kms_comment](docs/sdks/comment/README.md#patch_kms_comment) - Update a comment
* [patch_task_comment](docs/sdks/comment/README.md#patch_task_comment) - Update a comment
* [patch_uc_comment](docs/sdks/comment/README.md#patch_uc_comment) - Update a comment
* [remove_kms_comment](docs/sdks/comment/README.md#remove_kms_comment) - Remove a comment
* [remove_task_comment](docs/sdks/comment/README.md#remove_task_comment) - Remove a comment
* [remove_uc_comment](docs/sdks/comment/README.md#remove_uc_comment) - Remove a comment
* [update_kms_comment](docs/sdks/comment/README.md#update_kms_comment) - Update a comment
* [update_task_comment](docs/sdks/comment/README.md#update_task_comment) - Update a comment
* [update_uc_comment](docs/sdks/comment/README.md#update_uc_comment) - Update a comment

### [commerce](docs/sdks/commerce/README.md)

* [create_commerce_collection](docs/sdks/commerce/README.md#create_commerce_collection) - Create a collection
* [create_commerce_inventory](docs/sdks/commerce/README.md#create_commerce_inventory) - Create an inventory
* [create_commerce_item](docs/sdks/commerce/README.md#create_commerce_item) - Create an item
* [create_commerce_location](docs/sdks/commerce/README.md#create_commerce_location) - Create a location
* [create_commerce_review](docs/sdks/commerce/README.md#create_commerce_review) - Create a review
* [get_commerce_collection](docs/sdks/commerce/README.md#get_commerce_collection) - Retrieve a collection
* [get_commerce_inventory](docs/sdks/commerce/README.md#get_commerce_inventory) - Retrieve an inventory
* [get_commerce_item](docs/sdks/commerce/README.md#get_commerce_item) - Retrieve an item
* [get_commerce_location](docs/sdks/commerce/README.md#get_commerce_location) - Retrieve a location
* [get_commerce_review](docs/sdks/commerce/README.md#get_commerce_review) - Retrieve a review
* [list_commerce_collections](docs/sdks/commerce/README.md#list_commerce_collections) - List all collections
* [list_commerce_inventories](docs/sdks/commerce/README.md#list_commerce_inventories) - List all inventories
* [list_commerce_items](docs/sdks/commerce/README.md#list_commerce_items) - List all items
* [list_commerce_locations](docs/sdks/commerce/README.md#list_commerce_locations) - List all locations
* [list_commerce_reviews](docs/sdks/commerce/README.md#list_commerce_reviews) - List all reviews
* [patch_commerce_collection](docs/sdks/commerce/README.md#patch_commerce_collection) - Update a collection
* [patch_commerce_inventory](docs/sdks/commerce/README.md#patch_commerce_inventory) - Update an inventory
* [patch_commerce_item](docs/sdks/commerce/README.md#patch_commerce_item) - Update an item
* [patch_commerce_location](docs/sdks/commerce/README.md#patch_commerce_location) - Update a location
* [patch_commerce_review](docs/sdks/commerce/README.md#patch_commerce_review) - Update a review
* [remove_commerce_collection](docs/sdks/commerce/README.md#remove_commerce_collection) - Remove a collection
* [remove_commerce_inventory](docs/sdks/commerce/README.md#remove_commerce_inventory) - Remove an inventory
* [remove_commerce_item](docs/sdks/commerce/README.md#remove_commerce_item) - Remove an item
* [remove_commerce_location](docs/sdks/commerce/README.md#remove_commerce_location) - Remove a location
* [remove_commerce_review](docs/sdks/commerce/README.md#remove_commerce_review) - Remove a review
* [update_commerce_collection](docs/sdks/commerce/README.md#update_commerce_collection) - Update a collection
* [update_commerce_inventory](docs/sdks/commerce/README.md#update_commerce_inventory) - Update an inventory
* [update_commerce_item](docs/sdks/commerce/README.md#update_commerce_item) - Update an item
* [update_commerce_location](docs/sdks/commerce/README.md#update_commerce_location) - Update a location
* [update_commerce_review](docs/sdks/commerce/README.md#update_commerce_review) - Update a review

### [commit](docs/sdks/commit/README.md)

* [create_repo_commit](docs/sdks/commit/README.md#create_repo_commit) - Create a commit
* [get_repo_commit](docs/sdks/commit/README.md#get_repo_commit) - Retrieve a commit
* [list_repo_commits](docs/sdks/commit/README.md#list_repo_commits) - List all commits
* [patch_repo_commit](docs/sdks/commit/README.md#patch_repo_commit) - Update a commit
* [remove_repo_commit](docs/sdks/commit/README.md#remove_repo_commit) - Remove a commit
* [update_repo_commit](docs/sdks/commit/README.md#update_repo_commit) - Update a commit

### [company](docs/sdks/company/README.md)

* [create_ats_company](docs/sdks/company/README.md#create_ats_company) - Create a company
* [create_crm_company](docs/sdks/company/README.md#create_crm_company) - Create a company
* [create_hris_company](docs/sdks/company/README.md#create_hris_company) - Create a company
* [get_ats_company](docs/sdks/company/README.md#get_ats_company) - Retrieve a company
* [get_crm_company](docs/sdks/company/README.md#get_crm_company) - Retrieve a company
* [get_hris_company](docs/sdks/company/README.md#get_hris_company) - Retrieve a company
* [list_ats_companies](docs/sdks/company/README.md#list_ats_companies) - List all companies
* [list_crm_companies](docs/sdks/company/README.md#list_crm_companies) - List all companies
* [list_enrich_companies](docs/sdks/company/README.md#list_enrich_companies) - Retrieve enrichment information for a company
* [list_hris_companies](docs/sdks/company/README.md#list_hris_companies) - List all companies
* [patch_ats_company](docs/sdks/company/README.md#patch_ats_company) - Update a company
* [patch_crm_company](docs/sdks/company/README.md#patch_crm_company) - Update a company
* [patch_hris_company](docs/sdks/company/README.md#patch_hris_company) - Update a company
* [remove_ats_company](docs/sdks/company/README.md#remove_ats_company) - Remove a company
* [remove_crm_company](docs/sdks/company/README.md#remove_crm_company) - Remove a company
* [remove_hris_company](docs/sdks/company/README.md#remove_hris_company) - Remove a company
* [update_ats_company](docs/sdks/company/README.md#update_ats_company) - Update a company
* [update_crm_company](docs/sdks/company/README.md#update_crm_company) - Update a company
* [update_hris_company](docs/sdks/company/README.md#update_hris_company) - Update a company

### [connection](docs/sdks/connection/README.md)

* [create_unified_connection](docs/sdks/connection/README.md#create_unified_connection) - Create connection
* [get_unified_connection](docs/sdks/connection/README.md#get_unified_connection) - Retrieve connection
* [list_unified_connections](docs/sdks/connection/README.md#list_unified_connections) - List all connections
* [patch_unified_connection](docs/sdks/connection/README.md#patch_unified_connection) - Update connection
* [remove_unified_connection](docs/sdks/connection/README.md#remove_unified_connection) - Remove connection
* [update_unified_connection](docs/sdks/connection/README.md#update_unified_connection) - Update connection

### [contact](docs/sdks/contact/README.md)

* [create_accounting_contact](docs/sdks/contact/README.md#create_accounting_contact) - Create a contact
* [create_crm_contact](docs/sdks/contact/README.md#create_crm_contact) - Create a contact
* [create_uc_contact](docs/sdks/contact/README.md#create_uc_contact) - Create a contact
* [get_accounting_contact](docs/sdks/contact/README.md#get_accounting_contact) - Retrieve a contact
* [get_crm_contact](docs/sdks/contact/README.md#get_crm_contact) - Retrieve a contact
* [get_uc_contact](docs/sdks/contact/README.md#get_uc_contact) - Retrieve a contact
* [list_accounting_contacts](docs/sdks/contact/README.md#list_accounting_contacts) - List all contacts
* [list_crm_contacts](docs/sdks/contact/README.md#list_crm_contacts) - List all contacts
* [list_uc_contacts](docs/sdks/contact/README.md#list_uc_contacts) - List all contacts
* [patch_accounting_contact](docs/sdks/contact/README.md#patch_accounting_contact) - Update a contact
* [patch_crm_contact](docs/sdks/contact/README.md#patch_crm_contact) - Update a contact
* [patch_uc_contact](docs/sdks/contact/README.md#patch_uc_contact) - Update a contact
* [remove_accounting_contact](docs/sdks/contact/README.md#remove_accounting_contact) - Remove a contact
* [remove_crm_contact](docs/sdks/contact/README.md#remove_crm_contact) - Remove a contact
* [remove_uc_contact](docs/sdks/contact/README.md#remove_uc_contact) - Remove a contact
* [update_accounting_contact](docs/sdks/contact/README.md#update_accounting_contact) - Update a contact
* [update_crm_contact](docs/sdks/contact/README.md#update_crm_contact) - Update a contact
* [update_uc_contact](docs/sdks/contact/README.md#update_uc_contact) - Update a contact

### [course](docs/sdks/course/README.md)

* [create_lms_course](docs/sdks/course/README.md#create_lms_course) - Create a course
* [get_lms_course](docs/sdks/course/README.md#get_lms_course) - Retrieve a course
* [list_lms_courses](docs/sdks/course/README.md#list_lms_courses) - List all courses
* [patch_lms_course](docs/sdks/course/README.md#patch_lms_course) - Update a course
* [remove_lms_course](docs/sdks/course/README.md#remove_lms_course) - Remove a course
* [update_lms_course](docs/sdks/course/README.md#update_lms_course) - Update a course

### [creditmemo](docs/sdks/creditmemo/README.md)

* [create_accounting_creditmemo](docs/sdks/creditmemo/README.md#create_accounting_creditmemo) - Create a creditmemo
* [get_accounting_creditmemo](docs/sdks/creditmemo/README.md#get_accounting_creditmemo) - Retrieve a creditmemo
* [list_accounting_creditmemoes](docs/sdks/creditmemo/README.md#list_accounting_creditmemoes) - List all creditmemoes
* [patch_accounting_creditmemo](docs/sdks/creditmemo/README.md#patch_accounting_creditmemo) - Update a creditmemo
* [remove_accounting_creditmemo](docs/sdks/creditmemo/README.md#remove_accounting_creditmemo) - Remove a creditmemo
* [update_accounting_creditmemo](docs/sdks/creditmemo/README.md#update_accounting_creditmemo) - Update a creditmemo

### [crm](docs/sdks/crm/README.md)

* [create_crm_company](docs/sdks/crm/README.md#create_crm_company) - Create a company
* [create_crm_contact](docs/sdks/crm/README.md#create_crm_contact) - Create a contact
* [create_crm_deal](docs/sdks/crm/README.md#create_crm_deal) - Create a deal
* [create_crm_event](docs/sdks/crm/README.md#create_crm_event) - Create an event
* [create_crm_lead](docs/sdks/crm/README.md#create_crm_lead) - Create a lead
* [create_crm_pipeline](docs/sdks/crm/README.md#create_crm_pipeline) - Create a pipeline
* [get_crm_company](docs/sdks/crm/README.md#get_crm_company) - Retrieve a company
* [get_crm_contact](docs/sdks/crm/README.md#get_crm_contact) - Retrieve a contact
* [get_crm_deal](docs/sdks/crm/README.md#get_crm_deal) - Retrieve a deal
* [get_crm_event](docs/sdks/crm/README.md#get_crm_event) - Retrieve an event
* [get_crm_lead](docs/sdks/crm/README.md#get_crm_lead) - Retrieve a lead
* [get_crm_pipeline](docs/sdks/crm/README.md#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_companies](docs/sdks/crm/README.md#list_crm_companies) - List all companies
* [list_crm_contacts](docs/sdks/crm/README.md#list_crm_contacts) - List all contacts
* [list_crm_deals](docs/sdks/crm/README.md#list_crm_deals) - List all deals
* [list_crm_events](docs/sdks/crm/README.md#list_crm_events) - List all events
* [list_crm_leads](docs/sdks/crm/README.md#list_crm_leads) - List all leads
* [list_crm_pipelines](docs/sdks/crm/README.md#list_crm_pipelines) - List all pipelines
* [patch_crm_company](docs/sdks/crm/README.md#patch_crm_company) - Update a company
* [patch_crm_contact](docs/sdks/crm/README.md#patch_crm_contact) - Update a contact
* [patch_crm_deal](docs/sdks/crm/README.md#patch_crm_deal) - Update a deal
* [patch_crm_event](docs/sdks/crm/README.md#patch_crm_event) - Update an event
* [patch_crm_lead](docs/sdks/crm/README.md#patch_crm_lead) - Update a lead
* [patch_crm_pipeline](docs/sdks/crm/README.md#patch_crm_pipeline) - Update a pipeline
* [remove_crm_company](docs/sdks/crm/README.md#remove_crm_company) - Remove a company
* [remove_crm_contact](docs/sdks/crm/README.md#remove_crm_contact) - Remove a contact
* [remove_crm_deal](docs/sdks/crm/README.md#remove_crm_deal) - Remove a deal
* [remove_crm_event](docs/sdks/crm/README.md#remove_crm_event) - Remove an event
* [remove_crm_lead](docs/sdks/crm/README.md#remove_crm_lead) - Remove a lead
* [remove_crm_pipeline](docs/sdks/crm/README.md#remove_crm_pipeline) - Remove a pipeline
* [update_crm_company](docs/sdks/crm/README.md#update_crm_company) - Update a company
* [update_crm_contact](docs/sdks/crm/README.md#update_crm_contact) - Update a contact
* [update_crm_deal](docs/sdks/crm/README.md#update_crm_deal) - Update a deal
* [update_crm_event](docs/sdks/crm/README.md#update_crm_event) - Update an event
* [update_crm_lead](docs/sdks/crm/README.md#update_crm_lead) - Update a lead
* [update_crm_pipeline](docs/sdks/crm/README.md#update_crm_pipeline) - Update a pipeline

### [customer](docs/sdks/customer/README.md)

* [create_ticketing_customer](docs/sdks/customer/README.md#create_ticketing_customer) - Create a customer
* [get_ticketing_customer](docs/sdks/customer/README.md#get_ticketing_customer) - Retrieve a customer
* [list_ticketing_customers](docs/sdks/customer/README.md#list_ticketing_customers) - List all customers
* [patch_ticketing_customer](docs/sdks/customer/README.md#patch_ticketing_customer) - Update a customer
* [remove_ticketing_customer](docs/sdks/customer/README.md#remove_ticketing_customer) - Remove a customer
* [update_ticketing_customer](docs/sdks/customer/README.md#update_ticketing_customer) - Update a customer

### [deal](docs/sdks/deal/README.md)

* [create_crm_deal](docs/sdks/deal/README.md#create_crm_deal) - Create a deal
* [get_crm_deal](docs/sdks/deal/README.md#get_crm_deal) - Retrieve a deal
* [list_crm_deals](docs/sdks/deal/README.md#list_crm_deals) - List all deals
* [patch_crm_deal](docs/sdks/deal/README.md#patch_crm_deal) - Update a deal
* [remove_crm_deal](docs/sdks/deal/README.md#remove_crm_deal) - Remove a deal
* [update_crm_deal](docs/sdks/deal/README.md#update_crm_deal) - Update a deal

### [device](docs/sdks/device/README.md)

* [create_hris_device](docs/sdks/device/README.md#create_hris_device) - Create a device
* [get_hris_device](docs/sdks/device/README.md#get_hris_device) - Retrieve a device
* [list_hris_devices](docs/sdks/device/README.md#list_hris_devices) - List all devices
* [patch_hris_device](docs/sdks/device/README.md#patch_hris_device) - Update a device
* [remove_hris_device](docs/sdks/device/README.md#remove_hris_device) - Remove a device
* [update_hris_device](docs/sdks/device/README.md#update_hris_device) - Update a device

### [document](docs/sdks/document/README.md)

* [create_ats_document](docs/sdks/document/README.md#create_ats_document) - Create a document
* [get_ats_document](docs/sdks/document/README.md#get_ats_document) - Retrieve a document
* [list_ats_documents](docs/sdks/document/README.md#list_ats_documents) - List all documents
* [patch_ats_document](docs/sdks/document/README.md#patch_ats_document) - Update a document
* [remove_ats_document](docs/sdks/document/README.md#remove_ats_document) - Remove a document
* [update_ats_document](docs/sdks/document/README.md#update_ats_document) - Update a document

### [embedding](docs/sdks/embedding/README.md)

* [create_genai_embedding](docs/sdks/embedding/README.md#create_genai_embedding) - Create an embedding

### [employee](docs/sdks/employee/README.md)

* [create_hris_employee](docs/sdks/employee/README.md#create_hris_employee) - Create an employee
* [get_hris_employee](docs/sdks/employee/README.md#get_hris_employee) - Retrieve an employee
* [list_hris_employees](docs/sdks/employee/README.md#list_hris_employees) - List all employees
* [patch_hris_employee](docs/sdks/employee/README.md#patch_hris_employee) - Update an employee
* [remove_hris_employee](docs/sdks/employee/README.md#remove_hris_employee) - Remove an employee
* [update_hris_employee](docs/sdks/employee/README.md#update_hris_employee) - Update an employee

### [enrich](docs/sdks/enrich/README.md)

* [list_enrich_companies](docs/sdks/enrich/README.md#list_enrich_companies) - Retrieve enrichment information for a company
* [list_enrich_people](docs/sdks/enrich/README.md#list_enrich_people) - Retrieve enrichment information for a person

### [event](docs/sdks/event/README.md)

* [create_calendar_event](docs/sdks/event/README.md#create_calendar_event) - Create an event
* [create_crm_event](docs/sdks/event/README.md#create_crm_event) - Create an event
* [get_calendar_event](docs/sdks/event/README.md#get_calendar_event) - Retrieve an event
* [get_crm_event](docs/sdks/event/README.md#get_crm_event) - Retrieve an event
* [list_calendar_events](docs/sdks/event/README.md#list_calendar_events) - List all events
* [list_crm_events](docs/sdks/event/README.md#list_crm_events) - List all events
* [patch_calendar_event](docs/sdks/event/README.md#patch_calendar_event) - Update an event
* [patch_crm_event](docs/sdks/event/README.md#patch_crm_event) - Update an event
* [remove_calendar_event](docs/sdks/event/README.md#remove_calendar_event) - Remove an event
* [remove_crm_event](docs/sdks/event/README.md#remove_crm_event) - Remove an event
* [update_calendar_event](docs/sdks/event/README.md#update_calendar_event) - Update an event
* [update_crm_event](docs/sdks/event/README.md#update_crm_event) - Update an event

### [expense](docs/sdks/expense/README.md)

* [create_accounting_expense](docs/sdks/expense/README.md#create_accounting_expense) - Create an expense
* [get_accounting_expense](docs/sdks/expense/README.md#get_accounting_expense) - Retrieve an expense
* [list_accounting_expenses](docs/sdks/expense/README.md#list_accounting_expenses) - List all expenses
* [patch_accounting_expense](docs/sdks/expense/README.md#patch_accounting_expense) - Update an expense
* [remove_accounting_expense](docs/sdks/expense/README.md#remove_accounting_expense) - Remove an expense
* [update_accounting_expense](docs/sdks/expense/README.md#update_accounting_expense) - Update an expense

### [file](docs/sdks/file/README.md)

* [create_storage_file](docs/sdks/file/README.md#create_storage_file) - Create a file
* [get_storage_file](docs/sdks/file/README.md#get_storage_file) - Retrieve a file
* [list_storage_files](docs/sdks/file/README.md#list_storage_files) - List all files
* [patch_storage_file](docs/sdks/file/README.md#patch_storage_file) - Update a file
* [remove_storage_file](docs/sdks/file/README.md#remove_storage_file) - Remove a file
* [update_storage_file](docs/sdks/file/README.md#update_storage_file) - Update a file

### [genai](docs/sdks/genai/README.md)

* [create_genai_embedding](docs/sdks/genai/README.md#create_genai_embedding) - Create an embedding
* [create_genai_prompt](docs/sdks/genai/README.md#create_genai_prompt) - Create a prompt
* [get_genai_model](docs/sdks/genai/README.md#get_genai_model) - Retrieve a model
* [list_genai_models](docs/sdks/genai/README.md#list_genai_models) - List all models

### [group](docs/sdks/group/README.md)

* [create_hris_group](docs/sdks/group/README.md#create_hris_group) - Create a group
* [create_scim_groups](docs/sdks/group/README.md#create_scim_groups) - Create group
* [get_hris_group](docs/sdks/group/README.md#get_hris_group) - Retrieve a group
* [get_scim_groups](docs/sdks/group/README.md#get_scim_groups) - Get group
* [list_hris_groups](docs/sdks/group/README.md#list_hris_groups) - List all groups
* [list_scim_groups](docs/sdks/group/README.md#list_scim_groups) - List groups
* [patch_hris_group](docs/sdks/group/README.md#patch_hris_group) - Update a group
* [patch_scim_groups](docs/sdks/group/README.md#patch_scim_groups) - Update group
* [remove_hris_group](docs/sdks/group/README.md#remove_hris_group) - Remove a group
* [remove_scim_groups](docs/sdks/group/README.md#remove_scim_groups) - Delete group
* [update_hris_group](docs/sdks/group/README.md#update_hris_group) - Update a group
* [update_scim_groups](docs/sdks/group/README.md#update_scim_groups) - Update group

### [hris](docs/sdks/hris/README.md)

* [create_hris_company](docs/sdks/hris/README.md#create_hris_company) - Create a company
* [create_hris_device](docs/sdks/hris/README.md#create_hris_device) - Create a device
* [create_hris_employee](docs/sdks/hris/README.md#create_hris_employee) - Create an employee
* [create_hris_group](docs/sdks/hris/README.md#create_hris_group) - Create a group
* [create_hris_location](docs/sdks/hris/README.md#create_hris_location) - Create a location
* [create_hris_timeshift](docs/sdks/hris/README.md#create_hris_timeshift) - Create a timeshift
* [get_hris_company](docs/sdks/hris/README.md#get_hris_company) - Retrieve a company
* [get_hris_device](docs/sdks/hris/README.md#get_hris_device) - Retrieve a device
* [get_hris_employee](docs/sdks/hris/README.md#get_hris_employee) - Retrieve an employee
* [get_hris_group](docs/sdks/hris/README.md#get_hris_group) - Retrieve a group
* [get_hris_location](docs/sdks/hris/README.md#get_hris_location) - Retrieve a location
* [get_hris_payslip](docs/sdks/hris/README.md#get_hris_payslip) - Retrieve a payslip
* [get_hris_timeoff](docs/sdks/hris/README.md#get_hris_timeoff) - Retrieve a timeoff
* [get_hris_timeshift](docs/sdks/hris/README.md#get_hris_timeshift) - Retrieve a timeshift
* [list_hris_companies](docs/sdks/hris/README.md#list_hris_companies) - List all companies
* [list_hris_devices](docs/sdks/hris/README.md#list_hris_devices) - List all devices
* [list_hris_employees](docs/sdks/hris/README.md#list_hris_employees) - List all employees
* [list_hris_groups](docs/sdks/hris/README.md#list_hris_groups) - List all groups
* [list_hris_locations](docs/sdks/hris/README.md#list_hris_locations) - List all locations
* [list_hris_payslips](docs/sdks/hris/README.md#list_hris_payslips) - List all payslips
* [list_hris_timeoffs](docs/sdks/hris/README.md#list_hris_timeoffs) - List all timeoffs
* [list_hris_timeshifts](docs/sdks/hris/README.md#list_hris_timeshifts) - List all timeshifts
* [patch_hris_company](docs/sdks/hris/README.md#patch_hris_company) - Update a company
* [patch_hris_device](docs/sdks/hris/README.md#patch_hris_device) - Update a device
* [patch_hris_employee](docs/sdks/hris/README.md#patch_hris_employee) - Update an employee
* [patch_hris_group](docs/sdks/hris/README.md#patch_hris_group) - Update a group
* [patch_hris_location](docs/sdks/hris/README.md#patch_hris_location) - Update a location
* [patch_hris_timeshift](docs/sdks/hris/README.md#patch_hris_timeshift) - Update a timeshift
* [remove_hris_company](docs/sdks/hris/README.md#remove_hris_company) - Remove a company
* [remove_hris_device](docs/sdks/hris/README.md#remove_hris_device) - Remove a device
* [remove_hris_employee](docs/sdks/hris/README.md#remove_hris_employee) - Remove an employee
* [remove_hris_group](docs/sdks/hris/README.md#remove_hris_group) - Remove a group
* [remove_hris_location](docs/sdks/hris/README.md#remove_hris_location) - Remove a location
* [remove_hris_timeshift](docs/sdks/hris/README.md#remove_hris_timeshift) - Remove a timeshift
* [update_hris_company](docs/sdks/hris/README.md#update_hris_company) - Update a company
* [update_hris_device](docs/sdks/hris/README.md#update_hris_device) - Update a device
* [update_hris_employee](docs/sdks/hris/README.md#update_hris_employee) - Update an employee
* [update_hris_group](docs/sdks/hris/README.md#update_hris_group) - Update a group
* [update_hris_location](docs/sdks/hris/README.md#update_hris_location) - Update a location
* [update_hris_timeshift](docs/sdks/hris/README.md#update_hris_timeshift) - Update a timeshift

### [instructor](docs/sdks/instructor/README.md)

* [create_lms_instructor](docs/sdks/instructor/README.md#create_lms_instructor) - Create an instructor
* [get_lms_instructor](docs/sdks/instructor/README.md#get_lms_instructor) - Retrieve an instructor
* [list_lms_instructors](docs/sdks/instructor/README.md#list_lms_instructors) - List all instructors
* [patch_lms_instructor](docs/sdks/instructor/README.md#patch_lms_instructor) - Update an instructor
* [remove_lms_instructor](docs/sdks/instructor/README.md#remove_lms_instructor) - Remove an instructor
* [update_lms_instructor](docs/sdks/instructor/README.md#update_lms_instructor) - Update an instructor

### [integration](docs/sdks/integration/README.md)

* [get_unified_integration_auth](docs/sdks/integration/README.md#get_unified_integration_auth) - Authorize new connection
* [list_unified_integration_workspaces](docs/sdks/integration/README.md#list_unified_integration_workspaces) - Returns all activated integrations in a workspace
* [list_unified_integrations](docs/sdks/integration/README.md#list_unified_integrations) - Returns all integrations

### [interview](docs/sdks/interview/README.md)

* [create_ats_interview](docs/sdks/interview/README.md#create_ats_interview) - Create an interview
* [get_ats_interview](docs/sdks/interview/README.md#get_ats_interview) - Retrieve an interview
* [list_ats_interviews](docs/sdks/interview/README.md#list_ats_interviews) - List all interviews
* [patch_ats_interview](docs/sdks/interview/README.md#patch_ats_interview) - Update an interview
* [remove_ats_interview](docs/sdks/interview/README.md#remove_ats_interview) - Remove an interview
* [update_ats_interview](docs/sdks/interview/README.md#update_ats_interview) - Update an interview

### [inventory](docs/sdks/inventory/README.md)

* [create_commerce_inventory](docs/sdks/inventory/README.md#create_commerce_inventory) - Create an inventory
* [get_commerce_inventory](docs/sdks/inventory/README.md#get_commerce_inventory) - Retrieve an inventory
* [list_commerce_inventories](docs/sdks/inventory/README.md#list_commerce_inventories) - List all inventories
* [patch_commerce_inventory](docs/sdks/inventory/README.md#patch_commerce_inventory) - Update an inventory
* [remove_commerce_inventory](docs/sdks/inventory/README.md#remove_commerce_inventory) - Remove an inventory
* [update_commerce_inventory](docs/sdks/inventory/README.md#update_commerce_inventory) - Update an inventory

### [invoice](docs/sdks/invoice/README.md)

* [create_accounting_invoice](docs/sdks/invoice/README.md#create_accounting_invoice) - Create an invoice
* [get_accounting_invoice](docs/sdks/invoice/README.md#get_accounting_invoice) - Retrieve an invoice
* [list_accounting_invoices](docs/sdks/invoice/README.md#list_accounting_invoices) - List all invoices
* [patch_accounting_invoice](docs/sdks/invoice/README.md#patch_accounting_invoice) - Update an invoice
* [remove_accounting_invoice](docs/sdks/invoice/README.md#remove_accounting_invoice) - Remove an invoice
* [update_accounting_invoice](docs/sdks/invoice/README.md#update_accounting_invoice) - Update an invoice

### [issue](docs/sdks/issue/README.md)

* [get_unified_issue](docs/sdks/issue/README.md#get_unified_issue) - Retrieve support issue
* [list_unified_issues](docs/sdks/issue/README.md#list_unified_issues) - List support issues

### [item](docs/sdks/item/README.md)

* [create_commerce_item](docs/sdks/item/README.md#create_commerce_item) - Create an item
* [get_commerce_item](docs/sdks/item/README.md#get_commerce_item) - Retrieve an item
* [list_commerce_items](docs/sdks/item/README.md#list_commerce_items) - List all items
* [patch_commerce_item](docs/sdks/item/README.md#patch_commerce_item) - Update an item
* [remove_commerce_item](docs/sdks/item/README.md#remove_commerce_item) - Remove an item
* [update_commerce_item](docs/sdks/item/README.md#update_commerce_item) - Update an item

### [job](docs/sdks/job/README.md)

* [create_ats_job](docs/sdks/job/README.md#create_ats_job) - Create a job
* [get_ats_job](docs/sdks/job/README.md#get_ats_job) - Retrieve a job
* [list_ats_jobs](docs/sdks/job/README.md#list_ats_jobs) - List all jobs
* [patch_ats_job](docs/sdks/job/README.md#patch_ats_job) - Update a job
* [remove_ats_job](docs/sdks/job/README.md#remove_ats_job) - Remove a job
* [update_ats_job](docs/sdks/job/README.md#update_ats_job) - Update a job

### [journal](docs/sdks/journal/README.md)

* [create_accounting_journal](docs/sdks/journal/README.md#create_accounting_journal) - Create a journal
* [get_accounting_journal](docs/sdks/journal/README.md#get_accounting_journal) - Retrieve a journal
* [list_accounting_journals](docs/sdks/journal/README.md#list_accounting_journals) - List all journals
* [patch_accounting_journal](docs/sdks/journal/README.md#patch_accounting_journal) - Update a journal
* [remove_accounting_journal](docs/sdks/journal/README.md#remove_accounting_journal) - Remove a journal
* [update_accounting_journal](docs/sdks/journal/README.md#update_accounting_journal) - Update a journal

### [kms](docs/sdks/kms/README.md)

* [create_kms_comment](docs/sdks/kms/README.md#create_kms_comment) - Create a comment
* [create_kms_page](docs/sdks/kms/README.md#create_kms_page) - Create a page
* [create_kms_space](docs/sdks/kms/README.md#create_kms_space) - Create a space
* [get_kms_comment](docs/sdks/kms/README.md#get_kms_comment) - Retrieve a comment
* [get_kms_page](docs/sdks/kms/README.md#get_kms_page) - Retrieve a page
* [get_kms_space](docs/sdks/kms/README.md#get_kms_space) - Retrieve a space
* [list_kms_comments](docs/sdks/kms/README.md#list_kms_comments) - List all comments
* [list_kms_pages](docs/sdks/kms/README.md#list_kms_pages) - List all pages
* [list_kms_spaces](docs/sdks/kms/README.md#list_kms_spaces) - List all spaces
* [patch_kms_comment](docs/sdks/kms/README.md#patch_kms_comment) - Update a comment
* [patch_kms_page](docs/sdks/kms/README.md#patch_kms_page) - Update a page
* [patch_kms_space](docs/sdks/kms/README.md#patch_kms_space) - Update a space
* [remove_kms_comment](docs/sdks/kms/README.md#remove_kms_comment) - Remove a comment
* [remove_kms_page](docs/sdks/kms/README.md#remove_kms_page) - Remove a page
* [remove_kms_space](docs/sdks/kms/README.md#remove_kms_space) - Remove a space
* [update_kms_comment](docs/sdks/kms/README.md#update_kms_comment) - Update a comment
* [update_kms_page](docs/sdks/kms/README.md#update_kms_page) - Update a page
* [update_kms_space](docs/sdks/kms/README.md#update_kms_space) - Update a space

### [lead](docs/sdks/lead/README.md)

* [create_crm_lead](docs/sdks/lead/README.md#create_crm_lead) - Create a lead
* [get_crm_lead](docs/sdks/lead/README.md#get_crm_lead) - Retrieve a lead
* [list_crm_leads](docs/sdks/lead/README.md#list_crm_leads) - List all leads
* [patch_crm_lead](docs/sdks/lead/README.md#patch_crm_lead) - Update a lead
* [remove_crm_lead](docs/sdks/lead/README.md#remove_crm_lead) - Remove a lead
* [update_crm_lead](docs/sdks/lead/README.md#update_crm_lead) - Update a lead

### [link](docs/sdks/link/README.md)

* [create_calendar_link](docs/sdks/link/README.md#create_calendar_link) - Create a link
* [create_payment_link](docs/sdks/link/README.md#create_payment_link) - Create a link
* [get_calendar_link](docs/sdks/link/README.md#get_calendar_link) - Retrieve a link
* [get_payment_link](docs/sdks/link/README.md#get_payment_link) - Retrieve a link
* [list_calendar_links](docs/sdks/link/README.md#list_calendar_links) - List all links
* [list_payment_links](docs/sdks/link/README.md#list_payment_links) - List all links
* [patch_calendar_link](docs/sdks/link/README.md#patch_calendar_link) - Update a link
* [patch_payment_link](docs/sdks/link/README.md#patch_payment_link) - Update a link
* [remove_calendar_link](docs/sdks/link/README.md#remove_calendar_link) - Remove a link
* [remove_payment_link](docs/sdks/link/README.md#remove_payment_link) - Remove a link
* [update_calendar_link](docs/sdks/link/README.md#update_calendar_link) - Update a link
* [update_payment_link](docs/sdks/link/README.md#update_payment_link) - Update a link

### [list](docs/sdks/list/README.md)

* [create_martech_list](docs/sdks/list/README.md#create_martech_list) - Create a list
* [get_martech_list](docs/sdks/list/README.md#get_martech_list) - Retrieve a list
* [list_martech_lists](docs/sdks/list/README.md#list_martech_lists) - List all lists
* [patch_martech_list](docs/sdks/list/README.md#patch_martech_list) - Update a list
* [remove_martech_list](docs/sdks/list/README.md#remove_martech_list) - Remove a list
* [update_martech_list](docs/sdks/list/README.md#update_martech_list) - Update a list

### [lms](docs/sdks/lms/README.md)

* [create_lms_class](docs/sdks/lms/README.md#create_lms_class) - Create a class
* [create_lms_course](docs/sdks/lms/README.md#create_lms_course) - Create a course
* [create_lms_instructor](docs/sdks/lms/README.md#create_lms_instructor) - Create an instructor
* [create_lms_student](docs/sdks/lms/README.md#create_lms_student) - Create a student
* [get_lms_class](docs/sdks/lms/README.md#get_lms_class) - Retrieve a class
* [get_lms_course](docs/sdks/lms/README.md#get_lms_course) - Retrieve a course
* [get_lms_instructor](docs/sdks/lms/README.md#get_lms_instructor) - Retrieve an instructor
* [get_lms_student](docs/sdks/lms/README.md#get_lms_student) - Retrieve a student
* [list_lms_classes](docs/sdks/lms/README.md#list_lms_classes) - List all classes
* [list_lms_courses](docs/sdks/lms/README.md#list_lms_courses) - List all courses
* [list_lms_instructors](docs/sdks/lms/README.md#list_lms_instructors) - List all instructors
* [list_lms_students](docs/sdks/lms/README.md#list_lms_students) - List all students
* [patch_lms_class](docs/sdks/lms/README.md#patch_lms_class) - Update a class
* [patch_lms_course](docs/sdks/lms/README.md#patch_lms_course) - Update a course
* [patch_lms_instructor](docs/sdks/lms/README.md#patch_lms_instructor) - Update an instructor
* [patch_lms_student](docs/sdks/lms/README.md#patch_lms_student) - Update a student
* [remove_lms_class](docs/sdks/lms/README.md#remove_lms_class) - Remove a class
* [remove_lms_course](docs/sdks/lms/README.md#remove_lms_course) - Remove a course
* [remove_lms_instructor](docs/sdks/lms/README.md#remove_lms_instructor) - Remove an instructor
* [remove_lms_student](docs/sdks/lms/README.md#remove_lms_student) - Remove a student
* [update_lms_class](docs/sdks/lms/README.md#update_lms_class) - Update a class
* [update_lms_course](docs/sdks/lms/README.md#update_lms_course) - Update a course
* [update_lms_instructor](docs/sdks/lms/README.md#update_lms_instructor) - Update an instructor
* [update_lms_student](docs/sdks/lms/README.md#update_lms_student) - Update a student

### [location](docs/sdks/location/README.md)

* [create_commerce_location](docs/sdks/location/README.md#create_commerce_location) - Create a location
* [create_hris_location](docs/sdks/location/README.md#create_hris_location) - Create a location
* [get_commerce_location](docs/sdks/location/README.md#get_commerce_location) - Retrieve a location
* [get_hris_location](docs/sdks/location/README.md#get_hris_location) - Retrieve a location
* [list_commerce_locations](docs/sdks/location/README.md#list_commerce_locations) - List all locations
* [list_hris_locations](docs/sdks/location/README.md#list_hris_locations) - List all locations
* [patch_commerce_location](docs/sdks/location/README.md#patch_commerce_location) - Update a location
* [patch_hris_location](docs/sdks/location/README.md#patch_hris_location) - Update a location
* [remove_commerce_location](docs/sdks/location/README.md#remove_commerce_location) - Remove a location
* [remove_hris_location](docs/sdks/location/README.md#remove_hris_location) - Remove a location
* [update_commerce_location](docs/sdks/location/README.md#update_commerce_location) - Update a location
* [update_hris_location](docs/sdks/location/README.md#update_hris_location) - Update a location

### [login](docs/sdks/login/README.md)

* [get_unified_integration_login](docs/sdks/login/README.md#get_unified_integration_login) - Sign in a user

### [martech](docs/sdks/martech/README.md)

* [create_martech_list](docs/sdks/martech/README.md#create_martech_list) - Create a list
* [create_martech_member](docs/sdks/martech/README.md#create_martech_member) - Create a member
* [get_martech_list](docs/sdks/martech/README.md#get_martech_list) - Retrieve a list
* [get_martech_member](docs/sdks/martech/README.md#get_martech_member) - Retrieve a member
* [list_martech_lists](docs/sdks/martech/README.md#list_martech_lists) - List all lists
* [list_martech_members](docs/sdks/martech/README.md#list_martech_members) - List all members
* [patch_martech_list](docs/sdks/martech/README.md#patch_martech_list) - Update a list
* [patch_martech_member](docs/sdks/martech/README.md#patch_martech_member) - Update a member
* [remove_martech_list](docs/sdks/martech/README.md#remove_martech_list) - Remove a list
* [remove_martech_member](docs/sdks/martech/README.md#remove_martech_member) - Remove a member
* [update_martech_list](docs/sdks/martech/README.md#update_martech_list) - Update a list
* [update_martech_member](docs/sdks/martech/README.md#update_martech_member) - Update a member

### [member](docs/sdks/member/README.md)

* [create_martech_member](docs/sdks/member/README.md#create_martech_member) - Create a member
* [get_martech_member](docs/sdks/member/README.md#get_martech_member) - Retrieve a member
* [list_martech_members](docs/sdks/member/README.md#list_martech_members) - List all members
* [patch_martech_member](docs/sdks/member/README.md#patch_martech_member) - Update a member
* [remove_martech_member](docs/sdks/member/README.md#remove_martech_member) - Remove a member
* [update_martech_member](docs/sdks/member/README.md#update_martech_member) - Update a member

### [message](docs/sdks/message/README.md)

* [create_messaging_message](docs/sdks/message/README.md#create_messaging_message) - Create a message
* [get_messaging_message](docs/sdks/message/README.md#get_messaging_message) - Retrieve a message
* [list_messaging_messages](docs/sdks/message/README.md#list_messaging_messages) - List all messages
* [patch_messaging_message](docs/sdks/message/README.md#patch_messaging_message) - Update a message
* [remove_messaging_message](docs/sdks/message/README.md#remove_messaging_message) - Remove a message
* [update_messaging_message](docs/sdks/message/README.md#update_messaging_message) - Update a message

### [messaging](docs/sdks/messaging/README.md)

* [create_messaging_message](docs/sdks/messaging/README.md#create_messaging_message) - Create a message
* [get_messaging_channel](docs/sdks/messaging/README.md#get_messaging_channel) - Retrieve a channel
* [get_messaging_message](docs/sdks/messaging/README.md#get_messaging_message) - Retrieve a message
* [list_messaging_channels](docs/sdks/messaging/README.md#list_messaging_channels) - List all channels
* [list_messaging_messages](docs/sdks/messaging/README.md#list_messaging_messages) - List all messages
* [patch_messaging_message](docs/sdks/messaging/README.md#patch_messaging_message) - Update a message
* [remove_messaging_message](docs/sdks/messaging/README.md#remove_messaging_message) - Remove a message
* [update_messaging_message](docs/sdks/messaging/README.md#update_messaging_message) - Update a message

### [metadata](docs/sdks/metadata/README.md)

* [create_metadata_metadata](docs/sdks/metadata/README.md#create_metadata_metadata) - Create a metadata
* [get_metadata_metadata](docs/sdks/metadata/README.md#get_metadata_metadata) - Retrieve a metadata
* [list_metadata_metadatas](docs/sdks/metadata/README.md#list_metadata_metadatas) - List all metadatas
* [patch_metadata_metadata](docs/sdks/metadata/README.md#patch_metadata_metadata) - Update a metadata
* [remove_metadata_metadata](docs/sdks/metadata/README.md#remove_metadata_metadata) - Remove a metadata
* [update_metadata_metadata](docs/sdks/metadata/README.md#update_metadata_metadata) - Update a metadata

### [model](docs/sdks/model/README.md)

* [get_genai_model](docs/sdks/model/README.md#get_genai_model) - Retrieve a model
* [list_genai_models](docs/sdks/model/README.md#list_genai_models) - List all models

### [note](docs/sdks/note/README.md)

* [create_ticketing_note](docs/sdks/note/README.md#create_ticketing_note) - Create a note
* [get_ticketing_note](docs/sdks/note/README.md#get_ticketing_note) - Retrieve a note
* [list_ticketing_notes](docs/sdks/note/README.md#list_ticketing_notes) - List all notes
* [patch_ticketing_note](docs/sdks/note/README.md#patch_ticketing_note) - Update a note
* [remove_ticketing_note](docs/sdks/note/README.md#remove_ticketing_note) - Remove a note
* [update_ticketing_note](docs/sdks/note/README.md#update_ticketing_note) - Update a note

### [order](docs/sdks/order/README.md)

* [create_accounting_order](docs/sdks/order/README.md#create_accounting_order) - Create an order
* [get_accounting_order](docs/sdks/order/README.md#get_accounting_order) - Retrieve an order
* [list_accounting_orders](docs/sdks/order/README.md#list_accounting_orders) - List all orders
* [patch_accounting_order](docs/sdks/order/README.md#patch_accounting_order) - Update an order
* [remove_accounting_order](docs/sdks/order/README.md#remove_accounting_order) - Remove an order
* [update_accounting_order](docs/sdks/order/README.md#update_accounting_order) - Update an order

### [organization](docs/sdks/organization/README.md)

* [create_repo_organization](docs/sdks/organization/README.md#create_repo_organization) - Create an organization
* [get_accounting_organization](docs/sdks/organization/README.md#get_accounting_organization) - Retrieve an organization
* [get_repo_organization](docs/sdks/organization/README.md#get_repo_organization) - Retrieve an organization
* [list_accounting_organizations](docs/sdks/organization/README.md#list_accounting_organizations) - List all organizations
* [list_repo_organizations](docs/sdks/organization/README.md#list_repo_organizations) - List all organizations
* [patch_repo_organization](docs/sdks/organization/README.md#patch_repo_organization) - Update an organization
* [remove_repo_organization](docs/sdks/organization/README.md#remove_repo_organization) - Remove an organization
* [update_repo_organization](docs/sdks/organization/README.md#update_repo_organization) - Update an organization

### [package](docs/sdks/package/README.md)

* [get_verification_package](docs/sdks/package/README.md#get_verification_package) - Retrieve a package
* [list_verification_packages](docs/sdks/package/README.md#list_verification_packages) - List all packages

### [page](docs/sdks/page/README.md)

* [create_kms_page](docs/sdks/page/README.md#create_kms_page) - Create a page
* [get_kms_page](docs/sdks/page/README.md#get_kms_page) - Retrieve a page
* [list_kms_pages](docs/sdks/page/README.md#list_kms_pages) - List all pages
* [patch_kms_page](docs/sdks/page/README.md#patch_kms_page) - Update a page
* [remove_kms_page](docs/sdks/page/README.md#remove_kms_page) - Remove a page
* [update_kms_page](docs/sdks/page/README.md#update_kms_page) - Update a page

### [passthrough](docs/sdks/passthrough/README.md)

* [create_passthrough_json](docs/sdks/passthrough/README.md#create_passthrough_json) - Passthrough POST
* [create_passthrough_raw](docs/sdks/passthrough/README.md#create_passthrough_raw) - Passthrough POST
* [list_passthroughs](docs/sdks/passthrough/README.md#list_passthroughs) - Passthrough GET
* [patch_passthrough_json](docs/sdks/passthrough/README.md#patch_passthrough_json) - Passthrough PUT
* [patch_passthrough_raw](docs/sdks/passthrough/README.md#patch_passthrough_raw) - Passthrough PUT
* [remove_passthrough](docs/sdks/passthrough/README.md#remove_passthrough) - Passthrough DELETE
* [update_passthrough_json](docs/sdks/passthrough/README.md#update_passthrough_json) - Passthrough PUT
* [update_passthrough_raw](docs/sdks/passthrough/README.md#update_passthrough_raw) - Passthrough PUT

### [payment](docs/sdks/payment/README.md)

* [create_payment_link](docs/sdks/payment/README.md#create_payment_link) - Create a link
* [create_payment_payment](docs/sdks/payment/README.md#create_payment_payment) - Create a payment
* [create_payment_subscription](docs/sdks/payment/README.md#create_payment_subscription) - Create a subscription
* [get_payment_link](docs/sdks/payment/README.md#get_payment_link) - Retrieve a link
* [get_payment_payment](docs/sdks/payment/README.md#get_payment_payment) - Retrieve a payment
* [get_payment_payout](docs/sdks/payment/README.md#get_payment_payout) - Retrieve a payout
* [get_payment_refund](docs/sdks/payment/README.md#get_payment_refund) - Retrieve a refund
* [get_payment_subscription](docs/sdks/payment/README.md#get_payment_subscription) - Retrieve a subscription
* [list_payment_links](docs/sdks/payment/README.md#list_payment_links) - List all links
* [list_payment_payments](docs/sdks/payment/README.md#list_payment_payments) - List all payments
* [list_payment_payouts](docs/sdks/payment/README.md#list_payment_payouts) - List all payouts
* [list_payment_refunds](docs/sdks/payment/README.md#list_payment_refunds) - List all refunds
* [list_payment_subscriptions](docs/sdks/payment/README.md#list_payment_subscriptions) - List all subscriptions
* [patch_payment_link](docs/sdks/payment/README.md#patch_payment_link) - Update a link
* [patch_payment_payment](docs/sdks/payment/README.md#patch_payment_payment) - Update a payment
* [patch_payment_subscription](docs/sdks/payment/README.md#patch_payment_subscription) - Update a subscription
* [remove_payment_link](docs/sdks/payment/README.md#remove_payment_link) - Remove a link
* [remove_payment_payment](docs/sdks/payment/README.md#remove_payment_payment) - Remove a payment
* [remove_payment_subscription](docs/sdks/payment/README.md#remove_payment_subscription) - Remove a subscription
* [update_payment_link](docs/sdks/payment/README.md#update_payment_link) - Update a link
* [update_payment_payment](docs/sdks/payment/README.md#update_payment_payment) - Update a payment
* [update_payment_subscription](docs/sdks/payment/README.md#update_payment_subscription) - Update a subscription

### [payout](docs/sdks/payout/README.md)

* [get_payment_payout](docs/sdks/payout/README.md#get_payment_payout) - Retrieve a payout
* [list_payment_payouts](docs/sdks/payout/README.md#list_payment_payouts) - List all payouts

### [payslip](docs/sdks/payslip/README.md)

* [get_hris_payslip](docs/sdks/payslip/README.md#get_hris_payslip) - Retrieve a payslip
* [list_hris_payslips](docs/sdks/payslip/README.md#list_hris_payslips) - List all payslips

### [person](docs/sdks/person/README.md)

* [list_enrich_people](docs/sdks/person/README.md#list_enrich_people) - Retrieve enrichment information for a person

### [pipeline](docs/sdks/pipeline/README.md)

* [create_crm_pipeline](docs/sdks/pipeline/README.md#create_crm_pipeline) - Create a pipeline
* [get_crm_pipeline](docs/sdks/pipeline/README.md#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_pipelines](docs/sdks/pipeline/README.md#list_crm_pipelines) - List all pipelines
* [patch_crm_pipeline](docs/sdks/pipeline/README.md#patch_crm_pipeline) - Update a pipeline
* [remove_crm_pipeline](docs/sdks/pipeline/README.md#remove_crm_pipeline) - Remove a pipeline
* [update_crm_pipeline](docs/sdks/pipeline/README.md#update_crm_pipeline) - Update a pipeline

### [profitloss](docs/sdks/profitloss/README.md)

* [get_accounting_profitloss](docs/sdks/profitloss/README.md#get_accounting_profitloss) - Retrieve a profitloss
* [list_accounting_profitlosses](docs/sdks/profitloss/README.md#list_accounting_profitlosses) - List all profitlosses

### [project](docs/sdks/project/README.md)

* [create_task_project](docs/sdks/project/README.md#create_task_project) - Create a project
* [get_task_project](docs/sdks/project/README.md#get_task_project) - Retrieve a project
* [list_task_projects](docs/sdks/project/README.md#list_task_projects) - List all projects
* [patch_task_project](docs/sdks/project/README.md#patch_task_project) - Update a project
* [remove_task_project](docs/sdks/project/README.md#remove_task_project) - Remove a project
* [update_task_project](docs/sdks/project/README.md#update_task_project) - Update a project

### [prompt](docs/sdks/prompt/README.md)

* [create_genai_prompt](docs/sdks/prompt/README.md#create_genai_prompt) - Create a prompt

### [pullrequest](docs/sdks/pullrequest/README.md)

* [create_repo_pullrequest](docs/sdks/pullrequest/README.md#create_repo_pullrequest) - Create a pullrequest
* [get_repo_pullrequest](docs/sdks/pullrequest/README.md#get_repo_pullrequest) - Retrieve a pullrequest
* [list_repo_pullrequests](docs/sdks/pullrequest/README.md#list_repo_pullrequests) - List all pullrequests
* [patch_repo_pullrequest](docs/sdks/pullrequest/README.md#patch_repo_pullrequest) - Update a pullrequest
* [remove_repo_pullrequest](docs/sdks/pullrequest/README.md#remove_repo_pullrequest) - Remove a pullrequest
* [update_repo_pullrequest](docs/sdks/pullrequest/README.md#update_repo_pullrequest) - Update a pullrequest

### [purchaseorder](docs/sdks/purchaseorder/README.md)

* [create_accounting_purchaseorder](docs/sdks/purchaseorder/README.md#create_accounting_purchaseorder) - Create a purchaseorder
* [get_accounting_purchaseorder](docs/sdks/purchaseorder/README.md#get_accounting_purchaseorder) - Retrieve a purchaseorder
* [list_accounting_purchaseorders](docs/sdks/purchaseorder/README.md#list_accounting_purchaseorders) - List all purchaseorders
* [patch_accounting_purchaseorder](docs/sdks/purchaseorder/README.md#patch_accounting_purchaseorder) - Update a purchaseorder
* [remove_accounting_purchaseorder](docs/sdks/purchaseorder/README.md#remove_accounting_purchaseorder) - Remove a purchaseorder
* [update_accounting_purchaseorder](docs/sdks/purchaseorder/README.md#update_accounting_purchaseorder) - Update a purchaseorder

### [recording](docs/sdks/recording/README.md)

* [create_uc_recording](docs/sdks/recording/README.md#create_uc_recording) - Create a recording
* [get_calendar_recording](docs/sdks/recording/README.md#get_calendar_recording) - Retrieve a recording
* [get_uc_recording](docs/sdks/recording/README.md#get_uc_recording) - Retrieve a recording
* [list_calendar_recordings](docs/sdks/recording/README.md#list_calendar_recordings) - List all recordings
* [list_uc_recordings](docs/sdks/recording/README.md#list_uc_recordings) - List all recordings
* [patch_uc_recording](docs/sdks/recording/README.md#patch_uc_recording) - Update a recording
* [remove_uc_recording](docs/sdks/recording/README.md#remove_uc_recording) - Remove a recording
* [update_uc_recording](docs/sdks/recording/README.md#update_uc_recording) - Update a recording

### [refund](docs/sdks/refund/README.md)

* [get_payment_refund](docs/sdks/refund/README.md#get_payment_refund) - Retrieve a refund
* [list_payment_refunds](docs/sdks/refund/README.md#list_payment_refunds) - List all refunds

### [repo](docs/sdks/repo/README.md)

* [create_repo_branch](docs/sdks/repo/README.md#create_repo_branch) - Create a branch
* [create_repo_commit](docs/sdks/repo/README.md#create_repo_commit) - Create a commit
* [create_repo_organization](docs/sdks/repo/README.md#create_repo_organization) - Create an organization
* [create_repo_pullrequest](docs/sdks/repo/README.md#create_repo_pullrequest) - Create a pullrequest
* [create_repo_repository](docs/sdks/repo/README.md#create_repo_repository) - Create a repository
* [get_repo_branch](docs/sdks/repo/README.md#get_repo_branch) - Retrieve a branch
* [get_repo_commit](docs/sdks/repo/README.md#get_repo_commit) - Retrieve a commit
* [get_repo_organization](docs/sdks/repo/README.md#get_repo_organization) - Retrieve an organization
* [get_repo_pullrequest](docs/sdks/repo/README.md#get_repo_pullrequest) - Retrieve a pullrequest
* [get_repo_repository](docs/sdks/repo/README.md#get_repo_repository) - Retrieve a repository
* [list_repo_branches](docs/sdks/repo/README.md#list_repo_branches) - List all branches
* [list_repo_commits](docs/sdks/repo/README.md#list_repo_commits) - List all commits
* [list_repo_organizations](docs/sdks/repo/README.md#list_repo_organizations) - List all organizations
* [list_repo_pullrequests](docs/sdks/repo/README.md#list_repo_pullrequests) - List all pullrequests
* [list_repo_repositories](docs/sdks/repo/README.md#list_repo_repositories) - List all repositories
* [patch_repo_branch](docs/sdks/repo/README.md#patch_repo_branch) - Update a branch
* [patch_repo_commit](docs/sdks/repo/README.md#patch_repo_commit) - Update a commit
* [patch_repo_organization](docs/sdks/repo/README.md#patch_repo_organization) - Update an organization
* [patch_repo_pullrequest](docs/sdks/repo/README.md#patch_repo_pullrequest) - Update a pullrequest
* [patch_repo_repository](docs/sdks/repo/README.md#patch_repo_repository) - Update a repository
* [remove_repo_branch](docs/sdks/repo/README.md#remove_repo_branch) - Remove a branch
* [remove_repo_commit](docs/sdks/repo/README.md#remove_repo_commit) - Remove a commit
* [remove_repo_organization](docs/sdks/repo/README.md#remove_repo_organization) - Remove an organization
* [remove_repo_pullrequest](docs/sdks/repo/README.md#remove_repo_pullrequest) - Remove a pullrequest
* [remove_repo_repository](docs/sdks/repo/README.md#remove_repo_repository) - Remove a repository
* [update_repo_branch](docs/sdks/repo/README.md#update_repo_branch) - Update a branch
* [update_repo_commit](docs/sdks/repo/README.md#update_repo_commit) - Update a commit
* [update_repo_organization](docs/sdks/repo/README.md#update_repo_organization) - Update an organization
* [update_repo_pullrequest](docs/sdks/repo/README.md#update_repo_pullrequest) - Update a pullrequest
* [update_repo_repository](docs/sdks/repo/README.md#update_repo_repository) - Update a repository

### [report](docs/sdks/report/README.md)

* [get_accounting_report](docs/sdks/report/README.md#get_accounting_report) - Retrieve a report
* [list_accounting_reports](docs/sdks/report/README.md#list_accounting_reports) - List all reports

### [repository](docs/sdks/repository/README.md)

* [create_repo_repository](docs/sdks/repository/README.md#create_repo_repository) - Create a repository
* [get_repo_repository](docs/sdks/repository/README.md#get_repo_repository) - Retrieve a repository
* [list_repo_repositories](docs/sdks/repository/README.md#list_repo_repositories) - List all repositories
* [patch_repo_repository](docs/sdks/repository/README.md#patch_repo_repository) - Update a repository
* [remove_repo_repository](docs/sdks/repository/README.md#remove_repo_repository) - Remove a repository
* [update_repo_repository](docs/sdks/repository/README.md#update_repo_repository) - Update a repository

### [request](docs/sdks/request/README.md)

* [create_verification_request](docs/sdks/request/README.md#create_verification_request) - Create a request
* [get_verification_request](docs/sdks/request/README.md#get_verification_request) - Retrieve a request
* [list_verification_requests](docs/sdks/request/README.md#list_verification_requests) - List all requests
* [patch_verification_request](docs/sdks/request/README.md#patch_verification_request) - Update a request
* [remove_verification_request](docs/sdks/request/README.md#remove_verification_request) - Remove a request
* [update_verification_request](docs/sdks/request/README.md#update_verification_request) - Update a request

### [review](docs/sdks/review/README.md)

* [create_commerce_review](docs/sdks/review/README.md#create_commerce_review) - Create a review
* [get_commerce_review](docs/sdks/review/README.md#get_commerce_review) - Retrieve a review
* [list_commerce_reviews](docs/sdks/review/README.md#list_commerce_reviews) - List all reviews
* [patch_commerce_review](docs/sdks/review/README.md#patch_commerce_review) - Update a review
* [remove_commerce_review](docs/sdks/review/README.md#remove_commerce_review) - Remove a review
* [update_commerce_review](docs/sdks/review/README.md#update_commerce_review) - Update a review

### [salesorder](docs/sdks/salesorder/README.md)

* [create_accounting_salesorder](docs/sdks/salesorder/README.md#create_accounting_salesorder) - Create a salesorder
* [get_accounting_salesorder](docs/sdks/salesorder/README.md#get_accounting_salesorder) - Retrieve a salesorder
* [list_accounting_salesorders](docs/sdks/salesorder/README.md#list_accounting_salesorders) - List all salesorders
* [patch_accounting_salesorder](docs/sdks/salesorder/README.md#patch_accounting_salesorder) - Update a salesorder
* [remove_accounting_salesorder](docs/sdks/salesorder/README.md#remove_accounting_salesorder) - Remove a salesorder
* [update_accounting_salesorder](docs/sdks/salesorder/README.md#update_accounting_salesorder) - Update a salesorder

### [scim](docs/sdks/scim/README.md)

* [create_scim_groups](docs/sdks/scim/README.md#create_scim_groups) - Create group
* [create_scim_users](docs/sdks/scim/README.md#create_scim_users) - Create user
* [get_scim_groups](docs/sdks/scim/README.md#get_scim_groups) - Get group
* [get_scim_users](docs/sdks/scim/README.md#get_scim_users) - Get user
* [list_scim_groups](docs/sdks/scim/README.md#list_scim_groups) - List groups
* [list_scim_users](docs/sdks/scim/README.md#list_scim_users) - List users
* [patch_scim_groups](docs/sdks/scim/README.md#patch_scim_groups) - Update group
* [patch_scim_users](docs/sdks/scim/README.md#patch_scim_users) - Update user
* [remove_scim_groups](docs/sdks/scim/README.md#remove_scim_groups) - Delete group
* [remove_scim_users](docs/sdks/scim/README.md#remove_scim_users) - Delete user
* [update_scim_groups](docs/sdks/scim/README.md#update_scim_groups) - Update group
* [update_scim_users](docs/sdks/scim/README.md#update_scim_users) - Update user

### [scorecard](docs/sdks/scorecard/README.md)

* [create_ats_scorecard](docs/sdks/scorecard/README.md#create_ats_scorecard) - Create a scorecard
* [get_ats_scorecard](docs/sdks/scorecard/README.md#get_ats_scorecard) - Retrieve a scorecard
* [list_ats_scorecards](docs/sdks/scorecard/README.md#list_ats_scorecards) - List all scorecards
* [patch_ats_scorecard](docs/sdks/scorecard/README.md#patch_ats_scorecard) - Update a scorecard
* [remove_ats_scorecard](docs/sdks/scorecard/README.md#remove_ats_scorecard) - Remove a scorecard
* [update_ats_scorecard](docs/sdks/scorecard/README.md#update_ats_scorecard) - Update a scorecard

### [space](docs/sdks/space/README.md)

* [create_kms_space](docs/sdks/space/README.md#create_kms_space) - Create a space
* [get_kms_space](docs/sdks/space/README.md#get_kms_space) - Retrieve a space
* [list_kms_spaces](docs/sdks/space/README.md#list_kms_spaces) - List all spaces
* [patch_kms_space](docs/sdks/space/README.md#patch_kms_space) - Update a space
* [remove_kms_space](docs/sdks/space/README.md#remove_kms_space) - Remove a space
* [update_kms_space](docs/sdks/space/README.md#update_kms_space) - Update a space

### [storage](docs/sdks/storage/README.md)

* [create_storage_file](docs/sdks/storage/README.md#create_storage_file) - Create a file
* [get_storage_file](docs/sdks/storage/README.md#get_storage_file) - Retrieve a file
* [list_storage_files](docs/sdks/storage/README.md#list_storage_files) - List all files
* [patch_storage_file](docs/sdks/storage/README.md#patch_storage_file) - Update a file
* [remove_storage_file](docs/sdks/storage/README.md#remove_storage_file) - Remove a file
* [update_storage_file](docs/sdks/storage/README.md#update_storage_file) - Update a file

### [student](docs/sdks/student/README.md)

* [create_lms_student](docs/sdks/student/README.md#create_lms_student) - Create a student
* [get_lms_student](docs/sdks/student/README.md#get_lms_student) - Retrieve a student
* [list_lms_students](docs/sdks/student/README.md#list_lms_students) - List all students
* [patch_lms_student](docs/sdks/student/README.md#patch_lms_student) - Update a student
* [remove_lms_student](docs/sdks/student/README.md#remove_lms_student) - Remove a student
* [update_lms_student](docs/sdks/student/README.md#update_lms_student) - Update a student

### [subscription](docs/sdks/subscription/README.md)

* [create_payment_subscription](docs/sdks/subscription/README.md#create_payment_subscription) - Create a subscription
* [get_payment_subscription](docs/sdks/subscription/README.md#get_payment_subscription) - Retrieve a subscription
* [list_payment_subscriptions](docs/sdks/subscription/README.md#list_payment_subscriptions) - List all subscriptions
* [patch_payment_subscription](docs/sdks/subscription/README.md#patch_payment_subscription) - Update a subscription
* [remove_payment_subscription](docs/sdks/subscription/README.md#remove_payment_subscription) - Remove a subscription
* [update_payment_subscription](docs/sdks/subscription/README.md#update_payment_subscription) - Update a subscription

### [task](docs/sdks/task/README.md)

* [create_task_comment](docs/sdks/task/README.md#create_task_comment) - Create a comment
* [create_task_project](docs/sdks/task/README.md#create_task_project) - Create a project
* [create_task_task](docs/sdks/task/README.md#create_task_task) - Create a task
* [get_task_change](docs/sdks/task/README.md#get_task_change) - Retrieve a change
* [get_task_comment](docs/sdks/task/README.md#get_task_comment) - Retrieve a comment
* [get_task_project](docs/sdks/task/README.md#get_task_project) - Retrieve a project
* [get_task_task](docs/sdks/task/README.md#get_task_task) - Retrieve a task
* [list_task_changes](docs/sdks/task/README.md#list_task_changes) - List all changes
* [list_task_comments](docs/sdks/task/README.md#list_task_comments) - List all comments
* [list_task_projects](docs/sdks/task/README.md#list_task_projects) - List all projects
* [list_task_tasks](docs/sdks/task/README.md#list_task_tasks) - List all tasks
* [patch_task_comment](docs/sdks/task/README.md#patch_task_comment) - Update a comment
* [patch_task_project](docs/sdks/task/README.md#patch_task_project) - Update a project
* [patch_task_task](docs/sdks/task/README.md#patch_task_task) - Update a task
* [remove_task_comment](docs/sdks/task/README.md#remove_task_comment) - Remove a comment
* [remove_task_project](docs/sdks/task/README.md#remove_task_project) - Remove a project
* [remove_task_task](docs/sdks/task/README.md#remove_task_task) - Remove a task
* [update_task_comment](docs/sdks/task/README.md#update_task_comment) - Update a comment
* [update_task_project](docs/sdks/task/README.md#update_task_project) - Update a project
* [update_task_task](docs/sdks/task/README.md#update_task_task) - Update a task

### [taxrate](docs/sdks/taxrate/README.md)

* [create_accounting_taxrate](docs/sdks/taxrate/README.md#create_accounting_taxrate) - Create a taxrate
* [get_accounting_taxrate](docs/sdks/taxrate/README.md#get_accounting_taxrate) - Retrieve a taxrate
* [list_accounting_taxrates](docs/sdks/taxrate/README.md#list_accounting_taxrates) - List all taxrates
* [patch_accounting_taxrate](docs/sdks/taxrate/README.md#patch_accounting_taxrate) - Update a taxrate
* [remove_accounting_taxrate](docs/sdks/taxrate/README.md#remove_accounting_taxrate) - Remove a taxrate
* [update_accounting_taxrate](docs/sdks/taxrate/README.md#update_accounting_taxrate) - Update a taxrate

### [ticket](docs/sdks/ticket/README.md)

* [create_ticketing_ticket](docs/sdks/ticket/README.md#create_ticketing_ticket) - Create a ticket
* [get_ticketing_ticket](docs/sdks/ticket/README.md#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_tickets](docs/sdks/ticket/README.md#list_ticketing_tickets) - List all tickets
* [patch_ticketing_ticket](docs/sdks/ticket/README.md#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_ticket](docs/sdks/ticket/README.md#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_ticket](docs/sdks/ticket/README.md#update_ticketing_ticket) - Update a ticket

### [ticketing](docs/sdks/ticketing/README.md)

* [create_ticketing_category](docs/sdks/ticketing/README.md#create_ticketing_category) - Create a category
* [create_ticketing_customer](docs/sdks/ticketing/README.md#create_ticketing_customer) - Create a customer
* [create_ticketing_note](docs/sdks/ticketing/README.md#create_ticketing_note) - Create a note
* [create_ticketing_ticket](docs/sdks/ticketing/README.md#create_ticketing_ticket) - Create a ticket
* [get_ticketing_category](docs/sdks/ticketing/README.md#get_ticketing_category) - Retrieve a category
* [get_ticketing_customer](docs/sdks/ticketing/README.md#get_ticketing_customer) - Retrieve a customer
* [get_ticketing_note](docs/sdks/ticketing/README.md#get_ticketing_note) - Retrieve a note
* [get_ticketing_ticket](docs/sdks/ticketing/README.md#get_ticketing_ticket) - Retrieve a ticket
* [list_ticketing_categories](docs/sdks/ticketing/README.md#list_ticketing_categories) - List all categories
* [list_ticketing_customers](docs/sdks/ticketing/README.md#list_ticketing_customers) - List all customers
* [list_ticketing_notes](docs/sdks/ticketing/README.md#list_ticketing_notes) - List all notes
* [list_ticketing_tickets](docs/sdks/ticketing/README.md#list_ticketing_tickets) - List all tickets
* [patch_ticketing_category](docs/sdks/ticketing/README.md#patch_ticketing_category) - Update a category
* [patch_ticketing_customer](docs/sdks/ticketing/README.md#patch_ticketing_customer) - Update a customer
* [patch_ticketing_note](docs/sdks/ticketing/README.md#patch_ticketing_note) - Update a note
* [patch_ticketing_ticket](docs/sdks/ticketing/README.md#patch_ticketing_ticket) - Update a ticket
* [remove_ticketing_category](docs/sdks/ticketing/README.md#remove_ticketing_category) - Remove a category
* [remove_ticketing_customer](docs/sdks/ticketing/README.md#remove_ticketing_customer) - Remove a customer
* [remove_ticketing_note](docs/sdks/ticketing/README.md#remove_ticketing_note) - Remove a note
* [remove_ticketing_ticket](docs/sdks/ticketing/README.md#remove_ticketing_ticket) - Remove a ticket
* [update_ticketing_category](docs/sdks/ticketing/README.md#update_ticketing_category) - Update a category
* [update_ticketing_customer](docs/sdks/ticketing/README.md#update_ticketing_customer) - Update a customer
* [update_ticketing_note](docs/sdks/ticketing/README.md#update_ticketing_note) - Update a note
* [update_ticketing_ticket](docs/sdks/ticketing/README.md#update_ticketing_ticket) - Update a ticket

### [timeoff](docs/sdks/timeoff/README.md)

* [get_hris_timeoff](docs/sdks/timeoff/README.md#get_hris_timeoff) - Retrieve a timeoff
* [list_hris_timeoffs](docs/sdks/timeoff/README.md#list_hris_timeoffs) - List all timeoffs

### [timeshift](docs/sdks/timeshift/README.md)

* [create_hris_timeshift](docs/sdks/timeshift/README.md#create_hris_timeshift) - Create a timeshift
* [get_hris_timeshift](docs/sdks/timeshift/README.md#get_hris_timeshift) - Retrieve a timeshift
* [list_hris_timeshifts](docs/sdks/timeshift/README.md#list_hris_timeshifts) - List all timeshifts
* [patch_hris_timeshift](docs/sdks/timeshift/README.md#patch_hris_timeshift) - Update a timeshift
* [remove_hris_timeshift](docs/sdks/timeshift/README.md#remove_hris_timeshift) - Remove a timeshift
* [update_hris_timeshift](docs/sdks/timeshift/README.md#update_hris_timeshift) - Update a timeshift

### [transaction](docs/sdks/transaction/README.md)

* [create_accounting_transaction](docs/sdks/transaction/README.md#create_accounting_transaction) - Create a transaction
* [get_accounting_transaction](docs/sdks/transaction/README.md#get_accounting_transaction) - Retrieve a transaction
* [list_accounting_transactions](docs/sdks/transaction/README.md#list_accounting_transactions) - List all transactions
* [patch_accounting_transaction](docs/sdks/transaction/README.md#patch_accounting_transaction) - Update a transaction
* [remove_accounting_transaction](docs/sdks/transaction/README.md#remove_accounting_transaction) - Remove a transaction
* [update_accounting_transaction](docs/sdks/transaction/README.md#update_accounting_transaction) - Update a transaction

### [trialbalance](docs/sdks/trialbalance/README.md)

* [get_accounting_trialbalance](docs/sdks/trialbalance/README.md#get_accounting_trialbalance) - Retrieve a trialbalance
* [list_accounting_trialbalances](docs/sdks/trialbalance/README.md#list_accounting_trialbalances) - List all trialbalances

### [uc](docs/sdks/uc/README.md)

* [create_uc_comment](docs/sdks/uc/README.md#create_uc_comment) - Create a comment
* [create_uc_contact](docs/sdks/uc/README.md#create_uc_contact) - Create a contact
* [create_uc_recording](docs/sdks/uc/README.md#create_uc_recording) - Create a recording
* [get_uc_comment](docs/sdks/uc/README.md#get_uc_comment) - Retrieve a comment
* [get_uc_contact](docs/sdks/uc/README.md#get_uc_contact) - Retrieve a contact
* [get_uc_recording](docs/sdks/uc/README.md#get_uc_recording) - Retrieve a recording
* [list_uc_calls](docs/sdks/uc/README.md#list_uc_calls) - List all calls
* [list_uc_comments](docs/sdks/uc/README.md#list_uc_comments) - List all comments
* [list_uc_contacts](docs/sdks/uc/README.md#list_uc_contacts) - List all contacts
* [list_uc_recordings](docs/sdks/uc/README.md#list_uc_recordings) - List all recordings
* [patch_uc_comment](docs/sdks/uc/README.md#patch_uc_comment) - Update a comment
* [patch_uc_contact](docs/sdks/uc/README.md#patch_uc_contact) - Update a contact
* [patch_uc_recording](docs/sdks/uc/README.md#patch_uc_recording) - Update a recording
* [remove_uc_comment](docs/sdks/uc/README.md#remove_uc_comment) - Remove a comment
* [remove_uc_contact](docs/sdks/uc/README.md#remove_uc_contact) - Remove a contact
* [remove_uc_recording](docs/sdks/uc/README.md#remove_uc_recording) - Remove a recording
* [update_uc_comment](docs/sdks/uc/README.md#update_uc_comment) - Update a comment
* [update_uc_contact](docs/sdks/uc/README.md#update_uc_contact) - Update a contact
* [update_uc_recording](docs/sdks/uc/README.md#update_uc_recording) - Update a recording

### [unified](docs/sdks/unified/README.md)

* [create_unified_connection](docs/sdks/unified/README.md#create_unified_connection) - Create connection
* [create_unified_webhook](docs/sdks/unified/README.md#create_unified_webhook) - Create webhook subscription
* [get_unified_apicall](docs/sdks/unified/README.md#get_unified_apicall) - Retrieve specific API Call by its ID
* [get_unified_connection](docs/sdks/unified/README.md#get_unified_connection) - Retrieve connection
* [get_unified_integration_auth](docs/sdks/unified/README.md#get_unified_integration_auth) - Authorize new connection
* [get_unified_issue](docs/sdks/unified/README.md#get_unified_issue) - Retrieve support issue
* [get_unified_webhook](docs/sdks/unified/README.md#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_apicalls](docs/sdks/unified/README.md#list_unified_apicalls) - Returns API Calls
* [list_unified_connections](docs/sdks/unified/README.md#list_unified_connections) - List all connections
* [list_unified_integration_workspaces](docs/sdks/unified/README.md#list_unified_integration_workspaces) - Returns all activated integrations in a workspace
* [list_unified_integrations](docs/sdks/unified/README.md#list_unified_integrations) - Returns all integrations
* [list_unified_issues](docs/sdks/unified/README.md#list_unified_issues) - List support issues
* [list_unified_webhooks](docs/sdks/unified/README.md#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_connection](docs/sdks/unified/README.md#patch_unified_connection) - Update connection
* [patch_unified_webhook](docs/sdks/unified/README.md#patch_unified_webhook) - Update webhook subscription
* [patch_unified_webhook_trigger](docs/sdks/unified/README.md#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_connection](docs/sdks/unified/README.md#remove_unified_connection) - Remove connection
* [remove_unified_webhook](docs/sdks/unified/README.md#remove_unified_webhook) - Remove webhook subscription
* [update_unified_connection](docs/sdks/unified/README.md#update_unified_connection) - Update connection
* [update_unified_webhook](docs/sdks/unified/README.md#update_unified_webhook) - Update webhook subscription
* [update_unified_webhook_trigger](docs/sdks/unified/README.md#update_unified_webhook_trigger) - Trigger webhook

### [user](docs/sdks/user/README.md)

* [create_scim_users](docs/sdks/user/README.md#create_scim_users) - Create user
* [get_scim_users](docs/sdks/user/README.md#get_scim_users) - Get user
* [list_scim_users](docs/sdks/user/README.md#list_scim_users) - List users
* [patch_scim_users](docs/sdks/user/README.md#patch_scim_users) - Update user
* [remove_scim_users](docs/sdks/user/README.md#remove_scim_users) - Delete user
* [update_scim_users](docs/sdks/user/README.md#update_scim_users) - Update user

### [verification](docs/sdks/verification/README.md)

* [create_verification_request](docs/sdks/verification/README.md#create_verification_request) - Create a request
* [get_verification_package](docs/sdks/verification/README.md#get_verification_package) - Retrieve a package
* [get_verification_request](docs/sdks/verification/README.md#get_verification_request) - Retrieve a request
* [list_verification_packages](docs/sdks/verification/README.md#list_verification_packages) - List all packages
* [list_verification_requests](docs/sdks/verification/README.md#list_verification_requests) - List all requests
* [patch_verification_request](docs/sdks/verification/README.md#patch_verification_request) - Update a request
* [remove_verification_request](docs/sdks/verification/README.md#remove_verification_request) - Remove a request
* [update_verification_request](docs/sdks/verification/README.md#update_verification_request) - Update a request

### [webhook](docs/sdks/webhook/README.md)

* [create_unified_webhook](docs/sdks/webhook/README.md#create_unified_webhook) - Create webhook subscription
* [get_unified_webhook](docs/sdks/webhook/README.md#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_webhooks](docs/sdks/webhook/README.md#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_webhook](docs/sdks/webhook/README.md#patch_unified_webhook) - Update webhook subscription
* [patch_unified_webhook_trigger](docs/sdks/webhook/README.md#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_webhook](docs/sdks/webhook/README.md#remove_unified_webhook) - Remove webhook subscription
* [update_unified_webhook](docs/sdks/webhook/README.md#update_unified_webhook) - Update webhook subscription
* [update_unified_webhook_trigger](docs/sdks/webhook/README.md#update_unified_webhook_trigger) - Trigger webhook

</details>
<!-- End Available Resources and Operations [operations] -->







<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.create_passthrough_raw(request={
        "connection_id": "<id>",
        "path": "/var/log",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import BackoffStrategy, RetryConfig


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import BackoffStrategy, RetryConfig


with UnifiedTo(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`UnifiedToError`](./src/unified_python_sdk/models/errors/unifiedtoerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import errors, shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:
    res = None
    try:

        res = unified_to.accounting.create_accounting_account(request={
            "accounting_account": {},
            "connection_id": "<id>",
        })

        assert res.accounting_account is not None

        # Handle response
        print(res.accounting_account)


    except errors.UnifiedToError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`UnifiedToError`](./src/unified_python_sdk/models/errors/unifiedtoerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`UnifiedToError`](./src/unified_python_sdk/models/errors/unifiedtoerror.py)**:
* [`ResponseValidationError`](./src/unified_python_sdk/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                      | Description                |
| --- | --------------------------- | -------------------------- |
| 0   | `https://api.unified.to`    | North American data region |
| 1   | `https://api-eu.unified.to` | European data region       |
| 2   | `https://api-au.unified.to` | Australian data region     |

#### Example

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    server_idx=2,
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    server_url="https://api-au.unified.to",
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from unified_python_sdk import UnifiedTo
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = UnifiedTo(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = UnifiedTo(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name  | Type   | Scheme  |
| ----- | ------ | ------- |
| `jwt` | apiKey | API key |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account(request={
        "accounting_account": {},
        "connection_id": "<id>",
    })

    assert res.accounting_account is not None

    # Handle response
    print(res.accounting_account)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `UnifiedTo` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
def main():

    with UnifiedTo(
        security=shared.Security(
            jwt="<YOUR_API_KEY_HERE>",
        ),
    ) as unified_to:
        # Rest of application here...


# Or when using async:
async def amain():

    async with UnifiedTo(
        security=shared.Security(
            jwt="<YOUR_API_KEY_HERE>",
        ),
    ) as unified_to:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from unified_python_sdk import UnifiedTo
import logging

logging.basicConfig(level=logging.DEBUG)
s = UnifiedTo(debug_logger=logging.getLogger("unified_python_sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
