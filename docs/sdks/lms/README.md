# Lms

## Overview

### Available Operations

* [create_lms_activity](#create_lms_activity) - Create an activity
* [create_lms_class](#create_lms_class) - Create a class
* [create_lms_collection](#create_lms_collection) - Create a collection
* [create_lms_content](#create_lms_content) - Create a content
* [create_lms_course](#create_lms_course) - Create a course
* [create_lms_instructor](#create_lms_instructor) - Create an instructor
* [create_lms_student](#create_lms_student) - Create a student
* [get_lms_activity](#get_lms_activity) - Retrieve an activity
* [get_lms_class](#get_lms_class) - Retrieve a class
* [get_lms_collection](#get_lms_collection) - Retrieve a collection
* [get_lms_content](#get_lms_content) - Retrieve a content
* [get_lms_course](#get_lms_course) - Retrieve a course
* [get_lms_instructor](#get_lms_instructor) - Retrieve an instructor
* [get_lms_student](#get_lms_student) - Retrieve a student
* [list_lms_activities](#list_lms_activities) - List all activities
* [list_lms_classes](#list_lms_classes) - List all classes
* [list_lms_collections](#list_lms_collections) - List all collections
* [list_lms_contents](#list_lms_contents) - List all contents
* [list_lms_courses](#list_lms_courses) - List all courses
* [list_lms_instructors](#list_lms_instructors) - List all instructors
* [list_lms_students](#list_lms_students) - List all students
* [patch_lms_activity](#patch_lms_activity) - Update an activity
* [patch_lms_class](#patch_lms_class) - Update a class
* [patch_lms_collection](#patch_lms_collection) - Update a collection
* [patch_lms_content](#patch_lms_content) - Update a content
* [patch_lms_course](#patch_lms_course) - Update a course
* [patch_lms_instructor](#patch_lms_instructor) - Update an instructor
* [patch_lms_student](#patch_lms_student) - Update a student
* [remove_lms_activity](#remove_lms_activity) - Remove an activity
* [remove_lms_class](#remove_lms_class) - Remove a class
* [remove_lms_collection](#remove_lms_collection) - Remove a collection
* [remove_lms_content](#remove_lms_content) - Remove a content
* [remove_lms_course](#remove_lms_course) - Remove a course
* [remove_lms_instructor](#remove_lms_instructor) - Remove an instructor
* [remove_lms_student](#remove_lms_student) - Remove a student
* [update_lms_activity](#update_lms_activity) - Update an activity
* [update_lms_class](#update_lms_class) - Update a class
* [update_lms_collection](#update_lms_collection) - Update a collection
* [update_lms_content](#update_lms_content) - Update a content
* [update_lms_course](#update_lms_course) - Update a course
* [update_lms_instructor](#update_lms_instructor) - Update an instructor
* [update_lms_student](#update_lms_student) - Update a student

## create_lms_activity

Creates a LmsActivity. Provide the unified LmsActivity fields in the request body; they are mapped to the provider's API. Returns the created LmsActivity.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsActivity" method="post" path="/lms/{connection_id}/activity" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2023-12-17T08:45:27.914Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "ef2de1f9-c74e-4e7b-8303-5815feebc75a",
            "is_completed": True,
            "metadata": [],
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2021-04-27T01:44:21.768Z"),
            "updated_at": parse_datetime("2022-02-04T16:00:41.515Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateLmsActivityRequest](../../models/operations/createlmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateLmsActivityResponse](../../models/operations/createlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_class

Creates a LmsClass. Provide the unified LmsClass fields in the request body; they are mapped to the provider's API. Returns the created LmsClass.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsClass" method="post" path="/lms/{connection_id}/class" example="lms_class" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "e6b2baeb-249d-4d45-a179-86142cad61a7",
            "instructors": [],
            "languages": [
                "in",
            ],
            "media": [
                {
                    "content": "Defetiscor aetas acies benevolentia ulterius. Creta bis beneficium canis. Bonus valeo vulgo creator arca peior ceno earum culpa. Tabesco apostolus talis. Ultra accommodo deinde sono culpo arto cruciamentum triduana.",
                    "description": "Esse confido.",
                    "languages": [
                        "fa",
                        "da",
                    ],
                    "name": "illo",
                    "thumbnail_url": "https://loremflickr.com/199/1934?lock=4323325966476891",
                    "type": shared.LmsMediaType.VIDEO,
                    "url": "https://loremflickr.com/487/921?lock=5127962071241632",
                },
            ],
            "metadata": [],
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-08-21T17:44:33.768Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_class is not None

    # Handle response
    print(res.lms_class)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateLmsClassRequest](../../models/operations/createlmsclassrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateLmsClassResponse](../../models/operations/createlmsclassresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_collection

Creates a LmsCollection. Provide the unified LmsCollection fields in the request body; they are mapped to the provider's API. Returns the created LmsCollection.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsCollection" method="post" path="/lms/{connection_id}/collection" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "1a53096e-5c5b-45cc-a457-ba5cb0709d77",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "metadata": [],
            "name": "ara",
            "updated_at": parse_datetime("2026-08-20T10:04:26.139Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateLmsCollectionRequest](../../models/operations/createlmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateLmsCollectionResponse](../../models/operations/createlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_content

Creates a LmsContent. Provide the unified LmsContent fields in the request body; they are mapped to the provider's API. Returns the created LmsContent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsContent" method="post" path="/lms/{connection_id}/content" example="lms_content" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_content(request={
        "lms_content": {
            "categories": [
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "18252340-2793-4bcf-ba96-6c44a98ac6dd",
            "instructors": [],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Acervus.",
                    "language": "es",
                    "name": "talis",
                },
                {
                    "description": "Ratione.",
                    "language": "es",
                    "name": "sint",
                },
            ],
            "media": [
                {
                    "content": "Adnuo antepono vulticulus incidunt. Commemoro voro ocer arca velut vigor venustas una audeo. Consectetur totidem amor amo vigor. Patior ulciscor cohors necessitatibus beatae. Copiose cedo sub decens acer.",
                    "description": "Venia aeternus tandem spargo.",
                    "languages": [
                        "zu",
                        "ba",
                    ],
                    "name": "subiungo",
                    "thumbnail_url": "https://loremflickr.com/2056/3712?lock=5644845642923518",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://loremflickr.com/2593/1553?lock=8591263400111785",
                },
                {
                    "content": "Terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum. Absque adversus desino aut tabernus tollo vigor. Cur agnitio totidem consuasor bene doloribus. Vetus abundans curriculum curatio usitas.",
                    "description": "Comedo valde caste combibo.",
                    "languages": [
                        "it",
                        "hu",
                    ],
                    "name": "beneficium",
                    "thumbnail_url": "https://picsum.photos/seed/pNFr1/2597/885",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://loremflickr.com/3597/239?lock=7142808124990633",
                },
                {
                    "content": "Coepi demo adversus capillus aro unus templum. Aspicio alius vehemens terminatio varietas vomica. Apud thorax defero decet impedit verbera pauci laboriosam molestiae urbanus. Aveho vergo crux certus nulla caute sophismata. Caute voluptatibus patrocinor demo verumtamen adeo canis sapiente depraedor verus.",
                    "description": "Tunc barba decens.",
                    "languages": [
                        "bn",
                        "yo",
                    ],
                    "name": "qui",
                    "thumbnail_url": "https://loremflickr.com/1375/3377?lock=6601832177607674",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://loremflickr.com/3927/2086?lock=5199784913821481",
                },
            ],
            "metadata": [],
            "name": "ut",
            "provider_name": "Bins LLC",
            "published_at": parse_datetime("2022-09-10T01:00:41.526Z"),
            "short_description": "Caritas.",
            "skills": [
                "trucido",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "tibi",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "dens",
            ],
            "updated_at": parse_datetime("2022-10-11T06:40:48.171Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_content is not None

    # Handle response
    print(res.lms_content)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateLmsContentRequest](../../models/operations/createlmscontentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateLmsContentResponse](../../models/operations/createlmscontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_course

Creates a LmsCourse. Provide the unified LmsCourse fields in the request body; they are mapped to the provider's API. Returns the created LmsCourse.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsCourse" method="post" path="/lms/{connection_id}/course" example="lms_course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "749aea73-03b0-4b6a-b363-e5ad865eb3e2",
            "instructors": [],
            "is_active": True,
            "is_private": False,
            "languages": [
                "desparatus",
                "earum",
                "deripio",
            ],
            "media": [
                {
                    "content": "Adeptio crudelis ipsum utrimque quae architecto. Cum eius conitor anser abutor error adsuesco abeo. Denego nihil caries aveho.",
                    "description": "Adipiscor.",
                    "languages": [
                        "ms",
                        "te",
                    ],
                    "name": "tandem",
                    "thumbnail_url": "https://picsum.photos/seed/syTatRhK03/928/273",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/fQAbsk/2472/1671",
                },
            ],
            "metadata": [],
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2022-11-06T04:57:00.094Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-11T15:09:46.219Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateLmsCourseRequest](../../models/operations/createlmscourserequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateLmsCourseResponse](../../models/operations/createlmscourseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_instructor

Creates a LmsInstructor. Provide the unified LmsInstructor fields in the request body; they are mapped to the provider's API. Returns the created LmsInstructor.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsInstructor" method="post" path="/lms/{connection_id}/instructor" example="lms_instructor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_instructor(request={
        "lms_instructor": {
            "created_at": parse_datetime("2021-10-12T16:38:54.979Z"),
            "emails": [
                {},
            ],
            "first_name": "Deangelo",
            "id": "49d52415-a2a8-435a-967d-e8502308324a",
            "image_url": "https://avatars.githubusercontent.com/u/95131132",
            "last_name": "Ritchie",
            "metadata": [],
            "name": "Deangelo Ritchie",
            "telephones": [
                {
                    "telephone": "(605) 752-8163",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(430) 415-2451",
                    "type": shared.LmsTelephoneType.HOME,
                },
            ],
            "title": "Regional Security Agent",
            "updated_at": parse_datetime("2025-08-09T20:24:03.915Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_instructor is not None

    # Handle response
    print(res.lms_instructor)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateLmsInstructorRequest](../../models/operations/createlmsinstructorrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateLmsInstructorResponse](../../models/operations/createlmsinstructorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_student

Creates a LmsStudent. Provide the unified LmsStudent fields in the request body; they are mapped to the provider's API. Returns the created LmsStudent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsStudent" method="post" path="/lms/{connection_id}/student" example="lms_student" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.create_lms_student(request={
        "lms_student": {
            "address": {
                "address1": "15033 Corwin Circles",
                "city": "New Craigside",
                "country_code": "US",
                "postal_code": "73966",
                "region": "New Jersey",
                "region_code": "TX",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
            ],
            "first_name": "Marcella",
            "id": "b6c4a28d-3772-43bb-84cf-7daeb37124d8",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/56.jpg",
            "last_name": "Murazik",
            "metadata": [],
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(899) 827-6400",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(487) 213-8236",
                    "type": shared.LmsTelephoneType.FAX,
                },
                {
                    "telephone": "(980) 775-2940",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-07-08T12:13:30.447Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_student is not None

    # Handle response
    print(res.lms_student)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateLmsStudentRequest](../../models/operations/createlmsstudentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateLmsStudentResponse](../../models/operations/createlmsstudentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_activity

Retrieves a single LmsActivity by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsActivity" method="get" path="/lms/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_activity(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetLmsActivityRequest](../../models/operations/getlmsactivityrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetLmsActivityResponse](../../models/operations/getlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_class

Retrieves a single LmsClass by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsClass" method="get" path="/lms/{connection_id}/class/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_class(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_class is not None

    # Handle response
    print(res.lms_class)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetLmsClassRequest](../../models/operations/getlmsclassrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetLmsClassResponse](../../models/operations/getlmsclassresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_collection

Retrieves a single LmsCollection by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsCollection" method="get" path="/lms/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetLmsCollectionRequest](../../models/operations/getlmscollectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetLmsCollectionResponse](../../models/operations/getlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_content

Retrieves a single LmsContent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsContent" method="get" path="/lms/{connection_id}/content/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_content(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_content is not None

    # Handle response
    print(res.lms_content)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLmsContentRequest](../../models/operations/getlmscontentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetLmsContentResponse](../../models/operations/getlmscontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_course

Retrieves a single LmsCourse by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsCourse" method="get" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_course(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetLmsCourseRequest](../../models/operations/getlmscourserequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetLmsCourseResponse](../../models/operations/getlmscourseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_instructor

Retrieves a single LmsInstructor by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsInstructor" method="get" path="/lms/{connection_id}/instructor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_instructor(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_instructor is not None

    # Handle response
    print(res.lms_instructor)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetLmsInstructorRequest](../../models/operations/getlmsinstructorrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetLmsInstructorResponse](../../models/operations/getlmsinstructorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_student

Retrieves a single LmsStudent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsStudent" method="get" path="/lms/{connection_id}/student/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.get_lms_student(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_student is not None

    # Handle response
    print(res.lms_student)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLmsStudentRequest](../../models/operations/getlmsstudentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetLmsStudentResponse](../../models/operations/getlmsstudentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_activities

Returns a list of LmsActivities. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsActivities" method="get" path="/lms/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_activities(request={
        "connection_id": "<id>",
    })

    assert res.lms_activities is not None

    # Handle response
    print(res.lms_activities)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListLmsActivitiesRequest](../../models/operations/listlmsactivitiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListLmsActivitiesResponse](../../models/operations/listlmsactivitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_classes

Returns a list of LmsClasses. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsClasses" method="get" path="/lms/{connection_id}/class" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_classes(request={
        "connection_id": "<id>",
    })

    assert res.lms_classes is not None

    # Handle response
    print(res.lms_classes)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListLmsClassesRequest](../../models/operations/listlmsclassesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListLmsClassesResponse](../../models/operations/listlmsclassesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_collections

Returns a list of LmsCollections. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsCollections" method="get" path="/lms/{connection_id}/collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_collections(request={
        "connection_id": "<id>",
    })

    assert res.lms_collections is not None

    # Handle response
    print(res.lms_collections)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListLmsCollectionsRequest](../../models/operations/listlmscollectionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListLmsCollectionsResponse](../../models/operations/listlmscollectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_contents

Returns a list of LmsContents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsContents" method="get" path="/lms/{connection_id}/content" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_contents(request={
        "connection_id": "<id>",
    })

    assert res.lms_contents is not None

    # Handle response
    print(res.lms_contents)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListLmsContentsRequest](../../models/operations/listlmscontentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListLmsContentsResponse](../../models/operations/listlmscontentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_courses

Returns a list of LmsCourses. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsCourses" method="get" path="/lms/{connection_id}/course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_courses(request={
        "connection_id": "<id>",
    })

    assert res.lms_courses is not None

    # Handle response
    print(res.lms_courses)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListLmsCoursesRequest](../../models/operations/listlmscoursesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListLmsCoursesResponse](../../models/operations/listlmscoursesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_instructors

Returns a list of LmsInstructors. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsInstructors" method="get" path="/lms/{connection_id}/instructor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_instructors(request={
        "connection_id": "<id>",
    })

    assert res.lms_instructors is not None

    # Handle response
    print(res.lms_instructors)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListLmsInstructorsRequest](../../models/operations/listlmsinstructorsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListLmsInstructorsResponse](../../models/operations/listlmsinstructorsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_students

Returns a list of LmsStudents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsStudents" method="get" path="/lms/{connection_id}/student" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.list_lms_students(request={
        "connection_id": "<id>",
    })

    assert res.lms_students is not None

    # Handle response
    print(res.lms_students)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListLmsStudentsRequest](../../models/operations/listlmsstudentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListLmsStudentsResponse](../../models/operations/listlmsstudentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_activity

Updates the LmsActivity identified by `id`. Provide the unified LmsActivity fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsActivity" method="patch" path="/lms/{connection_id}/activity/{id}" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2023-12-17T08:45:27.919Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "cd9c799a-e67e-4624-9680-2bf00f40913a",
            "is_completed": True,
            "metadata": [],
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2021-04-27T01:44:21.769Z"),
            "updated_at": parse_datetime("2022-02-04T16:00:41.517Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchLmsActivityRequest](../../models/operations/patchlmsactivityrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchLmsActivityResponse](../../models/operations/patchlmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_class

Updates the LmsClass identified by `id`. Provide the unified LmsClass fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsClass" method="patch" path="/lms/{connection_id}/class/{id}" example="lms_class" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "6f8abf9d-1e73-4dd2-b1f7-1aa1706178b5",
            "instructors": [],
            "languages": [
                "in",
            ],
            "media": [
                {
                    "content": "Defetiscor aetas acies benevolentia ulterius. Creta bis beneficium canis. Bonus valeo vulgo creator arca peior ceno earum culpa. Tabesco apostolus talis. Ultra accommodo deinde sono culpo arto cruciamentum triduana.",
                    "description": "Esse confido.",
                    "languages": [
                        "fa",
                        "da",
                    ],
                    "name": "illo",
                    "thumbnail_url": "https://loremflickr.com/199/1934?lock=4323325966476891",
                    "type": shared.LmsMediaType.VIDEO,
                    "url": "https://loremflickr.com/487/921?lock=5127962071241632",
                },
            ],
            "metadata": [],
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-08-21T17:44:33.779Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_class is not None

    # Handle response
    print(res.lms_class)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchLmsClassRequest](../../models/operations/patchlmsclassrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchLmsClassResponse](../../models/operations/patchlmsclassresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_collection

Updates the LmsCollection identified by `id`. Provide the unified LmsCollection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsCollection" method="patch" path="/lms/{connection_id}/collection/{id}" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "aa9e0c33-1756-4918-8e08-38234562e33f",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "metadata": [],
            "name": "ara",
            "updated_at": parse_datetime("2026-08-20T10:04:26.147Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchLmsCollectionRequest](../../models/operations/patchlmscollectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchLmsCollectionResponse](../../models/operations/patchlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_content

Updates the LmsContent identified by `id`. Provide the unified LmsContent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsContent" method="patch" path="/lms/{connection_id}/content/{id}" example="lms_content" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_content(request={
        "lms_content": {
            "categories": [
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "ee642dee-eb26-482d-a5ce-a4b18fbce955",
            "instructors": [],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Acervus.",
                    "language": "es",
                    "name": "talis",
                },
                {
                    "description": "Ratione.",
                    "language": "es",
                    "name": "sint",
                },
            ],
            "media": [
                {
                    "content": "Adnuo antepono vulticulus incidunt. Commemoro voro ocer arca velut vigor venustas una audeo. Consectetur totidem amor amo vigor. Patior ulciscor cohors necessitatibus beatae. Copiose cedo sub decens acer.",
                    "description": "Venia aeternus tandem spargo.",
                    "languages": [
                        "zu",
                        "ba",
                    ],
                    "name": "subiungo",
                    "thumbnail_url": "https://loremflickr.com/2056/3712?lock=5644845642923518",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://loremflickr.com/2593/1553?lock=8591263400111785",
                },
                {
                    "content": "Terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum. Absque adversus desino aut tabernus tollo vigor. Cur agnitio totidem consuasor bene doloribus. Vetus abundans curriculum curatio usitas.",
                    "description": "Comedo valde caste combibo.",
                    "languages": [
                        "it",
                        "hu",
                    ],
                    "name": "beneficium",
                    "thumbnail_url": "https://picsum.photos/seed/pNFr1/2597/885",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://loremflickr.com/3597/239?lock=7142808124990633",
                },
                {
                    "content": "Coepi demo adversus capillus aro unus templum. Aspicio alius vehemens terminatio varietas vomica. Apud thorax defero decet impedit verbera pauci laboriosam molestiae urbanus. Aveho vergo crux certus nulla caute sophismata. Caute voluptatibus patrocinor demo verumtamen adeo canis sapiente depraedor verus.",
                    "description": "Tunc barba decens.",
                    "languages": [
                        "bn",
                        "yo",
                    ],
                    "name": "qui",
                    "thumbnail_url": "https://loremflickr.com/1375/3377?lock=6601832177607674",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://loremflickr.com/3927/2086?lock=5199784913821481",
                },
            ],
            "metadata": [],
            "name": "ut",
            "provider_name": "Bins LLC",
            "published_at": parse_datetime("2022-09-10T01:00:41.531Z"),
            "short_description": "Caritas.",
            "skills": [
                "trucido",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "tibi",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "dens",
            ],
            "updated_at": parse_datetime("2022-10-11T06:40:48.177Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_content is not None

    # Handle response
    print(res.lms_content)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchLmsContentRequest](../../models/operations/patchlmscontentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchLmsContentResponse](../../models/operations/patchlmscontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_course

Updates the LmsCourse identified by `id`. Provide the unified LmsCourse fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsCourse" method="patch" path="/lms/{connection_id}/course/{id}" example="lms_course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "72ff9408-507c-4154-b0a1-5847cbc4f06f",
            "instructors": [],
            "is_active": True,
            "is_private": False,
            "languages": [
                "desparatus",
                "earum",
                "deripio",
            ],
            "media": [
                {
                    "content": "Adeptio crudelis ipsum utrimque quae architecto. Cum eius conitor anser abutor error adsuesco abeo. Denego nihil caries aveho.",
                    "description": "Adipiscor.",
                    "languages": [
                        "ms",
                        "te",
                    ],
                    "name": "tandem",
                    "thumbnail_url": "https://picsum.photos/seed/syTatRhK03/928/273",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/fQAbsk/2472/1671",
                },
            ],
            "metadata": [],
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2022-11-06T04:57:00.095Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-11T15:09:46.221Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchLmsCourseRequest](../../models/operations/patchlmscourserequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchLmsCourseResponse](../../models/operations/patchlmscourseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_instructor

Updates the LmsInstructor identified by `id`. Provide the unified LmsInstructor fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsInstructor" method="patch" path="/lms/{connection_id}/instructor/{id}" example="lms_instructor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_instructor(request={
        "lms_instructor": {
            "created_at": parse_datetime("2021-10-12T16:38:54.979Z"),
            "emails": [
                {},
            ],
            "first_name": "Deangelo",
            "id": "b6391dd3-aa9b-495a-aeb6-a50f68c3247c",
            "image_url": "https://avatars.githubusercontent.com/u/95131132",
            "last_name": "Ritchie",
            "metadata": [],
            "name": "Deangelo Ritchie",
            "telephones": [
                {
                    "telephone": "(605) 752-8163",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(430) 415-2451",
                    "type": shared.LmsTelephoneType.HOME,
                },
            ],
            "title": "Regional Security Agent",
            "updated_at": parse_datetime("2025-08-09T20:24:03.922Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_instructor is not None

    # Handle response
    print(res.lms_instructor)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchLmsInstructorRequest](../../models/operations/patchlmsinstructorrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchLmsInstructorResponse](../../models/operations/patchlmsinstructorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_student

Updates the LmsStudent identified by `id`. Provide the unified LmsStudent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsStudent" method="patch" path="/lms/{connection_id}/student/{id}" example="lms_student" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.patch_lms_student(request={
        "lms_student": {
            "address": {
                "address1": "15033 Corwin Circles",
                "city": "New Craigside",
                "country_code": "US",
                "postal_code": "73966",
                "region": "New Jersey",
                "region_code": "TX",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
            ],
            "first_name": "Marcella",
            "id": "37745e48-8712-499e-a0ee-1a4dab6ce2e1",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/56.jpg",
            "last_name": "Murazik",
            "metadata": [],
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(899) 827-6400",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(487) 213-8236",
                    "type": shared.LmsTelephoneType.FAX,
                },
                {
                    "telephone": "(980) 775-2940",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-07-08T12:13:30.452Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_student is not None

    # Handle response
    print(res.lms_student)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchLmsStudentRequest](../../models/operations/patchlmsstudentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchLmsStudentResponse](../../models/operations/patchlmsstudentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_activity

Deletes the LmsActivity identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsActivity" method="delete" path="/lms/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_activity(request={
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
| `request`                                                                                  | [operations.RemoveLmsActivityRequest](../../models/operations/removelmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveLmsActivityResponse](../../models/operations/removelmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_class

Deletes the LmsClass identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsClass" method="delete" path="/lms/{connection_id}/class/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_class(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveLmsClassRequest](../../models/operations/removelmsclassrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveLmsClassResponse](../../models/operations/removelmsclassresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_collection

Deletes the LmsCollection identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsCollection" method="delete" path="/lms/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveLmsCollectionRequest](../../models/operations/removelmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveLmsCollectionResponse](../../models/operations/removelmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_content

Deletes the LmsContent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsContent" method="delete" path="/lms/{connection_id}/content/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_content(request={
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
| `request`                                                                                | [operations.RemoveLmsContentRequest](../../models/operations/removelmscontentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveLmsContentResponse](../../models/operations/removelmscontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_course

Deletes the LmsCourse identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsCourse" method="delete" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_course(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveLmsCourseRequest](../../models/operations/removelmscourserequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveLmsCourseResponse](../../models/operations/removelmscourseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_instructor

Deletes the LmsInstructor identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsInstructor" method="delete" path="/lms/{connection_id}/instructor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_instructor(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveLmsInstructorRequest](../../models/operations/removelmsinstructorrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveLmsInstructorResponse](../../models/operations/removelmsinstructorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_student

Deletes the LmsStudent identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsStudent" method="delete" path="/lms/{connection_id}/student/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.remove_lms_student(request={
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
| `request`                                                                                | [operations.RemoveLmsStudentRequest](../../models/operations/removelmsstudentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveLmsStudentResponse](../../models/operations/removelmsstudentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_activity

Updates the LmsActivity identified by `id`. Provide the unified LmsActivity fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsActivity" method="put" path="/lms/{connection_id}/activity/{id}" example="lms_activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_activity(request={
        "lms_activity": {
            "assigned_grade": "summopere",
            "completed_at": parse_datetime("2023-12-17T08:45:27.919Z"),
            "created_at": parse_datetime("2020-10-17T01:25:21.745Z"),
            "duration_minutes": 55.0,
            "id": "cd9c799a-e67e-4624-9680-2bf00f40913a",
            "is_completed": True,
            "metadata": [],
            "progress_percentage": 100.0,
            "started_at": parse_datetime("2021-04-27T01:44:21.769Z"),
            "updated_at": parse_datetime("2022-02-04T16:00:41.517Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_activity is not None

    # Handle response
    print(res.lms_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateLmsActivityRequest](../../models/operations/updatelmsactivityrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateLmsActivityResponse](../../models/operations/updatelmsactivityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_class

Updates the LmsClass identified by `id`. Provide the unified LmsClass fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsClass" method="put" path="/lms/{connection_id}/class/{id}" example="lms_class" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "6f8abf9d-1e73-4dd2-b1f7-1aa1706178b5",
            "instructors": [],
            "languages": [
                "in",
            ],
            "media": [
                {
                    "content": "Defetiscor aetas acies benevolentia ulterius. Creta bis beneficium canis. Bonus valeo vulgo creator arca peior ceno earum culpa. Tabesco apostolus talis. Ultra accommodo deinde sono culpo arto cruciamentum triduana.",
                    "description": "Esse confido.",
                    "languages": [
                        "fa",
                        "da",
                    ],
                    "name": "illo",
                    "thumbnail_url": "https://loremflickr.com/199/1934?lock=4323325966476891",
                    "type": shared.LmsMediaType.VIDEO,
                    "url": "https://loremflickr.com/487/921?lock=5127962071241632",
                },
            ],
            "metadata": [],
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-08-21T17:44:33.779Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_class is not None

    # Handle response
    print(res.lms_class)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateLmsClassRequest](../../models/operations/updatelmsclassrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateLmsClassResponse](../../models/operations/updatelmsclassresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_collection

Updates the LmsCollection identified by `id`. Provide the unified LmsCollection fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsCollection" method="put" path="/lms/{connection_id}/collection/{id}" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "aa9e0c33-1756-4918-8e08-38234562e33f",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "metadata": [],
            "name": "ara",
            "updated_at": parse_datetime("2026-08-20T10:04:26.147Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateLmsCollectionRequest](../../models/operations/updatelmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateLmsCollectionResponse](../../models/operations/updatelmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_content

Updates the LmsContent identified by `id`. Provide the unified LmsContent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsContent" method="put" path="/lms/{connection_id}/content/{id}" example="lms_content" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_content(request={
        "lms_content": {
            "categories": [
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "ee642dee-eb26-482d-a5ce-a4b18fbce955",
            "instructors": [],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Acervus.",
                    "language": "es",
                    "name": "talis",
                },
                {
                    "description": "Ratione.",
                    "language": "es",
                    "name": "sint",
                },
            ],
            "media": [
                {
                    "content": "Adnuo antepono vulticulus incidunt. Commemoro voro ocer arca velut vigor venustas una audeo. Consectetur totidem amor amo vigor. Patior ulciscor cohors necessitatibus beatae. Copiose cedo sub decens acer.",
                    "description": "Venia aeternus tandem spargo.",
                    "languages": [
                        "zu",
                        "ba",
                    ],
                    "name": "subiungo",
                    "thumbnail_url": "https://loremflickr.com/2056/3712?lock=5644845642923518",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://loremflickr.com/2593/1553?lock=8591263400111785",
                },
                {
                    "content": "Terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum. Absque adversus desino aut tabernus tollo vigor. Cur agnitio totidem consuasor bene doloribus. Vetus abundans curriculum curatio usitas.",
                    "description": "Comedo valde caste combibo.",
                    "languages": [
                        "it",
                        "hu",
                    ],
                    "name": "beneficium",
                    "thumbnail_url": "https://picsum.photos/seed/pNFr1/2597/885",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://loremflickr.com/3597/239?lock=7142808124990633",
                },
                {
                    "content": "Coepi demo adversus capillus aro unus templum. Aspicio alius vehemens terminatio varietas vomica. Apud thorax defero decet impedit verbera pauci laboriosam molestiae urbanus. Aveho vergo crux certus nulla caute sophismata. Caute voluptatibus patrocinor demo verumtamen adeo canis sapiente depraedor verus.",
                    "description": "Tunc barba decens.",
                    "languages": [
                        "bn",
                        "yo",
                    ],
                    "name": "qui",
                    "thumbnail_url": "https://loremflickr.com/1375/3377?lock=6601832177607674",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://loremflickr.com/3927/2086?lock=5199784913821481",
                },
            ],
            "metadata": [],
            "name": "ut",
            "provider_name": "Bins LLC",
            "published_at": parse_datetime("2022-09-10T01:00:41.531Z"),
            "short_description": "Caritas.",
            "skills": [
                "trucido",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "tibi",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "dens",
            ],
            "updated_at": parse_datetime("2022-10-11T06:40:48.177Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_content is not None

    # Handle response
    print(res.lms_content)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateLmsContentRequest](../../models/operations/updatelmscontentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateLmsContentResponse](../../models/operations/updatelmscontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_course

Updates the LmsCourse identified by `id`. Provide the unified LmsCourse fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsCourse" method="put" path="/lms/{connection_id}/course/{id}" example="lms_course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "72ff9408-507c-4154-b0a1-5847cbc4f06f",
            "instructors": [],
            "is_active": True,
            "is_private": False,
            "languages": [
                "desparatus",
                "earum",
                "deripio",
            ],
            "media": [
                {
                    "content": "Adeptio crudelis ipsum utrimque quae architecto. Cum eius conitor anser abutor error adsuesco abeo. Denego nihil caries aveho.",
                    "description": "Adipiscor.",
                    "languages": [
                        "ms",
                        "te",
                    ],
                    "name": "tandem",
                    "thumbnail_url": "https://picsum.photos/seed/syTatRhK03/928/273",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/fQAbsk/2472/1671",
                },
            ],
            "metadata": [],
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2022-11-06T04:57:00.095Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-11T15:09:46.221Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateLmsCourseRequest](../../models/operations/updatelmscourserequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateLmsCourseResponse](../../models/operations/updatelmscourseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_instructor

Updates the LmsInstructor identified by `id`. Provide the unified LmsInstructor fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsInstructor" method="put" path="/lms/{connection_id}/instructor/{id}" example="lms_instructor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_instructor(request={
        "lms_instructor": {
            "created_at": parse_datetime("2021-10-12T16:38:54.979Z"),
            "emails": [
                {},
            ],
            "first_name": "Deangelo",
            "id": "b6391dd3-aa9b-495a-aeb6-a50f68c3247c",
            "image_url": "https://avatars.githubusercontent.com/u/95131132",
            "last_name": "Ritchie",
            "metadata": [],
            "name": "Deangelo Ritchie",
            "telephones": [
                {
                    "telephone": "(605) 752-8163",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(430) 415-2451",
                    "type": shared.LmsTelephoneType.HOME,
                },
            ],
            "title": "Regional Security Agent",
            "updated_at": parse_datetime("2025-08-09T20:24:03.922Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_instructor is not None

    # Handle response
    print(res.lms_instructor)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateLmsInstructorRequest](../../models/operations/updatelmsinstructorrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateLmsInstructorResponse](../../models/operations/updatelmsinstructorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_student

Updates the LmsStudent identified by `id`. Provide the unified LmsStudent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsStudent" method="put" path="/lms/{connection_id}/student/{id}" example="lms_student" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.lms.update_lms_student(request={
        "lms_student": {
            "address": {
                "address1": "15033 Corwin Circles",
                "city": "New Craigside",
                "country_code": "US",
                "postal_code": "73966",
                "region": "New Jersey",
                "region_code": "TX",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
            ],
            "first_name": "Marcella",
            "id": "37745e48-8712-499e-a0ee-1a4dab6ce2e1",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/56.jpg",
            "last_name": "Murazik",
            "metadata": [],
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(899) 827-6400",
                    "type": shared.LmsTelephoneType.WORK,
                },
                {
                    "telephone": "(487) 213-8236",
                    "type": shared.LmsTelephoneType.FAX,
                },
                {
                    "telephone": "(980) 775-2940",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-07-08T12:13:30.452Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_student is not None

    # Handle response
    print(res.lms_student)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateLmsStudentRequest](../../models/operations/updatelmsstudentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateLmsStudentResponse](../../models/operations/updatelmsstudentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |