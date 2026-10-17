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
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "03478f03-48a4-4e39-892d-7819e702313c",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "32b08999-1e53-46e1-ae7d-0a68ac6f121b",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "7fead78a-c047-4ec6-a5d9-220ca94041cb",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-31T19:07:11.007Z"),
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
            "applied_at": parse_datetime("2025-09-27T04:24:36.619Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-09T08:34:57.498Z"),
            "id": "5dac2114-8a33-4c6e-afb2-b14a6e9ff6db",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-07T13:56:28.315Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-10-14T09:34:53.967Z"),
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
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "d1af0c70-5cd7-4774-87d1-e3d8c4bc7183",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "1d0ee449-eb20-410f-9fa4-ec4c61864cea",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-28T00:44:29.938Z"),
            "web_url": "https://expert-lender.name/",
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
            "id": "ca6dca0e-8079-479b-bbf3-852331c92cac",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-30T09:41:55.064Z"),
            "website_url": "https://somber-substitution.com/",
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
            "filename": "bah_white_frantically.bz",
            "id": "60033518-6cc4-486b-aabd-2f5aa51b06a8",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-12-06T04:53:55.019Z"),
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
            "end_at": parse_datetime("2025-10-16T09:42:53.940Z"),
            "external_event_xref": "b8c2a062-c3f0-4414-a751-d2aa1e738aa8",
            "id": "ff58343f-8013-4281-a060-36f5db377167",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "start_at": parse_datetime("2025-06-09T05:26:32.529Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-03-01T07:03:48.801Z"),
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
            "hiring_managers": [
                {
                    "id": "eb3bbf4e-4022-4122-9d44-39fd5b501e80",
                    "name": "Troy Greenholt",
                },
            ],
            "id": "4bc2c45f-82e6-47b6-8db8-8e94b3838c03",
            "industry": "Modern Granite Gloves",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "c85aa38f-1e59-4fcb-9efb-069a60e40c90",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vomica",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-06-04T08:04:36.256Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "51372 Kshlerin Creek",
                        "city": "Logancester",
                        "country_code": "US",
                        "postal_code": "85013-9865",
                        "region": "Vermont",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-29T06:46:09.702Z"),
                    "description": "Provident turbo cunabula spoliatio agnitio.",
                    "id": "372178cd-2056-4388-870e-e7c199761c7c",
                    "is_active": False,
                    "location": "2925 Connie Green",
                    "name": "Lead Intranet Developer",
                    "posting_url": "https://smart-summer.name/",
                    "updated_at": parse_datetime("2026-08-24T12:05:11.681Z"),
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
                    "max_length": 387.0,
                    "min_length": 1.0,
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
                    "id": "3a0b53b3-8f3e-48d4-ab9f-413a900d79b0",
                    "max_length": 430.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                    ],
                    "prompt": "Contra damno desolo suadeo utrimque cresco.",
                    "question": "Sodalitas desino sollers viduo volo cresco ventus tui sufficio iusto.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "id": "060ed8c8-ab8a-417c-8b25-edf38cb19b1c",
                    "max_length": 381.0,
                    "min_length": 1.0,
                    "options": [
                        "utroque",
                    ],
                    "prompt": "Vir crepusculum ait adeptio ait defendo cotidie porro uterque.",
                    "question": "Vulticulus depono abstergo possimus quibusdam deinde amoveo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "coaegresco",
                "appello",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Iste sto communis.",
            "updated_at": parse_datetime("2026-02-24T04:17:15.496Z"),
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
            "id": "957bb331-adff-43d8-9a5e-425d9da865b5",
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
            "updated_at": parse_datetime("2023-06-04T11:11:08.097Z"),
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
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "a8d16699-0c0a-4526-b1da-fea24ff3b08c",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "50b29d33-7a29-489e-82a5-89d90f197732",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "c515839c-324d-4207-92b3-d93f176476c6",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-31T19:07:11.021Z"),
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
            "applied_at": parse_datetime("2025-09-27T04:24:36.631Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-09T08:34:57.514Z"),
            "id": "a899a31b-70d2-4c9a-a31c-bdb5b467ee5c",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-07T13:56:28.334Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-10-14T09:34:53.986Z"),
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
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "fe2843b9-7136-4f64-91fc-a75eeb242f59",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "ad88991d-847d-4dd8-8d2d-9b67e57a9e42",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-28T00:44:29.942Z"),
            "web_url": "https://expert-lender.name/",
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
            "id": "6ea1dc06-0277-44ec-82bf-bd2bbae33563",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-30T09:41:55.066Z"),
            "website_url": "https://somber-substitution.com/",
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
            "filename": "bah_white_frantically.bz",
            "id": "d21300af-a277-406d-866b-b6cb706d9541",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-12-06T04:53:55.020Z"),
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
            "end_at": parse_datetime("2025-10-16T09:42:53.945Z"),
            "external_event_xref": "4a48b657-505b-450d-99e2-508b5e577773",
            "id": "7224c4eb-91c4-43d1-85e1-4c0789c8022f",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "start_at": parse_datetime("2025-06-09T05:26:32.533Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-03-01T07:03:48.806Z"),
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
            "hiring_managers": [
                {
                    "id": "eb3bbf4e-4022-4122-9d44-39fd5b501e80",
                    "name": "Troy Greenholt",
                },
            ],
            "id": "bd1a4114-3ed6-44d8-8e4e-b7598ae49b4a",
            "industry": "Modern Granite Gloves",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "1499b5d0-da4f-4fa8-97ce-4a6108a6bda1",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vomica",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-06-04T08:04:36.287Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "51372 Kshlerin Creek",
                        "city": "Logancester",
                        "country_code": "US",
                        "postal_code": "85013-9865",
                        "region": "Vermont",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-29T06:46:09.734Z"),
                    "description": "Provident turbo cunabula spoliatio agnitio.",
                    "id": "372178cd-2056-4388-870e-e7c199761c7c",
                    "is_active": False,
                    "location": "2925 Connie Green",
                    "name": "Lead Intranet Developer",
                    "posting_url": "https://smart-summer.name/",
                    "updated_at": parse_datetime("2026-08-24T12:05:11.714Z"),
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
                    "max_length": 387.0,
                    "min_length": 1.0,
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
                    "id": "3a0b53b3-8f3e-48d4-ab9f-413a900d79b0",
                    "max_length": 430.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                    ],
                    "prompt": "Contra damno desolo suadeo utrimque cresco.",
                    "question": "Sodalitas desino sollers viduo volo cresco ventus tui sufficio iusto.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "id": "060ed8c8-ab8a-417c-8b25-edf38cb19b1c",
                    "max_length": 381.0,
                    "min_length": 1.0,
                    "options": [
                        "utroque",
                    ],
                    "prompt": "Vir crepusculum ait adeptio ait defendo cotidie porro uterque.",
                    "question": "Vulticulus depono abstergo possimus quibusdam deinde amoveo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "coaegresco",
                "appello",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Iste sto communis.",
            "updated_at": parse_datetime("2026-02-24T04:17:15.525Z"),
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
            "id": "fdc8b15e-c668-465d-ac47-673539aafa33",
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
            "updated_at": parse_datetime("2023-06-04T11:11:08.099Z"),
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
            "bcc": [
                {
                    "email": "Mabel_Schuppe-Schowalter42@hotmail.com",
                    "name": "Rochelle Franey-Bechtelar",
                    "type": shared.AtsEmailType.HOME,
                },
            ],
            "cc": [
                {
                    "email": "Sasha24@hotmail.com",
                    "name": "Dr. Elbert Kuvalis",
                    "type": shared.AtsEmailType.HOME,
                },
                {
                    "email": "Rosetta_Donnelly@gmail.com",
                    "name": "Ramon Daniel",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Kathryne_Jast@yahoo.com",
                    "name": "Christian Jacobson",
                    "type": shared.AtsEmailType.OTHER,
                },
                {
                    "email": "Eldred95@yahoo.com",
                    "name": "Edna Bogan",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "created_at": parse_datetime("2022-08-07T03:16:43.865Z"),
            "description": "Amplus.",
            "from_": {
                "email": "Norwood.Wiza47@yahoo.com",
                "name": "Toby Grant",
                "type": shared.PropertyAtsActivityFromType.OTHER,
            },
            "id": "a8d16699-0c0a-4526-b1da-fea24ff3b08c",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "50b29d33-7a29-489e-82a5-89d90f197732",
                    "namespace": "activity",
                    "slug": "acer",
                    "value": "Pauci eius cena adamo summisse arguo pectus communis arcesso tergeo.",
                },
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "c515839c-324d-4207-92b3-d93f176476c6",
                    "namespace": "activity",
                    "slug": "tremo",
                    "value": "Amita delectus dicta temptatio utroque ex.",
                },
            ],
            "sub_type": "TASK",
            "title": "Senior Interactions Manager",
            "to": [
                {
                    "email": "Sister91@hotmail.com",
                    "name": "Eddie Nienow PhD",
                    "type": shared.AtsEmailType.WORK,
                },
            ],
            "type": shared.AtsActivityType.TASK,
            "updated_at": parse_datetime("2026-03-31T19:07:11.021Z"),
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
            "applied_at": parse_datetime("2025-09-27T04:24:36.631Z"),
            "created_at": parse_datetime("2023-10-17T07:19:48.787Z"),
            "hired_at": parse_datetime("2026-05-09T08:34:57.514Z"),
            "id": "a899a31b-70d2-4c9a-a31c-bdb5b467ee5c",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "a1302a79-0341-40e6-b91a-daeb95584617",
                    "namespace": "application",
                    "slug": "despecto",
                    "value": "Argentum decretum cultellus aveho distinctio verecundia stella depono.",
                },
            ],
            "offers": [],
            "original_status": "vomica",
            "original_substatus": "allatus",
            "rejected_at": parse_datetime("2026-10-07T13:56:28.334Z"),
            "rejected_reason": "Cometes amplitudo videlicet talio.",
            "source": "credo",
            "status": shared.AtsApplicationStatus.REVIEWING,
            "summary": "Comburo quidem vesica vulnus curatio. Appositus amita attonbitus conatus degenero charisma sordeo villa victoria varius. Cenaculum acsi officia.",
            "updated_at": parse_datetime("2026-10-14T09:34:53.986Z"),
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
                "address1": "802 Roberts Squares",
                "address2": "Suite 550",
                "city": "Lake Raeganside",
                "country_code": "US",
                "postal_code": "44530-0054",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "company_name": "Ferry, Legros and Feest",
            "created_at": parse_datetime("2023-10-16T05:42:56.049Z"),
            "education": [
                {
                    "degree": "mouser throughout",
                    "end_at": parse_datetime("1992-11-28T20:23:20.311Z"),
                    "field_of_study": "solutio",
                    "institution": "Heller - Lubowitz",
                    "level": "phd",
                    "start_at": parse_datetime("2001-03-26T08:12:11.510Z"),
                },
            ],
            "emails": [
                {
                    "email": "Ardith.Beatty@hotmail.com",
                    "name": "Opal Lindgren",
                    "type": shared.AtsEmailType.WORK,
                },
                {
                    "email": "Ardith_Beatty@gmail.com",
                    "name": "Kristi Nader",
                    "type": shared.AtsEmailType.OTHER,
                },
            ],
            "experiences": [
                {
                    "company_name": "Donnelly, Buckridge and Steuber",
                    "end_at": parse_datetime("1978-06-20T02:53:48.383Z"),
                    "start_at": parse_datetime("1980-02-06T17:16:53.798Z"),
                    "title": "Principal Brand Strategist",
                },
            ],
            "first_name": "Ardith",
            "id": "fe2843b9-7136-4f64-91fc-a75eeb242f59",
            "image_url": "https://loremflickr.com/40/3693?lock=5634712403880328",
            "job_ids": [],
            "last_name": "Beatty",
            "link_urls": [
                "https://sizzling-legislature.com",
                "https://soupy-interchange.net",
                "https://troubled-substitution.info",
            ],
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "ad88991d-847d-4dd8-8d2d-9b67e57a9e42",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "cariosus",
                },
            ],
            "name": "Ardith Beatty",
            "origin": shared.Origin.SOURCED,
            "skills": [
                "vita",
                "cohors",
            ],
            "sources": [
                "tactus",
            ],
            "summary": "Denego barba rerum similique via templum totam suus voluptatem. Depraedor virgo cui comminor commodi curvo. Chirographum pax spero nostrum damnatio averto pecus cervus aspicio absens.",
            "tags": [
                "aliquid",
            ],
            "telephones": [
                {
                    "telephone": "(779) 296-5994",
                    "type": shared.AtsTelephoneType.HOME,
                },
            ],
            "title": "Principal Implementation Analyst",
            "updated_at": parse_datetime("2024-04-28T00:44:29.942Z"),
            "web_url": "https://expert-lender.name/",
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
            "id": "6ea1dc06-0277-44ec-82bf-bd2bbae33563",
            "name": "Gulgowski, Dibbert and Wilderman",
            "phone": "1-602-210-4548",
            "updated_at": parse_datetime("2020-09-30T09:41:55.066Z"),
            "website_url": "https://somber-substitution.com/",
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
            "filename": "bah_white_frantically.bz",
            "id": "d21300af-a277-406d-866b-b6cb706d9541",
            "type": shared.AtsDocumentType.RESUME,
            "updated_at": parse_datetime("2022-12-06T04:53:55.020Z"),
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
            "end_at": parse_datetime("2025-10-16T09:42:53.945Z"),
            "external_event_xref": "4a48b657-505b-450d-99e2-508b5e577773",
            "id": "7224c4eb-91c4-43d1-85e1-4c0789c8022f",
            "location": "26596 Halle Trafficway",
            "meeting_url": "https://immaculate-foodstuffs.biz",
            "start_at": parse_datetime("2025-06-09T05:26:32.533Z"),
            "status": shared.AtsInterviewStatus.SCHEDULED,
            "updated_at": parse_datetime("2026-03-01T07:03:48.806Z"),
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
            "hiring_managers": [
                {
                    "id": "eb3bbf4e-4022-4122-9d44-39fd5b501e80",
                    "name": "Troy Greenholt",
                },
            ],
            "id": "bd1a4114-3ed6-44d8-8e4e-b7598ae49b4a",
            "industry": "Modern Granite Gloves",
            "language_locale": "en",
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.AtsMetadataFormat.TEXT,
                    "id": "1499b5d0-da4f-4fa8-97ce-4a6108a6bda1",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "vomica",
                },
            ],
            "minimum_degree": "Bachelor",
            "minimum_experience_years": 3.0,
            "name": "Forward Brand Producer",
            "number_of_openings": 1.0,
            "openings": [
                {
                    "close_reason": "Admoveo trado textilis.",
                    "opened_at": parse_datetime("2026-06-04T08:04:36.287Z"),
                    "status": shared.AtsJobOpeningStatus.OPEN,
                },
            ],
            "postings": [
                {
                    "address": {
                        "address1": "51372 Kshlerin Creek",
                        "city": "Logancester",
                        "country_code": "US",
                        "postal_code": "85013-9865",
                        "region": "Vermont",
                        "region_code": "MO",
                    },
                    "created_at": parse_datetime("2026-07-29T06:46:09.734Z"),
                    "description": "Provident turbo cunabula spoliatio agnitio.",
                    "id": "372178cd-2056-4388-870e-e7c199761c7c",
                    "is_active": False,
                    "location": "2925 Connie Green",
                    "name": "Lead Intranet Developer",
                    "posting_url": "https://smart-summer.name/",
                    "updated_at": parse_datetime("2026-08-24T12:05:11.714Z"),
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
                    "max_length": 387.0,
                    "min_length": 1.0,
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
                    "id": "3a0b53b3-8f3e-48d4-ab9f-413a900d79b0",
                    "max_length": 430.0,
                    "min_length": 1.0,
                    "options": [
                        "aetas",
                    ],
                    "prompt": "Contra damno desolo suadeo utrimque cresco.",
                    "question": "Sodalitas desino sollers viduo volo cresco ventus tui sufficio iusto.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
                {
                    "description": "Ara thermae aetas vivo constans victoria volo carbo vehemens praesentium.",
                    "id": "060ed8c8-ab8a-417c-8b25-edf38cb19b1c",
                    "max_length": 381.0,
                    "min_length": 1.0,
                    "options": [
                        "utroque",
                    ],
                    "prompt": "Vir crepusculum ait adeptio ait defendo cotidie porro uterque.",
                    "question": "Vulticulus depono abstergo possimus quibusdam deinde amoveo.",
                    "required": False,
                    "type": shared.AtsJobQuestionType.TEXT,
                },
            ],
            "skills": [
                "coaegresco",
                "appello",
            ],
            "status": shared.AtsJobStatus.ARCHIVED,
            "summary": "Iste sto communis.",
            "updated_at": parse_datetime("2026-02-24T04:17:15.525Z"),
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
            "id": "fdc8b15e-c668-465d-ac47-673539aafa33",
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
            "updated_at": parse_datetime("2023-06-04T11:11:08.099Z"),
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