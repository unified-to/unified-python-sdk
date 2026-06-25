# Webinar

## Overview

### Available Operations

* [create_calendar_webinar2](#create_calendar_webinar2) - Create a webinar
* [get_calendar_webinar2](#get_calendar_webinar2) - Retrieve a webinar
* [list_calendar_webinars2](#list_calendar_webinars2) - List all webinars
* [patch_calendar_webinar2](#patch_calendar_webinar2) - Update a webinar
* [remove_calendar_webinar2](#remove_calendar_webinar2) - Remove a webinar
* [update_calendar_webinar2](#update_calendar_webinar2) - Update a webinar

## create_calendar_webinar2

Create a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarWebinar2" method="post" path="/calendar/{connection_id}/webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.create_calendar_webinar2(request={
        "calendar_webinar": {},
        "connection_id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateCalendarWebinar2Request](../../models/operations/createcalendarwebinar2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateCalendarWebinar2Response](../../models/operations/createcalendarwebinar2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_webinar2

Retrieve a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarWebinar2" method="get" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.get_calendar_webinar2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCalendarWebinar2Request](../../models/operations/getcalendarwebinar2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetCalendarWebinar2Response](../../models/operations/getcalendarwebinar2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_webinars2

List all webinars

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarWebinars2" method="get" path="/calendar/{connection_id}/webinar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.list_calendar_webinars2(request={
        "connection_id": "<id>",
    })

    assert res.calendar_webinars is not None

    # Handle response
    print(res.calendar_webinars)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCalendarWebinars2Request](../../models/operations/listcalendarwebinars2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListCalendarWebinars2Response](../../models/operations/listcalendarwebinars2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_webinar2

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarWebinar2" method="patch" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.patch_calendar_webinar2(request={
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
| `request`                                                                                          | [operations.PatchCalendarWebinar2Request](../../models/operations/patchcalendarwebinar2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchCalendarWebinar2Response](../../models/operations/patchcalendarwebinar2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_webinar2

Remove a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarWebinar2" method="delete" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.remove_calendar_webinar2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveCalendarWebinar2Request](../../models/operations/removecalendarwebinar2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveCalendarWebinar2Response](../../models/operations/removecalendarwebinar2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_webinar2

Update a webinar

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarWebinar2" method="put" path="/calendar/{connection_id}/webinar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.webinar.update_calendar_webinar2(request={
        "calendar_webinar": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_webinar is not None

    # Handle response
    print(res.calendar_webinar)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateCalendarWebinar2Request](../../models/operations/updatecalendarwebinar2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateCalendarWebinar2Response](../../models/operations/updatecalendarwebinar2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |