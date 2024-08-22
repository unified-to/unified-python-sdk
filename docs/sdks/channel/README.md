# Channel
(*channel*)

## Overview

### Available Operations

* [get_messaging_channel](#get_messaging_channel) - Retrieve a channel
* [list_messaging_channels](#list_messaging_channels) - List all channels

## get_messaging_channel

Retrieve a channel

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.channel.get_messaging_channel(request=operations.GetMessagingChannelRequest(
    connection_id='<value>',
    id='<id>',
))

if res.messaging_channel is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMessagingChannelRequest](../../models/operations/getmessagingchannelrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |

### Response

**[operations.GetMessagingChannelResponse](../../models/operations/getmessagingchannelresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## list_messaging_channels

List all channels

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.channel.list_messaging_channels(request=operations.ListMessagingChannelsRequest(
    connection_id='<value>',
))

if res.messaging_channels is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListMessagingChannelsRequest](../../models/operations/listmessagingchannelsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[operations.ListMessagingChannelsResponse](../../models/operations/listmessagingchannelsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
