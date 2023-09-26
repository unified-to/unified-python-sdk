# Hris
(*hris*)

### Available Operations

* [delete_hris_connection_id_employee_id](#delete_hris_connection_id_employee_id) - Remove a Employee
* [delete_hris_connection_id_group_id](#delete_hris_connection_id_group_id) - Remove a Group
* [get_hris_connection_id_employee](#get_hris_connection_id_employee) - List all Employees
* [get_hris_connection_id_employee_id](#get_hris_connection_id_employee_id) - Retrieve a Employee
* [get_hris_connection_id_group](#get_hris_connection_id_group) - List all Groups
* [get_hris_connection_id_group_id](#get_hris_connection_id_group_id) - Retrieve a Group
* [patch_hris_connection_id_employee_id](#patch_hris_connection_id_employee_id) - Update a Employee
* [patch_hris_connection_id_group_id](#patch_hris_connection_id_group_id) - Update a Group
* [post_hris_connection_id_employee](#post_hris_connection_id_employee) - Create a Employee
* [post_hris_connection_id_group](#post_hris_connection_id_group) - Create a Group
* [put_hris_connection_id_employee_id](#put_hris_connection_id_employee_id) - Update a Employee
* [put_hris_connection_id_group_id](#put_hris_connection_id_group_id) - Update a Group

## delete_hris_connection_id_employee_id

Remove a Employee

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
    connection_id='excepturi',
    id='3e34316c-f55b-4431-b553-ccf1c204c4ad',
)

res = s.hris.delete_hris_connection_id_employee_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.DeleteHrisConnectionIDEmployeeIDRequest](../../models/operations/deletehrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.DeleteHrisConnectionIDEmployeeIDResponse](../../models/operations/deletehrisconnectionidemployeeidresponse.md)**


## delete_hris_connection_id_group_id

Remove a Group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteHrisConnectionIDGroupIDRequest(
    connection_id='quod',
    id='c9904c51-95b8-4648-8efa-78f1e2d3b901',
)

res = s.hris.delete_hris_connection_id_group_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteHrisConnectionIDGroupIDRequest](../../models/operations/deletehrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteHrisConnectionIDGroupIDResponse](../../models/operations/deletehrisconnectionidgroupidresponse.md)**


## get_hris_connection_id_employee

List all Employees

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
    connection_id='saepe',
    limit=289.94,
    offset=5725.89,
    order='corporis',
    query='explicabo',
    sort='distinctio',
    updated_gte=dateutil.parser.isoparse('2021-08-12T22:16:16.253Z'),
)

res = s.hris.get_hris_connection_id_employee(req)

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

Retrieve a Employee

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
    connection_id='tempora',
    id='cbb19f71-3d95-4a41-a9c1-387271e18ea9',
)

res = s.hris.get_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetHrisConnectionIDEmployeeIDRequest](../../models/operations/gethrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetHrisConnectionIDEmployeeIDResponse](../../models/operations/gethrisconnectionidemployeeidresponse.md)**


## get_hris_connection_id_group

List all Groups

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

req = operations.GetHrisConnectionIDGroupRequest(
    connection_id='debitis',
    limit=2501.58,
    offset=3333.54,
    order='illo',
    query='illo',
    sort='deleniti',
    updated_gte=dateutil.parser.isoparse('2022-07-26T10:34:40.123Z'),
)

res = s.hris.get_hris_connection_id_group(req)

if res.hris_groups is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetHrisConnectionIDGroupRequest](../../models/operations/gethrisconnectionidgrouprequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetHrisConnectionIDGroupResponse](../../models/operations/gethrisconnectionidgroupresponse.md)**


## get_hris_connection_id_group_id

Retrieve a Group

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetHrisConnectionIDGroupIDRequest(
    connection_id='optio',
    id='c57fbd60-b1a7-48ed-a9a9-d4eea85658c2',
)

res = s.hris.get_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetHrisConnectionIDGroupIDRequest](../../models/operations/gethrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetHrisConnectionIDGroupIDResponse](../../models/operations/gethrisconnectionidgroupidresponse.md)**


## patch_hris_connection_id_employee_id

Update a Employee

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
        address=shared.PropertyHrisEmployeeAddress(
            address1='at',
            address2='modi',
            city='Findlay',
            country='Saint Martin',
            country_code='LI',
            postal_code='69291-4598',
            region='unde',
            region_code='autem',
        ),
        created_at=dateutil.parser.isoparse('2022-07-11T08:13:45.102Z'),
        date_of_birth=dateutil.parser.isoparse('2022-02-18T07:36:00.073Z'),
        department='autem',
        division='placeat',
        emails=[
            shared.HrisEmail(
                email='Blaze97@yahoo.com',
                type=shared.HrisEmailType.OTHER,
            ),
        ],
        employee_number='id',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.INTERN,
        gender=shared.HrisEmployeeGender.INTERSEX,
        hired_at=dateutil.parser.isoparse('2020-08-13T08:33:47.369Z'),
        id='ef234c95-5b9b-4df2-990a-bd9bbcc2725e',
        location='impedit',
        manager_id='magni',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='Sabrina Schamberger Sr.',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='totam',
                type=shared.HrisTelephoneType.WORK,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2022-06-27T13:37:26.116Z'),
        title='Mr.',
        updated_at=dateutil.parser.isoparse('2021-10-27T12:07:56.119Z'),
    ),
    connection_id='excepturi',
    id='ef68e45c-8add-4fac-b545-00430c6632b4',
)

res = s.hris.patch_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchHrisConnectionIDEmployeeIDRequest](../../models/operations/patchhrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchHrisConnectionIDEmployeeIDResponse](../../models/operations/patchhrisconnectionidemployeeidresponse.md)**


## patch_hris_connection_id_group_id

Update a Group

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

req = operations.PatchHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.isoparse('2022-05-31T02:06:03.542Z'),
        description='inventore',
        employee_ids=[
            'sapiente',
        ],
        id='df01c3e9-1e8f-47bc-a9d4-60a77eceb26d',
        is_active=False,
        manager_ids=[
            'architecto',
        ],
        name='Lorene Bosco',
        parent_id='qui',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DEPARTMENT,
        updated_at=dateutil.parser.isoparse('2022-12-06T03:55:58.108Z'),
    ),
    connection_id='quisquam',
    id='7c0f0f87-3f9d-45c2-9fd3-e0b4a4a4253c',
)

