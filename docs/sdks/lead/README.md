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
    limit=7411.81,
    offset=9004.32,
    order='Operations candela Integration',
    query='impactful transform',
    sort='Tala defense Southwest',
    updated_gte=dateutil.parser.isoparse('2021-09-29T00:37:32.184Z'),
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

