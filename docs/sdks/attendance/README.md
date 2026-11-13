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

Creates a HrisAttendance. Provide the unified HrisAttendance fields in the request body; they are mapped to the provider's API. Returns the created HrisAttendance.

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
            "approved_at": parse_datetime("2021-09-20T01:41:07.252Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-25T16:26:22.868Z"),
                    "id": "f79012d2-06d3-40a6-a0d2-483eaeb3eeee",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-08T18:54:01.227Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-05T06:59:50.614Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "f611b474-e6e0-4501-80c0-0b02b0a2be87",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T03:46:49.466Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-21T20:15:17.056Z"),
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

Retrieves a single HrisAttendance by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of HrisAttendances. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the HrisAttendance identified by `id`. Provide the unified HrisAttendance fields to change in the request body.

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
            "approved_at": parse_datetime("2021-09-20T01:41:07.253Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-25T16:26:22.879Z"),
                    "id": "c5f745f2-45f5-451e-90ac-80efa4472ad1",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-08T18:54:01.237Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-05T06:59:50.626Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "7997764c-fa44-4c67-a54f-6e576ef54cc0",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T03:46:49.468Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-21T20:15:17.058Z"),
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

Deletes the HrisAttendance identified by `id`.

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

Updates the HrisAttendance identified by `id`. Provide the unified HrisAttendance fields to change in the request body.

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
            "approved_at": parse_datetime("2021-09-20T01:41:07.253Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-02-25T16:26:22.879Z"),
                    "id": "c5f745f2-45f5-451e-90ac-80efa4472ad1",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-08T18:54:01.237Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-05T06:59:50.626Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "7997764c-fa44-4c67-a54f-6e576ef54cc0",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T03:46:49.468Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "America/Atikokan",
            "updated_at": parse_datetime("2022-01-21T20:15:17.058Z"),
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