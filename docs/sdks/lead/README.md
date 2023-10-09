# Lead
(*lead*)

### Available Operations

* [delete_crm_connection_id_lead_id](#delete_crm_connection_id_lead_id) - Remove a lead
* [get_crm_connection_id_lead](#get_crm_connection_id_lead) - List all leads
* [get_crm_connection_id_lead_id](#get_crm_connection_id_lead_id) - Retrieve a lead
* [patch_crm_connection_id_lead_id](#patch_crm_connection_id_lead_id) - Update a lead
* [post_crm_connection_id_lead](#post_crm_connection_id_lead) - Create a lead
* [put_crm_connection_id_lead_id](#put_crm_connection_id_lead_id) - Update a lead

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

res = s.lead.delete_crm_connection_id_lead_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDLeadIDRequest](../../models/operations/deletecrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDLeadIDResponse](../../models/operations/deletecrmconnectionidleadidresponse.md)**


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

res = s.lead.get_crm_connection_id_lead(req)

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

res = s.lead.get_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDLeadIDRequest](../../models/operations/getcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDLeadIDResponse](../../models/operations/getcrmconnectionidleadidresponse.md)**


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

res = s.lead.patch_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDLeadIDRequest](../../models/operations/patchcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDLeadIDResponse](../../models/operations/patchcrmconnectionidleadidresponse.md)**


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

res = s.lead.post_crm_connection_id_lead(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDLeadRequest](../../models/operations/postcrmconnectionidleadrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDLeadResponse](../../models/operations/postcrmconnectionidleadresponse.md)**


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

res = s.lead.put_crm_connection_id_lead_id(req)

if res.crm_lead is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDLeadIDRequest](../../models/operations/putcrmconnectionidleadidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDLeadIDResponse](../../models/operations/putcrmconnectionidleadidresponse.md)**

