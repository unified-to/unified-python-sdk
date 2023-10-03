# Hris
(*hris*)

### Available Operations

* [delete_hris_connection_id_employee_id](#delete_hris_connection_id_employee_id) - Remove an employee
* [delete_hris_connection_id_group_id](#delete_hris_connection_id_group_id) - Remove a group
* [get_hris_connection_id_employee](#get_hris_connection_id_employee) - List all employees
* [get_hris_connection_id_employee_id](#get_hris_connection_id_employee_id) - Retrieve an employee
* [get_hris_connection_id_group](#get_hris_connection_id_group) - List all groups
* [get_hris_connection_id_group_id](#get_hris_connection_id_group_id) - Retrieve a group
* [patch_hris_connection_id_employee_id](#patch_hris_connection_id_employee_id) - Update an employee
* [patch_hris_connection_id_group_id](#patch_hris_connection_id_group_id) - Update a group
* [post_hris_connection_id_employee](#post_hris_connection_id_employee) - Create an employee
* [post_hris_connection_id_group](#post_hris_connection_id_group) - Create a group
* [put_hris_connection_id_employee_id](#put_hris_connection_id_employee_id) - Update an employee
* [put_hris_connection_id_group_id](#put_hris_connection_id_group_id) - Update a group

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

Remove a group

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
    connection_id='consequently platforms Metal',
    id='<ID>',
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
    limit=1798.52,
    offset=6683.19,
    order='Sports',
    query='TLS',
    sort='Jazz Trans',
    updated_gte=dateutil.parser.isoparse('2021-04-09T17:32:06.988Z'),
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

List all groups

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
    connection_id='Loan',
    limit=3486.96,
    offset=9705.73,
    order='Coordinator',
    query='World',
    sort='Dollar',
    updated_gte=dateutil.parser.isoparse('2021-01-15T16:06:13.340Z'),
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

Retrieve a group

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
    connection_id='behind',
    id='<ID>',
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
        address=shared.PropertyHrisEmployeeAddress(
            address1='Tennessee virtual',
            address2='Assurance forecast',
            city='Baton Rouge',
            country='Bahamas',
            country_code='TW',
            postal_code='93632',
            region='Bailey',
            region_code='navigating Oregon',
        ),
        created_at=dateutil.parser.isoparse('2023-01-31T08:11:49.561Z'),
        date_of_birth=dateutil.parser.isoparse('2021-10-08T23:14:10.860Z'),
        department='soupy web Robust',
        division='Corporate loudly quantify',
        emails=[
            shared.HrisEmail(
                email='Wendy_Kovacek@hotmail.com',
                type=shared.HrisEmailType.OTHER,
            ),
        ],
        employee_number='hydrate indigo transmit',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.FULL_TIME,
        gender=shared.HrisEmployeeGender.INTERSEX,
        hired_at=dateutil.parser.isoparse('2021-07-20T11:37:42.486Z'),
        id='<ID>',
        location='withdrawal wonderfully',
        manager_id='molestias white Gainesville',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='tensely technologies',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='Northeast Music Hassium',
                type=shared.HrisTelephoneType.MOBILE,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2023-08-07T01:58:28.622Z'),
        title='failing Southwest Kuhn',
        updated_at=dateutil.parser.isoparse('2023-05-18T01:32:56.083Z'),
    ),
    connection_id='South Money past',
    id='<ID>',
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

Update a group

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
        created_at=dateutil.parser.isoparse('2023-10-19T05:30:26.390Z'),
        description='Stand-alone asymmetric orchestration',
        employee_ids=[
            'shootdown',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            '24/7',
        ],
        name='Agender trainer',
        parent_id='Configuration Kids Sedan',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.DIVISION,
        updated_at=dateutil.parser.isoparse('2021-08-18T16:48:12.885Z'),
    ),
    connection_id='Intersex',
    id='<ID>',
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
        address=shared.PropertyHrisEmployeeAddress(
            address1='Southeast ea withdrawal',
            address2='Developer',
            city='Grand Forks',
            country='Cayman Islands',
            country_code='BM',
            postal_code='63867-8134',
            region='teal Northwest firewall',
            region_code='doubt Diesel COM',
        ),
        created_at=dateutil.parser.isoparse('2022-09-25T20:39:21.870Z'),
        date_of_birth=dateutil.parser.isoparse('2022-04-06T20:53:56.362Z'),
        department='payment mull',
        division='Blues red',
        emails=[
            shared.HrisEmail(
                email='Jacquelyn8@hotmail.com',
                type=shared.HrisEmailType.WORK,
            ),
        ],
        employee_number='North Southeast',
        employment_status=shared.HrisEmployeeEmploymentStatus.INACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.VOLUNTEER,
        gender=shared.HrisEmployeeGender.INTERSEX,
        hired_at=dateutil.parser.isoparse('2021-03-26T14:20:42.258Z'),
        id='<ID>',
        location='East',
        manager_id='Maserati',
        marital_status=shared.HrisEmployeeMaritalStatus.SINGLE,
        name='Xenogender copy',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='hmph',
                type=shared.HrisTelephoneType.WORK,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2022-08-16T03:13:22.861Z'),
        title='Regional synthesize',
        updated_at=dateutil.parser.isoparse('2022-06-15T02:35:02.446Z'),
    ),
    connection_id='past',
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

Create a group

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
        created_at=dateutil.parser.isoparse('2021-02-23T15:35:38.483Z'),
        description='Configurable stable product',
        employee_ids=[
            'Auto',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            'JSON',
        ],
        name='whereas Usability transmitting',
        parent_id='invoice Cyclocross Electric',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.GROUP,
        updated_at=dateutil.parser.isoparse('2021-04-30T12:40:50.129Z'),
    ),
    connection_id='Hybrid Schenectady',
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
        address=shared.PropertyHrisEmployeeAddress(
            address1='Northwest',
            address2='and',
            city='Uniquefield',
            country='Virgin Islands, British',
            country_code='AE',
            postal_code='41682',
            region='Adventure Avon',
            region_code='bah South',
        ),
        created_at=dateutil.parser.isoparse('2023-07-18T13:59:47.040Z'),
        date_of_birth=dateutil.parser.isoparse('2022-04-19T17:38:57.783Z'),
        department='West auxiliary',
        division='volt',
        emails=[
            shared.HrisEmail(
                email='Kenton_Turcotte@gmail.com',
                type=shared.HrisEmailType.HOME,
            ),
        ],
        employee_number='DNS coulomb Berkshire',
        employment_status=shared.HrisEmployeeEmploymentStatus.ACTIVE,
        employment_type=shared.HrisEmployeeEmploymentType.CASUAL,
        gender=shared.HrisEmployeeGender.FEMALE,
        hired_at=dateutil.parser.isoparse('2022-10-08T23:22:26.211Z'),
        id='<ID>',
        location='East primary',
        manager_id='Tokelau',
        marital_status=shared.HrisEmployeeMaritalStatus.MARRIED,
        name='Bespoke Investment',
        raw=shared.PropertyHrisEmployeeRaw(),
        telephones=[
            shared.HrisTelephone(
                telephone='East Investment',
                type=shared.HrisTelephoneType.OTHER,
            ),
        ],
        terminated_at=dateutil.parser.isoparse('2022-03-28T08:29:30.386Z'),
        title='unless',
        updated_at=dateutil.parser.isoparse('2022-06-29T10:38:14.570Z'),
    ),
    connection_id='Designer Tennessine',
    id='<ID>',
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

Update a group

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
        created_at=dateutil.parser.isoparse('2022-08-10T12:11:42.375Z'),
        description='Decentralized methodical projection',
        employee_ids=[
            'Credit',
        ],
        id='<ID>',
        is_active=False,
        manager_ids=[
            'South',
        ],
        name='Jeep brr Northwest',
        parent_id='quickly Licensed',
        raw=shared.PropertyHrisGroupRaw(),
        type=shared.HrisGroupType.BUSINESS_UNIT,
        updated_at=dateutil.parser.isoparse('2021-11-08T00:11:45.458Z'),
    ),
    connection_id='vortals interface Gasoline',
    id='<ID>',
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

