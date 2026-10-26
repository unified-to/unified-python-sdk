# Vendorcredit

## Overview

### Available Operations

* [create_accounting_vendorcredit](#create_accounting_vendorcredit) - Create a vendorcredit
* [get_accounting_vendorcredit](#get_accounting_vendorcredit) - Retrieve a vendorcredit
* [list_accounting_vendorcredits](#list_accounting_vendorcredits) - List all vendorcredits
* [patch_accounting_vendorcredit](#patch_accounting_vendorcredit) - Update a vendorcredit
* [remove_accounting_vendorcredit](#remove_accounting_vendorcredit) - Remove a vendorcredit
* [update_accounting_vendorcredit](#update_accounting_vendorcredit) - Update a vendorcredit

## create_accounting_vendorcredit

Creates a AccountingVendorcredit. Provide the unified AccountingVendorcredit fields in the request body; they are mapped to the provider's API. Returns the created AccountingVendorcredit.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingVendorcredit" method="post" path="/accounting/{connection_id}/vendorcredit" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.create_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "1988c215-66b1-4486-8ab0-77762c6740bb",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-03T17:42:34.878Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingVendorcreditRequest](../../models/operations/createaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.CreateAccountingVendorcreditResponse](../../models/operations/createaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_vendorcredit

Retrieves a single AccountingVendorcredit by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingVendorcredit" method="get" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.get_accounting_vendorcredit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingVendorcreditRequest](../../models/operations/getaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingVendorcreditResponse](../../models/operations/getaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_vendorcredits

Returns a list of AccountingVendorcredits. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingVendorcredits" method="get" path="/accounting/{connection_id}/vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.list_accounting_vendorcredits(request={
        "connection_id": "<id>",
    })

    assert res.accounting_vendorcredits is not None

    # Handle response
    print(res.accounting_vendorcredits)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingVendorcreditsRequest](../../models/operations/listaccountingvendorcreditsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingVendorcreditsResponse](../../models/operations/listaccountingvendorcreditsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_vendorcredit

Updates the AccountingVendorcredit identified by `id`. Provide the unified AccountingVendorcredit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingVendorcredit" method="patch" path="/accounting/{connection_id}/vendorcredit/{id}" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.patch_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "2e3da492-67d0-43a7-b8d5-a33aca9e3a61",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-03T17:42:34.884Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchAccountingVendorcreditRequest](../../models/operations/patchaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.PatchAccountingVendorcreditResponse](../../models/operations/patchaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_vendorcredit

Deletes the AccountingVendorcredit identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingVendorcredit" method="delete" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.remove_accounting_vendorcredit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.RemoveAccountingVendorcreditRequest](../../models/operations/removeaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.RemoveAccountingVendorcreditResponse](../../models/operations/removeaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_vendorcredit

Updates the AccountingVendorcredit identified by `id`. Provide the unified AccountingVendorcredit fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingVendorcredit" method="put" path="/accounting/{connection_id}/vendorcredit/{id}" example="accounting_vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.update_accounting_vendorcredit(request={
        "accounting_vendorcredit": {
            "applications": [],
            "balance_amount": 0.0,
            "created_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "currency": "USD",
            "id": "2e3da492-67d0-43a7-b8d5-a33aca9e3a61",
            "lineitems": [],
            "metadata": [],
            "notes": "Volup conatus cruciamentum decor avaritia.",
            "posted_at": parse_datetime("2023-04-15T21:14:08.197Z"),
            "status": shared.AccountingVendorcreditStatus.AUTHORIZED,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-10-03T17:42:34.884Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_vendorcredit is not None

    # Handle response
    print(res.accounting_vendorcredit)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateAccountingVendorcreditRequest](../../models/operations/updateaccountingvendorcreditrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.UpdateAccountingVendorcreditResponse](../../models/operations/updateaccountingvendorcreditresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |