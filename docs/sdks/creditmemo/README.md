# Creditmemo

## Overview

### Available Operations

* [create_accounting_creditmemo2](#create_accounting_creditmemo2) - Create a creditmemo
* [get_accounting_creditmemo2](#get_accounting_creditmemo2) - Retrieve a creditmemo
* [list_accounting_creditmemoes2](#list_accounting_creditmemoes2) - List all creditmemoes
* [patch_accounting_creditmemo2](#patch_accounting_creditmemo2) - Update a creditmemo
* [remove_accounting_creditmemo2](#remove_accounting_creditmemo2) - Remove a creditmemo
* [update_accounting_creditmemo2](#update_accounting_creditmemo2) - Update a creditmemo

## create_accounting_creditmemo2

Create a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCreditmemo2" method="post" path="/accounting/{connection_id}/creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.create_accounting_creditmemo2(request={
        "accounting_creditmemo": {},
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAccountingCreditmemo2Request](../../models/operations/createaccountingcreditmemo2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateAccountingCreditmemo2Response](../../models/operations/createaccountingcreditmemo2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_creditmemo2

Retrieve a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCreditmemo2" method="get" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.get_accounting_creditmemo2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingCreditmemo2Request](../../models/operations/getaccountingcreditmemo2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingCreditmemo2Response](../../models/operations/getaccountingcreditmemo2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_creditmemoes2

List all creditmemoes

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCreditmemoes2" method="get" path="/accounting/{connection_id}/creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.list_accounting_creditmemoes2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemoes is not None

    # Handle response
    print(res.accounting_creditmemoes)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListAccountingCreditmemoes2Request](../../models/operations/listaccountingcreditmemoes2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListAccountingCreditmemoes2Response](../../models/operations/listaccountingcreditmemoes2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_creditmemo2

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCreditmemo2" method="patch" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.patch_accounting_creditmemo2(request={
        "accounting_creditmemo": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAccountingCreditmemo2Request](../../models/operations/patchaccountingcreditmemo2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.PatchAccountingCreditmemo2Response](../../models/operations/patchaccountingcreditmemo2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_creditmemo2

Remove a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCreditmemo2" method="delete" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.remove_accounting_creditmemo2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveAccountingCreditmemo2Request](../../models/operations/removeaccountingcreditmemo2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveAccountingCreditmemo2Response](../../models/operations/removeaccountingcreditmemo2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_creditmemo2

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCreditmemo2" method="put" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.update_accounting_creditmemo2(request={
        "accounting_creditmemo": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateAccountingCreditmemo2Request](../../models/operations/updateaccountingcreditmemo2request.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.UpdateAccountingCreditmemo2Response](../../models/operations/updateaccountingcreditmemo2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |