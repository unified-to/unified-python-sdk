<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/unified-to/unified-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/unified-to/unified-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start Summary [summary] -->
## Summary

Unified.to  API: One API to Rule Them All

For more information about the API: [API Documentation](https://docs.unified.to)
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
# requires-python = ">=3.10"
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

    res = unified_to.accounting.create_accounting_account2(request={
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

        res = await unified_to.accounting.create_accounting_account2_async(request={
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

### [Account](docs/sdks/account/README.md)

* [create_accounting_account2](docs/sdks/account/README.md#create_accounting_account2) - Create an account
* [get_accounting_account2](docs/sdks/account/README.md#get_accounting_account2) - Retrieve an account
* [list_accounting_accounts2](docs/sdks/account/README.md#list_accounting_accounts2) - List all accounts
* [patch_accounting_account2](docs/sdks/account/README.md#patch_accounting_account2) - Update an account
* [remove_accounting_account2](docs/sdks/account/README.md#remove_accounting_account2) - Remove an account
* [update_accounting_account2](docs/sdks/account/README.md#update_accounting_account2) - Update an account

### [Accounting](docs/sdks/accounting/README.md)

* [create_accounting_account2](docs/sdks/accounting/README.md#create_accounting_account2) - Create an account
* [create_accounting_bill2](docs/sdks/accounting/README.md#create_accounting_bill2) - Create a bill
* [create_accounting_category2](docs/sdks/accounting/README.md#create_accounting_category2) - Create a category
* [create_accounting_contact2](docs/sdks/accounting/README.md#create_accounting_contact2) - Create a contact
* [create_accounting_creditmemo2](docs/sdks/accounting/README.md#create_accounting_creditmemo2) - Create a creditmemo
* [create_accounting_expense2](docs/sdks/accounting/README.md#create_accounting_expense2) - Create an expense
* [create_accounting_invoice2](docs/sdks/accounting/README.md#create_accounting_invoice2) - Create an invoice
* [create_accounting_journal2](docs/sdks/accounting/README.md#create_accounting_journal2) - Create a journal
* [create_accounting_order2](docs/sdks/accounting/README.md#create_accounting_order2) - Create an order
* [create_accounting_purchaseorder2](docs/sdks/accounting/README.md#create_accounting_purchaseorder2) - Create a purchaseorder
* [create_accounting_salesorder2](docs/sdks/accounting/README.md#create_accounting_salesorder2) - Create a salesorder
* [create_accounting_taxrate2](docs/sdks/accounting/README.md#create_accounting_taxrate2) - Create a taxrate
* [create_accounting_transaction2](docs/sdks/accounting/README.md#create_accounting_transaction2) - Create a transaction
* [get_accounting_account2](docs/sdks/accounting/README.md#get_accounting_account2) - Retrieve an account
* [get_accounting_balancesheet2](docs/sdks/accounting/README.md#get_accounting_balancesheet2) - Retrieve a balancesheet
* [get_accounting_bill2](docs/sdks/accounting/README.md#get_accounting_bill2) - Retrieve a bill
* [get_accounting_cashflow2](docs/sdks/accounting/README.md#get_accounting_cashflow2) - Retrieve a cashflow
* [get_accounting_category2](docs/sdks/accounting/README.md#get_accounting_category2) - Retrieve a category
* [get_accounting_contact2](docs/sdks/accounting/README.md#get_accounting_contact2) - Retrieve a contact
* [get_accounting_creditmemo2](docs/sdks/accounting/README.md#get_accounting_creditmemo2) - Retrieve a creditmemo
* [get_accounting_expense2](docs/sdks/accounting/README.md#get_accounting_expense2) - Retrieve an expense
* [get_accounting_invoice2](docs/sdks/accounting/README.md#get_accounting_invoice2) - Retrieve an invoice
* [get_accounting_journal2](docs/sdks/accounting/README.md#get_accounting_journal2) - Retrieve a journal
* [get_accounting_order2](docs/sdks/accounting/README.md#get_accounting_order2) - Retrieve an order
* [get_accounting_organization2](docs/sdks/accounting/README.md#get_accounting_organization2) - Retrieve an organization
* [get_accounting_profitloss2](docs/sdks/accounting/README.md#get_accounting_profitloss2) - Retrieve a profitloss
* [get_accounting_purchaseorder2](docs/sdks/accounting/README.md#get_accounting_purchaseorder2) - Retrieve a purchaseorder
* [get_accounting_report2](docs/sdks/accounting/README.md#get_accounting_report2) - Retrieve a report
* [get_accounting_salesorder2](docs/sdks/accounting/README.md#get_accounting_salesorder2) - Retrieve a salesorder
* [get_accounting_taxrate2](docs/sdks/accounting/README.md#get_accounting_taxrate2) - Retrieve a taxrate
* [get_accounting_transaction2](docs/sdks/accounting/README.md#get_accounting_transaction2) - Retrieve a transaction
* [get_accounting_trialbalance2](docs/sdks/accounting/README.md#get_accounting_trialbalance2) - Retrieve a trialbalance
* [list_accounting_accounts2](docs/sdks/accounting/README.md#list_accounting_accounts2) - List all accounts
* [list_accounting_balancesheets2](docs/sdks/accounting/README.md#list_accounting_balancesheets2) - List all balancesheets
* [list_accounting_bills2](docs/sdks/accounting/README.md#list_accounting_bills2) - List all bills
* [list_accounting_cashflows2](docs/sdks/accounting/README.md#list_accounting_cashflows2) - List all cashflows
* [list_accounting_categories2](docs/sdks/accounting/README.md#list_accounting_categories2) - List all categories
* [list_accounting_contacts2](docs/sdks/accounting/README.md#list_accounting_contacts2) - List all contacts
* [list_accounting_creditmemoes2](docs/sdks/accounting/README.md#list_accounting_creditmemoes2) - List all creditmemoes
* [list_accounting_expenses2](docs/sdks/accounting/README.md#list_accounting_expenses2) - List all expenses
* [list_accounting_invoices2](docs/sdks/accounting/README.md#list_accounting_invoices2) - List all invoices
* [list_accounting_journals2](docs/sdks/accounting/README.md#list_accounting_journals2) - List all journals
* [list_accounting_orders2](docs/sdks/accounting/README.md#list_accounting_orders2) - List all orders
* [list_accounting_organizations2](docs/sdks/accounting/README.md#list_accounting_organizations2) - List all organizations
* [list_accounting_profitlosses2](docs/sdks/accounting/README.md#list_accounting_profitlosses2) - List all profitlosses
* [list_accounting_purchaseorders2](docs/sdks/accounting/README.md#list_accounting_purchaseorders2) - List all purchaseorders
* [list_accounting_reports2](docs/sdks/accounting/README.md#list_accounting_reports2) - List all reports
* [list_accounting_salesorders2](docs/sdks/accounting/README.md#list_accounting_salesorders2) - List all salesorders
* [list_accounting_taxrates2](docs/sdks/accounting/README.md#list_accounting_taxrates2) - List all taxrates
* [list_accounting_transactions2](docs/sdks/accounting/README.md#list_accounting_transactions2) - List all transactions
* [list_accounting_trialbalances2](docs/sdks/accounting/README.md#list_accounting_trialbalances2) - List all trialbalances
* [patch_accounting_account2](docs/sdks/accounting/README.md#patch_accounting_account2) - Update an account
* [patch_accounting_bill2](docs/sdks/accounting/README.md#patch_accounting_bill2) - Update a bill
* [patch_accounting_category2](docs/sdks/accounting/README.md#patch_accounting_category2) - Update a category
* [patch_accounting_contact2](docs/sdks/accounting/README.md#patch_accounting_contact2) - Update a contact
* [patch_accounting_creditmemo2](docs/sdks/accounting/README.md#patch_accounting_creditmemo2) - Update a creditmemo
* [patch_accounting_expense2](docs/sdks/accounting/README.md#patch_accounting_expense2) - Update an expense
* [patch_accounting_invoice2](docs/sdks/accounting/README.md#patch_accounting_invoice2) - Update an invoice
* [patch_accounting_journal2](docs/sdks/accounting/README.md#patch_accounting_journal2) - Update a journal
* [patch_accounting_order2](docs/sdks/accounting/README.md#patch_accounting_order2) - Update an order
* [patch_accounting_purchaseorder2](docs/sdks/accounting/README.md#patch_accounting_purchaseorder2) - Update a purchaseorder
* [patch_accounting_salesorder2](docs/sdks/accounting/README.md#patch_accounting_salesorder2) - Update a salesorder
* [patch_accounting_taxrate2](docs/sdks/accounting/README.md#patch_accounting_taxrate2) - Update a taxrate
* [patch_accounting_transaction2](docs/sdks/accounting/README.md#patch_accounting_transaction2) - Update a transaction
* [remove_accounting_account2](docs/sdks/accounting/README.md#remove_accounting_account2) - Remove an account
* [remove_accounting_bill2](docs/sdks/accounting/README.md#remove_accounting_bill2) - Remove a bill
* [remove_accounting_category2](docs/sdks/accounting/README.md#remove_accounting_category2) - Remove a category
* [remove_accounting_contact2](docs/sdks/accounting/README.md#remove_accounting_contact2) - Remove a contact
* [remove_accounting_creditmemo2](docs/sdks/accounting/README.md#remove_accounting_creditmemo2) - Remove a creditmemo
* [remove_accounting_expense2](docs/sdks/accounting/README.md#remove_accounting_expense2) - Remove an expense
* [remove_accounting_invoice2](docs/sdks/accounting/README.md#remove_accounting_invoice2) - Remove an invoice
* [remove_accounting_journal2](docs/sdks/accounting/README.md#remove_accounting_journal2) - Remove a journal
* [remove_accounting_order2](docs/sdks/accounting/README.md#remove_accounting_order2) - Remove an order
* [remove_accounting_purchaseorder2](docs/sdks/accounting/README.md#remove_accounting_purchaseorder2) - Remove a purchaseorder
* [remove_accounting_salesorder2](docs/sdks/accounting/README.md#remove_accounting_salesorder2) - Remove a salesorder
* [remove_accounting_taxrate2](docs/sdks/accounting/README.md#remove_accounting_taxrate2) - Remove a taxrate
* [remove_accounting_transaction2](docs/sdks/accounting/README.md#remove_accounting_transaction2) - Remove a transaction
* [update_accounting_account2](docs/sdks/accounting/README.md#update_accounting_account2) - Update an account
* [update_accounting_bill2](docs/sdks/accounting/README.md#update_accounting_bill2) - Update a bill
* [update_accounting_category2](docs/sdks/accounting/README.md#update_accounting_category2) - Update a category
* [update_accounting_contact2](docs/sdks/accounting/README.md#update_accounting_contact2) - Update a contact
* [update_accounting_creditmemo2](docs/sdks/accounting/README.md#update_accounting_creditmemo2) - Update a creditmemo
* [update_accounting_expense2](docs/sdks/accounting/README.md#update_accounting_expense2) - Update an expense
* [update_accounting_invoice2](docs/sdks/accounting/README.md#update_accounting_invoice2) - Update an invoice
* [update_accounting_journal2](docs/sdks/accounting/README.md#update_accounting_journal2) - Update a journal
* [update_accounting_order2](docs/sdks/accounting/README.md#update_accounting_order2) - Update an order
* [update_accounting_purchaseorder2](docs/sdks/accounting/README.md#update_accounting_purchaseorder2) - Update a purchaseorder
* [update_accounting_salesorder2](docs/sdks/accounting/README.md#update_accounting_salesorder2) - Update a salesorder
* [update_accounting_taxrate2](docs/sdks/accounting/README.md#update_accounting_taxrate2) - Update a taxrate
* [update_accounting_transaction2](docs/sdks/accounting/README.md#update_accounting_transaction2) - Update a transaction

### [Activity](docs/sdks/activity/README.md)

* [create_ats_activity2](docs/sdks/activity/README.md#create_ats_activity2) - Create an activity
* [create_lms_activity2](docs/sdks/activity/README.md#create_lms_activity2) - Create an activity
* [get_ats_activity2](docs/sdks/activity/README.md#get_ats_activity2) - Retrieve an activity
* [get_clubs_activity2](docs/sdks/activity/README.md#get_clubs_activity2) - Retrieve an activity
* [get_lms_activity2](docs/sdks/activity/README.md#get_lms_activity2) - Retrieve an activity
* [list_ats_activities2](docs/sdks/activity/README.md#list_ats_activities2) - List all activities
* [list_clubs_activities2](docs/sdks/activity/README.md#list_clubs_activities2) - List all activities
* [list_lms_activities2](docs/sdks/activity/README.md#list_lms_activities2) - List all activities
* [patch_ats_activity2](docs/sdks/activity/README.md#patch_ats_activity2) - Update an activity
* [patch_lms_activity2](docs/sdks/activity/README.md#patch_lms_activity2) - Update an activity
* [remove_ats_activity2](docs/sdks/activity/README.md#remove_ats_activity2) - Remove an activity
* [remove_lms_activity2](docs/sdks/activity/README.md#remove_lms_activity2) - Remove an activity
* [update_ats_activity2](docs/sdks/activity/README.md#update_ats_activity2) - Update an activity
* [update_lms_activity2](docs/sdks/activity/README.md#update_lms_activity2) - Update an activity

### [Ad](docs/sdks/ad/README.md)

* [create_ads_ad2](docs/sdks/ad/README.md#create_ads_ad2) - Create an ad
* [get_ads_ad2](docs/sdks/ad/README.md#get_ads_ad2) - Retrieve an ad
* [list_ads_ads2](docs/sdks/ad/README.md#list_ads_ads2) - List all ads
* [patch_ads_ad2](docs/sdks/ad/README.md#patch_ads_ad2) - Update an ad
* [remove_ads_ad2](docs/sdks/ad/README.md#remove_ads_ad2) - Remove an ad
* [update_ads_ad2](docs/sdks/ad/README.md#update_ads_ad2) - Update an ad

### [Ads](docs/sdks/ads/README.md)

* [create_ads_ad2](docs/sdks/ads/README.md#create_ads_ad2) - Create an ad
* [create_ads_campaign2](docs/sdks/ads/README.md#create_ads_campaign2) - Create a campaign
* [create_ads_creative2](docs/sdks/ads/README.md#create_ads_creative2) - Create a creative
* [create_ads_group2](docs/sdks/ads/README.md#create_ads_group2) - Create a group
* [create_ads_insertionorder2](docs/sdks/ads/README.md#create_ads_insertionorder2) - Create an insertionorder
* [create_ads_organization2](docs/sdks/ads/README.md#create_ads_organization2) - Create an organization
* [get_ads_ad2](docs/sdks/ads/README.md#get_ads_ad2) - Retrieve an ad
* [get_ads_campaign2](docs/sdks/ads/README.md#get_ads_campaign2) - Retrieve a campaign
* [get_ads_creative2](docs/sdks/ads/README.md#get_ads_creative2) - Retrieve a creative
* [get_ads_group2](docs/sdks/ads/README.md#get_ads_group2) - Retrieve a group
* [get_ads_insertionorder2](docs/sdks/ads/README.md#get_ads_insertionorder2) - Retrieve an insertionorder
* [get_ads_organization2](docs/sdks/ads/README.md#get_ads_organization2) - Retrieve an organization
* [get_ads_promoted2](docs/sdks/ads/README.md#get_ads_promoted2) - Retrieve a promoted
* [get_ads_target2](docs/sdks/ads/README.md#get_ads_target2) - Retrieve a target
* [list_ads_ads2](docs/sdks/ads/README.md#list_ads_ads2) - List all ads
* [list_ads_campaigns2](docs/sdks/ads/README.md#list_ads_campaigns2) - List all campaigns
* [list_ads_creatives2](docs/sdks/ads/README.md#list_ads_creatives2) - List all creatives
* [list_ads_groups2](docs/sdks/ads/README.md#list_ads_groups2) - List all groups
* [list_ads_insertionorders2](docs/sdks/ads/README.md#list_ads_insertionorders2) - List all insertionorders
* [list_ads_organizations2](docs/sdks/ads/README.md#list_ads_organizations2) - List all organizations
* [list_ads_promoteds2](docs/sdks/ads/README.md#list_ads_promoteds2) - List all promoteds
* [list_ads_reports2](docs/sdks/ads/README.md#list_ads_reports2) - List all reports
* [list_ads_targets2](docs/sdks/ads/README.md#list_ads_targets2) - List all targets
* [patch_ads_ad2](docs/sdks/ads/README.md#patch_ads_ad2) - Update an ad
* [patch_ads_campaign2](docs/sdks/ads/README.md#patch_ads_campaign2) - Update a campaign
* [patch_ads_creative2](docs/sdks/ads/README.md#patch_ads_creative2) - Update a creative
* [patch_ads_group2](docs/sdks/ads/README.md#patch_ads_group2) - Update a group
* [patch_ads_insertionorder2](docs/sdks/ads/README.md#patch_ads_insertionorder2) - Update an insertionorder
* [patch_ads_organization2](docs/sdks/ads/README.md#patch_ads_organization2) - Update an organization
* [remove_ads_ad2](docs/sdks/ads/README.md#remove_ads_ad2) - Remove an ad
* [remove_ads_campaign2](docs/sdks/ads/README.md#remove_ads_campaign2) - Remove a campaign
* [remove_ads_creative2](docs/sdks/ads/README.md#remove_ads_creative2) - Remove a creative
* [remove_ads_group2](docs/sdks/ads/README.md#remove_ads_group2) - Remove a group
* [remove_ads_insertionorder2](docs/sdks/ads/README.md#remove_ads_insertionorder2) - Remove an insertionorder
* [remove_ads_organization2](docs/sdks/ads/README.md#remove_ads_organization2) - Remove an organization
* [update_ads_ad2](docs/sdks/ads/README.md#update_ads_ad2) - Update an ad
* [update_ads_campaign2](docs/sdks/ads/README.md#update_ads_campaign2) - Update a campaign
* [update_ads_creative2](docs/sdks/ads/README.md#update_ads_creative2) - Update a creative
* [update_ads_group2](docs/sdks/ads/README.md#update_ads_group2) - Update a group
* [update_ads_insertionorder2](docs/sdks/ads/README.md#update_ads_insertionorder2) - Update an insertionorder
* [update_ads_organization2](docs/sdks/ads/README.md#update_ads_organization2) - Update an organization

### [Analytics](docs/sdks/analytics/README.md)

* [create_analytics_event2](docs/sdks/analytics/README.md#create_analytics_event2) - Create an event
* [create_analytics_property2](docs/sdks/analytics/README.md#create_analytics_property2) - Create a property
* [create_analytics_visitor2](docs/sdks/analytics/README.md#create_analytics_visitor2) - Create a visitor
* [get_analytics_event2](docs/sdks/analytics/README.md#get_analytics_event2) - Retrieve an event
* [get_analytics_property2](docs/sdks/analytics/README.md#get_analytics_property2) - Retrieve a property
* [get_analytics_session2](docs/sdks/analytics/README.md#get_analytics_session2) - Retrieve a session
* [get_analytics_visitor2](docs/sdks/analytics/README.md#get_analytics_visitor2) - Retrieve a visitor
* [list_analytics_events2](docs/sdks/analytics/README.md#list_analytics_events2) - List all events
* [list_analytics_properties2](docs/sdks/analytics/README.md#list_analytics_properties2) - List all properties
* [list_analytics_reports2](docs/sdks/analytics/README.md#list_analytics_reports2) - List all reports
* [list_analytics_sessions2](docs/sdks/analytics/README.md#list_analytics_sessions2) - List all sessions
* [list_analytics_visitors2](docs/sdks/analytics/README.md#list_analytics_visitors2) - List all visitors
* [patch_analytics_property2](docs/sdks/analytics/README.md#patch_analytics_property2) - Update a property
* [patch_analytics_visitor2](docs/sdks/analytics/README.md#patch_analytics_visitor2) - Update a visitor
* [remove_analytics_property2](docs/sdks/analytics/README.md#remove_analytics_property2) - Remove a property
* [remove_analytics_visitor2](docs/sdks/analytics/README.md#remove_analytics_visitor2) - Remove a visitor
* [update_analytics_property2](docs/sdks/analytics/README.md#update_analytics_property2) - Update a property
* [update_analytics_visitor2](docs/sdks/analytics/README.md#update_analytics_visitor2) - Update a visitor

### [Apicall](docs/sdks/apicall/README.md)

* [get_unified_apicall](docs/sdks/apicall/README.md#get_unified_apicall) - Retrieve specific API Call by its ID
* [list_unified_apicalls](docs/sdks/apicall/README.md#list_unified_apicalls) - Returns API Calls

### [Application](docs/sdks/application/README.md)

* [create_ats_application2](docs/sdks/application/README.md#create_ats_application2) - Create an application
* [get_ats_application2](docs/sdks/application/README.md#get_ats_application2) - Retrieve an application
* [list_ats_applications2](docs/sdks/application/README.md#list_ats_applications2) - List all applications
* [patch_ats_application2](docs/sdks/application/README.md#patch_ats_application2) - Update an application
* [remove_ats_application2](docs/sdks/application/README.md#remove_ats_application2) - Remove an application
* [update_ats_application2](docs/sdks/application/README.md#update_ats_application2) - Update an application

### [Applicationstatus](docs/sdks/applicationstatus/README.md)

* [list_ats_applicationstatuses2](docs/sdks/applicationstatus/README.md#list_ats_applicationstatuses2) - List all applicationstatuses

### [Assessment](docs/sdks/assessment/README.md)

* [create_assessment_package2](docs/sdks/assessment/README.md#create_assessment_package2) - Create an assessment package
* [get_assessment_package2](docs/sdks/assessment/README.md#get_assessment_package2) - Get an assessment package
* [list_assessment_packages2](docs/sdks/assessment/README.md#list_assessment_packages2) - List assessment packages
* [patch_assessment_order2](docs/sdks/assessment/README.md#patch_assessment_order2) - Update an order
* [patch_assessment_package2](docs/sdks/assessment/README.md#patch_assessment_package2) - Update an assessment package
* [remove_assessment_package2](docs/sdks/assessment/README.md#remove_assessment_package2) - Delete an assessment package
* [update_assessment_order2](docs/sdks/assessment/README.md#update_assessment_order2) - Update an order
* [update_assessment_package2](docs/sdks/assessment/README.md#update_assessment_package2) - Update an assessment package

### [Ats](docs/sdks/ats/README.md)

* [create_ats_activity2](docs/sdks/ats/README.md#create_ats_activity2) - Create an activity
* [create_ats_application2](docs/sdks/ats/README.md#create_ats_application2) - Create an application
* [create_ats_candidate2](docs/sdks/ats/README.md#create_ats_candidate2) - Create a candidate
* [create_ats_company2](docs/sdks/ats/README.md#create_ats_company2) - Create a company
* [create_ats_document2](docs/sdks/ats/README.md#create_ats_document2) - Create a document
* [create_ats_interview2](docs/sdks/ats/README.md#create_ats_interview2) - Create an interview
* [create_ats_job2](docs/sdks/ats/README.md#create_ats_job2) - Create a job
* [create_ats_scorecard2](docs/sdks/ats/README.md#create_ats_scorecard2) - Create a scorecard
* [get_ats_activity2](docs/sdks/ats/README.md#get_ats_activity2) - Retrieve an activity
* [get_ats_application2](docs/sdks/ats/README.md#get_ats_application2) - Retrieve an application
* [get_ats_candidate2](docs/sdks/ats/README.md#get_ats_candidate2) - Retrieve a candidate
* [get_ats_company2](docs/sdks/ats/README.md#get_ats_company2) - Retrieve a company
* [get_ats_document2](docs/sdks/ats/README.md#get_ats_document2) - Retrieve a document
* [get_ats_interview2](docs/sdks/ats/README.md#get_ats_interview2) - Retrieve an interview
* [get_ats_job2](docs/sdks/ats/README.md#get_ats_job2) - Retrieve a job
* [get_ats_scorecard2](docs/sdks/ats/README.md#get_ats_scorecard2) - Retrieve a scorecard
* [list_ats_activities2](docs/sdks/ats/README.md#list_ats_activities2) - List all activities
* [list_ats_applications2](docs/sdks/ats/README.md#list_ats_applications2) - List all applications
* [list_ats_applicationstatuses2](docs/sdks/ats/README.md#list_ats_applicationstatuses2) - List all applicationstatuses
* [list_ats_candidates2](docs/sdks/ats/README.md#list_ats_candidates2) - List all candidates
* [list_ats_companies2](docs/sdks/ats/README.md#list_ats_companies2) - List all companies
* [list_ats_documents2](docs/sdks/ats/README.md#list_ats_documents2) - List all documents
* [list_ats_interviews2](docs/sdks/ats/README.md#list_ats_interviews2) - List all interviews
* [list_ats_jobs2](docs/sdks/ats/README.md#list_ats_jobs2) - List all jobs
* [list_ats_scorecards2](docs/sdks/ats/README.md#list_ats_scorecards2) - List all scorecards
* [patch_ats_activity2](docs/sdks/ats/README.md#patch_ats_activity2) - Update an activity
* [patch_ats_application2](docs/sdks/ats/README.md#patch_ats_application2) - Update an application
* [patch_ats_candidate2](docs/sdks/ats/README.md#patch_ats_candidate2) - Update a candidate
* [patch_ats_company2](docs/sdks/ats/README.md#patch_ats_company2) - Update a company
* [patch_ats_document2](docs/sdks/ats/README.md#patch_ats_document2) - Update a document
* [patch_ats_interview2](docs/sdks/ats/README.md#patch_ats_interview2) - Update an interview
* [patch_ats_job2](docs/sdks/ats/README.md#patch_ats_job2) - Update a job
* [patch_ats_scorecard2](docs/sdks/ats/README.md#patch_ats_scorecard2) - Update a scorecard
* [remove_ats_activity2](docs/sdks/ats/README.md#remove_ats_activity2) - Remove an activity
* [remove_ats_application2](docs/sdks/ats/README.md#remove_ats_application2) - Remove an application
* [remove_ats_candidate2](docs/sdks/ats/README.md#remove_ats_candidate2) - Remove a candidate
* [remove_ats_company2](docs/sdks/ats/README.md#remove_ats_company2) - Remove a company
* [remove_ats_document2](docs/sdks/ats/README.md#remove_ats_document2) - Remove a document
* [remove_ats_interview2](docs/sdks/ats/README.md#remove_ats_interview2) - Remove an interview
* [remove_ats_job2](docs/sdks/ats/README.md#remove_ats_job2) - Remove a job
* [remove_ats_scorecard2](docs/sdks/ats/README.md#remove_ats_scorecard2) - Remove a scorecard
* [update_ats_activity2](docs/sdks/ats/README.md#update_ats_activity2) - Update an activity
* [update_ats_application2](docs/sdks/ats/README.md#update_ats_application2) - Update an application
* [update_ats_candidate2](docs/sdks/ats/README.md#update_ats_candidate2) - Update a candidate
* [update_ats_company2](docs/sdks/ats/README.md#update_ats_company2) - Update a company
* [update_ats_document2](docs/sdks/ats/README.md#update_ats_document2) - Update a document
* [update_ats_interview2](docs/sdks/ats/README.md#update_ats_interview2) - Update an interview
* [update_ats_job2](docs/sdks/ats/README.md#update_ats_job2) - Update a job
* [update_ats_scorecard2](docs/sdks/ats/README.md#update_ats_scorecard2) - Update a scorecard

### [Auth](docs/sdks/auth/README.md)

* [get_unified_integration_auth](docs/sdks/auth/README.md#get_unified_integration_auth) - Authorize new connection
* [get_unified_integration_login](docs/sdks/auth/README.md#get_unified_integration_login) - Sign in a user

### [Availability](docs/sdks/availability/README.md)

* [list_commerce_availabilities2](docs/sdks/availability/README.md#list_commerce_availabilities2) - List all availabilities

### [Balancesheet](docs/sdks/balancesheet/README.md)

* [get_accounting_balancesheet2](docs/sdks/balancesheet/README.md#get_accounting_balancesheet2) - Retrieve a balancesheet
* [list_accounting_balancesheets2](docs/sdks/balancesheet/README.md#list_accounting_balancesheets2) - List all balancesheets

### [Bankaccount](docs/sdks/bankaccount/README.md)

* [create_hris_bankaccount2](docs/sdks/bankaccount/README.md#create_hris_bankaccount2) - Create a bankaccount
* [get_hris_bankaccount2](docs/sdks/bankaccount/README.md#get_hris_bankaccount2) - Retrieve a bankaccount
* [list_hris_bankaccounts2](docs/sdks/bankaccount/README.md#list_hris_bankaccounts2) - List all bankaccounts
* [patch_hris_bankaccount2](docs/sdks/bankaccount/README.md#patch_hris_bankaccount2) - Update a bankaccount
* [remove_hris_bankaccount2](docs/sdks/bankaccount/README.md#remove_hris_bankaccount2) - Remove a bankaccount
* [update_hris_bankaccount2](docs/sdks/bankaccount/README.md#update_hris_bankaccount2) - Update a bankaccount

### [Benefit](docs/sdks/benefit/README.md)

* [create_hris_benefit2](docs/sdks/benefit/README.md#create_hris_benefit2) - Create a benefit
* [get_hris_benefit2](docs/sdks/benefit/README.md#get_hris_benefit2) - Retrieve a benefit
* [list_hris_benefits2](docs/sdks/benefit/README.md#list_hris_benefits2) - List all benefits
* [patch_hris_benefit2](docs/sdks/benefit/README.md#patch_hris_benefit2) - Update a benefit
* [remove_hris_benefit2](docs/sdks/benefit/README.md#remove_hris_benefit2) - Remove a benefit
* [update_hris_benefit2](docs/sdks/benefit/README.md#update_hris_benefit2) - Update a benefit

### [Bill](docs/sdks/bill/README.md)

* [create_accounting_bill2](docs/sdks/bill/README.md#create_accounting_bill2) - Create a bill
* [get_accounting_bill2](docs/sdks/bill/README.md#get_accounting_bill2) - Retrieve a bill
* [list_accounting_bills2](docs/sdks/bill/README.md#list_accounting_bills2) - List all bills
* [patch_accounting_bill2](docs/sdks/bill/README.md#patch_accounting_bill2) - Update a bill
* [remove_accounting_bill2](docs/sdks/bill/README.md#remove_accounting_bill2) - Remove a bill
* [update_accounting_bill2](docs/sdks/bill/README.md#update_accounting_bill2) - Update a bill

### [Branch](docs/sdks/branch/README.md)

* [create_repo_branch2](docs/sdks/branch/README.md#create_repo_branch2) - Create a branch
* [get_repo_branch2](docs/sdks/branch/README.md#get_repo_branch2) - Retrieve a branch
* [list_repo_branches2](docs/sdks/branch/README.md#list_repo_branches2) - List all branches
* [patch_repo_branch2](docs/sdks/branch/README.md#patch_repo_branch2) - Update a branch
* [remove_repo_branch2](docs/sdks/branch/README.md#remove_repo_branch2) - Remove a branch
* [update_repo_branch2](docs/sdks/branch/README.md#update_repo_branch2) - Update a branch

### [Busy](docs/sdks/busy/README.md)

* [list_calendar_busies2](docs/sdks/busy/README.md#list_calendar_busies2) - List all busies

### [Calendar](docs/sdks/calendar/README.md)

* [create_calendar_calendar2](docs/sdks/calendar/README.md#create_calendar_calendar2) - Create a calendar
* [create_calendar_event2](docs/sdks/calendar/README.md#create_calendar_event2) - Create an event
* [create_calendar_link2](docs/sdks/calendar/README.md#create_calendar_link2) - Create a link
* [create_calendar_webinar2](docs/sdks/calendar/README.md#create_calendar_webinar2) - Create a webinar
* [get_calendar_calendar2](docs/sdks/calendar/README.md#get_calendar_calendar2) - Retrieve a calendar
* [get_calendar_event2](docs/sdks/calendar/README.md#get_calendar_event2) - Retrieve an event
* [get_calendar_link2](docs/sdks/calendar/README.md#get_calendar_link2) - Retrieve a link
* [get_calendar_recording2](docs/sdks/calendar/README.md#get_calendar_recording2) - Retrieve a recording
* [get_calendar_webinar2](docs/sdks/calendar/README.md#get_calendar_webinar2) - Retrieve a webinar
* [list_calendar_busies2](docs/sdks/calendar/README.md#list_calendar_busies2) - List all busies
* [list_calendar_calendars2](docs/sdks/calendar/README.md#list_calendar_calendars2) - List all calendars
* [list_calendar_events2](docs/sdks/calendar/README.md#list_calendar_events2) - List all events
* [list_calendar_links2](docs/sdks/calendar/README.md#list_calendar_links2) - List all links
* [list_calendar_recordings2](docs/sdks/calendar/README.md#list_calendar_recordings2) - List all recordings
* [list_calendar_webinars2](docs/sdks/calendar/README.md#list_calendar_webinars2) - List all webinars
* [patch_calendar_calendar2](docs/sdks/calendar/README.md#patch_calendar_calendar2) - Update a calendar
* [patch_calendar_event2](docs/sdks/calendar/README.md#patch_calendar_event2) - Update an event
* [patch_calendar_link2](docs/sdks/calendar/README.md#patch_calendar_link2) - Update a link
* [patch_calendar_webinar2](docs/sdks/calendar/README.md#patch_calendar_webinar2) - Update a webinar
* [remove_calendar_calendar2](docs/sdks/calendar/README.md#remove_calendar_calendar2) - Remove a calendar
* [remove_calendar_event2](docs/sdks/calendar/README.md#remove_calendar_event2) - Remove an event
* [remove_calendar_link2](docs/sdks/calendar/README.md#remove_calendar_link2) - Remove a link
* [remove_calendar_webinar2](docs/sdks/calendar/README.md#remove_calendar_webinar2) - Remove a webinar
* [update_calendar_calendar2](docs/sdks/calendar/README.md#update_calendar_calendar2) - Update a calendar
* [update_calendar_event2](docs/sdks/calendar/README.md#update_calendar_event2) - Update an event
* [update_calendar_link2](docs/sdks/calendar/README.md#update_calendar_link2) - Update a link
* [update_calendar_webinar2](docs/sdks/calendar/README.md#update_calendar_webinar2) - Update a webinar

### [Call](docs/sdks/call/README.md)

* [get_uc_call2](docs/sdks/call/README.md#get_uc_call2) - Retrieve a call
* [list_uc_calls2](docs/sdks/call/README.md#list_uc_calls2) - List all calls

### [Campaign](docs/sdks/campaign/README.md)

* [create_ads_campaign2](docs/sdks/campaign/README.md#create_ads_campaign2) - Create a campaign
* [create_martech_campaign2](docs/sdks/campaign/README.md#create_martech_campaign2) - Create a campaign
* [get_ads_campaign2](docs/sdks/campaign/README.md#get_ads_campaign2) - Retrieve a campaign
* [get_martech_campaign2](docs/sdks/campaign/README.md#get_martech_campaign2) - Retrieve a campaign
* [list_ads_campaigns2](docs/sdks/campaign/README.md#list_ads_campaigns2) - List all campaigns
* [list_martech_campaigns2](docs/sdks/campaign/README.md#list_martech_campaigns2) - List all campaigns
* [patch_ads_campaign2](docs/sdks/campaign/README.md#patch_ads_campaign2) - Update a campaign
* [patch_martech_campaign2](docs/sdks/campaign/README.md#patch_martech_campaign2) - Update a campaign
* [remove_ads_campaign2](docs/sdks/campaign/README.md#remove_ads_campaign2) - Remove a campaign
* [remove_martech_campaign2](docs/sdks/campaign/README.md#remove_martech_campaign2) - Remove a campaign
* [update_ads_campaign2](docs/sdks/campaign/README.md#update_ads_campaign2) - Update a campaign
* [update_martech_campaign2](docs/sdks/campaign/README.md#update_martech_campaign2) - Update a campaign

### [Candidate](docs/sdks/candidate/README.md)

* [create_ats_candidate2](docs/sdks/candidate/README.md#create_ats_candidate2) - Create a candidate
* [get_ats_candidate2](docs/sdks/candidate/README.md#get_ats_candidate2) - Retrieve a candidate
* [list_ats_candidates2](docs/sdks/candidate/README.md#list_ats_candidates2) - List all candidates
* [patch_ats_candidate2](docs/sdks/candidate/README.md#patch_ats_candidate2) - Update a candidate
* [remove_ats_candidate2](docs/sdks/candidate/README.md#remove_ats_candidate2) - Remove a candidate
* [update_ats_candidate2](docs/sdks/candidate/README.md#update_ats_candidate2) - Update a candidate

### [Carrier](docs/sdks/carrier/README.md)

* [get_shipping_carrier2](docs/sdks/carrier/README.md#get_shipping_carrier2) - Retrieve a carrier
* [list_shipping_carriers2](docs/sdks/carrier/README.md#list_shipping_carriers2) - List all carriers

### [Cashflow](docs/sdks/cashflow/README.md)

* [get_accounting_cashflow2](docs/sdks/cashflow/README.md#get_accounting_cashflow2) - Retrieve a cashflow
* [list_accounting_cashflows2](docs/sdks/cashflow/README.md#list_accounting_cashflows2) - List all cashflows

### [Category](docs/sdks/category/README.md)

* [create_accounting_category2](docs/sdks/category/README.md#create_accounting_category2) - Create a category
* [create_ticketing_category2](docs/sdks/category/README.md#create_ticketing_category2) - Create a category
* [get_accounting_category2](docs/sdks/category/README.md#get_accounting_category2) - Retrieve a category
* [get_ticketing_category2](docs/sdks/category/README.md#get_ticketing_category2) - Retrieve a category
* [list_accounting_categories2](docs/sdks/category/README.md#list_accounting_categories2) - List all categories
* [list_ticketing_categories2](docs/sdks/category/README.md#list_ticketing_categories2) - List all categories
* [patch_accounting_category2](docs/sdks/category/README.md#patch_accounting_category2) - Update a category
* [patch_ticketing_category2](docs/sdks/category/README.md#patch_ticketing_category2) - Update a category
* [remove_accounting_category2](docs/sdks/category/README.md#remove_accounting_category2) - Remove a category
* [remove_ticketing_category2](docs/sdks/category/README.md#remove_ticketing_category2) - Remove a category
* [update_accounting_category2](docs/sdks/category/README.md#update_accounting_category2) - Update a category
* [update_ticketing_category2](docs/sdks/category/README.md#update_ticketing_category2) - Update a category

### [Change](docs/sdks/change/README.md)

* [get_task_change2](docs/sdks/change/README.md#get_task_change2) - Retrieve a change
* [list_task_changes2](docs/sdks/change/README.md#list_task_changes2) - List all changes

### [Channel](docs/sdks/channel/README.md)

* [get_messaging_channel2](docs/sdks/channel/README.md#get_messaging_channel2) - Retrieve a channel
* [list_messaging_channels2](docs/sdks/channel/README.md#list_messaging_channels2) - List all channels

### [Class](docs/sdks/class/README.md)

* [create_lms_class2](docs/sdks/class/README.md#create_lms_class2) - Create a class
* [get_lms_class2](docs/sdks/class/README.md#get_lms_class2) - Retrieve a class
* [list_lms_classes2](docs/sdks/class/README.md#list_lms_classes2) - List all classes
* [patch_lms_class2](docs/sdks/class/README.md#patch_lms_class2) - Update a class
* [remove_lms_class2](docs/sdks/class/README.md#remove_lms_class2) - Remove a class
* [update_lms_class2](docs/sdks/class/README.md#update_lms_class2) - Update a class

### [Clubs](docs/sdks/clubs/README.md)

* [get_clubs_activity2](docs/sdks/clubs/README.md#get_clubs_activity2) - Retrieve an activity
* [get_clubs_event2](docs/sdks/clubs/README.md#get_clubs_event2) - Retrieve an event
* [get_clubs_group2](docs/sdks/clubs/README.md#get_clubs_group2) - Retrieve a group
* [get_clubs_location2](docs/sdks/clubs/README.md#get_clubs_location2) - Retrieve a location
* [get_clubs_member2](docs/sdks/clubs/README.md#get_clubs_member2) - Retrieve a member
* [list_clubs_activities2](docs/sdks/clubs/README.md#list_clubs_activities2) - List all activities
* [list_clubs_events2](docs/sdks/clubs/README.md#list_clubs_events2) - List all events
* [list_clubs_groups2](docs/sdks/clubs/README.md#list_clubs_groups2) - List all groups
* [list_clubs_locations2](docs/sdks/clubs/README.md#list_clubs_locations2) - List all locations
* [list_clubs_members2](docs/sdks/clubs/README.md#list_clubs_members2) - List all members

### [Collection](docs/sdks/collection/README.md)

* [create_commerce_collection2](docs/sdks/collection/README.md#create_commerce_collection2) - Create a collection
* [create_lms_collection2](docs/sdks/collection/README.md#create_lms_collection2) - Create a collection
* [get_commerce_collection2](docs/sdks/collection/README.md#get_commerce_collection2) - Retrieve a collection
* [get_lms_collection2](docs/sdks/collection/README.md#get_lms_collection2) - Retrieve a collection
* [list_commerce_collections2](docs/sdks/collection/README.md#list_commerce_collections2) - List all collections
* [list_lms_collections2](docs/sdks/collection/README.md#list_lms_collections2) - List all collections
* [patch_commerce_collection2](docs/sdks/collection/README.md#patch_commerce_collection2) - Update a collection
* [patch_lms_collection2](docs/sdks/collection/README.md#patch_lms_collection2) - Update a collection
* [remove_commerce_collection2](docs/sdks/collection/README.md#remove_commerce_collection2) - Remove a collection
* [remove_lms_collection2](docs/sdks/collection/README.md#remove_lms_collection2) - Remove a collection
* [update_commerce_collection2](docs/sdks/collection/README.md#update_commerce_collection2) - Update a collection
* [update_lms_collection2](docs/sdks/collection/README.md#update_lms_collection2) - Update a collection

### [Comment](docs/sdks/comment/README.md)

* [create_kms_comment2](docs/sdks/comment/README.md#create_kms_comment2) - Create a comment
* [create_task_comment2](docs/sdks/comment/README.md#create_task_comment2) - Create a comment
* [create_uc_comment2](docs/sdks/comment/README.md#create_uc_comment2) - Create a comment
* [get_kms_comment2](docs/sdks/comment/README.md#get_kms_comment2) - Retrieve a comment
* [get_task_comment2](docs/sdks/comment/README.md#get_task_comment2) - Retrieve a comment
* [get_uc_comment2](docs/sdks/comment/README.md#get_uc_comment2) - Retrieve a comment
* [list_kms_comments2](docs/sdks/comment/README.md#list_kms_comments2) - List all comments
* [list_task_comments2](docs/sdks/comment/README.md#list_task_comments2) - List all comments
* [list_uc_comments2](docs/sdks/comment/README.md#list_uc_comments2) - List all comments
* [patch_kms_comment2](docs/sdks/comment/README.md#patch_kms_comment2) - Update a comment
* [patch_task_comment2](docs/sdks/comment/README.md#patch_task_comment2) - Update a comment
* [patch_uc_comment2](docs/sdks/comment/README.md#patch_uc_comment2) - Update a comment
* [remove_kms_comment2](docs/sdks/comment/README.md#remove_kms_comment2) - Remove a comment
* [remove_task_comment2](docs/sdks/comment/README.md#remove_task_comment2) - Remove a comment
* [remove_uc_comment2](docs/sdks/comment/README.md#remove_uc_comment2) - Remove a comment
* [update_kms_comment2](docs/sdks/comment/README.md#update_kms_comment2) - Update a comment
* [update_task_comment2](docs/sdks/comment/README.md#update_task_comment2) - Update a comment
* [update_uc_comment2](docs/sdks/comment/README.md#update_uc_comment2) - Update a comment

### [Commerce](docs/sdks/commerce/README.md)

* [create_commerce_collection2](docs/sdks/commerce/README.md#create_commerce_collection2) - Create a collection
* [create_commerce_inventory2](docs/sdks/commerce/README.md#create_commerce_inventory2) - Create an inventory
* [create_commerce_item2](docs/sdks/commerce/README.md#create_commerce_item2) - Create an item
* [create_commerce_itemvariant2](docs/sdks/commerce/README.md#create_commerce_itemvariant2) - Create an itemvariant
* [create_commerce_location2](docs/sdks/commerce/README.md#create_commerce_location2) - Create a location
* [create_commerce_reservation2](docs/sdks/commerce/README.md#create_commerce_reservation2) - Create a reservation
* [create_commerce_review2](docs/sdks/commerce/README.md#create_commerce_review2) - Create a review
* [create_commerce_saleschannel2](docs/sdks/commerce/README.md#create_commerce_saleschannel2) - Create a saleschannel
* [get_commerce_collection2](docs/sdks/commerce/README.md#get_commerce_collection2) - Retrieve a collection
* [get_commerce_inventory2](docs/sdks/commerce/README.md#get_commerce_inventory2) - Retrieve an inventory
* [get_commerce_item2](docs/sdks/commerce/README.md#get_commerce_item2) - Retrieve an item
* [get_commerce_itemvariant2](docs/sdks/commerce/README.md#get_commerce_itemvariant2) - Retrieve an itemvariant
* [get_commerce_location2](docs/sdks/commerce/README.md#get_commerce_location2) - Retrieve a location
* [get_commerce_reservation2](docs/sdks/commerce/README.md#get_commerce_reservation2) - Retrieve a reservation
* [get_commerce_review2](docs/sdks/commerce/README.md#get_commerce_review2) - Retrieve a review
* [get_commerce_saleschannel2](docs/sdks/commerce/README.md#get_commerce_saleschannel2) - Retrieve a saleschannel
* [list_commerce_availabilities2](docs/sdks/commerce/README.md#list_commerce_availabilities2) - List all availabilities
* [list_commerce_collections2](docs/sdks/commerce/README.md#list_commerce_collections2) - List all collections
* [list_commerce_inventories2](docs/sdks/commerce/README.md#list_commerce_inventories2) - List all inventories
* [list_commerce_items2](docs/sdks/commerce/README.md#list_commerce_items2) - List all items
* [list_commerce_itemvariants2](docs/sdks/commerce/README.md#list_commerce_itemvariants2) - List all itemvariants
* [list_commerce_locations2](docs/sdks/commerce/README.md#list_commerce_locations2) - List all locations
* [list_commerce_reservations2](docs/sdks/commerce/README.md#list_commerce_reservations2) - List all reservations
* [list_commerce_reviews2](docs/sdks/commerce/README.md#list_commerce_reviews2) - List all reviews
* [list_commerce_saleschannels2](docs/sdks/commerce/README.md#list_commerce_saleschannels2) - List all saleschannels
* [patch_commerce_collection2](docs/sdks/commerce/README.md#patch_commerce_collection2) - Update a collection
* [patch_commerce_inventory2](docs/sdks/commerce/README.md#patch_commerce_inventory2) - Update an inventory
* [patch_commerce_item2](docs/sdks/commerce/README.md#patch_commerce_item2) - Update an item
* [patch_commerce_itemvariant2](docs/sdks/commerce/README.md#patch_commerce_itemvariant2) - Update an itemvariant
* [patch_commerce_location2](docs/sdks/commerce/README.md#patch_commerce_location2) - Update a location
* [patch_commerce_reservation2](docs/sdks/commerce/README.md#patch_commerce_reservation2) - Update a reservation
* [patch_commerce_review2](docs/sdks/commerce/README.md#patch_commerce_review2) - Update a review
* [patch_commerce_saleschannel2](docs/sdks/commerce/README.md#patch_commerce_saleschannel2) - Update a saleschannel
* [remove_commerce_collection2](docs/sdks/commerce/README.md#remove_commerce_collection2) - Remove a collection
* [remove_commerce_inventory2](docs/sdks/commerce/README.md#remove_commerce_inventory2) - Remove an inventory
* [remove_commerce_item2](docs/sdks/commerce/README.md#remove_commerce_item2) - Remove an item
* [remove_commerce_itemvariant2](docs/sdks/commerce/README.md#remove_commerce_itemvariant2) - Remove an itemvariant
* [remove_commerce_location2](docs/sdks/commerce/README.md#remove_commerce_location2) - Remove a location
* [remove_commerce_reservation2](docs/sdks/commerce/README.md#remove_commerce_reservation2) - Remove a reservation
* [remove_commerce_review2](docs/sdks/commerce/README.md#remove_commerce_review2) - Remove a review
* [remove_commerce_saleschannel2](docs/sdks/commerce/README.md#remove_commerce_saleschannel2) - Remove a saleschannel
* [update_commerce_collection2](docs/sdks/commerce/README.md#update_commerce_collection2) - Update a collection
* [update_commerce_inventory2](docs/sdks/commerce/README.md#update_commerce_inventory2) - Update an inventory
* [update_commerce_item2](docs/sdks/commerce/README.md#update_commerce_item2) - Update an item
* [update_commerce_itemvariant2](docs/sdks/commerce/README.md#update_commerce_itemvariant2) - Update an itemvariant
* [update_commerce_location2](docs/sdks/commerce/README.md#update_commerce_location2) - Update a location
* [update_commerce_reservation2](docs/sdks/commerce/README.md#update_commerce_reservation2) - Update a reservation
* [update_commerce_review2](docs/sdks/commerce/README.md#update_commerce_review2) - Update a review
* [update_commerce_saleschannel2](docs/sdks/commerce/README.md#update_commerce_saleschannel2) - Update a saleschannel

### [Commit](docs/sdks/commit/README.md)

* [create_repo_commit2](docs/sdks/commit/README.md#create_repo_commit2) - Create a commit
* [get_repo_commit2](docs/sdks/commit/README.md#get_repo_commit2) - Retrieve a commit
* [list_repo_commits2](docs/sdks/commit/README.md#list_repo_commits2) - List all commits
* [patch_repo_commit2](docs/sdks/commit/README.md#patch_repo_commit2) - Update a commit
* [remove_repo_commit2](docs/sdks/commit/README.md#remove_repo_commit2) - Remove a commit
* [update_repo_commit2](docs/sdks/commit/README.md#update_repo_commit2) - Update a commit

### [Company](docs/sdks/company/README.md)

* [create_ats_company2](docs/sdks/company/README.md#create_ats_company2) - Create a company
* [create_crm_company2](docs/sdks/company/README.md#create_crm_company2) - Create a company
* [create_hris_company2](docs/sdks/company/README.md#create_hris_company2) - Create a company
* [get_ats_company2](docs/sdks/company/README.md#get_ats_company2) - Retrieve a company
* [get_crm_company2](docs/sdks/company/README.md#get_crm_company2) - Retrieve a company
* [get_hris_company2](docs/sdks/company/README.md#get_hris_company2) - Retrieve a company
* [list_ats_companies2](docs/sdks/company/README.md#list_ats_companies2) - List all companies
* [list_crm_companies2](docs/sdks/company/README.md#list_crm_companies2) - List all companies
* [list_enrich_companies2](docs/sdks/company/README.md#list_enrich_companies2) - Retrieve enrichment information for a company
* [list_hris_companies2](docs/sdks/company/README.md#list_hris_companies2) - List all companies
* [patch_ats_company2](docs/sdks/company/README.md#patch_ats_company2) - Update a company
* [patch_crm_company2](docs/sdks/company/README.md#patch_crm_company2) - Update a company
* [patch_hris_company2](docs/sdks/company/README.md#patch_hris_company2) - Update a company
* [remove_ats_company2](docs/sdks/company/README.md#remove_ats_company2) - Remove a company
* [remove_crm_company2](docs/sdks/company/README.md#remove_crm_company2) - Remove a company
* [remove_hris_company2](docs/sdks/company/README.md#remove_hris_company2) - Remove a company
* [update_ats_company2](docs/sdks/company/README.md#update_ats_company2) - Update a company
* [update_crm_company2](docs/sdks/company/README.md#update_crm_company2) - Update a company
* [update_hris_company2](docs/sdks/company/README.md#update_hris_company2) - Update a company

### [Connection](docs/sdks/connection/README.md)

* [create_unified_connection](docs/sdks/connection/README.md#create_unified_connection) - Create connection
* [get_unified_connection](docs/sdks/connection/README.md#get_unified_connection) - Retrieve connection
* [list_unified_connections](docs/sdks/connection/README.md#list_unified_connections) - List all connections
* [patch_unified_connection](docs/sdks/connection/README.md#patch_unified_connection) - Update connection
* [remove_unified_connection](docs/sdks/connection/README.md#remove_unified_connection) - Remove connection
* [update_unified_connection](docs/sdks/connection/README.md#update_unified_connection) - Update connection

### [Contact](docs/sdks/contact/README.md)

* [create_accounting_contact2](docs/sdks/contact/README.md#create_accounting_contact2) - Create a contact
* [create_crm_contact2](docs/sdks/contact/README.md#create_crm_contact2) - Create a contact
* [create_uc_contact2](docs/sdks/contact/README.md#create_uc_contact2) - Create a contact
* [get_accounting_contact2](docs/sdks/contact/README.md#get_accounting_contact2) - Retrieve a contact
* [get_crm_contact2](docs/sdks/contact/README.md#get_crm_contact2) - Retrieve a contact
* [get_uc_contact2](docs/sdks/contact/README.md#get_uc_contact2) - Retrieve a contact
* [list_accounting_contacts2](docs/sdks/contact/README.md#list_accounting_contacts2) - List all contacts
* [list_crm_contacts2](docs/sdks/contact/README.md#list_crm_contacts2) - List all contacts
* [list_uc_contacts2](docs/sdks/contact/README.md#list_uc_contacts2) - List all contacts
* [patch_accounting_contact2](docs/sdks/contact/README.md#patch_accounting_contact2) - Update a contact
* [patch_crm_contact2](docs/sdks/contact/README.md#patch_crm_contact2) - Update a contact
* [patch_uc_contact2](docs/sdks/contact/README.md#patch_uc_contact2) - Update a contact
* [remove_accounting_contact2](docs/sdks/contact/README.md#remove_accounting_contact2) - Remove a contact
* [remove_crm_contact2](docs/sdks/contact/README.md#remove_crm_contact2) - Remove a contact
* [remove_uc_contact2](docs/sdks/contact/README.md#remove_uc_contact2) - Remove a contact
* [update_accounting_contact2](docs/sdks/contact/README.md#update_accounting_contact2) - Update a contact
* [update_crm_contact2](docs/sdks/contact/README.md#update_crm_contact2) - Update a contact
* [update_uc_contact2](docs/sdks/contact/README.md#update_uc_contact2) - Update a contact

### [Content](docs/sdks/content/README.md)

* [create_lms_content2](docs/sdks/content/README.md#create_lms_content2) - Create a content
* [get_lms_content2](docs/sdks/content/README.md#get_lms_content2) - Retrieve a content
* [list_lms_contents2](docs/sdks/content/README.md#list_lms_contents2) - List all contents
* [patch_lms_content2](docs/sdks/content/README.md#patch_lms_content2) - Update a content
* [remove_lms_content2](docs/sdks/content/README.md#remove_lms_content2) - Remove a content
* [update_lms_content2](docs/sdks/content/README.md#update_lms_content2) - Update a content

### [Course](docs/sdks/course/README.md)

* [create_lms_course2](docs/sdks/course/README.md#create_lms_course2) - Create a course
* [get_lms_course2](docs/sdks/course/README.md#get_lms_course2) - Retrieve a course
* [list_lms_courses2](docs/sdks/course/README.md#list_lms_courses2) - List all courses
* [patch_lms_course2](docs/sdks/course/README.md#patch_lms_course2) - Update a course
* [remove_lms_course2](docs/sdks/course/README.md#remove_lms_course2) - Remove a course
* [update_lms_course2](docs/sdks/course/README.md#update_lms_course2) - Update a course

### [Creative](docs/sdks/creative/README.md)

* [create_ads_creative2](docs/sdks/creative/README.md#create_ads_creative2) - Create a creative
* [get_ads_creative2](docs/sdks/creative/README.md#get_ads_creative2) - Retrieve a creative
* [list_ads_creatives2](docs/sdks/creative/README.md#list_ads_creatives2) - List all creatives
* [patch_ads_creative2](docs/sdks/creative/README.md#patch_ads_creative2) - Update a creative
* [remove_ads_creative2](docs/sdks/creative/README.md#remove_ads_creative2) - Remove a creative
* [update_ads_creative2](docs/sdks/creative/README.md#update_ads_creative2) - Update a creative

### [Creditmemo](docs/sdks/creditmemo/README.md)

* [create_accounting_creditmemo2](docs/sdks/creditmemo/README.md#create_accounting_creditmemo2) - Create a creditmemo
* [get_accounting_creditmemo2](docs/sdks/creditmemo/README.md#get_accounting_creditmemo2) - Retrieve a creditmemo
* [list_accounting_creditmemoes2](docs/sdks/creditmemo/README.md#list_accounting_creditmemoes2) - List all creditmemoes
* [patch_accounting_creditmemo2](docs/sdks/creditmemo/README.md#patch_accounting_creditmemo2) - Update a creditmemo
* [remove_accounting_creditmemo2](docs/sdks/creditmemo/README.md#remove_accounting_creditmemo2) - Remove a creditmemo
* [update_accounting_creditmemo2](docs/sdks/creditmemo/README.md#update_accounting_creditmemo2) - Update a creditmemo

### [Crm](docs/sdks/crm/README.md)

* [create_crm_company2](docs/sdks/crm/README.md#create_crm_company2) - Create a company
* [create_crm_contact2](docs/sdks/crm/README.md#create_crm_contact2) - Create a contact
* [create_crm_deal2](docs/sdks/crm/README.md#create_crm_deal2) - Create a deal
* [create_crm_event2](docs/sdks/crm/README.md#create_crm_event2) - Create an event
* [create_crm_lead2](docs/sdks/crm/README.md#create_crm_lead2) - Create a lead
* [create_crm_pipeline2](docs/sdks/crm/README.md#create_crm_pipeline2) - Create a pipeline
* [get_crm_company2](docs/sdks/crm/README.md#get_crm_company2) - Retrieve a company
* [get_crm_contact2](docs/sdks/crm/README.md#get_crm_contact2) - Retrieve a contact
* [get_crm_deal2](docs/sdks/crm/README.md#get_crm_deal2) - Retrieve a deal
* [get_crm_event2](docs/sdks/crm/README.md#get_crm_event2) - Retrieve an event
* [get_crm_lead2](docs/sdks/crm/README.md#get_crm_lead2) - Retrieve a lead
* [get_crm_pipeline2](docs/sdks/crm/README.md#get_crm_pipeline2) - Retrieve a pipeline
* [list_crm_companies2](docs/sdks/crm/README.md#list_crm_companies2) - List all companies
* [list_crm_contacts2](docs/sdks/crm/README.md#list_crm_contacts2) - List all contacts
* [list_crm_deals2](docs/sdks/crm/README.md#list_crm_deals2) - List all deals
* [list_crm_events2](docs/sdks/crm/README.md#list_crm_events2) - List all events
* [list_crm_leads2](docs/sdks/crm/README.md#list_crm_leads2) - List all leads
* [list_crm_pipelines2](docs/sdks/crm/README.md#list_crm_pipelines2) - List all pipelines
* [patch_crm_company2](docs/sdks/crm/README.md#patch_crm_company2) - Update a company
* [patch_crm_contact2](docs/sdks/crm/README.md#patch_crm_contact2) - Update a contact
* [patch_crm_deal2](docs/sdks/crm/README.md#patch_crm_deal2) - Update a deal
* [patch_crm_event2](docs/sdks/crm/README.md#patch_crm_event2) - Update an event
* [patch_crm_lead2](docs/sdks/crm/README.md#patch_crm_lead2) - Update a lead
* [patch_crm_pipeline2](docs/sdks/crm/README.md#patch_crm_pipeline2) - Update a pipeline
* [remove_crm_company2](docs/sdks/crm/README.md#remove_crm_company2) - Remove a company
* [remove_crm_contact2](docs/sdks/crm/README.md#remove_crm_contact2) - Remove a contact
* [remove_crm_deal2](docs/sdks/crm/README.md#remove_crm_deal2) - Remove a deal
* [remove_crm_event2](docs/sdks/crm/README.md#remove_crm_event2) - Remove an event
* [remove_crm_lead2](docs/sdks/crm/README.md#remove_crm_lead2) - Remove a lead
* [remove_crm_pipeline2](docs/sdks/crm/README.md#remove_crm_pipeline2) - Remove a pipeline
* [update_crm_company2](docs/sdks/crm/README.md#update_crm_company2) - Update a company
* [update_crm_contact2](docs/sdks/crm/README.md#update_crm_contact2) - Update a contact
* [update_crm_deal2](docs/sdks/crm/README.md#update_crm_deal2) - Update a deal
* [update_crm_event2](docs/sdks/crm/README.md#update_crm_event2) - Update an event
* [update_crm_lead2](docs/sdks/crm/README.md#update_crm_lead2) - Update a lead
* [update_crm_pipeline2](docs/sdks/crm/README.md#update_crm_pipeline2) - Update a pipeline

### [Customer](docs/sdks/customer/README.md)

* [create_ticketing_customer2](docs/sdks/customer/README.md#create_ticketing_customer2) - Create a customer
* [get_ticketing_customer2](docs/sdks/customer/README.md#get_ticketing_customer2) - Retrieve a customer
* [list_ticketing_customers2](docs/sdks/customer/README.md#list_ticketing_customers2) - List all customers
* [patch_ticketing_customer2](docs/sdks/customer/README.md#patch_ticketing_customer2) - Update a customer
* [remove_ticketing_customer2](docs/sdks/customer/README.md#remove_ticketing_customer2) - Remove a customer
* [update_ticketing_customer2](docs/sdks/customer/README.md#update_ticketing_customer2) - Update a customer

### [Database](docs/sdks/database/README.md)

* [create_datastore_database2](docs/sdks/database/README.md#create_datastore_database2) - Create a database
* [get_datastore_database2](docs/sdks/database/README.md#get_datastore_database2) - Retrieve a database
* [list_datastore_databases2](docs/sdks/database/README.md#list_datastore_databases2) - List all databases
* [patch_datastore_database2](docs/sdks/database/README.md#patch_datastore_database2) - Update a database
* [remove_datastore_database2](docs/sdks/database/README.md#remove_datastore_database2) - Remove a database
* [update_datastore_database2](docs/sdks/database/README.md#update_datastore_database2) - Update a database

### [Datastore](docs/sdks/datastore/README.md)

* [create_datastore_database2](docs/sdks/datastore/README.md#create_datastore_database2) - Create a database
* [create_datastore_query2](docs/sdks/datastore/README.md#create_datastore_query2) - Create a query
* [create_datastore_record2](docs/sdks/datastore/README.md#create_datastore_record2) - Create a record
* [create_datastore_table2](docs/sdks/datastore/README.md#create_datastore_table2) - Create a table
* [get_datastore_database2](docs/sdks/datastore/README.md#get_datastore_database2) - Retrieve a database
* [get_datastore_record2](docs/sdks/datastore/README.md#get_datastore_record2) - Retrieve a record
* [get_datastore_table2](docs/sdks/datastore/README.md#get_datastore_table2) - Retrieve a table
* [list_datastore_databases2](docs/sdks/datastore/README.md#list_datastore_databases2) - List all databases
* [list_datastore_records2](docs/sdks/datastore/README.md#list_datastore_records2) - List all records
* [list_datastore_tables2](docs/sdks/datastore/README.md#list_datastore_tables2) - List all tables
* [patch_datastore_database2](docs/sdks/datastore/README.md#patch_datastore_database2) - Update a database
* [patch_datastore_record2](docs/sdks/datastore/README.md#patch_datastore_record2) - Update a record
* [patch_datastore_table2](docs/sdks/datastore/README.md#patch_datastore_table2) - Update a table
* [remove_datastore_database2](docs/sdks/datastore/README.md#remove_datastore_database2) - Remove a database
* [remove_datastore_record2](docs/sdks/datastore/README.md#remove_datastore_record2) - Remove a record
* [remove_datastore_table2](docs/sdks/datastore/README.md#remove_datastore_table2) - Remove a table
* [update_datastore_database2](docs/sdks/datastore/README.md#update_datastore_database2) - Update a database
* [update_datastore_record2](docs/sdks/datastore/README.md#update_datastore_record2) - Update a record
* [update_datastore_table2](docs/sdks/datastore/README.md#update_datastore_table2) - Update a table

### [Deal](docs/sdks/deal/README.md)

* [create_crm_deal2](docs/sdks/deal/README.md#create_crm_deal2) - Create a deal
* [get_crm_deal2](docs/sdks/deal/README.md#get_crm_deal2) - Retrieve a deal
* [list_crm_deals2](docs/sdks/deal/README.md#list_crm_deals2) - List all deals
* [patch_crm_deal2](docs/sdks/deal/README.md#patch_crm_deal2) - Update a deal
* [remove_crm_deal2](docs/sdks/deal/README.md#remove_crm_deal2) - Remove a deal
* [update_crm_deal2](docs/sdks/deal/README.md#update_crm_deal2) - Update a deal

### [Deduction](docs/sdks/deduction/README.md)

* [create_hris_deduction2](docs/sdks/deduction/README.md#create_hris_deduction2) - Create a deduction
* [get_hris_deduction2](docs/sdks/deduction/README.md#get_hris_deduction2) - Retrieve a deduction
* [list_hris_deductions2](docs/sdks/deduction/README.md#list_hris_deductions2) - List all deductions
* [patch_hris_deduction2](docs/sdks/deduction/README.md#patch_hris_deduction2) - Update a deduction
* [remove_hris_deduction2](docs/sdks/deduction/README.md#remove_hris_deduction2) - Remove a deduction
* [update_hris_deduction2](docs/sdks/deduction/README.md#update_hris_deduction2) - Update a deduction

### [Device](docs/sdks/device/README.md)

* [create_hris_device2](docs/sdks/device/README.md#create_hris_device2) - Create a device
* [get_hris_device2](docs/sdks/device/README.md#get_hris_device2) - Retrieve a device
* [list_hris_devices2](docs/sdks/device/README.md#list_hris_devices2) - List all devices
* [patch_hris_device2](docs/sdks/device/README.md#patch_hris_device2) - Update a device
* [remove_hris_device2](docs/sdks/device/README.md#remove_hris_device2) - Remove a device
* [update_hris_device2](docs/sdks/device/README.md#update_hris_device2) - Update a device

### [Document](docs/sdks/document/README.md)

* [create_ats_document2](docs/sdks/document/README.md#create_ats_document2) - Create a document
* [create_signing_document2](docs/sdks/document/README.md#create_signing_document2) - Create a document
* [get_ats_document2](docs/sdks/document/README.md#get_ats_document2) - Retrieve a document
* [get_signing_document2](docs/sdks/document/README.md#get_signing_document2) - Retrieve a document
* [list_ats_documents2](docs/sdks/document/README.md#list_ats_documents2) - List all documents
* [list_signing_documents2](docs/sdks/document/README.md#list_signing_documents2) - List all documents
* [patch_ats_document2](docs/sdks/document/README.md#patch_ats_document2) - Update a document
* [patch_signing_document2](docs/sdks/document/README.md#patch_signing_document2) - Update a document
* [remove_ats_document2](docs/sdks/document/README.md#remove_ats_document2) - Remove a document
* [remove_signing_document2](docs/sdks/document/README.md#remove_signing_document2) - Remove a document
* [update_ats_document2](docs/sdks/document/README.md#update_ats_document2) - Update a document
* [update_signing_document2](docs/sdks/document/README.md#update_signing_document2) - Update a document

### [Embedding](docs/sdks/embedding/README.md)

* [create_genai_embedding2](docs/sdks/embedding/README.md#create_genai_embedding2) - Create an embedding

### [Employee](docs/sdks/employee/README.md)

* [create_hris_employee2](docs/sdks/employee/README.md#create_hris_employee2) - Create an employee
* [get_hris_employee2](docs/sdks/employee/README.md#get_hris_employee2) - Retrieve an employee
* [list_hris_employees2](docs/sdks/employee/README.md#list_hris_employees2) - List all employees
* [patch_hris_employee2](docs/sdks/employee/README.md#patch_hris_employee2) - Update an employee
* [remove_hris_employee2](docs/sdks/employee/README.md#remove_hris_employee2) - Remove an employee
* [update_hris_employee2](docs/sdks/employee/README.md#update_hris_employee2) - Update an employee

### [Enrich](docs/sdks/enrich/README.md)

* [list_enrich_companies2](docs/sdks/enrich/README.md#list_enrich_companies2) - Retrieve enrichment information for a company
* [list_enrich_people2](docs/sdks/enrich/README.md#list_enrich_people2) - Retrieve enrichment information for a person

### [Environment](docs/sdks/environment/README.md)

* [create_unified_environment](docs/sdks/environment/README.md#create_unified_environment) - Create new environments
* [list_unified_environments](docs/sdks/environment/README.md#list_unified_environments) - Returns all environments
* [remove_unified_environment](docs/sdks/environment/README.md#remove_unified_environment) - Remove an environment

### [Event](docs/sdks/event/README.md)

* [create_analytics_event2](docs/sdks/event/README.md#create_analytics_event2) - Create an event
* [create_calendar_event2](docs/sdks/event/README.md#create_calendar_event2) - Create an event
* [create_crm_event2](docs/sdks/event/README.md#create_crm_event2) - Create an event
* [get_analytics_event2](docs/sdks/event/README.md#get_analytics_event2) - Retrieve an event
* [get_calendar_event2](docs/sdks/event/README.md#get_calendar_event2) - Retrieve an event
* [get_clubs_event2](docs/sdks/event/README.md#get_clubs_event2) - Retrieve an event
* [get_crm_event2](docs/sdks/event/README.md#get_crm_event2) - Retrieve an event
* [list_analytics_events2](docs/sdks/event/README.md#list_analytics_events2) - List all events
* [list_calendar_events2](docs/sdks/event/README.md#list_calendar_events2) - List all events
* [list_clubs_events2](docs/sdks/event/README.md#list_clubs_events2) - List all events
* [list_crm_events2](docs/sdks/event/README.md#list_crm_events2) - List all events
* [patch_calendar_event2](docs/sdks/event/README.md#patch_calendar_event2) - Update an event
* [patch_crm_event2](docs/sdks/event/README.md#patch_crm_event2) - Update an event
* [patch_messaging_event2](docs/sdks/event/README.md#patch_messaging_event2) - Update an event
* [remove_calendar_event2](docs/sdks/event/README.md#remove_calendar_event2) - Remove an event
* [remove_crm_event2](docs/sdks/event/README.md#remove_crm_event2) - Remove an event
* [update_calendar_event2](docs/sdks/event/README.md#update_calendar_event2) - Update an event
* [update_crm_event2](docs/sdks/event/README.md#update_crm_event2) - Update an event
* [update_messaging_event2](docs/sdks/event/README.md#update_messaging_event2) - Update an event

### [Expense](docs/sdks/expense/README.md)

* [create_accounting_expense2](docs/sdks/expense/README.md#create_accounting_expense2) - Create an expense
* [get_accounting_expense2](docs/sdks/expense/README.md#get_accounting_expense2) - Retrieve an expense
* [list_accounting_expenses2](docs/sdks/expense/README.md#list_accounting_expenses2) - List all expenses
* [patch_accounting_expense2](docs/sdks/expense/README.md#patch_accounting_expense2) - Update an expense
* [remove_accounting_expense2](docs/sdks/expense/README.md#remove_accounting_expense2) - Remove an expense
* [update_accounting_expense2](docs/sdks/expense/README.md#update_accounting_expense2) - Update an expense

### [File](docs/sdks/file/README.md)

* [create_storage_file2](docs/sdks/file/README.md#create_storage_file2) - Create a file
* [get_storage_file2](docs/sdks/file/README.md#get_storage_file2) - Retrieve a file
* [list_storage_files2](docs/sdks/file/README.md#list_storage_files2) - List all files
* [patch_storage_file2](docs/sdks/file/README.md#patch_storage_file2) - Update a file
* [remove_storage_file2](docs/sdks/file/README.md#remove_storage_file2) - Remove a file
* [update_storage_file2](docs/sdks/file/README.md#update_storage_file2) - Update a file

### [Form](docs/sdks/form/README.md)

* [create_forms_form2](docs/sdks/form/README.md#create_forms_form2) - Create a form
* [get_forms_form2](docs/sdks/form/README.md#get_forms_form2) - Retrieve a form
* [list_forms_forms2](docs/sdks/form/README.md#list_forms_forms2) - List all forms
* [patch_forms_form2](docs/sdks/form/README.md#patch_forms_form2) - Update a form
* [remove_forms_form2](docs/sdks/form/README.md#remove_forms_form2) - Remove a form
* [update_forms_form2](docs/sdks/form/README.md#update_forms_form2) - Update a form

### [Forms](docs/sdks/forms/README.md)

* [create_forms_form2](docs/sdks/forms/README.md#create_forms_form2) - Create a form
* [get_forms_form2](docs/sdks/forms/README.md#get_forms_form2) - Retrieve a form
* [get_forms_submission2](docs/sdks/forms/README.md#get_forms_submission2) - Retrieve a submission
* [list_forms_forms2](docs/sdks/forms/README.md#list_forms_forms2) - List all forms
* [list_forms_submissions2](docs/sdks/forms/README.md#list_forms_submissions2) - List all submissions
* [patch_forms_form2](docs/sdks/forms/README.md#patch_forms_form2) - Update a form
* [remove_forms_form2](docs/sdks/forms/README.md#remove_forms_form2) - Remove a form
* [update_forms_form2](docs/sdks/forms/README.md#update_forms_form2) - Update a form

### [Genai](docs/sdks/genai/README.md)

* [create_genai_embedding2](docs/sdks/genai/README.md#create_genai_embedding2) - Create an embedding
* [create_genai_prompt2](docs/sdks/genai/README.md#create_genai_prompt2) - Create a prompt
* [get_genai_model2](docs/sdks/genai/README.md#get_genai_model2) - Retrieve a model
* [list_genai_models2](docs/sdks/genai/README.md#list_genai_models2) - List all models

### [Group](docs/sdks/group/README.md)

* [create_ads_group2](docs/sdks/group/README.md#create_ads_group2) - Create a group
* [create_hris_group2](docs/sdks/group/README.md#create_hris_group2) - Create a group
* [create_scim_groups](docs/sdks/group/README.md#create_scim_groups) - Create group
* [get_ads_group2](docs/sdks/group/README.md#get_ads_group2) - Retrieve a group
* [get_clubs_group2](docs/sdks/group/README.md#get_clubs_group2) - Retrieve a group
* [get_hris_group2](docs/sdks/group/README.md#get_hris_group2) - Retrieve a group
* [get_scim_groups](docs/sdks/group/README.md#get_scim_groups) - Get group
* [list_ads_groups2](docs/sdks/group/README.md#list_ads_groups2) - List all groups
* [list_clubs_groups2](docs/sdks/group/README.md#list_clubs_groups2) - List all groups
* [list_hris_groups2](docs/sdks/group/README.md#list_hris_groups2) - List all groups
* [list_scim_groups](docs/sdks/group/README.md#list_scim_groups) - List groups
* [patch_ads_group2](docs/sdks/group/README.md#patch_ads_group2) - Update a group
* [patch_hris_group2](docs/sdks/group/README.md#patch_hris_group2) - Update a group
* [patch_scim_groups](docs/sdks/group/README.md#patch_scim_groups) - Update group
* [remove_ads_group2](docs/sdks/group/README.md#remove_ads_group2) - Remove a group
* [remove_hris_group2](docs/sdks/group/README.md#remove_hris_group2) - Remove a group
* [remove_scim_groups](docs/sdks/group/README.md#remove_scim_groups) - Delete group
* [update_ads_group2](docs/sdks/group/README.md#update_ads_group2) - Update a group
* [update_hris_group2](docs/sdks/group/README.md#update_hris_group2) - Update a group
* [update_scim_groups](docs/sdks/group/README.md#update_scim_groups) - Update group

### [Hris](docs/sdks/hris/README.md)

* [create_hris_bankaccount2](docs/sdks/hris/README.md#create_hris_bankaccount2) - Create a bankaccount
* [create_hris_benefit2](docs/sdks/hris/README.md#create_hris_benefit2) - Create a benefit
* [create_hris_company2](docs/sdks/hris/README.md#create_hris_company2) - Create a company
* [create_hris_deduction2](docs/sdks/hris/README.md#create_hris_deduction2) - Create a deduction
* [create_hris_device2](docs/sdks/hris/README.md#create_hris_device2) - Create a device
* [create_hris_employee2](docs/sdks/hris/README.md#create_hris_employee2) - Create an employee
* [create_hris_group2](docs/sdks/hris/README.md#create_hris_group2) - Create a group
* [create_hris_location2](docs/sdks/hris/README.md#create_hris_location2) - Create a location
* [create_hris_timeoff2](docs/sdks/hris/README.md#create_hris_timeoff2) - Create a timeoff
* [create_hris_timeshift2](docs/sdks/hris/README.md#create_hris_timeshift2) - Create a timeshift
* [get_hris_bankaccount2](docs/sdks/hris/README.md#get_hris_bankaccount2) - Retrieve a bankaccount
* [get_hris_benefit2](docs/sdks/hris/README.md#get_hris_benefit2) - Retrieve a benefit
* [get_hris_company2](docs/sdks/hris/README.md#get_hris_company2) - Retrieve a company
* [get_hris_deduction2](docs/sdks/hris/README.md#get_hris_deduction2) - Retrieve a deduction
* [get_hris_device2](docs/sdks/hris/README.md#get_hris_device2) - Retrieve a device
* [get_hris_employee2](docs/sdks/hris/README.md#get_hris_employee2) - Retrieve an employee
* [get_hris_group2](docs/sdks/hris/README.md#get_hris_group2) - Retrieve a group
* [get_hris_location2](docs/sdks/hris/README.md#get_hris_location2) - Retrieve a location
* [get_hris_payslip2](docs/sdks/hris/README.md#get_hris_payslip2) - Retrieve a payslip
* [get_hris_timeoff2](docs/sdks/hris/README.md#get_hris_timeoff2) - Retrieve a timeoff
* [get_hris_timeshift2](docs/sdks/hris/README.md#get_hris_timeshift2) - Retrieve a timeshift
* [list_hris_bankaccounts2](docs/sdks/hris/README.md#list_hris_bankaccounts2) - List all bankaccounts
* [list_hris_benefits2](docs/sdks/hris/README.md#list_hris_benefits2) - List all benefits
* [list_hris_companies2](docs/sdks/hris/README.md#list_hris_companies2) - List all companies
* [list_hris_deductions2](docs/sdks/hris/README.md#list_hris_deductions2) - List all deductions
* [list_hris_devices2](docs/sdks/hris/README.md#list_hris_devices2) - List all devices
* [list_hris_employees2](docs/sdks/hris/README.md#list_hris_employees2) - List all employees
* [list_hris_groups2](docs/sdks/hris/README.md#list_hris_groups2) - List all groups
* [list_hris_locations2](docs/sdks/hris/README.md#list_hris_locations2) - List all locations
* [list_hris_payslips2](docs/sdks/hris/README.md#list_hris_payslips2) - List all payslips
* [list_hris_timeoffs2](docs/sdks/hris/README.md#list_hris_timeoffs2) - List all timeoffs
* [list_hris_timeshifts2](docs/sdks/hris/README.md#list_hris_timeshifts2) - List all timeshifts
* [patch_hris_bankaccount2](docs/sdks/hris/README.md#patch_hris_bankaccount2) - Update a bankaccount
* [patch_hris_benefit2](docs/sdks/hris/README.md#patch_hris_benefit2) - Update a benefit
* [patch_hris_company2](docs/sdks/hris/README.md#patch_hris_company2) - Update a company
* [patch_hris_deduction2](docs/sdks/hris/README.md#patch_hris_deduction2) - Update a deduction
* [patch_hris_device2](docs/sdks/hris/README.md#patch_hris_device2) - Update a device
* [patch_hris_employee2](docs/sdks/hris/README.md#patch_hris_employee2) - Update an employee
* [patch_hris_group2](docs/sdks/hris/README.md#patch_hris_group2) - Update a group
* [patch_hris_location2](docs/sdks/hris/README.md#patch_hris_location2) - Update a location
* [patch_hris_timeoff2](docs/sdks/hris/README.md#patch_hris_timeoff2) - Update a timeoff
* [patch_hris_timeshift2](docs/sdks/hris/README.md#patch_hris_timeshift2) - Update a timeshift
* [remove_hris_bankaccount2](docs/sdks/hris/README.md#remove_hris_bankaccount2) - Remove a bankaccount
* [remove_hris_benefit2](docs/sdks/hris/README.md#remove_hris_benefit2) - Remove a benefit
* [remove_hris_company2](docs/sdks/hris/README.md#remove_hris_company2) - Remove a company
* [remove_hris_deduction2](docs/sdks/hris/README.md#remove_hris_deduction2) - Remove a deduction
* [remove_hris_device2](docs/sdks/hris/README.md#remove_hris_device2) - Remove a device
* [remove_hris_employee2](docs/sdks/hris/README.md#remove_hris_employee2) - Remove an employee
* [remove_hris_group2](docs/sdks/hris/README.md#remove_hris_group2) - Remove a group
* [remove_hris_location2](docs/sdks/hris/README.md#remove_hris_location2) - Remove a location
* [remove_hris_timeoff2](docs/sdks/hris/README.md#remove_hris_timeoff2) - Remove a timeoff
* [remove_hris_timeshift2](docs/sdks/hris/README.md#remove_hris_timeshift2) - Remove a timeshift
* [update_hris_bankaccount2](docs/sdks/hris/README.md#update_hris_bankaccount2) - Update a bankaccount
* [update_hris_benefit2](docs/sdks/hris/README.md#update_hris_benefit2) - Update a benefit
* [update_hris_company2](docs/sdks/hris/README.md#update_hris_company2) - Update a company
* [update_hris_deduction2](docs/sdks/hris/README.md#update_hris_deduction2) - Update a deduction
* [update_hris_device2](docs/sdks/hris/README.md#update_hris_device2) - Update a device
* [update_hris_employee2](docs/sdks/hris/README.md#update_hris_employee2) - Update an employee
* [update_hris_group2](docs/sdks/hris/README.md#update_hris_group2) - Update a group
* [update_hris_location2](docs/sdks/hris/README.md#update_hris_location2) - Update a location
* [update_hris_timeoff2](docs/sdks/hris/README.md#update_hris_timeoff2) - Update a timeoff
* [update_hris_timeshift2](docs/sdks/hris/README.md#update_hris_timeshift2) - Update a timeshift

### [Insertionorder](docs/sdks/insertionorder/README.md)

* [create_ads_insertionorder2](docs/sdks/insertionorder/README.md#create_ads_insertionorder2) - Create an insertionorder
* [get_ads_insertionorder2](docs/sdks/insertionorder/README.md#get_ads_insertionorder2) - Retrieve an insertionorder
* [list_ads_insertionorders2](docs/sdks/insertionorder/README.md#list_ads_insertionorders2) - List all insertionorders
* [patch_ads_insertionorder2](docs/sdks/insertionorder/README.md#patch_ads_insertionorder2) - Update an insertionorder
* [remove_ads_insertionorder2](docs/sdks/insertionorder/README.md#remove_ads_insertionorder2) - Remove an insertionorder
* [update_ads_insertionorder2](docs/sdks/insertionorder/README.md#update_ads_insertionorder2) - Update an insertionorder

### [Instructor](docs/sdks/instructor/README.md)

* [create_lms_instructor2](docs/sdks/instructor/README.md#create_lms_instructor2) - Create an instructor
* [get_lms_instructor2](docs/sdks/instructor/README.md#get_lms_instructor2) - Retrieve an instructor
* [list_lms_instructors2](docs/sdks/instructor/README.md#list_lms_instructors2) - List all instructors
* [patch_lms_instructor2](docs/sdks/instructor/README.md#patch_lms_instructor2) - Update an instructor
* [remove_lms_instructor2](docs/sdks/instructor/README.md#remove_lms_instructor2) - Remove an instructor
* [update_lms_instructor2](docs/sdks/instructor/README.md#update_lms_instructor2) - Update an instructor

### [Integration](docs/sdks/integration/README.md)

* [get_unified_integration_auth](docs/sdks/integration/README.md#get_unified_integration_auth) - Authorize new connection
* [list_unified_integration_workspaces](docs/sdks/integration/README.md#list_unified_integration_workspaces) - Returns all activated integrations in a workspace
* [list_unified_integrations](docs/sdks/integration/README.md#list_unified_integrations) - Returns all integrations

### [Interview](docs/sdks/interview/README.md)

* [create_ats_interview2](docs/sdks/interview/README.md#create_ats_interview2) - Create an interview
* [get_ats_interview2](docs/sdks/interview/README.md#get_ats_interview2) - Retrieve an interview
* [list_ats_interviews2](docs/sdks/interview/README.md#list_ats_interviews2) - List all interviews
* [patch_ats_interview2](docs/sdks/interview/README.md#patch_ats_interview2) - Update an interview
* [remove_ats_interview2](docs/sdks/interview/README.md#remove_ats_interview2) - Remove an interview
* [update_ats_interview2](docs/sdks/interview/README.md#update_ats_interview2) - Update an interview

### [Inventory](docs/sdks/inventory/README.md)

* [create_commerce_inventory2](docs/sdks/inventory/README.md#create_commerce_inventory2) - Create an inventory
* [get_commerce_inventory2](docs/sdks/inventory/README.md#get_commerce_inventory2) - Retrieve an inventory
* [list_commerce_inventories2](docs/sdks/inventory/README.md#list_commerce_inventories2) - List all inventories
* [patch_commerce_inventory2](docs/sdks/inventory/README.md#patch_commerce_inventory2) - Update an inventory
* [remove_commerce_inventory2](docs/sdks/inventory/README.md#remove_commerce_inventory2) - Remove an inventory
* [update_commerce_inventory2](docs/sdks/inventory/README.md#update_commerce_inventory2) - Update an inventory

### [Invoice](docs/sdks/invoice/README.md)

* [create_accounting_invoice2](docs/sdks/invoice/README.md#create_accounting_invoice2) - Create an invoice
* [get_accounting_invoice2](docs/sdks/invoice/README.md#get_accounting_invoice2) - Retrieve an invoice
* [list_accounting_invoices2](docs/sdks/invoice/README.md#list_accounting_invoices2) - List all invoices
* [patch_accounting_invoice2](docs/sdks/invoice/README.md#patch_accounting_invoice2) - Update an invoice
* [remove_accounting_invoice2](docs/sdks/invoice/README.md#remove_accounting_invoice2) - Remove an invoice
* [update_accounting_invoice2](docs/sdks/invoice/README.md#update_accounting_invoice2) - Update an invoice

### [Issue](docs/sdks/issue/README.md)

* [get_unified_issue](docs/sdks/issue/README.md#get_unified_issue) - Retrieve support issue
* [list_unified_issues](docs/sdks/issue/README.md#list_unified_issues) - List support issues

### [Item](docs/sdks/item/README.md)

* [create_commerce_item2](docs/sdks/item/README.md#create_commerce_item2) - Create an item
* [get_commerce_item2](docs/sdks/item/README.md#get_commerce_item2) - Retrieve an item
* [list_commerce_items2](docs/sdks/item/README.md#list_commerce_items2) - List all items
* [patch_commerce_item2](docs/sdks/item/README.md#patch_commerce_item2) - Update an item
* [remove_commerce_item2](docs/sdks/item/README.md#remove_commerce_item2) - Remove an item
* [update_commerce_item2](docs/sdks/item/README.md#update_commerce_item2) - Update an item

### [Itemvariant](docs/sdks/itemvariant/README.md)

* [create_commerce_itemvariant2](docs/sdks/itemvariant/README.md#create_commerce_itemvariant2) - Create an itemvariant
* [get_commerce_itemvariant2](docs/sdks/itemvariant/README.md#get_commerce_itemvariant2) - Retrieve an itemvariant
* [list_commerce_itemvariants2](docs/sdks/itemvariant/README.md#list_commerce_itemvariants2) - List all itemvariants
* [patch_commerce_itemvariant2](docs/sdks/itemvariant/README.md#patch_commerce_itemvariant2) - Update an itemvariant
* [remove_commerce_itemvariant2](docs/sdks/itemvariant/README.md#remove_commerce_itemvariant2) - Remove an itemvariant
* [update_commerce_itemvariant2](docs/sdks/itemvariant/README.md#update_commerce_itemvariant2) - Update an itemvariant

### [Job](docs/sdks/job/README.md)

* [create_ats_job2](docs/sdks/job/README.md#create_ats_job2) - Create a job
* [get_ats_job2](docs/sdks/job/README.md#get_ats_job2) - Retrieve a job
* [list_ats_jobs2](docs/sdks/job/README.md#list_ats_jobs2) - List all jobs
* [patch_ats_job2](docs/sdks/job/README.md#patch_ats_job2) - Update a job
* [remove_ats_job2](docs/sdks/job/README.md#remove_ats_job2) - Remove a job
* [update_ats_job2](docs/sdks/job/README.md#update_ats_job2) - Update a job

### [Journal](docs/sdks/journal/README.md)

* [create_accounting_journal2](docs/sdks/journal/README.md#create_accounting_journal2) - Create a journal
* [get_accounting_journal2](docs/sdks/journal/README.md#get_accounting_journal2) - Retrieve a journal
* [list_accounting_journals2](docs/sdks/journal/README.md#list_accounting_journals2) - List all journals
* [patch_accounting_journal2](docs/sdks/journal/README.md#patch_accounting_journal2) - Update a journal
* [remove_accounting_journal2](docs/sdks/journal/README.md#remove_accounting_journal2) - Remove a journal
* [update_accounting_journal2](docs/sdks/journal/README.md#update_accounting_journal2) - Update a journal

### [Kms](docs/sdks/kms/README.md)

* [create_kms_comment2](docs/sdks/kms/README.md#create_kms_comment2) - Create a comment
* [create_kms_page2](docs/sdks/kms/README.md#create_kms_page2) - Create a page
* [create_kms_space2](docs/sdks/kms/README.md#create_kms_space2) - Create a space
* [get_kms_comment2](docs/sdks/kms/README.md#get_kms_comment2) - Retrieve a comment
* [get_kms_page2](docs/sdks/kms/README.md#get_kms_page2) - Retrieve a page
* [get_kms_space2](docs/sdks/kms/README.md#get_kms_space2) - Retrieve a space
* [list_kms_comments2](docs/sdks/kms/README.md#list_kms_comments2) - List all comments
* [list_kms_pages2](docs/sdks/kms/README.md#list_kms_pages2) - List all pages
* [list_kms_spaces2](docs/sdks/kms/README.md#list_kms_spaces2) - List all spaces
* [patch_kms_comment2](docs/sdks/kms/README.md#patch_kms_comment2) - Update a comment
* [patch_kms_page2](docs/sdks/kms/README.md#patch_kms_page2) - Update a page
* [patch_kms_space2](docs/sdks/kms/README.md#patch_kms_space2) - Update a space
* [remove_kms_comment2](docs/sdks/kms/README.md#remove_kms_comment2) - Remove a comment
* [remove_kms_page2](docs/sdks/kms/README.md#remove_kms_page2) - Remove a page
* [remove_kms_space2](docs/sdks/kms/README.md#remove_kms_space2) - Remove a space
* [update_kms_comment2](docs/sdks/kms/README.md#update_kms_comment2) - Update a comment
* [update_kms_page2](docs/sdks/kms/README.md#update_kms_page2) - Update a page
* [update_kms_space2](docs/sdks/kms/README.md#update_kms_space2) - Update a space

### [Label](docs/sdks/label/README.md)

* [create_shipping_label2](docs/sdks/label/README.md#create_shipping_label2) - Create a label
* [get_shipping_label2](docs/sdks/label/README.md#get_shipping_label2) - Retrieve a label
* [list_shipping_labels2](docs/sdks/label/README.md#list_shipping_labels2) - List all labels
* [patch_shipping_label2](docs/sdks/label/README.md#patch_shipping_label2) - Update a label
* [remove_shipping_label2](docs/sdks/label/README.md#remove_shipping_label2) - Remove a label
* [update_shipping_label2](docs/sdks/label/README.md#update_shipping_label2) - Update a label

### [Lead](docs/sdks/lead/README.md)

* [create_crm_lead2](docs/sdks/lead/README.md#create_crm_lead2) - Create a lead
* [get_crm_lead2](docs/sdks/lead/README.md#get_crm_lead2) - Retrieve a lead
* [list_crm_leads2](docs/sdks/lead/README.md#list_crm_leads2) - List all leads
* [patch_crm_lead2](docs/sdks/lead/README.md#patch_crm_lead2) - Update a lead
* [remove_crm_lead2](docs/sdks/lead/README.md#remove_crm_lead2) - Remove a lead
* [update_crm_lead2](docs/sdks/lead/README.md#update_crm_lead2) - Update a lead

### [Link](docs/sdks/link/README.md)

* [create_calendar_link2](docs/sdks/link/README.md#create_calendar_link2) - Create a link
* [create_payment_link2](docs/sdks/link/README.md#create_payment_link2) - Create a link
* [get_calendar_link2](docs/sdks/link/README.md#get_calendar_link2) - Retrieve a link
* [get_payment_link2](docs/sdks/link/README.md#get_payment_link2) - Retrieve a link
* [list_calendar_links2](docs/sdks/link/README.md#list_calendar_links2) - List all links
* [list_payment_links2](docs/sdks/link/README.md#list_payment_links2) - List all links
* [patch_calendar_link2](docs/sdks/link/README.md#patch_calendar_link2) - Update a link
* [patch_payment_link2](docs/sdks/link/README.md#patch_payment_link2) - Update a link
* [remove_calendar_link2](docs/sdks/link/README.md#remove_calendar_link2) - Remove a link
* [remove_payment_link2](docs/sdks/link/README.md#remove_payment_link2) - Remove a link
* [update_calendar_link2](docs/sdks/link/README.md#update_calendar_link2) - Update a link
* [update_payment_link2](docs/sdks/link/README.md#update_payment_link2) - Update a link

### [List](docs/sdks/list/README.md)

* [create_martech_list2](docs/sdks/list/README.md#create_martech_list2) - Create a list
* [get_martech_list2](docs/sdks/list/README.md#get_martech_list2) - Retrieve a list
* [list_martech_lists2](docs/sdks/list/README.md#list_martech_lists2) - List all lists
* [patch_martech_list2](docs/sdks/list/README.md#patch_martech_list2) - Update a list
* [remove_martech_list2](docs/sdks/list/README.md#remove_martech_list2) - Remove a list
* [update_martech_list2](docs/sdks/list/README.md#update_martech_list2) - Update a list

### [Lms](docs/sdks/lms/README.md)

* [create_lms_activity2](docs/sdks/lms/README.md#create_lms_activity2) - Create an activity
* [create_lms_class2](docs/sdks/lms/README.md#create_lms_class2) - Create a class
* [create_lms_collection2](docs/sdks/lms/README.md#create_lms_collection2) - Create a collection
* [create_lms_content2](docs/sdks/lms/README.md#create_lms_content2) - Create a content
* [create_lms_course2](docs/sdks/lms/README.md#create_lms_course2) - Create a course
* [create_lms_instructor2](docs/sdks/lms/README.md#create_lms_instructor2) - Create an instructor
* [create_lms_student2](docs/sdks/lms/README.md#create_lms_student2) - Create a student
* [get_lms_activity2](docs/sdks/lms/README.md#get_lms_activity2) - Retrieve an activity
* [get_lms_class2](docs/sdks/lms/README.md#get_lms_class2) - Retrieve a class
* [get_lms_collection2](docs/sdks/lms/README.md#get_lms_collection2) - Retrieve a collection
* [get_lms_content2](docs/sdks/lms/README.md#get_lms_content2) - Retrieve a content
* [get_lms_course2](docs/sdks/lms/README.md#get_lms_course2) - Retrieve a course
* [get_lms_instructor2](docs/sdks/lms/README.md#get_lms_instructor2) - Retrieve an instructor
* [get_lms_student2](docs/sdks/lms/README.md#get_lms_student2) - Retrieve a student
* [list_lms_activities2](docs/sdks/lms/README.md#list_lms_activities2) - List all activities
* [list_lms_classes2](docs/sdks/lms/README.md#list_lms_classes2) - List all classes
* [list_lms_collections2](docs/sdks/lms/README.md#list_lms_collections2) - List all collections
* [list_lms_contents2](docs/sdks/lms/README.md#list_lms_contents2) - List all contents
* [list_lms_courses2](docs/sdks/lms/README.md#list_lms_courses2) - List all courses
* [list_lms_instructors2](docs/sdks/lms/README.md#list_lms_instructors2) - List all instructors
* [list_lms_students2](docs/sdks/lms/README.md#list_lms_students2) - List all students
* [patch_lms_activity2](docs/sdks/lms/README.md#patch_lms_activity2) - Update an activity
* [patch_lms_class2](docs/sdks/lms/README.md#patch_lms_class2) - Update a class
* [patch_lms_collection2](docs/sdks/lms/README.md#patch_lms_collection2) - Update a collection
* [patch_lms_content2](docs/sdks/lms/README.md#patch_lms_content2) - Update a content
* [patch_lms_course2](docs/sdks/lms/README.md#patch_lms_course2) - Update a course
* [patch_lms_instructor2](docs/sdks/lms/README.md#patch_lms_instructor2) - Update an instructor
* [patch_lms_student2](docs/sdks/lms/README.md#patch_lms_student2) - Update a student
* [remove_lms_activity2](docs/sdks/lms/README.md#remove_lms_activity2) - Remove an activity
* [remove_lms_class2](docs/sdks/lms/README.md#remove_lms_class2) - Remove a class
* [remove_lms_collection2](docs/sdks/lms/README.md#remove_lms_collection2) - Remove a collection
* [remove_lms_content2](docs/sdks/lms/README.md#remove_lms_content2) - Remove a content
* [remove_lms_course2](docs/sdks/lms/README.md#remove_lms_course2) - Remove a course
* [remove_lms_instructor2](docs/sdks/lms/README.md#remove_lms_instructor2) - Remove an instructor
* [remove_lms_student2](docs/sdks/lms/README.md#remove_lms_student2) - Remove a student
* [update_lms_activity2](docs/sdks/lms/README.md#update_lms_activity2) - Update an activity
* [update_lms_class2](docs/sdks/lms/README.md#update_lms_class2) - Update a class
* [update_lms_collection2](docs/sdks/lms/README.md#update_lms_collection2) - Update a collection
* [update_lms_content2](docs/sdks/lms/README.md#update_lms_content2) - Update a content
* [update_lms_course2](docs/sdks/lms/README.md#update_lms_course2) - Update a course
* [update_lms_instructor2](docs/sdks/lms/README.md#update_lms_instructor2) - Update an instructor
* [update_lms_student2](docs/sdks/lms/README.md#update_lms_student2) - Update a student

### [Location](docs/sdks/location/README.md)

* [create_commerce_location2](docs/sdks/location/README.md#create_commerce_location2) - Create a location
* [create_hris_location2](docs/sdks/location/README.md#create_hris_location2) - Create a location
* [get_clubs_location2](docs/sdks/location/README.md#get_clubs_location2) - Retrieve a location
* [get_commerce_location2](docs/sdks/location/README.md#get_commerce_location2) - Retrieve a location
* [get_hris_location2](docs/sdks/location/README.md#get_hris_location2) - Retrieve a location
* [list_clubs_locations2](docs/sdks/location/README.md#list_clubs_locations2) - List all locations
* [list_commerce_locations2](docs/sdks/location/README.md#list_commerce_locations2) - List all locations
* [list_hris_locations2](docs/sdks/location/README.md#list_hris_locations2) - List all locations
* [patch_commerce_location2](docs/sdks/location/README.md#patch_commerce_location2) - Update a location
* [patch_hris_location2](docs/sdks/location/README.md#patch_hris_location2) - Update a location
* [remove_commerce_location2](docs/sdks/location/README.md#remove_commerce_location2) - Remove a location
* [remove_hris_location2](docs/sdks/location/README.md#remove_hris_location2) - Remove a location
* [update_commerce_location2](docs/sdks/location/README.md#update_commerce_location2) - Update a location
* [update_hris_location2](docs/sdks/location/README.md#update_hris_location2) - Update a location

### [Login](docs/sdks/login/README.md)

* [get_unified_integration_login](docs/sdks/login/README.md#get_unified_integration_login) - Sign in a user

### [Martech](docs/sdks/martech/README.md)

* [create_martech_campaign2](docs/sdks/martech/README.md#create_martech_campaign2) - Create a campaign
* [create_martech_list2](docs/sdks/martech/README.md#create_martech_list2) - Create a list
* [create_martech_member2](docs/sdks/martech/README.md#create_martech_member2) - Create a member
* [get_martech_campaign2](docs/sdks/martech/README.md#get_martech_campaign2) - Retrieve a campaign
* [get_martech_list2](docs/sdks/martech/README.md#get_martech_list2) - Retrieve a list
* [get_martech_member2](docs/sdks/martech/README.md#get_martech_member2) - Retrieve a member
* [list_martech_campaigns2](docs/sdks/martech/README.md#list_martech_campaigns2) - List all campaigns
* [list_martech_lists2](docs/sdks/martech/README.md#list_martech_lists2) - List all lists
* [list_martech_members2](docs/sdks/martech/README.md#list_martech_members2) - List all members
* [list_martech_reports2](docs/sdks/martech/README.md#list_martech_reports2) - List all reports
* [patch_martech_campaign2](docs/sdks/martech/README.md#patch_martech_campaign2) - Update a campaign
* [patch_martech_list2](docs/sdks/martech/README.md#patch_martech_list2) - Update a list
* [patch_martech_member2](docs/sdks/martech/README.md#patch_martech_member2) - Update a member
* [remove_martech_campaign2](docs/sdks/martech/README.md#remove_martech_campaign2) - Remove a campaign
* [remove_martech_list2](docs/sdks/martech/README.md#remove_martech_list2) - Remove a list
* [remove_martech_member2](docs/sdks/martech/README.md#remove_martech_member2) - Remove a member
* [update_martech_campaign2](docs/sdks/martech/README.md#update_martech_campaign2) - Update a campaign
* [update_martech_list2](docs/sdks/martech/README.md#update_martech_list2) - Update a list
* [update_martech_member2](docs/sdks/martech/README.md#update_martech_member2) - Update a member

### [Member](docs/sdks/member/README.md)

* [create_martech_member2](docs/sdks/member/README.md#create_martech_member2) - Create a member
* [get_clubs_member2](docs/sdks/member/README.md#get_clubs_member2) - Retrieve a member
* [get_martech_member2](docs/sdks/member/README.md#get_martech_member2) - Retrieve a member
* [list_clubs_members2](docs/sdks/member/README.md#list_clubs_members2) - List all members
* [list_martech_members2](docs/sdks/member/README.md#list_martech_members2) - List all members
* [patch_martech_member2](docs/sdks/member/README.md#patch_martech_member2) - Update a member
* [remove_martech_member2](docs/sdks/member/README.md#remove_martech_member2) - Remove a member
* [update_martech_member2](docs/sdks/member/README.md#update_martech_member2) - Update a member

### [Message](docs/sdks/message/README.md)

* [create_messaging_message2](docs/sdks/message/README.md#create_messaging_message2) - Create a message
* [get_messaging_message2](docs/sdks/message/README.md#get_messaging_message2) - Retrieve a message
* [list_messaging_messages2](docs/sdks/message/README.md#list_messaging_messages2) - List all messages
* [patch_messaging_message2](docs/sdks/message/README.md#patch_messaging_message2) - Update a message
* [remove_messaging_message2](docs/sdks/message/README.md#remove_messaging_message2) - Remove a message
* [update_messaging_message2](docs/sdks/message/README.md#update_messaging_message2) - Update a message

### [Messaging](docs/sdks/messaging/README.md)

* [create_messaging_message2](docs/sdks/messaging/README.md#create_messaging_message2) - Create a message
* [get_messaging_channel2](docs/sdks/messaging/README.md#get_messaging_channel2) - Retrieve a channel
* [get_messaging_message2](docs/sdks/messaging/README.md#get_messaging_message2) - Retrieve a message
* [list_messaging_channels2](docs/sdks/messaging/README.md#list_messaging_channels2) - List all channels
* [list_messaging_messages2](docs/sdks/messaging/README.md#list_messaging_messages2) - List all messages
* [patch_messaging_event2](docs/sdks/messaging/README.md#patch_messaging_event2) - Update an event
* [patch_messaging_message2](docs/sdks/messaging/README.md#patch_messaging_message2) - Update a message
* [remove_messaging_message2](docs/sdks/messaging/README.md#remove_messaging_message2) - Remove a message
* [update_messaging_event2](docs/sdks/messaging/README.md#update_messaging_event2) - Update an event
* [update_messaging_message2](docs/sdks/messaging/README.md#update_messaging_message2) - Update a message

### [Metadata](docs/sdks/metadata/README.md)

* [create_metadata_metadata2](docs/sdks/metadata/README.md#create_metadata_metadata2) - Create a metadata
* [get_metadata_metadata2](docs/sdks/metadata/README.md#get_metadata_metadata2) - Retrieve a metadata
* [list_metadata_metadatas2](docs/sdks/metadata/README.md#list_metadata_metadatas2) - List all metadatas
* [patch_metadata_metadata2](docs/sdks/metadata/README.md#patch_metadata_metadata2) - Update a metadata
* [remove_metadata_metadata2](docs/sdks/metadata/README.md#remove_metadata_metadata2) - Remove a metadata
* [update_metadata_metadata2](docs/sdks/metadata/README.md#update_metadata_metadata2) - Update a metadata

### [Model](docs/sdks/model/README.md)

* [get_genai_model2](docs/sdks/model/README.md#get_genai_model2) - Retrieve a model
* [list_genai_models2](docs/sdks/model/README.md#list_genai_models2) - List all models

### [Note](docs/sdks/note/README.md)

* [create_ticketing_note2](docs/sdks/note/README.md#create_ticketing_note2) - Create a note
* [get_ticketing_note2](docs/sdks/note/README.md#get_ticketing_note2) - Retrieve a note
* [list_ticketing_notes2](docs/sdks/note/README.md#list_ticketing_notes2) - List all notes
* [patch_ticketing_note2](docs/sdks/note/README.md#patch_ticketing_note2) - Update a note
* [remove_ticketing_note2](docs/sdks/note/README.md#remove_ticketing_note2) - Remove a note
* [update_ticketing_note2](docs/sdks/note/README.md#update_ticketing_note2) - Update a note

### [Order](docs/sdks/order/README.md)

* [create_accounting_order2](docs/sdks/order/README.md#create_accounting_order2) - Create an order
* [get_accounting_order2](docs/sdks/order/README.md#get_accounting_order2) - Retrieve an order
* [list_accounting_orders2](docs/sdks/order/README.md#list_accounting_orders2) - List all orders
* [patch_accounting_order2](docs/sdks/order/README.md#patch_accounting_order2) - Update an order
* [patch_assessment_order2](docs/sdks/order/README.md#patch_assessment_order2) - Update an order
* [remove_accounting_order2](docs/sdks/order/README.md#remove_accounting_order2) - Remove an order
* [update_accounting_order2](docs/sdks/order/README.md#update_accounting_order2) - Update an order
* [update_assessment_order2](docs/sdks/order/README.md#update_assessment_order2) - Update an order

### [Organization](docs/sdks/organization/README.md)

* [create_ads_organization2](docs/sdks/organization/README.md#create_ads_organization2) - Create an organization
* [create_repo_organization2](docs/sdks/organization/README.md#create_repo_organization2) - Create an organization
* [get_accounting_organization2](docs/sdks/organization/README.md#get_accounting_organization2) - Retrieve an organization
* [get_ads_organization2](docs/sdks/organization/README.md#get_ads_organization2) - Retrieve an organization
* [get_repo_organization2](docs/sdks/organization/README.md#get_repo_organization2) - Retrieve an organization
* [list_accounting_organizations2](docs/sdks/organization/README.md#list_accounting_organizations2) - List all organizations
* [list_ads_organizations2](docs/sdks/organization/README.md#list_ads_organizations2) - List all organizations
* [list_repo_organizations2](docs/sdks/organization/README.md#list_repo_organizations2) - List all organizations
* [patch_ads_organization2](docs/sdks/organization/README.md#patch_ads_organization2) - Update an organization
* [patch_repo_organization2](docs/sdks/organization/README.md#patch_repo_organization2) - Update an organization
* [remove_ads_organization2](docs/sdks/organization/README.md#remove_ads_organization2) - Remove an organization
* [remove_repo_organization2](docs/sdks/organization/README.md#remove_repo_organization2) - Remove an organization
* [update_ads_organization2](docs/sdks/organization/README.md#update_ads_organization2) - Update an organization
* [update_repo_organization2](docs/sdks/organization/README.md#update_repo_organization2) - Update an organization

### [Package](docs/sdks/package/README.md)

* [create_assessment_package2](docs/sdks/package/README.md#create_assessment_package2) - Create an assessment package
* [get_assessment_package2](docs/sdks/package/README.md#get_assessment_package2) - Get an assessment package
* [get_verification_package2](docs/sdks/package/README.md#get_verification_package2) - Retrieve a package
* [list_assessment_packages2](docs/sdks/package/README.md#list_assessment_packages2) - List assessment packages
* [list_verification_packages2](docs/sdks/package/README.md#list_verification_packages2) - List all packages
* [patch_assessment_package2](docs/sdks/package/README.md#patch_assessment_package2) - Update an assessment package
* [remove_assessment_package2](docs/sdks/package/README.md#remove_assessment_package2) - Delete an assessment package
* [update_assessment_package2](docs/sdks/package/README.md#update_assessment_package2) - Update an assessment package

### [Page](docs/sdks/page/README.md)

* [create_kms_page2](docs/sdks/page/README.md#create_kms_page2) - Create a page
* [get_kms_page2](docs/sdks/page/README.md#get_kms_page2) - Retrieve a page
* [list_kms_pages2](docs/sdks/page/README.md#list_kms_pages2) - List all pages
* [patch_kms_page2](docs/sdks/page/README.md#patch_kms_page2) - Update a page
* [remove_kms_page2](docs/sdks/page/README.md#remove_kms_page2) - Remove a page
* [update_kms_page2](docs/sdks/page/README.md#update_kms_page2) - Update a page

### [Passthrough](docs/sdks/passthrough/README.md)

* [create_passthrough2_json](docs/sdks/passthrough/README.md#create_passthrough2_json) - Passthrough POST
* [create_passthrough2_raw](docs/sdks/passthrough/README.md#create_passthrough2_raw) - Passthrough POST
* [list_passthroughs2](docs/sdks/passthrough/README.md#list_passthroughs2) - Passthrough GET
* [patch_passthrough2_json](docs/sdks/passthrough/README.md#patch_passthrough2_json) - Passthrough PUT
* [patch_passthrough2_raw](docs/sdks/passthrough/README.md#patch_passthrough2_raw) - Passthrough PUT
* [remove_passthrough2](docs/sdks/passthrough/README.md#remove_passthrough2) - Passthrough DELETE
* [update_passthrough2_json](docs/sdks/passthrough/README.md#update_passthrough2_json) - Passthrough PUT
* [update_passthrough2_raw](docs/sdks/passthrough/README.md#update_passthrough2_raw) - Passthrough PUT

### [Payment](docs/sdks/payment/README.md)

* [create_payment_link2](docs/sdks/payment/README.md#create_payment_link2) - Create a link
* [create_payment_payment2](docs/sdks/payment/README.md#create_payment_payment2) - Create a payment
* [create_payment_subscription2](docs/sdks/payment/README.md#create_payment_subscription2) - Create a subscription
* [get_payment_link2](docs/sdks/payment/README.md#get_payment_link2) - Retrieve a link
* [get_payment_payment2](docs/sdks/payment/README.md#get_payment_payment2) - Retrieve a payment
* [get_payment_payout2](docs/sdks/payment/README.md#get_payment_payout2) - Retrieve a payout
* [get_payment_refund2](docs/sdks/payment/README.md#get_payment_refund2) - Retrieve a refund
* [get_payment_subscription2](docs/sdks/payment/README.md#get_payment_subscription2) - Retrieve a subscription
* [list_payment_links2](docs/sdks/payment/README.md#list_payment_links2) - List all links
* [list_payment_payments2](docs/sdks/payment/README.md#list_payment_payments2) - List all payments
* [list_payment_payouts2](docs/sdks/payment/README.md#list_payment_payouts2) - List all payouts
* [list_payment_refunds2](docs/sdks/payment/README.md#list_payment_refunds2) - List all refunds
* [list_payment_subscriptions2](docs/sdks/payment/README.md#list_payment_subscriptions2) - List all subscriptions
* [patch_payment_link2](docs/sdks/payment/README.md#patch_payment_link2) - Update a link
* [patch_payment_payment2](docs/sdks/payment/README.md#patch_payment_payment2) - Update a payment
* [patch_payment_subscription2](docs/sdks/payment/README.md#patch_payment_subscription2) - Update a subscription
* [remove_payment_link2](docs/sdks/payment/README.md#remove_payment_link2) - Remove a link
* [remove_payment_payment2](docs/sdks/payment/README.md#remove_payment_payment2) - Remove a payment
* [remove_payment_subscription2](docs/sdks/payment/README.md#remove_payment_subscription2) - Remove a subscription
* [update_payment_link2](docs/sdks/payment/README.md#update_payment_link2) - Update a link
* [update_payment_payment2](docs/sdks/payment/README.md#update_payment_payment2) - Update a payment
* [update_payment_subscription2](docs/sdks/payment/README.md#update_payment_subscription2) - Update a subscription

### [Payout](docs/sdks/payout/README.md)

* [get_payment_payout2](docs/sdks/payout/README.md#get_payment_payout2) - Retrieve a payout
* [list_payment_payouts2](docs/sdks/payout/README.md#list_payment_payouts2) - List all payouts

### [Payslip](docs/sdks/payslip/README.md)

* [get_hris_payslip2](docs/sdks/payslip/README.md#get_hris_payslip2) - Retrieve a payslip
* [list_hris_payslips2](docs/sdks/payslip/README.md#list_hris_payslips2) - List all payslips

### [Person](docs/sdks/person/README.md)

* [list_enrich_people2](docs/sdks/person/README.md#list_enrich_people2) - Retrieve enrichment information for a person

### [Pipeline](docs/sdks/pipeline/README.md)

* [create_crm_pipeline2](docs/sdks/pipeline/README.md#create_crm_pipeline2) - Create a pipeline
* [get_crm_pipeline2](docs/sdks/pipeline/README.md#get_crm_pipeline2) - Retrieve a pipeline
* [list_crm_pipelines2](docs/sdks/pipeline/README.md#list_crm_pipelines2) - List all pipelines
* [patch_crm_pipeline2](docs/sdks/pipeline/README.md#patch_crm_pipeline2) - Update a pipeline
* [remove_crm_pipeline2](docs/sdks/pipeline/README.md#remove_crm_pipeline2) - Remove a pipeline
* [update_crm_pipeline2](docs/sdks/pipeline/README.md#update_crm_pipeline2) - Update a pipeline

### [Profitloss](docs/sdks/profitloss/README.md)

* [get_accounting_profitloss2](docs/sdks/profitloss/README.md#get_accounting_profitloss2) - Retrieve a profitloss
* [list_accounting_profitlosses2](docs/sdks/profitloss/README.md#list_accounting_profitlosses2) - List all profitlosses

### [Project](docs/sdks/project/README.md)

* [create_task_project2](docs/sdks/project/README.md#create_task_project2) - Create a project
* [get_task_project2](docs/sdks/project/README.md#get_task_project2) - Retrieve a project
* [list_task_projects2](docs/sdks/project/README.md#list_task_projects2) - List all projects
* [patch_task_project2](docs/sdks/project/README.md#patch_task_project2) - Update a project
* [remove_task_project2](docs/sdks/project/README.md#remove_task_project2) - Remove a project
* [update_task_project2](docs/sdks/project/README.md#update_task_project2) - Update a project

### [Promoted](docs/sdks/promoted/README.md)

* [get_ads_promoted2](docs/sdks/promoted/README.md#get_ads_promoted2) - Retrieve a promoted
* [list_ads_promoteds2](docs/sdks/promoted/README.md#list_ads_promoteds2) - List all promoteds

### [Prompt](docs/sdks/prompt/README.md)

* [create_genai_prompt2](docs/sdks/prompt/README.md#create_genai_prompt2) - Create a prompt

### [Property](docs/sdks/property/README.md)

* [create_analytics_property2](docs/sdks/property/README.md#create_analytics_property2) - Create a property
* [get_analytics_property2](docs/sdks/property/README.md#get_analytics_property2) - Retrieve a property
* [list_analytics_properties2](docs/sdks/property/README.md#list_analytics_properties2) - List all properties
* [patch_analytics_property2](docs/sdks/property/README.md#patch_analytics_property2) - Update a property
* [remove_analytics_property2](docs/sdks/property/README.md#remove_analytics_property2) - Remove a property
* [update_analytics_property2](docs/sdks/property/README.md#update_analytics_property2) - Update a property

### [Pullrequest](docs/sdks/pullrequest/README.md)

* [create_repo_pullrequest2](docs/sdks/pullrequest/README.md#create_repo_pullrequest2) - Create a pullrequest
* [get_repo_pullrequest2](docs/sdks/pullrequest/README.md#get_repo_pullrequest2) - Retrieve a pullrequest
* [list_repo_pullrequests2](docs/sdks/pullrequest/README.md#list_repo_pullrequests2) - List all pullrequests
* [patch_repo_pullrequest2](docs/sdks/pullrequest/README.md#patch_repo_pullrequest2) - Update a pullrequest
* [remove_repo_pullrequest2](docs/sdks/pullrequest/README.md#remove_repo_pullrequest2) - Remove a pullrequest
* [update_repo_pullrequest2](docs/sdks/pullrequest/README.md#update_repo_pullrequest2) - Update a pullrequest

### [Purchaseorder](docs/sdks/purchaseorder/README.md)

* [create_accounting_purchaseorder2](docs/sdks/purchaseorder/README.md#create_accounting_purchaseorder2) - Create a purchaseorder
* [get_accounting_purchaseorder2](docs/sdks/purchaseorder/README.md#get_accounting_purchaseorder2) - Retrieve a purchaseorder
* [list_accounting_purchaseorders2](docs/sdks/purchaseorder/README.md#list_accounting_purchaseorders2) - List all purchaseorders
* [patch_accounting_purchaseorder2](docs/sdks/purchaseorder/README.md#patch_accounting_purchaseorder2) - Update a purchaseorder
* [remove_accounting_purchaseorder2](docs/sdks/purchaseorder/README.md#remove_accounting_purchaseorder2) - Remove a purchaseorder
* [update_accounting_purchaseorder2](docs/sdks/purchaseorder/README.md#update_accounting_purchaseorder2) - Update a purchaseorder

### [Query](docs/sdks/query/README.md)

* [create_datastore_query2](docs/sdks/query/README.md#create_datastore_query2) - Create a query

### [Rate](docs/sdks/rate/README.md)

* [create_shipping_rate2](docs/sdks/rate/README.md#create_shipping_rate2) - Create a rate

### [Record](docs/sdks/record/README.md)

* [create_datastore_record2](docs/sdks/record/README.md#create_datastore_record2) - Create a record
* [get_datastore_record2](docs/sdks/record/README.md#get_datastore_record2) - Retrieve a record
* [list_datastore_records2](docs/sdks/record/README.md#list_datastore_records2) - List all records
* [patch_datastore_record2](docs/sdks/record/README.md#patch_datastore_record2) - Update a record
* [remove_datastore_record2](docs/sdks/record/README.md#remove_datastore_record2) - Remove a record
* [update_datastore_record2](docs/sdks/record/README.md#update_datastore_record2) - Update a record

### [Recording](docs/sdks/recording/README.md)

* [create_uc_recording2](docs/sdks/recording/README.md#create_uc_recording2) - Create a recording
* [get_calendar_recording2](docs/sdks/recording/README.md#get_calendar_recording2) - Retrieve a recording
* [get_uc_recording2](docs/sdks/recording/README.md#get_uc_recording2) - Retrieve a recording
* [list_calendar_recordings2](docs/sdks/recording/README.md#list_calendar_recordings2) - List all recordings
* [list_uc_recordings2](docs/sdks/recording/README.md#list_uc_recordings2) - List all recordings
* [patch_uc_recording2](docs/sdks/recording/README.md#patch_uc_recording2) - Update a recording
* [remove_uc_recording2](docs/sdks/recording/README.md#remove_uc_recording2) - Remove a recording
* [update_uc_recording2](docs/sdks/recording/README.md#update_uc_recording2) - Update a recording

### [Refund](docs/sdks/refund/README.md)

* [get_payment_refund2](docs/sdks/refund/README.md#get_payment_refund2) - Retrieve a refund
* [list_payment_refunds2](docs/sdks/refund/README.md#list_payment_refunds2) - List all refunds

### [Repo](docs/sdks/repo/README.md)

* [create_repo_branch2](docs/sdks/repo/README.md#create_repo_branch2) - Create a branch
* [create_repo_commit2](docs/sdks/repo/README.md#create_repo_commit2) - Create a commit
* [create_repo_organization2](docs/sdks/repo/README.md#create_repo_organization2) - Create an organization
* [create_repo_pullrequest2](docs/sdks/repo/README.md#create_repo_pullrequest2) - Create a pullrequest
* [create_repo_repository2](docs/sdks/repo/README.md#create_repo_repository2) - Create a repository
* [get_repo_branch2](docs/sdks/repo/README.md#get_repo_branch2) - Retrieve a branch
* [get_repo_commit2](docs/sdks/repo/README.md#get_repo_commit2) - Retrieve a commit
* [get_repo_organization2](docs/sdks/repo/README.md#get_repo_organization2) - Retrieve an organization
* [get_repo_pullrequest2](docs/sdks/repo/README.md#get_repo_pullrequest2) - Retrieve a pullrequest
* [get_repo_repository2](docs/sdks/repo/README.md#get_repo_repository2) - Retrieve a repository
* [list_repo_branches2](docs/sdks/repo/README.md#list_repo_branches2) - List all branches
* [list_repo_commits2](docs/sdks/repo/README.md#list_repo_commits2) - List all commits
* [list_repo_organizations2](docs/sdks/repo/README.md#list_repo_organizations2) - List all organizations
* [list_repo_pullrequests2](docs/sdks/repo/README.md#list_repo_pullrequests2) - List all pullrequests
* [list_repo_repositories2](docs/sdks/repo/README.md#list_repo_repositories2) - List all repositories
* [patch_repo_branch2](docs/sdks/repo/README.md#patch_repo_branch2) - Update a branch
* [patch_repo_commit2](docs/sdks/repo/README.md#patch_repo_commit2) - Update a commit
* [patch_repo_organization2](docs/sdks/repo/README.md#patch_repo_organization2) - Update an organization
* [patch_repo_pullrequest2](docs/sdks/repo/README.md#patch_repo_pullrequest2) - Update a pullrequest
* [patch_repo_repository2](docs/sdks/repo/README.md#patch_repo_repository2) - Update a repository
* [remove_repo_branch2](docs/sdks/repo/README.md#remove_repo_branch2) - Remove a branch
* [remove_repo_commit2](docs/sdks/repo/README.md#remove_repo_commit2) - Remove a commit
* [remove_repo_organization2](docs/sdks/repo/README.md#remove_repo_organization2) - Remove an organization
* [remove_repo_pullrequest2](docs/sdks/repo/README.md#remove_repo_pullrequest2) - Remove a pullrequest
* [remove_repo_repository2](docs/sdks/repo/README.md#remove_repo_repository2) - Remove a repository
* [update_repo_branch2](docs/sdks/repo/README.md#update_repo_branch2) - Update a branch
* [update_repo_commit2](docs/sdks/repo/README.md#update_repo_commit2) - Update a commit
* [update_repo_organization2](docs/sdks/repo/README.md#update_repo_organization2) - Update an organization
* [update_repo_pullrequest2](docs/sdks/repo/README.md#update_repo_pullrequest2) - Update a pullrequest
* [update_repo_repository2](docs/sdks/repo/README.md#update_repo_repository2) - Update a repository

### [Report](docs/sdks/report/README.md)

* [get_accounting_report2](docs/sdks/report/README.md#get_accounting_report2) - Retrieve a report
* [list_accounting_reports2](docs/sdks/report/README.md#list_accounting_reports2) - List all reports
* [list_ads_reports2](docs/sdks/report/README.md#list_ads_reports2) - List all reports
* [list_analytics_reports2](docs/sdks/report/README.md#list_analytics_reports2) - List all reports
* [list_martech_reports2](docs/sdks/report/README.md#list_martech_reports2) - List all reports

### [Repository](docs/sdks/repository/README.md)

* [create_repo_repository2](docs/sdks/repository/README.md#create_repo_repository2) - Create a repository
* [get_repo_repository2](docs/sdks/repository/README.md#get_repo_repository2) - Retrieve a repository
* [list_repo_repositories2](docs/sdks/repository/README.md#list_repo_repositories2) - List all repositories
* [patch_repo_repository2](docs/sdks/repository/README.md#patch_repo_repository2) - Update a repository
* [remove_repo_repository2](docs/sdks/repository/README.md#remove_repo_repository2) - Remove a repository
* [update_repo_repository2](docs/sdks/repository/README.md#update_repo_repository2) - Update a repository

### [Request](docs/sdks/request/README.md)

* [create_verification_request2](docs/sdks/request/README.md#create_verification_request2) - Create a request
* [get_verification_request2](docs/sdks/request/README.md#get_verification_request2) - Retrieve a request
* [list_verification_requests2](docs/sdks/request/README.md#list_verification_requests2) - List all requests
* [patch_verification_request2](docs/sdks/request/README.md#patch_verification_request2) - Update a request
* [remove_verification_request2](docs/sdks/request/README.md#remove_verification_request2) - Remove a request
* [update_verification_request2](docs/sdks/request/README.md#update_verification_request2) - Update a request

### [Reservation](docs/sdks/reservation/README.md)

* [create_commerce_reservation2](docs/sdks/reservation/README.md#create_commerce_reservation2) - Create a reservation
* [get_commerce_reservation2](docs/sdks/reservation/README.md#get_commerce_reservation2) - Retrieve a reservation
* [list_commerce_reservations2](docs/sdks/reservation/README.md#list_commerce_reservations2) - List all reservations
* [patch_commerce_reservation2](docs/sdks/reservation/README.md#patch_commerce_reservation2) - Update a reservation
* [remove_commerce_reservation2](docs/sdks/reservation/README.md#remove_commerce_reservation2) - Remove a reservation
* [update_commerce_reservation2](docs/sdks/reservation/README.md#update_commerce_reservation2) - Update a reservation

### [Review](docs/sdks/review/README.md)

* [create_commerce_review2](docs/sdks/review/README.md#create_commerce_review2) - Create a review
* [get_commerce_review2](docs/sdks/review/README.md#get_commerce_review2) - Retrieve a review
* [list_commerce_reviews2](docs/sdks/review/README.md#list_commerce_reviews2) - List all reviews
* [patch_commerce_review2](docs/sdks/review/README.md#patch_commerce_review2) - Update a review
* [remove_commerce_review2](docs/sdks/review/README.md#remove_commerce_review2) - Remove a review
* [update_commerce_review2](docs/sdks/review/README.md#update_commerce_review2) - Update a review

### [Saleschannel](docs/sdks/saleschannel/README.md)

* [create_commerce_saleschannel2](docs/sdks/saleschannel/README.md#create_commerce_saleschannel2) - Create a saleschannel
* [get_commerce_saleschannel2](docs/sdks/saleschannel/README.md#get_commerce_saleschannel2) - Retrieve a saleschannel
* [list_commerce_saleschannels2](docs/sdks/saleschannel/README.md#list_commerce_saleschannels2) - List all saleschannels
* [patch_commerce_saleschannel2](docs/sdks/saleschannel/README.md#patch_commerce_saleschannel2) - Update a saleschannel
* [remove_commerce_saleschannel2](docs/sdks/saleschannel/README.md#remove_commerce_saleschannel2) - Remove a saleschannel
* [update_commerce_saleschannel2](docs/sdks/saleschannel/README.md#update_commerce_saleschannel2) - Update a saleschannel

### [Salesorder](docs/sdks/salesorder/README.md)

* [create_accounting_salesorder2](docs/sdks/salesorder/README.md#create_accounting_salesorder2) - Create a salesorder
* [get_accounting_salesorder2](docs/sdks/salesorder/README.md#get_accounting_salesorder2) - Retrieve a salesorder
* [list_accounting_salesorders2](docs/sdks/salesorder/README.md#list_accounting_salesorders2) - List all salesorders
* [patch_accounting_salesorder2](docs/sdks/salesorder/README.md#patch_accounting_salesorder2) - Update a salesorder
* [remove_accounting_salesorder2](docs/sdks/salesorder/README.md#remove_accounting_salesorder2) - Remove a salesorder
* [update_accounting_salesorder2](docs/sdks/salesorder/README.md#update_accounting_salesorder2) - Update a salesorder

### [Scim](docs/sdks/scim/README.md)

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

### [Scorecard](docs/sdks/scorecard/README.md)

* [create_ats_scorecard2](docs/sdks/scorecard/README.md#create_ats_scorecard2) - Create a scorecard
* [get_ats_scorecard2](docs/sdks/scorecard/README.md#get_ats_scorecard2) - Retrieve a scorecard
* [list_ats_scorecards2](docs/sdks/scorecard/README.md#list_ats_scorecards2) - List all scorecards
* [patch_ats_scorecard2](docs/sdks/scorecard/README.md#patch_ats_scorecard2) - Update a scorecard
* [remove_ats_scorecard2](docs/sdks/scorecard/README.md#remove_ats_scorecard2) - Remove a scorecard
* [update_ats_scorecard2](docs/sdks/scorecard/README.md#update_ats_scorecard2) - Update a scorecard

### [Secretsmanager](docs/sdks/secretsmanager/README.md)

* [create_unified_workspace_secretsmanager](docs/sdks/secretsmanager/README.md#create_unified_workspace_secretsmanager) - Create secrets manager
* [get_unified_workspace_secretsmanager](docs/sdks/secretsmanager/README.md#get_unified_workspace_secretsmanager) - Retrieve secrets manager
* [list_unified_workspace_secretsmanagers](docs/sdks/secretsmanager/README.md#list_unified_workspace_secretsmanagers) - List secrets managers
* [remove_unified_workspace_secretsmanager](docs/sdks/secretsmanager/README.md#remove_unified_workspace_secretsmanager) - Remove secrets manager

### [Session](docs/sdks/session/README.md)

* [get_analytics_session2](docs/sdks/session/README.md#get_analytics_session2) - Retrieve a session
* [list_analytics_sessions2](docs/sdks/session/README.md#list_analytics_sessions2) - List all sessions

### [Shipment](docs/sdks/shipment/README.md)

* [create_shipping_shipment2](docs/sdks/shipment/README.md#create_shipping_shipment2) - Create a shipment
* [get_shipping_shipment2](docs/sdks/shipment/README.md#get_shipping_shipment2) - Retrieve a shipment
* [list_shipping_shipments2](docs/sdks/shipment/README.md#list_shipping_shipments2) - List all shipments
* [patch_shipping_shipment2](docs/sdks/shipment/README.md#patch_shipping_shipment2) - Update a shipment
* [remove_shipping_shipment2](docs/sdks/shipment/README.md#remove_shipping_shipment2) - Remove a shipment
* [update_shipping_shipment2](docs/sdks/shipment/README.md#update_shipping_shipment2) - Update a shipment

### [Shipping](docs/sdks/shipping/README.md)

* [create_shipping_label2](docs/sdks/shipping/README.md#create_shipping_label2) - Create a label
* [create_shipping_rate2](docs/sdks/shipping/README.md#create_shipping_rate2) - Create a rate
* [create_shipping_shipment2](docs/sdks/shipping/README.md#create_shipping_shipment2) - Create a shipment
* [get_shipping_carrier2](docs/sdks/shipping/README.md#get_shipping_carrier2) - Retrieve a carrier
* [get_shipping_label2](docs/sdks/shipping/README.md#get_shipping_label2) - Retrieve a label
* [get_shipping_shipment2](docs/sdks/shipping/README.md#get_shipping_shipment2) - Retrieve a shipment
* [get_shipping_tracking2](docs/sdks/shipping/README.md#get_shipping_tracking2) - Retrieve a tracking
* [list_shipping_carriers2](docs/sdks/shipping/README.md#list_shipping_carriers2) - List all carriers
* [list_shipping_labels2](docs/sdks/shipping/README.md#list_shipping_labels2) - List all labels
* [list_shipping_shipments2](docs/sdks/shipping/README.md#list_shipping_shipments2) - List all shipments
* [list_shipping_trackings2](docs/sdks/shipping/README.md#list_shipping_trackings2) - List all trackings
* [patch_shipping_label2](docs/sdks/shipping/README.md#patch_shipping_label2) - Update a label
* [patch_shipping_shipment2](docs/sdks/shipping/README.md#patch_shipping_shipment2) - Update a shipment
* [remove_shipping_label2](docs/sdks/shipping/README.md#remove_shipping_label2) - Remove a label
* [remove_shipping_shipment2](docs/sdks/shipping/README.md#remove_shipping_shipment2) - Remove a shipment
* [update_shipping_label2](docs/sdks/shipping/README.md#update_shipping_label2) - Update a label
* [update_shipping_shipment2](docs/sdks/shipping/README.md#update_shipping_shipment2) - Update a shipment

### [Signatory](docs/sdks/signatory/README.md)

* [create_signing_signatory2](docs/sdks/signatory/README.md#create_signing_signatory2) - Create a signatory
* [get_signing_signatory2](docs/sdks/signatory/README.md#get_signing_signatory2) - Retrieve a signatory
* [list_signing_signatories2](docs/sdks/signatory/README.md#list_signing_signatories2) - List all signatories
* [patch_signing_signatory2](docs/sdks/signatory/README.md#patch_signing_signatory2) - Update a signatory
* [remove_signing_signatory2](docs/sdks/signatory/README.md#remove_signing_signatory2) - Remove a signatory
* [update_signing_signatory2](docs/sdks/signatory/README.md#update_signing_signatory2) - Update a signatory

### [Signing](docs/sdks/signing/README.md)

* [create_signing_document2](docs/sdks/signing/README.md#create_signing_document2) - Create a document
* [create_signing_signatory2](docs/sdks/signing/README.md#create_signing_signatory2) - Create a signatory
* [get_signing_document2](docs/sdks/signing/README.md#get_signing_document2) - Retrieve a document
* [get_signing_signatory2](docs/sdks/signing/README.md#get_signing_signatory2) - Retrieve a signatory
* [get_signing_template2](docs/sdks/signing/README.md#get_signing_template2) - Retrieve a template
* [list_signing_documents2](docs/sdks/signing/README.md#list_signing_documents2) - List all documents
* [list_signing_signatories2](docs/sdks/signing/README.md#list_signing_signatories2) - List all signatories
* [list_signing_templates2](docs/sdks/signing/README.md#list_signing_templates2) - List all templates
* [patch_signing_document2](docs/sdks/signing/README.md#patch_signing_document2) - Update a document
* [patch_signing_signatory2](docs/sdks/signing/README.md#patch_signing_signatory2) - Update a signatory
* [remove_signing_document2](docs/sdks/signing/README.md#remove_signing_document2) - Remove a document
* [remove_signing_signatory2](docs/sdks/signing/README.md#remove_signing_signatory2) - Remove a signatory
* [update_signing_document2](docs/sdks/signing/README.md#update_signing_document2) - Update a document
* [update_signing_signatory2](docs/sdks/signing/README.md#update_signing_signatory2) - Update a signatory

### [Space](docs/sdks/space/README.md)

* [create_kms_space2](docs/sdks/space/README.md#create_kms_space2) - Create a space
* [get_kms_space2](docs/sdks/space/README.md#get_kms_space2) - Retrieve a space
* [list_kms_spaces2](docs/sdks/space/README.md#list_kms_spaces2) - List all spaces
* [patch_kms_space2](docs/sdks/space/README.md#patch_kms_space2) - Update a space
* [remove_kms_space2](docs/sdks/space/README.md#remove_kms_space2) - Remove a space
* [update_kms_space2](docs/sdks/space/README.md#update_kms_space2) - Update a space

### [Storage](docs/sdks/storage/README.md)

* [create_storage_file2](docs/sdks/storage/README.md#create_storage_file2) - Create a file
* [get_storage_file2](docs/sdks/storage/README.md#get_storage_file2) - Retrieve a file
* [list_storage_files2](docs/sdks/storage/README.md#list_storage_files2) - List all files
* [patch_storage_file2](docs/sdks/storage/README.md#patch_storage_file2) - Update a file
* [remove_storage_file2](docs/sdks/storage/README.md#remove_storage_file2) - Remove a file
* [update_storage_file2](docs/sdks/storage/README.md#update_storage_file2) - Update a file

### [Student](docs/sdks/student/README.md)

* [create_lms_student2](docs/sdks/student/README.md#create_lms_student2) - Create a student
* [get_lms_student2](docs/sdks/student/README.md#get_lms_student2) - Retrieve a student
* [list_lms_students2](docs/sdks/student/README.md#list_lms_students2) - List all students
* [patch_lms_student2](docs/sdks/student/README.md#patch_lms_student2) - Update a student
* [remove_lms_student2](docs/sdks/student/README.md#remove_lms_student2) - Remove a student
* [update_lms_student2](docs/sdks/student/README.md#update_lms_student2) - Update a student

### [Submission](docs/sdks/submission/README.md)

* [get_forms_submission2](docs/sdks/submission/README.md#get_forms_submission2) - Retrieve a submission
* [list_forms_submissions2](docs/sdks/submission/README.md#list_forms_submissions2) - List all submissions

### [Subscription](docs/sdks/subscription/README.md)

* [create_payment_subscription2](docs/sdks/subscription/README.md#create_payment_subscription2) - Create a subscription
* [get_payment_subscription2](docs/sdks/subscription/README.md#get_payment_subscription2) - Retrieve a subscription
* [list_payment_subscriptions2](docs/sdks/subscription/README.md#list_payment_subscriptions2) - List all subscriptions
* [patch_payment_subscription2](docs/sdks/subscription/README.md#patch_payment_subscription2) - Update a subscription
* [remove_payment_subscription2](docs/sdks/subscription/README.md#remove_payment_subscription2) - Remove a subscription
* [update_payment_subscription2](docs/sdks/subscription/README.md#update_payment_subscription2) - Update a subscription

### [Table](docs/sdks/table/README.md)

* [create_datastore_table2](docs/sdks/table/README.md#create_datastore_table2) - Create a table
* [get_datastore_table2](docs/sdks/table/README.md#get_datastore_table2) - Retrieve a table
* [list_datastore_tables2](docs/sdks/table/README.md#list_datastore_tables2) - List all tables
* [patch_datastore_table2](docs/sdks/table/README.md#patch_datastore_table2) - Update a table
* [remove_datastore_table2](docs/sdks/table/README.md#remove_datastore_table2) - Remove a table
* [update_datastore_table2](docs/sdks/table/README.md#update_datastore_table2) - Update a table

### [Target](docs/sdks/target/README.md)

* [get_ads_target2](docs/sdks/target/README.md#get_ads_target2) - Retrieve a target
* [list_ads_targets2](docs/sdks/target/README.md#list_ads_targets2) - List all targets

### [Task](docs/sdks/task/README.md)

* [create_task_comment2](docs/sdks/task/README.md#create_task_comment2) - Create a comment
* [create_task_project2](docs/sdks/task/README.md#create_task_project2) - Create a project
* [create_task_task2](docs/sdks/task/README.md#create_task_task2) - Create a task
* [get_task_change2](docs/sdks/task/README.md#get_task_change2) - Retrieve a change
* [get_task_comment2](docs/sdks/task/README.md#get_task_comment2) - Retrieve a comment
* [get_task_project2](docs/sdks/task/README.md#get_task_project2) - Retrieve a project
* [get_task_task2](docs/sdks/task/README.md#get_task_task2) - Retrieve a task
* [list_task_changes2](docs/sdks/task/README.md#list_task_changes2) - List all changes
* [list_task_comments2](docs/sdks/task/README.md#list_task_comments2) - List all comments
* [list_task_projects2](docs/sdks/task/README.md#list_task_projects2) - List all projects
* [list_task_tasks2](docs/sdks/task/README.md#list_task_tasks2) - List all tasks
* [patch_task_comment2](docs/sdks/task/README.md#patch_task_comment2) - Update a comment
* [patch_task_project2](docs/sdks/task/README.md#patch_task_project2) - Update a project
* [patch_task_task2](docs/sdks/task/README.md#patch_task_task2) - Update a task
* [remove_task_comment2](docs/sdks/task/README.md#remove_task_comment2) - Remove a comment
* [remove_task_project2](docs/sdks/task/README.md#remove_task_project2) - Remove a project
* [remove_task_task2](docs/sdks/task/README.md#remove_task_task2) - Remove a task
* [update_task_comment2](docs/sdks/task/README.md#update_task_comment2) - Update a comment
* [update_task_project2](docs/sdks/task/README.md#update_task_project2) - Update a project
* [update_task_task2](docs/sdks/task/README.md#update_task_task2) - Update a task

### [Taxrate](docs/sdks/taxrate/README.md)

* [create_accounting_taxrate2](docs/sdks/taxrate/README.md#create_accounting_taxrate2) - Create a taxrate
* [get_accounting_taxrate2](docs/sdks/taxrate/README.md#get_accounting_taxrate2) - Retrieve a taxrate
* [list_accounting_taxrates2](docs/sdks/taxrate/README.md#list_accounting_taxrates2) - List all taxrates
* [patch_accounting_taxrate2](docs/sdks/taxrate/README.md#patch_accounting_taxrate2) - Update a taxrate
* [remove_accounting_taxrate2](docs/sdks/taxrate/README.md#remove_accounting_taxrate2) - Remove a taxrate
* [update_accounting_taxrate2](docs/sdks/taxrate/README.md#update_accounting_taxrate2) - Update a taxrate

### [Template](docs/sdks/template/README.md)

* [get_signing_template2](docs/sdks/template/README.md#get_signing_template2) - Retrieve a template
* [list_signing_templates2](docs/sdks/template/README.md#list_signing_templates2) - List all templates

### [Ticket](docs/sdks/ticket/README.md)

* [create_ticketing_ticket2](docs/sdks/ticket/README.md#create_ticketing_ticket2) - Create a ticket
* [get_ticketing_ticket2](docs/sdks/ticket/README.md#get_ticketing_ticket2) - Retrieve a ticket
* [list_ticketing_tickets2](docs/sdks/ticket/README.md#list_ticketing_tickets2) - List all tickets
* [patch_ticketing_ticket2](docs/sdks/ticket/README.md#patch_ticketing_ticket2) - Update a ticket
* [remove_ticketing_ticket2](docs/sdks/ticket/README.md#remove_ticketing_ticket2) - Remove a ticket
* [update_ticketing_ticket2](docs/sdks/ticket/README.md#update_ticketing_ticket2) - Update a ticket

### [Ticketing](docs/sdks/ticketing/README.md)

* [create_ticketing_category2](docs/sdks/ticketing/README.md#create_ticketing_category2) - Create a category
* [create_ticketing_customer2](docs/sdks/ticketing/README.md#create_ticketing_customer2) - Create a customer
* [create_ticketing_note2](docs/sdks/ticketing/README.md#create_ticketing_note2) - Create a note
* [create_ticketing_ticket2](docs/sdks/ticketing/README.md#create_ticketing_ticket2) - Create a ticket
* [get_ticketing_category2](docs/sdks/ticketing/README.md#get_ticketing_category2) - Retrieve a category
* [get_ticketing_customer2](docs/sdks/ticketing/README.md#get_ticketing_customer2) - Retrieve a customer
* [get_ticketing_note2](docs/sdks/ticketing/README.md#get_ticketing_note2) - Retrieve a note
* [get_ticketing_ticket2](docs/sdks/ticketing/README.md#get_ticketing_ticket2) - Retrieve a ticket
* [list_ticketing_categories2](docs/sdks/ticketing/README.md#list_ticketing_categories2) - List all categories
* [list_ticketing_customers2](docs/sdks/ticketing/README.md#list_ticketing_customers2) - List all customers
* [list_ticketing_notes2](docs/sdks/ticketing/README.md#list_ticketing_notes2) - List all notes
* [list_ticketing_tickets2](docs/sdks/ticketing/README.md#list_ticketing_tickets2) - List all tickets
* [patch_ticketing_category2](docs/sdks/ticketing/README.md#patch_ticketing_category2) - Update a category
* [patch_ticketing_customer2](docs/sdks/ticketing/README.md#patch_ticketing_customer2) - Update a customer
* [patch_ticketing_note2](docs/sdks/ticketing/README.md#patch_ticketing_note2) - Update a note
* [patch_ticketing_ticket2](docs/sdks/ticketing/README.md#patch_ticketing_ticket2) - Update a ticket
* [remove_ticketing_category2](docs/sdks/ticketing/README.md#remove_ticketing_category2) - Remove a category
* [remove_ticketing_customer2](docs/sdks/ticketing/README.md#remove_ticketing_customer2) - Remove a customer
* [remove_ticketing_note2](docs/sdks/ticketing/README.md#remove_ticketing_note2) - Remove a note
* [remove_ticketing_ticket2](docs/sdks/ticketing/README.md#remove_ticketing_ticket2) - Remove a ticket
* [update_ticketing_category2](docs/sdks/ticketing/README.md#update_ticketing_category2) - Update a category
* [update_ticketing_customer2](docs/sdks/ticketing/README.md#update_ticketing_customer2) - Update a customer
* [update_ticketing_note2](docs/sdks/ticketing/README.md#update_ticketing_note2) - Update a note
* [update_ticketing_ticket2](docs/sdks/ticketing/README.md#update_ticketing_ticket2) - Update a ticket

### [Timeoff](docs/sdks/timeoff/README.md)

* [create_hris_timeoff2](docs/sdks/timeoff/README.md#create_hris_timeoff2) - Create a timeoff
* [get_hris_timeoff2](docs/sdks/timeoff/README.md#get_hris_timeoff2) - Retrieve a timeoff
* [list_hris_timeoffs2](docs/sdks/timeoff/README.md#list_hris_timeoffs2) - List all timeoffs
* [patch_hris_timeoff2](docs/sdks/timeoff/README.md#patch_hris_timeoff2) - Update a timeoff
* [remove_hris_timeoff2](docs/sdks/timeoff/README.md#remove_hris_timeoff2) - Remove a timeoff
* [update_hris_timeoff2](docs/sdks/timeoff/README.md#update_hris_timeoff2) - Update a timeoff

### [Timeshift](docs/sdks/timeshift/README.md)

* [create_hris_timeshift2](docs/sdks/timeshift/README.md#create_hris_timeshift2) - Create a timeshift
* [get_hris_timeshift2](docs/sdks/timeshift/README.md#get_hris_timeshift2) - Retrieve a timeshift
* [list_hris_timeshifts2](docs/sdks/timeshift/README.md#list_hris_timeshifts2) - List all timeshifts
* [patch_hris_timeshift2](docs/sdks/timeshift/README.md#patch_hris_timeshift2) - Update a timeshift
* [remove_hris_timeshift2](docs/sdks/timeshift/README.md#remove_hris_timeshift2) - Remove a timeshift
* [update_hris_timeshift2](docs/sdks/timeshift/README.md#update_hris_timeshift2) - Update a timeshift

### [Tracking](docs/sdks/tracking/README.md)

* [get_shipping_tracking2](docs/sdks/tracking/README.md#get_shipping_tracking2) - Retrieve a tracking
* [list_shipping_trackings2](docs/sdks/tracking/README.md#list_shipping_trackings2) - List all trackings

### [Transaction](docs/sdks/transaction/README.md)

* [create_accounting_transaction2](docs/sdks/transaction/README.md#create_accounting_transaction2) - Create a transaction
* [get_accounting_transaction2](docs/sdks/transaction/README.md#get_accounting_transaction2) - Retrieve a transaction
* [list_accounting_transactions2](docs/sdks/transaction/README.md#list_accounting_transactions2) - List all transactions
* [patch_accounting_transaction2](docs/sdks/transaction/README.md#patch_accounting_transaction2) - Update a transaction
* [remove_accounting_transaction2](docs/sdks/transaction/README.md#remove_accounting_transaction2) - Remove a transaction
* [update_accounting_transaction2](docs/sdks/transaction/README.md#update_accounting_transaction2) - Update a transaction

### [Trialbalance](docs/sdks/trialbalance/README.md)

* [get_accounting_trialbalance2](docs/sdks/trialbalance/README.md#get_accounting_trialbalance2) - Retrieve a trialbalance
* [list_accounting_trialbalances2](docs/sdks/trialbalance/README.md#list_accounting_trialbalances2) - List all trialbalances

### [Uc](docs/sdks/uc/README.md)

* [create_uc_comment2](docs/sdks/uc/README.md#create_uc_comment2) - Create a comment
* [create_uc_contact2](docs/sdks/uc/README.md#create_uc_contact2) - Create a contact
* [create_uc_recording2](docs/sdks/uc/README.md#create_uc_recording2) - Create a recording
* [get_uc_call2](docs/sdks/uc/README.md#get_uc_call2) - Retrieve a call
* [get_uc_comment2](docs/sdks/uc/README.md#get_uc_comment2) - Retrieve a comment
* [get_uc_contact2](docs/sdks/uc/README.md#get_uc_contact2) - Retrieve a contact
* [get_uc_recording2](docs/sdks/uc/README.md#get_uc_recording2) - Retrieve a recording
* [list_uc_calls2](docs/sdks/uc/README.md#list_uc_calls2) - List all calls
* [list_uc_comments2](docs/sdks/uc/README.md#list_uc_comments2) - List all comments
* [list_uc_contacts2](docs/sdks/uc/README.md#list_uc_contacts2) - List all contacts
* [list_uc_recordings2](docs/sdks/uc/README.md#list_uc_recordings2) - List all recordings
* [patch_uc_comment2](docs/sdks/uc/README.md#patch_uc_comment2) - Update a comment
* [patch_uc_contact2](docs/sdks/uc/README.md#patch_uc_contact2) - Update a contact
* [patch_uc_recording2](docs/sdks/uc/README.md#patch_uc_recording2) - Update a recording
* [remove_uc_comment2](docs/sdks/uc/README.md#remove_uc_comment2) - Remove a comment
* [remove_uc_contact2](docs/sdks/uc/README.md#remove_uc_contact2) - Remove a contact
* [remove_uc_recording2](docs/sdks/uc/README.md#remove_uc_recording2) - Remove a recording
* [update_uc_comment2](docs/sdks/uc/README.md#update_uc_comment2) - Update a comment
* [update_uc_contact2](docs/sdks/uc/README.md#update_uc_contact2) - Update a contact
* [update_uc_recording2](docs/sdks/uc/README.md#update_uc_recording2) - Update a recording

### [Unified](docs/sdks/unified/README.md)

* [create_unified_connection](docs/sdks/unified/README.md#create_unified_connection) - Create connection
* [create_unified_environment](docs/sdks/unified/README.md#create_unified_environment) - Create new environments
* [create_unified_webhook](docs/sdks/unified/README.md#create_unified_webhook) - Create webhook subscription
* [create_unified_workspace_secretsmanager](docs/sdks/unified/README.md#create_unified_workspace_secretsmanager) - Create secrets manager
* [get_unified_apicall](docs/sdks/unified/README.md#get_unified_apicall) - Retrieve specific API Call by its ID
* [get_unified_connection](docs/sdks/unified/README.md#get_unified_connection) - Retrieve connection
* [get_unified_integration_auth](docs/sdks/unified/README.md#get_unified_integration_auth) - Authorize new connection
* [get_unified_issue](docs/sdks/unified/README.md#get_unified_issue) - Retrieve support issue
* [get_unified_webhook](docs/sdks/unified/README.md#get_unified_webhook) - Retrieve webhook by its ID
* [get_unified_workspace_secretsmanager](docs/sdks/unified/README.md#get_unified_workspace_secretsmanager) - Retrieve secrets manager
* [list_unified_apicalls](docs/sdks/unified/README.md#list_unified_apicalls) - Returns API Calls
* [list_unified_connections](docs/sdks/unified/README.md#list_unified_connections) - List all connections
* [list_unified_environments](docs/sdks/unified/README.md#list_unified_environments) - Returns all environments
* [list_unified_integration_workspaces](docs/sdks/unified/README.md#list_unified_integration_workspaces) - Returns all activated integrations in a workspace
* [list_unified_integrations](docs/sdks/unified/README.md#list_unified_integrations) - Returns all integrations
* [list_unified_issues](docs/sdks/unified/README.md#list_unified_issues) - List support issues
* [list_unified_webhooks](docs/sdks/unified/README.md#list_unified_webhooks) - Returns all registered webhooks
* [list_unified_workspace_secretsmanagers](docs/sdks/unified/README.md#list_unified_workspace_secretsmanagers) - List secrets managers
* [patch_unified_connection](docs/sdks/unified/README.md#patch_unified_connection) - Update connection
* [patch_unified_webhook](docs/sdks/unified/README.md#patch_unified_webhook) - Update webhook subscription
* [patch_unified_webhook_trigger](docs/sdks/unified/README.md#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_connection](docs/sdks/unified/README.md#remove_unified_connection) - Remove connection
* [remove_unified_environment](docs/sdks/unified/README.md#remove_unified_environment) - Remove an environment
* [remove_unified_webhook](docs/sdks/unified/README.md#remove_unified_webhook) - Remove webhook subscription
* [remove_unified_workspace_secretsmanager](docs/sdks/unified/README.md#remove_unified_workspace_secretsmanager) - Remove secrets manager
* [update_unified_connection](docs/sdks/unified/README.md#update_unified_connection) - Update connection
* [update_unified_webhook](docs/sdks/unified/README.md#update_unified_webhook) - Update webhook subscription
* [update_unified_webhook_trigger](docs/sdks/unified/README.md#update_unified_webhook_trigger) - Trigger webhook

### [User](docs/sdks/user/README.md)

* [create_scim_users](docs/sdks/user/README.md#create_scim_users) - Create user
* [get_scim_users](docs/sdks/user/README.md#get_scim_users) - Get user
* [list_scim_users](docs/sdks/user/README.md#list_scim_users) - List users
* [patch_scim_users](docs/sdks/user/README.md#patch_scim_users) - Update user
* [remove_scim_users](docs/sdks/user/README.md#remove_scim_users) - Delete user
* [update_scim_users](docs/sdks/user/README.md#update_scim_users) - Update user

### [Verification](docs/sdks/verification/README.md)

* [create_verification_request2](docs/sdks/verification/README.md#create_verification_request2) - Create a request
* [get_verification_package2](docs/sdks/verification/README.md#get_verification_package2) - Retrieve a package
* [get_verification_request2](docs/sdks/verification/README.md#get_verification_request2) - Retrieve a request
* [list_verification_packages2](docs/sdks/verification/README.md#list_verification_packages2) - List all packages
* [list_verification_requests2](docs/sdks/verification/README.md#list_verification_requests2) - List all requests
* [patch_verification_request2](docs/sdks/verification/README.md#patch_verification_request2) - Update a request
* [remove_verification_request2](docs/sdks/verification/README.md#remove_verification_request2) - Remove a request
* [update_verification_request2](docs/sdks/verification/README.md#update_verification_request2) - Update a request

### [Visitor](docs/sdks/visitor/README.md)

* [create_analytics_visitor2](docs/sdks/visitor/README.md#create_analytics_visitor2) - Create a visitor
* [get_analytics_visitor2](docs/sdks/visitor/README.md#get_analytics_visitor2) - Retrieve a visitor
* [list_analytics_visitors2](docs/sdks/visitor/README.md#list_analytics_visitors2) - List all visitors
* [patch_analytics_visitor2](docs/sdks/visitor/README.md#patch_analytics_visitor2) - Update a visitor
* [remove_analytics_visitor2](docs/sdks/visitor/README.md#remove_analytics_visitor2) - Remove a visitor
* [update_analytics_visitor2](docs/sdks/visitor/README.md#update_analytics_visitor2) - Update a visitor

### [Webhook](docs/sdks/webhook/README.md)

* [create_unified_webhook](docs/sdks/webhook/README.md#create_unified_webhook) - Create webhook subscription
* [get_unified_webhook](docs/sdks/webhook/README.md#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_webhooks](docs/sdks/webhook/README.md#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_webhook](docs/sdks/webhook/README.md#patch_unified_webhook) - Update webhook subscription
* [patch_unified_webhook_trigger](docs/sdks/webhook/README.md#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_webhook](docs/sdks/webhook/README.md#remove_unified_webhook) - Remove webhook subscription
* [update_unified_webhook](docs/sdks/webhook/README.md#update_unified_webhook) - Update webhook subscription
* [update_unified_webhook_trigger](docs/sdks/webhook/README.md#update_unified_webhook_trigger) - Trigger webhook

### [Webinar](docs/sdks/webinar/README.md)

* [create_calendar_webinar2](docs/sdks/webinar/README.md#create_calendar_webinar2) - Create a webinar
* [get_calendar_webinar2](docs/sdks/webinar/README.md#get_calendar_webinar2) - Retrieve a webinar
* [list_calendar_webinars2](docs/sdks/webinar/README.md#list_calendar_webinars2) - List all webinars
* [patch_calendar_webinar2](docs/sdks/webinar/README.md#patch_calendar_webinar2) - Update a webinar
* [remove_calendar_webinar2](docs/sdks/webinar/README.md#remove_calendar_webinar2) - Remove a webinar
* [update_calendar_webinar2](docs/sdks/webinar/README.md#update_calendar_webinar2) - Update a webinar

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

    res = unified_to.passthrough.create_passthrough2_raw(request={
        "connection_id": "<id>",
        "path": "/net",
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

    res = unified_to.accounting.create_accounting_account2(request={
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

    res = unified_to.accounting.create_accounting_account2(request={
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

        res = unified_to.accounting.create_accounting_account2(request={
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
    server_idx=0,
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.accounting.create_accounting_account2(request={
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

    res = unified_to.accounting.create_accounting_account2(request={
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

    res = unified_to.accounting.create_accounting_account2(request={
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
