# Cashflow

## Overview

### Available Operations

* [get_accounting_cashflow](#get_accounting_cashflow) - Retrieve a cashflow
* [list_accounting_cashflows](#list_accounting_cashflows) - List all cashflows

## get_accounting_cashflow

Retrieve a cashflow

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCashflow" method="get" path="/accounting/{connection_id}/cashflow/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cashflow.get_accounting_cashflow(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_cashflow is not None

    # Handle response
    print(res.accounting_cashflow)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountingCashflowRequest](../../models/operations/getaccountingcashflowrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAccountingCashflowResponse](../../models/operations/getaccountingcashflowresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_cashflows

List all cashflows

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCashflows" method="get" path="/accounting/{connection_id}/cashflow" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cashflow.list_accounting_cashflows(request={
        "connection_id": "<id>",
    })

    assert res.accounting_cashflows is not None

    # Handle response
    print(res.accounting_cashflows)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAccountingCashflowsRequest](../../models/operations/listaccountingcashflowsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAccountingCashflowsResponse](../../models/operations/listaccountingcashflowsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |