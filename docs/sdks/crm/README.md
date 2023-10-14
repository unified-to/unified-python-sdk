# Crm
(*crm*)

### Available Operations

* [create_crm_company](#create_crm_company) - Create a company
* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_crm_deal](#create_crm_deal) - Create a deal
* [create_crm_event](#create_crm_event) - Create a event
* [create_crm_file](#create_crm_file) - Create a file
* [create_crm_lead](#create_crm_lead) - Create a lead
* [create_crm_pipeline](#create_crm_pipeline) - Create a pipeline
* [create_crm_team](#create_crm_team) - Create a team
* [create_crm_user](#create_crm_user) - Create a user
* [get_crm_company](#get_crm_company) - Retrieve a company
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_crm_deal](#get_crm_deal) - Retrieve a deal
* [get_crm_event](#get_crm_event) - Retrieve a event
* [get_crm_file](#get_crm_file) - Retrieve a file
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [get_crm_pipeline](#get_crm_pipeline) - Retrieve a pipeline
* [get_crm_team](#get_crm_team) - Retrieve a team
* [get_crm_user](#get_crm_user) - Retrieve a user
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_crm_deals](#list_crm_deals) - List all deals
* [list_crm_events](#list_crm_events) - List all events
* [list_crm_files](#list_crm_files) - List all files
* [list_crm_leads](#list_crm_leads) - List all leads
* [list_crm_pipelines](#list_crm_pipelines) - List all pipelines
* [list_crm_teams](#list_crm_teams) - List all teams
* [list_crm_users](#list_crm_users) - List all users
* [patch_crm_company](#patch_crm_company) - Update a company
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_crm_deal](#patch_crm_deal) - Update a deal
* [patch_crm_event](#patch_crm_event) - Update a event
* [patch_crm_file](#patch_crm_file) - Update a file
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [patch_crm_pipeline](#patch_crm_pipeline) - Update a pipeline
* [patch_crm_team](#patch_crm_team) - Update a team
* [patch_crm_user](#patch_crm_user) - Update a user
* [remove_crm_company](#remove_crm_company) - Remove a company
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_crm_deal](#remove_crm_deal) - Remove a deal
* [remove_crm_event](#remove_crm_event) - Remove a event
* [remove_crm_file](#remove_crm_file) - Remove a file
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [remove_crm_pipeline](#remove_crm_pipeline) - Remove a pipeline
* [remove_crm_team](#remove_crm_team) - Remove a team
* [remove_crm_user](#remove_crm_user) - Remove a user
* [update_crm_company](#update_crm_company) - Update a company
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_crm_deal](#update_crm_deal) - Update a deal
* [update_crm_event](#update_crm_event) - Update a event
* [update_crm_file](#update_crm_file) - Update a file
* [update_crm_lead](#update_crm_lead) - Update a lead
* [update_crm_pipeline](#update_crm_pipeline) - Update a pipeline
* [update_crm_team](#update_crm_team) - Update a team
* [update_crm_user](#update_crm_user) - Update a user

## create_crm_company

Create a company

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

req = operations.CreateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'connecting',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'carouse',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Germany',
            ),
        ],
        websites=[
            'yippee',
        ],
    ),
    connection_id='magenta Data woot',
    fields_=[
        'payment',
    ],
)

res = s.crm.create_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmCompanyRequest](../../models/operations/createcrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateCrmCompanyResponse](../../models/operations/createcrmcompanyresponse.md)**


## create_crm_contact

Create a contact

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

req = operations.CreateCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'Mendelevium',
        ],
        deal_ids=[
            'Account',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='towards',
            ),
        ],
    ),
    connection_id='Cambridgeshire Passenger Producer',
    fields_=[
        'Krypton',
    ],
)

res = s.crm.create_crm_contact(req)

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCrmContactRequest](../../models/operations/createcrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateCrmContactResponse](../../models/operations/createcrmcontactresponse.md)**


## create_crm_deal

Create a deal

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

req = operations.CreateCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'Toys',
        ],
    ),
    connection_id='Music Rap',
    fields_=[
        'wind',
    ],
)

res = s.crm.create_crm_deal(req)

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmDealRequest](../../models/operations/createcrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmDealResponse](../../models/operations/createcrmdealresponse.md)**


## create_crm_event

Create a event

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

req = operations.CreateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'repeatedly',
        ],
        contact_ids=[
            'Sedan',
        ],
        deal_ids=[
            'altruistic',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Hills',
            ],
            to=[
                'Bronze',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Savings',
    fields_=[
        'within',
    ],
)

res = s.crm.create_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**


## create_crm_file

Create a file

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

req = operations.CreateCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='ASCII Wooden the',
    fields_=[
        'Tungsten',
    ],
)

res = s.crm.create_crm_file(req)

if res.crm_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmFileRequest](../../models/operations/createcrmfilerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmFileResponse](../../models/operations/createcrmfileresponse.md)**


## create_crm_lead

Create a lead

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

req = operations.CreateCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='port steradian prize',
            ),
        ],
    ),
    connection_id='ability Einsteinium Orchestrator',
    fields_=[
        'orchid',
    ],
)

res = s.crm.create_crm_lead(req)

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmLeadRequest](../../models/operations/createcrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmLeadResponse](../../models/operations/createcrmleadresponse.md)**


## create_crm_pipeline

Create a pipeline

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

req = operations.CreateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='Paradigm Vista fuchsia',
    fields_=[
        'Hatchback',
    ],
)

res = s.crm.create_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**


## create_crm_team

Create a team

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

req = operations.CreateCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'exercitationem',
        ],
    ),
    connection_id='as New Senior',
    fields_=[
        'Buckinghamshire',
    ],
)

res = s.crm.create_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmTeamRequest](../../models/operations/createcrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmTeamResponse](../../models/operations/createcrmteamresponse.md)**


## create_crm_user

Create a user

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

req = operations.CreateCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='await male',
            ),
        ],
    ),
    connection_id='Incredible Virginia',
    fields_=[
        'Keyboard',
    ],
)

res = s.crm.create_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmUserRequest](../../models/operations/createcrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmUserResponse](../../models/operations/createcrmuserresponse.md)**


## get_crm_company

Retrieve a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmCompanyRequest(
    connection_id='THX Strategist deposit',
    fields_=[
        'snag',
    ],
    id='<ID>',
)

res = s.crm.get_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmCompanyRequest](../../models/operations/getcrmcompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetCrmCompanyResponse](../../models/operations/getcrmcompanyresponse.md)**


## get_crm_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmContactRequest(
    connection_id='Oregon',
    fields_=[
        'methodology',
    ],
    id='<ID>',
)

res = s.crm.get_crm_contact(req)

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCrmContactRequest](../../models/operations/getcrmcontactrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetCrmContactResponse](../../models/operations/getcrmcontactresponse.md)**


## get_crm_deal

Retrieve a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmDealRequest(
    connection_id='male orange',
    fields_=[
        'Reduced',
    ],
    id='<ID>',
)

res = s.crm.get_crm_deal(req)

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmDealRequest](../../models/operations/getcrmdealrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmDealResponse](../../models/operations/getcrmdealresponse.md)**


## get_crm_event

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmEventRequest(
    connection_id='Metal South blockchains',
    fields_=[
        'comics',
    ],
    id='<ID>',
)

res = s.crm.get_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**


## get_crm_file

Retrieve a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmFileRequest(
    connection_id='ease',
    fields_=[
        'bypassing',
    ],
    id='<ID>',
)

res = s.crm.get_crm_file(req)

if res.crm_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmFileRequest](../../models/operations/getcrmfilerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmFileResponse](../../models/operations/getcrmfileresponse.md)**


## get_crm_lead

Retrieve a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmLeadRequest(
    connection_id='Handmade Keyboard yum',
    fields_=[
        'magnetic',
    ],
    id='<ID>',
)

res = s.crm.get_crm_lead(req)

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmLeadRequest](../../models/operations/getcrmleadrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmLeadResponse](../../models/operations/getcrmleadresponse.md)**


## get_crm_pipeline

Retrieve a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmPipelineRequest(
    connection_id='withdrawal Southeast',
    fields_=[
        'evolve',
    ],
    id='<ID>',
)

res = s.crm.get_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**


## get_crm_team

Retrieve a team

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmTeamRequest(
    connection_id='digital awful',
    fields_=[
        'Peru',
    ],
    id='<ID>',
)

res = s.crm.get_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmTeamRequest](../../models/operations/getcrmteamrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmTeamResponse](../../models/operations/getcrmteamresponse.md)**


## get_crm_user

Retrieve a user

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmUserRequest(
    connection_id='Bespoke Dollar',
    fields_=[
        'unto',
    ],
    id='<ID>',
)

res = s.crm.get_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmUserRequest](../../models/operations/getcrmuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmUserResponse](../../models/operations/getcrmuserresponse.md)**


## list_crm_companies

List all companies

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

req = operations.ListCrmCompaniesRequest(
    connection_id='Jazz solid Lamborghini',
    fields_=[
        'Sleek',
    ],
)

res = s.crm.list_crm_companies(req)

if res.crm_companies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmCompaniesRequest](../../models/operations/listcrmcompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCrmCompaniesResponse](../../models/operations/listcrmcompaniesresponse.md)**


## list_crm_contacts

