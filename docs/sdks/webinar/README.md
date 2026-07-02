# Webinar

## Overview

### Available Operations

* [create_calendar_webinar](#create_calendar_webinar) - Create a webinar
* [get_calendar_webinar](#get_calendar_webinar) - Retrieve a webinar
* [list_calendar_webinars](#list_calendar_webinars) - List all webinars
* [patch_calendar_webinar](#patch_calendar_webinar) - Update a webinar
* [remove_calendar_webinar](#remove_calendar_webinar) - Remove a webinar
* [update_calendar_webinar](#update_calendar_webinar) - Update a webinar

## create_calendar_webinar

Create a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarWebinar" method="post" path="/calendar/{connection_id}/webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.create_calendar_webinar(request={
        "calendar_webinar": {},
        "connection_id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateCalendarWebinarRequest](../../models/operations/createcalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateCalendarWebinarResponse](../../models/operations/createcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_webinar

Retrieve a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarWebinar" method="get" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.get_calendar_webinar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetCalendarWebinarRequest](../../models/operations/getcalendarwebinarrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetCalendarWebinarResponse](../../models/operations/getcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_webinars

List all webinars

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarWebinars" method="get" path="/calendar/{connection_id}/webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.list_calendar_webinars(request={
        "connection_id": "<id>",
    })

    assert res.calendar_webinars is not None

    # Handle response
    print(res.calendar_webinars)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListCalendarWebinarsRequest](../../models/operations/listcalendarwebinarsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListCalendarWebinarsResponse](../../models/operations/listcalendarwebinarsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_webinar

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarWebinar" method="patch" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.patch_calendar_webinar(request={
        "calendar_webinar": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchCalendarWebinarRequest](../../models/operations/patchcalendarwebinarrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchCalendarWebinarResponse](../../models/operations/patchcalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_webinar

Remove a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarWebinar" method="delete" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.remove_calendar_webinar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveCalendarWebinarRequest](../../models/operations/removecalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveCalendarWebinarResponse](../../models/operations/removecalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_webinar

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarWebinar" method="put" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.update_calendar_webinar(request={
        "calendar_webinar": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateCalendarWebinarRequest](../../models/operations/updatecalendarwebinarrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateCalendarWebinarResponse](../../models/operations/updatecalendarwebinarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |