# application

### Available Operations

* [delete_ats_connection_id_application_id](#delete_ats_connection_id_application_id) - Remove an application
* [get_ats_connection_id_application](#get_ats_connection_id_application) - List all applications
* [get_ats_connection_id_application_id](#get_ats_connection_id_application_id) - Retrieve an application
* [patch_ats_connection_id_application_id](#patch_ats_connection_id_application_id) - Update an application
* [post_ats_connection_id_application](#post_ats_connection_id_application) - Create an application
* [put_ats_connection_id_application_id](#put_ats_connection_id_application_id) - Update an application

## delete_ats_connection_id_application_id

Remove an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteAtsConnectionIDApplicationIDRequest(
    connection_id='rerum',
    id='3fe49a8d-9cbf-4486-b332-3f9b77f3a410',
)

res = s.application.delete_ats_connection_id_application_id(req, operations.DeleteAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteAtsConnectionIDApplicationIDRequest](../../models/operations/deleteatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.DeleteAtsConnectionIDApplicationIDSecurity](../../models/operations/deleteatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.DeleteAtsConnectionIDApplicationIDResponse](../../models/operations/deleteatsconnectionidapplicationidresponse.md)**


## get_ats_connection_id_application

List all applications

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDApplicationRequest(
    candidate_id='ipsa',
    connection_id='iure',
    job_id='odio',
    limit=3117.96,
    offset=8810.05,
    order='quidem',
    query='voluptatibus',
    sort='voluptas',
    updated_gte=dateutil.parser.parse('2022-08-22').date(),
)

res = s.application.get_ats_connection_id_application(req, operations.GetAtsConnectionIDApplicationSecurity(
    jwt="",
))

if res.ats_applications is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAtsConnectionIDApplicationRequest](../../models/operations/getatsconnectionidapplicationrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.GetAtsConnectionIDApplicationSecurity](../../models/operations/getatsconnectionidapplicationsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.GetAtsConnectionIDApplicationResponse](../../models/operations/getatsconnectionidapplicationresponse.md)**


## get_ats_connection_id_application_id

Retrieve an application

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAtsConnectionIDApplicationIDRequest(
    connection_id='atque',
    id='0d1ba77a-89eb-4f73-bae4-203ce5e6a95d',
)

res = s.application.get_ats_connection_id_application_id(req, operations.GetAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAtsConnectionIDApplicationIDRequest](../../models/operations/getatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.GetAtsConnectionIDApplicationIDSecurity](../../models/operations/getatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.GetAtsConnectionIDApplicationIDResponse](../../models/operations/getatsconnectionidapplicationidresponse.md)**


## patch_ats_connection_id_application_id

Update an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.parse('2021-09-28').date(),
        candidate_id='alias',
        created_at=dateutil.parser.parse('2022-01-24').date(),
        id='46ce2af7-a73c-4f3b-a453-f870b326b5a7',
        job_id='ipsum',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.parse('2022-10-24').date(),
        rejected_reason='cupiditate',
        source='maxime',
        status=shared.AtsApplicationStatus.HIRED,
        updated_at=dateutil.parser.parse('2022-10-07').date(),
    ),
    connection_id='laborum',
    id='8422bb67-9d23-4227-95bf-0cbb1e31b8b9',
)

res = s.application.patch_ats_connection_id_application_id(req, operations.PatchAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchAtsConnectionIDApplicationIDRequest](../../models/operations/patchatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PatchAtsConnectionIDApplicationIDSecurity](../../models/operations/patchatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PatchAtsConnectionIDApplicationIDResponse](../../models/operations/patchatsconnectionidapplicationidresponse.md)**


## post_ats_connection_id_application

Create an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostAtsConnectionIDApplicationRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.parse('2022-01-14').date(),
        candidate_id='dolorem',
        created_at=dateutil.parser.parse('2022-09-18').date(),
        id='3a1108e0-adcf-44b9-a187-9fce953f73ef',
        job_id='dignissimos',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.parse('2020-11-08').date(),
        rejected_reason='quod',
        source='odio',
        status=shared.AtsApplicationStatus.BACKGROUND_CHECK,
        updated_at=dateutil.parser.parse('2021-04-02').date(),
    ),
    connection_id='ducimus',
)

res = s.application.post_ats_connection_id_application(req, operations.PostAtsConnectionIDApplicationSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PostAtsConnectionIDApplicationRequest](../../models/operations/postatsconnectionidapplicationrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.PostAtsConnectionIDApplicationSecurity](../../models/operations/postatsconnectionidapplicationsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostAtsConnectionIDApplicationResponse](../../models/operations/postatsconnectionidapplicationresponse.md)**


## put_ats_connection_id_application_id

Update an application

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.parse('2022-02-26').date(),
        candidate_id='illum',
        created_at=dateutil.parser.parse('2022-05-20').date(),
        id='c0f5d2cf-f7c7-40a4-9626-d436813f16d9',
        job_id='voluptatibus',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.parse('2022-01-15').date(),
        rejected_reason='quisquam',
        source='saepe',
        status=shared.AtsApplicationStatus.FIRST_INTERVIEW,
        updated_at=dateutil.parser.parse('2021-12-03').date(),
    ),
    connection_id='veniam',
    id='6146c3e2-50fb-4008-842e-141aac366c8d',
)

res = s.application.put_ats_connection_id_application_id(req, operations.PutAtsConnectionIDApplicationIDSecurity(
    jwt="",
))

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutAtsConnectionIDApplicationIDRequest](../../models/operations/putatsconnectionidapplicationidrequest.md)   | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `security`                                                                                                               | [operations.PutAtsConnectionIDApplicationIDSecurity](../../models/operations/putatsconnectionidapplicationidsecurity.md) | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |


### Response

**[operations.PutAtsConnectionIDApplicationIDResponse](../../models/operations/putatsconnectionidapplicationidresponse.md)**

