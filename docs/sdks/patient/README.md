# Patient

## Overview

### Available Operations

* [create_healthcare_patient](#create_healthcare_patient) - Create a patient
* [get_healthcare_patient](#get_healthcare_patient) - Retrieve a patient
* [list_healthcare_patients](#list_healthcare_patients) - List all patients
* [patch_healthcare_patient](#patch_healthcare_patient) - Update a patient
* [update_healthcare_patient](#update_healthcare_patient) - Update a patient

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

    res = unified_to.patient.create_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "3645 Zoila Isle",
                "address2": "Suite 613",
                "city": "Jacintostead",
                "country": "US",
                "postal_code": "31579",
                "region": "Minnesota",
            },
            "birthdate": "2025-02-09",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@yahoo.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "eca3858f-c799-4f09-9a26-8cd996b91528",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "92636004",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "en",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "659.223.0829 x590",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-19T23:26:26.323Z"),
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

    res = unified_to.patient.get_healthcare_patient(request={
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

    res = unified_to.patient.list_healthcare_patients(request={
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

    res = unified_to.patient.patch_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "3645 Zoila Isle",
                "address2": "Suite 613",
                "city": "Jacintostead",
                "country": "US",
                "postal_code": "31579",
                "region": "Minnesota",
            },
            "birthdate": "2025-02-09",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@yahoo.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "ff03defe-888a-412b-a562-feac195a7a8b",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "92636004",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "en",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "659.223.0829 x590",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-19T23:26:26.344Z"),
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

    res = unified_to.patient.update_healthcare_patient(request={
        "healthcare_patient": {
            "address": {
                "address1": "3645 Zoila Isle",
                "address2": "Suite 613",
                "city": "Jacintostead",
                "country": "US",
                "postal_code": "31579",
                "region": "Minnesota",
            },
            "birthdate": "2025-02-09",
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@yahoo.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "ff03defe-888a-412b-a562-feac195a7a8b",
            "identifiers": [
                {
                    "type": shared.HealthcareIdentifierType.MRN,
                    "value": "92636004",
                },
            ],
            "is_active": True,
            "is_deceased": False,
            "language": "en",
            "last_name": "Parker",
            "metadata": [],
            "name": "Alejandrin Parker",
            "practitioner_ids": [],
            "telephones": [
                {
                    "telephone": "659.223.0829 x590",
                    "type": shared.HealthcareTelephoneType.MOBILE,
                },
            ],
            "updated_at": parse_datetime("2026-06-19T23:26:26.344Z"),
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