List all contacts

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

req = operations.ListCrmContactsRequest(
    connection_id='Awesome index steradian',
    fields_=[
        'District',
    ],
)

res = s.crm.list_crm_contacts(req)

if res.crm_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCrmContactsRequest](../../models/operations/listcrmcontactsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListCrmContactsResponse](../../models/operations/listcrmcontactsresponse.md)**


## list_crm_deals

List all deals

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

req = operations.ListCrmDealsRequest(
    connection_id='Lamborghini',
    fields_=[
        'female',
    ],
)

res = s.crm.list_crm_deals(req)

if res.crm_deals is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmDealsRequest](../../models/operations/listcrmdealsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmDealsResponse](../../models/operations/listcrmdealsresponse.md)**


## list_crm_events

List all events

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

req = operations.ListCrmEventsRequest(
    connection_id='invoice gratefully',
    fields_=[
        'impactful',
    ],
)

res = s.crm.list_crm_events(req)

if res.crm_events is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**


## list_crm_files

List all files

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

req = operations.ListCrmFilesRequest(
    connection_id='lavender Genderflux Southeast',
    fields_=[
        'invoice',
    ],
)

res = s.crm.list_crm_files(req)

if res.crm_files is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmFilesRequest](../../models/operations/listcrmfilesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmFilesResponse](../../models/operations/listcrmfilesresponse.md)**


## list_crm_leads

List all leads

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

req = operations.ListCrmLeadsRequest(
    connection_id='International',
    fields_=[
        'ratione',
    ],
)

res = s.crm.list_crm_leads(req)

if res.crm_leads is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmLeadsRequest](../../models/operations/listcrmleadsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmLeadsResponse](../../models/operations/listcrmleadsresponse.md)**


## list_crm_pipelines

List all pipelines

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

req = operations.ListCrmPipelinesRequest(
    connection_id='primary',
    fields_=[
        'female',
    ],
)

res = s.crm.list_crm_pipelines(req)

if res.crm_pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**


## list_crm_teams

List all teams

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

req = operations.ListCrmTeamsRequest(
    connection_id='Classical microchip Wooden',
    fields_=[
        'Lutetium',
    ],
)

res = s.crm.list_crm_teams(req)

if res.crm_teams is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmTeamsRequest](../../models/operations/listcrmteamsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmTeamsResponse](../../models/operations/listcrmteamsresponse.md)**


## list_crm_users

List all users

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

req = operations.ListCrmUsersRequest(
    connection_id='careless Costa',
    fields_=[
        'olive',
    ],
)

res = s.crm.list_crm_users(req)

if res.crm_users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmUsersRequest](../../models/operations/listcrmusersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmUsersResponse](../../models/operations/listcrmusersresponse.md)**


## patch_crm_company

Update a company

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

req = operations.PatchCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Producer',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'Corporate',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='haptic Phased',
            ),
        ],
        websites=[
            'Investment',
        ],
    ),
    connection_id='Trans',
    fields_=[
        'Money',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmCompanyRequest](../../models/operations/patchcrmcompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchCrmCompanyResponse](../../models/operations/patchcrmcompanyresponse.md)**


## patch_crm_contact

Update a contact

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

req = operations.PatchCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'architecture',
        ],
        deal_ids=[
            'Buckinghamshire',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Practical',
            ),
        ],
    ),
    connection_id='Future Diesel',
    fields_=[
        'syndicate',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_contact(req)

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCrmContactRequest](../../models/operations/patchcrmcontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchCrmContactResponse](../../models/operations/patchcrmcontactresponse.md)**


## patch_crm_deal

Update a deal

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

req = operations.PatchCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'consign',
        ],
    ),
    connection_id='Platinum female',
    fields_=[
        'Berkshire',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_deal(req)

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmDealRequest](../../models/operations/patchcrmdealrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmDealResponse](../../models/operations/patchcrmdealresponse.md)**


## patch_crm_event

Update a event

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

req = operations.PatchCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'XML',
        ],
        contact_ids=[
            'Accountability',
        ],
        deal_ids=[
            'copying',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'after',
            ],
            to=[
                'Research',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='female',
    fields_=[
        'Connecticut',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**


## patch_crm_file

Update a file

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

req = operations.PatchCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='bluetooth',
    fields_=[
        'Bronze',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_file(req)

if res.crm_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmFileRequest](../../models/operations/patchcrmfilerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmFileResponse](../../models/operations/patchcrmfileresponse.md)**


## patch_crm_lead

Update a lead

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

req = operations.PatchCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='teal Hat',
            ),
        ],
    ),
    connection_id='Ball Chips',
    fields_=[
        'Southwest',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_lead(req)

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmLeadRequest](../../models/operations/patchcrmleadrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmLeadResponse](../../models/operations/patchcrmleadresponse.md)**


## patch_crm_pipeline

Update a pipeline

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

req = operations.PatchCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='imperfect Costa Southwest',
    fields_=[
        'excluding',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**


## patch_crm_team

Update a team

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

req = operations.PatchCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Account',
        ],
    ),
    connection_id='Transexual compress redefine',
    fields_=[
        'gold',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmTeamRequest](../../models/operations/patchcrmteamrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmTeamResponse](../../models/operations/patchcrmteamresponse.md)**


## patch_crm_user

Update a user

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

req = operations.PatchCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Bronze composite',
            ),
        ],
    ),
    connection_id='katal Industrial Classical',
    fields_=[
        'boo',
    ],
    id='<ID>',
)

res = s.crm.patch_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmUserRequest](../../models/operations/patchcrmuserrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmUserResponse](../../models/operations/patchcrmuserresponse.md)**


## remove_crm_company

Remove a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmCompanyRequest(
    connection_id='Mayaguez index wireless',
    id='<ID>',
)

res = s.crm.remove_crm_company(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCrmCompanyRequest](../../models/operations/removecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveCrmCompanyResponse](../../models/operations/removecrmcompanyresponse.md)**


## remove_crm_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmContactRequest(
    connection_id='Folk granular Concrete',
    id='<ID>',
)

res = s.crm.remove_crm_contact(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCrmContactRequest](../../models/operations/removecrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveCrmContactResponse](../../models/operations/removecrmcontactresponse.md)**


## remove_crm_deal

Remove a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmDealRequest(
    connection_id='Nihonium',
    id='<ID>',
)

res = s.crm.remove_crm_deal(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmDealRequest](../../models/operations/removecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmDealResponse](../../models/operations/removecrmdealresponse.md)**


## remove_crm_event

Remove a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmEventRequest(
    connection_id='card',
    id='<ID>',
)

