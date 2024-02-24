# Webhook
(*webhook*)

### Available Operations

* [create_unified_webhook](#create_unified_webhook) - Create webhook subscription
* [get_unified_webhook](#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_webhooks](#list_unified_webhooks) - Returns all registered webhooks
* [patch_unified_webhook_trigger](#patch_unified_webhook_trigger) - Trigger webhook
* [remove_unified_webhook](#remove_unified_webhook) - Remove webhook subscription
* [update_unified_webhook_trigger](#update_unified_webhook_trigger) - Trigger webhook

## create_unified_webhook

The data payload received by your server is described at https://docs.unified.to/unified/overview.  The `interval` field can be set as low as 15 minutes for paid accounts, and 60 minutes for free accounts.

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateUnifiedWebhookRequest()

res = s.webhook.create_unified_webhook(req, operations.CreateUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateUnifiedWebhookRequest](../../models/operations/createunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.CreateUnifiedWebhookSecurity](../../models/operations/createunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.CreateUnifiedWebhookResponse](../../models/operations/createunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unified_webhook

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookRequest(
    id='<id>',
)

res = s.webhook.get_unified_webhook(req, operations.GetUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedWebhookSecurity](../../models/operations/getunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_webhooks

Returns all registered webhooks

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListUnifiedWebhooksRequest()

res = s.webhook.list_unified_webhooks(req, operations.ListUnifiedWebhooksSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.webhooks is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListUnifiedWebhooksRequest](../../models/operations/listunifiedwebhooksrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ListUnifiedWebhooksSecurity](../../models/operations/listunifiedwebhookssecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ListUnifiedWebhooksResponse](../../models/operations/listunifiedwebhooksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchUnifiedWebhookTriggerRequest(
    id='<id>',
)

res = s.webhook.patch_unified_webhook_trigger(req, operations.PatchUnifiedWebhookTriggerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchUnifiedWebhookTriggerRequest](../../models/operations/patchunifiedwebhooktriggerrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PatchUnifiedWebhookTriggerSecurity](../../models/operations/patchunifiedwebhooktriggersecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PatchUnifiedWebhookTriggerResponse](../../models/operations/patchunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_unified_webhook

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveUnifiedWebhookRequest(
    id='<id>',
)

res = s.webhook.remove_unified_webhook(req, operations.RemoveUnifiedWebhookSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveUnifiedWebhookRequest](../../models/operations/removeunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.RemoveUnifiedWebhookSecurity](../../models/operations/removeunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.RemoveUnifiedWebhookResponse](../../models/operations/removeunifiedwebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_unified_webhook_trigger

Trigger webhook

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateUnifiedWebhookTriggerRequest(
    id='<id>',
)

res = s.webhook.update_unified_webhook_trigger(req, operations.UpdateUnifiedWebhookTriggerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.UpdateUnifiedWebhookTriggerRequest](../../models/operations/updateunifiedwebhooktriggerrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.UpdateUnifiedWebhookTriggerSecurity](../../models/operations/updateunifiedwebhooktriggersecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.UpdateUnifiedWebhookTriggerResponse](../../models/operations/updateunifiedwebhooktriggerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
