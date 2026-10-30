# Analytics

## Overview

### Available Operations

* [create_analytics_event](#create_analytics_event) - Create an event
* [create_analytics_property](#create_analytics_property) - Create a property
* [create_analytics_visitor](#create_analytics_visitor) - Create a visitor
* [get_analytics_event](#get_analytics_event) - Retrieve an event
* [get_analytics_property](#get_analytics_property) - Retrieve a property
* [get_analytics_session](#get_analytics_session) - Retrieve a session
* [get_analytics_visitor](#get_analytics_visitor) - Retrieve a visitor
* [list_analytics_events](#list_analytics_events) - List all events
* [list_analytics_properties](#list_analytics_properties) - List all properties
* [list_analytics_reports](#list_analytics_reports) - List all reports
* [list_analytics_sessions](#list_analytics_sessions) - List all sessions
* [list_analytics_visitors](#list_analytics_visitors) - List all visitors
* [patch_analytics_property](#patch_analytics_property) - Update a property
* [patch_analytics_visitor](#patch_analytics_visitor) - Update a visitor
* [remove_analytics_property](#remove_analytics_property) - Remove a property
* [remove_analytics_visitor](#remove_analytics_visitor) - Remove a visitor
* [update_analytics_property](#update_analytics_property) - Update a property
* [update_analytics_visitor](#update_analytics_visitor) - Update a visitor

## create_analytics_event

Creates a AnalyticsEvent. Provide the unified AnalyticsEvent fields in the request body; they are mapped to the provider's API. Returns the created AnalyticsEvent.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsEvent" method="post" path="/analytics/{connection_id}/event" example="analytics_event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_event(request={
        "analytics_event": {
            "created_at": parse_datetime("2023-06-21T03:13:22.954Z"),
            "event_type": shared.EventType.SCREEN_VIEW,
            "id": "fd13e109-3a25-40ca-946b-d166b45a26fd",
            "metadata": {
                "key": {},
            },
            "name": "page_view",
            "page_url": "https://golden-carboxyl.biz",
            "updated_at": parse_datetime("2023-09-25T09:23:59.346Z"),
        },
        "connection_id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAnalyticsEventRequest](../../models/operations/createanalyticseventrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAnalyticsEventResponse](../../models/operations/createanalyticseventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_analytics_property

Creates a AnalyticsProperty. Provide the unified AnalyticsProperty fields in the request body; they are mapped to the provider's API. Returns the created AnalyticsProperty.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsProperty" method="post" path="/analytics/{connection_id}/property" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "77bc2dcc-16d4-4671-8482-7406411d94da",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:29:17.144Z"),
        },
        "connection_id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAnalyticsPropertyRequest](../../models/operations/createanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAnalyticsPropertyResponse](../../models/operations/createanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_analytics_visitor

Creates a AnalyticsVisitor. Provide the unified AnalyticsVisitor fields in the request body; they are mapped to the provider's API. Returns the created AnalyticsVisitor.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsVisitor" method="post" path="/analytics/{connection_id}/visitor" example="analytics_visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "8c1ae2ad-a86f-4f64-b042-b25880386837",
            "last_seen_at": parse_datetime("2025-01-17T21:20:37.124Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-06T22:30:32.343Z"),
        },
        "connection_id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateAnalyticsVisitorRequest](../../models/operations/createanalyticsvisitorrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateAnalyticsVisitorResponse](../../models/operations/createanalyticsvisitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_event

Retrieves a single AnalyticsEvent by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsEvent" method="get" path="/analytics/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAnalyticsEventRequest](../../models/operations/getanalyticseventrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAnalyticsEventResponse](../../models/operations/getanalyticseventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_property

Retrieves a single AnalyticsProperty by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsProperty" method="get" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_property(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsPropertyRequest](../../models/operations/getanalyticspropertyrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsPropertyResponse](../../models/operations/getanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_session

Retrieves a single AnalyticsSession by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsSession" method="get" path="/analytics/{connection_id}/session/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_session(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_session is not None

    # Handle response
    print(res.analytics_session)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAnalyticsSessionRequest](../../models/operations/getanalyticssessionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetAnalyticsSessionResponse](../../models/operations/getanalyticssessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_visitor

Retrieves a single AnalyticsVisitor by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsVisitor" method="get" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_visitor(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAnalyticsVisitorRequest](../../models/operations/getanalyticsvisitorrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetAnalyticsVisitorResponse](../../models/operations/getanalyticsvisitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_events

Returns a list of AnalyticsEvents. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsEvents" method="get" path="/analytics/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_events(request={
        "connection_id": "<id>",
    })

    assert res.analytics_events is not None

    # Handle response
    print(res.analytics_events)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAnalyticsEventsRequest](../../models/operations/listanalyticseventsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAnalyticsEventsResponse](../../models/operations/listanalyticseventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_properties

Returns a list of AnalyticsProperties. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsProperties" method="get" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_properties(request={
        "connection_id": "<id>",
    })

    assert res.analytics_properties is not None

    # Handle response
    print(res.analytics_properties)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAnalyticsPropertiesRequest](../../models/operations/listanalyticspropertiesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAnalyticsPropertiesResponse](../../models/operations/listanalyticspropertiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_reports

Returns a list of AnalyticsReports. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsReports" method="get" path="/analytics/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_reports(request={
        "connection_id": "<id>",
    })

    assert res.analytics_reports is not None

    # Handle response
    print(res.analytics_reports)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAnalyticsReportsRequest](../../models/operations/listanalyticsreportsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAnalyticsReportsResponse](../../models/operations/listanalyticsreportsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_sessions

Returns a list of AnalyticsSessions. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsSessions" method="get" path="/analytics/{connection_id}/session" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_sessions(request={
        "connection_id": "<id>",
    })

    assert res.analytics_sessions is not None

    # Handle response
    print(res.analytics_sessions)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAnalyticsSessionsRequest](../../models/operations/listanalyticssessionsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAnalyticsSessionsResponse](../../models/operations/listanalyticssessionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_visitors

Returns a list of AnalyticsVisitors. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsVisitors" method="get" path="/analytics/{connection_id}/visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_visitors(request={
        "connection_id": "<id>",
    })

    assert res.analytics_visitors is not None

    # Handle response
    print(res.analytics_visitors)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAnalyticsVisitorsRequest](../../models/operations/listanalyticsvisitorsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAnalyticsVisitorsResponse](../../models/operations/listanalyticsvisitorsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_property

Updates the AnalyticsProperty identified by `id`. Provide the unified AnalyticsProperty fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsProperty" method="patch" path="/analytics/{connection_id}/property/{id}" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.patch_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "00a7118c-c888-496d-b6c1-2c52263167c4",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:29:17.144Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAnalyticsPropertyRequest](../../models/operations/patchanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAnalyticsPropertyResponse](../../models/operations/patchanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_visitor

Updates the AnalyticsVisitor identified by `id`. Provide the unified AnalyticsVisitor fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsVisitor" method="patch" path="/analytics/{connection_id}/visitor/{id}" example="analytics_visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.patch_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "93b6187e-4256-431c-81d4-4c12dd7514b9",
            "last_seen_at": parse_datetime("2025-01-17T21:20:37.135Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-06T22:30:32.354Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchAnalyticsVisitorRequest](../../models/operations/patchanalyticsvisitorrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchAnalyticsVisitorResponse](../../models/operations/patchanalyticsvisitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_property

Deletes the AnalyticsProperty identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsProperty" method="delete" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.remove_analytics_property(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAnalyticsPropertyRequest](../../models/operations/removeanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAnalyticsPropertyResponse](../../models/operations/removeanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_visitor

Deletes the AnalyticsVisitor identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsVisitor" method="delete" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.remove_analytics_visitor(request={
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
| `request`                                                                                            | [operations.RemoveAnalyticsVisitorRequest](../../models/operations/removeanalyticsvisitorrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveAnalyticsVisitorResponse](../../models/operations/removeanalyticsvisitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_analytics_property

Updates the AnalyticsProperty identified by `id`. Provide the unified AnalyticsProperty fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsProperty" method="put" path="/analytics/{connection_id}/property/{id}" example="analytics_property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.update_analytics_property(request={
        "analytics_property": {
            "created_at": parse_datetime("2021-09-05T19:04:58.430Z"),
            "currency": "USD",
            "id": "00a7118c-c888-496d-b6c1-2c52263167c4",
            "name": "Daniel, Goldner and Dickinson",
            "timezone": "UTC",
            "updated_at": parse_datetime("2021-09-14T21:29:17.144Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAnalyticsPropertyRequest](../../models/operations/updateanalyticspropertyrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAnalyticsPropertyResponse](../../models/operations/updateanalyticspropertyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_analytics_visitor

Updates the AnalyticsVisitor identified by `id`. Provide the unified AnalyticsVisitor fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsVisitor" method="put" path="/analytics/{connection_id}/visitor/{id}" example="analytics_visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.update_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "93b6187e-4256-431c-81d4-4c12dd7514b9",
            "last_seen_at": parse_datetime("2025-01-17T21:20:37.135Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-06T22:30:32.354Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateAnalyticsVisitorRequest](../../models/operations/updateanalyticsvisitorrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateAnalyticsVisitorResponse](../../models/operations/updateanalyticsvisitorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |