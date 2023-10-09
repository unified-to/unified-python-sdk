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
    connection_id='Southeast Human Southeast',
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
    connection_id='Refined Practical',
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
        emails=[
            shared.UcEmail(
                email='Van84@hotmail.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='Denar',
            ),
        ],
    ),
    connection_id='strategy Synergized',
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
        emails=[
            shared.UcEmail(
                email='Gilda_Jacobs@gmail.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='Account Orchestrator',
            ),
        ],
    ),
    connection_id='extend grey Avon',
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
        emails=[
            shared.UcEmail(
                email='Darien12@hotmail.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='reboot',
            ),
        ],
    ),
    connection_id='payment hem',
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

