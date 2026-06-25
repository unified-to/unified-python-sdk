# Trialbalance

## Overview

### Available Operations

* [get_accounting_trialbalance2](#get_accounting_trialbalance2) - Retrieve a trialbalance
* [list_accounting_trialbalances2](#list_accounting_trialbalances2) - List all trialbalances

## get_accounting_trialbalance2

Retrieve a trialbalance

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingTrialbalance2" method="get" path="/accounting/{connection_id}/trialbalance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.trialbalance.get_accounting_trialbalance2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_trialbalance is not None

    # Handle response
    print(res.accounting_trialbalance)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingTrialbalance2Request](../../models/operations/getaccountingtrialbalance2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetAccountingTrialbalance2Response](../../models/operations/getaccountingtrialbalance2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_trialbalances2

List all trialbalances

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingTrialbalances2" method="get" path="/accounting/{connection_id}/trialbalance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.trialbalance.list_accounting_trialbalances2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_trialbalances is not None

    # Handle response
    print(res.accounting_trialbalances)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingTrialbalances2Request](../../models/operations/listaccountingtrialbalances2request.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.ListAccountingTrialbalances2Response](../../models/operations/listaccountingtrialbalances2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |