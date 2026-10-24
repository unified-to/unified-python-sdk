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
            "id": "2637a1aa-262e-41ab-92d9-4b4c103622a8",
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
            "published_at": parse_datetime("2022-11-05T19:35:30.514Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-10T00:11:37.496Z"),
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
            "id": "11672845-45b4-465f-a26a-e9344f0a9552",
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
            "published_at": parse_datetime("2022-11-05T19:35:30.515Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-10T00:11:37.499Z"),
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
            "id": "11672845-45b4-465f-a26a-e9344f0a9552",
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
            "published_at": parse_datetime("2022-11-05T19:35:30.515Z"),
            "skills": [
                "adiuvo",
                "tam",
            ],
            "students": [],
            "time_estimate_minutes": 100.0,
            "updated_at": parse_datetime("2023-02-10T00:11:37.499Z"),
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