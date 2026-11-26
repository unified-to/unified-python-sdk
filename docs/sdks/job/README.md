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
            "id": "51b2e44b-bc3d-41b6-8a2b-801dc779bba1",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "21504bf0-8901-4c2f-b580-c140dd7ed16c",
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
                    "opened_at": parse_datetime("2026-07-09T20:52:00.154Z"),
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
                    "created_at": parse_datetime("2026-09-04T14:47:35.863Z"),
                    "description": "Sublime.",
                    "id": "baf58a0f-9733-491d-a1c0-466e05848254",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-01T16:44:34.707Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "f9c87bce-2f83-43a5-97a2-990f49711e96",
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
                    "id": "05f3c542-54e8-4be5-b1f4-7a355cb58925",
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
                    "id": "98fc3f1a-6987-4708-8242-819b85317545",
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
            "updated_at": parse_datetime("2026-03-28T10:16:05.688Z"),
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
            "id": "48f68109-bccc-45e3-ae33-c629ba7c189d",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-12T18:53:24.575Z"),
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
            "id": "adeb58d5-a0fb-481b-855c-6616f087ccd9",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "177d39f4-0857-4739-b21a-5566f26c685a",
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
                    "opened_at": parse_datetime("2026-07-09T20:52:00.189Z"),
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
                    "created_at": parse_datetime("2026-09-04T14:47:35.898Z"),
                    "description": "Sublime.",
                    "id": "26e7ff5b-c0f1-4abe-976f-49e77f5a67b4",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-01T16:44:34.744Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "b6e92350-665c-4108-a972-8397a78c870a",
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
                    "id": "e08216a8-df46-4801-84df-9ad4db1091d6",
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
                    "id": "d9bc518d-ba03-4606-ba5c-f1b33781a5a4",
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
            "updated_at": parse_datetime("2026-03-28T10:16:05.719Z"),
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
            "id": "7ca26670-3428-4d9f-8826-2ff233ba5ffb",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-12T18:53:24.609Z"),
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
            "id": "adeb58d5-a0fb-481b-855c-6616f087ccd9",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "177d39f4-0857-4739-b21a-5566f26c685a",
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
                    "opened_at": parse_datetime("2026-07-09T20:52:00.189Z"),
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
                    "created_at": parse_datetime("2026-09-04T14:47:35.898Z"),
                    "description": "Sublime.",
                    "id": "26e7ff5b-c0f1-4abe-976f-49e77f5a67b4",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-01T16:44:34.744Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "b6e92350-665c-4108-a972-8397a78c870a",
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
                    "id": "e08216a8-df46-4801-84df-9ad4db1091d6",
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
                    "id": "d9bc518d-ba03-4606-ba5c-f1b33781a5a4",
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
            "updated_at": parse_datetime("2026-03-28T10:16:05.719Z"),
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
            "id": "7ca26670-3428-4d9f-8826-2ff233ba5ffb",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-12T18:53:24.609Z"),
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