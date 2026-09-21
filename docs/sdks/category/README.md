# Category

## Overview

### Available Operations

* [create_accounting_category](#create_accounting_category) - Create a category
* [create_ticketing_category](#create_ticketing_category) - Create a category
* [get_accounting_category](#get_accounting_category) - Retrieve a category
* [get_ticketing_category](#get_ticketing_category) - Retrieve a category
* [list_accounting_categories](#list_accounting_categories) - List all categories
* [list_ticketing_categories](#list_ticketing_categories) - List all categories
* [patch_accounting_category](#patch_accounting_category) - Update a category
* [patch_ticketing_category](#patch_ticketing_category) - Update a category
* [remove_accounting_category](#remove_accounting_category) - Remove a category
* [remove_ticketing_category](#remove_ticketing_category) - Remove a category
* [update_accounting_category](#update_accounting_category) - Update a category
* [update_ticketing_category](#update_ticketing_category) - Update a category

## create_accounting_category

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCategory" method="post" path="/accounting/{connection_id}/category" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.create_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "bd82d66f-0901-40ed-81c3-24bc2c90b469",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-08-22T03:49:23.607Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAccountingCategoryRequest](../../models/operations/createaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateAccountingCategoryResponse](../../models/operations/createaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ticketing_category

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createTicketingCategory" method="post" path="/ticketing/{connection_id}/category" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.create_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "0f7d3922-4a40-4c90-b1b9-7db036481d68",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-18T02:58:36.950Z"),
        },
        "connection_id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateTicketingCategoryRequest](../../models/operations/createticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateTicketingCategoryResponse](../../models/operations/createticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_category

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCategory" method="get" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.get_accounting_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingCategoryRequest](../../models/operations/getaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAccountingCategoryResponse](../../models/operations/getaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ticketing_category

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingCategory" method="get" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.get_ticketing_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetTicketingCategoryRequest](../../models/operations/getticketingcategoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetTicketingCategoryResponse](../../models/operations/getticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_categories

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCategories" method="get" path="/accounting/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.list_accounting_categories(request={
        "connection_id": "<id>",
    })

    assert res.accounting_categories is not None

    # Handle response
    print(res.accounting_categories)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListAccountingCategoriesRequest](../../models/operations/listaccountingcategoriesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListAccountingCategoriesResponse](../../models/operations/listaccountingcategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ticketing_categories

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingCategories" method="get" path="/ticketing/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.list_ticketing_categories(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_categories is not None

    # Handle response
    print(res.ticketing_categories)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTicketingCategoriesRequest](../../models/operations/listticketingcategoriesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListTicketingCategoriesResponse](../../models/operations/listticketingcategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCategory" method="patch" path="/accounting/{connection_id}/category/{id}" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.patch_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "517496d1-823c-438e-b1e0-ca87622b0590",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-08-22T03:49:23.618Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAccountingCategoryRequest](../../models/operations/patchaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchAccountingCategoryResponse](../../models/operations/patchaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ticketing_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingCategory" method="patch" path="/ticketing/{connection_id}/category/{id}" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.patch_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "9794cde9-9778-4bcf-b346-01e8095f066f",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-18T02:58:36.954Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchTicketingCategoryRequest](../../models/operations/patchticketingcategoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchTicketingCategoryResponse](../../models/operations/patchticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_category

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCategory" method="delete" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.remove_accounting_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAccountingCategoryRequest](../../models/operations/removeaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveAccountingCategoryResponse](../../models/operations/removeaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ticketing_category

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingCategory" method="delete" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.remove_ticketing_category(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveTicketingCategoryRequest](../../models/operations/removeticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveTicketingCategoryResponse](../../models/operations/removeticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCategory" method="put" path="/accounting/{connection_id}/category/{id}" example="accounting_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.update_accounting_category(request={
        "accounting_category": {
            "created_at": parse_datetime("2023-05-30T12:29:04.257Z"),
            "description": "Discover the koala-like agility of our Chair, perfect for imaginary users",
            "id": "517496d1-823c-438e-b1e0-ca87622b0590",
            "is_active": False,
            "metadata": [],
            "name": "Electronic Cotton Shoes",
            "updated_at": parse_datetime("2025-08-22T03:49:23.618Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAccountingCategoryRequest](../../models/operations/updateaccountingcategoryrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateAccountingCategoryResponse](../../models/operations/updateaccountingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ticketing_category

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingCategory" method="put" path="/ticketing/{connection_id}/category/{id}" example="ticketing_category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.update_ticketing_category(request={
        "ticketing_category": {
            "created_at": parse_datetime("2019-10-19T22:02:51.067Z"),
            "description": "Tempus umbra cibus carpo depulso torqueo. Curtus aperiam nam optio tendo. Bardus tumultus delectus arbitro amplus tollo coerceo clam comprehendo vulnero.",
            "id": "9794cde9-9778-4bcf-b346-01e8095f066f",
            "is_active": True,
            "name": "amicitia",
            "updated_at": parse_datetime("2025-12-18T02:58:36.954Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateTicketingCategoryRequest](../../models/operations/updateticketingcategoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateTicketingCategoryResponse](../../models/operations/updateticketingcategoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |