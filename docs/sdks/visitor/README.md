# Visitor

## Overview

### Available Operations

* [create_analytics_visitor](#create_analytics_visitor) - Create a visitor
* [get_analytics_visitor](#get_analytics_visitor) - Retrieve a visitor
* [list_analytics_visitors](#list_analytics_visitors) - List all visitors
* [patch_analytics_visitor](#patch_analytics_visitor) - Update a visitor
* [remove_analytics_visitor](#remove_analytics_visitor) - Remove a visitor
* [update_analytics_visitor](#update_analytics_visitor) - Update a visitor

## create_analytics_visitor

Create a visitor

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

    res = unified_to.visitor.create_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "Dallas_Mitchell@yahoo.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "c4f48c8f-56d2-4cc8-b3f0-9a83509307e5",
            "last_seen_at": parse_datetime("2021-12-04T18:09:09.077Z"),
            "metadata": {
                "segment": {},
            },
            "name": "Desiree O'Hara",
            "total_events": 3639.0,
            "updated_at": parse_datetime("2025-06-03T08:27:48.122Z"),
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

## get_analytics_visitor

Retrieve a visitor

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

    res = unified_to.visitor.get_analytics_visitor(request={
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

## list_analytics_visitors

List all visitors

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

    res = unified_to.visitor.list_analytics_visitors(request={
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

## patch_analytics_visitor

Update a visitor

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

    res = unified_to.visitor.patch_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "Dallas_Mitchell@yahoo.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "88e685e7-218d-418d-889f-1a6162b7ce74",
            "last_seen_at": parse_datetime("2021-12-04T18:09:09.082Z"),
            "metadata": {
                "segment": {},
            },
            "name": "Desiree O'Hara",
            "total_events": 3639.0,
            "updated_at": parse_datetime("2025-06-03T08:27:48.137Z"),
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

## remove_analytics_visitor

Remove a visitor

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

    res = unified_to.visitor.remove_analytics_visitor(request={
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

## update_analytics_visitor

Update a visitor

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

    res = unified_to.visitor.update_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "Dallas_Mitchell@yahoo.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "88e685e7-218d-418d-889f-1a6162b7ce74",
            "last_seen_at": parse_datetime("2021-12-04T18:09:09.082Z"),
            "metadata": {
                "segment": {},
            },
            "name": "Desiree O'Hara",
            "total_events": 3639.0,
            "updated_at": parse_datetime("2025-06-03T08:27:48.137Z"),
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