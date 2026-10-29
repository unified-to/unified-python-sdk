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

Creates a HrisEmployee. Provide the unified HrisEmployee fields in the request body; they are mapped to the provider's API. Returns the created HrisEmployee.

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
                "address1": "7431 Hintz Parkway",
                "address2": "Apt. 520",
                "city": "Port Rogerview",
                "country_code": "US",
                "postal_code": "01711",
                "region": "Missouri",
                "region_code": "TN",
            },
            "bio": "fun advocate  🇱🇻",
            "compensation": [
                {
                    "amount": 95000.0,
                    "currency": "USD",
                    "frequency": shared.HrisCompensationFrequency.YEAR,
                    "notes": "Eius.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "USD",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "zetta.prohaska@insidious-stump.net",
                    "type": shared.HrisEmailType.WORK,
                },
            ],
            "employee_number": "uCk3qaL1ei",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.PART_TIME,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.EXEMPT,
            "gender": shared.HrisEmployeeGender.MALE,
            "has_mfa": True,
            "hired_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "id": "b4e6c1d9-01ad-49f7-b6cf-4324d97b4bf2",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/female/512/85.jpg",
            "language_locale": "in",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.HrisEmployeeMaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "6e7cd75f-5626-4243-ab3c-089dbd50f3ad",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tutis",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.WEEK,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "keith.prohaska@gmail.com",
                        },
                    ],
                    "name": "Keith Prohaska",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "keely.prohaska@icloud.com",
                        },
                    ],
                    "name": "Keely Prohaska",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Ms.",
            "ssn_sin": "284-82-8167",
            "storage_quota_allocated": 3653713.0,
            "storage_quota_available": 3017275.0,
            "storage_quota_used": 367449.0,
            "telephones": [
                {
                    "telephone": "(320) 980-1370",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(694) 840-0166",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timeoff_days_total": 17.0,
            "timeoff_days_used": 9.0,
            "timezone": "Europe/Ljubljana",
            "title": "District Branding Specialist",
            "updated_at": parse_datetime("2020-07-20T01:57:43.280Z"),
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

Retrieves a single HrisEmployee by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of HrisEmployees. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the HrisEmployee identified by `id`. Provide the unified HrisEmployee fields to change in the request body.

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
                "address1": "7431 Hintz Parkway",
                "address2": "Apt. 520",
                "city": "Port Rogerview",
                "country_code": "US",
                "postal_code": "01711",
                "region": "Missouri",
                "region_code": "TN",
            },
            "bio": "fun advocate  🇱🇻",
            "compensation": [
                {
                    "amount": 95000.0,
                    "currency": "USD",
                    "frequency": shared.HrisCompensationFrequency.YEAR,
                    "notes": "Eius.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "USD",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "zetta.prohaska@insidious-stump.net",
                    "type": shared.HrisEmailType.WORK,
                },
            ],
            "employee_number": "uCk3qaL1ei",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.PART_TIME,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.EXEMPT,
            "gender": shared.HrisEmployeeGender.MALE,
            "has_mfa": True,
            "hired_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "id": "691bfe1a-5d12-4044-b16e-6d2f769a0ab4",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/female/512/85.jpg",
            "language_locale": "in",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.HrisEmployeeMaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "a311d266-8876-42bf-8e0e-f5995e63dd66",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tutis",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.WEEK,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "keith.prohaska@gmail.com",
                        },
                    ],
                    "name": "Keith Prohaska",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "keely.prohaska@icloud.com",
                        },
                    ],
                    "name": "Keely Prohaska",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Ms.",
            "ssn_sin": "284-82-8167",
            "storage_quota_allocated": 3653713.0,
            "storage_quota_available": 3017275.0,
            "storage_quota_used": 367449.0,
            "telephones": [
                {
                    "telephone": "(320) 980-1370",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(694) 840-0166",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timeoff_days_total": 17.0,
            "timeoff_days_used": 9.0,
            "timezone": "Europe/Ljubljana",
            "title": "District Branding Specialist",
            "updated_at": parse_datetime("2020-07-20T01:57:43.289Z"),
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

Deletes the HrisEmployee identified by `id`.

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

Updates the HrisEmployee identified by `id`. Provide the unified HrisEmployee fields to change in the request body.

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
                "address1": "7431 Hintz Parkway",
                "address2": "Apt. 520",
                "city": "Port Rogerview",
                "country_code": "US",
                "postal_code": "01711",
                "region": "Missouri",
                "region_code": "TN",
            },
            "bio": "fun advocate  🇱🇻",
            "compensation": [
                {
                    "amount": 95000.0,
                    "currency": "USD",
                    "frequency": shared.HrisCompensationFrequency.YEAR,
                    "notes": "Eius.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "currency": "USD",
            "date_of_birth": parse_datetime("2001-04-22"),
            "emails": [
                {
                    "email": "zetta.prohaska@insidious-stump.net",
                    "type": shared.HrisEmailType.WORK,
                },
            ],
            "employee_number": "uCk3qaL1ei",
            "employment_status": shared.EmploymentStatus.ACTIVE,
            "employment_type": shared.HrisEmployeeEmploymentType.PART_TIME,
            "first_name": "Zetta",
            "flsa_status": shared.FlsaStatus.EXEMPT,
            "gender": shared.HrisEmployeeGender.MALE,
            "has_mfa": True,
            "hired_at": parse_datetime("2019-09-16T15:08:53.262Z"),
            "id": "691bfe1a-5d12-4044-b16e-6d2f769a0ab4",
            "image_url": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/female/512/85.jpg",
            "language_locale": "in",
            "last_name": "Prohaska",
            "locations": [],
            "marital_status": shared.HrisEmployeeMaritalStatus.MARRIED,
            "metadata": [
                {
                    "extra_data": {
                        "display_name": "Custom Property",
                    },
                    "format_": shared.HrisMetadataFormat.TEXT,
                    "id": "a311d266-8876-42bf-8e0e-f5995e63dd66",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tutis",
                },
            ],
            "name": "Zetta Prohaska",
            "pay_frequency": shared.PayFrequency.WEEK,
            "pronouns": "she/her",
            "relationships": [
                {
                    "emails": [
                        {
                            "email": "keith.prohaska@gmail.com",
                        },
                    ],
                    "name": "Keith Prohaska",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
                {
                    "emails": [
                        {
                            "email": "keely.prohaska@icloud.com",
                        },
                    ],
                    "name": "Keely Prohaska",
                    "type": shared.HrisEmployeerelationshipType.OTHER,
                },
            ],
            "salutation": "Ms.",
            "ssn_sin": "284-82-8167",
            "storage_quota_allocated": 3653713.0,
            "storage_quota_available": 3017275.0,
            "storage_quota_used": 367449.0,
            "telephones": [
                {
                    "telephone": "(320) 980-1370",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(694) 840-0166",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timeoff_days_total": 17.0,
            "timeoff_days_used": 9.0,
            "timezone": "Europe/Ljubljana",
            "title": "District Branding Specialist",
            "updated_at": parse_datetime("2020-07-20T01:57:43.289Z"),
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