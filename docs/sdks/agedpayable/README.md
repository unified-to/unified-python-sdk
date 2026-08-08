# Agedpayable

## Overview

### Available Operations

* [get_accounting_agedpayable](#get_accounting_agedpayable) - Retrieve an agedpayable
* [list_accounting_agedpayables](#list_accounting_agedpayables) - List all agedpayables

## get_accounting_agedpayable

Retrieve an agedpayable

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingAgedpayable" method="get" path="/accounting/{connection_id}/agedpayable/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agedpayable.get_accounting_agedpayable(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_agedpayable is not None

    # Handle response
    print(res.accounting_agedpayable)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingAgedpayableRequest](../../models/operations/getaccountingagedpayablerequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingAgedpayableResponse](../../models/operations/getaccountingagedpayableresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_agedpayables

List all agedpayables

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingAgedpayables" method="get" path="/accounting/{connection_id}/agedpayable" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.agedpayable.list_accounting_agedpayables(request={
        "connection_id": "<id>",
    })

    assert res.accounting_agedpayables is not None

    # Handle response
    print(res.accounting_agedpayables)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingAgedpayablesRequest](../../models/operations/listaccountingagedpayablesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingAgedpayablesResponse](../../models/operations/listaccountingagedpayablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |