# Application
(*application*)

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteAtsConnectionIDApplicationIDRequest(
    connection_id='markets sievert meh',
    id='<ID>',
)

res = s.application.delete_ats_connection_id_application_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.DeleteAtsConnectionIDApplicationIDRequest](../../models/operations/deleteatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.DeleteAtsConnectionIDApplicationIDResponse](../../models/operations/deleteatsconnectionidapplicationidresponse.md)**


## get_ats_connection_id_application

List all applications

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

req = operations.GetAtsConnectionIDApplicationRequest(
    candidate_id='turquoise',
    connection_id='Regional Bedfordshire',
    job_id='Northwest portal Electric',
    limit=576.8,
    offset=7467.13,
    order='Architect',
    query='loosely contingency',
    sort='female',
    updated_gte=dateutil.parser.isoparse('2023-09-05T13:59:23.348Z'),
)

res = s.application.get_ats_connection_id_application(req)

if res.ats_applications is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAtsConnectionIDApplicationRequest](../../models/operations/getatsconnectionidapplicationrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAtsConnectionIDApplicationResponse](../../models/operations/getatsconnectionidapplicationresponse.md)**


## get_ats_connection_id_application_id

Retrieve an application

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsConnectionIDApplicationIDRequest(
    connection_id='Buckinghamshire functionalities',
    id='<ID>',
)

res = s.application.get_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetAtsConnectionIDApplicationIDRequest](../../models/operations/getatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetAtsConnectionIDApplicationIDResponse](../../models/operations/getatsconnectionidapplicationidresponse.md)**


## patch_ats_connection_id_application_id

Update an application

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

req = operations.PatchAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2023-10-17T09:51:42.165Z'),
        candidate_id='North et beyond',
        created_at=dateutil.parser.isoparse('2023-01-08T08:26:22.845Z'),
        id='<ID>',
        job_id='ick Sausages Bronze',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2023-10-18T00:47:25.469Z'),
        rejected_reason='Avon Sum quis',
        source='Carolina Wooden Pop',
        status=shared.AtsApplicationStatus.HIRED,
        updated_at=dateutil.parser.isoparse('2021-07-20T22:05:46.009Z'),
    ),
    connection_id='Baby Paucek',
    id='<ID>',
)

res = s.application.patch_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PatchAtsConnectionIDApplicationIDRequest](../../models/operations/patchatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PatchAtsConnectionIDApplicationIDResponse](../../models/operations/patchatsconnectionidapplicationidresponse.md)**


## post_ats_connection_id_application

Create an application

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

req = operations.PostAtsConnectionIDApplicationRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2021-10-26T15:24:28.979Z'),
        candidate_id='solid',
        created_at=dateutil.parser.isoparse('2022-09-13T17:17:33.049Z'),
        id='<ID>',
        job_id='Gloves Pizza virtual',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2023-12-27T18:41:56.821Z'),
        rejected_reason='Northwest Kids',
        source='Human Tasty Loan',
        status=shared.AtsApplicationStatus.NEW,
        updated_at=dateutil.parser.isoparse('2022-11-01T21:08:50.319Z'),
    ),
    connection_id='Jazz',
)

res = s.application.post_ats_connection_id_application(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostAtsConnectionIDApplicationRequest](../../models/operations/postatsconnectionidapplicationrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostAtsConnectionIDApplicationResponse](../../models/operations/postatsconnectionidapplicationresponse.md)**


## put_ats_connection_id_application_id

Update an application

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

req = operations.PutAtsConnectionIDApplicationIDRequest(
    ats_application=shared.AtsApplication(
        applied_at=dateutil.parser.isoparse('2022-06-15T22:25:51.833Z'),
        candidate_id='farad Indianapolis',
        created_at=dateutil.parser.isoparse('2022-04-01T21:03:58.880Z'),
        id='<ID>',
        job_id='enable foreground',
        raw=shared.PropertyAtsApplicationRaw(),
        rejected_at=dateutil.parser.isoparse('2022-11-06T11:41:30.414Z'),
        rejected_reason='virtual North plum',
        source='Fort solid',
        status=shared.AtsApplicationStatus.SUBMITTED,
        updated_at=dateutil.parser.isoparse('2021-02-21T04:47:57.079Z'),
    ),
    connection_id='Southeast',
    id='<ID>',
)

res = s.application.put_ats_connection_id_application_id(req)

if res.ats_application is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PutAtsConnectionIDApplicationIDRequest](../../models/operations/putatsconnectionidapplicationidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PutAtsConnectionIDApplicationIDResponse](../../models/operations/putatsconnectionidapplicationidresponse.md)**

