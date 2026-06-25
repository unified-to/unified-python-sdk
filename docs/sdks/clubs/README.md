# Clubs

## Overview

### Available Operations

* [get_clubs_activity2](#get_clubs_activity2) - Retrieve an activity
* [get_clubs_event2](#get_clubs_event2) - Retrieve an event
* [get_clubs_group2](#get_clubs_group2) - Retrieve a group
* [get_clubs_location2](#get_clubs_location2) - Retrieve a location
* [get_clubs_member2](#get_clubs_member2) - Retrieve a member
* [list_clubs_activities2](#list_clubs_activities2) - List all activities
* [list_clubs_events2](#list_clubs_events2) - List all events
* [list_clubs_groups2](#list_clubs_groups2) - List all groups
* [list_clubs_locations2](#list_clubs_locations2) - List all locations
* [list_clubs_members2](#list_clubs_members2) - List all members

## get_clubs_activity2

Retrieve an activity

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsActivity2" method="get" path="/clubs/{connection_id}/activity/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.get_clubs_activity2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_activity is not None

    # Handle response
    print(res.clubs_activity)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetClubsActivity2Request](../../models/operations/getclubsactivity2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetClubsActivity2Response](../../models/operations/getclubsactivity2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_event2

Retrieve an event

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsEvent2" method="get" path="/clubs/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.get_clubs_event2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_event is not None

    # Handle response
    print(res.clubs_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetClubsEvent2Request](../../models/operations/getclubsevent2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetClubsEvent2Response](../../models/operations/getclubsevent2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_group2

Retrieve a group

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsGroup2" method="get" path="/clubs/{connection_id}/group/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.get_clubs_group2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_group is not None

    # Handle response
    print(res.clubs_group)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetClubsGroup2Request](../../models/operations/getclubsgroup2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetClubsGroup2Response](../../models/operations/getclubsgroup2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_location2

Retrieve a location

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsLocation2" method="get" path="/clubs/{connection_id}/location/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.get_clubs_location2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_location is not None

    # Handle response
    print(res.clubs_location)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetClubsLocation2Request](../../models/operations/getclubslocation2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetClubsLocation2Response](../../models/operations/getclubslocation2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clubs_member2

Retrieve a member

### Example Usage

<!-- UsageSnippet language="python" operationID="getClubsMember2" method="get" path="/clubs/{connection_id}/member/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.get_clubs_member2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.clubs_member is not None

    # Handle response
    print(res.clubs_member)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetClubsMember2Request](../../models/operations/getclubsmember2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetClubsMember2Response](../../models/operations/getclubsmember2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_activities2

List all activities

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsActivities2" method="get" path="/clubs/{connection_id}/activity" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.list_clubs_activities2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_activities is not None

    # Handle response
    print(res.clubs_activities)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListClubsActivities2Request](../../models/operations/listclubsactivities2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListClubsActivities2Response](../../models/operations/listclubsactivities2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_events2

List all events

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsEvents2" method="get" path="/clubs/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.list_clubs_events2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_events is not None

    # Handle response
    print(res.clubs_events)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListClubsEvents2Request](../../models/operations/listclubsevents2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListClubsEvents2Response](../../models/operations/listclubsevents2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_groups2

List all groups

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsGroups2" method="get" path="/clubs/{connection_id}/group" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.list_clubs_groups2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_groups is not None

    # Handle response
    print(res.clubs_groups)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListClubsGroups2Request](../../models/operations/listclubsgroups2request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListClubsGroups2Response](../../models/operations/listclubsgroups2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_locations2

List all locations

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsLocations2" method="get" path="/clubs/{connection_id}/location" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.list_clubs_locations2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_locations is not None

    # Handle response
    print(res.clubs_locations)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListClubsLocations2Request](../../models/operations/listclubslocations2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListClubsLocations2Response](../../models/operations/listclubslocations2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_clubs_members2

List all members

### Example Usage

<!-- UsageSnippet language="python" operationID="listClubsMembers2" method="get" path="/clubs/{connection_id}/member" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.clubs.list_clubs_members2(request={
        "connection_id": "<id>",
    })

    assert res.clubs_members is not None

    # Handle response
    print(res.clubs_members)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListClubsMembers2Request](../../models/operations/listclubsmembers2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListClubsMembers2Response](../../models/operations/listclubsmembers2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |