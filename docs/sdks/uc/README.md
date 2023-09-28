# Uc
(*uc*)

### Available Operations

* [delete_uc_connection_id_contact_id](#delete_uc_connection_id_contact_id) - Remove a contact
* [get_uc_connection_id_agent](#get_uc_connection_id_agent) - List all agents
* [get_uc_connection_id_call](#get_uc_connection_id_call) - List all calls
* [get_uc_connection_id_contact](#get_uc_connection_id_contact) - List all contacts
* [get_uc_connection_id_contact_id](#get_uc_connection_id_contact_id) - Retrieve a contact
* [patch_uc_connection_id_contact_id](#patch_uc_connection_id_contact_id) - Update a contact
* [post_uc_connection_id_contact](#post_uc_connection_id_contact) - Create a contact
* [put_uc_connection_id_contact_id](#put_uc_connection_id_contact_id) - Update a contact

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

res = s.uc.delete_uc_connection_id_contact_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteUcConnectionIDContactIDRequest](../../models/operations/deleteucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteUcConnectionIDContactIDResponse](../../models/operations/deleteucconnectionidcontactidresponse.md)**


## get_uc_connection_id_agent

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

req = operations.GetUcConnectionIDAgentRequest(
    connection_id='Regional East Sedan',
    contact_id='blue',
    limit=7827.68,
    offset=2116.69,
    order='Bicycle',
    query='Bacon officia iterate',
    sort='sticky vote lumen',
    updated_gte=dateutil.parser.isoparse('2021-07-05T19:53:29.041Z'),
)

res = s.uc.get_uc_connection_id_agent(req)

if res.uc_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUcConnectionIDAgentRequest](../../models/operations/getucconnectionidagentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUcConnectionIDAgentResponse](../../models/operations/getucconnectionidagentresponse.md)**


## get_uc_connection_id_call

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

req = operations.GetUcConnectionIDCallRequest(
    agent_id='Directives',
    connection_id='female than',
    contact_id='reintermediate Enid Applications',
    limit=1980.39,
    offset=3478,
    order='white Oklahoma Functionality',
    query='pricing whether Hillsboro',
    sort='Wooden desensitize SCSI',
    updated_gte=dateutil.parser.isoparse('2021-11-03T12:40:46.997Z'),
)

res = s.uc.get_uc_connection_id_call(req)

if res.uc_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetUcConnectionIDCallRequest](../../models/operations/getucconnectionidcallrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetUcConnectionIDCallResponse](../../models/operations/getucconnectionidcallresponse.md)**


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

res = s.uc.get_uc_connection_id_contact(req)

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

res = s.uc.get_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetUcConnectionIDContactIDRequest](../../models/operations/getucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetUcConnectionIDContactIDResponse](../../models/operations/getucconnectionidcontactidresponse.md)**


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

res = s.uc.patch_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchUcConnectionIDContactIDRequest](../../models/operations/patchucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchUcConnectionIDContactIDResponse](../../models/operations/patchucconnectionidcontactidresponse.md)**


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

res = s.uc.post_uc_connection_id_contact(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostUcConnectionIDContactRequest](../../models/operations/postucconnectionidcontactrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PostUcConnectionIDContactResponse](../../models/operations/postucconnectionidcontactresponse.md)**


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

res = s.uc.put_uc_connection_id_contact_id(req)

if res.uc_contact is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutUcConnectionIDContactIDRequest](../../models/operations/putucconnectionidcontactidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutUcConnectionIDContactIDResponse](../../models/operations/putucconnectionidcontactidresponse.md)**

