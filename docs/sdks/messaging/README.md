# Messaging

## Overview

### Available Operations

* [create_messaging_message2](#create_messaging_message2) - Create a message
* [get_messaging_channel2](#get_messaging_channel2) - Retrieve a channel
* [get_messaging_message2](#get_messaging_message2) - Retrieve a message
* [list_messaging_channels2](#list_messaging_channels2) - List all channels
* [list_messaging_messages2](#list_messaging_messages2) - List all messages
* [patch_messaging_event2](#patch_messaging_event2) - Update an event
* [patch_messaging_message2](#patch_messaging_message2) - Update a message
* [remove_messaging_message2](#remove_messaging_message2) - Remove a message
* [update_messaging_event2](#update_messaging_event2) - Update an event
* [update_messaging_message2](#update_messaging_message2) - Update a message

## create_messaging_message2

Create a message

### Example Usage

<!-- UsageSnippet language="python" operationID="createMessagingMessage2" method="post" path="/messaging/{connection_id}/message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.create_messaging_message2(request={
        "messaging_message": {},
        "connection_id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateMessagingMessage2Request](../../models/operations/createmessagingmessage2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateMessagingMessage2Response](../../models/operations/createmessagingmessage2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_messaging_channel2

Retrieve a channel

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessagingChannel2" method="get" path="/messaging/{connection_id}/channel/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.get_messaging_channel2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_channel is not None

    # Handle response
    print(res.messaging_channel)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetMessagingChannel2Request](../../models/operations/getmessagingchannel2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetMessagingChannel2Response](../../models/operations/getmessagingchannel2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_messaging_message2

Retrieve a message

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessagingMessage2" method="get" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.get_messaging_message2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetMessagingMessage2Request](../../models/operations/getmessagingmessage2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetMessagingMessage2Response](../../models/operations/getmessagingmessage2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_messaging_channels2

List all channels

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessagingChannels2" method="get" path="/messaging/{connection_id}/channel" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.list_messaging_channels2(request={
        "connection_id": "<id>",
    })

    assert res.messaging_channels is not None

    # Handle response
    print(res.messaging_channels)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListMessagingChannels2Request](../../models/operations/listmessagingchannels2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListMessagingChannels2Response](../../models/operations/listmessagingchannels2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_messaging_messages2

List all messages

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessagingMessages2" method="get" path="/messaging/{connection_id}/message" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.list_messaging_messages2(request={
        "connection_id": "<id>",
    })

    assert res.messaging_messages is not None

    # Handle response
    print(res.messaging_messages)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListMessagingMessages2Request](../../models/operations/listmessagingmessages2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListMessagingMessages2Response](../../models/operations/listmessagingmessages2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_event2

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingEvent2" method="patch" path="/messaging/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.patch_messaging_event2(request={
        "messaging_event": {},
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
| `request`                                                                                        | [operations.PatchMessagingEvent2Request](../../models/operations/patchmessagingevent2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchMessagingEvent2Response](../../models/operations/patchmessagingevent2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_messaging_message2

Update a message

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMessagingMessage2" method="patch" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.patch_messaging_message2(request={
        "messaging_message": {},
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
| `request`                                                                                            | [operations.PatchMessagingMessage2Request](../../models/operations/patchmessagingmessage2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchMessagingMessage2Response](../../models/operations/patchmessagingmessage2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_messaging_message2

Remove a message

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMessagingMessage2" method="delete" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.remove_messaging_message2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveMessagingMessage2Request](../../models/operations/removemessagingmessage2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveMessagingMessage2Response](../../models/operations/removemessagingmessage2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_event2

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingEvent2" method="put" path="/messaging/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.update_messaging_event2(request={
        "messaging_event": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_event is not None

    # Handle response
    print(res.messaging_event)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateMessagingEvent2Request](../../models/operations/updatemessagingevent2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateMessagingEvent2Response](../../models/operations/updatemessagingevent2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_messaging_message2

Update a message

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMessagingMessage2" method="put" path="/messaging/{connection_id}/message/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.messaging.update_messaging_message2(request={
        "messaging_message": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.messaging_message is not None

    # Handle response
    print(res.messaging_message)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateMessagingMessage2Request](../../models/operations/updatemessagingmessage2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateMessagingMessage2Response](../../models/operations/updatemessagingmessage2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |