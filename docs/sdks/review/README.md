# Review

## Overview

### Available Operations

* [create_commerce_review](#create_commerce_review) - Create a review
* [get_commerce_review](#get_commerce_review) - Retrieve a review
* [get_performance_review](#get_performance_review) - Retrieve a review
* [get_social_review](#get_social_review) - Retrieve a review
* [list_commerce_reviews](#list_commerce_reviews) - List all reviews
* [list_performance_reviews](#list_performance_reviews) - List all reviews
* [list_social_reviews](#list_social_reviews) - List all reviews
* [patch_commerce_review](#patch_commerce_review) - Update a review
* [patch_social_review](#patch_social_review) - Update a review
* [remove_commerce_review](#remove_commerce_review) - Remove a review
* [update_commerce_review](#update_commerce_review) - Update a review
* [update_social_review](#update_social_review) - Update a review

## create_commerce_review

Create a review

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceReview" method="post" path="/commerce/{connection_id}/review" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.create_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "9b676a48-a652-4c2d-af59-f8704bdbbb94",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "66ae1e30-9360-4d61-9123-105bfb6c0b66",
                    "metadata": [
                        {
                            "id": "b3fd4fbb-c135-45b2-bf9d-6cb5320f2810",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "cbf79437-06f8-491a-8369-b3f840ff6945",
                    "metadata": [
                        {
                            "id": "4df7b4b3-f057-4487-9792-b414977ff1f3",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "c6fcb4d8-e95c-4d66-89ac-ea17f0b8ff23",
                    "metadata": [
                        {
                            "id": "26700033-8588-47e2-a866-8bfeb9d1a3d2",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-07-25T17:49:18.797Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
        },
        "connection_id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateCommerceReviewRequest](../../models/operations/createcommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateCommerceReviewResponse](../../models/operations/createcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_review

Retrieve a review

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceReview" method="get" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.get_commerce_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetCommerceReviewRequest](../../models/operations/getcommercereviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetCommerceReviewResponse](../../models/operations/getcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_performance_review

Retrieve a review

### Example Usage

<!-- UsageSnippet language="python" operationID="getPerformanceReview" method="get" path="/performance/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.get_performance_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.performance_review is not None

    # Handle response
    print(res.performance_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetPerformanceReviewRequest](../../models/operations/getperformancereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetPerformanceReviewResponse](../../models/operations/getperformancereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_social_review

Retrieve a review

### Example Usage

<!-- UsageSnippet language="python" operationID="getSocialReview" method="get" path="/social/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.get_social_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.social_review is not None

    # Handle response
    print(res.social_review)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetSocialReviewRequest](../../models/operations/getsocialreviewrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetSocialReviewResponse](../../models/operations/getsocialreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_reviews

List all reviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceReviews" method="get" path="/commerce/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.list_commerce_reviews(request={
        "connection_id": "<id>",
    })

    assert res.commerce_reviews is not None

    # Handle response
    print(res.commerce_reviews)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListCommerceReviewsRequest](../../models/operations/listcommercereviewsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListCommerceReviewsResponse](../../models/operations/listcommercereviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_performance_reviews

List all reviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listPerformanceReviews" method="get" path="/performance/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.list_performance_reviews(request={
        "connection_id": "<id>",
    })

    assert res.performance_reviews is not None

    # Handle response
    print(res.performance_reviews)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListPerformanceReviewsRequest](../../models/operations/listperformancereviewsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListPerformanceReviewsResponse](../../models/operations/listperformancereviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_social_reviews

List all reviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listSocialReviews" method="get" path="/social/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.list_social_reviews(request={
        "connection_id": "<id>",
    })

    assert res.social_reviews is not None

    # Handle response
    print(res.social_reviews)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListSocialReviewsRequest](../../models/operations/listsocialreviewsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListSocialReviewsResponse](../../models/operations/listsocialreviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_review

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceReview" method="patch" path="/commerce/{connection_id}/review/{id}" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.patch_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "93135370-f2c2-4f01-b2bb-5d84f1480e58",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "a71e645f-b896-4c75-b7ed-231804e1750a",
                    "metadata": [
                        {
                            "id": "ac9835d9-1cc9-49fb-a1a8-2ad779f81c3f",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "dbe3c1c1-3198-4098-b5a2-682f0295c25b",
                    "metadata": [
                        {
                            "id": "52239305-ea00-407a-84c6-18e9e09d41af",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "5fbd502e-ada7-4a66-bf41-09fe9b335d9a",
                    "metadata": [
                        {
                            "id": "27b26aa1-fab0-44a6-9f41-5bafc48480a9",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-07-25T17:49:18.827Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchCommerceReviewRequest](../../models/operations/patchcommercereviewrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchCommerceReviewResponse](../../models/operations/patchcommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_social_review

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="patchSocialReview" method="patch" path="/social/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.patch_social_review(request={
        "social_review": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.social_review is not None

    # Handle response
    print(res.social_review)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchSocialReviewRequest](../../models/operations/patchsocialreviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchSocialReviewResponse](../../models/operations/patchsocialreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_review

Remove a review

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceReview" method="delete" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.remove_commerce_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveCommerceReviewRequest](../../models/operations/removecommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveCommerceReviewResponse](../../models/operations/removecommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_review

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceReview" method="put" path="/commerce/{connection_id}/review/{id}" example="commerce_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.update_commerce_review(request={
        "commerce_review": {
            "author_avatar_url": "https://picsum.photos/seed/ix4Br3LA/2245/1245",
            "author_email": "Cleve_Yundt@hotmail.com",
            "author_location": "ipsum",
            "author_name": "Marsha Krajcik",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 26.0,
            "id": "93135370-f2c2-4f01-b2bb-5d84f1480e58",
            "is_featured": True,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Adulescens.",
                    "height": 519.0,
                    "id": "a71e645f-b896-4c75-b7ed-231804e1750a",
                    "metadata": [
                        {
                            "id": "ac9835d9-1cc9-49fb-a1a8-2ad779f81c3f",
                            "slug": "aggero",
                            "value": "tero",
                        },
                    ],
                    "position": 72.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/882/1004?lock=7448492654002422",
                    "width": 75.0,
                },
                {
                    "alt": "Pauci timidus sol comburo thema.",
                    "height": 297.0,
                    "id": "dbe3c1c1-3198-4098-b5a2-682f0295c25b",
                    "metadata": [
                        {
                            "id": "52239305-ea00-407a-84c6-18e9e09d41af",
                            "slug": "vito",
                            "value": "cuppedia",
                        },
                    ],
                    "position": 61.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/3QDZ8/1208/2171",
                    "width": 96.0,
                },
                {
                    "alt": "Cuppedia vestrum patruus.",
                    "height": 6.0,
                    "id": "5fbd502e-ada7-4a66-bf41-09fe9b335d9a",
                    "metadata": [
                        {
                            "id": "27b26aa1-fab0-44a6-9f41-5bafc48480a9",
                            "slug": "arbitro",
                            "value": "villa",
                        },
                    ],
                    "position": 60.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/ytybC/2616/710",
                    "width": 74.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 49.0,
            "updated_at": parse_datetime("2025-07-25T17:49:18.827Z"),
            "url": "https://excitable-underneath.com",
            "verified_purchase": False,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateCommerceReviewRequest](../../models/operations/updatecommercereviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateCommerceReviewResponse](../../models/operations/updatecommercereviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_social_review

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSocialReview" method="put" path="/social/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.update_social_review(request={
        "social_review": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.social_review is not None

    # Handle response
    print(res.social_review)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateSocialReviewRequest](../../models/operations/updatesocialreviewrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateSocialReviewResponse](../../models/operations/updatesocialreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |