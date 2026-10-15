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

Create a recording

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
            "conversation_identifier": "722b8470-81b2-407c-9c99-a1a2d2e1016f",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-02T13:02:49.908Z"),
            "expires_at": parse_datetime("2026-04-21T08:11:28.112Z"),
            "id": "722b8470-81b2-407c-9c99-a1a2d2e1016f",
            "media": [
                {
                    "end_at": parse_datetime("2024-03-30T11:59:53.255Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-09T22:24:33.116Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-19T08:04:25.773Z"),
                            "start_at": parse_datetime("2024-05-30T16:23:39.564Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-09T10:26:34.430Z"),
                            "start_at": parse_datetime("2026-07-28T01:07:44.721Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "start_at": parse_datetime("2023-04-26T20:06:55.154Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-12T17:02:46.390Z"),
            "user_name": "Melyna Larson",
            "user_phone": "1-915-327-0429 x509",
            "web_url": "https://spherical-comparison.org",
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

Retrieve a recording

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

Retrieve a recording

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

List all recordings

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

List all recordings

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

Update a recording

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
            "conversation_identifier": "2e729bf6-1898-4d90-98da-a9f8107393b3",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-02T13:02:49.921Z"),
            "expires_at": parse_datetime("2026-04-21T08:11:28.141Z"),
            "id": "2e729bf6-1898-4d90-98da-a9f8107393b3",
            "media": [
                {
                    "end_at": parse_datetime("2024-03-30T11:59:53.267Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-09T22:24:33.146Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-19T08:04:25.800Z"),
                            "start_at": parse_datetime("2024-05-30T16:23:39.577Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-09T10:26:34.447Z"),
                            "start_at": parse_datetime("2026-07-28T01:07:44.751Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "start_at": parse_datetime("2023-04-26T20:06:55.159Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-12T17:02:46.410Z"),
            "user_name": "Melyna Larson",
            "user_phone": "1-915-327-0429 x509",
            "web_url": "https://spherical-comparison.org",
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

Remove a recording

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

Update a recording

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
            "conversation_identifier": "2e729bf6-1898-4d90-98da-a9f8107393b3",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-02T13:02:49.921Z"),
            "expires_at": parse_datetime("2026-04-21T08:11:28.141Z"),
            "id": "2e729bf6-1898-4d90-98da-a9f8107393b3",
            "media": [
                {
                    "end_at": parse_datetime("2024-03-30T11:59:53.267Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-09T22:24:33.146Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-19T08:04:25.800Z"),
                            "start_at": parse_datetime("2024-05-30T16:23:39.577Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-09T10:26:34.447Z"),
                            "start_at": parse_datetime("2026-07-28T01:07:44.751Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "start_at": parse_datetime("2023-04-26T20:06:55.159Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-12T17:02:46.410Z"),
            "user_name": "Melyna Larson",
            "user_phone": "1-915-327-0429 x509",
            "web_url": "https://spherical-comparison.org",
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