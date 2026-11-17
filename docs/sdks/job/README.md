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
            "hiring_managers": [],
            "id": "5c299772-bb61-4bd6-a478-12b4f52ebe87",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "b23c33b3-6ec2-40d7-9f3d-cfe1f6ff16f1",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "desolo",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-07-01T21:04:13.112Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "75008 Medhurst Road",
                        "city": "Madelynnshire",
                        "country_code": "US",
                        "postal_code": "98754",
                        "region": "Wisconsin",
                        "region_code": "CO",
                    },
                    "created_at": parse_datetime("2026-08-27T05:16:24.156Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "c2b45312-eb22-44a0-8507-47f0fa9291fc",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-09-23T02:34:57.791Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "d3584c60-6f82-4ca6-9582-43c54036b443",
                    "max_length": 117.0,
                    "min_length": 1.0,
                    "options": [
                        "tactus",
                        "vehemens",
                    ],
                    "prompt": "Totam maxime tres tergiversatio.",
                    "question": "Doloribus mollitia.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "1aca8db8-a345-459f-afd6-14bea2cb39db",
                    "max_length": 453.0,
                    "min_length": 1.0,
                    "options": [
                        "constans",
                    ],
                    "prompt": "Veritatis sodalitas nemo natus attonbitus reprehenderit voro depono.",
                    "question": "Nam.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "id": "1c3b9ba7-cde6-48ff-9892-8891439b4610",
                    "max_length": 66.0,
                    "min_length": 1.0,
                    "options": [
                        "repellendus",
                    ],
                    "prompt": "Tum tamisium autus.",
                    "question": "Confero trepide.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "suadeo",
                "utrimque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Crepusculum adsuesco vere.",
            "updated_at": parse_datetime("2026-03-21T04:11:47.167Z"),
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
            "code": "P-05547",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Alienus timor depromo bonus vobis creator tabella callide cavus triumphus caveo.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "43d56389-f6e8-40af-adb8-bc5590f31aba",
            "is_active": False,
            "metadata": [],
            "name": "Internal Integration Specialist",
            "updated_at": parse_datetime("2023-02-09T09:31:04.675Z"),
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
            "hiring_managers": [],
            "id": "cf515b25-171f-4002-9c68-5e1ec3b65a23",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "057e2ba6-817d-493b-a728-aa8eeb46b7b5",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "desolo",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-07-01T21:04:13.159Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "75008 Medhurst Road",
                        "city": "Madelynnshire",
                        "country_code": "US",
                        "postal_code": "98754",
                        "region": "Wisconsin",
                        "region_code": "CO",
                    },
                    "created_at": parse_datetime("2026-08-27T05:16:24.205Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "95d1ac1e-0a07-4b9c-b1b4-8cf63fe1ba18",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-09-23T02:34:57.841Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "21f5b40f-968c-4a41-a030-a1675e2e0279",
                    "max_length": 117.0,
                    "min_length": 1.0,
                    "options": [
                        "tactus",
                        "vehemens",
                    ],
                    "prompt": "Totam maxime tres tergiversatio.",
                    "question": "Doloribus mollitia.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "fb138a47-731b-4201-83d4-69671349fe05",
                    "max_length": 453.0,
                    "min_length": 1.0,
                    "options": [
                        "constans",
                    ],
                    "prompt": "Veritatis sodalitas nemo natus attonbitus reprehenderit voro depono.",
                    "question": "Nam.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "id": "09a82ab3-c96a-4d04-9706-e3cc7f7964e9",
                    "max_length": 66.0,
                    "min_length": 1.0,
                    "options": [
                        "repellendus",
                    ],
                    "prompt": "Tum tamisium autus.",
                    "question": "Confero trepide.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "suadeo",
                "utrimque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Crepusculum adsuesco vere.",
            "updated_at": parse_datetime("2026-03-21T04:11:47.210Z"),
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
            "code": "P-05547",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Alienus timor depromo bonus vobis creator tabella callide cavus triumphus caveo.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "9e336f5a-3285-4b74-babd-27e8c3f1aa82",
            "is_active": False,
            "metadata": [],
            "name": "Internal Integration Specialist",
            "updated_at": parse_datetime("2023-02-09T09:31:04.716Z"),
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
            "hiring_managers": [],
            "id": "cf515b25-171f-4002-9c68-5e1ec3b65a23",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "057e2ba6-817d-493b-a728-aa8eeb46b7b5",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "desolo",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-07-01T21:04:13.159Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "75008 Medhurst Road",
                        "city": "Madelynnshire",
                        "country_code": "US",
                        "postal_code": "98754",
                        "region": "Wisconsin",
                        "region_code": "CO",
                    },
                    "created_at": parse_datetime("2026-08-27T05:16:24.205Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "95d1ac1e-0a07-4b9c-b1b4-8cf63fe1ba18",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-09-23T02:34:57.841Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "21f5b40f-968c-4a41-a030-a1675e2e0279",
                    "max_length": 117.0,
                    "min_length": 1.0,
                    "options": [
                        "tactus",
                        "vehemens",
                    ],
                    "prompt": "Totam maxime tres tergiversatio.",
                    "question": "Doloribus mollitia.",
                    "required": True,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "id": "fb138a47-731b-4201-83d4-69671349fe05",
                    "max_length": 453.0,
                    "min_length": 1.0,
                    "options": [
                        "constans",
                    ],
                    "prompt": "Veritatis sodalitas nemo natus attonbitus reprehenderit voro depono.",
                    "question": "Nam.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Taceo rem compello spectaculum mollitia arcus compello.",
                    "id": "09a82ab3-c96a-4d04-9706-e3cc7f7964e9",
                    "max_length": 66.0,
                    "min_length": 1.0,
                    "options": [
                        "repellendus",
                    ],
                    "prompt": "Tum tamisium autus.",
                    "question": "Confero trepide.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "suadeo",
                "utrimque",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Crepusculum adsuesco vere.",
            "updated_at": parse_datetime("2026-03-21T04:11:47.210Z"),
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
            "code": "P-05547",
            "created_at": parse_datetime("2020-10-28T01:13:19.491Z"),
            "description": "Alienus timor depromo bonus vobis creator tabella callide cavus triumphus caveo.",
            "employment_type": shared.HrisJobEmploymentType.FREELANCE,
            "id": "9e336f5a-3285-4b74-babd-27e8c3f1aa82",
            "is_active": False,
            "metadata": [],
            "name": "Internal Integration Specialist",
            "updated_at": parse_datetime("2023-02-09T09:31:04.716Z"),
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