# Cashflow

## Overview

### Available Operations

* [get_accounting_cashflow2](#get_accounting_cashflow2) - Retrieve a cashflow
* [list_accounting_cashflows2](#list_accounting_cashflows2) - List all cashflows

## get_accounting_cashflow2

Retrieve a cashflow

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCashflow2" method="get" path="/accounting/{connection_id}/cashflow/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cashflow.get_accounting_cashflow2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_cashflow is not None

    # Handle response
    print(res.accounting_cashflow)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAccountingCashflow2Request](../../models/operations/getaccountingcashflow2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetAccountingCashflow2Response](../../models/operations/getaccountingcashflow2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_cashflows2

List all cashflows

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCashflows2" method="get" path="/accounting/{connection_id}/cashflow" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cashflow.list_accounting_cashflows2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_cashflows is not None

    # Handle response
    print(res.accounting_cashflows)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListAccountingCashflows2Request](../../models/operations/listaccountingcashflows2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListAccountingCashflows2Response](../../models/operations/listaccountingcashflows2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |