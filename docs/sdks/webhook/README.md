# Webhook
(*webhook*)

### Available Operations

* [get_unified_webhook](#get_unified_webhook) - Retrieve webhook by its ID
* [list_unified_webhooks](#list_unified_webhooks) - Returns all registered webhooks
* [remove_unified_webhook](#remove_unified_webhook) - Remove webhook subscription

## get_unified_webhook

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetUnifiedWebhookRequest(
    id='<ID>',
)

res = s.webhook.get_unified_webhook(req)

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
| errors.SDKError | 4x-5xx          | */*             |

## list_unified_webhooks

Returns all registered webhooks

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListUnifiedWebhooksRequest()

res = s.webhook.list_unified_webhooks(req)

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
| errors.SDKError | 4x-5xx          | */*             |

## remove_unified_webhook

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveUnifiedWebhookRequest(
    id='<ID>',
)

res = s.webhook.remove_unified_webhook(req)

if res.status_code == 200:
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
| errors.SDKError | 4x-5xx          | */*             |
