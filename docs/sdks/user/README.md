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
    pass
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
    pass
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
)

res = s.user.get_crm_connection_id_user(req)

if res.crm_users is not None:
    # handle response
    pass
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
    pass
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
    pass
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
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Customer',
            ),
        ],
    ),
    connection_id='violet groupware blanditiis',
    id='<ID>',
)

res = s.user.patch_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
    pass
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
    meta=shared.PropertyUserMeta(),
    name='virtual female',
    workspace_id='Jewelery',
    workspace_ids=[
        'interfaces',
    ],
)

res = s.user.patch_unified_user(req)

if res.user is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='driver East',
            ),
        ],
    ),
    connection_id='relationships Computer navigate',
)

res = s.user.post_crm_connection_id_user(req)

if res.crm_user is not None:
    # handle response
    pass
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
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Honduras',
            ),
        ],
    ),
    connection_id='Oxygen Libyan Burundi',
    id='<ID>',
)

res = s.user.put_crm_connection_id_user_id(req)

if res.crm_user is not None:
    # handle response
    pass
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
    meta=shared.PropertyUserMeta(),
    name='invoice Convertible Country',
    workspace_id='Ergonomic',
    workspace_ids=[
        'becquerel',
    ],
)

res = s.user.put_unified_user(req)

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PutUnifiedUserResponse](../../models/operations/putunifieduserresponse.md)**

