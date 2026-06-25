# Transaction

## Overview

### Available Operations

* [create_accounting_transaction2](#create_accounting_transaction2) - Create a transaction
* [get_accounting_transaction2](#get_accounting_transaction2) - Retrieve a transaction
* [list_accounting_transactions2](#list_accounting_transactions2) - List all transactions
* [patch_accounting_transaction2](#patch_accounting_transaction2) - Update a transaction
* [remove_accounting_transaction2](#remove_accounting_transaction2) - Remove a transaction
* [update_accounting_transaction2](#update_accounting_transaction2) - Update a transaction

## create_accounting_transaction2

Create a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingTransaction2" method="post" path="/accounting/{connection_id}/transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.create_accounting_transaction2(request={
        "accounting_transaction": {},
        "connection_id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingTransaction2Request](../../models/operations/createaccountingtransaction2request.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.CreateAccountingTransaction2Response](../../models/operations/createaccountingtransaction2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_transaction2

Retrieve a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingTransaction2" method="get" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.get_accounting_transaction2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingTransaction2Request](../../models/operations/getaccountingtransaction2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetAccountingTransaction2Response](../../models/operations/getaccountingtransaction2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_transactions2

List all transactions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingTransactions2" method="get" path="/accounting/{connection_id}/transaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.list_accounting_transactions2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_transactions is not None

    # Handle response
    print(res.accounting_transactions)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingTransactions2Request](../../models/operations/listaccountingtransactions2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingTransactions2Response](../../models/operations/listaccountingtransactions2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_transaction2

Update a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingTransaction2" method="patch" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.patch_accounting_transaction2(request={
        "accounting_transaction": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchAccountingTransaction2Request](../../models/operations/patchaccountingtransaction2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.PatchAccountingTransaction2Response](../../models/operations/patchaccountingtransaction2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_transaction2

Remove a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingTransaction2" method="delete" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.remove_accounting_transaction2(request={
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
| `request`                                                                                                        | [operations.RemoveAccountingTransaction2Request](../../models/operations/removeaccountingtransaction2request.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.RemoveAccountingTransaction2Response](../../models/operations/removeaccountingtransaction2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_transaction2

Update a transaction

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingTransaction2" method="put" path="/accounting/{connection_id}/transaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.transaction.update_accounting_transaction2(request={
        "accounting_transaction": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_transaction is not None

    # Handle response
    print(res.accounting_transaction)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateAccountingTransaction2Request](../../models/operations/updateaccountingtransaction2request.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.UpdateAccountingTransaction2Response](../../models/operations/updateaccountingtransaction2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |