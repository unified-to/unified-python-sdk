# Job

## Overview

### Available Operations

* [create_ats_job](#create_ats_job) - Create a job
* [get_ats_job](#get_ats_job) - Retrieve a job
* [list_ats_jobs](#list_ats_jobs) - List all jobs
* [patch_ats_job](#patch_ats_job) - Update a job
* [remove_ats_job](#remove_ats_job) - Remove a job
* [update_ats_job](#update_ats_job) - Update a job

## create_ats_job

Create a job

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsJob" method="post" path="/ats/{connection_id}/job" example="ats_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.create_ats_job(request={
        "ats_job": {
            "addresses": [
                {
                    "address1": "98097 Carlo Trail",
                    "city": "South Judd",
                    "country_code": "US",
                    "postal_code": "89776-0669",
                    "region": "Mississippi",
                    "region_code": "FL",
                },
            ],
            "compensation": [
                {
                    "currency": "AUD",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "MZN",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Global",
            "employment_type": shared.EmploymentType.FREELANCE,
            "hiring_managers": [
                {
                    "id": "fd9852e3-9035-4f42-beb3-bbf4e4022122",
                    "name": "Eloise Mueller PhD",
                },
            ],
            "id": "75b6d077-2d72-42f4-a8a7-0b855cb42d9f",
            "industry": "Gorgeous Plastic Computer",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "29c0f65a-9797-4258-bf1a-71b296d295bc",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "acceptus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-05-10T08:49:09.246Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "8460 Nils Trace",
                        "city": "West Mervinburgh",
                        "country_code": "US",
                        "postal_code": "14162",
                        "region": "Maine",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-03T01:07:52.512Z"),
                    "description": "Deduco cultellus alii terebro depono thesaurus.",
                    "id": "f6101769-deb3-4721-978c-d205638870ee",
                    "is_active": False,
                    "location": "6788 Oxford Road",
                    "name": "Forward Security Orchestrator",
                    "posting_url": "https://ajar-metabolite.net/",
                    "updated_at": parse_datetime("2026-07-28T15:56:59.964Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Trepide provident taceo rem.",
                    "id": "289f27c0-311c-41e5-ad9d-cbe2097332c2",
                    "options": [
                        "censura",
                        "tum",
                    ],
                    "prompt": "Spectaculum mollitia arcus compello.",
                    "question": "Sodalitas nemo natus attonbitus reprehenderit voro depono constans vehemens ante.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "b3a0b53b-38f3-4e8d-84b9-f413a900d79b",
                    "options": [
                        "odit",
                    ],
                    "prompt": "Similique absque temeritas celebrer enim.",
                    "question": "Vinitor sodalitas desino sollers viduo volo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Abstergo possimus quibusdam deinde amoveo.",
                    "id": "568be61d-060e-4d8c-a8ab-8a17cb25edf3",
                    "options": [
                        "vallum",
                    ],
                    "prompt": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "question": "Subiungo ambitus neque talis amitto terreo alienus quae vulticulus.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "amiculum",
                "crux",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Amicitia vergo hic.",
            "updated_at": parse_datetime("2026-02-01T12:24:34.770Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_job is not None

    # Handle response
    print(res.ats_job)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateAtsJobRequest](../../models/operations/createatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateAtsJobResponse](../../models/operations/createatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_job

Retrieve a job

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsJob" method="get" path="/ats/{connection_id}/job/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.get_ats_job(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_job is not None

    # Handle response
    print(res.ats_job)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetAtsJobRequest](../../models/operations/getatsjobrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetAtsJobResponse](../../models/operations/getatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_jobs

List all jobs

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsJobs" method="get" path="/ats/{connection_id}/job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.list_ats_jobs(request={
        "connection_id": "<id>",
    })

    assert res.ats_jobs is not None

    # Handle response
    print(res.ats_jobs)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListAtsJobsRequest](../../models/operations/listatsjobsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListAtsJobsResponse](../../models/operations/listatsjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_job

Update a job

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsJob" method="patch" path="/ats/{connection_id}/job/{id}" example="ats_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.patch_ats_job(request={
        "ats_job": {
            "addresses": [
                {
                    "address1": "98097 Carlo Trail",
                    "city": "South Judd",
                    "country_code": "US",
                    "postal_code": "89776-0669",
                    "region": "Mississippi",
                    "region_code": "FL",
                },
            ],
            "compensation": [
                {
                    "currency": "AUD",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "MZN",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Global",
            "employment_type": shared.EmploymentType.FREELANCE,
            "hiring_managers": [
                {
                    "id": "fd9852e3-9035-4f42-beb3-bbf4e4022122",
                    "name": "Eloise Mueller PhD",
                },
            ],
            "id": "73ff78f4-5549-459d-b2df-dc2a833a4322",
            "industry": "Gorgeous Plastic Computer",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "b514a558-5f19-4182-abe3-5d5cd6ae1f4c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "acceptus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-05-10T08:49:09.286Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "8460 Nils Trace",
                        "city": "West Mervinburgh",
                        "country_code": "US",
                        "postal_code": "14162",
                        "region": "Maine",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-03T01:07:52.554Z"),
                    "description": "Deduco cultellus alii terebro depono thesaurus.",
                    "id": "f6101769-deb3-4721-978c-d205638870ee",
                    "is_active": False,
                    "location": "6788 Oxford Road",
                    "name": "Forward Security Orchestrator",
                    "posting_url": "https://ajar-metabolite.net/",
                    "updated_at": parse_datetime("2026-07-28T15:57:00.007Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Trepide provident taceo rem.",
                    "id": "289f27c0-311c-41e5-ad9d-cbe2097332c2",
                    "options": [
                        "censura",
                        "tum",
                    ],
                    "prompt": "Spectaculum mollitia arcus compello.",
                    "question": "Sodalitas nemo natus attonbitus reprehenderit voro depono constans vehemens ante.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "b3a0b53b-38f3-4e8d-84b9-f413a900d79b",
                    "options": [
                        "odit",
                    ],
                    "prompt": "Similique absque temeritas celebrer enim.",
                    "question": "Vinitor sodalitas desino sollers viduo volo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Abstergo possimus quibusdam deinde amoveo.",
                    "id": "568be61d-060e-4d8c-a8ab-8a17cb25edf3",
                    "options": [
                        "vallum",
                    ],
                    "prompt": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "question": "Subiungo ambitus neque talis amitto terreo alienus quae vulticulus.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "amiculum",
                "crux",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Amicitia vergo hic.",
            "updated_at": parse_datetime("2026-02-01T12:24:34.807Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_job is not None

    # Handle response
    print(res.ats_job)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchAtsJobRequest](../../models/operations/patchatsjobrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.PatchAtsJobResponse](../../models/operations/patchatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_job

Remove a job

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsJob" method="delete" path="/ats/{connection_id}/job/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.remove_ats_job(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RemoveAtsJobRequest](../../models/operations/removeatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.RemoveAtsJobResponse](../../models/operations/removeatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_job

Update a job

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsJob" method="put" path="/ats/{connection_id}/job/{id}" example="ats_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.update_ats_job(request={
        "ats_job": {
            "addresses": [
                {
                    "address1": "98097 Carlo Trail",
                    "city": "South Judd",
                    "country_code": "US",
                    "postal_code": "89776-0669",
                    "region": "Mississippi",
                    "region_code": "FL",
                },
            ],
            "compensation": [
                {
                    "currency": "AUD",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "MZN",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Global",
            "employment_type": shared.EmploymentType.FREELANCE,
            "hiring_managers": [
                {
                    "id": "fd9852e3-9035-4f42-beb3-bbf4e4022122",
                    "name": "Eloise Mueller PhD",
                },
            ],
            "id": "73ff78f4-5549-459d-b2df-dc2a833a4322",
            "industry": "Gorgeous Plastic Computer",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "b514a558-5f19-4182-abe3-5d5cd6ae1f4c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "acceptus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-05-10T08:49:09.286Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "8460 Nils Trace",
                        "city": "West Mervinburgh",
                        "country_code": "US",
                        "postal_code": "14162",
                        "region": "Maine",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-03T01:07:52.554Z"),
                    "description": "Deduco cultellus alii terebro depono thesaurus.",
                    "id": "f6101769-deb3-4721-978c-d205638870ee",
                    "is_active": False,
                    "location": "6788 Oxford Road",
                    "name": "Forward Security Orchestrator",
                    "posting_url": "https://ajar-metabolite.net/",
                    "updated_at": parse_datetime("2026-07-28T15:57:00.007Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Trepide provident taceo rem.",
                    "id": "289f27c0-311c-41e5-ad9d-cbe2097332c2",
                    "options": [
                        "censura",
                        "tum",
                    ],
                    "prompt": "Spectaculum mollitia arcus compello.",
                    "question": "Sodalitas nemo natus attonbitus reprehenderit voro depono constans vehemens ante.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "b3a0b53b-38f3-4e8d-84b9-f413a900d79b",
                    "options": [
                        "odit",
                    ],
                    "prompt": "Similique absque temeritas celebrer enim.",
                    "question": "Vinitor sodalitas desino sollers viduo volo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Abstergo possimus quibusdam deinde amoveo.",
                    "id": "568be61d-060e-4d8c-a8ab-8a17cb25edf3",
                    "options": [
                        "vallum",
                    ],
                    "prompt": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "question": "Subiungo ambitus neque talis amitto terreo alienus quae vulticulus.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "amiculum",
                "crux",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Amicitia vergo hic.",
            "updated_at": parse_datetime("2026-02-01T12:24:34.807Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_job is not None

    # Handle response
    print(res.ats_job)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateAtsJobRequest](../../models/operations/updateatsjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateAtsJobResponse](../../models/operations/updateatsjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |