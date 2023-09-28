# User
(*user*)

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDUserIDRequest(
    connection_id='Intranet Data',
    id='<ID>',
)

res = s.user.delete_crm_connection_id_user_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDUserIDRequest](../../models/operations/deletecrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDUserIDResponse](../../models/operations/deletecrmconnectioniduseridresponse.md)**


## delete_unified_user

Delete your user object

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.user.delete_unified_user()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.DeleteUnifiedUserResponse](../../models/operations/deleteunifieduserresponse.md)**


## get_crm_connection_id_user

List all users

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

req = operations.GetCrmConnectionIDUserRequest(
    connection_id='suit Electronic Tampa',
    limit=2883.34,
    offset=8886.55,
    order='despite',
    query='frightfully Fitness',
    sort='success servant',
    updated_gte=dateutil.parser.isoparse('2023-02-23T05:53:04.259Z'),
)

res = s.user.get_crm_connection_id_user(req)

if res.crm_users is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDUserRequest](../../models/operations/getcrmconnectioniduserrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDUserResponse](../../models/operations/getcrmconnectioniduserresponse.md)**


## get_crm_connection_id_user_id

Retrieve a user

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDUserIDRequest(
    connection_id='connecting Program',
    id='<ID>',
)

res = s.user.get_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDUserIDRequest](../../models/operations/getcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDUserIDResponse](../../models/operations/getcrmconnectioniduseridresponse.md)**


## get_unified_user

Retrieve your user object

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.user.get_unified_user()

if res.user is not None:
    # handle response
```


### Response

**[operations.GetUnifiedUserResponse](../../models/operations/getunifieduserresponse.md)**


## get_unified_user_token

Retrieve your user token

### Example Usage

```python
import unified_to
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)


res = s.user.get_unified_user_token()

if res.get_unified_user_token_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.GetUnifiedUserTokenResponse](../../models/operations/getunifiedusertokenresponse.md)**


## patch_crm_connection_id_user_id

Update a user

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

req = operations.PatchCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='Customer',
            address2='violet groupware blanditiis',
            city='South Phoebeshire',
            country='Thailand',
            country_code='NO',
            postal_code='30801-4594',
            region='portals Vanadium',
            region_code='Future',
        ),
        created_at=dateutil.parser.isoparse('2023-01-04T02:42:28.788Z'),
        currency='Guinea Franc',
        department='Gloves global rosin',
        division='Berkshire Europium',
        emails=[
            shared.CrmEmail(
                email='Wade.Dach@gmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        image_url='Checking',
        language_locale='Sedan Porsche matrix',
        name='superstructure Nissan sedately',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='unto ubiquitous input',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        timezone='America/Tijuana',
        title='Computer Bicycle',
        updated_at=dateutil.parser.isoparse('2021-12-13T16:36:33.886Z'),
    ),
    connection_id='gold generating',
    id='<ID>',
)

res = s.user.patch_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDUserIDRequest](../../models/operations/patchcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDUserIDResponse](../../models/operations/patchcrmconnectioniduseridresponse.md)**


## patch_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = shared.User(
    created_at=dateutil.parser.isoparse('2022-04-24T15:25:24.483Z'),
    email='Emmalee.Quitzon@yahoo.com',
    environment='Bicycle',
    id='<ID>',
    meta=shared.PropertyUserMeta(),
    name='vice compressing',
    updated_at=dateutil.parser.isoparse('2023-05-05T16:52:20.023Z'),
    workspace_id='Hybrid methodologies',
    workspace_ids=[
        'Potassium',
    ],
)

res = s.user.patch_unified_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PatchUnifiedUserResponse](../../models/operations/patchunifieduserresponse.md)**


## post_crm_connection_id_user

Create a user

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

req = operations.PostCrmConnectionIDUserRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='driver East',
            address2='relationships Computer navigate',
            city='Homestead',
            country='Cayman Islands',
            country_code='BW',
            postal_code='34958',
            region='South',
            region_code='morph an colossal',
        ),
        created_at=dateutil.parser.isoparse('2021-02-02T08:27:21.693Z'),
        currency='Cayman Islands Dollar',
        department='um',
        division='West sievert generating',
        emails=[
            shared.CrmEmail(
                email='Jadon_Schumm45@gmail.com',
                type=shared.CrmEmailType.HOME,
            ),
        ],
        id='<ID>',
        image_url='radian Borders Southeast',
        language_locale='Silicon Awesome Industrial',
        name='Mouse Accounts',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='ohm Southeast ROI',
                type=shared.CrmTelephoneType.MOBILE,
            ),
        ],
        timezone='Europe/Bratislava',
        title='Money',
        updated_at=dateutil.parser.isoparse('2023-12-09T10:24:50.054Z'),
    ),
    connection_id='competent calculate',
)

res = s.user.post_crm_connection_id_user(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDUserRequest](../../models/operations/postcrmconnectioniduserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDUserResponse](../../models/operations/postcrmconnectioniduserresponse.md)**


## put_crm_connection_id_user_id

Update a user

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

req = operations.PutCrmConnectionIDUserIDRequest(
    crm_user=shared.CrmUser(
        active=False,
        address=shared.PropertyCrmUserAddress(
            address1='Honduras',
            address2='Oxygen Libyan Burundi',
            city='North Gertrudefield',
            country='Belgium',
            country_code='DK',
            postal_code='00781',
            region='Wagon',
            region_code='how overriding',
        ),
        created_at=dateutil.parser.isoparse('2023-03-13T00:47:15.649Z'),
        currency='Pakistan Rupee',
        department='Tricycle vaguely',
        division='Severn bluetooth Argon',
        emails=[
            shared.CrmEmail(
                email='Karl_Stehr4@hotmail.com',
                type=shared.CrmEmailType.WORK,
            ),
        ],
        id='<ID>',
        image_url='AGP romance didactic',
        language_locale='ROI Polarised',
        name='olive synthesizing',
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Honda Indiana',
                type=shared.CrmTelephoneType.FAX,
            ),
        ],
        timezone='Asia/Novosibirsk',
        title='compelling red compressing',
        updated_at=dateutil.parser.isoparse('2022-09-03T15:59:05.095Z'),
    ),
    connection_id='relationships',
    id='<ID>',
)

res = s.user.put_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDUserIDRequest](../../models/operations/putcrmconnectioniduseridrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDUserIDResponse](../../models/operations/putcrmconnectioniduseridresponse.md)**


## put_unified_user

Only the name field is updated.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = shared.User(
    created_at=dateutil.parser.isoparse('2023-07-31T04:46:29.769Z'),
    email='Selena59@yahoo.com',
    environment='Bedfordshire Lucia',
    id='<ID>',
    meta=shared.PropertyUserMeta(),
    name='Bicycle hacking South',
    updated_at=dateutil.parser.isoparse('2023-03-15T15:08:26.238Z'),
    workspace_id='Card defect',
    workspace_ids=[
        'repudiandae',
    ],
)

res = s.user.put_unified_user(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PutUnifiedUserResponse](../../models/operations/putunifieduserresponse.md)**

