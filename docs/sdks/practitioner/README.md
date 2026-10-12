# Practitioner

## Overview

### Available Operations

* [get_healthcare_practitioner](#get_healthcare_practitioner) - Retrieve a practitioner
* [list_healthcare_practitioners](#list_healthcare_practitioners) - List all practitioners

## get_healthcare_practitioner

Retrieve a practitioner

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcarePractitioner" method="get" path="/healthcare/{connection_id}/practitioner/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practitioner.get_healthcare_practitioner(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_practitioner is not None

    # Handle response
    print(res.healthcare_practitioner)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetHealthcarePractitionerRequest](../../models/operations/gethealthcarepractitionerrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetHealthcarePractitionerResponse](../../models/operations/gethealthcarepractitionerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_practitioners

List all practitioners

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcarePractitioners" method="get" path="/healthcare/{connection_id}/practitioner" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.practitioner.list_healthcare_practitioners(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_practitioners is not None

    # Handle response
    print(res.healthcare_practitioners)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListHealthcarePractitionersRequest](../../models/operations/listhealthcarepractitionersrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListHealthcarePractitionersResponse](../../models/operations/listhealthcarepractitionersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |