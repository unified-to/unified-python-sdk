# Employee

## Overview

### Available Operations

* [create_hris_employee](#create_hris_employee) - Create an employee
* [get_hris_employee](#get_hris_employee) - Retrieve an employee
* [list_hris_employees](#list_hris_employees) - List all employees
* [patch_hris_employee](#patch_hris_employee) - Update an employee
* [remove_hris_employee](#remove_hris_employee) - Remove an employee
* [update_hris_employee](#update_hris_employee) - Update an employee

## create_hris_employee

Create an employee

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisEmployee" method="post" path="/hris/{connection_id}/employee" example="hris_employee" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.create_hris_employee(request={
        "hris_employee": {
            "address": {
                "address1": "52008 Lansdowne Road",
                "address2": "Apt. 101",
                "city": "Connellyberg",
                "country_code": "US",
                "postal_code": "18978",
                "region": "South Dakota",
                "region_code": "NM",
            },
            "bio": "sushi devotee, singer",
            "compensation": [
                {
                    "amount": 60136.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.STOCK_OPTIONS,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "IDR",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "Zetta_Prohaska67@hotmail.com",
                    "type": shared.HrisEmailType.HOME,
                },
            ],
            "employee_number": "YuOt169CGu",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.VOLUNTEER,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.SALARIED_NONEXEMPT,
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": False,
            "hired_at": parse_datetime("2023-05-24T03:36:40.095Z"),
            "id": "e63651c3-2048-4f57-b1d0-7a261c418ae5",
            "image_url": "https://loremflickr.com/3684/2116?lock=4686991638584456",
            "language_locale": "es",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.MaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "6c552e4d-7d54-4940-a26e-bc0f4dca0a13",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "appono",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.BIWEEKLY,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "Deshaun.Sanford24@yahoo.com",
                        },
                        {
                            "email": "Rebeca.Dibbert11@hotmail.com",
                        },
                        {
                            "email": "Hester80@gmail.com",
                        },
                    ],
                    "name": "Automotive",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "Margot11@yahoo.com",
                        },
                        {
                            "email": "Jaden_Miller@gmail.com",
                        },
                    ],
                    "name": "Electronics",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 7748057.0,
            "storage_quota_available": 1590710.0,
            "storage_quota_used": 730343.0,
            "telephones": [
                {
                    "telephone": "(409) 801-3705",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "termination_reason": "Communis adnuo damnatio atavus terebro acies canis cogito triumphus creber temptatio defendo cubo amissio paulatim corroboro.",
            "timeoff_days_total": 12.0,
            "timeoff_days_used": 6.0,
            "timezone": "Africa/Harare",
            "title": "Investor Paradigm Liaison",
            "updated_at": parse_datetime("2022-02-28T06:16:40.938Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_employee is not None

    # Handle response
    print(res.hris_employee)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisEmployeeRequest](../../models/operations/createhrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisEmployeeResponse](../../models/operations/createhrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_employee

Retrieve an employee

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisEmployee" method="get" path="/hris/{connection_id}/employee/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.get_hris_employee(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_employee is not None

    # Handle response
    print(res.hris_employee)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisEmployeeRequest](../../models/operations/gethrisemployeerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisEmployeeResponse](../../models/operations/gethrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_employees

List all employees

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisEmployees" method="get" path="/hris/{connection_id}/employee" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.list_hris_employees(request={
        "connection_id": "<id>",
    })

    assert res.hris_employees is not None

    # Handle response
    print(res.hris_employees)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisEmployeesRequest](../../models/operations/listhrisemployeesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisEmployeesResponse](../../models/operations/listhrisemployeesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_employee

Update an employee

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisEmployee" method="patch" path="/hris/{connection_id}/employee/{id}" example="hris_employee" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.patch_hris_employee(request={
        "hris_employee": {
            "address": {
                "address1": "52008 Lansdowne Road",
                "address2": "Apt. 101",
                "city": "Connellyberg",
                "country_code": "US",
                "postal_code": "18978",
                "region": "South Dakota",
                "region_code": "NM",
            },
            "bio": "sushi devotee, singer",
            "compensation": [
                {
                    "amount": 60136.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.STOCK_OPTIONS,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "IDR",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "Zetta_Prohaska67@hotmail.com",
                    "type": shared.HrisEmailType.HOME,
                },
            ],
            "employee_number": "YuOt169CGu",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.VOLUNTEER,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.SALARIED_NONEXEMPT,
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": False,
            "hired_at": parse_datetime("2023-05-24T03:36:40.142Z"),
            "id": "59f3df6e-7191-49a1-9c02-1a72dba12fe9",
            "image_url": "https://loremflickr.com/3684/2116?lock=4686991638584456",
            "language_locale": "es",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.MaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "d6b99c0c-d3d3-4f24-a3c1-8db40f6f2973",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "appono",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.BIWEEKLY,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "Deshaun.Sanford24@yahoo.com",
                        },
                        {
                            "email": "Rebeca.Dibbert11@hotmail.com",
                        },
                        {
                            "email": "Hester80@gmail.com",
                        },
                    ],
                    "name": "Automotive",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "Margot11@yahoo.com",
                        },
                        {
                            "email": "Jaden_Miller@gmail.com",
                        },
                    ],
                    "name": "Electronics",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 7748057.0,
            "storage_quota_available": 1590710.0,
            "storage_quota_used": 730343.0,
            "telephones": [
                {
                    "telephone": "(409) 801-3705",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "termination_reason": "Communis adnuo damnatio atavus terebro acies canis cogito triumphus creber temptatio defendo cubo amissio paulatim corroboro.",
            "timeoff_days_total": 12.0,
            "timeoff_days_used": 6.0,
            "timezone": "Africa/Harare",
            "title": "Investor Paradigm Liaison",
            "updated_at": parse_datetime("2022-02-28T06:16:40.969Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_employee is not None

    # Handle response
    print(res.hris_employee)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisEmployeeRequest](../../models/operations/patchhrisemployeerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisEmployeeResponse](../../models/operations/patchhrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_employee

Remove an employee

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisEmployee" method="delete" path="/hris/{connection_id}/employee/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.remove_hris_employee(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisEmployeeRequest](../../models/operations/removehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisEmployeeResponse](../../models/operations/removehrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_employee

Update an employee

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisEmployee" method="put" path="/hris/{connection_id}/employee/{id}" example="hris_employee" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.employee.update_hris_employee(request={
        "hris_employee": {
            "address": {
                "address1": "52008 Lansdowne Road",
                "address2": "Apt. 101",
                "city": "Connellyberg",
                "country_code": "US",
                "postal_code": "18978",
                "region": "South Dakota",
                "region_code": "NM",
            },
            "bio": "sushi devotee, singer",
            "compensation": [
                {
                    "amount": 60136.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.STOCK_OPTIONS,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "IDR",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "Zetta_Prohaska67@hotmail.com",
                    "type": shared.HrisEmailType.HOME,
                },
            ],
            "employee_number": "YuOt169CGu",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.VOLUNTEER,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.SALARIED_NONEXEMPT,
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": False,
            "hired_at": parse_datetime("2023-05-24T03:36:40.142Z"),
            "id": "59f3df6e-7191-49a1-9c02-1a72dba12fe9",
            "image_url": "https://loremflickr.com/3684/2116?lock=4686991638584456",
            "language_locale": "es",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.MaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "d6b99c0c-d3d3-4f24-a3c1-8db40f6f2973",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "appono",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.BIWEEKLY,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "Deshaun.Sanford24@yahoo.com",
                        },
                        {
                            "email": "Rebeca.Dibbert11@hotmail.com",
                        },
                        {
                            "email": "Hester80@gmail.com",
                        },
                    ],
                    "name": "Automotive",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "Margot11@yahoo.com",
                        },
                        {
                            "email": "Jaden_Miller@gmail.com",
                        },
                    ],
                    "name": "Electronics",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 7748057.0,
            "storage_quota_available": 1590710.0,
            "storage_quota_used": 730343.0,
            "telephones": [
                {
                    "telephone": "(409) 801-3705",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "termination_reason": "Communis adnuo damnatio atavus terebro acies canis cogito triumphus creber temptatio defendo cubo amissio paulatim corroboro.",
            "timeoff_days_total": 12.0,
            "timeoff_days_used": 6.0,
            "timezone": "Africa/Harare",
            "title": "Investor Paradigm Liaison",
            "updated_at": parse_datetime("2022-02-28T06:16:40.969Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_employee is not None

    # Handle response
    print(res.hris_employee)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisEmployeeRequest](../../models/operations/updatehrisemployeerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisEmployeeResponse](../../models/operations/updatehrisemployeeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |