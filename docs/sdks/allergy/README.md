# Allergy

## Overview

### Available Operations

* [get_healthcare_allergy](#get_healthcare_allergy) - Retrieve an allergy
* [list_healthcare_allergies](#list_healthcare_allergies) - List all allergies

## get_healthcare_allergy

Retrieve an allergy

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareAllergy" method="get" path="/healthcare/{connection_id}/allergy/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.allergy.get_healthcare_allergy(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_allergy is not None

    # Handle response
    print(res.healthcare_allergy)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetHealthcareAllergyRequest](../../models/operations/gethealthcareallergyrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetHealthcareAllergyResponse](../../models/operations/gethealthcareallergyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_allergies

List all allergies

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareAllergies" method="get" path="/healthcare/{connection_id}/allergy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.allergy.list_healthcare_allergies(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_allergies is not None

    # Handle response
    print(res.healthcare_allergies)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListHealthcareAllergiesRequest](../../models/operations/listhealthcareallergiesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListHealthcareAllergiesResponse](../../models/operations/listhealthcareallergiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |