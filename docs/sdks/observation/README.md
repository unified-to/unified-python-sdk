# Observation

## Overview

### Available Operations

* [create_healthcare_observation](#create_healthcare_observation) - Create an observation
* [get_healthcare_observation](#get_healthcare_observation) - Retrieve an observation
* [list_healthcare_observations](#list_healthcare_observations) - List all observations

## create_healthcare_observation

Creates a HealthcareObservation. Provide the unified HealthcareObservation fields in the request body; they are mapped to the provider's API. Returns the created HealthcareObservation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHealthcareObservation" method="post" path="/healthcare/{connection_id}/observation" example="healthcare_observation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.observation.create_healthcare_observation(request={
        "healthcare_observation": {
            "codes": [
                {
                    "code": "85354-9",
                    "display": "Blood pressure panel",
                    "system": "http://loinc.org",
                },
            ],
            "components": [
                {
                    "codes": [
                        {
                            "code": "8480-6",
                            "system": "http://loinc.org",
                        },
                    ],
                    "name": "Systolic blood pressure",
                    "value_number": 103.0,
                    "value_unit": "mm[Hg]",
                },
                {
                    "codes": [
                        {
                            "code": "8462-4",
                            "system": "http://loinc.org",
                        },
                    ],
                    "name": "Diastolic blood pressure",
                    "value_number": 60.0,
                    "value_unit": "mm[Hg]",
                },
            ],
            "created_at": parse_datetime("2022-12-06T21:34:04.293Z"),
            "id": "3d95939a-fd15-4205-a9a7-8996dcd8717c",
            "interpretation": shared.Interpretation.CRITICAL_HIGH,
            "issued_at": parse_datetime("2025-05-12T01:23:42.793Z"),
            "metadata": [],
            "name": "Blood pressure panel",
            "observed_at": parse_datetime("2025-01-20T17:02:16.723Z"),
            "status": shared.HealthcareObservationStatus.CORRECTED,
            "type": shared.HealthcareObservationType.VITAL_SIGNS,
            "updated_at": parse_datetime("2026-03-25T02:38:27.139Z"),
        },
        "connection_id": "<id>",
    })

    assert res.healthcare_observation is not None

    # Handle response
    print(res.healthcare_observation)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateHealthcareObservationRequest](../../models/operations/createhealthcareobservationrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateHealthcareObservationResponse](../../models/operations/createhealthcareobservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_healthcare_observation

Retrieves a single HealthcareObservation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareObservation" method="get" path="/healthcare/{connection_id}/observation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.observation.get_healthcare_observation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_observation is not None

    # Handle response
    print(res.healthcare_observation)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetHealthcareObservationRequest](../../models/operations/gethealthcareobservationrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetHealthcareObservationResponse](../../models/operations/gethealthcareobservationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_observations

Returns a list of HealthcareObservations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareObservations" method="get" path="/healthcare/{connection_id}/observation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.observation.list_healthcare_observations(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_observations is not None

    # Handle response
    print(res.healthcare_observations)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListHealthcareObservationsRequest](../../models/operations/listhealthcareobservationsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListHealthcareObservationsResponse](../../models/operations/listhealthcareobservationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |