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
* [get_crm_company](#get_crm_company) - Retrieve a company
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_crm_deal](#get_crm_deal) - Retrieve a deal
* [get_crm_event](#get_crm_event) - Retrieve a event
* [get_crm_file](#get_crm_file) - Retrieve a file
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [get_crm_pipeline](#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_crm_deals](#list_crm_deals) - List all deals
* [list_crm_events](#list_crm_events) - List all events
* [list_crm_files](#list_crm_files) - List all files
* [list_crm_leads](#list_crm_leads) - List all leads
* [list_crm_pipelines](#list_crm_pipelines) - List all pipelines
* [patch_crm_company](#patch_crm_company) - Update a company
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_crm_deal](#patch_crm_deal) - Update a deal
* [patch_crm_event](#patch_crm_event) - Update a event
* [patch_crm_file](#patch_crm_file) - Update a file
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [patch_crm_pipeline](#patch_crm_pipeline) - Update a pipeline
* [remove_crm_company](#remove_crm_company) - Remove a company
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_crm_deal](#remove_crm_deal) - Remove a deal
* [remove_crm_event](#remove_crm_event) - Remove a event
* [remove_crm_file](#remove_crm_file) - Remove a file
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [remove_crm_pipeline](#remove_crm_pipeline) - Remove a pipeline
* [update_crm_company](#update_crm_company) - Update a company
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_crm_deal](#update_crm_deal) - Update a deal
* [update_crm_event](#update_crm_event) - Update a event
* [update_crm_file](#update_crm_file) - Update a file
* [update_crm_lead](#update_crm_lead) - Update a lead
* [update_crm_pipeline](#update_crm_pipeline) - Update a pipeline

## create_crm_company

Create a company

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
        websites=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_contact

Create a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_deal

Create a deal

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_event

Create a event

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        lead_ids=[
            'string',
        ],
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_file

Create a file

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_lead

Create a lead

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_crm_pipeline

Create a pipeline

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.CreateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_company

Retrieve a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmCompanyRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmContactRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_deal

Retrieve a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmDealRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_event

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmEventRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_file

Retrieve a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmFileRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_lead

Retrieve a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmLeadRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_crm_pipeline

Retrieve a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.GetCrmPipelineRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_companies

List all companies

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmCompaniesRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_contacts

List all contacts

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmContactsRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_deals

List all deals

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmDealsRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_events

List all events

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmEventsRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_files

List all files

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmFilesRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_leads

List all leads

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmLeadsRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_crm_pipelines

List all pipelines

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.ListCrmPipelinesRequest(
    connection_id='string',
    fields=[
        'string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_company

Update a company

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
        websites=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_contact

Update a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_deal

Update a deal

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_event

Update a event

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        lead_ids=[
            'string',
        ],
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_file

Update a file

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_lead

Update a lead

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_crm_pipeline

Update a pipeline

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_company

Remove a company

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmCompanyRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmContactRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_deal

Remove a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmDealRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_event

Remove a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmEventRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_file

Remove a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmFileRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_lead

Remove a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmLeadRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## remove_crm_pipeline

Remove a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.RemoveCrmPipelineRequest(
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_company

Update a company

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmCompanyRequest(
    crm_company=shared.CrmCompany(
        address=shared.PropertyCrmCompanyAddress(),
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmCompanyRaw(),
        tags=[
            'string',
        ],
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
        websites=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_contact

Update a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(),
        company_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_deal

Update a deal

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmDealRequest(
    crm_deal=shared.CrmDeal(
        raw=shared.PropertyCrmDealRaw(),
        tags=[
            'string',
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_event

Update a event

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        lead_ids=[
            'string',
        ],
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_file

Update a file

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmFileRequest(
    crm_file=shared.CrmFile(
        raw=shared.PropertyCrmFileRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_lead

Update a lead

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmLeadRequest(
    crm_lead=shared.CrmLead(
        address=shared.PropertyCrmLeadAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_crm_pipeline

Update a pipeline

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.UpdateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
