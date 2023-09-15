# Unified-php-sdk

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/unified-to/unified-python-sdk.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/bolt-php/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/unified-to/unified-python-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDAgentIDRequest(
    connection_id='corrupti',
    id='9bd9d8d6-9a67-44e0-b467-cc8796ed151a',
)

res = s.agent.delete_ticketing_connection_id_agent_id(req, operations.DeleteTicketingConnectionIDAgentIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [Agent](docs/sdks/agent/README.md)

* [delete_ticketing_connection_id_agent_id](docs/sdks/agent/README.md#delete_ticketing_connection_id_agent_id) - Remove a agent
* [get_ticketing_connection_id_agent](docs/sdks/agent/README.md#get_ticketing_connection_id_agent) - List all agents
* [get_ticketing_connection_id_agent_id](docs/sdks/agent/README.md#get_ticketing_connection_id_agent_id) - Retrieve a agent
* [get_uc_connection_id_agent](docs/sdks/agent/README.md#get_uc_connection_id_agent) - List all agents
* [patch_ticketing_connection_id_agent_id](docs/sdks/agent/README.md#patch_ticketing_connection_id_agent_id) - Update a agent
* [post_ticketing_connection_id_agent](docs/sdks/agent/README.md#post_ticketing_connection_id_agent) - Create a agent
* [put_ticketing_connection_id_agent_id](docs/sdks/agent/README.md#put_ticketing_connection_id_agent_id) - Update a agent

### [Apicall](docs/sdks/apicall/README.md)

* [get_unified_apicall](docs/sdks/apicall/README.md#get_unified_apicall) - Returns API Calls
* [get_unified_apicall_id](docs/sdks/apicall/README.md#get_unified_apicall_id) - Retrieve specific API Call by its ID

### [Application](docs/sdks/application/README.md)

* [delete_ats_connection_id_application_id](docs/sdks/application/README.md#delete_ats_connection_id_application_id) - Remove an application
* [get_ats_connection_id_application](docs/sdks/application/README.md#get_ats_connection_id_application) - List all applications
* [get_ats_connection_id_application_id](docs/sdks/application/README.md#get_ats_connection_id_application_id) - Retrieve an application
* [patch_ats_connection_id_application_id](docs/sdks/application/README.md#patch_ats_connection_id_application_id) - Update an application
* [post_ats_connection_id_application](docs/sdks/application/README.md#post_ats_connection_id_application) - Create an application
* [put_ats_connection_id_application_id](docs/sdks/application/README.md#put_ats_connection_id_application_id) - Update an application

### [Ats](docs/sdks/ats/README.md)

* [delete_ats_connection_id_application_id](docs/sdks/ats/README.md#delete_ats_connection_id_application_id) - Remove an application
* [delete_ats_connection_id_candidate_id](docs/sdks/ats/README.md#delete_ats_connection_id_candidate_id) - Remove a candidate
* [delete_ats_connection_id_interview_id](docs/sdks/ats/README.md#delete_ats_connection_id_interview_id) - Remove a interview
* [delete_ats_connection_id_job_id](docs/sdks/ats/README.md#delete_ats_connection_id_job_id) - Remove a job
* [delete_ats_connection_id_scorecard_id](docs/sdks/ats/README.md#delete_ats_connection_id_scorecard_id) - Remove a scorecard
* [get_ats_connection_id_application](docs/sdks/ats/README.md#get_ats_connection_id_application) - List all applications
* [get_ats_connection_id_application_id](docs/sdks/ats/README.md#get_ats_connection_id_application_id) - Retrieve an application
* [get_ats_connection_id_candidate](docs/sdks/ats/README.md#get_ats_connection_id_candidate) - List all candidates
* [get_ats_connection_id_candidate_id](docs/sdks/ats/README.md#get_ats_connection_id_candidate_id) - Retrieve a candidate
* [get_ats_connection_id_interview](docs/sdks/ats/README.md#get_ats_connection_id_interview) - List all interviews
* [get_ats_connection_id_interview_id](docs/sdks/ats/README.md#get_ats_connection_id_interview_id) - Retrieve a interview
* [get_ats_connection_id_job](docs/sdks/ats/README.md#get_ats_connection_id_job) - List all jobs
* [get_ats_connection_id_job_id](docs/sdks/ats/README.md#get_ats_connection_id_job_id) - Retrieve a job
* [get_ats_connection_id_scorecard](docs/sdks/ats/README.md#get_ats_connection_id_scorecard) - List all scorecards
* [get_ats_connection_id_scorecard_id](docs/sdks/ats/README.md#get_ats_connection_id_scorecard_id) - Retrieve a scorecard
* [patch_ats_connection_id_application_id](docs/sdks/ats/README.md#patch_ats_connection_id_application_id) - Update an application
* [patch_ats_connection_id_candidate_id](docs/sdks/ats/README.md#patch_ats_connection_id_candidate_id) - Update a candidate
* [patch_ats_connection_id_interview_id](docs/sdks/ats/README.md#patch_ats_connection_id_interview_id) - Update a interview
* [patch_ats_connection_id_job_id](docs/sdks/ats/README.md#patch_ats_connection_id_job_id) - Update a job
* [patch_ats_connection_id_scorecard_id](docs/sdks/ats/README.md#patch_ats_connection_id_scorecard_id) - Update a scorecard
* [post_ats_connection_id_application](docs/sdks/ats/README.md#post_ats_connection_id_application) - Create an application
* [post_ats_connection_id_candidate](docs/sdks/ats/README.md#post_ats_connection_id_candidate) - Create a candidate
* [post_ats_connection_id_interview](docs/sdks/ats/README.md#post_ats_connection_id_interview) - Create a interview
* [post_ats_connection_id_job](docs/sdks/ats/README.md#post_ats_connection_id_job) - Create a job
* [post_ats_connection_id_scorecard](docs/sdks/ats/README.md#post_ats_connection_id_scorecard) - Create a scorecard
* [put_ats_connection_id_application_id](docs/sdks/ats/README.md#put_ats_connection_id_application_id) - Update an application
* [put_ats_connection_id_candidate_id](docs/sdks/ats/README.md#put_ats_connection_id_candidate_id) - Update a candidate
* [put_ats_connection_id_interview_id](docs/sdks/ats/README.md#put_ats_connection_id_interview_id) - Update a interview
* [put_ats_connection_id_job_id](docs/sdks/ats/README.md#put_ats_connection_id_job_id) - Update a job
* [put_ats_connection_id_scorecard_id](docs/sdks/ats/README.md#put_ats_connection_id_scorecard_id) - Update a scorecard

### [Auth](docs/sdks/auth/README.md)

* [get_unified_integration_auth_workspace_id_integration_type](docs/sdks/auth/README.md#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_login_workspace_id_integration_type](docs/sdks/auth/README.md#get_unified_integration_login_workspace_id_integration_type) - Sign in a user

### [Call](docs/sdks/call/README.md)

* [get_uc_connection_id_call](docs/sdks/call/README.md#get_uc_connection_id_call) - List all calls

### [Candidate](docs/sdks/candidate/README.md)

* [delete_ats_connection_id_candidate_id](docs/sdks/candidate/README.md#delete_ats_connection_id_candidate_id) - Remove a candidate
* [get_ats_connection_id_candidate](docs/sdks/candidate/README.md#get_ats_connection_id_candidate) - List all candidates
* [get_ats_connection_id_candidate_id](docs/sdks/candidate/README.md#get_ats_connection_id_candidate_id) - Retrieve a candidate
* [patch_ats_connection_id_candidate_id](docs/sdks/candidate/README.md#patch_ats_connection_id_candidate_id) - Update a candidate
* [post_ats_connection_id_candidate](docs/sdks/candidate/README.md#post_ats_connection_id_candidate) - Create a candidate
* [put_ats_connection_id_candidate_id](docs/sdks/candidate/README.md#put_ats_connection_id_candidate_id) - Update a candidate

### [Company](docs/sdks/company/README.md)

* [delete_crm_connection_id_company_id](docs/sdks/company/README.md#delete_crm_connection_id_company_id) - Remove a company
* [delete_crm_connection_id_company_id_deal_deal_id](docs/sdks/company/README.md#delete_crm_connection_id_company_id_deal_deal_id) - Remove deal association from a company
* [get_crm_connection_id_company](docs/sdks/company/README.md#get_crm_connection_id_company) - List all companies
* [get_crm_connection_id_company_id](docs/sdks/company/README.md#get_crm_connection_id_company_id) - Retrieve a company
* [get_enrich_connection_id_company](docs/sdks/company/README.md#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [patch_crm_connection_id_company_id](docs/sdks/company/README.md#patch_crm_connection_id_company_id) - Update a company
* [patch_crm_connection_id_company_id_deal_deal_id](docs/sdks/company/README.md#patch_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company
* [post_crm_connection_id_company](docs/sdks/company/README.md#post_crm_connection_id_company) - Create a company
* [put_crm_connection_id_company_id](docs/sdks/company/README.md#put_crm_connection_id_company_id) - Update a company
* [put_crm_connection_id_company_id_deal_deal_id](docs/sdks/company/README.md#put_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company

### [Connection](docs/sdks/connection/README.md)

* [delete_unified_connection_id](docs/sdks/connection/README.md#delete_unified_connection_id) - Remove connection
* [get_unified_connection](docs/sdks/connection/README.md#get_unified_connection) - List all connections
* [get_unified_connection_id](docs/sdks/connection/README.md#get_unified_connection_id) - Retrieve connection
* [patch_unified_connection_id](docs/sdks/connection/README.md#patch_unified_connection_id) - Update connection
* [post_unified_connection](docs/sdks/connection/README.md#post_unified_connection) - Create connection
* [put_unified_connection_id](docs/sdks/connection/README.md#put_unified_connection_id) - Update connection

### [Contact](docs/sdks/contact/README.md)

* [delete_crm_connection_id_contact_id](docs/sdks/contact/README.md#delete_crm_connection_id_contact_id) - Remove a contact
* [delete_crm_connection_id_contact_id_company_company_id](docs/sdks/contact/README.md#delete_crm_connection_id_contact_id_company_company_id) - Remove company association from a contact
* [delete_crm_connection_id_contact_id_deal_deal_id](docs/sdks/contact/README.md#delete_crm_connection_id_contact_id_deal_deal_id) - Remove deal association from a contact
* [delete_uc_connection_id_contact_id](docs/sdks/contact/README.md#delete_uc_connection_id_contact_id) - Remove a contact
* [get_crm_connection_id_contact](docs/sdks/contact/README.md#get_crm_connection_id_contact) - List all contacts
* [get_crm_connection_id_contact_id](docs/sdks/contact/README.md#get_crm_connection_id_contact_id) - Retrieve a contact
* [get_uc_connection_id_contact](docs/sdks/contact/README.md#get_uc_connection_id_contact) - List all contacts
* [get_uc_connection_id_contact_id](docs/sdks/contact/README.md#get_uc_connection_id_contact_id) - Retrieve a contact
* [patch_crm_connection_id_contact_id](docs/sdks/contact/README.md#patch_crm_connection_id_contact_id) - Update a contact
* [patch_crm_connection_id_contact_id_company_company_id](docs/sdks/contact/README.md#patch_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [patch_crm_connection_id_contact_id_deal_deal_id](docs/sdks/contact/README.md#patch_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [patch_uc_connection_id_contact_id](docs/sdks/contact/README.md#patch_uc_connection_id_contact_id) - Update a contact
* [post_crm_connection_id_contact](docs/sdks/contact/README.md#post_crm_connection_id_contact) - Create a contact
* [post_uc_connection_id_contact](docs/sdks/contact/README.md#post_uc_connection_id_contact) - Create a contact
* [put_crm_connection_id_contact_id](docs/sdks/contact/README.md#put_crm_connection_id_contact_id) - Update a contact
* [put_crm_connection_id_contact_id_company_company_id](docs/sdks/contact/README.md#put_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [put_crm_connection_id_contact_id_deal_deal_id](docs/sdks/contact/README.md#put_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [put_uc_connection_id_contact_id](docs/sdks/contact/README.md#put_uc_connection_id_contact_id) - Update a contact

### [Crm](docs/sdks/crm/README.md)

* [delete_crm_connection_id_company_id](docs/sdks/crm/README.md#delete_crm_connection_id_company_id) - Remove a company
* [delete_crm_connection_id_company_id_deal_deal_id](docs/sdks/crm/README.md#delete_crm_connection_id_company_id_deal_deal_id) - Remove deal association from a company
* [delete_crm_connection_id_contact_id](docs/sdks/crm/README.md#delete_crm_connection_id_contact_id) - Remove a contact
* [delete_crm_connection_id_contact_id_company_company_id](docs/sdks/crm/README.md#delete_crm_connection_id_contact_id_company_company_id) - Remove company association from a contact
* [delete_crm_connection_id_contact_id_deal_deal_id](docs/sdks/crm/README.md#delete_crm_connection_id_contact_id_deal_deal_id) - Remove deal association from a contact
* [delete_crm_connection_id_deal_id](docs/sdks/crm/README.md#delete_crm_connection_id_deal_id) - Remove a deal
* [delete_crm_connection_id_event_id](docs/sdks/crm/README.md#delete_crm_connection_id_event_id) - Remove a event
* [delete_crm_connection_id_event_id_company_company_id](docs/sdks/crm/README.md#delete_crm_connection_id_event_id_company_company_id) - Remove company association from an event
* [delete_crm_connection_id_event_id_contact_contact_id](docs/sdks/crm/README.md#delete_crm_connection_id_event_id_contact_contact_id) - Remove contact association from an event
* [delete_crm_connection_id_event_id_deal_deal_id](docs/sdks/crm/README.md#delete_crm_connection_id_event_id_deal_deal_id) - Remove deal association from an event
* [delete_crm_connection_id_file_id](docs/sdks/crm/README.md#delete_crm_connection_id_file_id) - Remove a file
* [delete_crm_connection_id_lead_id](docs/sdks/crm/README.md#delete_crm_connection_id_lead_id) - Remove a lead
* [delete_crm_connection_id_pipeline_id](docs/sdks/crm/README.md#delete_crm_connection_id_pipeline_id) - Remove a pipeline
* [delete_crm_connection_id_team_id](docs/sdks/crm/README.md#delete_crm_connection_id_team_id) - Remove a team
* [delete_crm_connection_id_user_id](docs/sdks/crm/README.md#delete_crm_connection_id_user_id) - Remove a user
* [get_crm_connection_id_company](docs/sdks/crm/README.md#get_crm_connection_id_company) - List all companies
* [get_crm_connection_id_company_id](docs/sdks/crm/README.md#get_crm_connection_id_company_id) - Retrieve a company
* [get_crm_connection_id_contact](docs/sdks/crm/README.md#get_crm_connection_id_contact) - List all contacts
* [get_crm_connection_id_contact_id](docs/sdks/crm/README.md#get_crm_connection_id_contact_id) - Retrieve a contact
* [get_crm_connection_id_deal](docs/sdks/crm/README.md#get_crm_connection_id_deal) - List all deals
* [get_crm_connection_id_deal_id](docs/sdks/crm/README.md#get_crm_connection_id_deal_id) - Retrieve a deal
* [get_crm_connection_id_event](docs/sdks/crm/README.md#get_crm_connection_id_event) - List all events
* [get_crm_connection_id_event_id](docs/sdks/crm/README.md#get_crm_connection_id_event_id) - Retrieve a event
* [get_crm_connection_id_file](docs/sdks/crm/README.md#get_crm_connection_id_file) - List all files
* [get_crm_connection_id_file_id](docs/sdks/crm/README.md#get_crm_connection_id_file_id) - Retrieve a file
* [get_crm_connection_id_lead](docs/sdks/crm/README.md#get_crm_connection_id_lead) - List all leads
* [get_crm_connection_id_lead_id](docs/sdks/crm/README.md#get_crm_connection_id_lead_id) - Retrieve a lead
* [get_crm_connection_id_pipeline](docs/sdks/crm/README.md#get_crm_connection_id_pipeline) - List all pipelines
* [get_crm_connection_id_pipeline_id](docs/sdks/crm/README.md#get_crm_connection_id_pipeline_id) - Retrieve a pipeline
* [get_crm_connection_id_team](docs/sdks/crm/README.md#get_crm_connection_id_team) - List all teams
* [get_crm_connection_id_team_id](docs/sdks/crm/README.md#get_crm_connection_id_team_id) - Retrieve a team
* [get_crm_connection_id_user](docs/sdks/crm/README.md#get_crm_connection_id_user) - List all users
* [get_crm_connection_id_user_id](docs/sdks/crm/README.md#get_crm_connection_id_user_id) - Retrieve a user
* [patch_crm_connection_id_company_id](docs/sdks/crm/README.md#patch_crm_connection_id_company_id) - Update a company
* [patch_crm_connection_id_company_id_deal_deal_id](docs/sdks/crm/README.md#patch_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company
* [patch_crm_connection_id_contact_id](docs/sdks/crm/README.md#patch_crm_connection_id_contact_id) - Update a contact
* [patch_crm_connection_id_contact_id_company_company_id](docs/sdks/crm/README.md#patch_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [patch_crm_connection_id_contact_id_deal_deal_id](docs/sdks/crm/README.md#patch_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [patch_crm_connection_id_deal_id](docs/sdks/crm/README.md#patch_crm_connection_id_deal_id) - Update a deal
* [patch_crm_connection_id_event_id](docs/sdks/crm/README.md#patch_crm_connection_id_event_id) - Update a event
* [patch_crm_connection_id_event_id_company_company_id](docs/sdks/crm/README.md#patch_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [patch_crm_connection_id_event_id_contact_contact_id](docs/sdks/crm/README.md#patch_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [patch_crm_connection_id_event_id_deal_deal_id](docs/sdks/crm/README.md#patch_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event
* [patch_crm_connection_id_file_id](docs/sdks/crm/README.md#patch_crm_connection_id_file_id) - Update a file
* [patch_crm_connection_id_lead_id](docs/sdks/crm/README.md#patch_crm_connection_id_lead_id) - Update a lead
* [patch_crm_connection_id_pipeline_id](docs/sdks/crm/README.md#patch_crm_connection_id_pipeline_id) - Update a pipeline
* [patch_crm_connection_id_team_id](docs/sdks/crm/README.md#patch_crm_connection_id_team_id) - Update a team
* [patch_crm_connection_id_user_id](docs/sdks/crm/README.md#patch_crm_connection_id_user_id) - Update a user
* [post_crm_connection_id_company](docs/sdks/crm/README.md#post_crm_connection_id_company) - Create a company
* [post_crm_connection_id_contact](docs/sdks/crm/README.md#post_crm_connection_id_contact) - Create a contact
* [post_crm_connection_id_deal](docs/sdks/crm/README.md#post_crm_connection_id_deal) - Create a deal
* [post_crm_connection_id_event](docs/sdks/crm/README.md#post_crm_connection_id_event) - Create a event
* [post_crm_connection_id_file](docs/sdks/crm/README.md#post_crm_connection_id_file) - Create a file
* [post_crm_connection_id_lead](docs/sdks/crm/README.md#post_crm_connection_id_lead) - Create a lead
* [post_crm_connection_id_pipeline](docs/sdks/crm/README.md#post_crm_connection_id_pipeline) - Create a pipeline
* [post_crm_connection_id_team](docs/sdks/crm/README.md#post_crm_connection_id_team) - Create a team
* [post_crm_connection_id_user](docs/sdks/crm/README.md#post_crm_connection_id_user) - Create a user
* [put_crm_connection_id_company_id](docs/sdks/crm/README.md#put_crm_connection_id_company_id) - Update a company
* [put_crm_connection_id_company_id_deal_deal_id](docs/sdks/crm/README.md#put_crm_connection_id_company_id_deal_deal_id) - Associate a deal with a company
* [put_crm_connection_id_contact_id](docs/sdks/crm/README.md#put_crm_connection_id_contact_id) - Update a contact
* [put_crm_connection_id_contact_id_company_company_id](docs/sdks/crm/README.md#put_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [put_crm_connection_id_contact_id_deal_deal_id](docs/sdks/crm/README.md#put_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [put_crm_connection_id_deal_id](docs/sdks/crm/README.md#put_crm_connection_id_deal_id) - Update a deal
* [put_crm_connection_id_event_id](docs/sdks/crm/README.md#put_crm_connection_id_event_id) - Update a event
* [put_crm_connection_id_event_id_company_company_id](docs/sdks/crm/README.md#put_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [put_crm_connection_id_event_id_contact_contact_id](docs/sdks/crm/README.md#put_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [put_crm_connection_id_event_id_deal_deal_id](docs/sdks/crm/README.md#put_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event
* [put_crm_connection_id_file_id](docs/sdks/crm/README.md#put_crm_connection_id_file_id) - Update a file
* [put_crm_connection_id_lead_id](docs/sdks/crm/README.md#put_crm_connection_id_lead_id) - Update a lead
* [put_crm_connection_id_pipeline_id](docs/sdks/crm/README.md#put_crm_connection_id_pipeline_id) - Update a pipeline
* [put_crm_connection_id_team_id](docs/sdks/crm/README.md#put_crm_connection_id_team_id) - Update a team
* [put_crm_connection_id_user_id](docs/sdks/crm/README.md#put_crm_connection_id_user_id) - Update a user

### [Customer](docs/sdks/customer/README.md)

* [delete_ticketing_connection_id_customer_id](docs/sdks/customer/README.md#delete_ticketing_connection_id_customer_id) - Remove a customer
* [get_ticketing_connection_id_customer](docs/sdks/customer/README.md#get_ticketing_connection_id_customer) - List all customers
* [get_ticketing_connection_id_customer_id](docs/sdks/customer/README.md#get_ticketing_connection_id_customer_id) - Retrieve a customer
* [patch_ticketing_connection_id_customer_id](docs/sdks/customer/README.md#patch_ticketing_connection_id_customer_id) - Update a customer
* [post_ticketing_connection_id_customer](docs/sdks/customer/README.md#post_ticketing_connection_id_customer) - Create a customer
* [put_ticketing_connection_id_customer_id](docs/sdks/customer/README.md#put_ticketing_connection_id_customer_id) - Update a customer

### [Deal](docs/sdks/deal/README.md)

* [delete_crm_connection_id_deal_id](docs/sdks/deal/README.md#delete_crm_connection_id_deal_id) - Remove a deal
* [get_crm_connection_id_deal](docs/sdks/deal/README.md#get_crm_connection_id_deal) - List all deals
* [get_crm_connection_id_deal_id](docs/sdks/deal/README.md#get_crm_connection_id_deal_id) - Retrieve a deal
* [patch_crm_connection_id_deal_id](docs/sdks/deal/README.md#patch_crm_connection_id_deal_id) - Update a deal
* [post_crm_connection_id_deal](docs/sdks/deal/README.md#post_crm_connection_id_deal) - Create a deal
* [put_crm_connection_id_deal_id](docs/sdks/deal/README.md#put_crm_connection_id_deal_id) - Update a deal

### [Document](docs/sdks/document/README.md)

* [delete_ats_connection_id_scorecard_id](docs/sdks/document/README.md#delete_ats_connection_id_scorecard_id) - Remove a scorecard
* [get_ats_connection_id_scorecard](docs/sdks/document/README.md#get_ats_connection_id_scorecard) - List all scorecards
* [get_ats_connection_id_scorecard_id](docs/sdks/document/README.md#get_ats_connection_id_scorecard_id) - Retrieve a scorecard
* [patch_ats_connection_id_scorecard_id](docs/sdks/document/README.md#patch_ats_connection_id_scorecard_id) - Update a scorecard
* [post_ats_connection_id_scorecard](docs/sdks/document/README.md#post_ats_connection_id_scorecard) - Create a scorecard
* [put_ats_connection_id_scorecard_id](docs/sdks/document/README.md#put_ats_connection_id_scorecard_id) - Update a scorecard

### [Employee](docs/sdks/employee/README.md)

* [delete_hris_connection_id_employee_id](docs/sdks/employee/README.md#delete_hris_connection_id_employee_id) - Remove a Employee
* [get_hris_connection_id_employee](docs/sdks/employee/README.md#get_hris_connection_id_employee) - List all Employees
* [get_hris_connection_id_employee_id](docs/sdks/employee/README.md#get_hris_connection_id_employee_id) - Retrieve a Employee
* [patch_hris_connection_id_employee_id](docs/sdks/employee/README.md#patch_hris_connection_id_employee_id) - Update a Employee
* [post_hris_connection_id_employee](docs/sdks/employee/README.md#post_hris_connection_id_employee) - Create a Employee
* [put_hris_connection_id_employee_id](docs/sdks/employee/README.md#put_hris_connection_id_employee_id) - Update a Employee

### [Enrich](docs/sdks/enrich/README.md)

* [get_enrich_connection_id_company](docs/sdks/enrich/README.md#get_enrich_connection_id_company) - Retrieve enrichment information for a company
* [get_enrich_connection_id_person](docs/sdks/enrich/README.md#get_enrich_connection_id_person) - Retrieve enrichment information for a person

### [Event](docs/sdks/event/README.md)

* [delete_crm_connection_id_event_id](docs/sdks/event/README.md#delete_crm_connection_id_event_id) - Remove a event
* [delete_crm_connection_id_event_id_company_company_id](docs/sdks/event/README.md#delete_crm_connection_id_event_id_company_company_id) - Remove company association from an event
* [delete_crm_connection_id_event_id_contact_contact_id](docs/sdks/event/README.md#delete_crm_connection_id_event_id_contact_contact_id) - Remove contact association from an event
* [delete_crm_connection_id_event_id_deal_deal_id](docs/sdks/event/README.md#delete_crm_connection_id_event_id_deal_deal_id) - Remove deal association from an event
* [get_crm_connection_id_event](docs/sdks/event/README.md#get_crm_connection_id_event) - List all events
* [get_crm_connection_id_event_id](docs/sdks/event/README.md#get_crm_connection_id_event_id) - Retrieve a event
* [patch_crm_connection_id_event_id](docs/sdks/event/README.md#patch_crm_connection_id_event_id) - Update a event
* [patch_crm_connection_id_event_id_company_company_id](docs/sdks/event/README.md#patch_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [patch_crm_connection_id_event_id_contact_contact_id](docs/sdks/event/README.md#patch_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [patch_crm_connection_id_event_id_deal_deal_id](docs/sdks/event/README.md#patch_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event
* [post_crm_connection_id_event](docs/sdks/event/README.md#post_crm_connection_id_event) - Create a event
* [put_crm_connection_id_event_id](docs/sdks/event/README.md#put_crm_connection_id_event_id) - Update a event
* [put_crm_connection_id_event_id_company_company_id](docs/sdks/event/README.md#put_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [put_crm_connection_id_event_id_contact_contact_id](docs/sdks/event/README.md#put_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [put_crm_connection_id_event_id_deal_deal_id](docs/sdks/event/README.md#put_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event

### [File](docs/sdks/file/README.md)

* [delete_crm_connection_id_file_id](docs/sdks/file/README.md#delete_crm_connection_id_file_id) - Remove a file
* [get_crm_connection_id_file](docs/sdks/file/README.md#get_crm_connection_id_file) - List all files
* [get_crm_connection_id_file_id](docs/sdks/file/README.md#get_crm_connection_id_file_id) - Retrieve a file
* [patch_crm_connection_id_file_id](docs/sdks/file/README.md#patch_crm_connection_id_file_id) - Update a file
* [post_crm_connection_id_file](docs/sdks/file/README.md#post_crm_connection_id_file) - Create a file
* [put_crm_connection_id_file_id](docs/sdks/file/README.md#put_crm_connection_id_file_id) - Update a file

### [Group](docs/sdks/group/README.md)

* [delete_hris_connection_id_group_id](docs/sdks/group/README.md#delete_hris_connection_id_group_id) - Remove a Group
* [get_hris_connection_id_group](docs/sdks/group/README.md#get_hris_connection_id_group) - List all Groups
* [get_hris_connection_id_group_id](docs/sdks/group/README.md#get_hris_connection_id_group_id) - Retrieve a Group
* [patch_hris_connection_id_group_id](docs/sdks/group/README.md#patch_hris_connection_id_group_id) - Update a Group
* [post_hris_connection_id_group](docs/sdks/group/README.md#post_hris_connection_id_group) - Create a Group
* [put_hris_connection_id_group_id](docs/sdks/group/README.md#put_hris_connection_id_group_id) - Update a Group

### [Hris](docs/sdks/hris/README.md)

* [delete_hris_connection_id_employee_id](docs/sdks/hris/README.md#delete_hris_connection_id_employee_id) - Remove a Employee
* [delete_hris_connection_id_group_id](docs/sdks/hris/README.md#delete_hris_connection_id_group_id) - Remove a Group
* [get_hris_connection_id_employee](docs/sdks/hris/README.md#get_hris_connection_id_employee) - List all Employees
* [get_hris_connection_id_employee_id](docs/sdks/hris/README.md#get_hris_connection_id_employee_id) - Retrieve a Employee
* [get_hris_connection_id_group](docs/sdks/hris/README.md#get_hris_connection_id_group) - List all Groups
* [get_hris_connection_id_group_id](docs/sdks/hris/README.md#get_hris_connection_id_group_id) - Retrieve a Group
* [patch_hris_connection_id_employee_id](docs/sdks/hris/README.md#patch_hris_connection_id_employee_id) - Update a Employee
* [patch_hris_connection_id_group_id](docs/sdks/hris/README.md#patch_hris_connection_id_group_id) - Update a Group
* [post_hris_connection_id_employee](docs/sdks/hris/README.md#post_hris_connection_id_employee) - Create a Employee
* [post_hris_connection_id_group](docs/sdks/hris/README.md#post_hris_connection_id_group) - Create a Group
* [put_hris_connection_id_employee_id](docs/sdks/hris/README.md#put_hris_connection_id_employee_id) - Update a Employee
* [put_hris_connection_id_group_id](docs/sdks/hris/README.md#put_hris_connection_id_group_id) - Update a Group

### [Integration](docs/sdks/integration/README.md)

* [get_unified_integration](docs/sdks/integration/README.md#get_unified_integration) - Returns all integrations
* [get_unified_integration_auth_workspace_id_integration_type](docs/sdks/integration/README.md#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_integration_type](docs/sdks/integration/README.md#get_unified_integration_integration_type) - Retrieve an integration
* [get_unified_integration_workspace_workspace_id](docs/sdks/integration/README.md#get_unified_integration_workspace_workspace_id) - Returns all activated integrations in a workspace

### [Interview](docs/sdks/interview/README.md)

* [delete_ats_connection_id_interview_id](docs/sdks/interview/README.md#delete_ats_connection_id_interview_id) - Remove a interview
* [get_ats_connection_id_interview](docs/sdks/interview/README.md#get_ats_connection_id_interview) - List all interviews
* [get_ats_connection_id_interview_id](docs/sdks/interview/README.md#get_ats_connection_id_interview_id) - Retrieve a interview
* [patch_ats_connection_id_interview_id](docs/sdks/interview/README.md#patch_ats_connection_id_interview_id) - Update a interview
* [post_ats_connection_id_interview](docs/sdks/interview/README.md#post_ats_connection_id_interview) - Create a interview
* [put_ats_connection_id_interview_id](docs/sdks/interview/README.md#put_ats_connection_id_interview_id) - Update a interview

### [Job](docs/sdks/job/README.md)

* [delete_ats_connection_id_job_id](docs/sdks/job/README.md#delete_ats_connection_id_job_id) - Remove a job
* [get_ats_connection_id_job](docs/sdks/job/README.md#get_ats_connection_id_job) - List all jobs
* [get_ats_connection_id_job_id](docs/sdks/job/README.md#get_ats_connection_id_job_id) - Retrieve a job
* [patch_ats_connection_id_job_id](docs/sdks/job/README.md#patch_ats_connection_id_job_id) - Update a job
* [post_ats_connection_id_job](docs/sdks/job/README.md#post_ats_connection_id_job) - Create a job
* [put_ats_connection_id_job_id](docs/sdks/job/README.md#put_ats_connection_id_job_id) - Update a job

### [Lead](docs/sdks/lead/README.md)

* [delete_crm_connection_id_lead_id](docs/sdks/lead/README.md#delete_crm_connection_id_lead_id) - Remove a lead
* [get_crm_connection_id_lead](docs/sdks/lead/README.md#get_crm_connection_id_lead) - List all leads
* [get_crm_connection_id_lead_id](docs/sdks/lead/README.md#get_crm_connection_id_lead_id) - Retrieve a lead
* [patch_crm_connection_id_lead_id](docs/sdks/lead/README.md#patch_crm_connection_id_lead_id) - Update a lead
* [post_crm_connection_id_lead](docs/sdks/lead/README.md#post_crm_connection_id_lead) - Create a lead
* [put_crm_connection_id_lead_id](docs/sdks/lead/README.md#put_crm_connection_id_lead_id) - Update a lead

### [List](docs/sdks/list/README.md)

* [delete_martech_connection_id_list_id](docs/sdks/list/README.md#delete_martech_connection_id_list_id) - Remove a list
* [get_martech_connection_id_list](docs/sdks/list/README.md#get_martech_connection_id_list) - List all lists
* [get_martech_connection_id_list_id](docs/sdks/list/README.md#get_martech_connection_id_list_id) - Retrieve a list
* [patch_martech_connection_id_list_id](docs/sdks/list/README.md#patch_martech_connection_id_list_id) - Update a list
* [post_martech_connection_id_list](docs/sdks/list/README.md#post_martech_connection_id_list) - Create a list
* [put_martech_connection_id_list_id](docs/sdks/list/README.md#put_martech_connection_id_list_id) - Update a list

### [Login](docs/sdks/login/README.md)

* [get_unified_integration_login_workspace_id_integration_type](docs/sdks/login/README.md#get_unified_integration_login_workspace_id_integration_type) - Sign in a user

### [Martech](docs/sdks/martech/README.md)

* [delete_martech_connection_id_list_id](docs/sdks/martech/README.md#delete_martech_connection_id_list_id) - Remove a list
* [delete_martech_connection_id_list_id_member_id](docs/sdks/martech/README.md#delete_martech_connection_id_list_id_member_id) - Remove member from a list
* [get_martech_connection_id_list](docs/sdks/martech/README.md#get_martech_connection_id_list) - List all lists
* [get_martech_connection_id_list_id](docs/sdks/martech/README.md#get_martech_connection_id_list_id) - Retrieve a list
* [get_martech_connection_id_list_id_member](docs/sdks/martech/README.md#get_martech_connection_id_list_id_member) - List all members in a list
* [get_martech_connection_id_list_id_member_id](docs/sdks/martech/README.md#get_martech_connection_id_list_id_member_id) - Retrieve a member from a list
* [patch_martech_connection_id_list_id](docs/sdks/martech/README.md#patch_martech_connection_id_list_id) - Update a list
* [patch_martech_connection_id_list_id_member_id](docs/sdks/martech/README.md#patch_martech_connection_id_list_id_member_id) - Update a member in a list
* [post_martech_connection_id_list](docs/sdks/martech/README.md#post_martech_connection_id_list) - Create a list
* [post_martech_connection_id_list_id_member](docs/sdks/martech/README.md#post_martech_connection_id_list_id_member) - Create a member in a list
* [put_martech_connection_id_list_id](docs/sdks/martech/README.md#put_martech_connection_id_list_id) - Update a list
* [put_martech_connection_id_list_id_member_id](docs/sdks/martech/README.md#put_martech_connection_id_list_id_member_id) - Update a member in a list

### [Member](docs/sdks/member/README.md)

* [delete_martech_connection_id_list_id_member_id](docs/sdks/member/README.md#delete_martech_connection_id_list_id_member_id) - Remove member from a list
* [get_martech_connection_id_list_id_member](docs/sdks/member/README.md#get_martech_connection_id_list_id_member) - List all members in a list
* [get_martech_connection_id_list_id_member_id](docs/sdks/member/README.md#get_martech_connection_id_list_id_member_id) - Retrieve a member from a list
* [patch_martech_connection_id_list_id_member_id](docs/sdks/member/README.md#patch_martech_connection_id_list_id_member_id) - Update a member in a list
* [post_martech_connection_id_list_id_member](docs/sdks/member/README.md#post_martech_connection_id_list_id_member) - Create a member in a list
* [put_martech_connection_id_list_id_member_id](docs/sdks/member/README.md#put_martech_connection_id_list_id_member_id) - Update a member in a list

### [Note](docs/sdks/note/README.md)

* [delete_ticketing_connection_id_notes_ticket_id_id](docs/sdks/note/README.md#delete_ticketing_connection_id_notes_ticket_id_id) - Remove a note
* [get_ticketing_connection_id_notes_ticket_id](docs/sdks/note/README.md#get_ticketing_connection_id_notes_ticket_id) - List all notes
* [get_ticketing_connection_id_notes_ticket_id_id](docs/sdks/note/README.md#get_ticketing_connection_id_notes_ticket_id_id) - Retrieve a note
* [patch_ticketing_connection_id_notes_ticket_id_id](docs/sdks/note/README.md#patch_ticketing_connection_id_notes_ticket_id_id) - Update a note
* [post_ticketing_connection_id_notes_ticket_id](docs/sdks/note/README.md#post_ticketing_connection_id_notes_ticket_id) - Create a note
* [put_ticketing_connection_id_notes_ticket_id_id](docs/sdks/note/README.md#put_ticketing_connection_id_notes_ticket_id_id) - Update a note

### [Passthrough](docs/sdks/passthrough/README.md)

* [delete_passthrough_connection_id_path](docs/sdks/passthrough/README.md#delete_passthrough_connection_id_path) - Passthrough DELETE
* [get_passthrough_connection_id_path](docs/sdks/passthrough/README.md#get_passthrough_connection_id_path) - Passthrough GET
* [patch_passthrough_connection_id_path](docs/sdks/passthrough/README.md#patch_passthrough_connection_id_path) - Passthrough PUT
* [post_passthrough_connection_id_path](docs/sdks/passthrough/README.md#post_passthrough_connection_id_path) - Passthrough POST
* [put_passthrough_connection_id_path](docs/sdks/passthrough/README.md#put_passthrough_connection_id_path) - Passthrough PUT

### [Person](docs/sdks/person/README.md)

* [get_enrich_connection_id_person](docs/sdks/person/README.md#get_enrich_connection_id_person) - Retrieve enrichment information for a person

### [Pipeline](docs/sdks/pipeline/README.md)

* [delete_crm_connection_id_pipeline_id](docs/sdks/pipeline/README.md#delete_crm_connection_id_pipeline_id) - Remove a pipeline
* [get_crm_connection_id_pipeline](docs/sdks/pipeline/README.md#get_crm_connection_id_pipeline) - List all pipelines
* [get_crm_connection_id_pipeline_id](docs/sdks/pipeline/README.md#get_crm_connection_id_pipeline_id) - Retrieve a pipeline
* [patch_crm_connection_id_pipeline_id](docs/sdks/pipeline/README.md#patch_crm_connection_id_pipeline_id) - Update a pipeline
* [post_crm_connection_id_pipeline](docs/sdks/pipeline/README.md#post_crm_connection_id_pipeline) - Create a pipeline
* [put_crm_connection_id_pipeline_id](docs/sdks/pipeline/README.md#put_crm_connection_id_pipeline_id) - Update a pipeline

### [Team](docs/sdks/team/README.md)

* [delete_crm_connection_id_team_id](docs/sdks/team/README.md#delete_crm_connection_id_team_id) - Remove a team
* [get_crm_connection_id_team](docs/sdks/team/README.md#get_crm_connection_id_team) - List all teams
* [get_crm_connection_id_team_id](docs/sdks/team/README.md#get_crm_connection_id_team_id) - Retrieve a team
* [patch_crm_connection_id_team_id](docs/sdks/team/README.md#patch_crm_connection_id_team_id) - Update a team
* [post_crm_connection_id_team](docs/sdks/team/README.md#post_crm_connection_id_team) - Create a team
* [put_crm_connection_id_team_id](docs/sdks/team/README.md#put_crm_connection_id_team_id) - Update a team

### [Ticket](docs/sdks/ticket/README.md)

* [delete_ticketing_connection_id_ticket_id](docs/sdks/ticket/README.md#delete_ticketing_connection_id_ticket_id) - Remove a ticket
* [get_ticketing_connection_id_ticket](docs/sdks/ticket/README.md#get_ticketing_connection_id_ticket) - List all tickets
* [get_ticketing_connection_id_ticket_id](docs/sdks/ticket/README.md#get_ticketing_connection_id_ticket_id) - Retrieve a ticket
* [patch_ticketing_connection_id_ticket_id](docs/sdks/ticket/README.md#patch_ticketing_connection_id_ticket_id) - Update a ticket
* [post_ticketing_connection_id_ticket](docs/sdks/ticket/README.md#post_ticketing_connection_id_ticket) - Create a ticket
* [put_ticketing_connection_id_ticket_id](docs/sdks/ticket/README.md#put_ticketing_connection_id_ticket_id) - Update a ticket

### [Ticketing](docs/sdks/ticketing/README.md)

* [delete_ticketing_connection_id_agent_id](docs/sdks/ticketing/README.md#delete_ticketing_connection_id_agent_id) - Remove a agent
* [delete_ticketing_connection_id_customer_id](docs/sdks/ticketing/README.md#delete_ticketing_connection_id_customer_id) - Remove a customer
* [delete_ticketing_connection_id_notes_ticket_id_id](docs/sdks/ticketing/README.md#delete_ticketing_connection_id_notes_ticket_id_id) - Remove a note
* [delete_ticketing_connection_id_ticket_id](docs/sdks/ticketing/README.md#delete_ticketing_connection_id_ticket_id) - Remove a ticket
* [get_ticketing_connection_id_agent](docs/sdks/ticketing/README.md#get_ticketing_connection_id_agent) - List all agents
* [get_ticketing_connection_id_agent_id](docs/sdks/ticketing/README.md#get_ticketing_connection_id_agent_id) - Retrieve a agent
* [get_ticketing_connection_id_customer](docs/sdks/ticketing/README.md#get_ticketing_connection_id_customer) - List all customers
* [get_ticketing_connection_id_customer_id](docs/sdks/ticketing/README.md#get_ticketing_connection_id_customer_id) - Retrieve a customer
* [get_ticketing_connection_id_notes_ticket_id](docs/sdks/ticketing/README.md#get_ticketing_connection_id_notes_ticket_id) - List all notes
* [get_ticketing_connection_id_notes_ticket_id_id](docs/sdks/ticketing/README.md#get_ticketing_connection_id_notes_ticket_id_id) - Retrieve a note
* [get_ticketing_connection_id_ticket](docs/sdks/ticketing/README.md#get_ticketing_connection_id_ticket) - List all tickets
* [get_ticketing_connection_id_ticket_id](docs/sdks/ticketing/README.md#get_ticketing_connection_id_ticket_id) - Retrieve a ticket
* [patch_ticketing_connection_id_agent_id](docs/sdks/ticketing/README.md#patch_ticketing_connection_id_agent_id) - Update a agent
* [patch_ticketing_connection_id_customer_id](docs/sdks/ticketing/README.md#patch_ticketing_connection_id_customer_id) - Update a customer
* [patch_ticketing_connection_id_notes_ticket_id_id](docs/sdks/ticketing/README.md#patch_ticketing_connection_id_notes_ticket_id_id) - Update a note
* [patch_ticketing_connection_id_ticket_id](docs/sdks/ticketing/README.md#patch_ticketing_connection_id_ticket_id) - Update a ticket
* [post_ticketing_connection_id_agent](docs/sdks/ticketing/README.md#post_ticketing_connection_id_agent) - Create a agent
* [post_ticketing_connection_id_customer](docs/sdks/ticketing/README.md#post_ticketing_connection_id_customer) - Create a customer
* [post_ticketing_connection_id_notes_ticket_id](docs/sdks/ticketing/README.md#post_ticketing_connection_id_notes_ticket_id) - Create a note
* [post_ticketing_connection_id_ticket](docs/sdks/ticketing/README.md#post_ticketing_connection_id_ticket) - Create a ticket
* [put_ticketing_connection_id_agent_id](docs/sdks/ticketing/README.md#put_ticketing_connection_id_agent_id) - Update a agent
* [put_ticketing_connection_id_customer_id](docs/sdks/ticketing/README.md#put_ticketing_connection_id_customer_id) - Update a customer
* [put_ticketing_connection_id_notes_ticket_id_id](docs/sdks/ticketing/README.md#put_ticketing_connection_id_notes_ticket_id_id) - Update a note
* [put_ticketing_connection_id_ticket_id](docs/sdks/ticketing/README.md#put_ticketing_connection_id_ticket_id) - Update a ticket

### [Uc](docs/sdks/uc/README.md)

* [delete_uc_connection_id_contact_id](docs/sdks/uc/README.md#delete_uc_connection_id_contact_id) - Remove a contact
* [get_uc_connection_id_agent](docs/sdks/uc/README.md#get_uc_connection_id_agent) - List all agents
* [get_uc_connection_id_call](docs/sdks/uc/README.md#get_uc_connection_id_call) - List all calls
* [get_uc_connection_id_contact](docs/sdks/uc/README.md#get_uc_connection_id_contact) - List all contacts
* [get_uc_connection_id_contact_id](docs/sdks/uc/README.md#get_uc_connection_id_contact_id) - Retrieve a contact
* [patch_uc_connection_id_contact_id](docs/sdks/uc/README.md#patch_uc_connection_id_contact_id) - Update a contact
* [post_uc_connection_id_contact](docs/sdks/uc/README.md#post_uc_connection_id_contact) - Create a contact
* [put_uc_connection_id_contact_id](docs/sdks/uc/README.md#put_uc_connection_id_contact_id) - Update a contact

### [Unified](docs/sdks/unified/README.md)

* [delete_unified_connection_id](docs/sdks/unified/README.md#delete_unified_connection_id) - Remove connection
* [delete_unified_user](docs/sdks/unified/README.md#delete_unified_user) - Delete your user object
* [delete_unified_webhook_id](docs/sdks/unified/README.md#delete_unified_webhook_id) - Remove webhook subscription
* [get_unified_apicall](docs/sdks/unified/README.md#get_unified_apicall) - Returns API Calls
* [get_unified_apicall_id](docs/sdks/unified/README.md#get_unified_apicall_id) - Retrieve specific API Call by its ID
* [get_unified_connection](docs/sdks/unified/README.md#get_unified_connection) - List all connections
* [get_unified_connection_id](docs/sdks/unified/README.md#get_unified_connection_id) - Retrieve connection
* [get_unified_integration](docs/sdks/unified/README.md#get_unified_integration) - Returns all integrations
* [get_unified_integration_auth_workspace_id_integration_type](docs/sdks/unified/README.md#get_unified_integration_auth_workspace_id_integration_type) - Create connection indirectly
* [get_unified_integration_integration_type](docs/sdks/unified/README.md#get_unified_integration_integration_type) - Retrieve an integration
* [get_unified_integration_workspace_workspace_id](docs/sdks/unified/README.md#get_unified_integration_workspace_workspace_id) - Returns all activated integrations in a workspace
* [get_unified_user](docs/sdks/unified/README.md#get_unified_user) - Retrieve your user object
* [get_unified_user_token](docs/sdks/unified/README.md#get_unified_user_token) - Retrieve your user token
* [get_unified_webhook](docs/sdks/unified/README.md#get_unified_webhook) - Returns all registered webhooks
* [get_unified_webhook_id](docs/sdks/unified/README.md#get_unified_webhook_id) - Retrieve webhook by its ID
* [patch_unified_connection_id](docs/sdks/unified/README.md#patch_unified_connection_id) - Update connection
* [patch_unified_user](docs/sdks/unified/README.md#patch_unified_user) - Updates your user object
* [post_unified_connection](docs/sdks/unified/README.md#post_unified_connection) - Create connection
* [post_unified_webhook_connection_id_object](docs/sdks/unified/README.md#post_unified_webhook_connection_id_object) - Create webhook subscription
* [put_unified_connection_id](docs/sdks/unified/README.md#put_unified_connection_id) - Update connection
* [put_unified_user](docs/sdks/unified/README.md#put_unified_user) - Updates your user object

### [User](docs/sdks/user/README.md)

* [delete_crm_connection_id_user_id](docs/sdks/user/README.md#delete_crm_connection_id_user_id) - Remove a user
* [delete_unified_user](docs/sdks/user/README.md#delete_unified_user) - Delete your user object
* [get_crm_connection_id_user](docs/sdks/user/README.md#get_crm_connection_id_user) - List all users
* [get_crm_connection_id_user_id](docs/sdks/user/README.md#get_crm_connection_id_user_id) - Retrieve a user
* [get_unified_user](docs/sdks/user/README.md#get_unified_user) - Retrieve your user object
* [get_unified_user_token](docs/sdks/user/README.md#get_unified_user_token) - Retrieve your user token
* [patch_crm_connection_id_user_id](docs/sdks/user/README.md#patch_crm_connection_id_user_id) - Update a user
* [patch_unified_user](docs/sdks/user/README.md#patch_unified_user) - Updates your user object
* [post_crm_connection_id_user](docs/sdks/user/README.md#post_crm_connection_id_user) - Create a user
* [put_crm_connection_id_user_id](docs/sdks/user/README.md#put_crm_connection_id_user_id) - Update a user
* [put_unified_user](docs/sdks/user/README.md#put_unified_user) - Updates your user object

### [Webhook](docs/sdks/webhook/README.md)

* [delete_unified_webhook_id](docs/sdks/webhook/README.md#delete_unified_webhook_id) - Remove webhook subscription
* [get_unified_webhook](docs/sdks/webhook/README.md#get_unified_webhook) - Returns all registered webhooks
* [get_unified_webhook_id](docs/sdks/webhook/README.md#get_unified_webhook_id) - Retrieve webhook by its ID
* [post_unified_webhook_connection_id_object](docs/sdks/webhook/README.md#post_unified_webhook_connection_id_object) - Create webhook subscription
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
