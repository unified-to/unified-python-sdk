# Channel

## Overview

### Available Operations

* [get_messaging_channel2](#get_messaging_channel2) - Retrieve a channel
* [list_messaging_channels2](#list_messaging_channels2) - List all channels

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

    res = unified_to.channel.get_messaging_channel2(request={
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

    res = unified_to.channel.list_messaging_channels2(request={
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