# Crm
(*crm*)

### Available Operations

* [create_crm_company](#create_crm_company) - Create a company
* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_crm_deal](#create_crm_deal) - Create a deal
* [create_crm_event](#create_crm_event) - Create a event
* [create_crm_lead](#create_crm_lead) - Create a lead
* [create_crm_pipeline](#create_crm_pipeline) - Create a pipeline
* [get_crm_company](#get_crm_company) - Retrieve a company
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_crm_deal](#get_crm_deal) - Retrieve a deal
* [get_crm_event](#get_crm_event) - Retrieve a event
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [get_crm_pipeline](#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_companies](#list_crm_companies) - List all companies
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_crm_deals](#list_crm_deals) - List all deals
* [list_crm_events](#list_crm_events) - List all events
* [list_crm_leads](#list_crm_leads) - List all leads
* [list_crm_pipelines](#list_crm_pipelines) - List all pipelines
* [patch_crm_company](#patch_crm_company) - Update a company
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_crm_deal](#patch_crm_deal) - Update a deal
* [patch_crm_event](#patch_crm_event) - Update a event
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [patch_crm_pipeline](#patch_crm_pipeline) - Update a pipeline
* [remove_crm_company](#remove_crm_company) - Remove a company
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_crm_deal](#remove_crm_deal) - Remove a deal
* [remove_crm_event](#remove_crm_event) - Remove a event
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [remove_crm_pipeline](#remove_crm_pipeline) - Remove a pipeline
* [update_crm_company](#update_crm_company) - Update a company
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_crm_deal](#update_crm_deal) - Update a deal
* [update_crm_event](#update_crm_event) - Update a event
* [update_crm_lead](#update_crm_lead) - Update a lead
* [update_crm_pipeline](#update_crm_pipeline) - Update a pipeline

## create_crm_company

Create a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmCompanyRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_company(req, operations.CreateCrmCompanySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmCompanyRequest](../../models/operations/createcrmcompanyrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.CreateCrmCompanySecurity](../../models/operations/createcrmcompanysecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.CreateCrmCompanyResponse](../../models/operations/createcrmcompanyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_crm_contact

Create a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmContactRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_contact(req, operations.CreateCrmContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmContactRequest](../../models/operations/createcrmcontactrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.CreateCrmContactSecurity](../../models/operations/createcrmcontactsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.CreateCrmContactResponse](../../models/operations/createcrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_crm_deal

Create a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmDealRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_deal(req, operations.CreateCrmDealSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmDealRequest](../../models/operations/createcrmdealrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.CreateCrmDealSecurity](../../models/operations/createcrmdealsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.CreateCrmDealResponse](../../models/operations/createcrmdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_crm_event

Create a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmEventRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_event(req, operations.CreateCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.CreateCrmEventSecurity](../../models/operations/createcrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_crm_lead

Create a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmLeadRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_lead(req, operations.CreateCrmLeadSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmLeadRequest](../../models/operations/createcrmleadrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.CreateCrmLeadSecurity](../../models/operations/createcrmleadsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.CreateCrmLeadResponse](../../models/operations/createcrmleadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_crm_pipeline

Create a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmPipelineRequest(
    connection_id='<value>',
)

res = s.crm.create_crm_pipeline(req, operations.CreateCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateCrmPipelineSecurity](../../models/operations/createcrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_company

Retrieve a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmCompanyRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_company(req, operations.GetCrmCompanySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmCompanyRequest](../../models/operations/getcrmcompanyrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetCrmCompanySecurity](../../models/operations/getcrmcompanysecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetCrmCompanyResponse](../../models/operations/getcrmcompanyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_contact(req, operations.GetCrmContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmContactRequest](../../models/operations/getcrmcontactrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetCrmContactSecurity](../../models/operations/getcrmcontactsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetCrmContactResponse](../../models/operations/getcrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_deal

Retrieve a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmDealRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_deal(req, operations.GetCrmDealSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmDealRequest](../../models/operations/getcrmdealrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetCrmDealSecurity](../../models/operations/getcrmdealsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetCrmDealResponse](../../models/operations/getcrmdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_event

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_event(req, operations.GetCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetCrmEventSecurity](../../models/operations/getcrmeventsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_lead

Retrieve a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmLeadRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_lead(req, operations.GetCrmLeadSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmLeadRequest](../../models/operations/getcrmleadrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetCrmLeadSecurity](../../models/operations/getcrmleadsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetCrmLeadResponse](../../models/operations/getcrmleadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_pipeline

Retrieve a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.get_crm_pipeline(req, operations.GetCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetCrmPipelineSecurity](../../models/operations/getcrmpipelinesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_companies

List all companies

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmCompaniesRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_companies(req, operations.ListCrmCompaniesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_companies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCrmCompaniesRequest](../../models/operations/listcrmcompaniesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListCrmCompaniesSecurity](../../models/operations/listcrmcompaniessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListCrmCompaniesResponse](../../models/operations/listcrmcompaniesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_contacts

List all contacts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmContactsRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_contacts(req, operations.ListCrmContactsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmContactsRequest](../../models/operations/listcrmcontactsrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ListCrmContactsSecurity](../../models/operations/listcrmcontactssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ListCrmContactsResponse](../../models/operations/listcrmcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_deals

List all deals

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmDealsRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_deals(req, operations.ListCrmDealsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_deals is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmDealsRequest](../../models/operations/listcrmdealsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListCrmDealsSecurity](../../models/operations/listcrmdealssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListCrmDealsResponse](../../models/operations/listcrmdealsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_events

List all events

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmEventsRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_events(req, operations.ListCrmEventsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_events is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ListCrmEventsSecurity](../../models/operations/listcrmeventssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_leads

List all leads

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmLeadsRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_leads(req, operations.ListCrmLeadsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_leads is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmLeadsRequest](../../models/operations/listcrmleadsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListCrmLeadsSecurity](../../models/operations/listcrmleadssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListCrmLeadsResponse](../../models/operations/listcrmleadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_pipelines

List all pipelines

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmPipelinesRequest(
    connection_id='<value>',
)

res = s.crm.list_crm_pipelines(req, operations.ListCrmPipelinesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListCrmPipelinesSecurity](../../models/operations/listcrmpipelinessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_company

Update a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmCompanyRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_company(req, operations.PatchCrmCompanySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmCompanyRequest](../../models/operations/patchcrmcompanyrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PatchCrmCompanySecurity](../../models/operations/patchcrmcompanysecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.PatchCrmCompanyResponse](../../models/operations/patchcrmcompanyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_contact(req, operations.PatchCrmContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmContactRequest](../../models/operations/patchcrmcontactrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PatchCrmContactSecurity](../../models/operations/patchcrmcontactsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.PatchCrmContactResponse](../../models/operations/patchcrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_deal

Update a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmDealRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_deal(req, operations.PatchCrmDealSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmDealRequest](../../models/operations/patchcrmdealrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.PatchCrmDealSecurity](../../models/operations/patchcrmdealsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.PatchCrmDealResponse](../../models/operations/patchcrmdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_event

Update a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_event(req, operations.PatchCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.PatchCrmEventSecurity](../../models/operations/patchcrmeventsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_lead

Update a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmLeadRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_lead(req, operations.PatchCrmLeadSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmLeadRequest](../../models/operations/patchcrmleadrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.PatchCrmLeadSecurity](../../models/operations/patchcrmleadsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.PatchCrmLeadResponse](../../models/operations/patchcrmleadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.patch_crm_pipeline(req, operations.PatchCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchCrmPipelineSecurity](../../models/operations/patchcrmpipelinesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_company

Remove a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmCompanyRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_company(req, operations.RemoveCrmCompanySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmCompanyRequest](../../models/operations/removecrmcompanyrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.RemoveCrmCompanySecurity](../../models/operations/removecrmcompanysecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.RemoveCrmCompanyResponse](../../models/operations/removecrmcompanyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_contact(req, operations.RemoveCrmContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmContactRequest](../../models/operations/removecrmcontactrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.RemoveCrmContactSecurity](../../models/operations/removecrmcontactsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.RemoveCrmContactResponse](../../models/operations/removecrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_deal

Remove a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmDealRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_deal(req, operations.RemoveCrmDealSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmDealRequest](../../models/operations/removecrmdealrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.RemoveCrmDealSecurity](../../models/operations/removecrmdealsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.RemoveCrmDealResponse](../../models/operations/removecrmdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_event

Remove a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_event(req, operations.RemoveCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.RemoveCrmEventSecurity](../../models/operations/removecrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_lead

Remove a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmLeadRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_lead(req, operations.RemoveCrmLeadSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmLeadRequest](../../models/operations/removecrmleadrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.RemoveCrmLeadSecurity](../../models/operations/removecrmleadsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.RemoveCrmLeadResponse](../../models/operations/removecrmleadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_pipeline

Remove a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.remove_crm_pipeline(req, operations.RemoveCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveCrmPipelineSecurity](../../models/operations/removecrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_company

Update a company

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmCompanyRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_company(req, operations.UpdateCrmCompanySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_company is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmCompanyRequest](../../models/operations/updatecrmcompanyrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdateCrmCompanySecurity](../../models/operations/updatecrmcompanysecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdateCrmCompanyResponse](../../models/operations/updatecrmcompanyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_contact(req, operations.UpdateCrmContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmContactRequest](../../models/operations/updatecrmcontactrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdateCrmContactSecurity](../../models/operations/updatecrmcontactsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdateCrmContactResponse](../../models/operations/updatecrmcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_deal

Update a deal

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmDealRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_deal(req, operations.UpdateCrmDealSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_deal is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmDealRequest](../../models/operations/updatecrmdealrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdateCrmDealSecurity](../../models/operations/updatecrmdealsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdateCrmDealResponse](../../models/operations/updatecrmdealresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_event

Update a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_event(req, operations.UpdateCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.UpdateCrmEventSecurity](../../models/operations/updatecrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_lead

Update a lead

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmLeadRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_lead(req, operations.UpdateCrmLeadSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_lead is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmLeadRequest](../../models/operations/updatecrmleadrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpdateCrmLeadSecurity](../../models/operations/updatecrmleadsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpdateCrmLeadResponse](../../models/operations/updatecrmleadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.crm.update_crm_pipeline(req, operations.UpdateCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateCrmPipelineSecurity](../../models/operations/updatecrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
