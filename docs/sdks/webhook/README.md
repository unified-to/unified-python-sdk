# webhook

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteUnifiedWebhookIDRequest(
    id='d73809a0-2f06-4e92-a8b5-6065a5074bef',
)

res = s.webhook.delete_unified_webhook_id(req, operations.DeleteUnifiedWebhookIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteUnifiedWebhookIDRequest](../../models/operations/deleteunifiedwebhookidrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.DeleteUnifiedWebhookIDSecurity](../../models/operations/deleteunifiedwebhookidsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.DeleteUnifiedWebhookIDResponse](../../models/operations/deleteunifiedwebhookidresponse.md)**


## get_unified_webhook

Returns all registered webhooks

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookRequest(
    env='cum',
    limit=5185.71,
    object='laborum',
    offset=9427.54,
    order='eum',
    sort='rem',
    updated_gte=dateutil.parser.isoparse('2022-05-29T07:20:34.094Z'),
)

res = s.webhook.get_unified_webhook(req, operations.GetUnifiedWebhookSecurity(
    jwt="",
))

if res.webhooks is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetUnifiedWebhookRequest](../../models/operations/getunifiedwebhookrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.GetUnifiedWebhookSecurity](../../models/operations/getunifiedwebhooksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.GetUnifiedWebhookResponse](../../models/operations/getunifiedwebhookresponse.md)**


## get_unified_webhook_id

Retrieve webhook by its ID

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetUnifiedWebhookIDRequest(
    id='d2b99404-363a-4096-8c05-3876e39def9c',
)

res = s.webhook.get_unified_webhook_id(req, operations.GetUnifiedWebhookIDSecurity(
    jwt="",
))

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUnifiedWebhookIDRequest](../../models/operations/getunifiedwebhookidrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetUnifiedWebhookIDSecurity](../../models/operations/getunifiedwebhookidsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetUnifiedWebhookIDResponse](../../models/operations/getunifiedwebhookidresponse.md)**


## post_unified_webhook_connection_id_object

To maintain compatibility with the webhooks specification and Zapier webhooks, only the hook_url field is required in the payload when creating a Webhook.  When updated/new objects are found, the array of objects will be POSTed to the hook_url with the paramater hookId=<hookId>.

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostUnifiedWebhookConnectionIDObjectRequest(
    webhook=shared.Webhook(
        checked_at=dateutil.parser.isoparse('2022-08-13T23:23:14.155Z'),
        connection_id='minima',
        created_at=dateutil.parser.isoparse('2020-02-03T17:57:01.294Z'),
        environment='fugiat',
        events=[
            shared.PropertyWebhookEvents.UPDATED,
        ],
        hook_url='ipsum',
        id='54e5cb94-9770-417a-a620-4bb26ca4e999',
        include_raw=False,
        integration_type='quos',
        interval=1768.7,
        object_type=shared.WebhookObjectType.ENRICH_COMPANY,
        subscriptions=[
            'iure',
        ],
        updated_at=dateutil.parser.isoparse('2021-05-13T02:27:36.070Z'),
        workspace_id='debitis',
    ),
    connection_id='reiciendis',
    events=[
        operations.PostUnifiedWebhookConnectionIDObjectEvents.CREATED,
    ],
    object='perferendis',
)

res = s.webhook.post_unified_webhook_connection_id_object(req, operations.PostUnifiedWebhookConnectionIDObjectSecurity(
    jwt="",
))

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostUnifiedWebhookConnectionIDObjectRequest](../../models/operations/postunifiedwebhookconnectionidobjectrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.PostUnifiedWebhookConnectionIDObjectSecurity](../../models/operations/postunifiedwebhookconnectionidobjectsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.PostUnifiedWebhookConnectionIDObjectResponse](../../models/operations/postunifiedwebhookconnectionidobjectresponse.md)**

