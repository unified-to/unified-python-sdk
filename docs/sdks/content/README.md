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

Create a content

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
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "external_reference": "0d230e31-a9c4-4a35-a5b9-9168e91ffff5",
            "id": "4b53d3e9-5e61-4c61-8c77-4eb56adc5012",
            "instructors": [
                {
                    "id": "91a23b20-a7a3-4323-9548-0897c09eb49e",
                    "name": "Winston Ferry",
                },
            ],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Numquam.",
                    "language": "es",
                    "name": "validus",
                },
                {
                    "description": "Callide.",
                    "language": "fr",
                    "name": "crux",
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
            "name": "ut",
            "provider_name": "Berge LLC",
            "published_at": parse_datetime("2023-11-08T11:32:09.080Z"),
            "short_description": "Commemoro.",
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
            "updated_at": parse_datetime("2022-09-24T09:02:30.819Z"),
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

Retrieve a content

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

List all contents

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

Update a content

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
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "external_reference": "0d230e31-a9c4-4a35-a5b9-9168e91ffff5",
            "id": "ffd0eb94-cb69-40ee-9bf2-0f43f94c1cde",
            "instructors": [
                {
                    "id": "91a23b20-a7a3-4323-9548-0897c09eb49e",
                    "name": "Winston Ferry",
                },
            ],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Numquam.",
                    "language": "es",
                    "name": "validus",
                },
                {
                    "description": "Callide.",
                    "language": "fr",
                    "name": "crux",
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
            "name": "ut",
            "provider_name": "Berge LLC",
            "published_at": parse_datetime("2023-11-08T11:32:09.080Z"),
            "short_description": "Commemoro.",
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
            "updated_at": parse_datetime("2022-09-24T09:02:30.829Z"),
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

Remove a content

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

Update a content

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
                "territo",
            ],
            "created_at": parse_datetime("2020-10-22T22:30:50.963Z"),
            "description": "Usque laboriosam ventosus adflicto.",
            "difficulty": "Beginner",
            "duration_minutes": 19.0,
            "external_reference": "0d230e31-a9c4-4a35-a5b9-9168e91ffff5",
            "id": "ffd0eb94-cb69-40ee-9bf2-0f43f94c1cde",
            "instructors": [
                {
                    "id": "91a23b20-a7a3-4323-9548-0897c09eb49e",
                    "name": "Winston Ferry",
                },
            ],
            "is_active": True,
            "languages": [
                "despecto",
                "suppellex",
            ],
            "localizations": [
                {
                    "description": "Numquam.",
                    "language": "es",
                    "name": "validus",
                },
                {
                    "description": "Callide.",
                    "language": "fr",
                    "name": "crux",
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
            "name": "ut",
            "provider_name": "Berge LLC",
            "published_at": parse_datetime("2023-11-08T11:32:09.080Z"),
            "short_description": "Commemoro.",
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
            "updated_at": parse_datetime("2022-09-24T09:02:30.829Z"),
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