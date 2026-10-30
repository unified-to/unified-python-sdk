# Patient

## Overview

### Available Operations

* [create_healthcare_patient](#create_healthcare_patient) - Create a patient
* [get_healthcare_patient](#get_healthcare_patient) - Retrieve a patient
* [list_healthcare_patients](#list_healthcare_patients) - List all patients
* [patch_healthcare_patient](#patch_healthcare_patient) - Update a patient
* [update_healthcare_patient](#update_healthcare_patient) - Update a patient

## create_healthcare_patient

Creates a HealthcarePatient. Provide the unified HealthcarePatient fields in the request body; they are mapped to the provider's API. Returns the created HealthcarePatient.

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
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-21",
            "contacts": [
                {
                    "emails": [],
                    "name": "Antonia Lebsack",
                    "relationship": "Spouse",
                    "telephones": [
                        {
                            "telephone": "(695) 328-7029 x4412",
                            "type": shared.HealthcareTelephoneType.MOBILE,
                        },
                    ],
                },
            ],
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "ea69d077-6a50-486e-9810-8a535866a03d",
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
            "updated_at": parse_datetime("2026-07-01T07:54:51.048Z"),
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

Retrieves a single HealthcarePatient by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of HealthcarePatients. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the HealthcarePatient identified by `id`. Provide the unified HealthcarePatient fields to change in the request body.

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
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-21",
            "contacts": [
                {
                    "emails": [],
                    "name": "Antonia Lebsack",
                    "relationship": "Spouse",
                    "telephones": [
                        {
                            "telephone": "(695) 328-7029 x4412",
                            "type": shared.HealthcareTelephoneType.MOBILE,
                        },
                    ],
                },
            ],
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "9a6f868d-3f94-4581-b670-cc305ef43b99",
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
            "updated_at": parse_datetime("2026-07-01T07:54:51.090Z"),
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

Updates the HealthcarePatient identified by `id`. Provide the unified HealthcarePatient fields to change in the request body.

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
                "address1": "162 Kirlin Mall",
                "city": "Dickinsonborough",
                "country": "US",
                "postal_code": "54031",
                "region": "Nebraska",
            },
            "birthdate": "2025-02-21",
            "contacts": [
                {
                    "emails": [],
                    "name": "Antonia Lebsack",
                    "relationship": "Spouse",
                    "telephones": [
                        {
                            "telephone": "(695) 328-7029 x4412",
                            "type": shared.HealthcareTelephoneType.MOBILE,
                        },
                    ],
                },
            ],
            "created_at": parse_datetime("2021-06-05T21:08:04.917Z"),
            "emails": [
                {
                    "email": "alejandrin.parker@icloud.com",
                    "type": shared.HealthcareEmailType.HOME,
                },
            ],
            "first_name": "Alejandrin",
            "gender": shared.HealthcarePatientGender.FEMALE,
            "id": "9a6f868d-3f94-4581-b670-cc305ef43b99",
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
            "updated_at": parse_datetime("2026-07-01T07:54:51.090Z"),
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