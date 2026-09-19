# Course

## Overview

### Available Operations

* [create_lms_course](#create_lms_course) - Create a course
* [get_lms_course](#get_lms_course) - Retrieve a course
* [list_lms_courses](#list_lms_courses) - List all courses
* [patch_lms_course](#patch_lms_course) - Update a course
* [remove_lms_course](#remove_lms_course) - Remove a course
* [update_lms_course](#update_lms_course) - Update a course

## create_lms_course

Create a course

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

    res = unified_to.course.create_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "07366ae4-bfb5-4e49-8037-c19297201498",
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
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2023-12-30T03:35:03.902Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-07T00:25:41.280Z"),
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

## get_lms_course

Retrieve a course

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

    res = unified_to.course.get_lms_course(request={
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

## list_lms_courses

List all courses

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

    res = unified_to.course.list_lms_courses(request={
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

## patch_lms_course

Update a course

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

    res = unified_to.course.patch_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "6ed64692-685d-4ec9-98f9-1c42ef617a8e",
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
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2023-12-30T03:35:03.902Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-07T00:25:41.282Z"),
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

## remove_lms_course

Remove a course

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

    res = unified_to.course.remove_lms_course(request={
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

## update_lms_course

Update a course

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

    res = unified_to.course.update_lms_course(request={
        "lms_course": {
            "categories": [
                "tergiversatio",
                "tumultus",
            ],
            "created_at": parse_datetime("2022-10-06T09:58:53.559Z"),
            "currency": "FJD",
            "description": "Vinco alias aut capitulus.",
            "duration_minutes": 148.0,
            "id": "6ed64692-685d-4ec9-98f9-1c42ef617a8e",
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
            "name": "comptus",
            "price_amount": 84.0,
            "provider_name": "Homenick - Wunsch",
            "published_at": parse_datetime("2023-12-30T03:35:03.902Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-07T00:25:41.282Z"),
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