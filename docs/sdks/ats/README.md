# Ats

## Overview

### Available Operations

* [create_ats_activity](#create_ats_activity) - Create an activity
* [create_ats_application](#create_ats_application) - Create an application
* [create_ats_candidate](#create_ats_candidate) - Create a candidate
* [create_ats_company](#create_ats_company) - Create a company
* [create_ats_document](#create_ats_document) - Create a document
* [create_ats_interview](#create_ats_interview) - Create an interview
* [create_ats_job](#create_ats_job) - Create a job
* [create_ats_scorecard](#create_ats_scorecard) - Create a scorecard
* [get_ats_activity](#get_ats_activity) - Retrieve an activity
* [get_ats_application](#get_ats_application) - Retrieve an application
* [get_ats_applicationstatus](#get_ats_applicationstatus) - Retrieve an applicationstatus
* [get_ats_candidate](#get_ats_candidate) - Retrieve a candidate
* [get_ats_company](#get_ats_company) - Retrieve a company
* [get_ats_document](#get_ats_document) - Retrieve a document
* [get_ats_interview](#get_ats_interview) - Retrieve an interview
* [get_ats_job](#get_ats_job) - Retrieve a job
* [get_ats_scorecard](#get_ats_scorecard) - Retrieve a scorecard
* [list_ats_activities](#list_ats_activities) - List all activities
* [list_ats_applications](#list_ats_applications) - List all applications
* [list_ats_applicationstatuses](#list_ats_applicationstatuses) - List all applicationstatuses
* [list_ats_candidates](#list_ats_candidates) - List all candidates
* [list_ats_companies](#list_ats_companies) - List all companies
* [list_ats_documents](#list_ats_documents) - List all documents
* [list_ats_interviews](#list_ats_interviews) - List all interviews
* [list_ats_jobs](#list_ats_jobs) - List all jobs
* [list_ats_scorecards](#list_ats_scorecards) - List all scorecards
* [patch_ats_activity](#patch_ats_activity) - Update an activity
* [patch_ats_application](#patch_ats_application) - Update an application
* [patch_ats_candidate](#patch_ats_candidate) - Update a candidate
* [patch_ats_company](#patch_ats_company) - Update a company
* [patch_ats_document](#patch_ats_document) - Update a document
* [patch_ats_interview](#patch_ats_interview) - Update an interview
* [patch_ats_job](#patch_ats_job) - Update a job
* [patch_ats_scorecard](#patch_ats_scorecard) - Update a scorecard
* [remove_ats_activity](#remove_ats_activity) - Remove an activity
* [remove_ats_application](#remove_ats_application) - Remove an application
* [remove_ats_candidate](#remove_ats_candidate) - Remove a candidate
* [remove_ats_company](#remove_ats_company) - Remove a company
* [remove_ats_document](#remove_ats_document) - Remove a document
* [remove_ats_interview](#remove_ats_interview) - Remove an interview
* [remove_ats_job](#remove_ats_job) - Remove a job
* [remove_ats_scorecard](#remove_ats_scorecard) - Remove a scorecard
* [update_ats_activity](#update_ats_activity) - Update an activity
* [update_ats_application](#update_ats_application) - Update an application
* [update_ats_candidate](#update_ats_candidate) - Update a candidate
* [update_ats_company](#update_ats_company) - Update a company
* [update_ats_document](#update_ats_document) - Update a document
* [update_ats_interview](#update_ats_interview) - Update an interview
* [update_ats_job](#update_ats_job) - Update a job
* [update_ats_scorecard](#update_ats_scorecard) - Update a scorecard

## create_ats_activity

Create an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsActivity" method="post" path="/ats/{connection_id}/activity" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_activity(request={
        "ats_activity": {
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Sapiente.",
            "id": "cc456114-11b4-4454-b2c6-674da4151680",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "bc322752-5cd3-4a7f-91a8-4b2d8e660b4d",
                    "namespace": "activity",
                    "slug": "cimentarius",
                    "value": "Reprehenderit verto.",
                },
            ],
            "sub_type": "TASK",
            "title": "Venio blandior aureus.",
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-04-04T06:33:50.655Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAtsActivityRequest](../../models/operations/createatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAtsActivityResponse](../../models/operations/createatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ats_application

Create an application

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsApplication" method="post" path="/ats/{connection_id}/application" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-29T18:38:27.347Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-12T18:26:15.802Z"),
            "id": "3be64929-f537-4521-9361-c4c8326d0157",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "220edaf6-bc48-4c79-b54b-6ceb2c57dd0d",
                    "namespace": "application",
                    "slug": "stella",
                    "value": "Caput.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-11T13:02:04.086Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Arguo repudiandae defessus. Adflicto caecus claustrum annus addo vere crebro. Alias sponte turbo sopor vergo surculus nam.",
            "updated_at": parse_datetime("2026-10-18T09:16:18.517Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAtsApplicationRequest](../../models/operations/createatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAtsApplicationResponse](../../models/operations/createatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ats_candidate

Create a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsCandidate" method="post" path="/ats/{connection_id}/candidate" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "621ede17-d7bb-4d42-b84f-e8f3bead71b6",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "ca216ebe-fe55-403b-aad2-7b1e449ca34b",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-28T17:46:38.408Z"),
            "web_url": "https://fragrant-husband.net/",
        },
        "connection_id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsCandidateRequest](../../models/operations/createatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAtsCandidateResponse](../../models/operations/createatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ats_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsCompany" method="post" path="/ats/{connection_id}/company" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "798fe2f6-ae0a-4d17-aa92-734c80c4a4b9",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-882-360-2010",
            "updated_at": parse_datetime("2020-10-01T04:11:25.065Z"),
            "website_url": "https://www.gulgowskidibbert.com",
        },
        "connection_id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateAtsCompanyRequest](../../models/operations/createatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateAtsCompanyResponse](../../models/operations/createatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ats_document

Create a document

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsDocument" method="post" path="/ats/{connection_id}/document" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "1bb55c59-99ba-4c6a-be78-a8f1155ed818",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-07T04:58:38.769Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAtsDocumentRequest](../../models/operations/createatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateAtsDocumentResponse](../../models/operations/createatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ats_interview

Create an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsInterview" method="post" path="/ats/{connection_id}/interview" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2021-12-08T06:33:19.583Z"),
            "id": "ddcec412-5ab6-4d71-a2bc-813065c792ee",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "metadata": [],
            "start_at": parse_datetime("2021-12-08T06:03:19.583Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2023-09-23T16:37:18.637Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsInterviewRequest](../../models/operations/createatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAtsInterviewResponse](../../models/operations/createatsinterviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.ats.create_ats_job(request={
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
            "id": "d5878e4b-8b8f-42a6-8ed9-1078a38a0843",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "5ec867ec-230e-42d9-ab19-cc1e65806529",
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
                    "opened_at": parse_datetime("2026-06-07T21:23:37.269Z"),
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
                    "created_at": parse_datetime("2026-08-02T00:24:41.868Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "641a68a5-3712-4e4d-98fb-b45036a7a779",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-08-28T07:47:34.839Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "862283a1-8f32-48d3-b3f4-a27311eb8b87",
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
                    "id": "c437e681-b81f-4367-82ad-0ff3cebce049",
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
                    "id": "f614bca7-6772-4f1b-8d02-732ae899fd2f",
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
            "updated_at": parse_datetime("2026-02-27T09:43:12.513Z"),
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

## create_ats_scorecard

Create a scorecard

### Example Usage

<!-- UsageSnippet language="python" operationID="createAtsScorecard" method="post" path="/ats/{connection_id}/scorecard" example="ats_scorecard" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.create_ats_scorecard(request={
        "ats_scorecard": {
            "comment": "Maiores enim.",
            "created_at": parse_datetime("2022-02-20T17:09:45.498Z"),
            "id": "443f5ff6-4fd5-48f3-888d-da7840d715ea",
            "metadata": [],
            "questions": [
                {
                    "description": "Sulum textor eveniet facere vita.",
                    "text": "Aliquam.",
                },
                {
                    "answer": "Decretum.",
                    "description": "Conatus cicuta doloremque statua bonus.",
                    "text": "Pecto vulpes libero vomer comburo.",
                },
            ],
            "recommendation": shared.Recommendation.STRONG_YES,
            "updated_at": parse_datetime("2023-06-05T13:38:40.488Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ats_scorecard is not None

    # Handle response
    print(res.ats_scorecard)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAtsScorecardRequest](../../models/operations/createatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateAtsScorecardResponse](../../models/operations/createatsscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_activity

Retrieve an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsActivity" method="get" path="/ats/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAtsActivityRequest](../../models/operations/getatsactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAtsActivityResponse](../../models/operations/getatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_application

Retrieve an application

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsApplication" method="get" path="/ats/{connection_id}/application/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_application(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAtsApplicationRequest](../../models/operations/getatsapplicationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAtsApplicationResponse](../../models/operations/getatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_applicationstatus

Retrieve an applicationstatus

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsApplicationstatus" method="get" path="/ats/{connection_id}/applicationstatus/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_applicationstatus(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_status is not None

    # Handle response
    print(res.ats_status)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAtsApplicationstatusRequest](../../models/operations/getatsapplicationstatusrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAtsApplicationstatusResponse](../../models/operations/getatsapplicationstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_candidate

Retrieve a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsCandidate" method="get" path="/ats/{connection_id}/candidate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_candidate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsCandidateRequest](../../models/operations/getatscandidaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAtsCandidateResponse](../../models/operations/getatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsCompany" method="get" path="/ats/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAtsCompanyRequest](../../models/operations/getatscompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetAtsCompanyResponse](../../models/operations/getatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_document

Retrieve a document

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsDocument" method="get" path="/ats/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAtsDocumentRequest](../../models/operations/getatsdocumentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetAtsDocumentResponse](../../models/operations/getatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ats_interview

Retrieve an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsInterview" method="get" path="/ats/{connection_id}/interview/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_interview(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsInterviewRequest](../../models/operations/getatsinterviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAtsInterviewResponse](../../models/operations/getatsinterviewresponse.md)**

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

    res = unified_to.ats.get_ats_job(request={
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

## get_ats_scorecard

Retrieve a scorecard

### Example Usage

<!-- UsageSnippet language="python" operationID="getAtsScorecard" method="get" path="/ats/{connection_id}/scorecard/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.get_ats_scorecard(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_scorecard is not None

    # Handle response
    print(res.ats_scorecard)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetAtsScorecardRequest](../../models/operations/getatsscorecardrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetAtsScorecardResponse](../../models/operations/getatsscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_activities

List all activities

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsActivities" method="get" path="/ats/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_activities(request={
        "connection_id": "<id>",
    })

    assert res.ats_activities is not None

    # Handle response
    print(res.ats_activities)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsActivitiesRequest](../../models/operations/listatsactivitiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsActivitiesResponse](../../models/operations/listatsactivitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_applications

List all applications

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsApplications" method="get" path="/ats/{connection_id}/application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_applications(request={
        "connection_id": "<id>",
    })

    assert res.ats_applications is not None

    # Handle response
    print(res.ats_applications)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAtsApplicationsRequest](../../models/operations/listatsapplicationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAtsApplicationsResponse](../../models/operations/listatsapplicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_applicationstatuses

List all applicationstatuses

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsApplicationstatuses" method="get" path="/ats/{connection_id}/applicationstatus" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_applicationstatuses(request={
        "connection_id": "<id>",
    })

    assert res.ats_statuses is not None

    # Handle response
    print(res.ats_statuses)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAtsApplicationstatusesRequest](../../models/operations/listatsapplicationstatusesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAtsApplicationstatusesResponse](../../models/operations/listatsapplicationstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_candidates

List all candidates

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsCandidates" method="get" path="/ats/{connection_id}/candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_candidates(request={
        "connection_id": "<id>",
    })

    assert res.ats_candidates is not None

    # Handle response
    print(res.ats_candidates)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsCandidatesRequest](../../models/operations/listatscandidatesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsCandidatesResponse](../../models/operations/listatscandidatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsCompanies" method="get" path="/ats/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_companies(request={
        "connection_id": "<id>",
    })

    assert res.ats_companies is not None

    # Handle response
    print(res.ats_companies)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAtsCompaniesRequest](../../models/operations/listatscompaniesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAtsCompaniesResponse](../../models/operations/listatscompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_documents

List all documents

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsDocuments" method="get" path="/ats/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_documents(request={
        "connection_id": "<id>",
    })

    assert res.ats_documents is not None

    # Handle response
    print(res.ats_documents)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAtsDocumentsRequest](../../models/operations/listatsdocumentsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListAtsDocumentsResponse](../../models/operations/listatsdocumentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ats_interviews

List all interviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsInterviews" method="get" path="/ats/{connection_id}/interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_interviews(request={
        "connection_id": "<id>",
    })

    assert res.ats_interviews is not None

    # Handle response
    print(res.ats_interviews)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsInterviewsRequest](../../models/operations/listatsinterviewsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsInterviewsResponse](../../models/operations/listatsinterviewsresponse.md)**

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

    res = unified_to.ats.list_ats_jobs(request={
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

## list_ats_scorecards

List all scorecards

### Example Usage

<!-- UsageSnippet language="python" operationID="listAtsScorecards" method="get" path="/ats/{connection_id}/scorecard" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.list_ats_scorecards(request={
        "connection_id": "<id>",
    })

    assert res.ats_scorecards is not None

    # Handle response
    print(res.ats_scorecards)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAtsScorecardsRequest](../../models/operations/listatsscorecardsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListAtsScorecardsResponse](../../models/operations/listatsscorecardsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsActivity" method="patch" path="/ats/{connection_id}/activity/{id}" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_activity(request={
        "ats_activity": {
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Sapiente.",
            "id": "63e5469f-6bde-4fc0-aa25-9df6dd1ed565",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "91cf4e1f-d934-4511-9c1e-930e4e9d1404",
                    "namespace": "activity",
                    "slug": "cimentarius",
                    "value": "Reprehenderit verto.",
                },
            ],
            "sub_type": "TASK",
            "title": "Venio blandior aureus.",
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-04-04T06:33:50.681Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAtsActivityRequest](../../models/operations/patchatsactivityrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAtsActivityResponse](../../models/operations/patchatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_application

Update an application

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsApplication" method="patch" path="/ats/{connection_id}/application/{id}" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-29T18:38:27.368Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-12T18:26:15.830Z"),
            "id": "e191ba0a-9c3b-4d82-ab5b-223b65befa0a",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "e488328a-175e-4b51-952f-7f0e4f54e681",
                    "namespace": "application",
                    "slug": "stella",
                    "value": "Caput.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-11T13:02:04.118Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Arguo repudiandae defessus. Adflicto caecus claustrum annus addo vere crebro. Alias sponte turbo sopor vergo surculus nam.",
            "updated_at": parse_datetime("2026-10-18T09:16:18.549Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchAtsApplicationRequest](../../models/operations/patchatsapplicationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchAtsApplicationResponse](../../models/operations/patchatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_candidate

Update a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsCandidate" method="patch" path="/ats/{connection_id}/candidate/{id}" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "f8c3986e-ed87-4952-b5af-9ee7d02a0118",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "0985bb29-678c-4e1f-a509-dc7855ae8d34",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-28T17:46:38.414Z"),
            "web_url": "https://fragrant-husband.net/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsCandidateRequest](../../models/operations/patchatscandidaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAtsCandidateResponse](../../models/operations/patchatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsCompany" method="patch" path="/ats/{connection_id}/company/{id}" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "ddb9cba7-1919-4a13-b0ba-b3bd702d1efd",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-882-360-2010",
            "updated_at": parse_datetime("2020-10-01T04:11:25.070Z"),
            "website_url": "https://www.gulgowskidibbert.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchAtsCompanyRequest](../../models/operations/patchatscompanyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchAtsCompanyResponse](../../models/operations/patchatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsDocument" method="patch" path="/ats/{connection_id}/document/{id}" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "bb7df27b-3a46-431f-a4d7-5f8398e0e9a6",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-07T04:58:38.774Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchAtsDocumentRequest](../../models/operations/patchatsdocumentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchAtsDocumentResponse](../../models/operations/patchatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ats_interview

Update an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsInterview" method="patch" path="/ats/{connection_id}/interview/{id}" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2021-12-08T06:33:19.583Z"),
            "id": "ea829ecb-45a9-4a25-b7c9-dbb578bd83bb",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "metadata": [],
            "start_at": parse_datetime("2021-12-08T06:03:19.583Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2023-09-23T16:37:18.644Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsInterviewRequest](../../models/operations/patchatsinterviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAtsInterviewResponse](../../models/operations/patchatsinterviewresponse.md)**

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

    res = unified_to.ats.patch_ats_job(request={
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
            "id": "5d34a61a-1e4a-4ab6-b66c-1be6e5d9b7fc",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "32cda706-335c-49ef-a6b0-14f6a1c0bd7c",
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
                    "opened_at": parse_datetime("2026-06-07T21:23:37.323Z"),
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
                    "created_at": parse_datetime("2026-08-02T00:24:41.925Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "f1ba3e64-d9ba-41f2-925b-88b51d905251",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-08-28T07:47:34.897Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "c1bf2bc5-f39c-4807-97d5-9099eae0ece1",
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
                    "id": "15c8ed80-3a14-407c-b4ab-3c5701c80ee9",
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
                    "id": "4d682ebe-2e5b-4be3-b67a-b9658a10394a",
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
            "updated_at": parse_datetime("2026-02-27T09:43:12.562Z"),
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

## patch_ats_scorecard

Update a scorecard

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAtsScorecard" method="patch" path="/ats/{connection_id}/scorecard/{id}" example="ats_scorecard" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.patch_ats_scorecard(request={
        "ats_scorecard": {
            "comment": "Maiores enim.",
            "created_at": parse_datetime("2022-02-20T17:09:45.498Z"),
            "id": "8599f5f7-5ae9-4b70-829f-e8272e18818d",
            "metadata": [],
            "questions": [
                {
                    "description": "Sulum textor eveniet facere vita.",
                    "text": "Aliquam.",
                },
                {
                    "answer": "Decretum.",
                    "description": "Conatus cicuta doloremque statua bonus.",
                    "text": "Pecto vulpes libero vomer comburo.",
                },
            ],
            "recommendation": shared.Recommendation.STRONG_YES,
            "updated_at": parse_datetime("2023-06-05T13:38:40.492Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_scorecard is not None

    # Handle response
    print(res.ats_scorecard)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchAtsScorecardRequest](../../models/operations/patchatsscorecardrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchAtsScorecardResponse](../../models/operations/patchatsscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_activity

Remove an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsActivity" method="delete" path="/ats/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveAtsActivityRequest](../../models/operations/removeatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAtsActivityResponse](../../models/operations/removeatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_application

Remove an application

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsApplication" method="delete" path="/ats/{connection_id}/application/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_application(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveAtsApplicationRequest](../../models/operations/removeatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveAtsApplicationResponse](../../models/operations/removeatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_candidate

Remove a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsCandidate" method="delete" path="/ats/{connection_id}/candidate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_candidate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsCandidateRequest](../../models/operations/removeatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAtsCandidateResponse](../../models/operations/removeatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsCompany" method="delete" path="/ats/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveAtsCompanyRequest](../../models/operations/removeatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveAtsCompanyResponse](../../models/operations/removeatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_document

Remove a document

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsDocument" method="delete" path="/ats/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveAtsDocumentRequest](../../models/operations/removeatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveAtsDocumentResponse](../../models/operations/removeatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ats_interview

Remove an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsInterview" method="delete" path="/ats/{connection_id}/interview/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_interview(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsInterviewRequest](../../models/operations/removeatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAtsInterviewResponse](../../models/operations/removeatsinterviewresponse.md)**

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

    res = unified_to.ats.remove_ats_job(request={
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

## remove_ats_scorecard

Remove a scorecard

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAtsScorecard" method="delete" path="/ats/{connection_id}/scorecard/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.remove_ats_scorecard(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveAtsScorecardRequest](../../models/operations/removeatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveAtsScorecardResponse](../../models/operations/removeatsscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_activity

Update an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsActivity" method="put" path="/ats/{connection_id}/activity/{id}" example="ats_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_activity(request={
        "ats_activity": {
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Sapiente.",
            "id": "63e5469f-6bde-4fc0-aa25-9df6dd1ed565",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "91cf4e1f-d934-4511-9c1e-930e4e9d1404",
                    "namespace": "activity",
                    "slug": "cimentarius",
                    "value": "Reprehenderit verto.",
                },
            ],
            "sub_type": "TASK",
            "title": "Venio blandior aureus.",
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-04-04T06:33:50.681Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_activity is not None

    # Handle response
    print(res.ats_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAtsActivityRequest](../../models/operations/updateatsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAtsActivityResponse](../../models/operations/updateatsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_application

Update an application

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsApplication" method="put" path="/ats/{connection_id}/application/{id}" example="ats_application" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_application(request={
        "ats_application": {
            "answers": [],
            "applied_at": parse_datetime("2025-09-29T18:38:27.368Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-12T18:26:15.830Z"),
            "id": "e191ba0a-9c3b-4d82-ab5b-223b65befa0a",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "e488328a-175e-4b51-952f-7f0e4f54e681",
                    "namespace": "application",
                    "slug": "stella",
                    "value": "Caput.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-11T13:02:04.118Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Arguo repudiandae defessus. Adflicto caecus claustrum annus addo vere crebro. Alias sponte turbo sopor vergo surculus nam.",
            "updated_at": parse_datetime("2026-10-18T09:16:18.549Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_application is not None

    # Handle response
    print(res.ats_application)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateAtsApplicationRequest](../../models/operations/updateatsapplicationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateAtsApplicationResponse](../../models/operations/updateatsapplicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_candidate

Update a candidate

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsCandidate" method="put" path="/ats/{connection_id}/candidate/{id}" example="ats_candidate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_candidate(request={
        "ats_candidate": {
            "address": {
                "address1": "6790 S 1st Street",
                "city": "Ferrystad",
                "country_code": "US",
                "postal_code": "91605",
                "region": "Idaho",
                "region_code": "HI",
            },
            "company_name": "Lehner and Sons",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "date_of_birth": parse_datetime("1994-07-05T19:48:57.631Z"),
            "education": [
                {
                    "degree": "emphasize tricky",
                    "end_at": parse_datetime("1978-04-14T07:58:36.326Z"),
                    "field_of_study": "curtus",
                    "institution": "Abbott - Batz",
                    "level": "phd",
                    "start_at": parse_datetime("1994-06-09T13:31:39.059Z"),
                },
                {
                    "degree": "blah cappelletti",
                    "end_at": parse_datetime("1989-09-06T03:32:39.901Z"),
                    "field_of_study": "crustulum",
                    "institution": "Herman, Franey and Lebsack",
                    "level": "highschool",
                    "start_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                },
            ],
            "emails": [
                {
                    "email": "ardith.beatty@outlook.com",
                    "name": "Ardith Beatty",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "experiences": [
                {
                    "company_name": "Kutch, Lind and Marks",
                    "end_at": parse_datetime("1974-03-01T17:02:58.824Z"),
                    "start_at": parse_datetime("1999-09-21T22:12:51.663Z"),
                    "title": "Lead Security Technician",
                },
                {
                    "company_name": "Trantow, Sipes and Witting",
                    "end_at": parse_datetime("2004-10-14T14:01:00.717Z"),
                    "start_at": parse_datetime("1996-12-15T04:12:04.582Z"),
                    "title": "Regional Applications Planner",
                },
            ],
            "first_name": "Ardith",
            "id": "f8c3986e-ed87-4952-b5af-9ee7d02a0118",
            "image_url": "https://avatars.githubusercontent.com/u/27464445",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://www.linkedin.com/in/ardith-beatty",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "0985bb29-678c-4e1f-a509-dc7855ae8d34",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "officia",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.AGENCY,
            "skills": [
                "trepide",
                "voveo",
            ],
            "sources": [
                "vesper",
                "utroque",
            ],
            "summary": "Laborum trado carcer delibero patruus totam. Vita cohors cariosus trans denego barba rerum similique. Templum totam suus voluptatem cui depraedor virgo cui comminor commodi.",
            "tags": [
                "voro",
            ],
            "telephones": [
                {
                    "telephone": "(837) 251-3896",
                    "type": shared.AtsTelephoneType.MOBILE,
                },
            ],
            "title": "Customer Division Producer",
            "updated_at": parse_datetime("2024-04-28T17:46:38.414Z"),
            "web_url": "https://fragrant-husband.net/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_candidate is not None

    # Handle response
    print(res.ats_candidate)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsCandidateRequest](../../models/operations/updateatscandidaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAtsCandidateResponse](../../models/operations/updateatscandidateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsCompany" method="put" path="/ats/{connection_id}/company/{id}" example="ats_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_company(request={
        "ats_company": {
            "created_at": parse_datetime("2019-04-22T03:50:02.920Z"),
            "id": "ddb9cba7-1919-4a13-b0ba-b3bd702d1efd",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-882-360-2010",
            "updated_at": parse_datetime("2020-10-01T04:11:25.070Z"),
            "website_url": "https://www.gulgowskidibbert.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_company is not None

    # Handle response
    print(res.ats_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateAtsCompanyRequest](../../models/operations/updateatscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateAtsCompanyResponse](../../models/operations/updateatscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsDocument" method="put" path="/ats/{connection_id}/document/{id}" example="ats_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_document(request={
        "ats_document": {
            "created_at": parse_datetime("2021-08-20T08:00:27.437Z"),
            "document_url": "https://vengeful-lashes.biz",
            "filename": "lonzo_schowalter_resume.pdf",
            "id": "bb7df27b-3a46-431f-a4d7-5f8398e0e9a6",
            "metadata": [],
            "type": shared.AtsDocumentType.COVER_LETTER,
            "updated_at": parse_datetime("2022-12-07T04:58:38.774Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_document is not None

    # Handle response
    print(res.ats_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAtsDocumentRequest](../../models/operations/updateatsdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateAtsDocumentResponse](../../models/operations/updateatsdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ats_interview

Update an interview

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsInterview" method="put" path="/ats/{connection_id}/interview/{id}" example="ats_interview" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_interview(request={
        "ats_interview": {
            "created_at": parse_datetime("2021-11-28T03:14:47.774Z"),
            "end_at": parse_datetime("2021-12-08T06:33:19.583Z"),
            "id": "ea829ecb-45a9-4a25-b7c9-dbb578bd83bb",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "metadata": [],
            "start_at": parse_datetime("2021-12-08T06:03:19.583Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2023-09-23T16:37:18.644Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_interview is not None

    # Handle response
    print(res.ats_interview)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsInterviewRequest](../../models/operations/updateatsinterviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAtsInterviewResponse](../../models/operations/updateatsinterviewresponse.md)**

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

    res = unified_to.ats.update_ats_job(request={
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
            "id": "5d34a61a-1e4a-4ab6-b66c-1be6e5d9b7fc",
            "industry": "Handcrafted Bamboo Soap",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "32cda706-335c-49ef-a6b0-14f6a1c0bd7c",
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
                    "opened_at": parse_datetime("2026-06-07T21:23:37.323Z"),
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
                    "created_at": parse_datetime("2026-08-02T00:24:41.925Z"),
                    "description": "Beatus eum volutabrum balbus victus ipsa tubineus claustrum.",
                    "id": "f1ba3e64-d9ba-41f2-925b-88b51d905251",
                    "is_active": False,
                    "location": "1725 Hessel Keys",
                    "name": "International Identity Manager",
                    "posting_url": "https://obedient-yak.com",
                    "updated_at": parse_datetime("2026-08-28T07:47:34.897Z"),
                },
            ],
            "public_job_urls": [
                "https://trustworthy-elver.info",
                "https://parched-dash.info",
            ],
            "questions": [
                {
                    "description": "Auctus deporto tolero administratio capitulus animi agnosco tendo aetas vado.",
                    "id": "c1bf2bc5-f39c-4807-97d5-9099eae0ece1",
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
                    "id": "15c8ed80-3a14-407c-b4ab-3c5701c80ee9",
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
                    "id": "4d682ebe-2e5b-4be3-b67a-b9658a10394a",
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
            "updated_at": parse_datetime("2026-02-27T09:43:12.562Z"),
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

## update_ats_scorecard

Update a scorecard

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAtsScorecard" method="put" path="/ats/{connection_id}/scorecard/{id}" example="ats_scorecard" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.ats.update_ats_scorecard(request={
        "ats_scorecard": {
            "comment": "Maiores enim.",
            "created_at": parse_datetime("2022-02-20T17:09:45.498Z"),
            "id": "8599f5f7-5ae9-4b70-829f-e8272e18818d",
            "metadata": [],
            "questions": [
                {
                    "description": "Sulum textor eveniet facere vita.",
                    "text": "Aliquam.",
                },
                {
                    "answer": "Decretum.",
                    "description": "Conatus cicuta doloremque statua bonus.",
                    "text": "Pecto vulpes libero vomer comburo.",
                },
            ],
            "recommendation": shared.Recommendation.STRONG_YES,
            "updated_at": parse_datetime("2023-06-05T13:38:40.492Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ats_scorecard is not None

    # Handle response
    print(res.ats_scorecard)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAtsScorecardRequest](../../models/operations/updateatsscorecardrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateAtsScorecardResponse](../../models/operations/updateatsscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |