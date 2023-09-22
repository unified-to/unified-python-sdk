# Contact

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDContactIDRequest(
    connection_id='porro',
    id='6ab21d29-dfc9-44d6-becd-799390066a6d',
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


## delete_crm_connection_id_contact_id_company_company_id

Remove company association from a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='explicabo',
    connection_id='fugiat',
    id='00035533-8cec-4086-ba21-e9152cb31191',
)

res = s.contact.delete_crm_connection_id_contact_id_company_company_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/deletecrmconnectionidcontactidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |


### Response

**[operations.DeleteCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/deletecrmconnectionidcontactidcompanycompanyidresponse.md)**


## delete_crm_connection_id_contact_id_deal_deal_id

Remove deal association from a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='autem',
    deal_id='ducimus',
    id='b8e3c8db-0340-48d6-9364-ffd455906d12',
)

res = s.contact.delete_crm_connection_id_contact_id_deal_deal_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.DeleteCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/deletecrmconnectionidcontactiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.DeleteCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/deletecrmconnectionidcontactiddealdealidresponse.md)**


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
    connection_id='commodi',
    id='3d48e935-c2c9-4e81-b30b-e3e43202d721',
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
    company_id='aliquid',
    connection_id='ad',
    deal_id='voluptate',
    limit=4265.94,
    offset=3249.99,
    order='sit',
    query='vel',
    sort='laboriosam',
    updated_gte=dateutil.parser.isoparse('2022-11-27T15:29:14.022Z'),
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
    connection_id='rem',
    id='70d9d21f-9ad0-430c-8ecc-11a083642906',
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
    agent_id='laudantium',
    connection_id='facilis',
    limit=5146.09,
    offset=3530.75,
    order='aut',
    query='quia',
    sort='officia',
    updated_gte=dateutil.parser.isoparse('2022-08-22T02:23:15.742Z'),
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
    connection_id='accusamus',
    id='7f73bc84-5e32-40a3-99f4-badf947c9a86',
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
            address1='nihil',
            address2='facilis',
            city='Goyetteberg',
            country='French Polynesia',
            country_code='CH',
            postal_code='44350',
            region='suscipit',
            region_code='quibusdam',
        ),
        company='Russel, Nader and Little',
        company_ids=[
            'voluptates',
        ],
        created_at=dateutil.parser.isoparse('2021-11-25T22:17:39.417Z'),
        deal_ids=[
            'illo',
        ],
        emails=[
            shared.CrmEmail(
                email='Nyasia76@hotmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='93ec12cd-aad0-4ec7-afed-bd80df448a47',
        name='Jackie Fahey DDS',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='minima',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-12-11T07:04:52.187Z'),
    ),
    connection_id='provident',
    id='83dabf9e-f3ff-4dd9-b7f0-79af4d35724c',
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


## patch_crm_connection_id_contact_id_company_company_id

Associate a company with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='fugiat',
    connection_id='soluta',
    id='0f4d2811-87d5-4684-8ede-d85a9065e628',
)

res = s.contact.patch_crm_connection_id_contact_id_company_company_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.PatchCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/patchcrmconnectionidcontactidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.PatchCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/patchcrmconnectionidcontactidcompanycompanyidresponse.md)**


## patch_crm_connection_id_contact_id_deal_deal_id

Associate a deal with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='quidem',
    deal_id='illum',
    id='fc2032b6-c879-4923-b7e1-3584f7ae12c6',
)

