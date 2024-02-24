# Lead
(*lead*)

### Available Operations

* [create_crm_lead](#create_crm_lead) - Create a lead
* [get_crm_lead](#get_crm_lead) - Retrieve a lead
* [list_crm_leads](#list_crm_leads) - List all leads
* [patch_crm_lead](#patch_crm_lead) - Update a lead
* [remove_crm_lead](#remove_crm_lead) - Remove a lead
* [update_crm_lead](#update_crm_lead) - Update a lead

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

res = s.lead.create_crm_lead(req, operations.CreateCrmLeadSecurity(
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

res = s.lead.get_crm_lead(req, operations.GetCrmLeadSecurity(
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

res = s.lead.list_crm_leads(req, operations.ListCrmLeadsSecurity(
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

res = s.lead.patch_crm_lead(req, operations.PatchCrmLeadSecurity(
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

res = s.lead.remove_crm_lead(req, operations.RemoveCrmLeadSecurity(
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

res = s.lead.update_crm_lead(req, operations.UpdateCrmLeadSecurity(
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