res = s.hris.patch_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchHrisConnectionIDGroupIDRequest](../../models/operations/patchhrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchHrisConnectionIDGroupIDResponse](../../models/operations/patchhrisconnectionidgroupidresponse.md)**


## post_hris_connection_id_employee

Create a Employee

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
        address=shared.PropertyHrisEmployeeAddress(
            address1='amet',
            address2='ipsa',
            city='West Jaunitaland',
            country='Bahrain',
            country_code='YE',
            postal_code='18494',
            region='pariatur',
            region_code='porro',
        ),
        created_at=dateutil.parser.isoparse('2022-09-23T16:00:07.090Z'),
        date_of_birth=dateutil.parser.isoparse('2021-07-11T10:12:07.009Z'),
        department='itaque',
        division='sit',
        emails=[
            shared.HrisEmail(
                email='Timmothy68@yahoo.com',
                type=shared.HrisEmailType.HOME,
            ),
        ],
        employee_number='culpa',
        employment_status=shared.HrisEmployeeEmploymentStatus.ACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.FULL_TIME,
        gender=shared.HrisEmployeeGender.FEMALE,
        hired_at=dateutil.parser.isoparse('2021-01-27T23:42:02.589Z'),
        id='12a4ba9d-5998-4819-acfd-0c77c53e7e7d',
        location='eius',
        manager_id='accusamus',
        marital_status=shared.HrisEmployeeMaritalStatus.SINGLE,
        name='Sophie Lesch',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='consequatur',
                type=shared.HrisTelephoneType.FAX,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2021-06-09T00:38:41.199Z'),
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-06-19T22:55:28.813Z'),
    ),
    connection_id='saepe',
)