res = s.contact.patch_crm_connection_id_contact_id_deal_deal_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.PatchCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/patchcrmconnectionidcontactiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.PatchCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/patchcrmconnectionidcontactiddealdealidresponse.md)**


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
        company='Morissette - Brown',
        created_at=dateutil.parser.isoparse('2021-06-15T21:46:49.215Z'),
        emails=[
            shared.UcEmail(
                email='Nicolas8@gmail.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='71723053-77dc-4fa8-9df9-75e356686092',
        name='Austin Runte',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='temporibus',
                type=shared.UcTelephoneType.FAX,
            ),
        ],
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-09-08T04:57:24.220Z'),
    ),
    connection_id='vitae',
    id='1dea1026-d541-4a4d-990f-eb21780bccc0',
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
            address1='possimus',
            address2='distinctio',
            city='Shanahanhaven',
            country='Saint Helena',
            country_code='FR',
            postal_code='24059-7392',
            region='natus',
            region_code='ab',
        ),
        company='Keeling, Prohaska and Schowalter',
        company_ids=[
            'ab',
        ],
        created_at=dateutil.parser.isoparse('2022-07-02T04:44:41.833Z'),
        deal_ids=[
            'porro',
        ],
        emails=[
            shared.CrmEmail(
                email='Omer.Graham25@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='99ea3422-60e9-4b20-8ce7-8a1bd8fb7a0a',
        name='Julie Homenick',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='dignissimos',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2022-01-24T20:30:44.279Z'),
    ),
    connection_id='aut',
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
        company='Koch - Windler',
        created_at=dateutil.parser.isoparse('2022-08-16T16:49:13.505Z'),
        emails=[
            shared.UcEmail(
                email='Sonia_Morar@gmail.com',
                type=shared.UcEmailType.HOME,
            ),
        ],
        id='25b29122-030d-483f-9aeb-7799d22e8c1f',
        name='Clifford Mertz',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='sunt',
                type=shared.UcTelephoneType.HOME,
            ),
        ],
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2020-08-28T22:20:14.231Z'),
    ),
    connection_id='quaerat',
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
            address1='magni',
            address2='cumque',
            city='Isidroview',
            country='Singapore',
            country_code='CA',
            postal_code='18963-7970',
            region='nobis',
            region_code='esse',
        ),
        company='Christiansen - Donnelly',
        company_ids=[
            'alias',
        ],
        created_at=dateutil.parser.isoparse('2021-05-04T15:01:38.967Z'),
        deal_ids=[
            'numquam',
        ],
        emails=[
            shared.CrmEmail(
                email='Will69@gmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='23fdb14d-b6be-45a6-8599-8e22ae20da16',
        name='Sylvester Cormier',
        raw=shared.PropertyCrmContactRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='iusto',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        title='Miss',
        updated_at=dateutil.parser.isoparse('2022-07-01T20:28:02.172Z'),
    ),
    connection_id='sint',
    id='c57e854e-9043-49d2-a246-569462407084',
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


## put_crm_connection_id_contact_id_company_company_id

Associate a company with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDContactIDCompanyCompanyIDRequest(
    company_id='delectus',
    connection_id='quam',
    id='ab37cef0-2225-4194-9b55-410adc669af9',
)

res = s.contact.put_crm_connection_id_contact_id_company_company_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PutCrmConnectionIDContactIDCompanyCompanyIDRequest](../../models/operations/putcrmconnectionidcontactidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PutCrmConnectionIDContactIDCompanyCompanyIDResponse](../../models/operations/putcrmconnectionidcontactidcompanycompanyidresponse.md)**


## put_crm_connection_id_contact_id_deal_deal_id

Associate a deal with a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDContactIDDealDealIDRequest(
    connection_id='alias',
    deal_id='deserunt',
    id='26c7cdc9-81f0-4689-81d6-bb33cfaa348c',
)

res = s.contact.put_crm_connection_id_contact_id_deal_deal_id(req)

if res.crm_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PutCrmConnectionIDContactIDDealDealIDRequest](../../models/operations/putcrmconnectionidcontactiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PutCrmConnectionIDContactIDDealDealIDResponse](../../models/operations/putcrmconnectionidcontactiddealdealidresponse.md)**


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
        company='Boehm LLC',
        created_at=dateutil.parser.isoparse('2022-02-04T10:58:23.701Z'),
        emails=[
            shared.UcEmail(
                email='Jerrold.Watsica98@gmail.com',
                type=shared.UcEmailType.OTHER,
            ),
        ],
        id='f0c42b78-f156-4263-98a0-dc766324ccb0',
        name='Leticia Leannon',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='inventore',
                type=shared.UcTelephoneType.WORK,
            ),
        ],
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2022-10-30T04:54:37.407Z'),
    ),
    connection_id='enim',
    id='29270b8d-5722-4dd8-95b8-bcf24db95969',
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

