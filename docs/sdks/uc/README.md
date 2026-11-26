# Uc

## Overview

### Available Operations

* [create_uc_call](#create_uc_call) - Create a call
* [create_uc_comment](#create_uc_comment) - Create a comment
* [create_uc_contact](#create_uc_contact) - Create a contact
* [create_uc_fax](#create_uc_fax) - Create a fax
* [create_uc_recording](#create_uc_recording) - Create a recording
* [get_uc_call](#get_uc_call) - Retrieve a call
* [get_uc_comment](#get_uc_comment) - Retrieve a comment
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [get_uc_fax](#get_uc_fax) - Retrieve a fax
* [get_uc_recording](#get_uc_recording) - Retrieve a recording
* [get_uc_scorecard](#get_uc_scorecard) - Retrieve a scorecard
* [get_uc_scorecardtemplate](#get_uc_scorecardtemplate) - Retrieve a scorecardtemplate
* [list_uc_calls](#list_uc_calls) - List all calls
* [list_uc_comments](#list_uc_comments) - List all comments
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [list_uc_faxes](#list_uc_faxes) - List all faxes
* [list_uc_recordings](#list_uc_recordings) - List all recordings
* [list_uc_scorecards](#list_uc_scorecards) - List all scorecards
* [list_uc_scorecardtemplates](#list_uc_scorecardtemplates) - List all scorecardtemplates
* [patch_uc_call](#patch_uc_call) - Update a call
* [patch_uc_comment](#patch_uc_comment) - Update a comment
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [patch_uc_recording](#patch_uc_recording) - Update a recording
* [remove_uc_comment](#remove_uc_comment) - Remove a comment
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
* [remove_uc_fax](#remove_uc_fax) - Remove a fax
* [remove_uc_recording](#remove_uc_recording) - Remove a recording
* [update_uc_call](#update_uc_call) - Update a call
* [update_uc_comment](#update_uc_comment) - Update a comment
* [update_uc_contact](#update_uc_contact) - Update a contact
* [update_uc_recording](#update_uc_recording) - Update a recording

## create_uc_call

Creates a UcCall. Provide the unified UcCall fields in the request body; they are mapped to the provider's API. Returns the created UcCall.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcCall" method="post" path="/uc/{connection_id}/call" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.create_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-06-03T19:12:45.478Z"),
            "contacts": [],
            "conversation_identifier": "529b1de6-deb4-4af8-ae25-5eba44819594",
            "cost_amount": 2.7016,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2132.0,
            "end_at": parse_datetime("2024-06-10T09:59:23.364Z"),
            "id": "529b1de6-deb4-4af8-ae25-5eba44819594",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "a99c963e-47be-4d02-aa75-2721e15498c9",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "voluptatem",
                },
            ],
            "start_at": parse_datetime("2023-12-24T03:12:49.716Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(507) 787-3877",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-06T05:51:27.207Z"),
            "user_phone": "1-894-431-7163 x39343",
        },
        "connection_id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateUcCallRequest](../../models/operations/createuccallrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateUcCallResponse](../../models/operations/createuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_uc_comment

Creates a UcComment. Provide the unified UcComment fields in the request body; they are mapped to the provider's API. Returns the created UcComment.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcComment" method="post" path="/uc/{connection_id}/comment" example="uc_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.create_uc_comment(request={
        "uc_comment": {
            "content": "Aestivus odit ducimus nulla talis.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "7f9f5143-956f-491f-ba70-070e1108257d",
            "metadata": [],
            "updated_at": "2024-02-18T10:33:29.703Z",
        },
        "connection_id": "<id>",
    })

    assert res.uc_comment is not None

    # Handle response
    print(res.uc_comment)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateUcCommentRequest](../../models/operations/createuccommentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateUcCommentResponse](../../models/operations/createuccommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_uc_contact

Creates a UcContact. Provide the unified UcContact fields in the request body; they are mapped to the provider's API. Returns the created UcContact.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcContact" method="post" path="/uc/{connection_id}/contact" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.create_uc_contact(request={
        "uc_contact": {
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "2c39d126-e669-4218-8db5-e84c7d941baf",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.045Z"),
        },
        "connection_id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateUcContactRequest](../../models/operations/createuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateUcContactResponse](../../models/operations/createuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_uc_fax

Creates a UcFax. Provide the unified UcFax fields in the request body; they are mapped to the provider's API. Returns the created UcFax.

### Example Usage

<!-- UsageSnippet language="python" operationID="createUcFax" method="post" path="/uc/{connection_id}/fax" example="uc_fax" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.create_uc_fax(request={
        "uc_fax": {
            "cost_amount": 1.8536,
            "created_at": parse_datetime("2022-10-25T13:37:51.431Z"),
            "currency": "USD",
            "from_telephone": "+15108540908",
            "id": "2e13c7ac-bfdc-412a-8b29-02f1bebb12ef",
            "media_url": "https://pitiful-stranger.net/",
            "metadata": [],
            "pages": 10.0,
            "status": shared.UcFaxStatus.DELIVERED,
            "to_telephone": "+13999866972",
            "type": shared.UcFaxType.INBOUND,
            "updated_at": parse_datetime("2023-04-17T23:52:59.787Z"),
        },
        "connection_id": "<id>",
    })

    assert res.uc_fax is not None

    # Handle response
    print(res.uc_fax)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateUcFaxRequest](../../models/operations/createucfaxrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CreateUcFaxResponse](../../models/operations/createucfaxresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.uc.create_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "d497a35f-0858-4f74-988c-9957470cf547",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-19T07:35:14.513Z"),
            "expires_at": parse_datetime("2026-05-28T10:53:36.596Z"),
            "id": "d497a35f-0858-4f74-988c-9957470cf547",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-15T08:05:49.499Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-16T13:44:18.088Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-26T17:20:43.789Z"),
                            "start_at": parse_datetime("2024-06-17T06:02:42.166Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-30T17:34:16.725Z"),
                            "start_at": parse_datetime("2026-09-05T22:11:13.370Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T02:12:59.339Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-07T08:56:54.998Z"),
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

## get_uc_call

Retrieves a single UcCall by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcCall" method="get" path="/uc/{connection_id}/call/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_call(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetUcCallRequest](../../models/operations/getuccallrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetUcCallResponse](../../models/operations/getuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_comment

Retrieves a single UcComment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcComment" method="get" path="/uc/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_comment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_comment is not None

    # Handle response
    print(res.uc_comment)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetUcCommentRequest](../../models/operations/getuccommentrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetUcCommentResponse](../../models/operations/getuccommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_contact

Retrieves a single UcContact by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcContact" method="get" path="/uc/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_contact(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetUcContactRequest](../../models/operations/getuccontactrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetUcContactResponse](../../models/operations/getuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_fax

Retrieves a single UcFax by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcFax" method="get" path="/uc/{connection_id}/fax/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_fax(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_fax is not None

    # Handle response
    print(res.uc_fax)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUcFaxRequest](../../models/operations/getucfaxrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.GetUcFaxResponse](../../models/operations/getucfaxresponse.md)**

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

    res = unified_to.uc.get_uc_recording(request={
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

## get_uc_scorecard

Retrieves a single UcScorecard by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcScorecard" method="get" path="/uc/{connection_id}/scorecard/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_scorecard(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_scorecard is not None

    # Handle response
    print(res.uc_scorecard)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetUcScorecardRequest](../../models/operations/getucscorecardrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetUcScorecardResponse](../../models/operations/getucscorecardresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uc_scorecardtemplate

Retrieves a single UcScorecardtemplate by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUcScorecardtemplate" method="get" path="/uc/{connection_id}/scorecardtemplate/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.get_uc_scorecardtemplate(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_scorecardtemplate is not None

    # Handle response
    print(res.uc_scorecardtemplate)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUcScorecardtemplateRequest](../../models/operations/getucscorecardtemplaterequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetUcScorecardtemplateResponse](../../models/operations/getucscorecardtemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_calls

Returns a list of UcCalls. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcCalls" method="get" path="/uc/{connection_id}/call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_calls(request={
        "connection_id": "<id>",
    })

    assert res.uc_calls is not None

    # Handle response
    print(res.uc_calls)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcCallsRequest](../../models/operations/listuccallsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListUcCallsResponse](../../models/operations/listuccallsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_comments

Returns a list of UcComments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcComments" method="get" path="/uc/{connection_id}/comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_comments(request={
        "connection_id": "<id>",
    })

    assert res.uc_comments is not None

    # Handle response
    print(res.uc_comments)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListUcCommentsRequest](../../models/operations/listuccommentsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListUcCommentsResponse](../../models/operations/listuccommentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_contacts

Returns a list of UcContacts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcContacts" method="get" path="/uc/{connection_id}/contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_contacts(request={
        "connection_id": "<id>",
    })

    assert res.uc_contacts is not None

    # Handle response
    print(res.uc_contacts)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListUcContactsRequest](../../models/operations/listuccontactsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListUcContactsResponse](../../models/operations/listuccontactsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_faxes

Returns a list of UcFaxes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcFaxes" method="get" path="/uc/{connection_id}/fax" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_faxes(request={
        "connection_id": "<id>",
    })

    assert res.uc_faxes is not None

    # Handle response
    print(res.uc_faxes)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListUcFaxesRequest](../../models/operations/listucfaxesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ListUcFaxesResponse](../../models/operations/listucfaxesresponse.md)**

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

    res = unified_to.uc.list_uc_recordings(request={
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

## list_uc_scorecards

Returns a list of UcScorecards. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcScorecards" method="get" path="/uc/{connection_id}/scorecard" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_scorecards(request={
        "connection_id": "<id>",
    })

    assert res.uc_scorecards is not None

    # Handle response
    print(res.uc_scorecards)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListUcScorecardsRequest](../../models/operations/listucscorecardsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListUcScorecardsResponse](../../models/operations/listucscorecardsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_uc_scorecardtemplates

Returns a list of UcScorecardtemplates. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUcScorecardtemplates" method="get" path="/uc/{connection_id}/scorecardtemplate" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.list_uc_scorecardtemplates(request={
        "connection_id": "<id>",
    })

    assert res.uc_scorecardtemplates is not None

    # Handle response
    print(res.uc_scorecardtemplates)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListUcScorecardtemplatesRequest](../../models/operations/listucscorecardtemplatesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListUcScorecardtemplatesResponse](../../models/operations/listucscorecardtemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_call

Updates the UcCall identified by `id`. Provide the unified UcCall fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcCall" method="patch" path="/uc/{connection_id}/call/{id}" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.patch_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-06-03T19:12:45.495Z"),
            "contacts": [],
            "conversation_identifier": "a13f63d6-851f-4643-9210-3d64723bb645",
            "cost_amount": 2.7016,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2132.0,
            "end_at": parse_datetime("2024-06-10T09:59:23.373Z"),
            "id": "a13f63d6-851f-4643-9210-3d64723bb645",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "2225cec5-23f5-44a5-bc6f-235c59cac729",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "voluptatem",
                },
            ],
            "start_at": parse_datetime("2023-12-24T03:12:49.722Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(507) 787-3877",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-06T05:51:27.210Z"),
            "user_phone": "1-894-431-7163 x39343",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchUcCallRequest](../../models/operations/patchuccallrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.PatchUcCallResponse](../../models/operations/patchuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_comment

Updates the UcComment identified by `id`. Provide the unified UcComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcComment" method="patch" path="/uc/{connection_id}/comment/{id}" example="uc_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.patch_uc_comment(request={
        "uc_comment": {
            "content": "Aestivus odit ducimus nulla talis.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "b44a8148-7740-4287-92d1-2c64e6d34670",
            "metadata": [],
            "updated_at": "2024-02-18T10:33:29.705Z",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_comment is not None

    # Handle response
    print(res.uc_comment)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchUcCommentRequest](../../models/operations/patchuccommentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchUcCommentResponse](../../models/operations/patchuccommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_uc_contact

Updates the UcContact identified by `id`. Provide the unified UcContact fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchUcContact" method="patch" path="/uc/{connection_id}/contact/{id}" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.patch_uc_contact(request={
        "uc_contact": {
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "ee028c4e-42f3-448f-b77e-fc5a6aa90ee3",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.053Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchUcContactRequest](../../models/operations/patchuccontactrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchUcContactResponse](../../models/operations/patchuccontactresponse.md)**

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

    res = unified_to.uc.patch_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "c925f649-3bc0-4210-abb7-11474287b123",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-19T07:35:14.523Z"),
            "expires_at": parse_datetime("2026-05-28T10:53:36.618Z"),
            "id": "c925f649-3bc0-4210-abb7-11474287b123",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-15T08:05:49.508Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-16T13:44:18.110Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-26T17:20:43.810Z"),
                            "start_at": parse_datetime("2024-06-17T06:02:42.176Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-30T17:34:16.738Z"),
                            "start_at": parse_datetime("2026-09-05T22:11:13.393Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T02:12:59.342Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-07T08:56:55.014Z"),
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

## remove_uc_comment

Deletes the UcComment identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcComment" method="delete" path="/uc/{connection_id}/comment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.remove_uc_comment(request={
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
| `request`                                                                              | [operations.RemoveUcCommentRequest](../../models/operations/removeuccommentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveUcCommentResponse](../../models/operations/removeuccommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_uc_contact

Deletes the UcContact identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcContact" method="delete" path="/uc/{connection_id}/contact/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.remove_uc_contact(request={
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
| `request`                                                                              | [operations.RemoveUcContactRequest](../../models/operations/removeuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveUcContactResponse](../../models/operations/removeuccontactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_uc_fax

Deletes the UcFax identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeUcFax" method="delete" path="/uc/{connection_id}/fax/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.remove_uc_fax(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RemoveUcFaxRequest](../../models/operations/removeucfaxrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.RemoveUcFaxResponse](../../models/operations/removeucfaxresponse.md)**

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

    res = unified_to.uc.remove_uc_recording(request={
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

## update_uc_call

Updates the UcCall identified by `id`. Provide the unified UcCall fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcCall" method="put" path="/uc/{connection_id}/call/{id}" example="uc_call" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.update_uc_call(request={
        "uc_call": {
            "answer_at": parse_datetime("2025-06-03T19:12:45.495Z"),
            "contacts": [],
            "conversation_identifier": "a13f63d6-851f-4643-9210-3d64723bb645",
            "cost_amount": 2.7016,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2132.0,
            "end_at": parse_datetime("2024-06-10T09:59:23.373Z"),
            "id": "a13f63d6-851f-4643-9210-3d64723bb645",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "2225cec5-23f5-44a5-bc6f-235c59cac729",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "voluptatem",
                },
            ],
            "start_at": parse_datetime("2023-12-24T03:12:49.722Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(507) 787-3877",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-06T05:51:27.210Z"),
            "user_phone": "1-894-431-7163 x39343",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_call is not None

    # Handle response
    print(res.uc_call)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateUcCallRequest](../../models/operations/updateuccallrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.UpdateUcCallResponse](../../models/operations/updateuccallresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_uc_comment

Updates the UcComment identified by `id`. Provide the unified UcComment fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcComment" method="put" path="/uc/{connection_id}/comment/{id}" example="uc_comment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.update_uc_comment(request={
        "uc_comment": {
            "content": "Aestivus odit ducimus nulla talis.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "b44a8148-7740-4287-92d1-2c64e6d34670",
            "metadata": [],
            "updated_at": "2024-02-18T10:33:29.705Z",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_comment is not None

    # Handle response
    print(res.uc_comment)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateUcCommentRequest](../../models/operations/updateuccommentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateUcCommentResponse](../../models/operations/updateuccommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_uc_contact

Updates the UcContact identified by `id`. Provide the unified UcContact fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateUcContact" method="put" path="/uc/{connection_id}/contact/{id}" example="uc_contact" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.uc.update_uc_contact(request={
        "uc_contact": {
            "company": "Olson - Stanton",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Norval_Brekke@gmail.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Norval",
            "id": "ee028c4e-42f3-448f-b77e-fc5a6aa90ee3",
            "last_name": "Brekke",
            "metadata": [],
            "name": "Norval Brekke",
            "telephones": [
                {
                    "telephone": "(992) 368-1868",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(238) 374-6019",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(736) 235-7480",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Internal Creative Director",
            "updated_at": parse_datetime("2023-12-29T13:20:51.053Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.uc_contact is not None

    # Handle response
    print(res.uc_contact)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateUcContactRequest](../../models/operations/updateuccontactrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateUcContactResponse](../../models/operations/updateuccontactresponse.md)**

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

    res = unified_to.uc.update_uc_recording(request={
        "uc_recording": {
            "contacts": [],
            "conversation_identifier": "c925f649-3bc0-4210-abb7-11474287b123",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-19T07:35:14.523Z"),
            "expires_at": parse_datetime("2026-05-28T10:53:36.618Z"),
            "id": "c925f649-3bc0-4210-abb7-11474287b123",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-15T08:05:49.508Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-06-16T13:44:18.110Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-03-26T17:20:43.810Z"),
                            "start_at": parse_datetime("2024-06-17T06:02:42.176Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-30T17:34:16.738Z"),
                            "start_at": parse_datetime("2026-09-05T22:11:13.393Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-05-03T02:12:59.342Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-04-07T08:56:55.014Z"),
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