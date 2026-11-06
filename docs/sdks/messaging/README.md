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
            "id": "e8d26688-75bb-4b1a-b01b-150ffcdad942",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-04T04:50:05.229Z"),
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
                    "content_identifier": "21d9d644-6875-459b-b37a-6db4c75eb61b",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "9194ff69-193c-4b88-bb2c-c11ff5ea2477",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "e88c5c7d-7248-4d03-bef3-76324615d803",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "9194ff69-193c-4b88-bb2c-c11ff5ea2477",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-22T18:34:02.305Z"),
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
            "id": "8e128b8b-80e4-4fc2-b548-b85bc29f2f99",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-04T04:50:05.236Z"),
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
            "id": "9fc5de70-4738-405c-ab6c-a1a2143fb4f2",
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
                    "content_identifier": "0186d054-5d24-43e9-a2e0-82b1494f5692",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "fff32d6b-598a-4da2-b160-5f9e76f4be43",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "167dbc61-9659-4781-a754-42e65f7b07bf",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "fff32d6b-598a-4da2-b160-5f9e76f4be43",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-22T18:34:02.313Z"),
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
            "id": "8e128b8b-80e4-4fc2-b548-b85bc29f2f99",
            "is_active": False,
            "is_private": True,
            "members": [],
            "metadata": [],
            "name": "tego",
            "updated_at": parse_datetime("2026-06-04T04:50:05.236Z"),
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
            "id": "9fc5de70-4738-405c-ab6c-a1a2143fb4f2",
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
                    "content_identifier": "0186d054-5d24-43e9-a2e0-82b1494f5692",
                    "content_type": "coaegresco",
                    "download_url": "https://rotating-advertisement.org",
                    "filename": "super",
                    "message_id": "fff32d6b-598a-4da2-b160-5f9e76f4be43",
                    "size": 327.0,
                },
            ],
            "buttons": [
                {
                    "id": "167dbc61-9659-4781-a754-42e65f7b07bf",
                    "text": "comparo",
                },
            ],
            "created_at": parse_datetime("2021-11-26T09:26:33.973Z"),
            "destination_members": [],
            "has_children": True,
            "hidden_members": [],
            "id": "fff32d6b-598a-4da2-b160-5f9e76f4be43",
            "is_unread": False,
            "mentioned_members": [],
            "message": "Sum utique aliquid.",
            "message_html": "Articulus tardus tergiversatio.",
            "message_markdown": "Territo uterque tergo curiositas.",
            "metadata": [],
            "reactions": [],
            "subject": "Cernuus optio cohaero summisse in.",
            "updated_at": parse_datetime("2023-07-22T18:34:02.313Z"),
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