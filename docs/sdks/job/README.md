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
            "id": "3ab57108-6bc5-409a-955b-6c82c5542d0f",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "11e21416-724e-4f18-bfcf-1f888b55982c",
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
                    "opened_at": parse_datetime("2026-07-10T20:01:30.707Z"),
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
                    "created_at": parse_datetime("2026-09-05T15:07:33.059Z"),
                    "description": "Sublime.",
                    "id": "25f867f5-1da7-4bcc-a6b1-aeccfcf048e9",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-02T17:38:08.977Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "9c9d4d4d-11ed-4587-b44d-4960715f58df",
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
                    "id": "d1cc070a-0b4c-4782-8006-7e496384c27f",
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
                    "id": "be09c6ce-b6bb-45b1-b42f-65ed91330632",
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
            "updated_at": parse_datetime("2026-03-29T07:17:11.670Z"),
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
            "id": "638911ba-832d-4cf8-8eb5-4861df8ef88d",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T04:42:55.725Z"),
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
            "id": "1584e045-d089-4f99-8ad6-3fb169dd4f03",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1a72bb7-3196-49b9-8f47-55b8f7972662",
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
                    "opened_at": parse_datetime("2026-07-10T20:01:30.758Z"),
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
                    "created_at": parse_datetime("2026-09-05T15:07:33.112Z"),
                    "description": "Sublime.",
                    "id": "407855cb-6747-4ad8-86fd-89ea9b1355f7",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-02T17:38:09.032Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "6fc65b89-aff2-467b-b55d-1c8f9f7b060b",
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
                    "id": "5d1aa8fe-e798-4826-aac5-c65631b743f5",
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
                    "id": "0d46be5f-11fa-446a-9b0e-401e374ba19b",
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
            "updated_at": parse_datetime("2026-03-29T07:17:11.716Z"),
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
            "id": "de1d5d35-6d81-47bb-bcac-7c0cd7a62fe2",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T04:42:55.778Z"),
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
            "id": "1584e045-d089-4f99-8ad6-3fb169dd4f03",
            "industry": "Refined Ceramic Keyboard",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1a72bb7-3196-49b9-8f47-55b8f7972662",
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
                    "opened_at": parse_datetime("2026-07-10T20:01:30.758Z"),
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
                    "created_at": parse_datetime("2026-09-05T15:07:33.112Z"),
                    "description": "Sublime.",
                    "id": "407855cb-6747-4ad8-86fd-89ea9b1355f7",
                    "is_active": False,
                    "location": "5699 Purdy Motorway",
                    "name": "Legacy Implementation Orchestrator",
                    "posting_url": "https://elementary-privilege.com/",
                    "updated_at": parse_datetime("2026-10-02T17:38:09.032Z"),
                },
            ],
            "public_job_urls": [
                "https://parched-dash.info",
                "https://mild-midwife.org/",
            ],
            "questions": [
                {
                    "description": "Capitulus.",
                    "id": "6fc65b89-aff2-467b-b55d-1c8f9f7b060b",
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
                    "id": "5d1aa8fe-e798-4826-aac5-c65631b743f5",
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
                    "id": "0d46be5f-11fa-446a-9b0e-401e374ba19b",
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
            "updated_at": parse_datetime("2026-03-29T07:17:11.716Z"),
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
            "id": "de1d5d35-6d81-47bb-bcac-7c0cd7a62fe2",
            "is_active": False,
            "metadata": [],
            "name": "Customer Security Assistant",
            "updated_at": parse_datetime("2023-02-13T04:42:55.778Z"),
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