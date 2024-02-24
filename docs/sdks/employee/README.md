# Employee
(*employee*)

### Available Operations

* [create_hris_employee](#create_hris_employee) - Create an employee
* [get_hris_employee](#get_hris_employee) - Retrieve an employee
* [list_hris_employees](#list_hris_employees) - List all employees
* [patch_hris_employee](#patch_hris_employee) - Update an employee
* [remove_hris_employee](#remove_hris_employee) - Remove an employee
* [update_hris_employee](#update_hris_employee) - Update an employee

## create_hris_employee

Create an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateHrisEmployeeRequest(
    connection_id='<value>',
)

res = s.employee.create_hris_employee(req, operations.CreateHrisEmployeeSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateHrisEmployeeRequest](../../models/operations/createhrisemployeerequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateHrisEmployeeSecurity](../../models/operations/createhrisemployeesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateHrisEmployeeResponse](../../models/operations/createhrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_hris_employee

Retrieve an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisEmployeeRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.employee.get_hris_employee(req, operations.GetHrisEmployeeSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisEmployeeRequest](../../models/operations/gethrisemployeerequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetHrisEmployeeSecurity](../../models/operations/gethrisemployeesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetHrisEmployeeResponse](../../models/operations/gethrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_hris_employees

List all employees

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListHrisEmployeesRequest(
    connection_id='<value>',
)

res = s.employee.list_hris_employees(req, operations.ListHrisEmployeesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_employees is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisEmployeesRequest](../../models/operations/listhrisemployeesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListHrisEmployeesSecurity](../../models/operations/listhrisemployeessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListHrisEmployeesResponse](../../models/operations/listhrisemployeesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_hris_employee

Update an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchHrisEmployeeRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.employee.patch_hris_employee(req, operations.PatchHrisEmployeeSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchHrisEmployeeRequest](../../models/operations/patchhrisemployeerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PatchHrisEmployeeSecurity](../../models/operations/patchhrisemployeesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PatchHrisEmployeeResponse](../../models/operations/patchhrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_hris_employee

Remove an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveHrisEmployeeRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.employee.remove_hris_employee(req, operations.RemoveHrisEmployeeSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveHrisEmployeeRequest](../../models/operations/removehrisemployeerequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.RemoveHrisEmployeeSecurity](../../models/operations/removehrisemployeesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.RemoveHrisEmployeeResponse](../../models/operations/removehrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_hris_employee

Update an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateHrisEmployeeRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.employee.update_hris_employee(req, operations.UpdateHrisEmployeeSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.hris_employee is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateHrisEmployeeRequest](../../models/operations/updatehrisemployeerequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateHrisEmployeeSecurity](../../models/operations/updatehrisemployeesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateHrisEmployeeResponse](../../models/operations/updatehrisemployeeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
