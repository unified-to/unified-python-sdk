# Review

## Overview

### Available Operations

* [create_commerce_review2](#create_commerce_review2) - Create a review
* [get_commerce_review2](#get_commerce_review2) - Retrieve a review
* [list_commerce_reviews2](#list_commerce_reviews2) - List all reviews
* [patch_commerce_review2](#patch_commerce_review2) - Update a review
* [remove_commerce_review2](#remove_commerce_review2) - Remove a review
* [update_commerce_review2](#update_commerce_review2) - Update a review

## create_commerce_review2

Create a review

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceReview2" method="post" path="/commerce/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.create_commerce_review2(request={
        "commerce_review": {},
        "connection_id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateCommerceReview2Request](../../models/operations/createcommercereview2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateCommerceReview2Response](../../models/operations/createcommercereview2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_review2

Retrieve a review

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceReview2" method="get" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.get_commerce_review2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetCommerceReview2Request](../../models/operations/getcommercereview2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetCommerceReview2Response](../../models/operations/getcommercereview2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_reviews2

List all reviews

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceReviews2" method="get" path="/commerce/{connection_id}/review" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.list_commerce_reviews2(request={
        "connection_id": "<id>",
    })

    assert res.commerce_reviews is not None

    # Handle response
    print(res.commerce_reviews)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListCommerceReviews2Request](../../models/operations/listcommercereviews2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListCommerceReviews2Response](../../models/operations/listcommercereviews2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_review2

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceReview2" method="patch" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.patch_commerce_review2(request={
        "commerce_review": {},
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
| `request`                                                                                        | [operations.PatchCommerceReview2Request](../../models/operations/patchcommercereview2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchCommerceReview2Response](../../models/operations/patchcommercereview2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_review2

Remove a review

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceReview2" method="delete" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.remove_commerce_review2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveCommerceReview2Request](../../models/operations/removecommercereview2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveCommerceReview2Response](../../models/operations/removecommercereview2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_review2

Update a review

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceReview2" method="put" path="/commerce/{connection_id}/review/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.review.update_commerce_review2(request={
        "commerce_review": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_review is not None

    # Handle response
    print(res.commerce_review)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateCommerceReview2Request](../../models/operations/updatecommercereview2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateCommerceReview2Response](../../models/operations/updatecommercereview2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |