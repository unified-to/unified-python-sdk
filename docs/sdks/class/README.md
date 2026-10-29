# Class

## Overview

### Available Operations

* [create_lms_class](#create_lms_class) - Create a class
* [get_lms_class](#get_lms_class) - Retrieve a class
* [list_lms_classes](#list_lms_classes) - List all classes
* [patch_lms_class](#patch_lms_class) - Update a class
* [remove_lms_class](#remove_lms_class) - Remove a class
* [update_lms_class](#update_lms_class) - Update a class

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

    res = unified_to.class_.create_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "dbabefc1-b8d5-4f26-a9c9-cf946b54f271",
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
            "updated_at": parse_datetime("2025-08-10T03:54:30.892Z"),
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

    res = unified_to.class_.get_lms_class(request={
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

    res = unified_to.class_.list_lms_classes(request={
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

    res = unified_to.class_.patch_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "d0107c86-5e71-4a4c-9f73-b76715c9b496",
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
            "updated_at": parse_datetime("2025-08-10T03:54:30.906Z"),
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

    res = unified_to.class_.remove_lms_class(request={
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

    res = unified_to.class_.update_lms_class(request={
        "lms_class": {
            "created_at": parse_datetime("2020-02-20T14:48:51.845Z"),
            "description": "Anser sperno decerno.",
            "id": "d0107c86-5e71-4a4c-9f73-b76715c9b496",
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
            "updated_at": parse_datetime("2025-08-10T03:54:30.906Z"),
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