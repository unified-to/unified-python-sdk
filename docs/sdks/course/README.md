# Course

## Overview

### Available Operations

* [create_lms_course2](#create_lms_course2) - Create a course
* [get_lms_course2](#get_lms_course2) - Retrieve a course
* [list_lms_courses2](#list_lms_courses2) - List all courses
* [patch_lms_course2](#patch_lms_course2) - Update a course
* [remove_lms_course2](#remove_lms_course2) - Remove a course
* [update_lms_course2](#update_lms_course2) - Update a course

## create_lms_course2

Create a course

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsCourse2" method="post" path="/lms/{connection_id}/course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.create_lms_course2(request={
        "lms_course": {},
        "connection_id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateLmsCourse2Request](../../models/operations/createlmscourse2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateLmsCourse2Response](../../models/operations/createlmscourse2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_course2

Retrieve a course

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsCourse2" method="get" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.get_lms_course2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLmsCourse2Request](../../models/operations/getlmscourse2request.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetLmsCourse2Response](../../models/operations/getlmscourse2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_courses2

List all courses

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsCourses2" method="get" path="/lms/{connection_id}/course" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.list_lms_courses2(request={
        "connection_id": "<id>",
    })

    assert res.lms_courses is not None

    # Handle response
    print(res.lms_courses)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListLmsCourses2Request](../../models/operations/listlmscourses2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListLmsCourses2Response](../../models/operations/listlmscourses2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_course2

Update a course

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsCourse2" method="patch" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.patch_lms_course2(request={
        "lms_course": {},
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
| `request`                                                                              | [operations.PatchLmsCourse2Request](../../models/operations/patchlmscourse2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchLmsCourse2Response](../../models/operations/patchlmscourse2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_course2

Remove a course

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsCourse2" method="delete" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.remove_lms_course2(request={
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
| `request`                                                                                | [operations.RemoveLmsCourse2Request](../../models/operations/removelmscourse2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveLmsCourse2Response](../../models/operations/removelmscourse2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_course2

Update a course

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsCourse2" method="put" path="/lms/{connection_id}/course/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.course.update_lms_course2(request={
        "lms_course": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_course is not None

    # Handle response
    print(res.lms_course)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateLmsCourse2Request](../../models/operations/updatelmscourse2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateLmsCourse2Response](../../models/operations/updatelmscourse2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |