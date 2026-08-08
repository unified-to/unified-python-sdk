# Agedreceivable

## Overview

### Available Operations

* [get_accounting_agedreceivable](#get_accounting_agedreceivable) - Retrieve an agedreceivable
* [list_accounting_agedreceivables](#list_accounting_agedreceivables) - List all agedreceivables

## get_accounting_agedreceivable

Retrieve an agedreceivable

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingAgedreceivable" method="get" path="/accounting/{connection_id}/agedreceivable/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agedreceivable.get_accounting_agedreceivable(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_agedreceivable is not None

    # Handle response
    print(res.accounting_agedreceivable)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAccountingAgedreceivableRequest](../../models/operations/getaccountingagedreceivablerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.GetAccountingAgedreceivableResponse](../../models/operations/getaccountingagedreceivableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_agedreceivables

List all agedreceivables

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingAgedreceivables" method="get" path="/accounting/{connection_id}/agedreceivable" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agedreceivable.list_accounting_agedreceivables(request={
        "connection_id": "<id>",
    })

    assert res.accounting_agedreceivables is not None

    # Handle response
    print(res.accounting_agedreceivables)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.ListAccountingAgedreceivablesRequest](../../models/operations/listaccountingagedreceivablesrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.ListAccountingAgedreceivablesResponse](../../models/operations/listaccountingagedreceivablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |