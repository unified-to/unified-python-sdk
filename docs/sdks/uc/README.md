# uc

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUcConnectionIDContactIDRequest(
    connection_id='incidunt',
    id='52a9f01f-3442-4c61-be13-3bacde532b65',
)

res = s.uc.delete_uc_connection_id_contact_id(req, operations.DeleteUcConnectionIDContactIDSecurity(
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


## get_uc_connection_id_agent

List all agents

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDAgentRequest(
    connection_id='eos',
    contact_id='laboriosam',
    limit=9714.32,
    offset=5083.12,
    order='suscipit',
    query='explicabo',
    sort='quos',
    updated_gte=dateutil.parser.isoparse('2022-10-16T11:52:18.503Z'),
)

res = s.uc.get_uc_connection_id_agent(req, operations.GetUcConnectionIDAgentSecurity(
    jwt="",
))

if res.uc_agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetUcConnectionIDAgentRequest](../../models/operations/getucconnectionidagentrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.GetUcConnectionIDAgentSecurity](../../models/operations/getucconnectionidagentsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetUcConnectionIDAgentResponse](../../models/operations/getucconnectionidagentresponse.md)**


## get_uc_connection_id_call

List all calls

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDCallRequest(
    agent_id='hic',
    connection_id='eveniet',
    contact_id='eos',
    limit=5126.45,
    offset=3151.64,
    order='provident',
    query='maxime',
    sort='officiis',
    updated_gte=dateutil.parser.isoparse('2022-11-01T07:11:20.903Z'),
)

res = s.uc.get_uc_connection_id_call(req, operations.GetUcConnectionIDCallSecurity(
    jwt="",
))

if res.uc_calls is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUcConnectionIDCallRequest](../../models/operations/getucconnectionidcallrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetUcConnectionIDCallSecurity](../../models/operations/getucconnectionidcallsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetUcConnectionIDCallResponse](../../models/operations/getucconnectionidcallresponse.md)**


## get_uc_connection_id_contact

List all contacts

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUcConnectionIDContactRequest(
    agent_id='consequuntur',
    connection_id='quia',
    limit=1905.14,
    offset=718.84,
    order='doloribus',
    query='earum',
    sort='commodi',
    updated_gte=dateutil.parser.isoparse('2022-08-09T11:19:33.586Z'),
)

res = s.uc.get_uc_connection_id_contact(req, operations.GetUcConnectionIDContactSecurity(
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
    connection_id='dolore',
    id='c41d2fba-5cba-4069-b8d2-91beb810a2aa',
)

res = s.uc.get_uc_connection_id_contact_id(req, operations.GetUcConnectionIDContactIDSecurity(
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
        company='Kreiger - Gutmann',
        created_at=dateutil.parser.isoparse('2022-06-03T00:19:22.099Z'),
        emails=[
            shared.UcEmail(
                email='Leanna_Walsh26@yahoo.com',
                type=shared.UcEmailType.OTHER,
            ),
        ],
        id='cf7b50cf-87f0-48f3-9271-076a24b40c8f',
        name='Terry Rau',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='quae',
                type=shared.UcTelephoneType.WORK,
            ),
        ],
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-02-04T19:42:40.275Z'),
    ),
    connection_id='laudantium',
    id='8f86996c-8e22-4be0-a3cf-47893bd23f86',
)

res = s.uc.patch_uc_connection_id_contact_id(req, operations.PatchUcConnectionIDContactIDSecurity(
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
        company='Abbott - Beatty',
        created_at=dateutil.parser.isoparse('2021-10-06T16:45:34.362Z'),
        emails=[
            shared.UcEmail(
                email='Ova.Kovacek@gmail.com',
                type=shared.UcEmailType.WORK,
            ),
        ],
        id='273caa91-18b3-48f1-b61a-331a54dc1029',
        name='Johanna Muller',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='debitis',
                type=shared.UcTelephoneType.MOBILE,
            ),
        ],
        title='Miss',
        updated_at=dateutil.parser.isoparse('2022-05-29T03:50:25.472Z'),
    ),
    connection_id='expedita',
)

res = s.uc.post_uc_connection_id_contact(req, operations.PostUcConnectionIDContactSecurity(
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
        company='Lynch - Zemlak',
        created_at=dateutil.parser.isoparse('2022-11-29T18:41:38.693Z'),
        emails=[
            shared.UcEmail(
                email='Cary.McKenzie@hotmail.com',
                type=shared.UcEmailType.OTHER,
            ),
        ],
        id='20ee1228-ac3a-4dc6-87d2-40bc11ea4828',
        name='Danielle Schamberger',
        raw=shared.PropertyUcContactRaw(),
        telephones=[
            shared.UcTelephone(
                telephone='aliquid',
                type=shared.UcTelephoneType.FAX,
            ),
        ],
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2022-10-31T15:11:09.832Z'),
    ),
    connection_id='reiciendis',
    id='5b9d3cb1-1a76-487d-b100-e8e2b9b0d746',
)

res = s.uc.put_uc_connection_id_contact_id(req, operations.PutUcConnectionIDContactIDSecurity(
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

