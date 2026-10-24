# Uc

## Overview

### Available Operations

* [create_uc_call](#create_uc_call) - Create a call
* [create_uc_comment](#create_uc_comment) - Create a comment
* [create_uc_contact](#create_uc_contact) - Create a contact
* [create_uc_recording](#create_uc_recording) - Create a recording
* [get_uc_call](#get_uc_call) - Retrieve a call
* [get_uc_comment](#get_uc_comment) - Retrieve a comment
* [get_uc_contact](#get_uc_contact) - Retrieve a contact
* [get_uc_recording](#get_uc_recording) - Retrieve a recording
* [get_uc_scorecard](#get_uc_scorecard) - Retrieve a scorecard
* [get_uc_scorecardtemplate](#get_uc_scorecardtemplate) - Retrieve a scorecardtemplate
* [list_uc_calls](#list_uc_calls) - List all calls
* [list_uc_comments](#list_uc_comments) - List all comments
* [list_uc_contacts](#list_uc_contacts) - List all contacts
* [list_uc_recordings](#list_uc_recordings) - List all recordings
* [list_uc_scorecards](#list_uc_scorecards) - List all scorecards
* [list_uc_scorecardtemplates](#list_uc_scorecardtemplates) - List all scorecardtemplates
* [patch_uc_call](#patch_uc_call) - Update a call
* [patch_uc_comment](#patch_uc_comment) - Update a comment
* [patch_uc_contact](#patch_uc_contact) - Update a contact
* [patch_uc_recording](#patch_uc_recording) - Update a recording
* [remove_uc_comment](#remove_uc_comment) - Remove a comment
* [remove_uc_contact](#remove_uc_contact) - Remove a contact
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
            "answer_at": parse_datetime("2025-05-15T07:37:02.253Z"),
            "contacts": [],
            "conversation_identifier": "085edbd2-3d92-4092-81ac-f87d135ddc04",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-05-30T23:10:59.811Z"),
            "id": "085edbd2-3d92-4092-81ac-f87d135ddc04",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "fb337f42-7980-422b-8573-5ebd3cdac692",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-17T22:48:25.791Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T14:04:16.016Z"),
            "user_phone": "819-894-3317 x163",
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
            "content": "Vociferor vitiosus.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "b8e1d3d0-6bd7-4c56-a9a1-27a85eaf7d94",
            "metadata": [],
            "updated_at": "2024-02-10T10:59:58.179Z",
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
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "2a82574d-fc19-4325-9ae1-6ffaed04cffe",
            "last_name": "Rogahn",
            "metadata": [],
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-10T01:24:46.718Z"),
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
            "conversation_identifier": "8eb66fad-9526-455a-8707-f819230fb91f",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-06T03:10:51.496Z"),
            "expires_at": parse_datetime("2026-04-29T06:46:46.972Z"),
            "id": "8eb66fad-9526-455a-8707-f819230fb91f",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-02T21:19:48.105Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-17T23:41:58.555Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-26T21:47:50.071Z"),
                            "start_at": parse_datetime("2024-06-03T10:37:02.244Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-13T23:48:42.866Z"),
                            "start_at": parse_datetime("2026-08-05T13:54:58.106Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-04-28T04:13:59.905Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-18T04:50:03.493Z"),
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
            "answer_at": parse_datetime("2025-05-15T07:37:02.284Z"),
            "contacts": [],
            "conversation_identifier": "1e462f3b-0ea0-4223-95b0-3fe50625c540",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-05-30T23:10:59.827Z"),
            "id": "1e462f3b-0ea0-4223-95b0-3fe50625c540",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "b4f7ed1b-2634-4173-9152-2f806e9fecf2",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-17T22:48:25.801Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T14:04:16.020Z"),
            "user_phone": "819-894-3317 x163",
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
            "content": "Vociferor vitiosus.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "3a243e53-5d14-461d-b852-6365e7647755",
            "metadata": [],
            "updated_at": "2024-02-10T10:59:58.181Z",
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
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "b62c16f0-bb64-4d08-9110-8f80c0d9480d",
            "last_name": "Rogahn",
            "metadata": [],
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-10T01:24:46.724Z"),
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
            "conversation_identifier": "c41fc96e-6c21-4fa0-b341-4193927c7def",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-06T03:10:51.511Z"),
            "expires_at": parse_datetime("2026-04-29T06:46:47.004Z"),
            "id": "c41fc96e-6c21-4fa0-b341-4193927c7def",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-02T21:19:48.118Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-17T23:41:58.588Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-26T21:47:50.102Z"),
                            "start_at": parse_datetime("2024-06-03T10:37:02.259Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-13T23:48:42.884Z"),
                            "start_at": parse_datetime("2026-08-05T13:54:58.141Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-04-28T04:13:59.910Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-18T04:50:03.516Z"),
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
            "answer_at": parse_datetime("2025-05-15T07:37:02.284Z"),
            "contacts": [],
            "conversation_identifier": "1e462f3b-0ea0-4223-95b0-3fe50625c540",
            "cost_amount": 1.564,
            "created_at": parse_datetime("2023-04-22T19:05:34.882Z"),
            "currency": "USD",
            "duration_seconds": 2556.0,
            "end_at": parse_datetime("2024-05-30T23:10:59.827Z"),
            "id": "1e462f3b-0ea0-4223-95b0-3fe50625c540",
            "is_private": False,
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.UcMetadataFormat.PRICE,
                    "id": "b4f7ed1b-2634-4173-9152-2f806e9fecf2",
                    "namespace": "custom",
                    "slug": "custom_field",
                    "value": "tui",
                },
            ],
            "start_at": parse_datetime("2023-12-17T22:48:25.801Z"),
            "status": shared.UcCallStatus.IN_PROGRESS,
            "telephone": {
                "telephone": "(493) 534-0768",
                "type": shared.PropertyUcCallTelephoneType.MOBILE,
            },
            "type": shared.UcCallType.INBOUND,
            "updated_at": parse_datetime("2023-08-03T14:04:16.020Z"),
            "user_phone": "819-894-3317 x163",
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
            "content": "Vociferor vitiosus.",
            "created_at": "2023-04-02T23:42:31.571Z",
            "id": "3a243e53-5d14-461d-b852-6365e7647755",
            "metadata": [],
            "updated_at": "2024-02-10T10:59:58.181Z",
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
            "company": "Tillman Group",
            "created_at": parse_datetime("2019-10-28T11:06:56.460Z"),
            "emails": [
                {
                    "email": "Luther_Rogahn32@yahoo.com",
                    "type": shared.UcEmailType.WORK,
                },
            ],
            "first_name": "Luther",
            "id": "b62c16f0-bb64-4d08-9110-8f80c0d9480d",
            "last_name": "Rogahn",
            "metadata": [],
            "name": "Luther Rogahn",
            "telephones": [
                {
                    "telephone": "(809) 992-1681",
                    "type": shared.UcTelephoneType.FAX,
                },
                {
                    "telephone": "(868) 238-2746",
                    "type": shared.UcTelephoneType.HOME,
                },
                {
                    "telephone": "(219) 736-0357",
                    "type": shared.UcTelephoneType.MOBILE,
                },
            ],
            "title": "Chief Optimization Executive",
            "updated_at": parse_datetime("2023-12-10T01:24:46.724Z"),
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
            "conversation_identifier": "c41fc96e-6c21-4fa0-b341-4193927c7def",
            "created_at": parse_datetime("2022-09-17T19:41:46.956Z"),
            "end_at": parse_datetime("2024-05-06T03:10:51.511Z"),
            "expires_at": parse_datetime("2026-04-29T06:46:47.004Z"),
            "id": "c41fc96e-6c21-4fa0-b341-4193927c7def",
            "media": [
                {
                    "end_at": parse_datetime("2024-04-02T21:19:48.118Z"),
                    "language": "en",
                    "recording_download_url": "https://parched-wasabi.com/",
                    "start_at": parse_datetime("2026-05-17T23:41:58.588Z"),
                    "transcript_download_url": "https://colossal-cuckoo.name",
                    "transcripts": [
                        {
                            "end_at": parse_datetime("2026-02-26T21:47:50.102Z"),
                            "start_at": parse_datetime("2024-06-03T10:37:02.259Z"),
                            "text": "Turpis maiores ducimus tero speculum.",
                        },
                        {
                            "end_at": parse_datetime("2024-10-13T23:48:42.884Z"),
                            "start_at": parse_datetime("2026-08-05T13:54:58.141Z"),
                            "text": "Magnam consuasor uxor tergiversatio subseco.",
                        },
                    ],
                },
            ],
            "metadata": [],
            "start_at": parse_datetime("2023-04-28T04:13:59.910Z"),
            "type": shared.UcRecordingType.OUTBOUND,
            "updated_at": parse_datetime("2025-03-18T04:50:03.516Z"),
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