# Message

## Overview

### Available Operations

* [create_messaging_message](#create_messaging_message) - Create a message
* [get_messaging_message](#get_messaging_message) - Retrieve a message
* [list_messaging_messages](#list_messaging_messages) - List all messages
* [patch_messaging_message](#patch_messaging_message) - Update a message
* [remove_messaging_message](#remove_messaging_message) - Remove a message
* [update_messaging_message](#update_messaging_message) - Update a message

## create_messaging_message

Create a message

### Example Usage

<!-- UsageSnippet language="python" operationID="createMessagingMessage" method="post" path="/messaging/{connection_id}/message" example="messaging_message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.create_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "d33f0273-d96d-4f8c-b093-bab5f80e19b3",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "7d4eb35d-cb45-443d-b520-d98cd8e04502",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "4c3f6c35-66f6-4936-acfe-0c9861f747fa",
                    "text": "denuo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "7d4eb35d-cb45-443d-b520-d98cd8e04502",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "reactions": [],
            "reference": "571483f2-d95b-4f06-8b78-d35e7046bb74",
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-06T21:46:25.362Z"),
            "web_url": "https://grumpy-kit.net",
        },
        "connection_id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateMessagingMessageRequest](../../models/operations/createmessagingmessagerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateMessagingMessageResponse](../../models/operations/createmessagingmessageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_messaging_message

Retrieve a message

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessagingMessage" method="get" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.get_messaging_message(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMessagingMessageRequest](../../models/operations/getmessagingmessagerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetMessagingMessageResponse](../../models/operations/getmessagingmessageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_messaging_messages

List all messages

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessagingMessages" method="get" path="/messaging/{connection_id}/message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.list_messaging_messages(request={
        "connection_id": "<id>",
    })

    assert res.messaging_messages is not None

    # Handle response
    print(res.messaging_messages)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListMessagingMessagesRequest](../../models/operations/listmessagingmessagesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListMessagingMessagesResponse](../../models/operations/listmessagingmessagesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_message

Update a message

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingMessage" method="patch" path="/messaging/{connection_id}/message/{id}" example="messaging_message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.patch_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "eb815f22-9e31-4760-802a-63ebe3b23c31",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "d630012e-814f-47c0-bab4-43053d1d2485",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "64f74427-7a7f-467f-b575-52c580a1fdfc",
                    "text": "denuo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "d630012e-814f-47c0-bab4-43053d1d2485",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "reactions": [],
            "reference": "571483f2-d95b-4f06-8b78-d35e7046bb74",
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-06T21:46:25.372Z"),
            "web_url": "https://grumpy-kit.net",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchMessagingMessageRequest](../../models/operations/patchmessagingmessagerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchMessagingMessageResponse](../../models/operations/patchmessagingmessageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_messaging_message

Remove a message

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMessagingMessage" method="delete" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.remove_messaging_message(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveMessagingMessageRequest](../../models/operations/removemessagingmessagerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveMessagingMessageResponse](../../models/operations/removemessagingmessageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_message

Update a message

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingMessage" method="put" path="/messaging/{connection_id}/message/{id}" example="messaging_message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.message.update_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "eb815f22-9e31-4760-802a-63ebe3b23c31",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "d630012e-814f-47c0-bab4-43053d1d2485",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "64f74427-7a7f-467f-b575-52c580a1fdfc",
                    "text": "denuo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "d630012e-814f-47c0-bab4-43053d1d2485",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "reactions": [],
            "reference": "571483f2-d95b-4f06-8b78-d35e7046bb74",
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-06T21:46:25.372Z"),
            "web_url": "https://grumpy-kit.net",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateMessagingMessageRequest](../../models/operations/updatemessagingmessagerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateMessagingMessageResponse](../../models/operations/updatemessagingmessageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |