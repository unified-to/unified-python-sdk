# Lead

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
    connection_id='totam',
    id='6c3ae7d7-b67f-4eef-9e14-2d95b1dbecef',
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
    connection_id='voluptatibus',
    limit=4809.57,
    offset=7789.75,
    order='non',
    query='tempore',
    sort='quae',
    updated_gte=dateutil.parser.isoparse('2022-08-03T04:30:42.588Z'),
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
    connection_id='itaque',
    id='9278275e-ea76-4817-8680-63f799b7956c',
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
            address1='quae',
            address2='quidem',
            city='Fort Maddisontown',
            country='Paraguay',
            country_code='PY',
            postal_code='06209',
            region='reprehenderit',
            region_code='quo',
        ),
        company_id='incidunt',
        contact_id='id',
        created_at=dateutil.parser.isoparse('2021-10-20T07:58:35.149Z'),
        creator_user_id='quaerat',
        emails=[
            shared.CrmEmail(
                email='Giovanni48@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='657b01a0-7c08-4fd3-921c-257930d6f093',
        name='Earl Towne',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='aliquam',
                type=shared.CrmTelephoneType.HOME,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-13T09:05:51.677Z'),
        user_id='autem',
    ),
    connection_id='ea',
    id='dfa1011a-091b-43ec-8b53-862de1a9d14f',
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
            address1='debitis',
            address2='reprehenderit',
            city='Fort Fritzville',
            country='Bangladesh',
            country_code='ZA',
            postal_code='02028-9722',
            region='laudantium',
            region_code='velit',
        ),
        company_id='natus',
        contact_id='molestiae',
        created_at=dateutil.parser.isoparse('2020-03-03T18:07:31.494Z'),
        creator_user_id='hic',
        emails=[
            shared.CrmEmail(
                email='Hanna86@yahoo.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='2090fc15-7ac9-4fe1-961c-e9be41c869dd',
        name='Rosemarie Moen V',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='repellendus',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-04-24T12:06:20.344Z'),
        user_id='odit',
    ),
    connection_id='aut',
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
            address1='eaque',
            address2='deserunt',
            city='New Vito',
            country='Uruguay',
            country_code='ST',
            postal_code='63489',
            region='laudantium',
            region_code='sapiente',
        ),
        company_id='facere',
        contact_id='laudantium',
        created_at=dateutil.parser.isoparse('2022-09-11T02:42:21.444Z'),
        creator_user_id='fuga',
        emails=[
            shared.CrmEmail(
                email='Shannon73@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='620cd9c5-afdd-404c-b752-512beae1d87e',
        name='Roosevelt Hessel',
        raw=shared.PropertyCrmLeadRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='quod',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-12-04T00:59:07.070Z'),
        user_id='eveniet',
    ),
    connection_id='molestiae',
    id='a8831166-2cda-46d7-bc1d-86066237d422',
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

