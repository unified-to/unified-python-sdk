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

    res = unified_to.visitor.create_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "10f98270-8599-4be4-83f1-d4dc7e0a26d0",
            "last_seen_at": parse_datetime("2025-01-14T23:24:42.654Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-03T17:43:52.154Z"),
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

    res = unified_to.visitor.patch_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "540f7f7b-ce79-4af7-8f5c-1e8aa0e4eddf",
            "last_seen_at": parse_datetime("2025-01-14T23:24:42.666Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-03T17:43:52.167Z"),
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

    res = unified_to.visitor.update_analytics_visitor(request={
        "analytics_visitor": {
            "created_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "email": "desiree.o.hara@icloud.com",
            "first_seen_at": parse_datetime("2020-04-16T20:29:48.281Z"),
            "id": "540f7f7b-ce79-4af7-8f5c-1e8aa0e4eddf",
            "last_seen_at": parse_datetime("2025-01-14T23:24:42.666Z"),
            "metadata": {
                "segment": {},
            },
            "total_events": 2916.0,
            "updated_at": parse_datetime("2025-07-03T17:43:52.167Z"),
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