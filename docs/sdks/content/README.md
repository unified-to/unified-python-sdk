# Content

## Overview

### Available Operations

* [create_lms_content](#create_lms_content) - Create a content
* [get_lms_content](#get_lms_content) - Retrieve a content
* [list_lms_contents](#list_lms_contents) - List all contents
* [patch_lms_content](#patch_lms_content) - Update a content
* [remove_lms_content](#remove_lms_content) - Remove a content
* [update_lms_content](#update_lms_content) - Update a content

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

    res = unified_to.content.create_lms_content(request={
        "lms_content": {
            "categories": [
                "tergum",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Adflicto despecto suppellex socius cresco.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "74f7f086-8baa-4d4e-8e95-970baaeb4f52",
            "instructors": [],
            "is_active": True,
            "languages": [
                "campana",
                "viriliter",
            ],
            "localizations": [
                {
                    "description": "Vindico vorago.",
                    "language": "es",
                    "name": "aeger",
                },
                {
                    "description": "Sulum.",
                    "language": "es",
                    "name": "voluptate",
                },
            ],
            "media": [
                {
                    "content": "Cohors necessitatibus beatae copiose copiose cedo sub decens acer. Spiritus velum adulatio commodi textus beneficium termes comedo valde caste. Sodalitas bos timor abeo cur. Sperno decet acquiro tabgo canto terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum.",
                    "description": "Incidunt tepidus commemoro voro ocer.",
                    "languages": [
                        "ro",
                        "af",
                    ],
                    "name": "antepono",
                    "thumbnail_url": "https://picsum.photos/seed/URbmlO66Wk/587/3603",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/4KFvVbCx83/2788/2850",
                },
                {
                    "content": "Ago neque qui cursim tunc barba decens. Tutamen amplus tabella tabgo infit. Demo adversus capillus aro unus. Dedico aspicio alius vehemens terminatio varietas vomica voluptatibus apud. Defero decet impedit verbera pauci laboriosam molestiae urbanus mollitia. Vergo crux certus nulla.",
                    "description": "Bene doloribus.",
                    "languages": [
                        "ru",
                        "sw",
                    ],
                    "name": "totidem",
                    "thumbnail_url": "https://picsum.photos/seed/qpRev/1286/3718",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://picsum.photos/seed/JOWrp5/254/2004",
                },
                {
                    "content": "Laborum adiuvo labore officia demulceo. Abduco mollitia ventosus synagoga certus magni vado cilicium stella. Velut capitulus attero odio advenio similique acsi totam atavus aufero. Ventosus campana animi.",
                    "description": "Trucido dens pecus aer stella.",
                    "languages": [
                        "is",
                        "sk",
                    ],
                    "name": "territo",
                    "thumbnail_url": "https://picsum.photos/seed/81EuDedaf/557/986",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/BtV2eDuVm7/3644/1033",
                },
            ],
            "metadata": [],
            "name": "laboriosam",
            "provider_name": "Mraz - Keeling",
            "published_at": parse_datetime("2022-09-15T01:51:13.531Z"),
            "short_description": "Videlicet pauci.",
            "skills": [
                "soleo",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "clam",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "audio",
            ],
            "updated_at": parse_datetime("2022-10-16T13:00:57.008Z"),
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

    res = unified_to.content.get_lms_content(request={
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

    res = unified_to.content.list_lms_contents(request={
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

    res = unified_to.content.patch_lms_content(request={
        "lms_content": {
            "categories": [
                "tergum",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Adflicto despecto suppellex socius cresco.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "dbbe59ec-47a9-42cf-9eac-cfd232c77744",
            "instructors": [],
            "is_active": True,
            "languages": [
                "campana",
                "viriliter",
            ],
            "localizations": [
                {
                    "description": "Vindico vorago.",
                    "language": "es",
                    "name": "aeger",
                },
                {
                    "description": "Sulum.",
                    "language": "es",
                    "name": "voluptate",
                },
            ],
            "media": [
                {
                    "content": "Cohors necessitatibus beatae copiose copiose cedo sub decens acer. Spiritus velum adulatio commodi textus beneficium termes comedo valde caste. Sodalitas bos timor abeo cur. Sperno decet acquiro tabgo canto terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum.",
                    "description": "Incidunt tepidus commemoro voro ocer.",
                    "languages": [
                        "ro",
                        "af",
                    ],
                    "name": "antepono",
                    "thumbnail_url": "https://picsum.photos/seed/URbmlO66Wk/587/3603",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/4KFvVbCx83/2788/2850",
                },
                {
                    "content": "Ago neque qui cursim tunc barba decens. Tutamen amplus tabella tabgo infit. Demo adversus capillus aro unus. Dedico aspicio alius vehemens terminatio varietas vomica voluptatibus apud. Defero decet impedit verbera pauci laboriosam molestiae urbanus mollitia. Vergo crux certus nulla.",
                    "description": "Bene doloribus.",
                    "languages": [
                        "ru",
                        "sw",
                    ],
                    "name": "totidem",
                    "thumbnail_url": "https://picsum.photos/seed/qpRev/1286/3718",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://picsum.photos/seed/JOWrp5/254/2004",
                },
                {
                    "content": "Laborum adiuvo labore officia demulceo. Abduco mollitia ventosus synagoga certus magni vado cilicium stella. Velut capitulus attero odio advenio similique acsi totam atavus aufero. Ventosus campana animi.",
                    "description": "Trucido dens pecus aer stella.",
                    "languages": [
                        "is",
                        "sk",
                    ],
                    "name": "territo",
                    "thumbnail_url": "https://picsum.photos/seed/81EuDedaf/557/986",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/BtV2eDuVm7/3644/1033",
                },
            ],
            "metadata": [],
            "name": "laboriosam",
            "provider_name": "Mraz - Keeling",
            "published_at": parse_datetime("2022-09-15T01:51:13.540Z"),
            "short_description": "Videlicet pauci.",
            "skills": [
                "soleo",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "clam",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "audio",
            ],
            "updated_at": parse_datetime("2022-10-16T13:00:57.017Z"),
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

    res = unified_to.content.remove_lms_content(request={
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

    res = unified_to.content.update_lms_content(request={
        "lms_content": {
            "categories": [
                "tergum",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Adflicto despecto suppellex socius cresco.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "id": "dbbe59ec-47a9-42cf-9eac-cfd232c77744",
            "instructors": [],
            "is_active": True,
            "languages": [
                "campana",
                "viriliter",
            ],
            "localizations": [
                {
                    "description": "Vindico vorago.",
                    "language": "es",
                    "name": "aeger",
                },
                {
                    "description": "Sulum.",
                    "language": "es",
                    "name": "voluptate",
                },
            ],
            "media": [
                {
                    "content": "Cohors necessitatibus beatae copiose copiose cedo sub decens acer. Spiritus velum adulatio commodi textus beneficium termes comedo valde caste. Sodalitas bos timor abeo cur. Sperno decet acquiro tabgo canto terminatio acidus tripudio teres. Compono demum aut aestivus ambitus pecus tergum verumtamen vestrum.",
                    "description": "Incidunt tepidus commemoro voro ocer.",
                    "languages": [
                        "ro",
                        "af",
                    ],
                    "name": "antepono",
                    "thumbnail_url": "https://picsum.photos/seed/URbmlO66Wk/587/3603",
                    "type": shared.LmsMediaType.OTHER,
                    "url": "https://picsum.photos/seed/4KFvVbCx83/2788/2850",
                },
                {
                    "content": "Ago neque qui cursim tunc barba decens. Tutamen amplus tabella tabgo infit. Demo adversus capillus aro unus. Dedico aspicio alius vehemens terminatio varietas vomica voluptatibus apud. Defero decet impedit verbera pauci laboriosam molestiae urbanus mollitia. Vergo crux certus nulla.",
                    "description": "Bene doloribus.",
                    "languages": [
                        "ru",
                        "sw",
                    ],
                    "name": "totidem",
                    "thumbnail_url": "https://picsum.photos/seed/qpRev/1286/3718",
                    "type": shared.LmsMediaType.WEB,
                    "url": "https://picsum.photos/seed/JOWrp5/254/2004",
                },
                {
                    "content": "Laborum adiuvo labore officia demulceo. Abduco mollitia ventosus synagoga certus magni vado cilicium stella. Velut capitulus attero odio advenio similique acsi totam atavus aufero. Ventosus campana animi.",
                    "description": "Trucido dens pecus aer stella.",
                    "languages": [
                        "is",
                        "sk",
                    ],
                    "name": "territo",
                    "thumbnail_url": "https://picsum.photos/seed/81EuDedaf/557/986",
                    "type": shared.LmsMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/BtV2eDuVm7/3644/1033",
                },
            ],
            "metadata": [],
            "name": "laboriosam",
            "provider_name": "Mraz - Keeling",
            "published_at": parse_datetime("2022-09-15T01:51:13.540Z"),
            "short_description": "Videlicet pauci.",
            "skills": [
                "soleo",
            ],
            "sort_order": 3.0,
            "subjects": [
                {
                    "name": "clam",
                    "rank": 1.0,
                },
            ],
            "tags": [
                "audio",
            ],
            "updated_at": parse_datetime("2022-10-16T13:00:57.017Z"),
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