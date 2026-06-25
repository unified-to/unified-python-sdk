# Analytics

## Overview

### Available Operations

* [create_analytics_event2](#create_analytics_event2) - Create an event
* [create_analytics_property2](#create_analytics_property2) - Create a property
* [create_analytics_visitor2](#create_analytics_visitor2) - Create a visitor
* [get_analytics_event2](#get_analytics_event2) - Retrieve an event
* [get_analytics_property2](#get_analytics_property2) - Retrieve a property
* [get_analytics_session2](#get_analytics_session2) - Retrieve a session
* [get_analytics_visitor2](#get_analytics_visitor2) - Retrieve a visitor
* [list_analytics_events2](#list_analytics_events2) - List all events
* [list_analytics_properties2](#list_analytics_properties2) - List all properties
* [list_analytics_reports2](#list_analytics_reports2) - List all reports
* [list_analytics_sessions2](#list_analytics_sessions2) - List all sessions
* [list_analytics_visitors2](#list_analytics_visitors2) - List all visitors
* [patch_analytics_property2](#patch_analytics_property2) - Update a property
* [patch_analytics_visitor2](#patch_analytics_visitor2) - Update a visitor
* [remove_analytics_property2](#remove_analytics_property2) - Remove a property
* [remove_analytics_visitor2](#remove_analytics_visitor2) - Remove a visitor
* [update_analytics_property2](#update_analytics_property2) - Update a property
* [update_analytics_visitor2](#update_analytics_visitor2) - Update a visitor

## create_analytics_event2

Create an event

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsEvent2" method="post" path="/analytics/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_event2(request={
        "analytics_event": {},
        "connection_id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAnalyticsEvent2Request](../../models/operations/createanalyticsevent2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAnalyticsEvent2Response](../../models/operations/createanalyticsevent2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_analytics_property2

Create a property

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsProperty2" method="post" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_property2(request={
        "analytics_property": {},
        "connection_id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAnalyticsProperty2Request](../../models/operations/createanalyticsproperty2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateAnalyticsProperty2Response](../../models/operations/createanalyticsproperty2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_analytics_visitor2

Create a visitor

### Example Usage

<!-- UsageSnippet language="python" operationID="createAnalyticsVisitor2" method="post" path="/analytics/{connection_id}/visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.create_analytics_visitor2(request={
        "analytics_visitor": {},
        "connection_id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAnalyticsVisitor2Request](../../models/operations/createanalyticsvisitor2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAnalyticsVisitor2Response](../../models/operations/createanalyticsvisitor2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_event2

Retrieve an event

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsEvent2" method="get" path="/analytics/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_event2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_event is not None

    # Handle response
    print(res.analytics_event)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAnalyticsEvent2Request](../../models/operations/getanalyticsevent2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAnalyticsEvent2Response](../../models/operations/getanalyticsevent2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_property2

Retrieve a property

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsProperty2" method="get" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_property2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAnalyticsProperty2Request](../../models/operations/getanalyticsproperty2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAnalyticsProperty2Response](../../models/operations/getanalyticsproperty2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_session2

Retrieve a session

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsSession2" method="get" path="/analytics/{connection_id}/session/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_session2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_session is not None

    # Handle response
    print(res.analytics_session)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsSession2Request](../../models/operations/getanalyticssession2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsSession2Response](../../models/operations/getanalyticssession2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_analytics_visitor2

Retrieve a visitor

### Example Usage

<!-- UsageSnippet language="python" operationID="getAnalyticsVisitor2" method="get" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.get_analytics_visitor2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAnalyticsVisitor2Request](../../models/operations/getanalyticsvisitor2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAnalyticsVisitor2Response](../../models/operations/getanalyticsvisitor2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_events2

List all events

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsEvents2" method="get" path="/analytics/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_events2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_events is not None

    # Handle response
    print(res.analytics_events)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAnalyticsEvents2Request](../../models/operations/listanalyticsevents2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAnalyticsEvents2Response](../../models/operations/listanalyticsevents2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_properties2

List all properties

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsProperties2" method="get" path="/analytics/{connection_id}/property" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_properties2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_properties is not None

    # Handle response
    print(res.analytics_properties)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListAnalyticsProperties2Request](../../models/operations/listanalyticsproperties2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.ListAnalyticsProperties2Response](../../models/operations/listanalyticsproperties2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_reports2

List all reports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsReports2" method="get" path="/analytics/{connection_id}/report" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_reports2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_reports is not None

    # Handle response
    print(res.analytics_reports)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAnalyticsReports2Request](../../models/operations/listanalyticsreports2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAnalyticsReports2Response](../../models/operations/listanalyticsreports2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_sessions2

List all sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsSessions2" method="get" path="/analytics/{connection_id}/session" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_sessions2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_sessions is not None

    # Handle response
    print(res.analytics_sessions)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAnalyticsSessions2Request](../../models/operations/listanalyticssessions2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAnalyticsSessions2Response](../../models/operations/listanalyticssessions2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_analytics_visitors2

List all visitors

### Example Usage

<!-- UsageSnippet language="python" operationID="listAnalyticsVisitors2" method="get" path="/analytics/{connection_id}/visitor" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.list_analytics_visitors2(request={
        "connection_id": "<id>",
    })

    assert res.analytics_visitors is not None

    # Handle response
    print(res.analytics_visitors)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAnalyticsVisitors2Request](../../models/operations/listanalyticsvisitors2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAnalyticsVisitors2Response](../../models/operations/listanalyticsvisitors2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_property2

Update a property

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsProperty2" method="patch" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.patch_analytics_property2(request={
        "analytics_property": {},
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
| `request`                                                                                              | [operations.PatchAnalyticsProperty2Request](../../models/operations/patchanalyticsproperty2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchAnalyticsProperty2Response](../../models/operations/patchanalyticsproperty2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_analytics_visitor2

Update a visitor

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAnalyticsVisitor2" method="patch" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.patch_analytics_visitor2(request={
        "analytics_visitor": {},
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
| `request`                                                                                            | [operations.PatchAnalyticsVisitor2Request](../../models/operations/patchanalyticsvisitor2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAnalyticsVisitor2Response](../../models/operations/patchanalyticsvisitor2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_property2

Remove a property

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsProperty2" method="delete" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.remove_analytics_property2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAnalyticsProperty2Request](../../models/operations/removeanalyticsproperty2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveAnalyticsProperty2Response](../../models/operations/removeanalyticsproperty2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_analytics_visitor2

Remove a visitor

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAnalyticsVisitor2" method="delete" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.remove_analytics_visitor2(request={
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
| `request`                                                                                              | [operations.RemoveAnalyticsVisitor2Request](../../models/operations/removeanalyticsvisitor2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAnalyticsVisitor2Response](../../models/operations/removeanalyticsvisitor2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_analytics_property2

Update a property

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsProperty2" method="put" path="/analytics/{connection_id}/property/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.update_analytics_property2(request={
        "analytics_property": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_property is not None

    # Handle response
    print(res.analytics_property)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAnalyticsProperty2Request](../../models/operations/updateanalyticsproperty2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateAnalyticsProperty2Response](../../models/operations/updateanalyticsproperty2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_analytics_visitor2

Update a visitor

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAnalyticsVisitor2" method="put" path="/analytics/{connection_id}/visitor/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.analytics.update_analytics_visitor2(request={
        "analytics_visitor": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.analytics_visitor is not None

    # Handle response
    print(res.analytics_visitor)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAnalyticsVisitor2Request](../../models/operations/updateanalyticsvisitor2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAnalyticsVisitor2Response](../../models/operations/updateanalyticsvisitor2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |