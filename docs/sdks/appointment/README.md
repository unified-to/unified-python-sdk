# Appointment

## Overview

### Available Operations

* [create_healthcare_appointment](#create_healthcare_appointment) - Create an appointment
* [get_healthcare_appointment](#get_healthcare_appointment) - Retrieve an appointment
* [list_healthcare_appointments](#list_healthcare_appointments) - List all appointments
* [patch_healthcare_appointment](#patch_healthcare_appointment) - Update an appointment
* [remove_healthcare_appointment](#remove_healthcare_appointment) - Remove an appointment
* [update_healthcare_appointment](#update_healthcare_appointment) - Update an appointment

## create_healthcare_appointment

Creates a HealthcareAppointment. Provide the unified HealthcareAppointment fields in the request body; they are mapped to the provider's API. Returns the created HealthcareAppointment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHealthcareAppointment" method="post" path="/healthcare/{connection_id}/appointment" example="healthcare_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.create_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "62d303ae-53b6-4a15-9518-42727558b84f",
            "is_virtual": True,
            "meeting_url": "https://expensive-slipper.name/",
            "metadata": [],
            "notes": "Stabilis triduana colo casus anser ver alo beatus contabesco amiculum.",
            "practitioner_ids": [],
            "service_types": [
                {
                    "code": "12762740",
                    "display": "New patient visit",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2026-09-27T23:23:06.249Z"),
        },
        "connection_id": "<id>",
    })

    assert res.healthcare_appointment is not None

    # Handle response
    print(res.healthcare_appointment)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateHealthcareAppointmentRequest](../../models/operations/createhealthcareappointmentrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateHealthcareAppointmentResponse](../../models/operations/createhealthcareappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_healthcare_appointment

Retrieves a single HealthcareAppointment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareAppointment" method="get" path="/healthcare/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.get_healthcare_appointment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_appointment is not None

    # Handle response
    print(res.healthcare_appointment)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetHealthcareAppointmentRequest](../../models/operations/gethealthcareappointmentrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetHealthcareAppointmentResponse](../../models/operations/gethealthcareappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_appointments

Returns a list of HealthcareAppointments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareAppointments" method="get" path="/healthcare/{connection_id}/appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.list_healthcare_appointments(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_appointments is not None

    # Handle response
    print(res.healthcare_appointments)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListHealthcareAppointmentsRequest](../../models/operations/listhealthcareappointmentsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListHealthcareAppointmentsResponse](../../models/operations/listhealthcareappointmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_healthcare_appointment

Updates the HealthcareAppointment identified by `id`. Provide the unified HealthcareAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHealthcareAppointment" method="patch" path="/healthcare/{connection_id}/appointment/{id}" example="healthcare_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.patch_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "f0326e12-6fc5-4401-b780-1b70f99f01f3",
            "is_virtual": True,
            "meeting_url": "https://expensive-slipper.name/",
            "metadata": [],
            "notes": "Stabilis triduana colo casus anser ver alo beatus contabesco amiculum.",
            "practitioner_ids": [],
            "service_types": [
                {
                    "code": "12762740",
                    "display": "New patient visit",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2026-09-27T23:23:06.273Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_appointment is not None

    # Handle response
    print(res.healthcare_appointment)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchHealthcareAppointmentRequest](../../models/operations/patchhealthcareappointmentrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.PatchHealthcareAppointmentResponse](../../models/operations/patchhealthcareappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_healthcare_appointment

Deletes the HealthcareAppointment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHealthcareAppointment" method="delete" path="/healthcare/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.remove_healthcare_appointment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveHealthcareAppointmentRequest](../../models/operations/removehealthcareappointmentrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveHealthcareAppointmentResponse](../../models/operations/removehealthcareappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_healthcare_appointment

Updates the HealthcareAppointment identified by `id`. Provide the unified HealthcareAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHealthcareAppointment" method="put" path="/healthcare/{connection_id}/appointment/{id}" example="healthcare_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.update_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "f0326e12-6fc5-4401-b780-1b70f99f01f3",
            "is_virtual": True,
            "meeting_url": "https://expensive-slipper.name/",
            "metadata": [],
            "notes": "Stabilis triduana colo casus anser ver alo beatus contabesco amiculum.",
            "practitioner_ids": [],
            "service_types": [
                {
                    "code": "12762740",
                    "display": "New patient visit",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2026-09-27T23:23:06.273Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_appointment is not None

    # Handle response
    print(res.healthcare_appointment)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateHealthcareAppointmentRequest](../../models/operations/updatehealthcareappointmentrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.UpdateHealthcareAppointmentResponse](../../models/operations/updatehealthcareappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |