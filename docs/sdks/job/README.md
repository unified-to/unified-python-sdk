# Job
(*job*)

### Available Operations

* [delete_ats_connection_id_job_id](#delete_ats_connection_id_job_id) - Remove a job
* [get_ats_connection_id_job](#get_ats_connection_id_job) - List all jobs
* [get_ats_connection_id_job_id](#get_ats_connection_id_job_id) - Retrieve a job
* [patch_ats_connection_id_job_id](#patch_ats_connection_id_job_id) - Update a job
* [post_ats_connection_id_job](#post_ats_connection_id_job) - Create a job
* [put_ats_connection_id_job_id](#put_ats_connection_id_job_id) - Update a job

## delete_ats_connection_id_job_id

Remove a job

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteAtsConnectionIDJobIDRequest(
    connection_id='Sedan Bedfordshire Hybrid',
    id='<ID>',
)

res = s.job.delete_ats_connection_id_job_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteAtsConnectionIDJobIDRequest](../../models/operations/deleteatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.DeleteAtsConnectionIDJobIDResponse](../../models/operations/deleteatsconnectionidjobidresponse.md)**


## get_ats_connection_id_job

List all jobs

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

req = operations.GetAtsConnectionIDJobRequest(
    connection_id='City katal',
    limit=3542.62,
    offset=5417.97,
    order='publisher',
    query='Folding',
    sort='Kip gross recontextualize',
    updated_gte=dateutil.parser.isoparse('2022-10-12T03:36:20.050Z'),
)

res = s.job.get_ats_connection_id_job(req)

if res.ats_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAtsConnectionIDJobRequest](../../models/operations/getatsconnectionidjobrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAtsConnectionIDJobResponse](../../models/operations/getatsconnectionidjobresponse.md)**


## get_ats_connection_id_job_id

Retrieve a job

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetAtsConnectionIDJobIDRequest(
    connection_id='Jazz',
    id='<ID>',
)

res = s.job.get_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAtsConnectionIDJobIDRequest](../../models/operations/getatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetAtsConnectionIDJobIDResponse](../../models/operations/getatsconnectionidjobidresponse.md)**


## patch_ats_connection_id_job_id

Update a job

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

req = operations.PatchAtsConnectionIDJobIDRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='Transexual',
                address2='Planner redundant Towels',
                city='Starkboro',
                country='Chad',
                country_code='NU',
                postal_code='22603',
                region='Cambridgeshire',
                region_code='Account Copernicium at',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2023-01-02T09:14:26.844Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Metical',
                frequency=shared.AtsCompensationFrequency.HOUR,
                max=1424.24,
                min=3626.17,
                type=shared.AtsCompensationType.SALARY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-03-16T15:29:37.822Z'),
        departments=[
            'Sports',
        ],
        description='Operative bi-directional capability',
        employment_type=shared.AtsJobEmploymentType.INTERN,
        hiring_manager_ids=[
            'Hop',
        ],
        id='<ID>',
        language_locale='hence gracefully invoice',
        name='Southeast vacantly Uranium',
        public_job_urls=[
            'Keith',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'happily',
        ],
        remote=False,
        status=shared.AtsJobStatus.OPEN,
        updated_at=dateutil.parser.isoparse('2023-08-04T07:33:03.088Z'),
    ),
    connection_id='Cis benchmark',
    id='<ID>',
)

res = s.job.patch_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAtsConnectionIDJobIDRequest](../../models/operations/patchatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PatchAtsConnectionIDJobIDResponse](../../models/operations/patchatsconnectionidjobidresponse.md)**


## post_ats_connection_id_job

Create a job

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

req = operations.PostAtsConnectionIDJobRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='Forward',
                address2='Electric fuchsia kelvin',
                city='Fort Sibylmouth',
                country='Solomon Islands',
                country_code='DO',
                postal_code='39037',
                region='Rockford',
                region_code='Trafficway eaque athwart',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-04-22T19:01:40.265Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Gourde',
                frequency=shared.AtsCompensationFrequency.YEAR,
                max=5349.62,
                min=526.63,
                type=shared.AtsCompensationType.EQUITY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2021-04-02T18:44:02.642Z'),
        departments=[
            'Polonium',
        ],
        description='Progressive disintermediate matrix',
        employment_type=shared.AtsJobEmploymentType.INTERN,
        hiring_manager_ids=[
            'itaque',
        ],
        id='<ID>',
        language_locale='the joyfully',
        name='Other because harbor',
        public_job_urls=[
            'coil',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'JSON',
        ],
        remote=False,
        status=shared.AtsJobStatus.ARCHIVED,
        updated_at=dateutil.parser.isoparse('2022-05-24T04:21:24.567Z'),
    ),
    connection_id='Coordinator applications',
)

res = s.job.post_ats_connection_id_job(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PostAtsConnectionIDJobRequest](../../models/operations/postatsconnectionidjobrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PostAtsConnectionIDJobResponse](../../models/operations/postatsconnectionidjobresponse.md)**


## put_ats_connection_id_job_id

Update a job

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

req = operations.PutAtsConnectionIDJobIDRequest(
    ats_job=shared.AtsJob(
        addresses=[
            shared.AtsAddress(
                address1='cotton Washington',
                address2='rosin meanwhile male',
                city='East Sierra',
                country='Somalia',
                country_code='BQ',
                postal_code='63475-6123',
                region='lighthearted online Bicycle',
                region_code='robust',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2021-05-06T11:53:52.940Z'),
        compensation=[
            shared.AtsCompensation(
                currency='Iranian Rial',
                frequency=shared.AtsCompensationFrequency.YEAR,
                max=5965.42,
                min=5273.81,
                type=shared.AtsCompensationType.BONUS,
            ),
        ],
        created_at=dateutil.parser.isoparse('2023-07-19T02:36:00.215Z'),
        departments=[
            'embrace',
        ],
        description='Programmable tertiary benchmark',
        employment_type=shared.AtsJobEmploymentType.CONTRACTOR,
        hiring_manager_ids=[
            'New',
        ],
        id='<ID>',
        language_locale='Facilitator Gasoline application',
        name='North impractical',
        public_job_urls=[
            'clamber',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'West',
        ],
        remote=False,
        status=shared.AtsJobStatus.CLOSED,
        updated_at=dateutil.parser.isoparse('2023-02-01T04:41:47.094Z'),
    ),
    connection_id='North',
    id='<ID>',
)

res = s.job.put_ats_connection_id_job_id(req)

if res.ats_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PutAtsConnectionIDJobIDRequest](../../models/operations/putatsconnectionidjobidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PutAtsConnectionIDJobIDResponse](../../models/operations/putatsconnectionidjobidresponse.md)**

