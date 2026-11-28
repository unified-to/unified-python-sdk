# Review

## Overview

### Available Operations

* [create_commerce_review](#create_commerce_review) - Create a review
* [get_commerce_review](#get_commerce_review) - Retrieve a review
* [get_performance_review](#get_performance_review) - Retrieve a review
* [get_property_review](#get_property_review) - Retrieve a review
* [get_social_review](#get_social_review) - Retrieve a review
* [list_commerce_reviews](#list_commerce_reviews) - List all reviews
* [list_performance_reviews](#list_performance_reviews) - List all reviews
* [list_property_reviews](#list_property_reviews) - List all reviews
* [list_social_reviews](#list_social_reviews) - List all reviews
* [patch_commerce_review](#patch_commerce_review) - Update a review
* [patch_property_review](#patch_property_review) - Update a review
* [patch_social_review](#patch_social_review) - Update a review
* [remove_commerce_review](#remove_commerce_review) - Remove a review
* [update_commerce_review](#update_commerce_review) - Update a review
* [update_property_review](#update_property_review) - Update a review
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
            "author_avatar_url": "https://picsum.photos/seed/jt3vcEZv/1605/7",
            "author_email": "jovan.bartell@hotmail.com",
            "author_location": "comburo",
            "author_name": "Jovan Bartell",
            "comments": [],
            "content": "Vix taedium thymum adipiscor amicitia.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "b1d556b4-9b74-4eb2-a17d-c9431d478ca2",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Teneo.",
                    "height": 749.0,
                    "id": "36641fea-f271-47b7-96ce-d983e980730b",
                    "metadata": [
                        {
                            "id": "eb8184d7-eb9c-4675-b216-b41e2d22a3e5",
                            "slug": "numquam",
                            "value": "bos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/jNDix4Br/995/2602",
                    "width": 72.0,
                },
                {
                    "alt": "Ratione vulticulus arbitro ultio pauci.",
                    "height": 957.0,
                    "id": "7eed467d-d728-4c77-9595-efd1662d63c5",
                    "metadata": [
                        {
                            "id": "e9bed246-c5a7-410d-9a2e-ab9c764bd5a9",
                            "slug": "timidus",
                            "value": "sol",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/b35MixS23/1004/1925",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Auxilium.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-09-21T21:59:32.313Z"),
            "url": "https://whispered-hawk.name",
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

## get_property_review

Retrieves a single PropertyReview by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyReview" method="get" path="/property/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.get_property_review(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPropertyReviewRequest](../../models/operations/getpropertyreviewrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetPropertyReviewResponse](../../models/operations/getpropertyreviewresponse.md)**

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

## list_property_reviews

Returns a list of PropertyReviews. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyReviews" method="get" path="/property/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.list_property_reviews(request={
        "connection_id": "<id>",
    })

    assert res.property_reviews is not None

    # Handle response
    print(res.property_reviews)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListPropertyReviewsRequest](../../models/operations/listpropertyreviewsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListPropertyReviewsResponse](../../models/operations/listpropertyreviewsresponse.md)**

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
            "author_avatar_url": "https://picsum.photos/seed/jt3vcEZv/1605/7",
            "author_email": "jovan.bartell@hotmail.com",
            "author_location": "comburo",
            "author_name": "Jovan Bartell",
            "comments": [],
            "content": "Vix taedium thymum adipiscor amicitia.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "67bf1a80-c4bb-4c8c-b829-d555a79eb710",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Teneo.",
                    "height": 749.0,
                    "id": "028e0a1a-1269-4024-8ace-69d2cad1bc23",
                    "metadata": [
                        {
                            "id": "889ffb4c-0faf-4571-8e77-34e5ec8e1c9c",
                            "slug": "numquam",
                            "value": "bos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/jNDix4Br/995/2602",
                    "width": 72.0,
                },
                {
                    "alt": "Ratione vulticulus arbitro ultio pauci.",
                    "height": 957.0,
                    "id": "d6dd1202-9328-4ae5-b47a-93a6ac90c7fd",
                    "metadata": [
                        {
                            "id": "44d2f025-b755-4f86-8d31-6b75cf1bea68",
                            "slug": "timidus",
                            "value": "sol",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/b35MixS23/1004/1925",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Auxilium.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-09-21T21:59:32.347Z"),
            "url": "https://whispered-hawk.name",
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

## patch_property_review

Updates the PropertyReview identified by `id`. Provide the unified PropertyReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPropertyReview" method="patch" path="/property/{connection_id}/review/{id}" example="property_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.patch_property_review(request={
        "property_review": {
            "author_name": "Hilma Volkman",
            "category_ratings": [
                {
                    "category": shared.PropertyCategoryratingCategory.CLEANLINESS,
                    "comment": "Sum blanditiis terreo adinventitias capitulus dolorem verus studio voluptates temperantia.",
                    "rating": 5.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.ACCURACY,
                    "comment": "Avarus caelum curvo utor odit arcesso quisquam.",
                    "rating": 4.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.COMMUNICATION,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.CHECKIN,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.LOCATION,
                    "rating": 2.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.VALUE,
                    "comment": "Iusto artificiose odit nemo sui.",
                    "rating": 5.0,
                },
            ],
            "content": "Attonbitus comitatus auditor. Tergo nostrum deleo vomica comprehendo tertius summopere. Apparatus incidunt tabula pauci confido colo fugiat umquam perferendis amitto.",
            "created_at": parse_datetime("2022-10-17T11:17:07.682Z"),
            "id": "2193330a-422e-4c0f-b8c9-431a2e6c508f",
            "is_public": True,
            "metadata": [],
            "private_feedback": "Patria stella magni.",
            "rating": 3.0,
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-03-14T09:33:57.490Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchPropertyReviewRequest](../../models/operations/patchpropertyreviewrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchPropertyReviewResponse](../../models/operations/patchpropertyreviewresponse.md)**

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
            "author_avatar_url": "https://picsum.photos/seed/jt3vcEZv/1605/7",
            "author_email": "jovan.bartell@hotmail.com",
            "author_location": "comburo",
            "author_name": "Jovan Bartell",
            "comments": [],
            "content": "Vix taedium thymum adipiscor amicitia.",
            "created_at": parse_datetime("2019-12-12T18:10:22.988Z"),
            "helpful_votes": 66.0,
            "id": "67bf1a80-c4bb-4c8c-b829-d555a79eb710",
            "is_featured": False,
            "is_public": True,
            "is_verified": False,
            "media": [
                {
                    "alt": "Teneo.",
                    "height": 749.0,
                    "id": "028e0a1a-1269-4024-8ace-69d2cad1bc23",
                    "metadata": [
                        {
                            "id": "889ffb4c-0faf-4571-8e77-34e5ec8e1c9c",
                            "slug": "numquam",
                            "value": "bos",
                        },
                    ],
                    "position": 29.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://picsum.photos/seed/jNDix4Br/995/2602",
                    "width": 72.0,
                },
                {
                    "alt": "Ratione vulticulus arbitro ultio pauci.",
                    "height": 957.0,
                    "id": "d6dd1202-9328-4ae5-b47a-93a6ac90c7fd",
                    "metadata": [
                        {
                            "id": "44d2f025-b755-4f86-8d31-6b75cf1bea68",
                            "slug": "timidus",
                            "value": "sol",
                        },
                    ],
                    "position": 69.0,
                    "type": shared.CommerceItemMediaType.IMAGE,
                    "url": "https://picsum.photos/seed/b35MixS23/1004/1925",
                    "width": 61.0,
                },
            ],
            "metadata": [],
            "rating": 3.0,
            "status": shared.CommerceReviewStatus.APPROVED,
            "title": "Auxilium.",
            "unhelpful_votes": 88.0,
            "updated_at": parse_datetime("2025-09-21T21:59:32.347Z"),
            "url": "https://whispered-hawk.name",
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

## update_property_review

Updates the PropertyReview identified by `id`. Provide the unified PropertyReview fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePropertyReview" method="put" path="/property/{connection_id}/review/{id}" example="property_review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.update_property_review(request={
        "property_review": {
            "author_name": "Hilma Volkman",
            "category_ratings": [
                {
                    "category": shared.PropertyCategoryratingCategory.CLEANLINESS,
                    "comment": "Sum blanditiis terreo adinventitias capitulus dolorem verus studio voluptates temperantia.",
                    "rating": 5.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.ACCURACY,
                    "comment": "Avarus caelum curvo utor odit arcesso quisquam.",
                    "rating": 4.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.COMMUNICATION,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.CHECKIN,
                    "rating": 1.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.LOCATION,
                    "rating": 2.0,
                },
                {
                    "category": shared.PropertyCategoryratingCategory.VALUE,
                    "comment": "Iusto artificiose odit nemo sui.",
                    "rating": 5.0,
                },
            ],
            "content": "Attonbitus comitatus auditor. Tergo nostrum deleo vomica comprehendo tertius summopere. Apparatus incidunt tabula pauci confido colo fugiat umquam perferendis amitto.",
            "created_at": parse_datetime("2022-10-17T11:17:07.682Z"),
            "id": "2193330a-422e-4c0f-b8c9-431a2e6c508f",
            "is_public": True,
            "metadata": [],
            "private_feedback": "Patria stella magni.",
            "rating": 3.0,
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-03-14T09:33:57.490Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_review is not None

    # Handle response
    print(res.property_review)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdatePropertyReviewRequest](../../models/operations/updatepropertyreviewrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdatePropertyReviewResponse](../../models/operations/updatepropertyreviewresponse.md)**

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