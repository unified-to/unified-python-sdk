# Instructor
(*instructor*)

## Overview

### Available Operations

* [create_lms_instructor](#create_lms_instructor) - Create an instructor
* [get_lms_instructor](#get_lms_instructor) - Retrieve an instructor
* [list_lms_instructors](#list_lms_instructors) - List all instructors
* [patch_lms_instructor](#patch_lms_instructor) - Update an instructor
* [remove_lms_instructor](#remove_lms_instructor) - Remove an instructor
* [update_lms_instructor](#update_lms_instructor) - Update an instructor

## create_lms_instructor

Create an instructor

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.create_lms_instructor(request={
    "connection_id": "<id>",
})

if res.lms_instructor is not None:
    # handle response
    pass

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

## get_lms_instructor

Retrieve an instructor

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.get_lms_instructor(request={
    "connection_id": "<id>",
    "id": "<id>",
})

if res.lms_instructor is not None:
    # handle response
    pass

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

## list_lms_instructors

List all instructors

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.list_lms_instructors(request={
    "connection_id": "<id>",
})

if res.lms_instructors is not None:
    # handle response
    pass

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

## patch_lms_instructor

Update an instructor

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.patch_lms_instructor(request={
    "connection_id": "<id>",
    "id": "<id>",
})

if res.lms_instructor is not None:
    # handle response
    pass

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

## remove_lms_instructor

Remove an instructor

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.remove_lms_instructor(request={
    "connection_id": "<id>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

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

## update_lms_instructor

Update an instructor

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.instructor.update_lms_instructor(request={
    "connection_id": "<id>",
    "id": "<id>",
})

if res.lms_instructor is not None:
    # handle response
    pass

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