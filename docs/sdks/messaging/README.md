# Messaging

## Overview

### Available Operations

* [create_messaging_channel](#create_messaging_channel) - Create a channel
* [create_messaging_message](#create_messaging_message) - Create a message
* [get_messaging_channel](#get_messaging_channel) - Retrieve a channel
* [get_messaging_message](#get_messaging_message) - Retrieve a message
* [list_messaging_channels](#list_messaging_channels) - List all channels
* [list_messaging_messages](#list_messaging_messages) - List all messages
* [patch_messaging_channel](#patch_messaging_channel) - Update a channel
* [patch_messaging_event](#patch_messaging_event) - Update an event
* [patch_messaging_message](#patch_messaging_message) - Update a message
* [remove_messaging_channel](#remove_messaging_channel) - Remove a channel
* [remove_messaging_message](#remove_messaging_message) - Remove a message
* [update_messaging_channel](#update_messaging_channel) - Update a channel
* [update_messaging_event](#update_messaging_event) - Update an event
* [update_messaging_message](#update_messaging_message) - Update a message

## create_messaging_channel

Creates a MessagingChannel. Provide the unified MessagingChannel fields in the request body; they are mapped to the provider's API. Returns the created MessagingChannel.

### Example Usage

<!-- UsageSnippet language="python" operationID="createMessagingChannel" method="post" path="/messaging/{connection_id}/channel" example="messaging_channel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.create_messaging_channel(request={
        "messaging_channel": {
            "created_at": parse_datetime("2023-10-05T02:09:22.795Z"),
            "description": "Dolores tutis.",
            "has_subchannels": True,
            "id": "89cbe9a7-7e08-43ab-8d2a-e896744ec53a",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-08T14:50:19.667Z"),
            "web_url": "https://svelte-rule.name/",
        },
        "connection_id": "<id>",
    })

    assert res.messaging_channel is not None

    # Handle response
    print(res.messaging_channel)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateMessagingChannelRequest](../../models/operations/createmessagingchannelrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateMessagingChannelResponse](../../models/operations/createmessagingchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_messaging_message

Creates a MessagingMessage. Provide the unified MessagingMessage fields in the request body; they are mapped to the provider's API. Returns the created MessagingMessage.

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

    res = unified_to.messaging.create_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "b294cba9-90ab-4bd9-973b-ae7cb73a77d1",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "a8455d6d-71c9-44c6-91e5-46e9c7792368",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "5d9d1b2e-7f23-4c9b-91de-28f0e523aae2",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "a8455d6d-71c9-44c6-91e5-46e9c7792368",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-24T11:37:21.374Z"),
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

## get_messaging_channel

Retrieves a single MessagingChannel by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessagingChannel" method="get" path="/messaging/{connection_id}/channel/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.get_messaging_channel(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_channel is not None

    # Handle response
    print(res.messaging_channel)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMessagingChannelRequest](../../models/operations/getmessagingchannelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetMessagingChannelResponse](../../models/operations/getmessagingchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_messaging_message

Retrieves a single MessagingMessage by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

    res = unified_to.messaging.get_messaging_message(request={
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

## list_messaging_channels

Returns a list of MessagingChannels. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessagingChannels" method="get" path="/messaging/{connection_id}/channel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.list_messaging_channels(request={
        "connection_id": "<id>",
    })

    assert res.messaging_channels is not None

    # Handle response
    print(res.messaging_channels)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListMessagingChannelsRequest](../../models/operations/listmessagingchannelsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListMessagingChannelsResponse](../../models/operations/listmessagingchannelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_messaging_messages

Returns a list of MessagingMessages. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

    res = unified_to.messaging.list_messaging_messages(request={
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

## patch_messaging_channel

Updates the MessagingChannel identified by `id`. Provide the unified MessagingChannel fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingChannel" method="patch" path="/messaging/{connection_id}/channel/{id}" example="messaging_channel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.patch_messaging_channel(request={
        "messaging_channel": {
            "created_at": parse_datetime("2023-10-05T02:09:22.795Z"),
            "description": "Dolores tutis.",
            "has_subchannels": True,
            "id": "f8b39046-14b0-4a4c-9b57-decd2708364a",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-08T14:50:19.678Z"),
            "web_url": "https://svelte-rule.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_channel is not None

    # Handle response
    print(res.messaging_channel)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchMessagingChannelRequest](../../models/operations/patchmessagingchannelrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchMessagingChannelResponse](../../models/operations/patchmessagingchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_event

Updates the MessagingEvent identified by `id`. Provide the unified MessagingEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingEvent" method="patch" path="/messaging/{connection_id}/event/{id}" example="messaging_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.patch_messaging_event(request={
        "messaging_event": {
            "channel": {
                "id": "",
                "name": "",
            },
            "created_at": parse_datetime("2019-05-30T19:44:46.461Z"),
            "id": "82d91b98-ab6a-4dbc-a3d8-d9329048498d",
            "is_replacing_original": False,
            "metadata": [],
            "type": shared.MessagingEventType.BUTTON_CLICK,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_event is not None

    # Handle response
    print(res.messaging_event)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchMessagingEventRequest](../../models/operations/patchmessagingeventrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchMessagingEventResponse](../../models/operations/patchmessagingeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_message

Updates the MessagingMessage identified by `id`. Provide the unified MessagingMessage fields to change in the request body.

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

    res = unified_to.messaging.patch_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "72f17c54-bbb2-46db-a9c9-53b51de0349c",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "0b8ef3ab-f0e6-436d-b70b-64ca7a066d76",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "00dffde4-5f1e-47b3-b311-0e1504b8487c",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "0b8ef3ab-f0e6-436d-b70b-64ca7a066d76",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-24T11:37:21.383Z"),
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

## remove_messaging_channel

Deletes the MessagingChannel identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMessagingChannel" method="delete" path="/messaging/{connection_id}/channel/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.remove_messaging_channel(request={
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
| `request`                                                                                            | [operations.RemoveMessagingChannelRequest](../../models/operations/removemessagingchannelrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveMessagingChannelResponse](../../models/operations/removemessagingchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_messaging_message

Deletes the MessagingMessage identified by `id`.

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

    res = unified_to.messaging.remove_messaging_message(request={
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

## update_messaging_channel

Updates the MessagingChannel identified by `id`. Provide the unified MessagingChannel fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingChannel" method="put" path="/messaging/{connection_id}/channel/{id}" example="messaging_channel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.update_messaging_channel(request={
        "messaging_channel": {
            "created_at": parse_datetime("2023-10-05T02:09:22.795Z"),
            "description": "Dolores tutis.",
            "has_subchannels": True,
            "id": "f8b39046-14b0-4a4c-9b57-decd2708364a",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-08T14:50:19.678Z"),
            "web_url": "https://svelte-rule.name/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_channel is not None

    # Handle response
    print(res.messaging_channel)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateMessagingChannelRequest](../../models/operations/updatemessagingchannelrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateMessagingChannelResponse](../../models/operations/updatemessagingchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_event

Updates the MessagingEvent identified by `id`. Provide the unified MessagingEvent fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingEvent" method="put" path="/messaging/{connection_id}/event/{id}" example="messaging_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.update_messaging_event(request={
        "messaging_event": {
            "channel": {
                "id": "",
                "name": "",
            },
            "created_at": parse_datetime("2019-05-30T19:44:46.461Z"),
            "id": "82d91b98-ab6a-4dbc-a3d8-d9329048498d",
            "is_replacing_original": False,
            "metadata": [],
            "type": shared.MessagingEventType.BUTTON_CLICK,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_event is not None

    # Handle response
    print(res.messaging_event)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateMessagingEventRequest](../../models/operations/updatemessagingeventrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateMessagingEventResponse](../../models/operations/updatemessagingeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_message

Updates the MessagingMessage identified by `id`. Provide the unified MessagingMessage fields to change in the request body.

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

    res = unified_to.messaging.update_messaging_message(request={
        "messaging_message": {
            "attachments": [
                {
                    "content_identifier": "72f17c54-bbb2-46db-a9c9-53b51de0349c",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "0b8ef3ab-f0e6-436d-b70b-64ca7a066d76",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "00dffde4-5f1e-47b3-b311-0e1504b8487c",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "0b8ef3ab-f0e6-436d-b70b-64ca7a066d76",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-24T11:37:21.383Z"),
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