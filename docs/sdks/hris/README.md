# Hris

## Overview

### Available Operations

* [create_hris_attendance](#create_hris_attendance) - Create an attendance
* [create_hris_bankaccount](#create_hris_bankaccount) - Create a bankaccount
* [create_hris_benefit](#create_hris_benefit) - Create a benefit
* [create_hris_company](#create_hris_company) - Create a company
* [create_hris_deduction](#create_hris_deduction) - Create a deduction
* [create_hris_device](#create_hris_device) - Create a device
* [create_hris_document](#create_hris_document) - Create a document
* [create_hris_employee](#create_hris_employee) - Create an employee
* [create_hris_group](#create_hris_group) - Create a group
* [create_hris_location](#create_hris_location) - Create a location
* [create_hris_taxonomy](#create_hris_taxonomy) - Create a taxonomy
* [create_hris_timeoff](#create_hris_timeoff) - Create a timeoff
* [create_hris_timeshift](#create_hris_timeshift) - Create a timeshift
* [get_hris_attendance](#get_hris_attendance) - Retrieve an attendance
* [get_hris_bankaccount](#get_hris_bankaccount) - Retrieve a bankaccount
* [get_hris_benefit](#get_hris_benefit) - Retrieve a benefit
* [get_hris_company](#get_hris_company) - Retrieve a company
* [get_hris_deduction](#get_hris_deduction) - Retrieve a deduction
* [get_hris_device](#get_hris_device) - Retrieve a device
* [get_hris_document](#get_hris_document) - Retrieve a document
* [get_hris_employee](#get_hris_employee) - Retrieve an employee
* [get_hris_group](#get_hris_group) - Retrieve a group
* [get_hris_location](#get_hris_location) - Retrieve a location
* [get_hris_payslip](#get_hris_payslip) - Retrieve a payslip
* [get_hris_taxonomy](#get_hris_taxonomy) - Retrieve a taxonomy
* [get_hris_timeoff](#get_hris_timeoff) - Retrieve a timeoff
* [get_hris_timeshift](#get_hris_timeshift) - Retrieve a timeshift
* [list_hris_attendances](#list_hris_attendances) - List all attendances
* [list_hris_bankaccounts](#list_hris_bankaccounts) - List all bankaccounts
* [list_hris_benefits](#list_hris_benefits) - List all benefits
* [list_hris_companies](#list_hris_companies) - List all companies
* [list_hris_deductions](#list_hris_deductions) - List all deductions
* [list_hris_devices](#list_hris_devices) - List all devices
* [list_hris_documents](#list_hris_documents) - List all documents
* [list_hris_employees](#list_hris_employees) - List all employees
* [list_hris_groups](#list_hris_groups) - List all groups
* [list_hris_locations](#list_hris_locations) - List all locations
* [list_hris_payslips](#list_hris_payslips) - List all payslips
* [list_hris_taxonomies](#list_hris_taxonomies) - List all taxonomies
* [list_hris_timeoffs](#list_hris_timeoffs) - List all timeoffs
* [list_hris_timeshifts](#list_hris_timeshifts) - List all timeshifts
* [patch_hris_attendance](#patch_hris_attendance) - Update an attendance
* [patch_hris_bankaccount](#patch_hris_bankaccount) - Update a bankaccount
* [patch_hris_benefit](#patch_hris_benefit) - Update a benefit
* [patch_hris_company](#patch_hris_company) - Update a company
* [patch_hris_deduction](#patch_hris_deduction) - Update a deduction
* [patch_hris_device](#patch_hris_device) - Update a device
* [patch_hris_document](#patch_hris_document) - Update a document
* [patch_hris_employee](#patch_hris_employee) - Update an employee
* [patch_hris_group](#patch_hris_group) - Update a group
* [patch_hris_location](#patch_hris_location) - Update a location
* [patch_hris_timeoff](#patch_hris_timeoff) - Update a timeoff
* [patch_hris_timeshift](#patch_hris_timeshift) - Update a timeshift
* [remove_hris_attendance](#remove_hris_attendance) - Remove an attendance
* [remove_hris_bankaccount](#remove_hris_bankaccount) - Remove a bankaccount
* [remove_hris_benefit](#remove_hris_benefit) - Remove a benefit
* [remove_hris_company](#remove_hris_company) - Remove a company
* [remove_hris_deduction](#remove_hris_deduction) - Remove a deduction
* [remove_hris_device](#remove_hris_device) - Remove a device
* [remove_hris_document](#remove_hris_document) - Remove a document
* [remove_hris_employee](#remove_hris_employee) - Remove an employee
* [remove_hris_group](#remove_hris_group) - Remove a group
* [remove_hris_location](#remove_hris_location) - Remove a location
* [remove_hris_timeoff](#remove_hris_timeoff) - Remove a timeoff
* [remove_hris_timeshift](#remove_hris_timeshift) - Remove a timeshift
* [update_hris_attendance](#update_hris_attendance) - Update an attendance
* [update_hris_bankaccount](#update_hris_bankaccount) - Update a bankaccount
* [update_hris_benefit](#update_hris_benefit) - Update a benefit
* [update_hris_company](#update_hris_company) - Update a company
* [update_hris_deduction](#update_hris_deduction) - Update a deduction
* [update_hris_device](#update_hris_device) - Update a device
* [update_hris_document](#update_hris_document) - Update a document
* [update_hris_employee](#update_hris_employee) - Update an employee
* [update_hris_group](#update_hris_group) - Update a group
* [update_hris_location](#update_hris_location) - Update a location
* [update_hris_timeoff](#update_hris_timeoff) - Update a timeoff
* [update_hris_timeshift](#update_hris_timeshift) - Update a timeshift

## create_hris_attendance

Create an attendance

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisAttendance" method="post" path="/hris/{connection_id}/attendance" example="hris_attendance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-08-13T10:36:02.582Z"),
            "breaks": [
                {
                    "duration_minutes": 12.0,
                    "end_at": parse_datetime("2023-10-22T16:22:21.274Z"),
                    "id": "d60a1001-5a8a-4991-8c21-f4da6036cc87",
                    "is_paid": True,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-15T20:48:40.844Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "UGX",
            "declared_tips_amount": 161.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-06T03:55:51.518Z"),
            "hourly_rate": 53.0,
            "hours": 10.0,
            "id": "6f3bbdc4-75ab-4b78-bdfb-8918d1b18b95",
            "job_name": "Global Creative Supervisor",
            "non_cash_tips_amount": 54.0,
            "start_at": parse_datetime("2021-11-09T10:25:57.025Z"),
            "status": shared.HrisAttendanceStatus.CLOSED,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-17T01:24:59.755Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_attendance is not None

    # Handle response
    print(res.hris_attendance)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateHrisAttendanceRequest](../../models/operations/createhrisattendancerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateHrisAttendanceResponse](../../models/operations/createhrisattendanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_bankaccount

Create a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBankaccount" method="post" path="/hris/{connection_id}/bankaccount" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "4e298ff9-1f66-4c1f-b1ec-5ee895cda7bf",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.787Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateHrisBankaccountRequest](../../models/operations/createhrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateHrisBankaccountResponse](../../models/operations/createhrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_benefit

Create a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBenefit" method="post" path="/hris/{connection_id}/benefit" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "316f6179-1072-40b5-ac95-647349da2fa6",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-06T11:00:21.275Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisBenefitRequest](../../models/operations/createhrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisBenefitResponse](../../models/operations/createhrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_company

Create a company

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisCompany" method="post" path="/hris/{connection_id}/company" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "a9419166-ed13-4cc3-9ca1-f086d2325ece",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.918Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisCompanyRequest](../../models/operations/createhriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisCompanyResponse](../../models/operations/createhriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_deduction

Create a deduction

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDeduction" method="post" path="/hris/{connection_id}/deduction" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_deduction(request={
        "hris_deduction": {
            "amount": 139655.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_ONLY,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "end_at": parse_datetime("2026-05-22T22:51:41.898Z"),
            "frequency": shared.HrisDeductionFrequency.MONTH,
            "id": "80baec67-8dfd-44cb-a5e3-8faaaf906a97",
            "is_active": False,
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-02-18T04:37:41.118Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-01T23:41:41.373Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateHrisDeductionRequest](../../models/operations/createhrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateHrisDeductionResponse](../../models/operations/createhrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_device

Create a device

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDevice" method="post" path="/hris/{connection_id}/device" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "aa9bf3e8-ef2a-4460-9de0-f7f31a76743e",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-21T00:56:05.168Z"),
            "version": "2.20.17",
        },
        "connection_id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateHrisDeviceRequest](../../models/operations/createhrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateHrisDeviceResponse](../../models/operations/createhrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_document

Create a document

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisDocument" method="post" path="/hris/{connection_id}/document" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "9c44ea1a-df06-48eb-ae08-025996b09343",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-17T01:54:33.584Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisDocumentRequest](../../models/operations/createhrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisDocumentResponse](../../models/operations/createhrisdocumentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.hris.create_hris_employee(request={
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
                    "amount": 69148.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.EQUITY,
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
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": True,
            "hired_at": parse_datetime("2023-05-10T16:14:24.235Z"),
            "id": "0b47556b-dd67-4604-a3e7-3326e7ac2cc4",
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
                    "id": "8ff023c4-b1c3-4575-904d-5a28abce4f7c",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tenetur",
                },
            ],
            "name": "Zetta Prohaska",
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
                    "type": shared.HrisEmployeerelationshipType.EMERGENCY,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                        {
                            "email": "Princess_Rath43@gmail.com",
                        },
                        {
                            "email": "Elmira92@yahoo.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Jane30@gmail.com",
                        },
                    ],
                    "name": "Jewelry",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 3674489.0,
            "storage_quota_available": 7748057.0,
            "storage_quota_used": 301727.0,
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
            "updated_at": parse_datetime("2022-02-19T07:01:46.451Z"),
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

## create_hris_group

Create a group

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisGroup" method="post" path="/hris/{connection_id}/group" example="hris_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_group(request={
        "hris_group": {
            "created_at": parse_datetime("2023-11-01T13:13:40.714Z"),
            "description": "Absorbeo casso.",
            "id": "75c0e738-bb94-4051-9c72-8e563c3e92ea",
            "is_active": False,
            "name": "Games",
            "type": shared.HrisGroupType.BUSINESS_UNIT,
            "updated_at": parse_datetime("2026-04-23T14:24:36.666Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_group is not None

    # Handle response
    print(res.hris_group)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateHrisGroupRequest](../../models/operations/createhrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateHrisGroupResponse](../../models/operations/createhrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_location

Create a location

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisLocation" method="post" path="/hris/{connection_id}/location" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "f7f353fd-05db-464e-813d-53ebc1a79d24",
            "id": "854e19af-cf20-4edc-8a76-c80b50974f65",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-09T00:39:51.875Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisLocationRequest](../../models/operations/createhrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisLocationResponse](../../models/operations/createhrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_taxonomy

Create a taxonomy

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTaxonomy" method="post" path="/hris/{connection_id}/taxonomy" example="hris_taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_taxonomy(request={
        "hris_taxonomy": {
            "created_at": parse_datetime("2022-06-23T02:10:00.789Z"),
            "description": "Apto demonstro audacia adstringo cursim tristis solio careo.",
            "domain": "Electronics",
            "id": "ede085db-5709-4d53-a490-746f3de5be17",
            "is_active": False,
            "name": "International Functionality Architect",
            "parent_id": "6524b2a7-6520-4e15-8c4e-1aa6793db837",
            "role_ids": [
                "2b1ef757-eb4c-4207-8af1-929afe49cd65",
            ],
            "subcategory": "Bamboo",
            "type": shared.HrisTaxonomyType.KNOWLEDGE,
            "updated_at": parse_datetime("2023-05-22T04:57:25.374Z"),
            "url": "https://our-polarisation.name",
        },
        "connection_id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisTaxonomyRequest](../../models/operations/createhristaxonomyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisTaxonomyResponse](../../models/operations/createhristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_timeoff

Create a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeoff" method="post" path="/hris/{connection_id}/timeoff" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-20T21:02:37.695Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2024-12-07T13:50:55.449Z"),
            "id": "efd938fb-bb4a-492d-b313-90f0578f3165",
            "is_paid": True,
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-08-23T06:56:44.757Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-07T19:34:54.248Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateHrisTimeoffRequest](../../models/operations/createhristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateHrisTimeoffResponse](../../models/operations/createhristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_hris_timeshift

Create a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTimeshift" method="post" path="/hris/{connection_id}/timeshift" example="hris_timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.create_hris_timeshift(request={
        "hris_timeshift": {
            "approved_at": parse_datetime("2023-06-05T14:31:38.445Z"),
            "compensation": [
                {
                    "amount": 76761.0,
                    "currency": "JPY",
                    "frequency": shared.HrisCompensationFrequency.HOUR,
                    "notes": "Annus adficio suasoria architecto aggero.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-07-01T23:53:15.738Z"),
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2026-08-25T08:28:11.837Z"),
            "hours": 8.0,
            "id": "8091d49f-00cf-416b-a771-e6834ab7026d",
            "is_approved": True,
            "start_at": parse_datetime("2023-06-24T19:29:28.668Z"),
            "updated_at": parse_datetime("2021-06-22T20:53:14.292Z"),
        },
        "connection_id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateHrisTimeshiftRequest](../../models/operations/createhristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateHrisTimeshiftResponse](../../models/operations/createhristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_attendance

Retrieve an attendance

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisAttendance" method="get" path="/hris/{connection_id}/attendance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_attendance(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_attendance is not None

    # Handle response
    print(res.hris_attendance)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetHrisAttendanceRequest](../../models/operations/gethrisattendancerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetHrisAttendanceResponse](../../models/operations/gethrisattendanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_bankaccount

Retrieve a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBankaccount" method="get" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_bankaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetHrisBankaccountRequest](../../models/operations/gethrisbankaccountrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetHrisBankaccountResponse](../../models/operations/gethrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_benefit

Retrieve a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBenefit" method="get" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_benefit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisBenefitRequest](../../models/operations/gethrisbenefitrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisBenefitResponse](../../models/operations/gethrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_company

Retrieve a company

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisCompany" method="get" path="/hris/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisCompanyRequest](../../models/operations/gethriscompanyrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisCompanyResponse](../../models/operations/gethriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_deduction

Retrieve a deduction

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDeduction" method="get" path="/hris/{connection_id}/deduction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_deduction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisDeductionRequest](../../models/operations/gethrisdeductionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetHrisDeductionResponse](../../models/operations/gethrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_device

Retrieve a device

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDevice" method="get" path="/hris/{connection_id}/device/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_device(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetHrisDeviceRequest](../../models/operations/gethrisdevicerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetHrisDeviceResponse](../../models/operations/gethrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_document

Retrieve a document

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisDocument" method="get" path="/hris/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_document(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisDocumentRequest](../../models/operations/gethrisdocumentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisDocumentResponse](../../models/operations/gethrisdocumentresponse.md)**

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

    res = unified_to.hris.get_hris_employee(request={
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

## get_hris_group

Retrieve a group

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisGroup" method="get" path="/hris/{connection_id}/group/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_group(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_group is not None

    # Handle response
    print(res.hris_group)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetHrisGroupRequest](../../models/operations/gethrisgrouprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetHrisGroupResponse](../../models/operations/gethrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_location

Retrieve a location

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisLocation" method="get" path="/hris/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_location(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisLocationRequest](../../models/operations/gethrislocationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisLocationResponse](../../models/operations/gethrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_payslip

Retrieve a payslip

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisPayslip" method="get" path="/hris/{connection_id}/payslip/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_payslip(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_payslip is not None

    # Handle response
    print(res.hris_payslip)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisPayslipRequest](../../models/operations/gethrispaysliprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisPayslipResponse](../../models/operations/gethrispayslipresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_taxonomy

Retrieve a taxonomy

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTaxonomy" method="get" path="/hris/{connection_id}/taxonomy/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_taxonomy(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisTaxonomyRequest](../../models/operations/gethristaxonomyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisTaxonomyResponse](../../models/operations/gethristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeoff

Retrieve a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeoff" method="get" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_timeoff(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisTimeoffRequest](../../models/operations/gethristimeoffrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisTimeoffResponse](../../models/operations/gethristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_timeshift

Retrieve a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTimeshift" method="get" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.get_hris_timeshift(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisTimeshiftRequest](../../models/operations/gethristimeshiftrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetHrisTimeshiftResponse](../../models/operations/gethristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_attendances

List all attendances

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisAttendances" method="get" path="/hris/{connection_id}/attendance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_attendances(request={
        "connection_id": "<id>",
    })

    assert res.hris_attendances is not None

    # Handle response
    print(res.hris_attendances)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListHrisAttendancesRequest](../../models/operations/listhrisattendancesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListHrisAttendancesResponse](../../models/operations/listhrisattendancesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_bankaccounts

List all bankaccounts

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBankaccounts" method="get" path="/hris/{connection_id}/bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_bankaccounts(request={
        "connection_id": "<id>",
    })

    assert res.hris_bankaccounts is not None

    # Handle response
    print(res.hris_bankaccounts)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListHrisBankaccountsRequest](../../models/operations/listhrisbankaccountsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListHrisBankaccountsResponse](../../models/operations/listhrisbankaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_benefits

List all benefits

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBenefits" method="get" path="/hris/{connection_id}/benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_benefits(request={
        "connection_id": "<id>",
    })

    assert res.hris_benefits is not None

    # Handle response
    print(res.hris_benefits)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisBenefitsRequest](../../models/operations/listhrisbenefitsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisBenefitsResponse](../../models/operations/listhrisbenefitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_companies

List all companies

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisCompanies" method="get" path="/hris/{connection_id}/company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_companies(request={
        "connection_id": "<id>",
    })

    assert res.hris_companies is not None

    # Handle response
    print(res.hris_companies)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisCompaniesRequest](../../models/operations/listhriscompaniesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisCompaniesResponse](../../models/operations/listhriscompaniesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_deductions

List all deductions

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDeductions" method="get" path="/hris/{connection_id}/deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_deductions(request={
        "connection_id": "<id>",
    })

    assert res.hris_deductions is not None

    # Handle response
    print(res.hris_deductions)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisDeductionsRequest](../../models/operations/listhrisdeductionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisDeductionsResponse](../../models/operations/listhrisdeductionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_devices

List all devices

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDevices" method="get" path="/hris/{connection_id}/device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_devices(request={
        "connection_id": "<id>",
    })

    assert res.hris_devices is not None

    # Handle response
    print(res.hris_devices)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListHrisDevicesRequest](../../models/operations/listhrisdevicesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListHrisDevicesResponse](../../models/operations/listhrisdevicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_documents

List all documents

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisDocuments" method="get" path="/hris/{connection_id}/document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_documents(request={
        "connection_id": "<id>",
    })

    assert res.hris_documents is not None

    # Handle response
    print(res.hris_documents)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisDocumentsRequest](../../models/operations/listhrisdocumentsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisDocumentsResponse](../../models/operations/listhrisdocumentsresponse.md)**

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

    res = unified_to.hris.list_hris_employees(request={
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

## list_hris_groups

List all groups

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisGroups" method="get" path="/hris/{connection_id}/group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_groups(request={
        "connection_id": "<id>",
    })

    assert res.hris_groups is not None

    # Handle response
    print(res.hris_groups)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListHrisGroupsRequest](../../models/operations/listhrisgroupsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListHrisGroupsResponse](../../models/operations/listhrisgroupsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_locations

List all locations

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisLocations" method="get" path="/hris/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_locations(request={
        "connection_id": "<id>",
    })

    assert res.hris_locations is not None

    # Handle response
    print(res.hris_locations)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisLocationsRequest](../../models/operations/listhrislocationsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisLocationsResponse](../../models/operations/listhrislocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_payslips

List all payslips

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisPayslips" method="get" path="/hris/{connection_id}/payslip" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_payslips(request={
        "connection_id": "<id>",
    })

    assert res.hris_payslips is not None

    # Handle response
    print(res.hris_payslips)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisPayslipsRequest](../../models/operations/listhrispayslipsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisPayslipsResponse](../../models/operations/listhrispayslipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_taxonomies

List all taxonomies

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTaxonomies" method="get" path="/hris/{connection_id}/taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_taxonomies(request={
        "connection_id": "<id>",
    })

    assert res.hris_taxonomies is not None

    # Handle response
    print(res.hris_taxonomies)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisTaxonomiesRequest](../../models/operations/listhristaxonomiesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisTaxonomiesResponse](../../models/operations/listhristaxonomiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeoffs

List all timeoffs

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeoffs" method="get" path="/hris/{connection_id}/timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_timeoffs(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeoffs is not None

    # Handle response
    print(res.hris_timeoffs)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisTimeoffsRequest](../../models/operations/listhristimeoffsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisTimeoffsResponse](../../models/operations/listhristimeoffsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_timeshifts

List all timeshifts

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTimeshifts" method="get" path="/hris/{connection_id}/timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.list_hris_timeshifts(request={
        "connection_id": "<id>",
    })

    assert res.hris_timeshifts is not None

    # Handle response
    print(res.hris_timeshifts)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisTimeshiftsRequest](../../models/operations/listhristimeshiftsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisTimeshiftsResponse](../../models/operations/listhristimeshiftsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_attendance

Update an attendance

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisAttendance" method="patch" path="/hris/{connection_id}/attendance/{id}" example="hris_attendance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-08-13T10:36:02.582Z"),
            "breaks": [
                {
                    "duration_minutes": 12.0,
                    "end_at": parse_datetime("2023-10-22T16:22:21.282Z"),
                    "id": "d60a1001-5a8a-4991-8c21-f4da6036cc87",
                    "is_paid": True,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-15T20:48:40.852Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "UGX",
            "declared_tips_amount": 161.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-06T03:55:51.527Z"),
            "hourly_rate": 53.0,
            "hours": 10.0,
            "id": "cbcfba0c-c599-4187-8cc1-b796e089ae62",
            "job_name": "Global Creative Supervisor",
            "non_cash_tips_amount": 54.0,
            "start_at": parse_datetime("2021-11-09T10:25:57.026Z"),
            "status": shared.HrisAttendanceStatus.CLOSED,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-17T01:24:59.757Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_attendance is not None

    # Handle response
    print(res.hris_attendance)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchHrisAttendanceRequest](../../models/operations/patchhrisattendancerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchHrisAttendanceResponse](../../models/operations/patchhrisattendanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_bankaccount

Update a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBankaccount" method="patch" path="/hris/{connection_id}/bankaccount/{id}" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "6b53796b-c6e2-4608-939f-57d8d920c7b2",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.792Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchHrisBankaccountRequest](../../models/operations/patchhrisbankaccountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchHrisBankaccountResponse](../../models/operations/patchhrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_benefit

Update a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBenefit" method="patch" path="/hris/{connection_id}/benefit/{id}" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "20ebb126-9b3a-4c47-8f83-06f96f663e09",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-06T11:00:21.279Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisBenefitRequest](../../models/operations/patchhrisbenefitrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisBenefitResponse](../../models/operations/patchhrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisCompany" method="patch" path="/hris/{connection_id}/company/{id}" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "6d8a376c-449b-4d6f-8921-ca1ab6158e9a",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.930Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisCompanyRequest](../../models/operations/patchhriscompanyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisCompanyResponse](../../models/operations/patchhriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_deduction

Update a deduction

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDeduction" method="patch" path="/hris/{connection_id}/deduction/{id}" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_deduction(request={
        "hris_deduction": {
            "amount": 139655.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_ONLY,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "end_at": parse_datetime("2026-05-22T22:51:41.904Z"),
            "frequency": shared.HrisDeductionFrequency.MONTH,
            "id": "2aec3d2c-839a-4dda-90d3-91870b50eae7",
            "is_active": False,
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-02-18T04:37:41.123Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-01T23:41:41.377Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchHrisDeductionRequest](../../models/operations/patchhrisdeductionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchHrisDeductionResponse](../../models/operations/patchhrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_device

Update a device

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDevice" method="patch" path="/hris/{connection_id}/device/{id}" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "6ad75d41-833e-41c9-af5a-7c98b7cac6f5",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-21T00:56:05.174Z"),
            "version": "2.20.17",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchHrisDeviceRequest](../../models/operations/patchhrisdevicerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchHrisDeviceResponse](../../models/operations/patchhrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisDocument" method="patch" path="/hris/{connection_id}/document/{id}" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "b42682b1-d9f4-4260-af8a-f6317dd1bd80",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-17T01:54:33.589Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisDocumentRequest](../../models/operations/patchhrisdocumentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisDocumentResponse](../../models/operations/patchhrisdocumentresponse.md)**

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

    res = unified_to.hris.patch_hris_employee(request={
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
                    "amount": 69148.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.EQUITY,
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
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": True,
            "hired_at": parse_datetime("2023-05-10T16:14:24.268Z"),
            "id": "5a45c156-b945-45a7-bdbb-7fcc013a456d",
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
                    "id": "a06af6d2-ccab-4f6e-b714-1de7dc125067",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tenetur",
                },
            ],
            "name": "Zetta Prohaska",
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
                    "type": shared.HrisEmployeerelationshipType.EMERGENCY,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                        {
                            "email": "Princess_Rath43@gmail.com",
                        },
                        {
                            "email": "Elmira92@yahoo.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Jane30@gmail.com",
                        },
                    ],
                    "name": "Jewelry",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 3674489.0,
            "storage_quota_available": 7748057.0,
            "storage_quota_used": 301727.0,
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
            "updated_at": parse_datetime("2022-02-19T07:01:46.473Z"),
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

## patch_hris_group

Update a group

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisGroup" method="patch" path="/hris/{connection_id}/group/{id}" example="hris_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_group(request={
        "hris_group": {
            "created_at": parse_datetime("2023-11-01T13:13:40.714Z"),
            "description": "Absorbeo casso.",
            "id": "8d454ca4-ebee-4004-9ee1-070a8a4f8f74",
            "is_active": False,
            "name": "Games",
            "type": shared.HrisGroupType.BUSINESS_UNIT,
            "updated_at": parse_datetime("2026-04-23T14:24:36.672Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_group is not None

    # Handle response
    print(res.hris_group)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchHrisGroupRequest](../../models/operations/patchhrisgrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchHrisGroupResponse](../../models/operations/patchhrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_location

Update a location

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisLocation" method="patch" path="/hris/{connection_id}/location/{id}" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "633d799f-e467-4730-a2c1-d0442c073b57",
            "id": "d267ea88-128c-42f6-8cdf-1a9e361e0183",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-09T00:39:51.880Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisLocationRequest](../../models/operations/patchhrislocationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisLocationResponse](../../models/operations/patchhrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeoff

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeoff" method="patch" path="/hris/{connection_id}/timeoff/{id}" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-20T21:02:37.696Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2024-12-07T13:50:55.454Z"),
            "id": "c38c4f38-07e2-4fb7-b3aa-93df41a86943",
            "is_paid": True,
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-08-23T06:56:44.760Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-07T19:34:54.250Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchHrisTimeoffRequest](../../models/operations/patchhristimeoffrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchHrisTimeoffResponse](../../models/operations/patchhristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_timeshift

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTimeshift" method="patch" path="/hris/{connection_id}/timeshift/{id}" example="hris_timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.patch_hris_timeshift(request={
        "hris_timeshift": {
            "approved_at": parse_datetime("2023-06-05T14:31:38.450Z"),
            "compensation": [
                {
                    "amount": 76761.0,
                    "currency": "JPY",
                    "frequency": shared.HrisCompensationFrequency.HOUR,
                    "notes": "Annus adficio suasoria architecto aggero.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-07-01T23:53:15.738Z"),
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2026-08-25T08:28:11.847Z"),
            "hours": 8.0,
            "id": "7cccfab5-5f8c-4543-ba66-c6178393a826",
            "is_approved": True,
            "start_at": parse_datetime("2023-06-24T19:29:28.673Z"),
            "updated_at": parse_datetime("2021-06-22T20:53:14.295Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchHrisTimeshiftRequest](../../models/operations/patchhristimeshiftrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchHrisTimeshiftResponse](../../models/operations/patchhristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_attendance

Remove an attendance

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisAttendance" method="delete" path="/hris/{connection_id}/attendance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_attendance(request={
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
| `request`                                                                                        | [operations.RemoveHrisAttendanceRequest](../../models/operations/removehrisattendancerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveHrisAttendanceResponse](../../models/operations/removehrisattendanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_bankaccount

Remove a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBankaccount" method="delete" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_bankaccount(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveHrisBankaccountRequest](../../models/operations/removehrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveHrisBankaccountResponse](../../models/operations/removehrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_benefit

Remove a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBenefit" method="delete" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_benefit(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveHrisBenefitRequest](../../models/operations/removehrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisBenefitResponse](../../models/operations/removehrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_company

Remove a company

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisCompany" method="delete" path="/hris/{connection_id}/company/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_company(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveHrisCompanyRequest](../../models/operations/removehriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisCompanyResponse](../../models/operations/removehriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_deduction

Remove a deduction

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDeduction" method="delete" path="/hris/{connection_id}/deduction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_deduction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveHrisDeductionRequest](../../models/operations/removehrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveHrisDeductionResponse](../../models/operations/removehrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_device

Remove a device

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDevice" method="delete" path="/hris/{connection_id}/device/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_device(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveHrisDeviceRequest](../../models/operations/removehrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveHrisDeviceResponse](../../models/operations/removehrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_document

Remove a document

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisDocument" method="delete" path="/hris/{connection_id}/document/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_document(request={
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
| `request`                                                                                    | [operations.RemoveHrisDocumentRequest](../../models/operations/removehrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisDocumentResponse](../../models/operations/removehrisdocumentresponse.md)**

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

    res = unified_to.hris.remove_hris_employee(request={
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

## remove_hris_group

Remove a group

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisGroup" method="delete" path="/hris/{connection_id}/group/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_group(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveHrisGroupRequest](../../models/operations/removehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveHrisGroupResponse](../../models/operations/removehrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_location

Remove a location

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisLocation" method="delete" path="/hris/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_location(request={
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
| `request`                                                                                    | [operations.RemoveHrisLocationRequest](../../models/operations/removehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisLocationResponse](../../models/operations/removehrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeoff

Remove a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeoff" method="delete" path="/hris/{connection_id}/timeoff/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_timeoff(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveHrisTimeoffRequest](../../models/operations/removehristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveHrisTimeoffResponse](../../models/operations/removehristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_timeshift

Remove a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTimeshift" method="delete" path="/hris/{connection_id}/timeshift/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.remove_hris_timeshift(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveHrisTimeshiftRequest](../../models/operations/removehristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveHrisTimeshiftResponse](../../models/operations/removehristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_attendance

Update an attendance

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisAttendance" method="put" path="/hris/{connection_id}/attendance/{id}" example="hris_attendance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-08-13T10:36:02.582Z"),
            "breaks": [
                {
                    "duration_minutes": 12.0,
                    "end_at": parse_datetime("2023-10-22T16:22:21.282Z"),
                    "id": "d60a1001-5a8a-4991-8c21-f4da6036cc87",
                    "is_paid": True,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-15T20:48:40.852Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "UGX",
            "declared_tips_amount": 161.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-06T03:55:51.527Z"),
            "hourly_rate": 53.0,
            "hours": 10.0,
            "id": "cbcfba0c-c599-4187-8cc1-b796e089ae62",
            "job_name": "Global Creative Supervisor",
            "non_cash_tips_amount": 54.0,
            "start_at": parse_datetime("2021-11-09T10:25:57.026Z"),
            "status": shared.HrisAttendanceStatus.CLOSED,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-17T01:24:59.757Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_attendance is not None

    # Handle response
    print(res.hris_attendance)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateHrisAttendanceRequest](../../models/operations/updatehrisattendancerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateHrisAttendanceResponse](../../models/operations/updatehrisattendanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_bankaccount

Update a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBankaccount" method="put" path="/hris/{connection_id}/bankaccount/{id}" example="hris_bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_bankaccount(request={
        "hris_bankaccount": {
            "account_number": "****3777",
            "account_number_last4": "3777",
            "account_type": shared.HrisBankaccountAccountType.CHECKING,
            "bank_name": "Huel Group",
            "created_at": parse_datetime("2019-11-16T16:43:45.976Z"),
            "id": "6b53796b-c6e2-4608-939f-57d8d920c7b2",
            "is_primary": False,
            "name": "Checking Account",
            "routing_number": "448650724",
            "updated_at": parse_datetime("2025-06-04T11:30:29.792Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateHrisBankaccountRequest](../../models/operations/updatehrisbankaccountrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateHrisBankaccountResponse](../../models/operations/updatehrisbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_benefit

Update a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBenefit" method="put" path="/hris/{connection_id}/benefit/{id}" example="hris_benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_benefit(request={
        "hris_benefit": {
            "coverage_level": shared.CoverageLevel.EMPLOYEE_SPOUSE,
            "created_at": parse_datetime("2020-06-11T01:24:05.654Z"),
            "currency": "JOD",
            "description": "Vomito voluptas dolor sed.",
            "employer_contribution_amount": 185006.0,
            "employer_contribution_max_amount": 179093.0,
            "employer_contribution_type": shared.EmployerContributionType.PERCENTAGE,
            "frequency": shared.HrisBenefitFrequency.HOUR,
            "id": "20ebb126-9b3a-4c47-8f83-06f96f663e09",
            "is_active": False,
            "name": "Frozen Wooden Ball",
            "tax": shared.Tax.PRE_TAX,
            "type": shared.HrisBenefitType.GARNISHMENT,
            "updated_at": parse_datetime("2023-03-06T11:00:21.279Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisBenefitRequest](../../models/operations/updatehrisbenefitrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisBenefitResponse](../../models/operations/updatehrisbenefitresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_company

Update a company

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisCompany" method="put" path="/hris/{connection_id}/company/{id}" example="hris_company" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_company(request={
        "hris_company": {
            "address": {
                "address1": "2549 Church Walk",
                "city": "Lake Nettiebury",
                "country_code": "US",
                "postal_code": "32877-4898",
                "region": "Idaho",
                "region_code": "PA",
            },
            "created_at": parse_datetime("2021-05-02T22:27:38.970Z"),
            "id": "6d8a376c-449b-4d6f-8921-ca1ab6158e9a",
            "legal_name": "Schultz LLC",
            "name": "Gottlieb Group",
            "updated_at": parse_datetime("2026-09-05T21:10:56.930Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_company is not None

    # Handle response
    print(res.hris_company)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisCompanyRequest](../../models/operations/updatehriscompanyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisCompanyResponse](../../models/operations/updatehriscompanyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_deduction

Update a deduction

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDeduction" method="put" path="/hris/{connection_id}/deduction/{id}" example="hris_deduction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_deduction(request={
        "hris_deduction": {
            "amount": 139655.0,
            "coverage_level": shared.HrisDeductionCoverageLevel.EMPLOYEE_ONLY,
            "created_at": parse_datetime("2020-02-05T01:46:31.384Z"),
            "end_at": parse_datetime("2026-05-22T22:51:41.904Z"),
            "frequency": shared.HrisDeductionFrequency.MONTH,
            "id": "2aec3d2c-839a-4dda-90d3-91870b50eae7",
            "is_active": False,
            "notes": "Carmen desidero.",
            "start_at": parse_datetime("2025-02-18T04:37:41.123Z"),
            "type": shared.HrisDeductionType.FIXED,
            "updated_at": parse_datetime("2024-03-01T23:41:41.377Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_deduction is not None

    # Handle response
    print(res.hris_deduction)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateHrisDeductionRequest](../../models/operations/updatehrisdeductionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateHrisDeductionResponse](../../models/operations/updatehrisdeductionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_device

Update a device

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDevice" method="put" path="/hris/{connection_id}/device/{id}" example="hris_device" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_device(request={
        "hris_device": {
            "admin_user_ids": [],
            "asset_tag": "dpho9OuFNG",
            "created_at": parse_datetime("2019-04-04T17:11:40.322Z"),
            "has_antivirus": False,
            "has_firewall": True,
            "has_hd_encrypted": True,
            "has_password_manager": True,
            "has_screenlock": True,
            "id": "6ad75d41-833e-41c9-af5a-7c98b7cac6f5",
            "is_missing": False,
            "manufacturer": "Sanford - Hamill",
            "model": "Refined",
            "name": "cross_contamination_if.rar",
            "os": "monitor",
            "os_version": "1.12.16",
            "updated_at": parse_datetime("2023-05-21T00:56:05.174Z"),
            "version": "2.20.17",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_device is not None

    # Handle response
    print(res.hris_device)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateHrisDeviceRequest](../../models/operations/updatehrisdevicerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateHrisDeviceResponse](../../models/operations/updatehrisdeviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_document

Update a document

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisDocument" method="put" path="/hris/{connection_id}/document/{id}" example="hris_document" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_document(request={
        "hris_document": {
            "created_at": parse_datetime("2022-10-27T11:47:26.086Z"),
            "document_url": "https://sore-decision.biz/",
            "filename": "ridge_forager.xsl",
            "id": "b42682b1-d9f4-4260-af8a-f6317dd1bd80",
            "type": shared.HrisDocumentType.POLICY,
            "updated_at": parse_datetime("2025-09-17T01:54:33.589Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_document is not None

    # Handle response
    print(res.hris_document)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisDocumentRequest](../../models/operations/updatehrisdocumentrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisDocumentResponse](../../models/operations/updatehrisdocumentresponse.md)**

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

    res = unified_to.hris.update_hris_employee(request={
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
                    "amount": 69148.0,
                    "currency": "CRC",
                    "frequency": shared.HrisCompensationFrequency.QUARTER,
                    "notes": "Tergeo laborum laboriosam tutis.",
                    "type": shared.HrisCompensationType.EQUITY,
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
            "gender": shared.HrisEmployeeGender.INTERSEX,
            "has_mfa": True,
            "hired_at": parse_datetime("2023-05-10T16:14:24.268Z"),
            "id": "5a45c156-b945-45a7-bdbb-7fcc013a456d",
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
                    "id": "a06af6d2-ccab-4f6e-b714-1de7dc125067",
                    "namespace": "custom",
                    "slug": "custom_property",
                    "value": "tenetur",
                },
            ],
            "name": "Zetta Prohaska",
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
                    "type": shared.HrisEmployeerelationshipType.EMERGENCY,
                },
                {
                    "emails": [
                        {
                            "email": "Benedict_Wisozk83@hotmail.com",
                        },
                        {
                            "email": "Princess_Rath43@gmail.com",
                        },
                        {
                            "email": "Elmira92@yahoo.com",
                        },
                    ],
                    "name": "Music",
                    "type": shared.HrisEmployeerelationshipType.FRIEND,
                },
                {
                    "emails": [
                        {
                            "email": "Jane30@gmail.com",
                        },
                    ],
                    "name": "Jewelry",
                    "type": shared.HrisEmployeerelationshipType.SIBLING,
                },
            ],
            "salutation": "Miss",
            "ssn_sin": "yMRtj0Q3xO",
            "storage_quota_allocated": 3674489.0,
            "storage_quota_available": 7748057.0,
            "storage_quota_used": 301727.0,
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
            "updated_at": parse_datetime("2022-02-19T07:01:46.473Z"),
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

## update_hris_group

Update a group

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisGroup" method="put" path="/hris/{connection_id}/group/{id}" example="hris_group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_group(request={
        "hris_group": {
            "created_at": parse_datetime("2023-11-01T13:13:40.714Z"),
            "description": "Absorbeo casso.",
            "id": "8d454ca4-ebee-4004-9ee1-070a8a4f8f74",
            "is_active": False,
            "name": "Games",
            "type": shared.HrisGroupType.BUSINESS_UNIT,
            "updated_at": parse_datetime("2026-04-23T14:24:36.672Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_group is not None

    # Handle response
    print(res.hris_group)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateHrisGroupRequest](../../models/operations/updatehrisgrouprequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateHrisGroupResponse](../../models/operations/updatehrisgroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_location

Update a location

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisLocation" method="put" path="/hris/{connection_id}/location/{id}" example="hris_location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_location(request={
        "hris_location": {
            "address": {
                "address1": "2743 Connelly Summit",
                "address2": "Apt. 350",
                "city": "Titusville",
                "country_code": "US",
                "postal_code": "16154-1095",
                "region": "Oregon",
                "region_code": "AL",
            },
            "created_at": parse_datetime("2021-07-18T10:32:01.414Z"),
            "currency": "MUR",
            "description": "Acervus caries.",
            "external_identifier": "633d799f-e467-4730-a2c1-d0442c073b57",
            "id": "d267ea88-128c-42f6-8cdf-1a9e361e0183",
            "is_active": True,
            "is_hq": False,
            "language_locale": "fr",
            "name": "adhuc",
            "telephones": [
                {
                    "telephone": "(710) 550-6997",
                    "type": shared.HrisTelephoneType.FAX,
                },
                {
                    "telephone": "(208) 555-8542",
                    "type": shared.HrisTelephoneType.HOME,
                },
                {
                    "telephone": "(712) 473-5482",
                    "type": shared.HrisTelephoneType.FAX,
                },
            ],
            "timezone": "America/Guyana",
            "updated_at": parse_datetime("2023-06-09T00:39:51.880Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_location is not None

    # Handle response
    print(res.hris_location)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisLocationRequest](../../models/operations/updatehrislocationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisLocationResponse](../../models/operations/updatehrislocationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeoff

Update a timeoff

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeoff" method="put" path="/hris/{connection_id}/timeoff/{id}" example="hris_timeoff" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_timeoff(request={
        "hris_timeoff": {
            "approved_at": parse_datetime("2022-02-20T21:02:37.696Z"),
            "comments": "Blandior ventus curiositas amplitudo.",
            "created_at": parse_datetime("2021-10-06T18:00:20.615Z"),
            "duration": 4.0,
            "duration_type": shared.DurationType.DAY,
            "end_at": parse_datetime("2024-12-07T13:50:55.454Z"),
            "id": "c38c4f38-07e2-4fb7-b3aa-93df41a86943",
            "is_paid": True,
            "original_type": "acerbitas ut",
            "reason": "verto",
            "start_at": parse_datetime("2023-08-23T06:56:44.760Z"),
            "status": shared.HrisTimeoffStatus.DENIED,
            "type": shared.HrisTimeoffType.IN_LIEU,
            "updated_at": parse_datetime("2022-07-07T19:34:54.250Z"),
            "user_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeoff is not None

    # Handle response
    print(res.hris_timeoff)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateHrisTimeoffRequest](../../models/operations/updatehristimeoffrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateHrisTimeoffResponse](../../models/operations/updatehristimeoffresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_timeshift

Update a timeshift

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTimeshift" method="put" path="/hris/{connection_id}/timeshift/{id}" example="hris_timeshift" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.hris.update_hris_timeshift(request={
        "hris_timeshift": {
            "approved_at": parse_datetime("2023-06-05T14:31:38.450Z"),
            "compensation": [
                {
                    "amount": 76761.0,
                    "currency": "JPY",
                    "frequency": shared.HrisCompensationFrequency.HOUR,
                    "notes": "Annus adficio suasoria architecto aggero.",
                    "type": shared.HrisCompensationType.OTHER,
                },
            ],
            "created_at": parse_datetime("2019-07-01T23:53:15.738Z"),
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2026-08-25T08:28:11.847Z"),
            "hours": 8.0,
            "id": "7cccfab5-5f8c-4543-ba66-c6178393a826",
            "is_approved": True,
            "start_at": parse_datetime("2023-06-24T19:29:28.673Z"),
            "updated_at": parse_datetime("2021-06-22T20:53:14.295Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_timeshift is not None

    # Handle response
    print(res.hris_timeshift)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateHrisTimeshiftRequest](../../models/operations/updatehristimeshiftrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateHrisTimeshiftResponse](../../models/operations/updatehristimeshiftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |