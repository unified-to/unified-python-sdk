# Category

## Overview

### Available Operations

* [create_accounting_category2](#create_accounting_category2) - Create a category
* [create_ticketing_category2](#create_ticketing_category2) - Create a category
* [get_accounting_category2](#get_accounting_category2) - Retrieve a category
* [get_ticketing_category2](#get_ticketing_category2) - Retrieve a category
* [list_accounting_categories2](#list_accounting_categories2) - List all categories
* [list_ticketing_categories2](#list_ticketing_categories2) - List all categories
* [patch_accounting_category2](#patch_accounting_category2) - Update a category
* [patch_ticketing_category2](#patch_ticketing_category2) - Update a category
* [remove_accounting_category2](#remove_accounting_category2) - Remove a category
* [remove_ticketing_category2](#remove_ticketing_category2) - Remove a category
* [update_accounting_category2](#update_accounting_category2) - Update a category
* [update_ticketing_category2](#update_ticketing_category2) - Update a category

## create_accounting_category2

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCategory2" method="post" path="/accounting/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.create_accounting_category2(request={
        "accounting_category": {},
        "connection_id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateAccountingCategory2Request](../../models/operations/createaccountingcategory2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreateAccountingCategory2Response](../../models/operations/createaccountingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_ticketing_category2

Create a category

### Example Usage

<!-- UsageSnippet language="python" operationID="createTicketingCategory2" method="post" path="/ticketing/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.create_ticketing_category2(request={
        "ticketing_category": {},
        "connection_id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateTicketingCategory2Request](../../models/operations/createticketingcategory2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateTicketingCategory2Response](../../models/operations/createticketingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_category2

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCategory2" method="get" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.get_accounting_category2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAccountingCategory2Request](../../models/operations/getaccountingcategory2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetAccountingCategory2Response](../../models/operations/getaccountingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ticketing_category2

Retrieve a category

### Example Usage

<!-- UsageSnippet language="python" operationID="getTicketingCategory2" method="get" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.get_ticketing_category2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetTicketingCategory2Request](../../models/operations/getticketingcategory2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetTicketingCategory2Response](../../models/operations/getticketingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_categories2

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCategories2" method="get" path="/accounting/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.list_accounting_categories2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_categories is not None

    # Handle response
    print(res.accounting_categories)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListAccountingCategories2Request](../../models/operations/listaccountingcategories2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListAccountingCategories2Response](../../models/operations/listaccountingcategories2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ticketing_categories2

List all categories

### Example Usage

<!-- UsageSnippet language="python" operationID="listTicketingCategories2" method="get" path="/ticketing/{connection_id}/category" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.list_ticketing_categories2(request={
        "connection_id": "<id>",
    })

    assert res.ticketing_categories is not None

    # Handle response
    print(res.ticketing_categories)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListTicketingCategories2Request](../../models/operations/listticketingcategories2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListTicketingCategories2Response](../../models/operations/listticketingcategories2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_category2

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCategory2" method="patch" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.patch_accounting_category2(request={
        "accounting_category": {},
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
| `request`                                                                                                | [operations.PatchAccountingCategory2Request](../../models/operations/patchaccountingcategory2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PatchAccountingCategory2Response](../../models/operations/patchaccountingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ticketing_category2

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="patchTicketingCategory2" method="patch" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.patch_ticketing_category2(request={
        "ticketing_category": {},
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
| `request`                                                                                              | [operations.PatchTicketingCategory2Request](../../models/operations/patchticketingcategory2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchTicketingCategory2Response](../../models/operations/patchticketingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_category2

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCategory2" method="delete" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.remove_accounting_category2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveAccountingCategory2Request](../../models/operations/removeaccountingcategory2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.RemoveAccountingCategory2Response](../../models/operations/removeaccountingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ticketing_category2

Remove a category

### Example Usage

<!-- UsageSnippet language="python" operationID="removeTicketingCategory2" method="delete" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.remove_ticketing_category2(request={
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
| `request`                                                                                                | [operations.RemoveTicketingCategory2Request](../../models/operations/removeticketingcategory2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveTicketingCategory2Response](../../models/operations/removeticketingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_category2

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCategory2" method="put" path="/accounting/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.update_accounting_category2(request={
        "accounting_category": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_category is not None

    # Handle response
    print(res.accounting_category)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateAccountingCategory2Request](../../models/operations/updateaccountingcategory2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UpdateAccountingCategory2Response](../../models/operations/updateaccountingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ticketing_category2

Update a category

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTicketingCategory2" method="put" path="/ticketing/{connection_id}/category/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.category.update_ticketing_category2(request={
        "ticketing_category": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ticketing_category is not None

    # Handle response
    print(res.ticketing_category)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateTicketingCategory2Request](../../models/operations/updateticketingcategory2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateTicketingCategory2Response](../../models/operations/updateticketingcategory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |