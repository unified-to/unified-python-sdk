# Contact
(*contact*)

### Available Operations

* [create_accounting_contact](#create_accounting_contact) - Create a contact
* [create_crm_contact](#create_crm_contact) - Create a contact
* [create_uc_contact](#create_uc_contact) - Create a contact
* [get_accounting_contact](#get_accounting_contact) - Retrieve a contact
* [get_crm_contact](#get_crm_contact) - Retrieve a contact
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [list_accounting_contacts](#list_accounting_contacts) - List all contacts
* [list_crm_contacts](#list_crm_contacts) - List all contacts
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [patch_accounting_contact](#patch_accounting_contact) - Update a contact
* [patch_crm_contact](#patch_crm_contact) - Update a contact
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [remove_accounting_contact](#remove_accounting_contact) - Remove a contact
* [remove_crm_contact](#remove_crm_contact) - Remove a contact
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
* [update_accounting_contact](#update_accounting_contact) - Update a contact
* [update_crm_contact](#update_crm_contact) - Update a contact
* [update_uc_contact](#update_uc_contact) - Update a contact

## create_accounting_contact

Create a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateAccountingContactRequest(
    connection_id='<value>',
)

res = s.contact.create_accounting_contact(req, operations.CreateAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingContactRequest](../../models/operations/createaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateAccountingContactSecurity](../../models/operations/createaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateAccountingContactResponse](../../models/operations/createaccountingcontactresponse.md)**
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

res = s.contact.create_crm_contact(req, operations.CreateCrmContactSecurity(
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

## create_uc_contact

Create a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateUcContactRequest(
    connection_id='<value>',
)

res = s.contact.create_uc_contact(req, operations.CreateUcContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateUcContactRequest](../../models/operations/createuccontactrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.CreateUcContactSecurity](../../models/operations/createuccontactsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.CreateUcContactResponse](../../models/operations/createuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_accounting_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.get_accounting_contact(req, operations.GetAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingContactRequest](../../models/operations/getaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetAccountingContactSecurity](../../models/operations/getaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetAccountingContactResponse](../../models/operations/getaccountingcontactresponse.md)**
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

res = s.contact.get_crm_contact(req, operations.GetCrmContactSecurity(
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

## get_uc_contact

Retrieve a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.get_uc_contact(req, operations.GetUcContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetUcContactRequest](../../models/operations/getuccontactrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.GetUcContactSecurity](../../models/operations/getuccontactsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.GetUcContactResponse](../../models/operations/getuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_contacts

List all contacts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingContactsRequest(
    connection_id='<value>',
)

res = s.contact.list_accounting_contacts(req, operations.ListAccountingContactsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingContactsRequest](../../models/operations/listaccountingcontactsrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListAccountingContactsSecurity](../../models/operations/listaccountingcontactssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListAccountingContactsResponse](../../models/operations/listaccountingcontactsresponse.md)**
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

res = s.contact.list_crm_contacts(req, operations.ListCrmContactsSecurity(
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

## list_uc_contacts

List all contacts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUcContactsRequest(
    connection_id='<value>',
)

res = s.contact.list_uc_contacts(req, operations.ListUcContactsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_contacts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListUcContactsRequest](../../models/operations/listuccontactsrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.ListUcContactsSecurity](../../models/operations/listuccontactssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.ListUcContactsResponse](../../models/operations/listuccontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_accounting_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.patch_accounting_contact(req, operations.PatchAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingContactRequest](../../models/operations/patchaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchAccountingContactSecurity](../../models/operations/patchaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchAccountingContactResponse](../../models/operations/patchaccountingcontactresponse.md)**
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

res = s.contact.patch_crm_contact(req, operations.PatchCrmContactSecurity(
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

## patch_uc_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchUcContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.patch_uc_contact(req, operations.PatchUcContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchUcContactRequest](../../models/operations/patchuccontactrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PatchUcContactSecurity](../../models/operations/patchuccontactsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PatchUcContactResponse](../../models/operations/patchuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_accounting_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.remove_accounting_contact(req, operations.RemoveAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingContactRequest](../../models/operations/removeaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveAccountingContactSecurity](../../models/operations/removeaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveAccountingContactResponse](../../models/operations/removeaccountingcontactresponse.md)**
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

res = s.contact.remove_crm_contact(req, operations.RemoveCrmContactSecurity(
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

## remove_uc_contact

Remove a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveUcContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.remove_uc_contact(req, operations.RemoveUcContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveUcContactRequest](../../models/operations/removeuccontactrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.RemoveUcContactSecurity](../../models/operations/removeuccontactsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.RemoveUcContactResponse](../../models/operations/removeuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_accounting_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateAccountingContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.update_accounting_contact(req, operations.UpdateAccountingContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingContactRequest](../../models/operations/updateaccountingcontactrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateAccountingContactSecurity](../../models/operations/updateaccountingcontactsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateAccountingContactResponse](../../models/operations/updateaccountingcontactresponse.md)**
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

res = s.contact.update_crm_contact(req, operations.UpdateCrmContactSecurity(
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

## update_uc_contact

Update a contact

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateUcContactRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.contact.update_uc_contact(req, operations.UpdateUcContactSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.uc_contact is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateUcContactRequest](../../models/operations/updateuccontactrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.UpdateUcContactSecurity](../../models/operations/updateuccontactsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.UpdateUcContactResponse](../../models/operations/updateuccontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
