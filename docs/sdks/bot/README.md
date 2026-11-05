# Bot

## Overview

### Available Operations

* [create_calendar_bot](#create_calendar_bot) - Create a bot
* [get_calendar_bot](#get_calendar_bot) - Retrieve a bot
* [list_calendar_bots](#list_calendar_bots) - List all bots
* [patch_calendar_bot](#patch_calendar_bot) - Update a bot
* [remove_calendar_bot](#remove_calendar_bot) - Remove a bot
* [update_calendar_bot](#update_calendar_bot) - Update a bot

## create_calendar_bot

Creates a CalendarBot. Provide the unified CalendarBot fields in the request body; they are mapped to the provider's API. Returns the created CalendarBot.

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarBot" method="post" path="/calendar/{connection_id}/bot" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.create_calendar_bot(request={
        "calendar_bot": {},
        "connection_id": "<id>",
    })

    assert res.calendar_bot is not None

    # Handle response
    print(res.calendar_bot)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCalendarBotRequest](../../models/operations/createcalendarbotrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateCalendarBotResponse](../../models/operations/createcalendarbotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_bot

Retrieves a single CalendarBot by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarBot" method="get" path="/calendar/{connection_id}/bot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.get_calendar_bot(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_bot is not None

    # Handle response
    print(res.calendar_bot)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCalendarBotRequest](../../models/operations/getcalendarbotrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetCalendarBotResponse](../../models/operations/getcalendarbotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_bots

Returns a list of CalendarBots. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarBots" method="get" path="/calendar/{connection_id}/bot" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.list_calendar_bots(request={
        "connection_id": "<id>",
    })

    assert res.calendar_bots is not None

    # Handle response
    print(res.calendar_bots)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCalendarBotsRequest](../../models/operations/listcalendarbotsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCalendarBotsResponse](../../models/operations/listcalendarbotsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_bot

Updates the CalendarBot identified by `id`. Provide the unified CalendarBot fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarBot" method="patch" path="/calendar/{connection_id}/bot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.patch_calendar_bot(request={
        "calendar_bot": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_bot is not None

    # Handle response
    print(res.calendar_bot)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCalendarBotRequest](../../models/operations/patchcalendarbotrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchCalendarBotResponse](../../models/operations/patchcalendarbotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_bot

Deletes the CalendarBot identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarBot" method="delete" path="/calendar/{connection_id}/bot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.remove_calendar_bot(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCalendarBotRequest](../../models/operations/removecalendarbotrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveCalendarBotResponse](../../models/operations/removecalendarbotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_bot

Updates the CalendarBot identified by `id`. Provide the unified CalendarBot fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarBot" method="put" path="/calendar/{connection_id}/bot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bot.update_calendar_bot(request={
        "calendar_bot": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_bot is not None

    # Handle response
    print(res.calendar_bot)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCalendarBotRequest](../../models/operations/updatecalendarbotrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateCalendarBotResponse](../../models/operations/updatecalendarbotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |