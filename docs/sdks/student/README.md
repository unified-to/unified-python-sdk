# Student

## Overview

### Available Operations

* [create_lms_student](#create_lms_student) - Create a student
* [get_lms_student](#get_lms_student) - Retrieve a student
* [list_lms_students](#list_lms_students) - List all students
* [patch_lms_student](#patch_lms_student) - Update a student
* [remove_lms_student](#remove_lms_student) - Remove a student
* [update_lms_student](#update_lms_student) - Update a student

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

    res = unified_to.student.create_lms_student(request={
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
            "id": "ba61c987-c772-4121-ba95-9cd28a202fa6",
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
            "updated_at": parse_datetime("2022-07-01T23:04:14.778Z"),
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

    res = unified_to.student.get_lms_student(request={
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

    res = unified_to.student.list_lms_students(request={
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

    res = unified_to.student.patch_lms_student(request={
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
            "id": "c5a46add-c6b9-4b15-ba30-807d15e32c3a",
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
            "updated_at": parse_datetime("2022-07-01T23:04:14.787Z"),
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

    res = unified_to.student.remove_lms_student(request={
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

    res = unified_to.student.update_lms_student(request={
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
            "id": "c5a46add-c6b9-4b15-ba30-807d15e32c3a",
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
            "updated_at": parse_datetime("2022-07-01T23:04:14.787Z"),
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