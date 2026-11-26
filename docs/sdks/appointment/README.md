# Appointment

## Overview

### Available Operations

* [create_dms_appointment](#create_dms_appointment) - Create an appointment
* [create_healthcare_appointment](#create_healthcare_appointment) - Create an appointment
* [get_dms_appointment](#get_dms_appointment) - Retrieve an appointment
* [get_healthcare_appointment](#get_healthcare_appointment) - Retrieve an appointment
* [list_dms_appointments](#list_dms_appointments) - List all appointments
* [list_healthcare_appointments](#list_healthcare_appointments) - List all appointments
* [patch_dms_appointment](#patch_dms_appointment) - Update an appointment
* [patch_healthcare_appointment](#patch_healthcare_appointment) - Update an appointment
* [remove_dms_appointment](#remove_dms_appointment) - Remove an appointment
* [remove_healthcare_appointment](#remove_healthcare_appointment) - Remove an appointment
* [update_dms_appointment](#update_dms_appointment) - Update an appointment
* [update_healthcare_appointment](#update_healthcare_appointment) - Update an appointment

## create_dms_appointment

Creates a DmsAppointment. Provide the unified DmsAppointment fields in the request body; they are mapped to the provider's API. Returns the created DmsAppointment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDmsAppointment" method="post" path="/dms/{connection_id}/appointment" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.create_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.610Z"),
            "id": "430e7b3d-b8dd-439a-b13f-8bdf6962dc64",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "4c2736ea-f419-4ae0-997a-4991e091d780",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "62b7aa53-d974-49b9-a2ae-a89a668b90aa",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "94fb6c00-9163-48d5-8efd-784e629482a9",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.610Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.986Z"),
        },
        "connection_id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateDmsAppointmentRequest](../../models/operations/createdmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateDmsAppointmentResponse](../../models/operations/createdmsappointmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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
            "description": "cubicularis caput viriliter",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "62341001-6b7b-4e1b-8def-4eca476ec5fb",
            "is_virtual": True,
            "meeting_url": "https://cautious-cannon.com/",
            "metadata": [],
            "notes": "Casus anser ver alo beatus.",
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
            "updated_at": parse_datetime("2026-10-27T09:00:39.157Z"),
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

## get_dms_appointment

Retrieves a single DmsAppointment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDmsAppointment" method="get" path="/dms/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.get_dms_appointment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetDmsAppointmentRequest](../../models/operations/getdmsappointmentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetDmsAppointmentResponse](../../models/operations/getdmsappointmentresponse.md)**

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

## list_dms_appointments

Returns a list of DmsAppointments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDmsAppointments" method="get" path="/dms/{connection_id}/appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.list_dms_appointments(request={
        "connection_id": "<id>",
    })

    assert res.dms_appointments is not None

    # Handle response
    print(res.dms_appointments)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListDmsAppointmentsRequest](../../models/operations/listdmsappointmentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListDmsAppointmentsResponse](../../models/operations/listdmsappointmentsresponse.md)**

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

## patch_dms_appointment

Updates the DmsAppointment identified by `id`. Provide the unified DmsAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchDmsAppointment" method="patch" path="/dms/{connection_id}/appointment/{id}" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.patch_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.631Z"),
            "id": "4adcb137-9ab5-4404-99d5-9b49a342578e",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "d7f17954-4053-4eba-a7be-f4016074238d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "52fba2cc-a29d-457d-a0d5-14d9e9481c0d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "c653de4e-1054-4fec-9696-51886b2362b2",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.631Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.998Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchDmsAppointmentRequest](../../models/operations/patchdmsappointmentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchDmsAppointmentResponse](../../models/operations/patchdmsappointmentresponse.md)**

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
            "description": "cubicularis caput viriliter",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "1325d1db-161e-41c1-8cd9-b1495ef889e9",
            "is_virtual": True,
            "meeting_url": "https://cautious-cannon.com/",
            "metadata": [],
            "notes": "Casus anser ver alo beatus.",
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
            "updated_at": parse_datetime("2026-10-27T09:00:39.176Z"),
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

## remove_dms_appointment

Deletes the DmsAppointment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDmsAppointment" method="delete" path="/dms/{connection_id}/appointment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.remove_dms_appointment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveDmsAppointmentRequest](../../models/operations/removedmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveDmsAppointmentResponse](../../models/operations/removedmsappointmentresponse.md)**

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

## update_dms_appointment

Updates the DmsAppointment identified by `id`. Provide the unified DmsAppointment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDmsAppointment" method="put" path="/dms/{connection_id}/appointment/{id}" example="dms_appointment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.appointment.update_dms_appointment(request={
        "dms_appointment": {
            "created_at": parse_datetime("2023-10-16T02:56:45.127Z"),
            "end_at": parse_datetime("2026-05-07T05:34:50.631Z"),
            "id": "4adcb137-9ab5-4404-99d5-9b49a342578e",
            "metadata": [],
            "notes": "Soluta conitor timidus confero.",
            "number": "A541909",
            "services": [
                {
                    "id": "d7f17954-4053-4eba-a7be-f4016074238d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.WARRANTY,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Check engine light on",
                    "id": "52fba2cc-a29d-457d-a0d5-14d9e9481c0d",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
                {
                    "complaint": "Due for service",
                    "id": "c653de4e-1054-4fec-9696-51886b2362b2",
                    "name": "Customer concern",
                    "pay_type": shared.PayType.CUSTOMER,
                    "technician_user_ids": [],
                },
            ],
            "start_at": parse_datetime("2026-05-06T22:34:50.631Z"),
            "status": shared.DmsAppointmentStatus.CANCELLED,
            "transport_type": shared.TransportType.LOANER,
            "updated_at": parse_datetime("2025-04-06T04:21:26.998Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.dms_appointment is not None

    # Handle response
    print(res.dms_appointment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateDmsAppointmentRequest](../../models/operations/updatedmsappointmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateDmsAppointmentResponse](../../models/operations/updatedmsappointmentresponse.md)**

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
            "description": "cubicularis caput viriliter",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "1325d1db-161e-41c1-8cd9-b1495ef889e9",
            "is_virtual": True,
            "meeting_url": "https://cautious-cannon.com/",
            "metadata": [],
            "notes": "Casus anser ver alo beatus.",
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
            "updated_at": parse_datetime("2026-10-27T09:00:39.176Z"),
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