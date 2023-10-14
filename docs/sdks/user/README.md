# User
(*user*)

### Available Operations

* [create_crm_user](#create_crm_user) - Create a user
* [get_crm_user](#get_crm_user) - Retrieve a user
* [list_crm_users](#list_crm_users) - List all users
* [patch_crm_user](#patch_crm_user) - Update a user
* [remove_crm_user](#remove_crm_user) - Remove a user
* [update_crm_user](#update_crm_user) - Update a user

## create_crm_user

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

req = operations.CreateCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='await male',
            ),
        ],
    ),
    connection_id='Incredible Virginia',
    fields_=[
        'Keyboard',
    ],
)

res = s.user.create_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateCrmUserRequest](../../models/operations/createcrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateCrmUserResponse](../../models/operations/createcrmuserresponse.md)**


## get_crm_user

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

req = operations.GetCrmUserRequest(
    connection_id='Bespoke Dollar',
    fields_=[
        'unto',
    ],
    id='<ID>',
)

res = s.user.get_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCrmUserRequest](../../models/operations/getcrmuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetCrmUserResponse](../../models/operations/getcrmuserresponse.md)**


## list_crm_users

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

req = operations.ListCrmUsersRequest(
    connection_id='careless Costa',
    fields_=[
        'olive',
    ],
)

res = s.user.list_crm_users(req)

if res.crm_users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListCrmUsersRequest](../../models/operations/listcrmusersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListCrmUsersResponse](../../models/operations/listcrmusersresponse.md)**


## patch_crm_user

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

req = operations.PatchCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Bronze composite',
            ),
        ],
    ),
    connection_id='katal Industrial Classical',
    fields_=[
        'boo',
    ],
    id='<ID>',
)

res = s.user.patch_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchCrmUserRequest](../../models/operations/patchcrmuserrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PatchCrmUserResponse](../../models/operations/patchcrmuserresponse.md)**


## remove_crm_user

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

req = operations.RemoveCrmUserRequest(
    connection_id='Southeast',
    id='<ID>',
)

res = s.user.remove_crm_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveCrmUserRequest](../../models/operations/removecrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RemoveCrmUserResponse](../../models/operations/removecrmuserresponse.md)**


## update_crm_user

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

req = operations.UpdateCrmUserRequest(
    crm_user=shared.CrmUser(
        address=shared.PropertyCrmUserAddress(),
        emails=[
            shared.CrmEmail(),
        ],
        raw=shared.PropertyCrmUserRaw(),
        telephones=[
            shared.CrmTelephone(
                telephone='Idaho green',
            ),
        ],
    ),
    connection_id='Savings',
    fields_=[
        'Corwin',
    ],
    id='<ID>',
)

res = s.user.update_crm_user(req)

if res.crm_user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCrmUserRequest](../../models/operations/updatecrmuserrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateCrmUserResponse](../../models/operations/updatecrmuserresponse.md)**

