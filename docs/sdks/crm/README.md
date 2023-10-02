# Crm
(*crm*)

### Available Operations

* [delete_crm_connection_id_company_id](#delete_crm_connection_id_company_id) - Remove a company
* [delete_crm_connection_id_contact_id](#delete_crm_connection_id_contact_id) - Remove a contact
* [delete_crm_connection_id_deal_id](#delete_crm_connection_id_deal_id) - Remove a deal
* [delete_crm_connection_id_event_id](#delete_crm_connection_id_event_id) - Remove a event
* [delete_crm_connection_id_file_id](#delete_crm_connection_id_file_id) - Remove a file
* [delete_crm_connection_id_lead_id](#delete_crm_connection_id_lead_id) - Remove a lead
* [delete_crm_connection_id_pipeline_id](#delete_crm_connection_id_pipeline_id) - Remove a pipeline
* [delete_crm_connection_id_team_id](#delete_crm_connection_id_team_id) - Remove a team
* [delete_crm_connection_id_user_id](#delete_crm_connection_id_user_id) - Remove a user
* [get_crm_connection_id_company](#get_crm_connection_id_company) - List all companies
* [get_crm_connection_id_company_id](#get_crm_connection_id_company_id) - Retrieve a company
* [get_crm_connection_id_contact](#get_crm_connection_id_contact) - List all contacts
* [get_crm_connection_id_contact_id](#get_crm_connection_id_contact_id) - Retrieve a contact
* [get_crm_connection_id_deal](#get_crm_connection_id_deal) - List all deals
* [get_crm_connection_id_deal_id](#get_crm_connection_id_deal_id) - Retrieve a deal
* [get_crm_connection_id_event](#get_crm_connection_id_event) - List all events
* [get_crm_connection_id_event_id](#get_crm_connection_id_event_id) - Retrieve a event
* [get_crm_connection_id_file](#get_crm_connection_id_file) - List all files
* [get_crm_connection_id_file_id](#get_crm_connection_id_file_id) - Retrieve a file
* [get_crm_connection_id_lead](#get_crm_connection_id_lead) - List all leads
* [get_crm_connection_id_lead_id](#get_crm_connection_id_lead_id) - Retrieve a lead
* [get_crm_connection_id_pipeline](#get_crm_connection_id_pipeline) - List all pipelines
* [get_crm_connection_id_pipeline_id](#get_crm_connection_id_pipeline_id) - Retrieve a pipeline
* [get_crm_connection_id_team](#get_crm_connection_id_team) - List all teams
* [get_crm_connection_id_team_id](#get_crm_connection_id_team_id) - Retrieve a team
* [get_crm_connection_id_user](#get_crm_connection_id_user) - List all users
* [get_crm_connection_id_user_id](#get_crm_connection_id_user_id) - Retrieve a user
* [patch_crm_connection_id_company_id](#patch_crm_connection_id_company_id) - Update a company
* [patch_crm_connection_id_contact_id](#patch_crm_connection_id_contact_id) - Update a contact
* [patch_crm_connection_id_deal_id](#patch_crm_connection_id_deal_id) - Update a deal
* [patch_crm_connection_id_event_id](#patch_crm_connection_id_event_id) - Update a event
* [patch_crm_connection_id_file_id](#patch_crm_connection_id_file_id) - Update a file
* [patch_crm_connection_id_lead_id](#patch_crm_connection_id_lead_id) - Update a lead
* [patch_crm_connection_id_pipeline_id](#patch_crm_connection_id_pipeline_id) - Update a pipeline
* [patch_crm_connection_id_team_id](#patch_crm_connection_id_team_id) - Update a team
* [patch_crm_connection_id_user_id](#patch_crm_connection_id_user_id) - Update a user
* [post_crm_connection_id_company](#post_crm_connection_id_company) - Create a company
* [post_crm_connection_id_contact](#post_crm_connection_id_contact) - Create a contact
* [post_crm_connection_id_deal](#post_crm_connection_id_deal) - Create a deal
* [post_crm_connection_id_event](#post_crm_connection_id_event) - Create a event
* [post_crm_connection_id_file](#post_crm_connection_id_file) - Create a file
* [post_crm_connection_id_lead](#post_crm_connection_id_lead) - Create a lead
* [post_crm_connection_id_pipeline](#post_crm_connection_id_pipeline) - Create a pipeline
* [post_crm_connection_id_team](#post_crm_connection_id_team) - Create a team
* [post_crm_connection_id_user](#post_crm_connection_id_user) - Create a user
* [put_crm_connection_id_company_id](#put_crm_connection_id_company_id) - Update a company
* [put_crm_connection_id_contact_id](#put_crm_connection_id_contact_id) - Update a contact
* [put_crm_connection_id_deal_id](#put_crm_connection_id_deal_id) - Update a deal
* [put_crm_connection_id_event_id](#put_crm_connection_id_event_id) - Update a event
* [put_crm_connection_id_file_id](#put_crm_connection_id_file_id) - Update a file
* [put_crm_connection_id_lead_id](#put_crm_connection_id_lead_id) - Update a lead
* [put_crm_connection_id_pipeline_id](#put_crm_connection_id_pipeline_id) - Update a pipeline
* [put_crm_connection_id_team_id](#put_crm_connection_id_team_id) - Update a team
* [put_crm_connection_id_user_id](#put_crm_connection_id_user_id) - Update a user

## delete_crm_connection_id_company_id

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

req = operations.DeleteCrmConnectionIDCompanyIDRequest(
    connection_id='hertz morph',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_company_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteCrmConnectionIDCompanyIDRequest](../../models/operations/deletecrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteCrmConnectionIDCompanyIDResponse](../../models/operations/deletecrmconnectionidcompanyidresponse.md)**


## delete_crm_connection_id_contact_id

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

req = operations.DeleteCrmConnectionIDContactIDRequest(
    connection_id='chargesheet',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_contact_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteCrmConnectionIDContactIDRequest](../../models/operations/deletecrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteCrmConnectionIDContactIDResponse](../../models/operations/deletecrmconnectionidcontactidresponse.md)**


## delete_crm_connection_id_deal_id

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

req = operations.DeleteCrmConnectionIDDealIDRequest(
    connection_id='Fresh',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_deal_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDDealIDRequest](../../models/operations/deletecrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDDealIDResponse](../../models/operations/deletecrmconnectioniddealidresponse.md)**


## delete_crm_connection_id_event_id

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

req = operations.DeleteCrmConnectionIDEventIDRequest(
    connection_id='Wooden Latin',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_event_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCrmConnectionIDEventIDRequest](../../models/operations/deletecrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.DeleteCrmConnectionIDEventIDResponse](../../models/operations/deletecrmconnectionideventidresponse.md)**


## delete_crm_connection_id_file_id

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

req = operations.DeleteCrmConnectionIDFileIDRequest(
    connection_id='Bicycle',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_file_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDFileIDRequest](../../models/operations/deletecrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDFileIDResponse](../../models/operations/deletecrmconnectionidfileidresponse.md)**


## delete_crm_connection_id_lead_id

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

req = operations.DeleteCrmConnectionIDLeadIDRequest(
    connection_id='Senior azure',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_lead_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDLeadIDRequest](../../models/operations/deletecrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDLeadIDResponse](../../models/operations/deletecrmconnectionidleadidresponse.md)**


## delete_crm_connection_id_pipeline_id

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

req = operations.DeleteCrmConnectionIDPipelineIDRequest(
    connection_id='Customer',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_pipeline_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteCrmConnectionIDPipelineIDRequest](../../models/operations/deletecrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.DeleteCrmConnectionIDPipelineIDResponse](../../models/operations/deletecrmconnectionidpipelineidresponse.md)**


## delete_crm_connection_id_team_id

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

req = operations.DeleteCrmConnectionIDTeamIDRequest(
    connection_id='Diverse',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_team_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDTeamIDRequest](../../models/operations/deletecrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDTeamIDResponse](../../models/operations/deletecrmconnectionidteamidresponse.md)**


## delete_crm_connection_id_user_id

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

req = operations.DeleteCrmConnectionIDUserIDRequest(
    connection_id='Intranet Data',
    id='<ID>',
)

res = s.crm.delete_crm_connection_id_user_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDUserIDRequest](../../models/operations/deletecrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDUserIDResponse](../../models/operations/deletecrmconnectioniduseridresponse.md)**


## get_crm_connection_id_company

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

req = operations.GetCrmConnectionIDCompanyRequest(
    connection_id='indexing',
    contact_id='Porsche firewall',
    deal_id='Hafnium Computers',
    limit=902.85,
    offset=2893.88,
    order='Interactions relationships juxtapose',
    query='newton Luxembourg',
    sort='Dakota quantifying Actinium',
    updated_gte=dateutil.parser.isoparse('2022-09-27T07:42:48.074Z'),
)

res = s.crm.get_crm_connection_id_company(req)

if res.crm_companies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDCompanyRequest](../../models/operations/getcrmconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCrmConnectionIDCompanyResponse](../../models/operations/getcrmconnectionidcompanyresponse.md)**


## get_crm_connection_id_company_id

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

req = operations.GetCrmConnectionIDCompanyIDRequest(
    connection_id='Netherlands',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCrmConnectionIDCompanyIDRequest](../../models/operations/getcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCrmConnectionIDCompanyIDResponse](../../models/operations/getcrmconnectionidcompanyidresponse.md)**


## get_crm_connection_id_contact

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

req = operations.GetCrmConnectionIDContactRequest(
    company_id='Southeast Human Southeast',
    connection_id='magenta loose',
    deal_id='intuitive',
    limit=9605,
    offset=8572.44,
    order='Music Electronics',
    query='Elegant',
    sort='North Analyst Otis',
    updated_gte=dateutil.parser.isoparse('2022-09-18T15:42:24.943Z'),
)

res = s.crm.get_crm_connection_id_contact(req)

if res.crm_contacts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDContactRequest](../../models/operations/getcrmconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCrmConnectionIDContactResponse](../../models/operations/getcrmconnectionidcontactresponse.md)**


## get_crm_connection_id_contact_id

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

req = operations.GetCrmConnectionIDContactIDRequest(
    connection_id='Account fountain visionary',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCrmConnectionIDContactIDRequest](../../models/operations/getcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCrmConnectionIDContactIDResponse](../../models/operations/getcrmconnectionidcontactidresponse.md)**


## get_crm_connection_id_deal

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

req = operations.GetCrmConnectionIDDealRequest(
    company_id='Tools Card copying',
    connection_id='Renminbi',
    contact_id='till payment World',
    limit=8656.16,
    offset=4455.8,
    order='global',
    query='Program Bespoke Wisconsin',
    sort='Netherlands under',
    updated_gte=dateutil.parser.isoparse('2022-12-23T01:47:21.816Z'),
)

res = s.crm.get_crm_connection_id_deal(req)

if res.crm_deals is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDDealRequest](../../models/operations/getcrmconnectioniddealrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDDealResponse](../../models/operations/getcrmconnectioniddealresponse.md)**


## get_crm_connection_id_deal_id

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

req = operations.GetCrmConnectionIDDealIDRequest(
    connection_id='Concrete Director',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDDealIDRequest](../../models/operations/getcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDDealIDResponse](../../models/operations/getcrmconnectioniddealidresponse.md)**


## get_crm_connection_id_event

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

req = operations.GetCrmConnectionIDEventRequest(
    company_id='Zirconium Avon Bedfordshire',
    connection_id='Hybrid grey Ferrari',
    contact_id='Checking Southeast',
    deal_id='Graham till Caesium',
    limit=2928.84,
    offset=5904.77,
    order='furthermore Tricycle Hop',
    query='auxiliary',
    sort='Southeast Bicycle Gorgeous',
    updated_gte=dateutil.parser.isoparse('2023-01-15T23:49:53.643Z'),
)

res = s.crm.get_crm_connection_id_event(req)

if res.crm_events is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCrmConnectionIDEventRequest](../../models/operations/getcrmconnectionideventrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetCrmConnectionIDEventResponse](../../models/operations/getcrmconnectionideventresponse.md)**


## get_crm_connection_id_event_id

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

req = operations.GetCrmConnectionIDEventIDRequest(
    connection_id='Future equalise',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDEventIDRequest](../../models/operations/getcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCrmConnectionIDEventIDResponse](../../models/operations/getcrmconnectionideventidresponse.md)**


## get_crm_connection_id_file

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

req = operations.GetCrmConnectionIDFileRequest(
    company_id='reboot',
    connection_id='customise far',
    contact_id='Electronic proactive',
    deal_id='withdrawal deposit Gloves',
    limit=1588.79,
    offset=3754.81,
    order='Implemented fairly meh',
    query='FTP Producer',
    sort='soprano deliverables',
    updated_gte=dateutil.parser.isoparse('2022-03-02T03:00:09.711Z'),
)

res = s.crm.get_crm_connection_id_file(req)

if res.crm_files is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDFileRequest](../../models/operations/getcrmconnectionidfilerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDFileResponse](../../models/operations/getcrmconnectionidfileresponse.md)**


## get_crm_connection_id_file_id

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

req = operations.GetCrmConnectionIDFileIDRequest(
    connection_id='Bicycle',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDFileIDRequest](../../models/operations/getcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDFileIDResponse](../../models/operations/getcrmconnectionidfileidresponse.md)**


## get_crm_connection_id_lead

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

req = operations.GetCrmConnectionIDLeadRequest(
    connection_id='Computer Hop',
    limit=7411.81,
    offset=9004.32,
    order='Operations candela Integration',
    query='impactful transform',
    sort='Tala defense Southwest',
    updated_gte=dateutil.parser.isoparse('2021-09-29T00:37:32.184Z'),
)

res = s.crm.get_crm_connection_id_lead(req)

if res.crm_leads is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDLeadRequest](../../models/operations/getcrmconnectionidleadrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDLeadResponse](../../models/operations/getcrmconnectionidleadresponse.md)**


## get_crm_connection_id_lead_id

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

req = operations.GetCrmConnectionIDLeadIDRequest(
    connection_id='users Minnesota Bypass',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDLeadIDRequest](../../models/operations/getcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDLeadIDResponse](../../models/operations/getcrmconnectionidleadidresponse.md)**


## get_crm_connection_id_pipeline

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

req = operations.GetCrmConnectionIDPipelineRequest(
    connection_id='dirty Awesome Checking',
    limit=9055.88,
    offset=3443.76,
    order='glom',
    query='panel',
    sort='Latin tightly',
    updated_gte=dateutil.parser.isoparse('2022-03-01T15:47:43.244Z'),
)

res = s.crm.get_crm_connection_id_pipeline(req)

if res.crm_pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCrmConnectionIDPipelineRequest](../../models/operations/getcrmconnectionidpipelinerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetCrmConnectionIDPipelineResponse](../../models/operations/getcrmconnectionidpipelineresponse.md)**


## get_crm_connection_id_pipeline_id

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

req = operations.GetCrmConnectionIDPipelineIDRequest(
    connection_id='Tricycle roughly markets',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetCrmConnectionIDPipelineIDRequest](../../models/operations/getcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetCrmConnectionIDPipelineIDResponse](../../models/operations/getcrmconnectionidpipelineidresponse.md)**


## get_crm_connection_id_team

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

req = operations.GetCrmConnectionIDTeamRequest(
    connection_id='bath Lamborghini',
    limit=1042.31,
    offset=1586.42,
    order='Diesel Bike virtual',
    query='bakery',
    sort='Senior',
    updated_gte=dateutil.parser.isoparse('2021-12-04T23:56:00.028Z'),
)

res = s.crm.get_crm_connection_id_team(req)

if res.crm_teams is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDTeamRequest](../../models/operations/getcrmconnectionidteamrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDTeamResponse](../../models/operations/getcrmconnectionidteamresponse.md)**


## get_crm_connection_id_team_id

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

req = operations.GetCrmConnectionIDTeamIDRequest(
    connection_id='Intelligent invoice Tesla',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDTeamIDRequest](../../models/operations/getcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDTeamIDResponse](../../models/operations/getcrmconnectionidteamidresponse.md)**


## get_crm_connection_id_user

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

req = operations.GetCrmConnectionIDUserRequest(
    connection_id='suit Electronic Tampa',
    limit=2883.34,
    offset=8886.55,
    order='despite',
    query='frightfully Fitness',
    sort='success servant',
    updated_gte=dateutil.parser.isoparse('2023-02-23T05:53:04.259Z'),
)

res = s.crm.get_crm_connection_id_user(req)

if res.crm_users is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDUserRequest](../../models/operations/getcrmconnectioniduserrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDUserResponse](../../models/operations/getcrmconnectioniduserresponse.md)**


## get_crm_connection_id_user_id

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

req = operations.GetCrmConnectionIDUserIDRequest(
    connection_id='connecting Program',
    id='<ID>',
)

res = s.crm.get_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDUserIDRequest](../../models/operations/getcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDUserIDResponse](../../models/operations/getcrmconnectioniduseridresponse.md)**


## patch_crm_connection_id_company_id

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

req = operations.PatchCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='invoice',
            address2='indexing Ford',
            city='McAllen',
            country='Netherlands',
            country_code='PF',
            postal_code='93486',
            region='Steel impactful',
            region_code='Dong',
        ),
        created_at=dateutil.parser.isoparse('2023-07-25T08:43:38.995Z'),
        deal_ids=[
            'usefully',
        ],
        emails=[
            shared.CrmEmail(
                email='Annabel31@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        name='Toys Vermont Astatine',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'Trigender',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='female',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-12-22T11:39:56.432Z'),
        websites=[
            'Latin',
        ],
    ),
    connection_id='North kilogram connecting',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchCrmConnectionIDCompanyIDRequest](../../models/operations/patchcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PatchCrmConnectionIDCompanyIDResponse](../../models/operations/patchcrmconnectionidcompanyidresponse.md)**


## patch_crm_connection_id_contact_id

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

req = operations.PatchCrmConnectionIDContactIDRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='until instantly Taiwan',
            address2='disintermediate ah Southwest',
            city='San Antonio',
            country='Djibouti',
            country_code='LA',
            postal_code='23695',
            region='grey around',
            region_code='Folding',
        ),
        company='Johnson - Gerlach',
        company_ids=[
            'Personal',
        ],
        created_at=dateutil.parser.isoparse('2022-07-24T05:16:20.203Z'),
        deal_ids=[
            'generation',
        ],
        emails=[
            shared.CrmEmail(
                email='Leora_Konopelski27@hotmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='Innovative indeed brand',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='unsung Borders',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        title='withdrawal',
        updated_at=dateutil.parser.isoparse('2022-05-05T23:37:21.563Z'),
    ),
    connection_id='markets radian',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchCrmConnectionIDContactIDRequest](../../models/operations/patchcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PatchCrmConnectionIDContactIDResponse](../../models/operations/patchcrmconnectionidcontactidresponse.md)**


## patch_crm_connection_id_deal_id

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

req = operations.PatchCrmConnectionIDDealIDRequest(
    crm_deal=shared.CrmDeal(
        amount=7725.78,
        closed_at=dateutil.parser.isoparse('2021-10-28T08:42:49.591Z'),
        created_at=dateutil.parser.isoparse('2023-04-23T15:03:53.999Z'),
        currency='Afghani',
        id='<ID>',
        lost_reason='North',
        name='midnight',
        pipeline='envisioneer Functionality Loan',
        probability=7051.73,
        raw=shared.PropertyCrmDealRaw(),
        source='Krone',
        stage='pascal aliquam gripping',
        tags=[
            'where',
        ],
        updated_at=dateutil.parser.isoparse('2022-04-05T10:21:22.505Z'),
        won_reason='Savings kilogram',
    ),
    connection_id='Chair weber silver',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDDealIDRequest](../../models/operations/patchcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDDealIDResponse](../../models/operations/patchcrmconnectioniddealidresponse.md)**


## patch_crm_connection_id_event_id

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

req = operations.PatchCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Optional zero defect function',
            duration=5434.61,
        ),
        company_ids=[
            'silver',
        ],
        contact_ids=[
            'redefine',
        ],
        created_at=dateutil.parser.isoparse('2021-07-21T06:46:42.528Z'),
        deal_ids=[
            'Solutions',
        ],
        email=shared.PropertyCrmEventEmail(
            body='French',
            cc=[
                'Checking',
            ],
            from_='SDD Toyota Northeast',
            subject='Convertible',
            to=[
                'Electronics',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Monitored mission-critical customer loyalty',
            end_at=dateutil.parser.isoparse('2022-09-22T17:43:00.863Z'),
            start_at=dateutil.parser.isoparse('2023-04-24T06:40:04.926Z'),
            title='Kip Switchable Chicken',
        ),
        note=shared.PropertyCrmEventNote(
            description='Cross-group high-level functionalities',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Horizontal empowering forecast',
            name='Principal extremely Jast',
            status='striped Concrete Bronze',
        ),
        type=shared.CrmEventType.NOTE,
        updated_at=dateutil.parser.isoparse('2021-02-18T21:34:24.992Z'),
    ),
    connection_id='Dinar benchmark till',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchCrmConnectionIDEventIDRequest](../../models/operations/patchcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PatchCrmConnectionIDEventIDResponse](../../models/operations/patchcrmconnectionideventidresponse.md)**


## patch_crm_connection_id_file_id

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

req = operations.PatchCrmConnectionIDFileIDRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='duh Handmade harness',
        company_id='CFP',
        contact_id='unaware yellow generating',
        created_at=dateutil.parser.isoparse('2021-05-04T04:54:33.785Z'),
        deal_id='channels SUV',
        description='De-engineered didactic hardware',
        file_name='metical_silver_yellow.html',
        file_size=6861.53,
        file_type='video',
        file_url='navigate Funk',
        id='<ID>',
        lead_id='internal',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-02-21T13:46:42.012Z'),
        user_id='Interactions',
    ),
    connection_id='Handcrafted',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDFileIDRequest](../../models/operations/patchcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDFileIDResponse](../../models/operations/patchcrmconnectionidfileidresponse.md)**


## patch_crm_connection_id_lead_id

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

req = operations.PatchCrmConnectionIDLeadIDRequest(
    crm_lead=shared.CrmLead(
        active=False,
        address=shared.PropertyCrmLeadAddress(
            address1='Cambridgeshire',
            address2='Oriental farad male',
            city='D\'Amorebury',
            country='Reunion',
            country_code='UY',
            postal_code='87017-9001',
            region='Buckinghamshire Electric',
            region_code='South gee',
        ),
        company_id='Gasoline conglomeration Tennessine',
        contact_id='grow hub',
        created_at=dateutil.parser.isoparse('2023-06-09T15:23:12.644Z'),
        creator_user_id='voluptates',
        emails=[
            shared.CrmEmail(
                email='Jeffrey.Denesik52@yahoo.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='whiteboard lumen',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Cheese before against',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-07-12T14:19:50.007Z'),
        user_id='Games yellow Towels',
    ),
    connection_id='brr misuse',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDLeadIDRequest](../../models/operations/patchcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDLeadIDResponse](../../models/operations/patchcrmconnectionidleadidresponse.md)**


## patch_crm_connection_id_pipeline_id

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

req = operations.PatchCrmConnectionIDPipelineIDRequest(
    crm_pipeline=shared.CrmPipeline(
        active=False,
        created_at=dateutil.parser.isoparse('2023-08-24T17:39:51.183Z'),
        deal_probability=False,
        display_order=664.58,
        id='<ID>',
        name='bandwidth',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2023-11-27T01:55:15.440Z'),
    ),
    connection_id='Chips',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchCrmConnectionIDPipelineIDRequest](../../models/operations/patchcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PatchCrmConnectionIDPipelineIDResponse](../../models/operations/patchcrmconnectionidpipelineidresponse.md)**


## patch_crm_connection_id_team_id

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

req = operations.PatchCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2021-05-20T12:47:48.451Z'),
        description='Automated executive emulation',
        id='<ID>',
        name='Internal experiences',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-05-22T09:41:53.599Z'),
        user_ids=[
            'lumen',
        ],
    ),
    connection_id='up Candace',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDTeamIDRequest](../../models/operations/patchcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDTeamIDResponse](../../models/operations/patchcrmconnectionidteamidresponse.md)**


## patch_crm_connection_id_user_id

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

req = operations.PatchCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='Customer',
            address2='violet groupware blanditiis',
            city='South Phoebeshire',
            country='Thailand',
            country_code='NO',
            postal_code='30801-4594',
            region='portals Vanadium',
            region_code='Future',
        ),
        created_at=dateutil.parser.isoparse('2023-01-04T02:42:28.788Z'),
        currency='Guinea Franc',
        department='Gloves global rosin',
        division='Berkshire Europium',
        emails=[
            shared.CrmEmail(
                email='Wade.Dach@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        image_url='Checking',
        language_locale='Sedan Porsche matrix',
        name='superstructure Nissan sedately',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='unto ubiquitous input',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        timezone='America/Tijuana',
        title='Computer Bicycle',
        updated_at=dateutil.parser.isoparse('2021-12-13T16:36:33.886Z'),
    ),
    connection_id='gold generating',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDUserIDRequest](../../models/operations/patchcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDUserIDResponse](../../models/operations/patchcrmconnectioniduseridresponse.md)**


## post_crm_connection_id_company

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

req = operations.PostCrmConnectionIDCompanyRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='consequently gosh',
            address2='phooey',
            city='Antonettaville',
            country='Lebanon',
            country_code='SI',
            postal_code='79462',
            region='orchid Oxygen Kids',
            region_code='Electric utilisation',
        ),
        created_at=dateutil.parser.isoparse('2021-10-01T08:46:18.197Z'),
        deal_ids=[
            'Tennessee',
        ],
        emails=[
            shared.CrmEmail(
                email='Jaida.McDermott26@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='Hydrogen Wooden',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'CSS',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Account invoice',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-09-12T17:31:24.634Z'),
        websites=[
            'Intuitive',
        ],
    ),
    connection_id='Gasoline',
)

res = s.crm.post_crm_connection_id_company(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostCrmConnectionIDCompanyRequest](../../models/operations/postcrmconnectionidcompanyrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostCrmConnectionIDCompanyResponse](../../models/operations/postcrmconnectionidcompanyresponse.md)**


## post_crm_connection_id_contact

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

req = operations.PostCrmConnectionIDContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='orchid',
            address2='invoice wherever watt',
            city='Rempelcester',
            country='Nepal',
            country_code='FI',
            postal_code='27896-6482',
            region='swig',
            region_code='Recumbent',
        ),
        company='Fritsch - Bernhard',
        company_ids=[
            'Executive',
        ],
        created_at=dateutil.parser.isoparse('2021-07-26T17:34:53.280Z'),
        deal_ids=[
            'Southwest',
        ],
        emails=[
            shared.CrmEmail(
                email='Colby24@hotmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='farad',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Dynamic withdrawal',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        title='second Fresh',
        updated_at=dateutil.parser.isoparse('2023-01-03T09:41:22.581Z'),
    ),
    connection_id='what',
)

res = s.crm.post_crm_connection_id_contact(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostCrmConnectionIDContactRequest](../../models/operations/postcrmconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostCrmConnectionIDContactResponse](../../models/operations/postcrmconnectionidcontactresponse.md)**


## post_crm_connection_id_deal

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

req = operations.PostCrmConnectionIDDealRequest(
    crm_deal=shared.CrmDeal(
        amount=6144.41,
        closed_at=dateutil.parser.isoparse('2022-07-10T09:55:59.977Z'),
        created_at=dateutil.parser.isoparse('2022-01-20T07:28:03.436Z'),
        currency='Convertible Marks',
        id='<ID>',
        lost_reason='pfft female',
        name='Expressway',
        pipeline='withdrawal Extended busily',
        probability=7998.22,
        raw=shared.PropertyCrmDealRaw(),
        source='spiffy sometimes',
        stage='transmitter',
        tags=[
            'intermediate',
        ],
        updated_at=dateutil.parser.isoparse('2022-10-06T18:34:11.762Z'),
        won_reason='Cisgender input HTTP',
    ),
    connection_id='accusantium Checking',
)

res = s.crm.post_crm_connection_id_deal(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDDealRequest](../../models/operations/postcrmconnectioniddealrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDDealResponse](../../models/operations/postcrmconnectioniddealresponse.md)**


## post_crm_connection_id_event

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

req = operations.PostCrmConnectionIDEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Visionary bandwidth-monitored hardware',
            duration=9256.02,
        ),
        company_ids=[
            'Kentucky',
        ],
        contact_ids=[
            'Rustic',
        ],
        created_at=dateutil.parser.isoparse('2023-02-12T10:03:55.861Z'),
        deal_ids=[
            'agonizing',
        ],
        email=shared.PropertyCrmEventEmail(
            body='protocol',
            cc=[
                'Ratke',
            ],
            from_='woman',
            subject='East Soft',
            to=[
                'Southeast',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Streamlined intangible time-frame',
            end_at=dateutil.parser.isoparse('2022-04-18T21:50:55.608Z'),
            start_at=dateutil.parser.isoparse('2021-08-24T14:06:25.626Z'),
            title='violet Synergized blah',
        ),
        note=shared.PropertyCrmEventNote(
            description='Mandatory eco-centric toolset',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Team-oriented dynamic forecast',
            name='Grocery',
            status='excitedly Bacon',
        ),
        type=shared.CrmEventType.EMAIL,
        updated_at=dateutil.parser.isoparse('2021-09-09T20:12:06.214Z'),
    ),
    connection_id='Progressive',
)

res = s.crm.post_crm_connection_id_event(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostCrmConnectionIDEventRequest](../../models/operations/postcrmconnectionideventrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostCrmConnectionIDEventResponse](../../models/operations/postcrmconnectionideventresponse.md)**


## post_crm_connection_id_file

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

req = operations.PostCrmConnectionIDFileRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='tan impedit Pickup',
        company_id='Manager',
        contact_id='Florida Shoes East',
        created_at=dateutil.parser.isoparse('2023-01-08T11:37:24.708Z'),
        deal_id='Agent',
        description='Multi-lateral well-modulated portal',
        file_name='panel_city.wav',
        file_size=1401.73,
        file_type='application',
        file_url='for Chips under',
        id='<ID>',
        lead_id='abaft Checking',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-02-25T09:46:59.608Z'),
        user_id='Mexico withdrawal',
    ),
    connection_id='national Lead',
)

res = s.crm.post_crm_connection_id_file(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDFileRequest](../../models/operations/postcrmconnectionidfilerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDFileResponse](../../models/operations/postcrmconnectionidfileresponse.md)**


## post_crm_connection_id_lead

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

req = operations.PostCrmConnectionIDLeadRequest(
    crm_lead=shared.CrmLead(
        active=False,
        address=shared.PropertyCrmLeadAddress(
            address1='XSS Country knowledge',
            address2='structure',
            city='Giovaniton',
            country='Ghana',
            country_code='CO',
            postal_code='34495-0585',
            region='Modern',
            region_code='Diesel',
        ),
        company_id='yuppify',
        contact_id='demanding scratch male',
        created_at=dateutil.parser.isoparse('2023-03-07T11:22:05.657Z'),
        creator_user_id='masticate South',
        emails=[
            shared.CrmEmail(
                email='Gregorio37@gmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='Granite Tools',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Hassium Balanced male',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-06-26T11:56:58.926Z'),
        user_id='Consultant',
    ),
    connection_id='solutions gosh',
)

res = s.crm.post_crm_connection_id_lead(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDLeadRequest](../../models/operations/postcrmconnectionidleadrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDLeadResponse](../../models/operations/postcrmconnectionidleadresponse.md)**


## post_crm_connection_id_pipeline

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

req = operations.PostCrmConnectionIDPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        active=False,
        created_at=dateutil.parser.isoparse('2023-12-10T23:55:22.206Z'),
        deal_probability=False,
        display_order=3879.73,
        id='<ID>',
        name='upward Mayaguez',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2021-09-25T10:43:23.679Z'),
    ),
    connection_id='Lead Health',
)

res = s.crm.post_crm_connection_id_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostCrmConnectionIDPipelineRequest](../../models/operations/postcrmconnectionidpipelinerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostCrmConnectionIDPipelineResponse](../../models/operations/postcrmconnectionidpipelineresponse.md)**


## post_crm_connection_id_team

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

req = operations.PostCrmConnectionIDTeamRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2022-02-12T08:57:03.070Z'),
        description='Organic transitional portal',
        id='<ID>',
        name='male bandwidth',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-12-29T15:50:04.365Z'),
        user_ids=[
            'meter',
        ],
    ),
    connection_id='Guaynabo AGP East',
)

res = s.crm.post_crm_connection_id_team(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDTeamRequest](../../models/operations/postcrmconnectionidteamrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDTeamResponse](../../models/operations/postcrmconnectionidteamresponse.md)**


## post_crm_connection_id_user

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

req = operations.PostCrmConnectionIDUserRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='driver East',
            address2='relationships Computer navigate',
            city='Homestead',
            country='Cayman Islands',
            country_code='BW',
            postal_code='34958',
            region='South',
            region_code='morph an colossal',
        ),
        created_at=dateutil.parser.isoparse('2021-02-02T08:27:21.693Z'),
        currency='Cayman Islands Dollar',
        department='um',
        division='West sievert generating',
        emails=[
            shared.CrmEmail(
                email='Jadon_Schumm45@gmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        image_url='radian Borders Southeast',
        language_locale='Silicon Awesome Industrial',
        name='Mouse Accounts',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='ohm Southeast ROI',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        timezone='Europe/Bratislava',
        title='Money',
        updated_at=dateutil.parser.isoparse('2023-12-09T10:24:50.054Z'),
    ),
    connection_id='competent calculate',
)

res = s.crm.post_crm_connection_id_user(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDUserRequest](../../models/operations/postcrmconnectioniduserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDUserResponse](../../models/operations/postcrmconnectioniduserresponse.md)**


## put_crm_connection_id_company_id

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

req = operations.PutCrmConnectionIDCompanyIDRequest(
    crm_company=shared.CrmCompany(
        active=False,
        address=shared.PropertyCrmCompanyAddress(
            address1='Northwest Northwest',
            address2='portals Diesel',
            city='Azusa',
            country='Qatar',
            country_code='CG',
            postal_code='52396',
            region='Tuna sticky lest',
            region_code='Soft boo Missoula',
        ),
        created_at=dateutil.parser.isoparse('2022-05-14T19:17:30.970Z'),
        deal_ids=[
            'Hybrid',
        ],
        emails=[
            shared.CrmEmail(
                email='Vance_Cruickshank93@gmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='lest Northwest',
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'East',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='Bronze round',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-02-21T09:41:36.696Z'),
        websites=[
            'Keyboard',
        ],
    ),
    connection_id='orange Bespoke',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutCrmConnectionIDCompanyIDRequest](../../models/operations/putcrmconnectionidcompanyidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutCrmConnectionIDCompanyIDResponse](../../models/operations/putcrmconnectionidcompanyidresponse.md)**


## put_crm_connection_id_contact_id

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

req = operations.PutCrmConnectionIDContactIDRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='idolized',
            address2='Southeast Specialist background',
            city='New Orlando',
            country='Switzerland',
            country_code='GL',
            postal_code='95864',
            region='Intersex mmm',
            region_code='Specialist',
        ),
        company='Mann and Sons',
        company_ids=[
            'impedit',
        ],
        created_at=dateutil.parser.isoparse('2023-10-28T10:36:29.710Z'),
        deal_ids=[
            'transmitting',
        ],
        emails=[
            shared.CrmEmail(
                email='Marjorie.Feeney14@hotmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='shuttle',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Bolivia',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        title='Austria reinvent',
        updated_at=dateutil.parser.isoparse('2023-03-20T11:49:01.796Z'),
    ),
    connection_id='hic truck',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutCrmConnectionIDContactIDRequest](../../models/operations/putcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutCrmConnectionIDContactIDResponse](../../models/operations/putcrmconnectionidcontactidresponse.md)**


## put_crm_connection_id_deal_id

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

req = operations.PutCrmConnectionIDDealIDRequest(
    crm_deal=shared.CrmDeal(
        amount=4050.98,
        closed_at=dateutil.parser.isoparse('2022-01-15T04:05:31.641Z'),
        created_at=dateutil.parser.isoparse('2023-06-04T01:28:32.466Z'),
        currency='Bermudian Dollar (customarily known as Bermuda Dollar)',
        id='<ID>',
        lost_reason='laudantium Southwest',
        name='wail Developer',
        pipeline='male Samarium Gourde',
        probability=6728.74,
        raw=shared.PropertyCrmDealRaw(),
        source='Stage Gasoline Metal',
        stage='Corporate withdrawal Tasty',
        tags=[
            'extranet',
        ],
        updated_at=dateutil.parser.isoparse('2021-10-16T22:38:02.052Z'),
        won_reason='phooey',
    ),
    connection_id='Jazz',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDDealIDRequest](../../models/operations/putcrmconnectioniddealidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDDealIDResponse](../../models/operations/putcrmconnectioniddealidresponse.md)**


## put_crm_connection_id_event_id

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

req = operations.PutCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Re-engineered composite time-frame',
            duration=5444.58,
        ),
        company_ids=[
            'DNS',
        ],
        contact_ids=[
            'Skokie',
        ],
        created_at=dateutil.parser.isoparse('2022-07-05T01:37:36.877Z'),
        deal_ids=[
            'lux',
        ],
        email=shared.PropertyCrmEventEmail(
            body='Hatchback card',
            cc=[
                'Gasoline',
            ],
            from_='Caribbean',
            subject='Account medium',
            to=[
                'copy',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Inverse optimizing model',
            end_at=dateutil.parser.isoparse('2022-03-21T17:32:41.888Z'),
            start_at=dateutil.parser.isoparse('2022-10-17T10:31:48.119Z'),
            title='male henry Hat',
        ),
        note=shared.PropertyCrmEventNote(
            description='Self-enabling asymmetric functionalities',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Reduced 4th generation analyzer',
            name='Savings Female nor',
            status='Customer sky',
        ),
        type=shared.CrmEventType.NOTE,
        updated_at=dateutil.parser.isoparse('2023-07-27T14:02:37.510Z'),
    ),
    connection_id='transparent',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCrmConnectionIDEventIDRequest](../../models/operations/putcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PutCrmConnectionIDEventIDResponse](../../models/operations/putcrmconnectionideventidresponse.md)**


## put_crm_connection_id_file_id

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

req = operations.PutCrmConnectionIDFileIDRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='Cotton',
        company_id='Northeast',
        contact_id='Computer',
        created_at=dateutil.parser.isoparse('2021-04-09T13:10:01.367Z'),
        deal_id='toward confiscate East',
        description='Devolved upward-trending matrices',
        file_name='generation_tactics.wav',
        file_size=4770.09,
        file_type='audio',
        file_url='framework azure Metal',
        id='<ID>',
        lead_id='ampere costume',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-05-15T05:04:24.130Z'),
        user_id='Research payment',
    ),
    connection_id='East Associate Mazda',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDFileIDRequest](../../models/operations/putcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDFileIDResponse](../../models/operations/putcrmconnectionidfileidresponse.md)**


## put_crm_connection_id_lead_id

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

req = operations.PutCrmConnectionIDLeadIDRequest(
    crm_lead=shared.CrmLead(
        active=False,
        address=shared.PropertyCrmLeadAddress(
            address1='Extension',
            address2='supposing Dorado Assistant',
            city='South Gate',
            country='Reunion',
            country_code='IS',
            postal_code='73732-2192',
            region='JBOD phew',
            region_code='Southeast Framingham female',
        ),
        company_id='deposit male',
        contact_id='bunch edge',
        created_at=dateutil.parser.isoparse('2021-04-03T18:08:02.798Z'),
        creator_user_id='East Panama',
        emails=[
            shared.CrmEmail(
                email='Jamal20@yahoo.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        name='pianist',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='caricature female',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-08-09T07:11:50.077Z'),
        user_id='Designer Folding',
    ),
    connection_id='Lanthanum wink Regional',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDLeadIDRequest](../../models/operations/putcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDLeadIDResponse](../../models/operations/putcrmconnectionidleadidresponse.md)**


## put_crm_connection_id_pipeline_id

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

req = operations.PutCrmConnectionIDPipelineIDRequest(
    crm_pipeline=shared.CrmPipeline(
        active=False,
        created_at=dateutil.parser.isoparse('2021-05-16T17:24:47.805Z'),
        deal_probability=False,
        display_order=5470.76,
        id='<ID>',
        name='West',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2022-02-28T07:49:31.151Z'),
    ),
    connection_id='optimizing',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutCrmConnectionIDPipelineIDRequest](../../models/operations/putcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PutCrmConnectionIDPipelineIDResponse](../../models/operations/putcrmconnectionidpipelineidresponse.md)**


## put_crm_connection_id_team_id

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

req = operations.PutCrmConnectionIDTeamIDRequest(
    crm_team=shared.CrmTeam(
        created_at=dateutil.parser.isoparse('2023-08-14T23:28:53.515Z'),
        description='Inverse multi-tasking task-force',
        id='<ID>',
        name='Indonesia Orchestrator Division',
        raw=shared.PropertyCrmTeamRaw(),
        updated_at=dateutil.parser.isoparse('2022-10-23T23:13:25.973Z'),
        user_ids=[
            'thoroughly',
        ],
    ),
    connection_id='delectus',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDTeamIDRequest](../../models/operations/putcrmconnectionidteamidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDTeamIDResponse](../../models/operations/putcrmconnectionidteamidresponse.md)**


## put_crm_connection_id_user_id

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

req = operations.PutCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='Honduras',
            address2='Oxygen Libyan Burundi',
            city='North Gertrudefield',
            country='Belgium',
            country_code='DK',
            postal_code='00781',
            region='Wagon',
            region_code='how overriding',
        ),
        created_at=dateutil.parser.isoparse('2023-03-13T00:47:15.649Z'),
        currency='Pakistan Rupee',
        department='Tricycle vaguely',
        division='Severn bluetooth Argon',
        emails=[
            shared.CrmEmail(
                email='Karl_Stehr4@hotmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        image_url='AGP romance didactic',
        language_locale='ROI Polarised',
        name='olive synthesizing',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Honda Indiana',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        timezone='Asia/Novosibirsk',
        title='compelling red compressing',
        updated_at=dateutil.parser.isoparse('2022-09-03T15:59:05.095Z'),
    ),
    connection_id='relationships',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDUserIDRequest](../../models/operations/putcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDUserIDResponse](../../models/operations/putcrmconnectioniduseridresponse.md)**

