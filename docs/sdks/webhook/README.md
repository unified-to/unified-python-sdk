# Webhook
(*webhook*)

### Available Operations

* [create_unified_webhook](#create_unified_webhook) - Create webhook subscription
* [get_unified_webhook](#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_webhooks](#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_webhook](#patch_unified_webhook) - Update webhook subscription
* [patch_unified_webhook_trigger](#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_webhook](#remove_unified_webhook) - Remove webhook subscription
* [update_unified_webhook](#update_unified_webhook) - Update webhook subscription
* [update_unified_webhook_trigger](#update_unified_webhook_trigger) - Trigger webhook

## create_unified_webhook

The data payload received by your server is described at https://docs.unified.to/unified/overview. The `interval` field can be set as low as 1 minute for paid accounts, and 60 minutes for free accounts.

### Example Usage

```python
import unified_to

s = unified_to.UnifiedTo()


res = s.webhook.create_unified_webhook()

if res.webhook is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateUnifiedWebhookRequest](../../models/operations/createunifiedwebhookrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateUnifiedWebhookResponse](../../models/operations/createunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_unified_webhook

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.get_unified_webhook(request=operations.GetUnifiedWebhookRequest(
    id='<id>',
))

if res.webhook is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_unified_webhooks

Returns all registered webhooks

### Example Usage

```python
import unified_to

s = unified_to.UnifiedTo()


res = s.webhook.list_unified_webhooks()

if res.webhooks is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListUnifiedWebhooksRequest](../../models/operations/listunifiedwebhooksrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ListUnifiedWebhooksResponse](../../models/operations/listunifiedwebhooksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_unified_webhook

Update webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.patch_unified_webhook(request=operations.PatchUnifiedWebhookRequest(
    id='<id>',
))

if res.webhook is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchUnifiedWebhookRequest](../../models/operations/patchunifiedwebhookrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PatchUnifiedWebhookResponse](../../models/operations/patchunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.patch_unified_webhook_trigger(request=operations.PatchUnifiedWebhookTriggerRequest(
    id='<id>',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchUnifiedWebhookTriggerRequest](../../models/operations/patchunifiedwebhooktriggerrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchUnifiedWebhookTriggerResponse](../../models/operations/patchunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## remove_unified_webhook

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.remove_unified_webhook(request=operations.RemoveUnifiedWebhookRequest(
    id='<id>',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveUnifiedWebhookRequest](../../models/operations/removeunifiedwebhookrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RemoveUnifiedWebhookResponse](../../models/operations/removeunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_unified_webhook

Update webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.update_unified_webhook(request=operations.UpdateUnifiedWebhookRequest(
    id='<id>',
))

if res.webhook is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateUnifiedWebhookRequest](../../models/operations/updateunifiedwebhookrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateUnifiedWebhookResponse](../../models/operations/updateunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.webhook.update_unified_webhook_trigger(request=operations.UpdateUnifiedWebhookTriggerRequest(
    id='<id>',
))

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateUnifiedWebhookTriggerRequest](../../models/operations/updateunifiedwebhooktriggerrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.UpdateUnifiedWebhookTriggerResponse](../../models/operations/updateunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
