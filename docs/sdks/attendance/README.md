# Attendance

## Overview

### Available Operations

* [create_hris_attendance](#create_hris_attendance) - Create an attendance
* [get_hris_attendance](#get_hris_attendance) - Retrieve an attendance
* [list_hris_attendances](#list_hris_attendances) - List all attendances
* [patch_hris_attendance](#patch_hris_attendance) - Update an attendance
* [remove_hris_attendance](#remove_hris_attendance) - Remove an attendance
* [update_hris_attendance](#update_hris_attendance) - Update an attendance

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

    res = unified_to.attendance.create_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-09-19T13:29:51.219Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-13T23:10:02.182Z"),
                    "id": "7144f26d-d531-44c3-a145-69a3200233b4",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-29T10:36:12.825Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-22T16:38:49.792Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "63651294-24dd-4ad5-b336-92aa45c2f811",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-10T23:31:01.438Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-19T18:35:11.706Z"),
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

    res = unified_to.attendance.get_hris_attendance(request={
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

    res = unified_to.attendance.list_hris_attendances(request={
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

    res = unified_to.attendance.patch_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-09-19T13:29:51.219Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-13T23:10:02.197Z"),
                    "id": "0de77d03-f775-428f-a0d9-b147df14cb7d",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-29T10:36:12.838Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-22T16:38:49.808Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "8d202e21-8d8a-43b8-82da-6517a39217b8",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-10T23:31:01.440Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-19T18:35:11.708Z"),
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

    res = unified_to.attendance.remove_hris_attendance(request={
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

    res = unified_to.attendance.update_hris_attendance(request={
        "hris_attendance": {
            "address": {
                "address1": "14108 Allie Flats",
                "city": "Kearaborough",
                "country_code": "US",
                "postal_code": "23844-2344",
                "region": "Tennessee",
                "region_code": "CA",
            },
            "approved_at": parse_datetime("2021-09-19T13:29:51.219Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-13T23:10:02.197Z"),
                    "id": "0de77d03-f775-428f-a0d9-b147df14cb7d",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-10-29T10:36:12.838Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-04-22T16:38:49.808Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "8d202e21-8d8a-43b8-82da-6517a39217b8",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-10T23:31:01.440Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-19T18:35:11.708Z"),
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