res = s.crm.remove_crm_event(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**


## remove_crm_file

Remove a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmFileRequest(
    connection_id='cash',
    id='<ID>',
)

res = s.crm.remove_crm_file(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmFileRequest](../../models/operations/removecrmfilerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmFileResponse](../../models/operations/removecrmfileresponse.md)**


## remove_crm_lead

Remove a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmLeadRequest(
    connection_id='Southeast',
    id='<ID>',
)

res = s.crm.remove_crm_lead(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmLeadRequest](../../models/operations/removecrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmLeadResponse](../../models/operations/removecrmleadresponse.md)**


## remove_crm_pipeline

Remove a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmPipelineRequest(
    connection_id='Hybrid merrily',
    id='<ID>',
)

res = s.crm.remove_crm_pipeline(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**


## remove_crm_team

Remove a team

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmTeamRequest(
    connection_id='Sol',
    id='<ID>',
)

res = s.crm.remove_crm_team(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmTeamRequest](../../models/operations/removecrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmTeamResponse](../../models/operations/removecrmteamresponse.md)**


## remove_crm_user

Remove a user

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmUserRequest(
    connection_id='Southeast',
    id='<ID>',
)

res = s.crm.remove_crm_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmUserRequest](../../models/operations/removecrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmUserResponse](../../models/operations/removecrmuserresponse.md)**


## update_crm_company

Update a company

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

req = operations.UpdateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'SMS',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'barrel',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Account alarm infrastructure',
            ),
        ],
        websites=[
            'Visionary',
        ],
    ),
    connection_id='Southeast ad',
    fields_=[
        'Practical',
    ],
    id='<ID>',
)

res = s.crm.update_crm_company(req)

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmCompanyRequest](../../models/operations/updatecrmcompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateCrmCompanyResponse](../../models/operations/updatecrmcompanyresponse.md)**


## update_crm_contact

Update a contact

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

req = operations.UpdateCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'Universal',
        ],
        deal_ids=[
            'Harbors',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Analyst Des green',
            ),
        ],
    ),
    connection_id='man panel',
    fields_=[
        'Mauritania',
    ],
    id='<ID>',
)

res = s.crm.update_crm_contact(req)

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCrmContactRequest](../../models/operations/updatecrmcontactrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateCrmContactResponse](../../models/operations/updatecrmcontactresponse.md)**


## update_crm_deal

Update a deal

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

req = operations.UpdateCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'South',
        ],
    ),
    connection_id='Shirt',
    fields_=[
        'whiteboard',
    ],
    id='<ID>',
)

res = s.crm.update_crm_deal(req)

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmDealRequest](../../models/operations/updatecrmdealrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmDealResponse](../../models/operations/updatecrmdealresponse.md)**


## update_crm_event

Update a event

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

req = operations.UpdateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'Account',
        ],
        contact_ids=[
            'DRAM',
        ],
        deal_ids=[
            'input',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Bicycle',
            ],
            to=[
                'Wagon',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Accountability',
    fields_=[
        'Manager',
    ],
    id='<ID>',
)

res = s.crm.update_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**


## update_crm_file

Update a file

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

req = operations.UpdateCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='Orchestrator',
    fields_=[
        'male',
    ],
    id='<ID>',
)

res = s.crm.update_crm_file(req)

if res.crm_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmFileRequest](../../models/operations/updatecrmfilerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmFileResponse](../../models/operations/updatecrmfileresponse.md)**


## update_crm_lead

Update a lead

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

req = operations.UpdateCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='compelling',
            ),
        ],
    ),
    connection_id='Pickup Polestar Checking',
    fields_=[
        'Concrete',
    ],
    id='<ID>',
)

res = s.crm.update_crm_lead(req)

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmLeadRequest](../../models/operations/updatecrmleadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmLeadResponse](../../models/operations/updatecrmleadresponse.md)**


## update_crm_pipeline

Update a pipeline

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

req = operations.UpdateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='needily',
    fields_=[
        'Androgyne',
    ],
    id='<ID>',
)

res = s.crm.update_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**


## update_crm_team

Update a team

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

req = operations.UpdateCrmTeamRequest(
    crm_team=shared.CrmTeam(
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Carbon',
        ],
    ),
    connection_id='Dakota',
    fields_=[
        'female',
    ],
    id='<ID>',
)

res = s.crm.update_crm_team(req)

if res.crm_team is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmTeamRequest](../../models/operations/updatecrmteamrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmTeamResponse](../../models/operations/updatecrmteamresponse.md)**


## update_crm_user

Update a user

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

req = operations.UpdateCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Idaho green',
            ),
        ],
    ),
    connection_id='Savings',
    fields_=[
        'Corwin',
    ],
    id='<ID>',
)

res = s.crm.update_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmUserRequest](../../models/operations/updatecrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmUserResponse](../../models/operations/updatecrmuserresponse.md)**

