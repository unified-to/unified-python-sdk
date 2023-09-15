# Employee

### Available Operations

* [delete_hris_connection_id_employee_id](#delete_hris_connection_id_employee_id) - Remove a Employee
* [get_hris_connection_id_employee](#get_hris_connection_id_employee) - List all Employees
* [get_hris_connection_id_employee_id](#get_hris_connection_id_employee_id) - Retrieve a Employee
* [patch_hris_connection_id_employee_id](#patch_hris_connection_id_employee_id) - Update a Employee
* [post_hris_connection_id_employee](#post_hris_connection_id_employee) - Create a Employee
* [put_hris_connection_id_employee_id](#put_hris_connection_id_employee_id) - Update a Employee

## delete_hris_connection_id_employee_id

Remove a Employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteHrisConnectionIDEmployeeIDRequest(
    connection_id='delectus',
    id='4844225e-75b7-4960-a5c0-efa6f93b90a1',
)

res = s.employee.delete_hris_connection_id_employee_id(req, operations.DeleteHrisConnectionIDEmployeeIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteHrisConnectionIDEmployeeIDRequest](../../models/operations/deletehrisconnectionidemployeeidrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.DeleteHrisConnectionIDEmployeeIDSecurity](../../models/operations/deletehrisconnectionidemployeeidsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.DeleteHrisConnectionIDEmployeeIDResponse](../../models/operations/deletehrisconnectionidemployeeidresponse.md)**


## get_hris_connection_id_employee

List all Employees

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisConnectionIDEmployeeRequest(
    connection_id='distinctio',
    limit=5362.02,
    offset=7558.48,
    order='unde',
    query='veniam',
    sort='nam',
    updated_gte=dateutil.parser.isoparse('2022-08-28T08:17:40.334Z'),
)

res = s.employee.get_hris_connection_id_employee(req, operations.GetHrisConnectionIDEmployeeSecurity(
    jwt="",
))

if res.hris_employees is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetHrisConnectionIDEmployeeRequest](../../models/operations/gethrisconnectionidemployeerequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.GetHrisConnectionIDEmployeeSecurity](../../models/operations/gethrisconnectionidemployeesecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.GetHrisConnectionIDEmployeeResponse](../../models/operations/gethrisconnectionidemployeeresponse.md)**


## get_hris_connection_id_employee_id

Retrieve a Employee

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetHrisConnectionIDEmployeeIDRequest(
    connection_id='explicabo',
    id='54b739f4-fe77-4210-91f6-558c99c722d2',
)

res = s.employee.get_hris_connection_id_employee_id(req, operations.GetHrisConnectionIDEmployeeIDSecurity(
    jwt="",
))

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetHrisConnectionIDEmployeeIDRequest](../../models/operations/gethrisconnectionidemployeeidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetHrisConnectionIDEmployeeIDSecurity](../../models/operations/gethrisconnectionidemployeeidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetHrisConnectionIDEmployeeIDResponse](../../models/operations/gethrisconnectionidemployeeidresponse.md)**


## patch_hris_connection_id_employee_id

Update a Employee

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchHrisConnectionIDEmployeeIDRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(
            address1='nam',
            address2='optio',
            city='Fort Kentonburgh',
            country='Anguilla',
            country_code='LS',
            postal_code='85866',
            region='recusandae',
            region_code='doloremque',
        ),
        created_at=dateutil.parser.isoparse('2022-11-04T08:22:44.750Z'),
        date_of_birth=dateutil.parser.isoparse('2020-06-24T16:30:44.804Z'),
        department='voluptate',
        division='placeat',
        emails=[
            shared.HrisEmail(
                email='Manuela_Schowalter@hotmail.com',
                type=shared.HrisEmailType.WORK,
            ),
        ],
        employee_number='minus',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.CASUAL,
        gender=shared.HrisEmployeeGender.MALE,
        hired_at=dateutil.parser.isoparse('2020-02-21T17:23:34.909Z'),
        id='e9e15df9-0390-47f3-b831-983d42e54a85',
        location='dolore',
        manager_id='commodi',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='Ramona Kub',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='consequatur',
                type=shared.HrisTelephoneType.WORK,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2022-10-20T10:23:58.834Z'),
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2022-09-26T09:29:33.100Z'),
    ),
    connection_id='nihil',
    id='1d51aaa6-ddf5-4abd-a487-c5fc2b862a00',
)

res = s.employee.patch_hris_connection_id_employee_id(req, operations.PatchHrisConnectionIDEmployeeIDSecurity(
    jwt="",
))

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchHrisConnectionIDEmployeeIDRequest](../../models/operations/patchhrisconnectionidemployeeidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PatchHrisConnectionIDEmployeeIDSecurity](../../models/operations/patchhrisconnectionidemployeeidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PatchHrisConnectionIDEmployeeIDResponse](../../models/operations/patchhrisconnectionidemployeeidresponse.md)**


## post_hris_connection_id_employee

Create a Employee

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostHrisConnectionIDEmployeeRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(
            address1='nobis',
            address2='saepe',
            city='Irvine',
            country='Montserrat',
            country_code='TT',
            postal_code='00034',
            region='suscipit',
            region_code='dolor',
        ),
        created_at=dateutil.parser.isoparse('2022-04-09T11:38:39.555Z'),
        date_of_birth=dateutil.parser.isoparse('2020-12-14T05:42:01.818Z'),
        department='nihil',
        division='similique',
        emails=[
            shared.HrisEmail(
                email='Roman_Torp27@hotmail.com',
                type=shared.HrisEmailType.HOME,
            ),
        ],
        employee_number='dolor',
        employment_status=shared.HrisEmployeeEmploymentStatus.ACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.CASUAL,
        gender=shared.HrisEmployeeGender.FEMALE,
        hired_at=dateutil.parser.isoparse('2022-11-14T11:24:15.321Z'),
        id='38e1a735-ac26-4ae3-bbef-971a8f46bca1',
        location='quae',
        manager_id='aut',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='Frankie Mohr',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='soluta',
                type=shared.HrisTelephoneType.OTHER,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2022-11-23T11:50:41.638Z'),
        title='Dr.',
        updated_at=dateutil.parser.isoparse('2022-07-01T14:41:51.539Z'),
    ),
    connection_id='eligendi',
)

