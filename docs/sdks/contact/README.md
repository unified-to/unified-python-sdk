# Contact
(*contact*)

### Available Operations

* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_uc_contact](#create_uc_contact) - Create a contact
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_uc_contact](#update_uc_contact) - Update a contact

## create_crm_contact

Create a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

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

res = s.contact.create_crm_contact(req)

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

## create_uc_contact

Create a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateUcContactRequest(
    uc_contact=shared.UcContact(
        emails=[
            shared.UcEmail(
                email='Dulce_Becker30@yahoo.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
)

res = s.contact.create_uc_contact(req)

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateUcContactRequest](../../models/operations/createuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateUcContactResponse](../../models/operations/createuccontactresponse.md)**
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

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCrmContactRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.contact.get_crm_contact(req)

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

## get_uc_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetUcContactRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.contact.get_uc_contact(req)

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetUcContactRequest](../../models/operations/getuccontactrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetUcContactResponse](../../models/operations/getuccontactresponse.md)**
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

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListCrmContactsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.contact.list_crm_contacts(req)

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

## list_uc_contacts

List all contacts

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListUcContactsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.contact.list_uc_contacts(req)

if res.uc_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListUcContactsRequest](../../models/operations/listuccontactsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ListUcContactsResponse](../../models/operations/listuccontactsresponse.md)**
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

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

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

res = s.contact.patch_crm_contact(req)

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

## patch_uc_contact

Update a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchUcContactRequest(
    uc_contact=shared.UcContact(
        emails=[
            shared.UcEmail(
                email='Norene_Boehm97@hotmail.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.contact.patch_uc_contact(req)

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchUcContactRequest](../../models/operations/patchuccontactrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PatchUcContactResponse](../../models/operations/patchuccontactresponse.md)**
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

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCrmContactRequest(
    connection_id='string',
    id='<ID>',
)

res = s.contact.remove_crm_contact(req)

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

## remove_uc_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveUcContactRequest(
    connection_id='string',
    id='<ID>',
)

res = s.contact.remove_uc_contact(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveUcContactRequest](../../models/operations/removeuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RemoveUcContactResponse](../../models/operations/removeuccontactresponse.md)**
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

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

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

res = s.contact.update_crm_contact(req)

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

## update_uc_contact

Update a contact

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateUcContactRequest(
    uc_contact=shared.UcContact(
        emails=[
            shared.UcEmail(
                email='Kianna.Witting90@gmail.com',
            ),
        ],
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.contact.update_uc_contact(req)

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateUcContactRequest](../../models/operations/updateuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateUcContactResponse](../../models/operations/updateuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
