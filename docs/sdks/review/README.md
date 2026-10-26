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

Creates a CommerceReview. Provide the unified CommerceReview fields in the request body; they are mapped to the provider's API. Returns the created CommerceReview.

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
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "7f303d0d-0092-4bed-8220-5bb0602955ec",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "cfc3476a-b153-4839-b670-814255285bf2",
                    "metadata": [
                        {
                            "id": "9bd1756a-ad10-4b52-99ef-62858c6b0bcd",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "4410505c-3037-45c6-802d-473813853abf",
                    "metadata": [
                        {
                            "id": "971b2c89-9a72-428e-afdf-b41581859a00",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-25T12:57:18.601Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
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

Retrieves a single CommerceReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PerformanceReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single SocialReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of CommerceReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PerformanceReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of SocialReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the CommerceReview identified by `id`. Provide the unified CommerceReview fields to change in the request body.

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
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "48d52e60-40ea-415c-aab3-c75fb44bd534",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "dde6a996-74df-425e-b398-4cc30e975f82",
                    "metadata": [
                        {
                            "id": "e2122dd6-1590-4c59-98d7-099605842053",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "530fe9f8-029e-49e9-9931-abb35f926208",
                    "metadata": [
                        {
                            "id": "ef89cc7e-3a90-4052-8b87-fc9e80e617a7",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-25T12:57:18.627Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
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

Updates the SocialReview identified by `id`. Provide the unified SocialReview fields to change in the request body.

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

Deletes the CommerceReview identified by `id`.

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

Updates the CommerceReview identified by `id`. Provide the unified CommerceReview fields to change in the request body.

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
            "author_avatar_url": "https://loremflickr.com/7/2660?lock=4279109054086693",
            "author_email": "nyasia.macgyver@hotmail.com",
            "author_location": "denique",
            "author_name": "Nyasia MacGyver",
            "comments": [],
            "content": "Taedium thymum adipiscor amicitia cui.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "48d52e60-40ea-415c-aab3-c75fb44bd534",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Desipio carpo sol laudantium colo.",
                    "height": 749.0,
                    "id": "dde6a996-74df-425e-b398-4cc30e975f82",
                    "metadata": [
                        {
                            "id": "e2122dd6-1590-4c59-98d7-099605842053",
                            "slug": "textor",
                            "value": "quos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/196/2041?lock=5845524773114807",
                    "width": 72.0,
                },
                {
                    "alt": "Adopto teneo numquam.",
                    "height": 957.0,
                    "id": "530fe9f8-029e-49e9-9931-abb35f926208",
                    "metadata": [
                        {
                            "id": "ef89cc7e-3a90-4052-8b87-fc9e80e617a7",
                            "slug": "bos",
                            "value": "casso",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://loremflickr.com/1178/2175?lock=5466640101053206",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Coepi adamo amicitia auxilium toties.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-08-25T12:57:18.627Z"),
            "url": "https://diligent-bandwidth.biz",
            "verified_purchase": True,
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

Updates the SocialReview identified by `id`. Provide the unified SocialReview fields to change in the request body.

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