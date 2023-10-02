# Contact
(*contact*)

### Available Operations

* [delete_crm_connection_id_contact_id](#delete_crm_connection_id_contact_id) - Remove a contact
* [delete_uc_connection_id_contact_id](#delete_uc_connection_id_contact_id) - Remove a contact
* [get_crm_connection_id_contact](#get_crm_connection_id_contact) - List all contacts
* [get_crm_connection_id_contact_id](#get_crm_connection_id_contact_id) - Retrieve a contact
* [get_uc_connection_id_contact](#get_uc_connection_id_contact) - List all contacts
* [get_uc_connection_id_contact_id](#get_uc_connection_id_contact_id) - Retrieve a contact
* [patch_crm_connection_id_contact_id](#patch_crm_connection_id_contact_id) - Update a contact
* [patch_uc_connection_id_contact_id](#patch_uc_connection_id_contact_id) - Update a contact
* [post_crm_connection_id_contact](#post_crm_connection_id_contact) - Create a contact
* [post_uc_connection_id_contact](#post_uc_connection_id_contact) - Create a contact
* [put_crm_connection_id_contact_id](#put_crm_connection_id_contact_id) - Update a contact
* [put_uc_connection_id_contact_id](#put_uc_connection_id_contact_id) - Update a contact

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

res = s.contact.delete_crm_connection_id_contact_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteCrmConnectionIDContactIDRequest](../../models/operations/deletecrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteCrmConnectionIDContactIDResponse](../../models/operations/deletecrmconnectionidcontactidresponse.md)**


## delete_uc_connection_id_contact_id

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

req = operations.DeleteUcConnectionIDContactIDRequest(
    connection_id='Southeast Modern commonly',
    id='<ID>',
)

res = s.contact.delete_uc_connection_id_contact_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteUcConnectionIDContactIDRequest](../../models/operations/deleteucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteUcConnectionIDContactIDResponse](../../models/operations/deleteucconnectionidcontactidresponse.md)**


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

res = s.contact.get_crm_connection_id_contact(req)

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

res = s.contact.get_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCrmConnectionIDContactIDRequest](../../models/operations/getcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCrmConnectionIDContactIDResponse](../../models/operations/getcrmconnectionidcontactidresponse.md)**


## get_uc_connection_id_contact

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

req = operations.GetUcConnectionIDContactRequest(
    agent_id='Refined Practical',
    connection_id='inasmuch Dodge',
    limit=7215.14,
    offset=2910.48,
    order='Vermont',
    query='maroon JBOD',
    sort='hertz',
    updated_gte=dateutil.parser.isoparse('2023-01-29T17:06:35.136Z'),
)

res = s.contact.get_uc_connection_id_contact(req)

if res.uc_contacts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetUcConnectionIDContactRequest](../../models/operations/getucconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetUcConnectionIDContactResponse](../../models/operations/getucconnectionidcontactresponse.md)**


## get_uc_connection_id_contact_id

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

req = operations.GetUcConnectionIDContactIDRequest(
    connection_id='Land',
    id='<ID>',
)

res = s.contact.get_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetUcConnectionIDContactIDRequest](../../models/operations/getucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetUcConnectionIDContactIDResponse](../../models/operations/getucconnectionidcontactidresponse.md)**


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

res = s.contact.patch_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchCrmConnectionIDContactIDRequest](../../models/operations/patchcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PatchCrmConnectionIDContactIDResponse](../../models/operations/patchcrmconnectionidcontactidresponse.md)**


## patch_uc_connection_id_contact_id

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

req = operations.PatchUcConnectionIDContactIDRequest(
    uc_contact=shared.UcContact(
        company='Wilderman, Cremin and Gislason',
        created_at=dateutil.parser.isoparse('2023-07-18T06:13:06.229Z'),
        emails=[
            shared.UcEmail(
                email='Henry.Leannon@gmail.com',
                type=shared.UcEmailType.OTHER,
            ),
        ],
        id='<ID>',
        name='quirky digital',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='Lead 24/7 overriding',
                type=shared.UcTelephoneType.OTHER,
            ),
        ],
        title='Small Legacy',
        updated_at=dateutil.parser.isoparse('2022-07-11T16:02:41.922Z'),
    ),
    connection_id='Bohrium',
    id='<ID>',
)

res = s.contact.patch_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchUcConnectionIDContactIDRequest](../../models/operations/patchucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchUcConnectionIDContactIDResponse](../../models/operations/patchucconnectionidcontactidresponse.md)**


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

res = s.contact.post_crm_connection_id_contact(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostCrmConnectionIDContactRequest](../../models/operations/postcrmconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostCrmConnectionIDContactResponse](../../models/operations/postcrmconnectionidcontactresponse.md)**


## post_uc_connection_id_contact

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

req = operations.PostUcConnectionIDContactRequest(
    uc_contact=shared.UcContact(
        company='Howell and Sons',
        created_at=dateutil.parser.isoparse('2022-12-18T04:56:44.573Z'),
        emails=[
            shared.UcEmail(
                email='Garret81@hotmail.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='Southeast Gasoline extend',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='Togo Division Human',
                type=shared.UcTelephoneType.HOME,
            ),
        ],
        title='COM that',
        updated_at=dateutil.parser.isoparse('2023-02-07T16:19:58.439Z'),
    ),
    connection_id='Tennessee',
)

res = s.contact.post_uc_connection_id_contact(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostUcConnectionIDContactRequest](../../models/operations/postucconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PostUcConnectionIDContactResponse](../../models/operations/postucconnectionidcontactresponse.md)**


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

res = s.contact.put_crm_connection_id_contact_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutCrmConnectionIDContactIDRequest](../../models/operations/putcrmconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutCrmConnectionIDContactIDResponse](../../models/operations/putcrmconnectionidcontactidresponse.md)**


## put_uc_connection_id_contact_id

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

req = operations.PutUcConnectionIDContactIDRequest(
    uc_contact=shared.UcContact(
        company='Feeney, Gusikowski and Douglas',
        created_at=dateutil.parser.isoparse('2021-05-15T18:36:56.888Z'),
        emails=[
            shared.UcEmail(
                email='Katrina.Walker@gmail.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='Investment Hip Southwest',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='powerless Shirt',
                type=shared.UcTelephoneType.FAX,
            ),
        ],
        title='Wooden Buckinghamshire',
        updated_at=dateutil.parser.isoparse('2022-10-29T19:58:07.810Z'),
    ),
    connection_id='doubtfully',
    id='<ID>',
)

res = s.contact.put_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutUcConnectionIDContactIDRequest](../../models/operations/putucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutUcConnectionIDContactIDResponse](../../models/operations/putucconnectionidcontactidresponse.md)**

