# Uc
(*uc*)

### Available Operations

* [create_uc_contact](#create_uc_contact) - Create a contact
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [list_uc_agents](#list_uc_agents) - List all agents
* [list_uc_calls](#list_uc_calls) - List all calls
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
* [update_uc_contact](#update_uc_contact) - Update a contact

## create_uc_contact

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
                telephone='indigo indeed',
            ),
        ],
    ),
    connection_id='meanwhile',
    fields_=[
        'whose',
    ],
)

res = s.uc.create_uc_contact(req)

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


## get_uc_contact

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

req = operations.GetUcContactRequest(
    connection_id='JBOD ivory fool',
    fields_=[
        'Mouse',
    ],
    id='<ID>',
)

res = s.uc.get_uc_contact(req)

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


## list_uc_agents

List all agents

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

req = operations.ListUcAgentsRequest(
    connection_id='Representative',
    fields_=[
        'olive',
    ],
)

res = s.uc.list_uc_agents(req)

if res.uc_agents is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListUcAgentsRequest](../../models/operations/listucagentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListUcAgentsResponse](../../models/operations/listucagentsresponse.md)**


## list_uc_calls

List all calls

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

req = operations.ListUcCallsRequest(
    connection_id='optical',
    fields_=[
        'South',
    ],
)

res = s.uc.list_uc_calls(req)

if res.uc_calls is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcCallsRequest](../../models/operations/listuccallsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListUcCallsResponse](../../models/operations/listuccallsresponse.md)**


## list_uc_contacts

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

req = operations.ListUcContactsRequest(
    connection_id='Bicycle male',
    fields_=[
        'East',
    ],
)

res = s.uc.list_uc_contacts(req)

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


## patch_uc_contact

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
                telephone='male',
            ),
        ],
    ),
    connection_id='South Pants candela',
    fields_=[
        'Investor',
    ],
    id='<ID>',
)

res = s.uc.patch_uc_contact(req)

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


## remove_uc_contact

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

req = operations.RemoveUcContactRequest(
    connection_id='Configurable',
    id='<ID>',
)

res = s.uc.remove_uc_contact(req)

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


## update_uc_contact

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
                telephone='Illinois Electronic Northwest',
            ),
        ],
    ),
    connection_id='Cruiser',
    fields_=[
        'Awesome',
    ],
    id='<ID>',
)

res = s.uc.update_uc_contact(req)

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