res = s.employee.post_hris_connection_id_employee(req, operations.PostHrisConnectionIDEmployeeSecurity(
    jwt="",
))

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostHrisConnectionIDEmployeeRequest](../../models/operations/posthrisconnectionidemployeerequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PostHrisConnectionIDEmployeeSecurity](../../models/operations/posthrisconnectionidemployeesecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PostHrisConnectionIDEmployeeResponse](../../models/operations/posthrisconnectionidemployeeresponse.md)**


## put_hris_connection_id_employee_id

Update a Employee

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutHrisConnectionIDEmployeeIDRequest(
    hris_employee=shared.HrisEmployee(
        address=shared.PropertyHrisEmployeeAddress(
            address1='tenetur',
            address2='deleniti',
            city='Stantonfort',
            country='Namibia',
            country_code='WF',
            postal_code='75563',
            region='quis',
            region_code='doloremque',
        ),
        created_at=dateutil.parser.isoparse('2022-02-19T05:47:56.169Z'),
        date_of_birth=dateutil.parser.isoparse('2022-08-03T10:40:15.780Z'),
        department='eveniet',
        division='possimus',
        emails=[
            shared.HrisEmail(
                email='Claire_Frami3@gmail.com',
                type=shared.HrisEmailType.OTHER,
            ),
        ],
        employee_number='officiis',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.CASUAL,
        gender=shared.HrisEmployeeGender.TRANS,
        hired_at=dateutil.parser.isoparse('2022-08-31T15:51:12.518Z'),
        id='432a986e-b7e1-44ca-9640-89150097019a',
        location='eius',
        manager_id='rem',
        marital_status=shared.HrisEmployeeMaritalStatus.SINGLE,
        name='Armando Wehner',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='reprehenderit',
                type=shared.HrisTelephoneType.FAX,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2021-04-08T14:13:47.569Z'),
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2022-02-05T17:52:52.343Z'),
    ),
    connection_id='consequatur',
    id='1105d389-0816-42c6-beb6-8a0f657b7d03',
)

res = s.employee.put_hris_connection_id_employee_id(req, operations.PutHrisConnectionIDEmployeeIDSecurity(
    jwt="",
))

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutHrisConnectionIDEmployeeIDRequest](../../models/operations/puthrisconnectionidemployeeidrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PutHrisConnectionIDEmployeeIDSecurity](../../models/operations/puthrisconnectionidemployeeidsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PutHrisConnectionIDEmployeeIDResponse](../../models/operations/puthrisconnectionidemployeeidresponse.md)**

