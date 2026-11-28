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
                "address1": "18002 Elm Street",
                "city": "Port Gaetano",
                "country_code": "US",
                "postal_code": "42344",
                "region": "Vermont",
                "region_code": "MI",
            },
            "approved_at": parse_datetime("2021-09-20T09:13:55.287Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-03-03T22:36:12.717Z"),
                    "id": "beabe61e-8d44-4584-a5da-2df1fd7e60c0",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-15T04:38:44.443Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-13T02:12:45.435Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "76664e05-36ad-4920-8f34-18432010ff75",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T21:16:51.834Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "Africa/Ouagadougou",
            "updated_at": parse_datetime("2022-01-23T03:00:33.309Z"),
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
                "address1": "18002 Elm Street",
                "city": "Port Gaetano",
                "country_code": "US",
                "postal_code": "42344",
                "region": "Vermont",
                "region_code": "MI",
            },
            "approved_at": parse_datetime("2021-09-20T09:13:55.288Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-03-03T22:36:12.727Z"),
                    "id": "323f51bb-9713-4b67-b8a4-b07f47ef336e",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-15T04:38:44.452Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-13T02:12:45.446Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "22d86359-cf1d-452f-9164-d004f875a149",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T21:16:51.835Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "Africa/Ouagadougou",
            "updated_at": parse_datetime("2022-01-23T03:00:33.311Z"),
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
                "address1": "18002 Elm Street",
                "city": "Port Gaetano",
                "country_code": "US",
                "postal_code": "42344",
                "region": "Vermont",
                "region_code": "MI",
            },
            "approved_at": parse_datetime("2021-09-20T09:13:55.288Z"),
            "breaks": [
                {
                    "duration_minutes": 51.0,
                    "end_at": parse_datetime("2024-03-03T22:36:12.727Z"),
                    "id": "323f51bb-9713-4b67-b8a4-b07f47ef336e",
                    "is_paid": False,
                    "name": "Lunch",
                    "start_at": parse_datetime("2023-11-15T04:38:44.452Z"),
                },
            ],
            "created_at": parse_datetime("2021-08-10T19:43:18.452Z"),
            "currency": "EUR",
            "declared_tips_amount": 54.0,
            "employee_user_id": "<id>",
            "end_at": parse_datetime("2024-05-13T02:12:45.446Z"),
            "hourly_rate": 16.0,
            "hours": 10.0,
            "id": "22d86359-cf1d-452f-9164-d004f875a149",
            "job_name": "Human Accountability Administrator",
            "metadata": [],
            "non_cash_tips_amount": 167.0,
            "start_at": parse_datetime("2021-11-12T21:16:51.835Z"),
            "status": shared.HrisAttendanceStatus.OPEN,
            "timezone": "Africa/Ouagadougou",
            "updated_at": parse_datetime("2022-01-23T03:00:33.311Z"),
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