# Recording

## Overview

### Available Operations

* [create_uc_recording](#create_uc_recording) - Create a recording
* [get_calendar_recording](#get_calendar_recording) - Retrieve a recording
* [get_uc_recording](#get_uc_recording) - Retrieve a recording
* [list_calendar_recordings](#list_calendar_recordings) - List all recordings
* [list_uc_recordings](#list_uc_recordings) - List all recordings
* [patch_uc_recording](#patch_uc_recording) - Update a recording
* [remove_uc_recording](#remove_uc_recording) - Remove a recording
* [update_uc_recording](#update_uc_recording) - Update a recording

## create_uc_recording

Creates a UcRecording. Provide the unified UcRecording fields in the request body; they are mapped to the provider's API. Returns the created UcRecording.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcRecording" method="post" path="/uc/{connection_id}/recording" example="uc_recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.create_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "a5563146-f281-4fa5-b1fb-564ebcdc4c90",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-20T03:20:52.501Z"),
            "expires_at": parse_datetime("2026-05-30T06:37:03.927Z"),
            "id": "a5563146-f281-4fa5-b1fb-564ebcdc4c90",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-16T02:45:21.615Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-18T10:04:56.862Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-28T11:02:09.378Z"),
                            "start_at": parse_datetime("2024-06-18T02:44:37.423Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-31T18:39:44.722Z"),
                            "start_at": parse_datetime("2026-09-07T21:10:07.243Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T09:35:05.622Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-08T15:10:58.935Z"),
            "user_phone": "(327) 242-9509",
            "web_url": "https://ignorant-tuba.biz",
        },
        "connection_id": "<id>",
    })

    assert res.uc_recording is not None

    # Handle response
    print(res.uc_recording)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateUcRecordingRequest](../../models/operations/createucrecordingrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateUcRecordingResponse](../../models/operations/createucrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_recording

Retrieves a single CalendarRecording by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarRecording" method="get" path="/calendar/{connection_id}/recording/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.get_calendar_recording(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_recording is not None

    # Handle response
    print(res.calendar_recording)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCalendarRecordingRequest](../../models/operations/getcalendarrecordingrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetCalendarRecordingResponse](../../models/operations/getcalendarrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_recording

Retrieves a single UcRecording by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcRecording" method="get" path="/uc/{connection_id}/recording/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.get_uc_recording(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_recording is not None

    # Handle response
    print(res.uc_recording)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetUcRecordingRequest](../../models/operations/getucrecordingrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetUcRecordingResponse](../../models/operations/getucrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_recordings

Returns a list of CalendarRecordings. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarRecordings" method="get" path="/calendar/{connection_id}/recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.list_calendar_recordings(request={
        "connection_id": "<id>",
    })

    assert res.calendar_recordings is not None

    # Handle response
    print(res.calendar_recordings)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListCalendarRecordingsRequest](../../models/operations/listcalendarrecordingsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListCalendarRecordingsResponse](../../models/operations/listcalendarrecordingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_recordings

Returns a list of UcRecordings. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcRecordings" method="get" path="/uc/{connection_id}/recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.list_uc_recordings(request={
        "connection_id": "<id>",
    })

    assert res.uc_recordings is not None

    # Handle response
    print(res.uc_recordings)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListUcRecordingsRequest](../../models/operations/listucrecordingsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListUcRecordingsResponse](../../models/operations/listucrecordingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_recording

Updates the UcRecording identified by `id`. Provide the unified UcRecording fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcRecording" method="patch" path="/uc/{connection_id}/recording/{id}" example="uc_recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.patch_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "e98757ed-a496-4ee4-99f7-d3eddc3444e8",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-20T03:20:52.517Z"),
            "expires_at": parse_datetime("2026-05-30T06:37:03.962Z"),
            "id": "e98757ed-a496-4ee4-99f7-d3eddc3444e8",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-16T02:45:21.630Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-18T10:04:56.897Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-28T11:02:09.411Z"),
                            "start_at": parse_datetime("2024-06-18T02:44:37.440Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-31T18:39:44.743Z"),
                            "start_at": parse_datetime("2026-09-07T21:10:07.280Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T09:35:05.628Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-08T15:10:58.960Z"),
            "user_phone": "(327) 242-9509",
            "web_url": "https://ignorant-tuba.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_recording is not None

    # Handle response
    print(res.uc_recording)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchUcRecordingRequest](../../models/operations/patchucrecordingrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchUcRecordingResponse](../../models/operations/patchucrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_uc_recording

Deletes the UcRecording identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcRecording" method="delete" path="/uc/{connection_id}/recording/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.remove_uc_recording(request={
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
| `request`                                                                                  | [operations.RemoveUcRecordingRequest](../../models/operations/removeucrecordingrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveUcRecordingResponse](../../models/operations/removeucrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_uc_recording

Updates the UcRecording identified by `id`. Provide the unified UcRecording fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcRecording" method="put" path="/uc/{connection_id}/recording/{id}" example="uc_recording" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.recording.update_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "e98757ed-a496-4ee4-99f7-d3eddc3444e8",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-20T03:20:52.517Z"),
            "expires_at": parse_datetime("2026-05-30T06:37:03.962Z"),
            "id": "e98757ed-a496-4ee4-99f7-d3eddc3444e8",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-16T02:45:21.630Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-18T10:04:56.897Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-28T11:02:09.411Z"),
                            "start_at": parse_datetime("2024-06-18T02:44:37.440Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-31T18:39:44.743Z"),
                            "start_at": parse_datetime("2026-09-07T21:10:07.280Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T09:35:05.628Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-08T15:10:58.960Z"),
            "user_phone": "(327) 242-9509",
            "web_url": "https://ignorant-tuba.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_recording is not None

    # Handle response
    print(res.uc_recording)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateUcRecordingRequest](../../models/operations/updateucrecordingrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateUcRecordingResponse](../../models/operations/updateucrecordingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |