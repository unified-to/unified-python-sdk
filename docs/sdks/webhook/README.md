# Webhook
(*webhook*)

### Available Operations

* [delete_unified_webhook_id](#delete_unified_webhook_id) - Remove webhook subscription
* [get_unified_webhook](#get_unified_webhook) - Returns all registered webhooks
* [get_unified_webhook_id](#get_unified_webhook_id) - Retrieve webhook by its ID
* [post_unified_webhook_connection_id_object](#post_unified_webhook_connection_id_object) - Create webhook subscription

## delete_unified_webhook_id

Remove webhook subscription

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteUnifiedWebhookIDRequest(
    id='<ID>',
)

res = s.webhook.delete_unified_webhook_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteUnifiedWebhookIDRequest](../../models/operations/deleteunifiedwebhookidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteUnifiedWebhookIDResponse](../../models/operations/deleteunifiedwebhookidresponse.md)**


## get_unified_webhook

Returns all registered webhooks

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedWebhookRequest()

res = s.webhook.get_unified_webhook(req)

if res.webhooks is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**


## get_unified_webhook_id

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetUnifiedWebhookIDRequest(
    id='<ID>',
)

res = s.webhook.get_unified_webhook_id(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetUnifiedWebhookIDRequest](../../models/operations/getunifiedwebhookidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetUnifiedWebhookIDResponse](../../models/operations/getunifiedwebhookidresponse.md)**


## post_unified_webhook_connection_id_object

To maintain compatibility with the webhooks specification and Zapier webhooks, only the hook_url field is required in the payload when creating a Webhook.  When updated/new objects are found, the array of objects will be POSTed to the hook_url with the paramater hookId=<hookId>.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PostUnifiedWebhookConnectionIDObjectRequest(
    webhook=shared.Webhook(
        connection_id='drat',
        events=[
            shared.PropertyWebhookEvents.UPDATED,
        ],
        hook_url='siemens National',
        integration_type='GB Rustic deposit',
        interval=6073.96,
        object_type=shared.WebhookObjectType.CRM_CONTACT,
        subscriptions=[
            'Diesel',
        ],
        workspace_id='female ken',
    ),
    connection_id='chocolate',
    events=[
        operations.PostUnifiedWebhookConnectionIDObjectEvents.UPDATED,
    ],
    object='female driver',
)

res = s.webhook.post_unified_webhook_connection_id_object(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PostUnifiedWebhookConnectionIDObjectRequest](../../models/operations/postunifiedwebhookconnectionidobjectrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PostUnifiedWebhookConnectionIDObjectResponse](../../models/operations/postunifiedwebhookconnectionidobjectresponse.md)**

