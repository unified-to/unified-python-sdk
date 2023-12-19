# Hris
(*hris*)

### Available Operations

* [create_hris_employee](#create_hris_employee) - Create an employee
* [create_hris_group](#create_hris_group) - Create a group
* [get_hris_employee](#get_hris_employee) - Retrieve an employee
* [get_hris_group](#get_hris_group) - Retrieve a group
* [list_hris_employees](#list_hris_employees) - List all employees
* [list_hris_groups](#list_hris_groups) - List all groups
* [patch_hris_employee](#patch_hris_employee) - Update an employee
* [patch_hris_group](#patch_hris_group) - Update a group
* [remove_hris_employee](#remove_hris_employee) - Remove an employee
* [remove_hris_group](#remove_hris_group) - Remove a group
* [update_hris_employee](#update_hris_employee) - Update an employee
* [update_hris_group](#update_hris_group) - Update a group

## create_hris_employee

Create an employee

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

req = operations.CreateHrisEmployeeRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Adriel_Hansen@hotmail.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
)

res = s.hris.create_hris_employee(req)

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisEmployeeRequest](../../models/operations/createhrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateHrisEmployeeResponse](../../models/operations/createhrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_hris_group

Create a group

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

req = operations.CreateHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'string',
        ],
        manager_ids=[
            'string',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='string',
)

res = s.hris.create_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateHrisGroupRequest](../../models/operations/createhrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateHrisGroupResponse](../../models/operations/createhrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_hris_employee

Retrieve an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetHrisEmployeeRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.hris.get_hris_employee(req)

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisEmployeeRequest](../../models/operations/gethrisemployeerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetHrisEmployeeResponse](../../models/operations/gethrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_hris_group

Retrieve a group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetHrisGroupRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.hris.get_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetHrisGroupRequest](../../models/operations/gethrisgrouprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetHrisGroupResponse](../../models/operations/gethrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_hris_employees

List all employees

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

req = operations.ListHrisEmployeesRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.hris.list_hris_employees(req)

if res.hris_employees is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisEmployeesRequest](../../models/operations/listhrisemployeesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ListHrisEmployeesResponse](../../models/operations/listhrisemployeesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_hris_groups

List all groups

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

req = operations.ListHrisGroupsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.hris.list_hris_groups(req)

if res.hris_groups is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListHrisGroupsRequest](../../models/operations/listhrisgroupsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ListHrisGroupsResponse](../../models/operations/listhrisgroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_hris_employee

Update an employee

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

req = operations.PatchHrisEmployeeRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Zetta.Cassin@yahoo.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.hris.patch_hris_employee(req)

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisEmployeeRequest](../../models/operations/patchhrisemployeerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PatchHrisEmployeeResponse](../../models/operations/patchhrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_hris_group

Update a group

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

req = operations.PatchHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'string',
        ],
        manager_ids=[
            'string',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.hris.patch_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchHrisGroupRequest](../../models/operations/patchhrisgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PatchHrisGroupResponse](../../models/operations/patchhrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_hris_employee

Remove an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveHrisEmployeeRequest(
    connection_id='string',
    id='<ID>',
)

res = s.hris.remove_hris_employee(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisEmployeeRequest](../../models/operations/removehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.RemoveHrisEmployeeResponse](../../models/operations/removehrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_hris_group

Remove a group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveHrisGroupRequest(
    connection_id='string',
    id='<ID>',
)

res = s.hris.remove_hris_group(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveHrisGroupRequest](../../models/operations/removehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RemoveHrisGroupResponse](../../models/operations/removehrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_hris_employee

Update an employee

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

req = operations.UpdateHrisEmployeeRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Abbie_Aufderhar@gmail.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='string',
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.hris.update_hris_employee(req)

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisEmployeeRequest](../../models/operations/updatehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateHrisEmployeeResponse](../../models/operations/updatehrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_hris_group

Update a group

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

req = operations.UpdateHrisGroupRequest(
    hris_group=shared.HrisGroup(
        employee_ids=[
            'string',
        ],
        manager_ids=[
            'string',
        ],
        raw=shared.PropertyHrisGroupRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.hris.update_hris_group(req)

if res.hris_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateHrisGroupRequest](../../models/operations/updatehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateHrisGroupResponse](../../models/operations/updatehrisgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
