# Encounter

## Overview

### Available Operations

* [get_healthcare_encounter](#get_healthcare_encounter) - Retrieve an encounter
* [list_healthcare_encounters](#list_healthcare_encounters) - List all encounters

## get_healthcare_encounter

Retrieve an encounter

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareEncounter" method="get" path="/healthcare/{connection_id}/encounter/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.encounter.get_healthcare_encounter(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_encounter is not None

    # Handle response
    print(res.healthcare_encounter)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetHealthcareEncounterRequest](../../models/operations/gethealthcareencounterrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetHealthcareEncounterResponse](../../models/operations/gethealthcareencounterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_encounters

List all encounters

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareEncounters" method="get" path="/healthcare/{connection_id}/encounter" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.encounter.list_healthcare_encounters(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_encounters is not None

    # Handle response
    print(res.healthcare_encounters)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListHealthcareEncountersRequest](../../models/operations/listhealthcareencountersrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListHealthcareEncountersResponse](../../models/operations/listhealthcareencountersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |