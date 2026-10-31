# Conversation

## Overview

### Available Operations

* [create_property_conversation](#create_property_conversation) - Create a conversation
* [get_property_conversation](#get_property_conversation) - Retrieve a conversation
* [list_property_conversations](#list_property_conversations) - List all conversations

## create_property_conversation

Creates a PropertyConversation. Provide the unified PropertyConversation fields in the request body; they are mapped to the provider's API. Returns the created PropertyConversation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyConversation" method="post" path="/property/{connection_id}/conversation" example="property_conversation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.conversation.create_property_conversation(request={
        "property_conversation": {
            "created_at": parse_datetime("2022-06-20T00:02:46.530Z"),
            "guest_name": "Evie Okuneva",
            "id": "278f6fbd-dbe3-4fae-8ef3-f12c4c287b08",
            "is_unread": False,
            "messages": [
                {
                    "attachments": [],
                    "created_at": parse_datetime("2025-04-22T23:30:42.003Z"),
                    "id": "ea884b5c-bba9-4360-9ceb-a2ebd2cc9e45",
                    "is_automatic": False,
                    "message": "Vinitor caterva amor sophismata admitto colo tempore aufero torrens.",
                    "sender_name": "Evie Okuneva",
                    "sender_type": shared.SenderType.GUEST,
                },
                {
                    "attachments": [],
                    "created_at": parse_datetime("2026-05-06T10:57:43.865Z"),
                    "id": "b89d74c0-0765-4b04-84f4-075103e00b13",
                    "message": "Aequitas torqueo curiositas cimentarius repellendus auditor degero ademptio adnuo.",
                    "sender_name": "Ms. Patti Lynch",
                    "sender_type": shared.SenderType.HOST,
                },
            ],
            "metadata": [],
            "source": "Airbnb",
            "updated_at": parse_datetime("2026-05-06T10:57:43.865Z"),
        },
        "connection_id": "<id>",
    })

    assert res.property_conversation is not None

    # Handle response
    print(res.property_conversation)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreatePropertyConversationRequest](../../models/operations/createpropertyconversationrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreatePropertyConversationResponse](../../models/operations/createpropertyconversationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_property_conversation

Retrieves a single PropertyConversation by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPropertyConversation" method="get" path="/property/{connection_id}/conversation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.conversation.get_property_conversation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.property_conversation is not None

    # Handle response
    print(res.property_conversation)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetPropertyConversationRequest](../../models/operations/getpropertyconversationrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetPropertyConversationResponse](../../models/operations/getpropertyconversationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_property_conversations

Returns a list of PropertyConversations. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPropertyConversations" method="get" path="/property/{connection_id}/conversation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.conversation.list_property_conversations(request={
        "connection_id": "<id>",
    })

    assert res.property_conversations is not None

    # Handle response
    print(res.property_conversations)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListPropertyConversationsRequest](../../models/operations/listpropertyconversationsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListPropertyConversationsResponse](../../models/operations/listpropertyconversationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |