# Job

## Overview

### Available Operations

* [create_ats_job](#create_ats_job) - Create a job
* [create_hris_job](#create_hris_job) - Create a job
* [get_ats_job](#get_ats_job) - Retrieve a job
* [get_hris_job](#get_hris_job) - Retrieve a job
* [list_ats_jobs](#list_ats_jobs) - List all jobs
* [list_hris_jobs](#list_hris_jobs) - List all jobs
* [patch_ats_job](#patch_ats_job) - Update a job
* [patch_hris_job](#patch_hris_job) - Update a job
* [remove_ats_job](#remove_ats_job) - Remove a job
* [remove_hris_job](#remove_hris_job) - Remove a job
* [update_ats_job](#update_ats_job) - Update a job
* [update_hris_job](#update_hris_job) - Update a job

## create_ats_job

Creates a AtsJob. Provide the unified AtsJob fields in the request body; they are mapped to the provider's API. Returns the created AtsJob.

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
                    "address1": "458 E 8th Street",
                    "city": "Visalia",
                    "country_code": "US",
                    "postal_code": "60669-0678",
                    "region": "Oregon",
                    "region_code": "DE",
                },
            ],
            "compensation": [
                {
                    "currency": "GBP",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "KMF",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Senior",
            "employment_type": shared.EmploymentType.FREELANCE,
            "fees": [
                {
                    "amount": 35146.0,
                    "currency": "AFN",
                    "type": shared.AtsFeeType.CONTINGENCY,
                },
            ],
            "hiring_managers": [],
            "id": "7c2d0f84-2243-48f6-9e51-26251ca9aed1",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "3117555d-fd2e-4afe-822f-fc1b06ddba7b",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "cursus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Senior Interactions Developer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Tolero aequus tamquam inflammatio asporto canis vinitor utrum.",
                    "opened_at": parse_datetime("2026-07-11T16:59:33.526Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "295 First Street",
                        "city": "East Agustinton",
                        "country_code": "US",
                        "postal_code": "57059",
                        "region": "Utah",
                        "region_code": "NE",
                    },
                    "created_at": parse_datetime("2026-09-06T13:09:22.636Z"),
                    "description": "Sublime.",
                    "id": "cf36aabc-11c4-43c6-a8eb-ac46dc02774f",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-03T16:10:24.791Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "a1286f3b-f07e-42aa-818b-97d550af12ca",
                    "max_length": 214.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                        "vado",
                    ],
                    "prompt": "Agnosco tendo.",
                    "question": "Deporto tolero.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "0d37bd1d-ce7e-458f-b79c-aaa567106afc",
                    "max_length": 309.0,
                    "min_length": 1.0,
                    "options": [
                        "sodalitas",
                    ],
                    "prompt": "Supra veritatis.",
                    "question": "Maxime tres tergiversatio tactus vehemens architecto ab nam defetiscor.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Confero trepide.",
                    "id": "d7127209-a6ea-4383-826c-f0ff5f785a0d",
                    "max_length": 428.0,
                    "min_length": 1.0,
                    "options": [
                        "censura",
                    ],
                    "prompt": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "question": "Attonbitus reprehenderit voro depono constans vehemens.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "similique",
                "absque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Contra damno desolo suadeo utrimque cresco aetas turpis.",
            "updated_at": parse_datetime("2026-03-30T02:18:58.852Z"),
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

## create_hris_job

Creates a HrisJob. Provide the unified HrisJob fields in the request body; they are mapped to the provider's API. Returns the created HrisJob.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisJob" method="post" path="/hris/{connection_id}/job" example="hris_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.create_hris_job(request={
        "hris_job": {
            "code": "P-54753",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Bonus vobis creator tabella callide cavus triumphus caveo abbas patria.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "199aad8c-3bc0-4e31-b07f-870d3b7af2eb",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T13:36:40.288Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_job is not None

    # Handle response
    print(res.hris_job)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateHrisJobRequest](../../models/operations/createhrisjobrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateHrisJobResponse](../../models/operations/createhrisjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_job

Retrieves a single AtsJob by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

## get_hris_job

Retrieves a single HrisJob by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisJob" method="get" path="/hris/{connection_id}/job/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.get_hris_job(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_job is not None

    # Handle response
    print(res.hris_job)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetHrisJobRequest](../../models/operations/gethrisjobrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GetHrisJobResponse](../../models/operations/gethrisjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_jobs

Returns a list of AtsJobs. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

## list_hris_jobs

Returns a list of HrisJobs. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisJobs" method="get" path="/hris/{connection_id}/job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.list_hris_jobs(request={
        "connection_id": "<id>",
    })

    assert res.hris_jobs is not None

    # Handle response
    print(res.hris_jobs)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListHrisJobsRequest](../../models/operations/listhrisjobsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.ListHrisJobsResponse](../../models/operations/listhrisjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_job

Updates the AtsJob identified by `id`. Provide the unified AtsJob fields to change in the request body.

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
                    "address1": "458 E 8th Street",
                    "city": "Visalia",
                    "country_code": "US",
                    "postal_code": "60669-0678",
                    "region": "Oregon",
                    "region_code": "DE",
                },
            ],
            "compensation": [
                {
                    "currency": "GBP",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "KMF",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Senior",
            "employment_type": shared.EmploymentType.FREELANCE,
            "fees": [
                {
                    "amount": 35146.0,
                    "currency": "AFN",
                    "type": shared.AtsFeeType.CONTINGENCY,
                },
            ],
            "hiring_managers": [],
            "id": "40644135-27ad-43a0-b1e3-0d6a1430ceff",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "3cd43e41-abdf-407a-9fc2-78906920e7e3",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "cursus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Senior Interactions Developer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Tolero aequus tamquam inflammatio asporto canis vinitor utrum.",
                    "opened_at": parse_datetime("2026-07-11T16:59:33.580Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "295 First Street",
                        "city": "East Agustinton",
                        "country_code": "US",
                        "postal_code": "57059",
                        "region": "Utah",
                        "region_code": "NE",
                    },
                    "created_at": parse_datetime("2026-09-06T13:09:22.693Z"),
                    "description": "Sublime.",
                    "id": "1a8da578-3715-4a97-90a4-582427a2840d",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-03T16:10:24.849Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "dd5cb256-8aa3-48cd-bd36-8b2c77e19263",
                    "max_length": 214.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                        "vado",
                    ],
                    "prompt": "Agnosco tendo.",
                    "question": "Deporto tolero.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "3ea22b02-f2da-4627-b91d-2eb61231a1b4",
                    "max_length": 309.0,
                    "min_length": 1.0,
                    "options": [
                        "sodalitas",
                    ],
                    "prompt": "Supra veritatis.",
                    "question": "Maxime tres tergiversatio tactus vehemens architecto ab nam defetiscor.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Confero trepide.",
                    "id": "b6f6c291-2109-4989-9a2f-dfa808ca0898",
                    "max_length": 428.0,
                    "min_length": 1.0,
                    "options": [
                        "censura",
                    ],
                    "prompt": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "question": "Attonbitus reprehenderit voro depono constans vehemens.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "similique",
                "absque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Contra damno desolo suadeo utrimque cresco aetas turpis.",
            "updated_at": parse_datetime("2026-03-30T02:18:58.902Z"),
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

## patch_hris_job

Updates the HrisJob identified by `id`. Provide the unified HrisJob fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisJob" method="patch" path="/hris/{connection_id}/job/{id}" example="hris_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.patch_hris_job(request={
        "hris_job": {
            "code": "P-54753",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Bonus vobis creator tabella callide cavus triumphus caveo abbas patria.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "97769657-5d9c-40c5-9d0b-5059c852ff60",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T13:36:40.338Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_job is not None

    # Handle response
    print(res.hris_job)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PatchHrisJobRequest](../../models/operations/patchhrisjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.PatchHrisJobResponse](../../models/operations/patchhrisjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_job

Deletes the AtsJob identified by `id`.

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

## remove_hris_job

Deletes the HrisJob identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisJob" method="delete" path="/hris/{connection_id}/job/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.remove_hris_job(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveHrisJobRequest](../../models/operations/removehrisjobrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.RemoveHrisJobResponse](../../models/operations/removehrisjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_job

Updates the AtsJob identified by `id`. Provide the unified AtsJob fields to change in the request body.

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
                    "address1": "458 E 8th Street",
                    "city": "Visalia",
                    "country_code": "US",
                    "postal_code": "60669-0678",
                    "region": "Oregon",
                    "region_code": "DE",
                },
            ],
            "compensation": [
                {
                    "currency": "GBP",
                    "frequency": shared.Frequency.DAY,
                    "max": 174303.0,
                    "min": 174042.0,
                    "type": shared.AtsCompensationType.BONUS,
                },
                {
                    "currency": "KMF",
                    "frequency": shared.Frequency.MONTH,
                    "max": 171171.0,
                    "min": 151975.0,
                    "type": shared.AtsCompensationType.SALARY,
                },
            ],
            "created_at": parse_datetime("2023-06-16T12:51:44.518Z"),
            "description": "Senior",
            "employment_type": shared.EmploymentType.FREELANCE,
            "fees": [
                {
                    "amount": 35146.0,
                    "currency": "AFN",
                    "type": shared.AtsFeeType.CONTINGENCY,
                },
            ],
            "hiring_managers": [],
            "id": "40644135-27ad-43a0-b1e3-0d6a1430ceff",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "3cd43e41-abdf-407a-9fc2-78906920e7e3",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "cursus",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Senior Interactions Developer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Tolero aequus tamquam inflammatio asporto canis vinitor utrum.",
                    "opened_at": parse_datetime("2026-07-11T16:59:33.580Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "295 First Street",
                        "city": "East Agustinton",
                        "country_code": "US",
                        "postal_code": "57059",
                        "region": "Utah",
                        "region_code": "NE",
                    },
                    "created_at": parse_datetime("2026-09-06T13:09:22.693Z"),
                    "description": "Sublime.",
                    "id": "1a8da578-3715-4a97-90a4-582427a2840d",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-03T16:10:24.849Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "dd5cb256-8aa3-48cd-bd36-8b2c77e19263",
                    "max_length": 214.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                        "vado",
                    ],
                    "prompt": "Agnosco tendo.",
                    "question": "Deporto tolero.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "3ea22b02-f2da-4627-b91d-2eb61231a1b4",
                    "max_length": 309.0,
                    "min_length": 1.0,
                    "options": [
                        "sodalitas",
                    ],
                    "prompt": "Supra veritatis.",
                    "question": "Maxime tres tergiversatio tactus vehemens architecto ab nam defetiscor.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Confero trepide.",
                    "id": "b6f6c291-2109-4989-9a2f-dfa808ca0898",
                    "max_length": 428.0,
                    "min_length": 1.0,
                    "options": [
                        "censura",
                    ],
                    "prompt": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "question": "Attonbitus reprehenderit voro depono constans vehemens.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "similique",
                "absque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Contra damno desolo suadeo utrimque cresco aetas turpis.",
            "updated_at": parse_datetime("2026-03-30T02:18:58.902Z"),
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

## update_hris_job

Updates the HrisJob identified by `id`. Provide the unified HrisJob fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisJob" method="put" path="/hris/{connection_id}/job/{id}" example="hris_job" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.job.update_hris_job(request={
        "hris_job": {
            "code": "P-54753",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Bonus vobis creator tabella callide cavus triumphus caveo abbas patria.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "97769657-5d9c-40c5-9d0b-5059c852ff60",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T13:36:40.338Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_job is not None

    # Handle response
    print(res.hris_job)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateHrisJobRequest](../../models/operations/updatehrisjobrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.UpdateHrisJobResponse](../../models/operations/updatehrisjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |