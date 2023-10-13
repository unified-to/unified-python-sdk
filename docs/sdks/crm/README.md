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
    pass
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
    pass
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
    pass
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
    pass
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
    pass
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
    pass
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
    pass
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
    pass
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
    pass
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
)

res = s.crm.get_crm_connection_id_company(req)

if res.crm_companies is not None:
    # handle response
    pass
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
    pass
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
    connection_id='Southeast Human Southeast',
)

res = s.crm.get_crm_connection_id_contact(req)

if res.crm_contacts is not None:
    # handle response
    pass
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
    pass
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
    connection_id='Tools Card copying',
)

res = s.crm.get_crm_connection_id_deal(req)

if res.crm_deals is not None:
    # handle response
    pass
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
    pass
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
    connection_id='Zirconium Avon Bedfordshire',
)

res = s.crm.get_crm_connection_id_event(req)

if res.crm_events is not None:
    # handle response
    pass
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
    pass
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
    connection_id='reboot',
)

res = s.crm.get_crm_connection_id_file(req)

if res.crm_files is not None:
    # handle response
    pass
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
    pass
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
)

res = s.crm.get_crm_connection_id_lead(req)

if res.crm_leads is not None:
    # handle response
    pass
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
    pass
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
)

res = s.crm.get_crm_connection_id_pipeline(req)

if res.crm_pipelines is not None:
    # handle response
    pass
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
    pass
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
)

res = s.crm.get_crm_connection_id_team(req)

if res.crm_teams is not None:
    # handle response
    pass
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
    pass
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
)

res = s.crm.get_crm_connection_id_user(req)

if res.crm_users is not None:
    # handle response
    pass
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
    pass
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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Soft',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'invoice',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='miniature Quality',
            ),
        ],
        websites=[
            'redefine',
        ],
    ),
    connection_id='invoice National',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'Bicycle',
        ],
        deal_ids=[
            'instantly',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='stimulating',
            ),
        ],
    ),
    connection_id='synergy',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'Bicycle',
        ],
    ),
    connection_id='partnerships',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'parse',
        ],
        contact_ids=[
            'intranet',
        ],
        deal_ids=[
            'silver',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'redefine',
            ],
            to=[
                'Baby',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Steel',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='duh Handmade harness',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Cambridgeshire',
            ),
        ],
    ),
    connection_id='Oriental farad male',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='Bedfordshire bandwidth a',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'Arizona',
        ],
    ),
    connection_id='Internal experiences',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Customer',
            ),
        ],
    ),
    connection_id='violet groupware blanditiis',
    id='<ID>',
)

res = s.crm.patch_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'Personal',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'gosh',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='phooey',
            ),
        ],
        websites=[
            'primary',
        ],
    ),
    connection_id='neural',
)

res = s.crm.post_crm_connection_id_company(req)

if res.crm_company is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'integrated',
        ],
        deal_ids=[
            'Mobility',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='who SUV',
            ),
        ],
    ),
    connection_id='sievert Tungsten',
)

res = s.crm.post_crm_connection_id_contact(req)

if res.crm_contact is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'M2F',
        ],
    ),
    connection_id='Borders pfft',
)

res = s.crm.post_crm_connection_id_deal(req)

if res.crm_deal is not None:
    # handle response
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'carburize',
        ],
        contact_ids=[
            'SDR',
        ],
        deal_ids=[
            'Kentucky',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Rustic',
            ],
            to=[
                'male',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Hat',
)

res = s.crm.post_crm_connection_id_event(req)

if res.crm_event is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='tan impedit Pickup',
)

res = s.crm.post_crm_connection_id_file(req)

if res.crm_file is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='XSS Country knowledge',
            ),
        ],
    ),
    connection_id='structure',
)

res = s.crm.post_crm_connection_id_lead(req)

if res.crm_lead is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='Interface alpaca program',
)

res = s.crm.post_crm_connection_id_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'local',
        ],
    ),
    connection_id='pascal male bandwidth',
)

res = s.crm.post_crm_connection_id_team(req)

if res.crm_team is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='driver East',
            ),
        ],
    ),
    connection_id='relationships Computer navigate',
)

res = s.crm.post_crm_connection_id_user(req)

if res.crm_user is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'dicta',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'background',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='veniam secondary',
            ),
        ],
        websites=[
            'Southwest',
        ],
    ),
    connection_id='Calcium',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_company_id(req)

if res.crm_company is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'Outdoors',
        ],
        deal_ids=[
            'Credit',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Specialist background',
            ),
        ],
    ),
    connection_id='quo gloomy',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'Account',
        ],
    ),
    connection_id='payment',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_deal_id(req)

if res.crm_deal is not None:
    # handle response
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'Iron',
        ],
        contact_ids=[
            'marshmallow',
        ],
        deal_ids=[
            'DNS',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Skokie',
            ],
            to=[
                'calculating',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Blues firewall engineer',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='Cotton',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Extension',
            ),
        ],
    ),
    connection_id='supposing Dorado Assistant',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='back',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
    pass
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
        raw=shared.PropertyCrmTeamRaw(),
        user_ids=[
            'immense',
        ],
    ),
    connection_id='duh Indonesia',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_team_id(req)

if res.crm_team is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Honduras',
            ),
        ],
    ),
    connection_id='Oxygen Libyan Burundi',
    id='<ID>',
)

res = s.crm.put_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDUserIDRequest](../../models/operations/putcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDUserIDResponse](../../models/operations/putcrmconnectioniduseridresponse.md)**

