# contact

### Available Operations

* [delete_crm_connection_id_contact_id](#delete_crm_connection_id_contact_id) - Remove a contact
* [delete_crm_connection_id_contact_id_company_company_id](#delete_crm_connection_id_contact_id_company_company_id) - Remove company association from a contact
* [delete_crm_connection_id_contact_id_deal_deal_id](#delete_crm_connection_id_contact_id_deal_deal_id) - Remove deal association from a contact
* [delete_uc_connection_id_contact_id](#delete_uc_connection_id_contact_id) - Remove a contact
* [get_crm_connection_id_contact](#get_crm_connection_id_contact) - List all contacts
* [get_crm_connection_id_contact_id](#get_crm_connection_id_contact_id) - Retrieve a contact
* [get_uc_connection_id_contact](#get_uc_connection_id_contact) - List all contacts
* [get_uc_connection_id_contact_id](#get_uc_connection_id_contact_id) - Retrieve a contact
* [patch_crm_connection_id_contact_id](#patch_crm_connection_id_contact_id) - Update a contact
* [patch_crm_connection_id_contact_id_company_company_id](#patch_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [patch_crm_connection_id_contact_id_deal_deal_id](#patch_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [patch_uc_connection_id_contact_id](#patch_uc_connection_id_contact_id) - Update a contact
* [post_crm_connection_id_contact](#post_crm_connection_id_contact) - Create a contact
* [post_uc_connection_id_contact](#post_uc_connection_id_contact) - Create a contact
* [put_crm_connection_id_contact_id](#put_crm_connection_id_contact_id) - Update a contact
* [put_crm_connection_id_contact_id_company_company_id](#put_crm_connection_id_contact_id_company_company_id) - Associate a company with a contact
* [put_crm_connection_id_contact_id_deal_deal_id](#put_crm_connection_id_contact_id_deal_deal_id) - Associate a deal with a contact
* [put_uc_connection_id_contact_id](#put_uc_connection_id_contact_id) - Update a contact

## delete_crm_connection_id_contact_id

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDContactIDRequest(
    connection_id='molestias',
    id='57a9e618-76c6-4ab2-9d29-dfc94d6fecd7',
)

res = s.contact.delete_crm_connection_id_contact_id(req, operations.DeleteCrmConnectionIDContactIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteCrmConnectionIDContactIDRequest](../../models/operations/deletecrmconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.DeleteCrmConnectionIDContactIDSecurity](../../models/operations/deletecrmconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.DeleteCrmConnectionIDContactIDResponse](../../models/operations/deletecrmconnectionidcontactidresponse.md)**


## delete_crm_connection_id_contact_id_company_company_id

Remove company association from a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='iste',
    connection_id='provident',
    id='390066a6-d2d0-4003-9533-8cec086fa21e',
)

res = s.contact.delete_crm_connection_id_contact_id_company_company_id(req, operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/deletecrmconnectionidcontactidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |
| `security`                                                                                                                                             | [operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDSecurity](../../models/operations/deletecrmconnectionidcontactidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                                     | The security requirements to use for the request.                                                                                                      |


### Response

**[operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/deletecrmconnectionidcontactidcompanycompanyidresponse.md)**


## delete_crm_connection_id_contact_id_deal_deal_id

Remove deal association from a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='iste',
    deal_id='dicta',
    id='52cb3119-167b-48e3-88db-03408d6d364f',
)

res = s.contact.delete_crm_connection_id_contact_id_deal_deal_id(req, operations.DeleteCrmConnectionIDContactIDDealDealIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.DeleteCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/deletecrmconnectionidcontactiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `security`                                                                                                                                 | [operations.DeleteCrmConnectionIDContactIDDealDealIDSecurity](../../models/operations/deletecrmconnectionidcontactiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                         | The security requirements to use for the request.                                                                                          |


### Response

**[operations.DeleteCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/deletecrmconnectionidcontactiddealdealidresponse.md)**


## delete_uc_connection_id_contact_id

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUcConnectionIDContactIDRequest(
    connection_id='tenetur',
    id='d455906d-1263-4d48-a935-c2c9e81f30be',
)

res = s.contact.delete_uc_connection_id_contact_id(req, operations.DeleteUcConnectionIDContactIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteUcConnectionIDContactIDRequest](../../models/operations/deleteucconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.DeleteUcConnectionIDContactIDSecurity](../../models/operations/deleteucconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.DeleteUcConnectionIDContactIDResponse](../../models/operations/deleteucconnectionidcontactidresponse.md)**


## get_crm_connection_id_contact

List all contacts

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDContactRequest(
    company_id='sequi',
    connection_id='recusandae',
    deal_id='labore',
    limit=2406.24,
    offset=1667.41,
    order='aperiam',
    query='dolores',
    sort='illum',
    updated_gte=dateutil.parser.isoparse('2022-10-31T07:46:10.277Z'),
)

res = s.contact.get_crm_connection_id_contact(req, operations.GetCrmConnectionIDContactSecurity(
    jwt="",
))

if res.crm_contacts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCrmConnectionIDContactRequest](../../models/operations/getcrmconnectionidcontactrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetCrmConnectionIDContactSecurity](../../models/operations/getcrmconnectionidcontactsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetCrmConnectionIDContactResponse](../../models/operations/getcrmconnectionidcontactresponse.md)**


## get_crm_connection_id_contact_id

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDContactIDRequest(
    connection_id='beatae',
    id='65765066-4187-40d9-921f-9ad030c4ecc1',
)

res = s.contact.get_crm_connection_id_contact_id(req, operations.GetCrmConnectionIDContactIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetCrmConnectionIDContactIDRequest](../../models/operations/getcrmconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetCrmConnectionIDContactIDSecurity](../../models/operations/getcrmconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetCrmConnectionIDContactIDResponse](../../models/operations/getcrmconnectionidcontactidresponse.md)**


## get_uc_connection_id_contact

List all contacts

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDContactRequest(
    agent_id='beatae',
    connection_id='id',
    limit=90.6,
    offset=5515.76,
    order='ratione',
    query='iure',
    sort='tempora',
    updated_gte=dateutil.parser.isoparse('2022-05-21T02:14:12.604Z'),
)

res = s.contact.get_uc_connection_id_contact(req, operations.GetUcConnectionIDContactSecurity(
    jwt="",
))

if res.uc_contacts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetUcConnectionIDContactRequest](../../models/operations/getucconnectionidcontactrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetUcConnectionIDContactSecurity](../../models/operations/getucconnectionidcontactsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetUcConnectionIDContactResponse](../../models/operations/getucconnectionidcontactresponse.md)**


## get_uc_connection_id_contact_id

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDContactIDRequest(
    connection_id='voluptatem',
    id='68b8502a-55e7-4f73-bc84-5e320a319f4b',
)

res = s.contact.get_uc_connection_id_contact_id(req, operations.GetUcConnectionIDContactIDSecurity(
    jwt="",
))

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetUcConnectionIDContactIDRequest](../../models/operations/getucconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.GetUcConnectionIDContactIDSecurity](../../models/operations/getucconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.GetUcConnectionIDContactIDResponse](../../models/operations/getucconnectionidcontactidresponse.md)**


## patch_crm_connection_id_contact_id

Update a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDContactIDRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='dolorum',
            address2='quibusdam',
            city='Mission',
            country='El Salvador',
            country_code='KM',
            postal_code='66534-7721',
            region='magnam',
            region_code='dolores',
        ),
        company='Kemmer - Kassulke',
        company_ids=[
            'ad',
        ],
        created_at=dateutil.parser.isoparse('2022-11-07T21:20:17.353Z'),
        deal_ids=[
            'suscipit',
        ],
        emails=[
            shared.CrmEmail(
                email='Rupert_Russel@hotmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='f51fcb4c-593e-4c12-8daa-d0ec7afedbd8',
        name='Paulette White',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='corrupti',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-01-12T14:31:46.273Z'),
    ),
    connection_id='iste',
    id='390c5888-0983-4dab-b9ef-3ffdd9f7f079',
)

res = s.contact.patch_crm_connection_id_contact_id(req, operations.PatchCrmConnectionIDContactIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchCrmConnectionIDContactIDRequest](../../models/operations/patchcrmconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PatchCrmConnectionIDContactIDSecurity](../../models/operations/patchcrmconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PatchCrmConnectionIDContactIDResponse](../../models/operations/patchcrmconnectionidcontactidresponse.md)**


## patch_crm_connection_id_contact_id_company_company_id

Associate a company with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='similique',
    connection_id='asperiores',
    id='4d35724c-db0f-44d2-8118-7d56844eded8',
)

res = s.contact.patch_crm_connection_id_contact_id_company_company_id(req, operations.PatchCrmConnectionIDContactIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.PatchCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/patchcrmconnectionidcontactidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `security`                                                                                                                                           | [operations.PatchCrmConnectionIDContactIDCompanyCompanyIDSecurity](../../models/operations/patchcrmconnectionidcontactidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                                   | The security requirements to use for the request.                                                                                                    |


### Response

**[operations.PatchCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/patchcrmconnectionidcontactidcompanycompanyidresponse.md)**


## patch_crm_connection_id_contact_id_deal_deal_id

Associate a deal with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='enim',
    deal_id='animi',
    id='9065e628-bdfc-4203-ab6c-879923b7e135',
)

res = s.contact.patch_crm_connection_id_contact_id_deal_deal_id(req, operations.PatchCrmConnectionIDContactIDDealDealIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PatchCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/patchcrmconnectionidcontactiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `security`                                                                                                                               | [operations.PatchCrmConnectionIDContactIDDealDealIDSecurity](../../models/operations/patchcrmconnectionidcontactiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                       | The security requirements to use for the request.                                                                                        |


### Response

**[operations.PatchCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/patchcrmconnectionidcontactiddealdealidresponse.md)**


## patch_uc_connection_id_contact_id

Update a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchUcConnectionIDContactIDRequest(
    uc_contact=shared.UcContact(
        company='Graham - Zboncak',
        created_at=dateutil.parser.isoparse('2022-05-10T21:25:57.790Z'),
        emails=[
            shared.UcEmail(
                email='Augustine.Davis50@hotmail.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='1f82ce11-5717-4230-9377-dcfa89df975e',
        name='Erica Jerde',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='aliquid',
                type=shared.UcTelephoneType.WORK,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-01-25T19:10:58.985Z'),
    ),
    connection_id='unde',
    id='c3ddc5f1-11de-4a10-a6d5-41a4d190feb2',
)

res = s.contact.patch_uc_connection_id_contact_id(req, operations.PatchUcConnectionIDContactIDSecurity(
    jwt="",
))

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchUcConnectionIDContactIDRequest](../../models/operations/patchucconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PatchUcConnectionIDContactIDSecurity](../../models/operations/patchucconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PatchUcConnectionIDContactIDResponse](../../models/operations/patchucconnectionidcontactidresponse.md)**


## post_crm_connection_id_contact

Create a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostCrmConnectionIDContactRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='vitae',
            address2='odio',
            city='Amyacester',
            country='Slovenia',
            country_code='SI',
            postal_code='08778-8725',
            region='tempora',
            region_code='esse',
        ),
        company='Lowe Group',
        company_ids=[
            'facilis',
        ],
        created_at=dateutil.parser.isoparse('2022-01-29T03:16:14.679Z'),
        deal_ids=[
            'amet',
        ],
        emails=[
            shared.CrmEmail(
                email='Annetta_Torphy@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='158c4c4e-5459-49ea-b422-60e9b200ce78',
        name='Carl Rath',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='maiores',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-11-30T23:34:54.352Z'),
    ),
    connection_id='fuga',
)

res = s.contact.post_crm_connection_id_contact(req, operations.PostCrmConnectionIDContactSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostCrmConnectionIDContactRequest](../../models/operations/postcrmconnectionidcontactrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PostCrmConnectionIDContactSecurity](../../models/operations/postcrmconnectionidcontactsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PostCrmConnectionIDContactResponse](../../models/operations/postcrmconnectionidcontactresponse.md)**


## post_uc_connection_id_contact

Create a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostUcConnectionIDContactRequest(
    uc_contact=shared.UcContact(
        company='Braun and Sons',
        created_at=dateutil.parser.isoparse('2020-05-06T08:27:54.041Z'),
        emails=[
            shared.UcEmail(
                email='Caleb.Dickens1@yahoo.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='7fa30e9a-f725-4b29-9220-30d83f5aeb77',
        name='Mr. Tracy Shields',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='deleniti',
                type=shared.UcTelephoneType.FAX,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2021-05-16T15:40:19.045Z'),
    ),
    connection_id='magnam',
)

res = s.contact.post_uc_connection_id_contact(req, operations.PostUcConnectionIDContactSecurity(
    jwt="",
))

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostUcConnectionIDContactRequest](../../models/operations/postucconnectionidcontactrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.PostUcConnectionIDContactSecurity](../../models/operations/postucconnectionidcontactsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.PostUcConnectionIDContactResponse](../../models/operations/postucconnectionidcontactresponse.md)**


## put_crm_connection_id_contact_id

Update a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDContactIDRequest(
    crm_contact=shared.CrmContact(
        address=shared.PropertyCrmContactAddress(
            address1='perspiciatis',
            address2='amet',
            city='Braedenbury',
            country='Venezuela',
            country_code='SY',
            postal_code='31754-4817',
            region='consequuntur',
            region_code='possimus',
        ),
        company='Pollich, Haag and Rosenbaum',
        company_ids=[
            'hic',
        ],
        created_at=dateutil.parser.isoparse('2022-10-10T04:57:04.387Z'),
        deal_ids=[
            'nobis',
        ],
        emails=[
            shared.CrmEmail(
                email='Gladyce0@yahoo.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='841fb1bd-23fd-4b14-9b6b-e5a685998e22',
        name='Dr. Hugo Daugherty',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='quae',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2022-07-21T21:21:59.349Z'),
    ),
    connection_id='nam',
    id='271a289c-57e8-454e-9043-9d2224656946',
)

res = s.contact.put_crm_connection_id_contact_id(req, operations.PutCrmConnectionIDContactIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutCrmConnectionIDContactIDRequest](../../models/operations/putcrmconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.PutCrmConnectionIDContactIDSecurity](../../models/operations/putcrmconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.PutCrmConnectionIDContactIDResponse](../../models/operations/putcrmconnectionidcontactidresponse.md)**


## put_crm_connection_id_contact_id_company_company_id

Associate a company with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='explicabo',
    connection_id='modi',
    id='07084f7a-b37c-4ef0-a225-194db55410ad',
)

res = s.contact.put_crm_connection_id_contact_id_company_company_id(req, operations.PutCrmConnectionIDContactIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PutCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/putcrmconnectionidcontactidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |
| `security`                                                                                                                                       | [operations.PutCrmConnectionIDContactIDCompanyCompanyIDSecurity](../../models/operations/putcrmconnectionidcontactidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                               | The security requirements to use for the request.                                                                                                |


### Response

**[operations.PutCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/putcrmconnectionidcontactidcompanycompanyidresponse.md)**


## put_crm_connection_id_contact_id_deal_deal_id

Associate a deal with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='quo',
    deal_id='suscipit',
    id='69af90a2-6c7c-4dc9-81f0-68981d6bb33c',
)

res = s.contact.put_crm_connection_id_contact_id_deal_deal_id(req, operations.PutCrmConnectionIDContactIDDealDealIDSecurity(
    jwt="",
))

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PutCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/putcrmconnectionidcontactiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.PutCrmConnectionIDContactIDDealDealIDSecurity](../../models/operations/putcrmconnectionidcontactiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.PutCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/putcrmconnectionidcontactiddealdealidresponse.md)**


## put_uc_connection_id_contact_id

Update a contact

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutUcConnectionIDContactIDRequest(
    uc_contact=shared.UcContact(
        company='Murphy, Pfannerstill and Feest',
        created_at=dateutil.parser.isoparse('2022-06-26T16:56:56.149Z'),
        emails=[
            shared.UcEmail(
                email='Dax_Boehm30@hotmail.com',
                type=shared.UcEmailType.WORK,
            ),
        ],
        id='7ee4fcf0-c42b-478f-9562-6398a0dc7663',
        name='Jamie Schneider',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='accusantium',
                type=shared.UcTelephoneType.OTHER,
            ),
        ],
        title='Miss',
        updated_at=dateutil.parser.isoparse('2021-06-23T12:33:28.750Z'),
    ),
    connection_id='est',
    id='12d02529-270b-48d5-b22d-d895b8bcf24d',
)

res = s.contact.put_uc_connection_id_contact_id(req, operations.PutUcConnectionIDContactIDSecurity(
    jwt="",
))

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutUcConnectionIDContactIDRequest](../../models/operations/putucconnectionidcontactidrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PutUcConnectionIDContactIDSecurity](../../models/operations/putucconnectionidcontactidsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PutUcConnectionIDContactIDResponse](../../models/operations/putucconnectionidcontactidresponse.md)**

