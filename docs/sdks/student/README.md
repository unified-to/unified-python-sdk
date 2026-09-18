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

Create a student

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
                "address1": "94082 Kassandra Camp",
                "address2": "Apt. 461",
                "city": "New Ibrahimmouth",
                "country_code": "US",
                "postal_code": "52851",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
                {},
            ],
            "first_name": "Marcella",
            "id": "8bc0cb22-4e46-4da8-b2ef-49aa7508d4ce",
            "image_url": "https://avatars.githubusercontent.com/u/36301374",
            "last_name": "Murazik",
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(482) 469-8067",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-06-19T13:55:47.489Z"),
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

Retrieve a student

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

List all students

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

Update a student

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
                "address1": "94082 Kassandra Camp",
                "address2": "Apt. 461",
                "city": "New Ibrahimmouth",
                "country_code": "US",
                "postal_code": "52851",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
                {},
            ],
            "first_name": "Marcella",
            "id": "8c067562-a326-4d81-a8ae-f087841b1a98",
            "image_url": "https://avatars.githubusercontent.com/u/36301374",
            "last_name": "Murazik",
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(482) 469-8067",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-06-19T13:55:47.495Z"),
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

Remove a student

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

Update a student

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
                "address1": "94082 Kassandra Camp",
                "address2": "Apt. 461",
                "city": "New Ibrahimmouth",
                "country_code": "US",
                "postal_code": "52851",
                "region": "Tennessee",
                "region_code": "NV",
            },
            "created_at": parse_datetime("2020-03-23T06:59:29.777Z"),
            "emails": [
                {},
                {},
            ],
            "first_name": "Marcella",
            "id": "8c067562-a326-4d81-a8ae-f087841b1a98",
            "image_url": "https://avatars.githubusercontent.com/u/36301374",
            "last_name": "Murazik",
            "name": "Marcella Murazik",
            "telephones": [
                {
                    "telephone": "(482) 469-8067",
                    "type": shared.LmsTelephoneType.FAX,
                },
            ],
            "updated_at": parse_datetime("2022-06-19T13:55:47.495Z"),
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