res = s.hris.post_hris_connection_id_employee(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostHrisConnectionIDEmployeeRequest](../../models/operations/posthrisconnectionidemployeerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostHrisConnectionIDEmployeeResponse](../../models/operations/posthrisconnectionidemployeeresponse.md)**


## post_hris_connection_id_group

Create a Group

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

req = operations.PostHrisConnectionIDGroupRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.isoparse('2022-10-11T00:06:05.180Z'),
        description='sint',
        employee_ids=[
            'ea',
        ],
        id='703fec31-c508-424d-989a-36a6b2d27eb7',
        is_active=False,
        manager_ids=[
            'accusantium',
        ],
        name='Harriet Orn DDS',
        parent_id='voluptatum',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.SUB_DEPARTMENT,
        updated_at=dateutil.parser.isoparse('2022-02-14T18:55:03.442Z'),
    ),
    connection_id='commodi',
)

res = s.hris.post_hris_connection_id_group(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostHrisConnectionIDGroupRequest](../../models/operations/posthrisconnectionidgrouprequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PostHrisConnectionIDGroupResponse](../../models/operations/posthrisconnectionidgroupresponse.md)**


## put_hris_connection_id_employee_id

Update a Employee

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
        address=shared.PropertyHrisEmployeeAddress(
            address1='debitis',
            address2='commodi',
            city='South Izaiahhaven',
            country='Paraguay',
            country_code='MS',
            postal_code='72740-9977',
            region='nisi',
            region_code='occaecati',
        ),
        created_at=dateutil.parser.isoparse('2022-12-15T12:15:10.431Z'),
        date_of_birth=dateutil.parser.isoparse('2020-03-31T16:49:34.939Z'),
        department='odio',
        division='nihil',
        emails=[
            shared.HrisEmail(
                email='Tamia.Doyle@gmail.com',
                type=shared.HrisEmailType.HOME,
            ),
        ],
        employee_number='iusto',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.OTHER,
        gender=shared.HrisEmployeeGender.INTERSEX,
        hired_at=dateutil.parser.isoparse('2022-06-18T09:54:51.929Z'),
        id='06e61b0d-3087-414c-a0a3-d98637ca85c3',
        location='delectus',
        manager_id='repudiandae',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='Erin Kris',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='harum',
                type=shared.HrisTelephoneType.FAX,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2021-02-20T15:13:08.610Z'),
        title='Mrs.',
        updated_at=dateutil.parser.isoparse('2022-01-28T12:53:07.770Z'),
    ),
    connection_id='placeat',
    id='98f13af2-8db2-4cf2-bf4f-3ded356d7e14',
)

res = s.hris.put_hris_connection_id_employee_id(req)

if res.hris_employee is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PutHrisConnectionIDEmployeeIDRequest](../../models/operations/puthrisconnectionidemployeeidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PutHrisConnectionIDEmployeeIDResponse](../../models/operations/puthrisconnectionidemployeeidresponse.md)**


## put_hris_connection_id_group_id

Update a Group

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

req = operations.PutHrisConnectionIDGroupIDRequest(
    hris_group=shared.HrisGroup(
        created_at=dateutil.parser.isoparse('2022-08-29T10:06:09.751Z'),
        description='beatae',
        employee_ids=[
            'eligendi',
        ],
        id='d98196d5-5af6-49a1-84b7-9ae33681c23c',
        is_active=False,
        manager_ids=[
            'dolorem',
        ],
        name='Grant Klein PhD',
        parent_id='ab',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DIVISION,
        updated_at=dateutil.parser.isoparse('2020-11-07T15:44:18.546Z'),
    ),
    connection_id='quasi',
    id='2c5ba825-fe22-4cd5-8ba6-fbfec932af68',
)

res = s.hris.put_hris_connection_id_group_id(req)

if res.hris_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutHrisConnectionIDGroupIDRequest](../../models/operations/puthrisconnectionidgroupidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutHrisConnectionIDGroupIDResponse](../../models/operations/puthrisconnectionidgroupidresponse.md)**

