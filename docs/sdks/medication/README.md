# Medication

## Overview

### Available Operations

* [get_healthcare_medication](#get_healthcare_medication) - Retrieve a medication
* [list_healthcare_medications](#list_healthcare_medications) - List all medications

## get_healthcare_medication

Retrieve a medication

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareMedication" method="get" path="/healthcare/{connection_id}/medication/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.medication.get_healthcare_medication(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_medication is not None

    # Handle response
    print(res.healthcare_medication)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetHealthcareMedicationRequest](../../models/operations/gethealthcaremedicationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetHealthcareMedicationResponse](../../models/operations/gethealthcaremedicationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_medications

List all medications

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareMedications" method="get" path="/healthcare/{connection_id}/medication" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.medication.list_healthcare_medications(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_medications is not None

    # Handle response
    print(res.healthcare_medications)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListHealthcareMedicationsRequest](../../models/operations/listhealthcaremedicationsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListHealthcareMedicationsResponse](../../models/operations/listhealthcaremedicationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |