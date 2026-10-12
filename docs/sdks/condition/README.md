# Condition

## Overview

### Available Operations

* [get_healthcare_condition](#get_healthcare_condition) - Retrieve a condition
* [list_healthcare_conditions](#list_healthcare_conditions) - List all conditions

## get_healthcare_condition

Retrieve a condition

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareCondition" method="get" path="/healthcare/{connection_id}/condition/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.condition.get_healthcare_condition(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_condition is not None

    # Handle response
    print(res.healthcare_condition)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetHealthcareConditionRequest](../../models/operations/gethealthcareconditionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetHealthcareConditionResponse](../../models/operations/gethealthcareconditionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_conditions

List all conditions

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareConditions" method="get" path="/healthcare/{connection_id}/condition" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.condition.list_healthcare_conditions(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_conditions is not None

    # Handle response
    print(res.healthcare_conditions)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListHealthcareConditionsRequest](../../models/operations/listhealthcareconditionsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListHealthcareConditionsResponse](../../models/operations/listhealthcareconditionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |