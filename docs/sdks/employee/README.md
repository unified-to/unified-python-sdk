# Employee
(*employee*)

### Available Operations

* [delete_hris_connection_id_employee_id](#delete_hris_connection_id_employee_id) - Remove an employee
* [get_hris_connection_id_employee](#get_hris_connection_id_employee) - List all employees
* [get_hris_connection_id_employee_id](#get_hris_connection_id_employee_id) - Retrieve an employee
* [patch_hris_connection_id_employee_id](#patch_hris_connection_id_employee_id) - Update an employee
* [post_hris_connection_id_employee](#post_hris_connection_id_employee) - Create an employee
* [put_hris_connection_id_employee_id](#put_hris_connection_id_employee_id) - Update an employee

## delete_hris_connection_id_employee_id

Remove an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteHrisConnectionIDEmployeeIDRequest(
    connection_id='Laredo turquoise port',
    id='<ID>',
)

res = s.employee.delete_hris_connection_id_employee_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteHrisConnectionIDEmployeeIDRequest](../../models/operations/deletehrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteHrisConnectionIDEmployeeIDResponse](../../models/operations/deletehrisconnectionidemployeeidresponse.md)**


## get_hris_connection_id_employee

List all employees

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

req = operations.GetHrisConnectionIDEmployeeRequest(
    connection_id='initiatives greedily project',
)

res = s.employee.get_hris_connection_id_employee(req)

if res.hris_employees is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetHrisConnectionIDEmployeeRequest](../../models/operations/gethrisconnectionidemployeerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetHrisConnectionIDEmployeeResponse](../../models/operations/gethrisconnectionidemployeeresponse.md)**


## get_hris_connection_id_employee_id

Retrieve an employee

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetHrisConnectionIDEmployeeIDRequest(
    connection_id='Keyboard cleverly Rubber',
    id='<ID>',
)

res = s.employee.get_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetHrisConnectionIDEmployeeIDRequest](../../models/operations/gethrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetHrisConnectionIDEmployeeIDResponse](../../models/operations/gethrisconnectionidemployeeidresponse.md)**


## patch_hris_connection_id_employee_id

Update an employee

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

req = operations.PatchHrisConnectionIDEmployeeIDRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Brennan.Senger@yahoo.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='Assurance forecast',
            ),
        ],
    ),
    connection_id='Bahamas if fictionalise',
    id='<ID>',
)

res = s.employee.patch_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchHrisConnectionIDEmployeeIDRequest](../../models/operations/patchhrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchHrisConnectionIDEmployeeIDResponse](../../models/operations/patchhrisconnectionidemployeeidresponse.md)**


## post_hris_connection_id_employee

Create an employee

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

req = operations.PostHrisConnectionIDEmployeeRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Berry.Reinger@hotmail.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='Chicken Southwest',
            ),
        ],
    ),
    connection_id='generate Forward Diesel',
)

res = s.employee.post_hris_connection_id_employee(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostHrisConnectionIDEmployeeRequest](../../models/operations/posthrisconnectionidemployeerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostHrisConnectionIDEmployeeResponse](../../models/operations/posthrisconnectionidemployeeresponse.md)**


## put_hris_connection_id_employee_id

Update an employee

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

req = operations.PutHrisConnectionIDEmployeeIDRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(),
        emails=[
            shared.HrisEmail(
                email='Bert90@gmail.com',
            ),
        ],
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='mobile',
            ),
        ],
    ),
    connection_id='a online olive',
    id='<ID>',
)

res = s.employee.put_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutHrisConnectionIDEmployeeIDRequest](../../models/operations/puthrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutHrisConnectionIDEmployeeIDResponse](../../models/operations/puthrisconnectionidemployeeidresponse.md)**

