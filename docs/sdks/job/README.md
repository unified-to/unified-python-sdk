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
    connection_id='adipisci',
    id='2e3b49db-e0f2-43b7-b6d9-948d6eded477',
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
    connection_id='voluptas',
    limit=5378.51,
    offset=504.05,
    order='reiciendis',
    query='minus',
    sort='iure',
    updated_gte=dateutil.parser.isoparse('2022-11-11T00:39:35.207Z'),
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
    connection_id='iure',
    id='a82e5e82-fd28-4d10-80a7-e91392ab44cb',
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
                address1='architecto',
                address2='totam',
                city='West Aaron',
                country='Aruba',
                country_code='LA',
                postal_code='23078-3185',
                region='illo',
                region_code='tempora',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-05-27T21:54:13.074Z'),
        compensation=[
            shared.AtsCompensation(
                currency='rem',
                frequency=shared.AtsCompensationFrequency.HOUR,
                max=6129.79,
                min=7255.92,
                type=shared.AtsCompensationType.EQUITY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-08-10T22:57:33.587Z'),
        departments=[
            'aperiam',
        ],
        description='similique',
        employment_type=shared.AtsJobEmploymentType.FREELANCE,
        hiring_manager_ids=[
            'pariatur',
        ],
        id='fde410c3-7daa-4918-aa49-d9625d3caffc',
        language_locale='inventore',
        name='Guy Von',
        public_job_urls=[
            'modi',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'quaerat',
        ],
        remote=False,
        status=shared.AtsJobStatus.PENDING,
        updated_at=dateutil.parser.isoparse('2022-07-04T21:18:33.130Z'),
    ),
    connection_id='unde',
    id='2bcd440e-a98b-4ecc-a048-6de0d56d73b0',
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
                address1='quae',
                address2='quis',
                city='North Consuelo',
                country='Turkmenistan',
                country_code='LK',
                postal_code='74149-9447',
                region='iure',
                region_code='ullam',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-07-06T19:55:18.068Z'),
        compensation=[
            shared.AtsCompensation(
                currency='enim',
                frequency=shared.AtsCompensationFrequency.WEEK,
                max=3432.31,
                min=6902.62,
                type=shared.AtsCompensationType.STOCK_OPTIONS,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-01-28T21:56:06.312Z'),
        departments=[
            'consectetur',
        ],
        description='vero',
        employment_type=shared.AtsJobEmploymentType.CONTRACTOR,
        hiring_manager_ids=[
            'optio',
        ],
        id='fcc6a91e-c526-424d-8001-4ef45cea11ac',
        language_locale='minima',
        name='Henrietta Powlowski',
        public_job_urls=[
            'nostrum',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'corrupti',
        ],
        remote=False,
        status=shared.AtsJobStatus.DRAFT,
        updated_at=dateutil.parser.isoparse('2022-04-19T01:37:46.134Z'),
    ),
    connection_id='eius',
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
                address1='voluptatem',
                address2='magnam',
                city='West Randibury',
                country='Rwanda',
                country_code='MK',
                postal_code='89820-0695',
                region='doloribus',
                region_code='unde',
            ),
        ],
        closed_at=dateutil.parser.isoparse('2022-03-17T10:24:00.538Z'),
        compensation=[
            shared.AtsCompensation(
                currency='id',
                frequency=shared.AtsCompensationFrequency.WEEK,
                max=1012.53,
                min=7482.56,
                type=shared.AtsCompensationType.SALARY,
            ),
        ],
        created_at=dateutil.parser.isoparse('2022-08-21T15:07:46.264Z'),
        departments=[
            'a',
        ],
        description='architecto',
        employment_type=shared.AtsJobEmploymentType.FREELANCE,
        hiring_manager_ids=[
            'vitae',
        ],
        id='4718c6fa-2fad-40c0-ac5d-95472cdd14fc',
        language_locale='eius',
        name='Miss Bridget King',
        public_job_urls=[
            'fuga',
        ],
        raw=shared.PropertyAtsJobRaw(),
        recruiter_ids=[
            'laudantium',
        ],
        remote=False,
        status=shared.AtsJobStatus.DRAFT,
        updated_at=dateutil.parser.isoparse('2020-12-28T11:43:36.436Z'),
    ),
    connection_id='dignissimos',
    id='0c43351c-3dd1-4eb8-b7f7-5f4f23f1c0a5',
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

