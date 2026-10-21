# Healthcare

## Overview

### Available Operations

* [create_healthcare_appointment](#create_healthcare_appointment) - Create an appointment
* [create_healthcare_observation](#create_healthcare_observation) - Create an observation
* [create_healthcare_patient](#create_healthcare_patient) - Create a patient
* [get_healthcare_allergy](#get_healthcare_allergy) - Retrieve an allergy
* [get_healthcare_appointment](#get_healthcare_appointment) - Retrieve an appointment
* [get_healthcare_condition](#get_healthcare_condition) - Retrieve a condition
* [get_healthcare_encounter](#get_healthcare_encounter) - Retrieve an encounter
* [get_healthcare_immunization](#get_healthcare_immunization) - Retrieve an immunization
* [get_healthcare_location](#get_healthcare_location) - Retrieve a location
* [get_healthcare_medication](#get_healthcare_medication) - Retrieve a medication
* [get_healthcare_observation](#get_healthcare_observation) - Retrieve an observation
* [get_healthcare_patient](#get_healthcare_patient) - Retrieve a patient
* [get_healthcare_practitioner](#get_healthcare_practitioner) - Retrieve a practitioner
* [get_healthcare_slot](#get_healthcare_slot) - Retrieve a slot
* [list_healthcare_allergies](#list_healthcare_allergies) - List all allergies
* [list_healthcare_appointments](#list_healthcare_appointments) - List all appointments
* [list_healthcare_conditions](#list_healthcare_conditions) - List all conditions
* [list_healthcare_encounters](#list_healthcare_encounters) - List all encounters
* [list_healthcare_immunizations](#list_healthcare_immunizations) - List all immunizations
* [list_healthcare_locations](#list_healthcare_locations) - List all locations
* [list_healthcare_medications](#list_healthcare_medications) - List all medications
* [list_healthcare_observations](#list_healthcare_observations) - List all observations
* [list_healthcare_patients](#list_healthcare_patients) - List all patients
* [list_healthcare_practitioners](#list_healthcare_practitioners) - List all practitioners
* [list_healthcare_slots](#list_healthcare_slots) - List all slots
* [patch_healthcare_appointment](#patch_healthcare_appointment) - Update an appointment
* [patch_healthcare_patient](#patch_healthcare_patient) - Update a patient
* [remove_healthcare_appointment](#remove_healthcare_appointment) - Remove an appointment
* [update_healthcare_appointment](#update_healthcare_appointment) - Update an appointment
* [update_healthcare_patient](#update_healthcare_patient) - Update a patient

## create_healthcare_appointment

Create an appointment

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

    res = unified_to.healthcare.create_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "78e3419c-3f84-444a-95b2-32813aaa7e55",
            "metadata": [],
            "practitioner_ids": [],
            "reasons": [
                {
                    "code": "12762740",
                    "display": "cubicularis caput",
                    "system": "http://snomed.info/sct",
                },
            ],
            "service_types": [
                {
                    "code": "61128108",
                    "display": "Annual physical",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2025-11-19T10:37:36.973Z"),
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

## create_healthcare_observation

Create an observation

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

    res = unified_to.healthcare.create_healthcare_observation(request={
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
            "id": "878c4fbe-c6da-4f1c-8b2b-3415da6a3e0e",
            "interpretation": shared.Interpretation.CRITICAL_HIGH,
            "issued_at": parse_datetime("2025-05-11T10:26:23.241Z"),
            "metadata": [],
            "name": "Blood pressure panel",
            "observed_at": parse_datetime("2025-01-20T03:57:34.624Z"),
            "status": shared.HealthcareObservationStatus.CORRECTED,
            "type": shared.HealthcareObservationType.VITAL_SIGNS,
            "updated_at": parse_datetime("2026-03-24T06:20:26.478Z"),
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

## create_healthcare_patient

Create a patient

### Example Usage

<!-- UsageSnippet language="python" operationID="createHealthcarePatient" method="post" path="/healthcare/{connection_id}/patient" example="healthcare_patient" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.create_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-12",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "345c3b07-8ea6-4168-9475-bfe6f301545f",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "57992636",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "zh",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "1-219-555-9023 x08295",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-22T20:13:50.798Z"),
        },
        "connection_id": "<id>",
    })

    assert res.healthcare_patient is not None

    # Handle response
    print(res.healthcare_patient)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateHealthcarePatientRequest](../../models/operations/createhealthcarepatientrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateHealthcarePatientResponse](../../models/operations/createhealthcarepatientresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.healthcare.get_healthcare_allergy(request={
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

## get_healthcare_appointment

Retrieve an appointment

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

    res = unified_to.healthcare.get_healthcare_appointment(request={
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

    res = unified_to.healthcare.get_healthcare_condition(request={
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

    res = unified_to.healthcare.get_healthcare_encounter(request={
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

## get_healthcare_immunization

Retrieve an immunization

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareImmunization" method="get" path="/healthcare/{connection_id}/immunization/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.get_healthcare_immunization(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_immunization is not None

    # Handle response
    print(res.healthcare_immunization)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetHealthcareImmunizationRequest](../../models/operations/gethealthcareimmunizationrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetHealthcareImmunizationResponse](../../models/operations/gethealthcareimmunizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_healthcare_location

Retrieve a location

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareLocation" method="get" path="/healthcare/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.get_healthcare_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_location is not None

    # Handle response
    print(res.healthcare_location)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetHealthcareLocationRequest](../../models/operations/gethealthcarelocationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetHealthcareLocationResponse](../../models/operations/gethealthcarelocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.healthcare.get_healthcare_medication(request={
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

## get_healthcare_observation

Retrieve an observation

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

    res = unified_to.healthcare.get_healthcare_observation(request={
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

## get_healthcare_patient

Retrieve a patient

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcarePatient" method="get" path="/healthcare/{connection_id}/patient/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.get_healthcare_patient(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_patient is not None

    # Handle response
    print(res.healthcare_patient)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetHealthcarePatientRequest](../../models/operations/gethealthcarepatientrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetHealthcarePatientResponse](../../models/operations/gethealthcarepatientresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.healthcare.get_healthcare_practitioner(request={
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

## get_healthcare_slot

Retrieve a slot

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthcareSlot" method="get" path="/healthcare/{connection_id}/slot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.get_healthcare_slot(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_slot is not None

    # Handle response
    print(res.healthcare_slot)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetHealthcareSlotRequest](../../models/operations/gethealthcareslotrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetHealthcareSlotResponse](../../models/operations/gethealthcareslotresponse.md)**

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

    res = unified_to.healthcare.list_healthcare_allergies(request={
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

## list_healthcare_appointments

List all appointments

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

    res = unified_to.healthcare.list_healthcare_appointments(request={
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

    res = unified_to.healthcare.list_healthcare_conditions(request={
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

    res = unified_to.healthcare.list_healthcare_encounters(request={
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

## list_healthcare_immunizations

List all immunizations

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareImmunizations" method="get" path="/healthcare/{connection_id}/immunization" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.list_healthcare_immunizations(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_immunizations is not None

    # Handle response
    print(res.healthcare_immunizations)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListHealthcareImmunizationsRequest](../../models/operations/listhealthcareimmunizationsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.ListHealthcareImmunizationsResponse](../../models/operations/listhealthcareimmunizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_healthcare_locations

List all locations

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareLocations" method="get" path="/healthcare/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.list_healthcare_locations(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_locations is not None

    # Handle response
    print(res.healthcare_locations)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListHealthcareLocationsRequest](../../models/operations/listhealthcarelocationsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListHealthcareLocationsResponse](../../models/operations/listhealthcarelocationsresponse.md)**

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

    res = unified_to.healthcare.list_healthcare_medications(request={
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

## list_healthcare_observations

List all observations

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

    res = unified_to.healthcare.list_healthcare_observations(request={
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

## list_healthcare_patients

List all patients

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcarePatients" method="get" path="/healthcare/{connection_id}/patient" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.list_healthcare_patients(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_patients is not None

    # Handle response
    print(res.healthcare_patients)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListHealthcarePatientsRequest](../../models/operations/listhealthcarepatientsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListHealthcarePatientsResponse](../../models/operations/listhealthcarepatientsresponse.md)**

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

    res = unified_to.healthcare.list_healthcare_practitioners(request={
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

## list_healthcare_slots

List all slots

### Example Usage

<!-- UsageSnippet language="python" operationID="listHealthcareSlots" method="get" path="/healthcare/{connection_id}/slot" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.list_healthcare_slots(request={
        "connection_id": "<id>",
    })

    assert res.healthcare_slots is not None

    # Handle response
    print(res.healthcare_slots)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListHealthcareSlotsRequest](../../models/operations/listhealthcareslotsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListHealthcareSlotsResponse](../../models/operations/listhealthcareslotsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_healthcare_appointment

Update an appointment

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

    res = unified_to.healthcare.patch_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "738d9041-01ed-4d17-bddb-4774797ef8d1",
            "metadata": [],
            "practitioner_ids": [],
            "reasons": [
                {
                    "code": "12762740",
                    "display": "cubicularis caput",
                    "system": "http://snomed.info/sct",
                },
            ],
            "service_types": [
                {
                    "code": "61128108",
                    "display": "Annual physical",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2025-11-19T10:37:36.995Z"),
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

## patch_healthcare_patient

Update a patient

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHealthcarePatient" method="patch" path="/healthcare/{connection_id}/patient/{id}" example="healthcare_patient" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.patch_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-12",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "52690fb3-4b8c-47df-b212-a82439f0afef",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "57992636",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "zh",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "1-219-555-9023 x08295",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-22T20:13:50.834Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_patient is not None

    # Handle response
    print(res.healthcare_patient)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchHealthcarePatientRequest](../../models/operations/patchhealthcarepatientrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchHealthcarePatientResponse](../../models/operations/patchhealthcarepatientresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_healthcare_appointment

Remove an appointment

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

    res = unified_to.healthcare.remove_healthcare_appointment(request={
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

Update an appointment

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

    res = unified_to.healthcare.update_healthcare_appointment(request={
        "healthcare_appointment": {
            "created_at": parse_datetime("2023-04-11T08:16:20.874Z"),
            "description": "clarus aptus cetera",
            "end_at": parse_datetime("2023-12-12T13:04:41.451Z"),
            "id": "738d9041-01ed-4d17-bddb-4774797ef8d1",
            "metadata": [],
            "practitioner_ids": [],
            "reasons": [
                {
                    "code": "12762740",
                    "display": "cubicularis caput",
                    "system": "http://snomed.info/sct",
                },
            ],
            "service_types": [
                {
                    "code": "61128108",
                    "display": "Annual physical",
                    "system": "http://snomed.info/sct",
                },
            ],
            "slot_ids": [],
            "start_at": parse_datetime("2023-12-12T12:34:41.451Z"),
            "status": shared.HealthcareAppointmentStatus.BOOKED,
            "updated_at": parse_datetime("2025-11-19T10:37:36.995Z"),
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

## update_healthcare_patient

Update a patient

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHealthcarePatient" method="put" path="/healthcare/{connection_id}/patient/{id}" example="healthcare_patient" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.healthcare.update_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-12",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "52690fb3-4b8c-47df-b212-a82439f0afef",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "57992636",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "zh",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "1-219-555-9023 x08295",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-22T20:13:50.834Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.healthcare_patient is not None

    # Handle response
    print(res.healthcare_patient)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateHealthcarePatientRequest](../../models/operations/updatehealthcarepatientrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateHealthcarePatientResponse](../../models/operations/updatehealthcarepatientresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |