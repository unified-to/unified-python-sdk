# user

### Available Operations

* [delete_crm_connection_id_user_id](#delete_crm_connection_id_user_id) - Remove a user
* [delete_unified_user](#delete_unified_user) - Delete your user object
* [get_crm_connection_id_user](#get_crm_connection_id_user) - List all users
* [get_crm_connection_id_user_id](#get_crm_connection_id_user_id) - Retrieve a user
* [get_unified_user](#get_unified_user) - Retrieve your user object
* [get_unified_user_token](#get_unified_user_token) - Retrieve your user token
* [patch_crm_connection_id_user_id](#patch_crm_connection_id_user_id) - Update a user
* [patch_unified_user](#patch_unified_user) - Updates your user object
* [post_crm_connection_id_user](#post_crm_connection_id_user) - Create a user
* [put_crm_connection_id_user_id](#put_crm_connection_id_user_id) - Update a user
* [put_unified_user](#put_unified_user) - Updates your user object

## delete_crm_connection_id_user_id

Remove a user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDUserIDRequest(
    connection_id='deleniti',
    id='b1d187b5-1eb5-4fd3-8bfe-03490cf20254',
)

res = s.user.delete_crm_connection_id_user_id(req, operations.DeleteCrmConnectionIDUserIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCrmConnectionIDUserIDRequest](../../models/operations/deletecrmconnectioniduseridrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.DeleteCrmConnectionIDUserIDSecurity](../../models/operations/deletecrmconnectioniduseridsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.DeleteCrmConnectionIDUserIDResponse](../../models/operations/deletecrmconnectioniduseridresponse.md)**


## delete_unified_user

Delete your user object

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.delete_unified_user(operations.DeleteUnifiedUserSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.DeleteUnifiedUserSecurity](../../models/operations/deleteunifiedusersecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.DeleteUnifiedUserResponse](../../models/operations/deleteunifieduserresponse.md)**


## get_crm_connection_id_user

List all users

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDUserRequest(
    connection_id='id',
    limit=6080.08,
    offset=3220.16,
    order='unde',
    query='consequatur',
    sort='quaerat',
    updated_gte=dateutil.parser.isoparse('2022-03-13T04:13:10.861Z'),
)

res = s.user.get_crm_connection_id_user(req, operations.GetCrmConnectionIDUserSecurity(
    jwt="",
))

if res.crm_users is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCrmConnectionIDUserRequest](../../models/operations/getcrmconnectioniduserrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.GetCrmConnectionIDUserSecurity](../../models/operations/getcrmconnectionidusersecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.GetCrmConnectionIDUserResponse](../../models/operations/getcrmconnectioniduserresponse.md)**


## get_crm_connection_id_user_id

Retrieve a user

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDUserIDRequest(
    connection_id='distinctio',
    id='462d6bc9-917f-498e-8792-b979a413d6a8',
)

res = s.user.get_crm_connection_id_user_id(req, operations.GetCrmConnectionIDUserIDSecurity(
    jwt="",
))

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDUserIDRequest](../../models/operations/getcrmconnectioniduseridrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.GetCrmConnectionIDUserIDSecurity](../../models/operations/getcrmconnectioniduseridsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.GetCrmConnectionIDUserIDResponse](../../models/operations/getcrmconnectioniduseridresponse.md)**


## get_unified_user

Retrieve your user object

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.get_unified_user(operations.GetUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `security`                                                                             | [operations.GetUnifiedUserSecurity](../../models/operations/getunifiedusersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetUnifiedUserResponse](../../models/operations/getunifieduserresponse.md)**


## get_unified_user_token

Retrieve your user token

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.user.get_unified_user_token(operations.GetUnifiedUserTokenSecurity(
    jwt="",
))

if res.get_unified_user_token_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `security`                                                                                       | [operations.GetUnifiedUserTokenSecurity](../../models/operations/getunifiedusertokensecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedUserTokenResponse](../../models/operations/getunifiedusertokenresponse.md)**


## patch_crm_connection_id_user_id

Update a user

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='impedit',
            address2='perspiciatis',
            city='South Josianeberg',
            country='Papua New Guinea',
            country_code='TG',
            postal_code='40808-6577',
            region='repellat',
            region_code='voluptatum',
        ),
        created_at=dateutil.parser.isoparse('2021-04-22T20:59:04.118Z'),
        currency='amet',
        department='totam',
        division='ex',
        emails=[
            shared.CrmEmail(
                email='Bennie_Langosh@gmail.com',
                type=shared.CrmEmailType.OTHER,
            ),
        ],
        id='76c002fa-cb13-4ac2-8c81-43b866c575a1',
        image_url='recusandae',
        language_locale='quia',
        name='Carla Lubowitz',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='accusantium',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        timezone='accusamus',
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-04-24T03:57:57.473Z'),
    ),
    connection_id='sit',
    id='e8fbc48d-dc7e-469b-9351-0505014dca10',
)

res = s.user.patch_crm_connection_id_user_id(req, operations.PatchCrmConnectionIDUserIDSecurity(
    jwt="",
))

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchCrmConnectionIDUserIDRequest](../../models/operations/patchcrmconnectioniduseridrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchCrmConnectionIDUserIDSecurity](../../models/operations/patchcrmconnectioniduseridsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchCrmConnectionIDUserIDResponse](../../models/operations/patchcrmconnectioniduseridresponse.md)**


## patch_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.User(
    created_at=dateutil.parser.isoparse('2022-06-17T20:12:07.816Z'),
    email='Candido.Hahn@yahoo.com',
    environment='impedit',
    id='36e94889-2782-4d34-a0b8-fc0d59f57b9f',
    meta=shared.PropertyUserMeta(),
    name='Miss Ian Connelly',
    updated_at=dateutil.parser.isoparse('2022-07-09T07:24:05.365Z'),
    workspace_id='deleniti',
    workspace_ids=[
        'aperiam',
    ],
)

res = s.user.patch_unified_user(req, operations.PatchUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.User](../../models/shared/user.md)                                                 | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchUnifiedUserSecurity](../../models/operations/patchunifiedusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchUnifiedUserResponse](../../models/operations/patchunifieduserresponse.md)**


## post_crm_connection_id_user

Create a user

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostCrmConnectionIDUserRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='quos',
            address2='maxime',
            city='South Nestor',
            country='Mongolia',
            country_code='TO',
            postal_code='94023',
            region='magnam',
            region_code='recusandae',
        ),
        created_at=dateutil.parser.isoparse('2022-12-13T13:34:20.729Z'),
        currency='maiores',
        department='tempora',
        division='reprehenderit',
        emails=[
            shared.CrmEmail(
                email='Stuart22@yahoo.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='483f748e-efcc-4b69-9541-b4b393f35666',
        image_url='consequuntur',
        language_locale='quis',
        name='Tomas Pacocha',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='consequuntur',
                type=shared.CrmTelephoneType.WORK,
            ),
        ],
        timezone='illo',
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2020-08-23T15:43:14.003Z'),
    ),
    connection_id='sequi',
)

res = s.user.post_crm_connection_id_user(req, operations.PostCrmConnectionIDUserSecurity(
    jwt="",
))

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostCrmConnectionIDUserRequest](../../models/operations/postcrmconnectioniduserrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.PostCrmConnectionIDUserSecurity](../../models/operations/postcrmconnectionidusersecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.PostCrmConnectionIDUserResponse](../../models/operations/postcrmconnectioniduserresponse.md)**


## put_crm_connection_id_user_id

Update a user

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='reprehenderit',
            address2='sint',
            city='Hintzfurt',
            country='Martinique',
            country_code='TR',
            postal_code='08257-3819',
            region='omnis',
            region_code='itaque',
        ),
        created_at=dateutil.parser.isoparse('2022-11-29T02:49:06.048Z'),
        currency='fugiat',
        department='provident',
        division='voluptatem',
        emails=[
            shared.CrmEmail(
                email='Rosanna45@hotmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='6bfc7677-f0f5-404a-ae48-28fb6daee19c',
        image_url='explicabo',
        language_locale='nisi',
        name='Frank Ryan',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='quasi',
                type=shared.CrmTelephoneType.OTHER,
            ),
        ],
        timezone='maxime',
        title='Ms.',
        updated_at=dateutil.parser.isoparse('2022-10-11T03:37:06.147Z'),
    ),
    connection_id='vitae',
    id='cabdab76-7a44-44dd-8da0-abe58eb3d54b',
)

res = s.user.put_crm_connection_id_user_id(req, operations.PutCrmConnectionIDUserIDSecurity(
    jwt="",
))

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCrmConnectionIDUserIDRequest](../../models/operations/putcrmconnectioniduseridrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.PutCrmConnectionIDUserIDSecurity](../../models/operations/putcrmconnectioniduseridsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.PutCrmConnectionIDUserIDResponse](../../models/operations/putcrmconnectioniduseridresponse.md)**


## put_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = shared.User(
    created_at=dateutil.parser.isoparse('2022-11-07T21:46:44.444Z'),
    email='Melissa_Dooley30@hotmail.com',
    environment='sint',
    id='b8e5c18b-25e8-47f6-8823-255be95c0cbc',
    meta=shared.PropertyUserMeta(),
    name='Billy Schmeler',
    updated_at=dateutil.parser.isoparse('2022-06-05T12:45:52.497Z'),
    workspace_id='quae',
    workspace_ids=[
        'quos',
    ],
)

res = s.user.put_unified_user(req, operations.PutUnifiedUserSecurity(
    jwt="",
))

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.User](../../models/shared/user.md)                                             | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PutUnifiedUserSecurity](../../models/operations/putunifiedusersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PutUnifiedUserResponse](../../models/operations/putunifieduserresponse.md)**

