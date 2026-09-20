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

Create a class

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
            "id": "952c8cd0-b71d-4987-a436-295323e73323",
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
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-07-08T23:25:54.003Z"),
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

Retrieve a class

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

List all classes

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

Update a class

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
            "id": "70cf1ed2-3269-4bc4-a792-7b52c9667cd3",
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
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-07-08T23:25:54.011Z"),
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

Remove a class

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

Update a class

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
            "id": "70cf1ed2-3269-4bc4-a792-7b52c9667cd3",
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
            "name": "virtus",
            "students": [],
            "updated_at": parse_datetime("2025-07-08T23:25:54.011Z"),
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