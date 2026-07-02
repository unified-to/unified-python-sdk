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

Create a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingVendorcredit" method="post" path="/accounting/{connection_id}/vendorcredit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.create_accounting_vendorcredit(request={
        "accounting_vendorcredit": {},
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

Retrieve a vendorcredit

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

List all vendorcredits

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

Update a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingVendorcredit" method="patch" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.patch_accounting_vendorcredit(request={
        "accounting_vendorcredit": {},
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

Remove a vendorcredit

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

Update a vendorcredit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingVendorcredit" method="put" path="/accounting/{connection_id}/vendorcredit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.vendorcredit.update_accounting_vendorcredit(request={
        "accounting_vendorcredit": {},
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