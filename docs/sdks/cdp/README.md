# Cdp

## Overview

### Available Operations

* [create_cdp_activation](#create_cdp_activation) - Create an activation
* [create_cdp_destination](#create_cdp_destination) - Create a destination
* [create_cdp_event](#create_cdp_event) - Create an event
* [create_cdp_profile](#create_cdp_profile) - Create a profile
* [create_cdp_segment](#create_cdp_segment) - Create a segment
* [create_cdp_source](#create_cdp_source) - Create a source
* [get_cdp_activation](#get_cdp_activation) - Retrieve an activation
* [get_cdp_destination](#get_cdp_destination) - Retrieve a destination
* [get_cdp_event](#get_cdp_event) - Retrieve an event
* [get_cdp_profile](#get_cdp_profile) - Retrieve a profile
* [get_cdp_segment](#get_cdp_segment) - Retrieve a segment
* [get_cdp_source](#get_cdp_source) - Retrieve a source
* [list_cdp_activations](#list_cdp_activations) - List all activations
* [list_cdp_destinations](#list_cdp_destinations) - List all destinations
* [list_cdp_events](#list_cdp_events) - List all events
* [list_cdp_profiles](#list_cdp_profiles) - List all profiles
* [list_cdp_segments](#list_cdp_segments) - List all segments
* [list_cdp_sources](#list_cdp_sources) - List all sources
* [patch_cdp_activation](#patch_cdp_activation) - Update an activation
* [patch_cdp_destination](#patch_cdp_destination) - Update a destination
* [patch_cdp_event](#patch_cdp_event) - Update an event
* [patch_cdp_profile](#patch_cdp_profile) - Update a profile
* [patch_cdp_segment](#patch_cdp_segment) - Update a segment
* [patch_cdp_source](#patch_cdp_source) - Update a source
* [remove_cdp_activation](#remove_cdp_activation) - Remove an activation
* [remove_cdp_destination](#remove_cdp_destination) - Remove a destination
* [remove_cdp_event](#remove_cdp_event) - Remove an event
* [remove_cdp_profile](#remove_cdp_profile) - Remove a profile
* [remove_cdp_segment](#remove_cdp_segment) - Remove a segment
* [remove_cdp_source](#remove_cdp_source) - Remove a source
* [update_cdp_activation](#update_cdp_activation) - Update an activation
* [update_cdp_destination](#update_cdp_destination) - Update a destination
* [update_cdp_event](#update_cdp_event) - Update an event
* [update_cdp_profile](#update_cdp_profile) - Update a profile
* [update_cdp_segment](#update_cdp_segment) - Update a segment
* [update_cdp_source](#update_cdp_source) - Update a source

## create_cdp_activation

Create an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpActivation" method="post" path="/cdp/{connection_id}/activation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateCdpActivationRequest](../../models/operations/createcdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateCdpActivationResponse](../../models/operations/createcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_destination

Create a destination

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpDestination" method="post" path="/cdp/{connection_id}/destination" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_destination(request={
        "cdp_destination": {},
        "connection_id": "<id>",
    })

    assert res.cdp_destination is not None

    # Handle response
    print(res.cdp_destination)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateCdpDestinationRequest](../../models/operations/createcdpdestinationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateCdpDestinationResponse](../../models/operations/createcdpdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_event

Create an event

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpEvent" method="post" path="/cdp/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCdpEventRequest](../../models/operations/createcdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateCdpEventResponse](../../models/operations/createcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_profile

Create a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpProfile" method="post" path="/cdp/{connection_id}/profile" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCdpProfileRequest](../../models/operations/createcdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCdpProfileResponse](../../models/operations/createcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_segment

Create a segment

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpSegment" method="post" path="/cdp/{connection_id}/segment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_segment(request={
        "cdp_segment": {},
        "connection_id": "<id>",
    })

    assert res.cdp_segment is not None

    # Handle response
    print(res.cdp_segment)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCdpSegmentRequest](../../models/operations/createcdpsegmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateCdpSegmentResponse](../../models/operations/createcdpsegmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_cdp_source

Create a source

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpSource" method="post" path="/cdp/{connection_id}/source" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.create_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateCdpSourceRequest](../../models/operations/createcdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateCdpSourceResponse](../../models/operations/createcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_activation

Retrieve an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpActivation" method="get" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_activation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCdpActivationRequest](../../models/operations/getcdpactivationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetCdpActivationResponse](../../models/operations/getcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_destination

Retrieve a destination

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpDestination" method="get" path="/cdp/{connection_id}/destination/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_destination(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_destination is not None

    # Handle response
    print(res.cdp_destination)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetCdpDestinationRequest](../../models/operations/getcdpdestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetCdpDestinationResponse](../../models/operations/getcdpdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_event

Retrieve an event

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpEvent" method="get" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCdpEventRequest](../../models/operations/getcdpeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetCdpEventResponse](../../models/operations/getcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_profile

Retrieve a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpProfile" method="get" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_profile(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCdpProfileRequest](../../models/operations/getcdpprofilerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCdpProfileResponse](../../models/operations/getcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_segment

Retrieve a segment

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpSegment" method="get" path="/cdp/{connection_id}/segment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_segment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_segment is not None

    # Handle response
    print(res.cdp_segment)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCdpSegmentRequest](../../models/operations/getcdpsegmentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetCdpSegmentResponse](../../models/operations/getcdpsegmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_source

Retrieve a source

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpSource" method="get" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.get_cdp_source(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCdpSourceRequest](../../models/operations/getcdpsourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetCdpSourceResponse](../../models/operations/getcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_activations

List all activations

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpActivations" method="get" path="/cdp/{connection_id}/activation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_activations(request={
        "connection_id": "<id>",
    })

    assert res.cdp_activations is not None

    # Handle response
    print(res.cdp_activations)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCdpActivationsRequest](../../models/operations/listcdpactivationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListCdpActivationsResponse](../../models/operations/listcdpactivationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_destinations

List all destinations

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpDestinations" method="get" path="/cdp/{connection_id}/destination" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_destinations(request={
        "connection_id": "<id>",
    })

    assert res.cdp_destinations is not None

    # Handle response
    print(res.cdp_destinations)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListCdpDestinationsRequest](../../models/operations/listcdpdestinationsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListCdpDestinationsResponse](../../models/operations/listcdpdestinationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_events

List all events

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpEvents" method="get" path="/cdp/{connection_id}/event" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_events(request={
        "connection_id": "<id>",
    })

    assert res.cdp_events is not None

    # Handle response
    print(res.cdp_events)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCdpEventsRequest](../../models/operations/listcdpeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListCdpEventsResponse](../../models/operations/listcdpeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_profiles

List all profiles

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpProfiles" method="get" path="/cdp/{connection_id}/profile" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_profiles(request={
        "connection_id": "<id>",
    })

    assert res.cdp_profiles is not None

    # Handle response
    print(res.cdp_profiles)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCdpProfilesRequest](../../models/operations/listcdpprofilesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListCdpProfilesResponse](../../models/operations/listcdpprofilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_segments

List all segments

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpSegments" method="get" path="/cdp/{connection_id}/segment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_segments(request={
        "connection_id": "<id>",
    })

    assert res.cdp_segments is not None

    # Handle response
    print(res.cdp_segments)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCdpSegmentsRequest](../../models/operations/listcdpsegmentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListCdpSegmentsResponse](../../models/operations/listcdpsegmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_sources

List all sources

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpSources" method="get" path="/cdp/{connection_id}/source" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.list_cdp_sources(request={
        "connection_id": "<id>",
    })

    assert res.cdp_sources is not None

    # Handle response
    print(res.cdp_sources)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListCdpSourcesRequest](../../models/operations/listcdpsourcesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListCdpSourcesResponse](../../models/operations/listcdpsourcesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_activation

Update an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpActivation" method="patch" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchCdpActivationRequest](../../models/operations/patchcdpactivationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchCdpActivationResponse](../../models/operations/patchcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_destination

Update a destination

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpDestination" method="patch" path="/cdp/{connection_id}/destination/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_destination(request={
        "cdp_destination": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_destination is not None

    # Handle response
    print(res.cdp_destination)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchCdpDestinationRequest](../../models/operations/patchcdpdestinationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchCdpDestinationResponse](../../models/operations/patchcdpdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_event

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpEvent" method="patch" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCdpEventRequest](../../models/operations/patchcdpeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchCdpEventResponse](../../models/operations/patchcdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_profile

Update a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpProfile" method="patch" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCdpProfileRequest](../../models/operations/patchcdpprofilerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCdpProfileResponse](../../models/operations/patchcdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_segment

Update a segment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpSegment" method="patch" path="/cdp/{connection_id}/segment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_segment(request={
        "cdp_segment": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_segment is not None

    # Handle response
    print(res.cdp_segment)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchCdpSegmentRequest](../../models/operations/patchcdpsegmentrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchCdpSegmentResponse](../../models/operations/patchcdpsegmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_source

Update a source

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpSource" method="patch" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.patch_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchCdpSourceRequest](../../models/operations/patchcdpsourcerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchCdpSourceResponse](../../models/operations/patchcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_activation

Remove an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpActivation" method="delete" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_activation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveCdpActivationRequest](../../models/operations/removecdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveCdpActivationResponse](../../models/operations/removecdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_destination

Remove a destination

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpDestination" method="delete" path="/cdp/{connection_id}/destination/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_destination(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveCdpDestinationRequest](../../models/operations/removecdpdestinationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveCdpDestinationResponse](../../models/operations/removecdpdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_event

Remove an event

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpEvent" method="delete" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_event(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCdpEventRequest](../../models/operations/removecdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveCdpEventResponse](../../models/operations/removecdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_profile

Remove a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpProfile" method="delete" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_profile(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCdpProfileRequest](../../models/operations/removecdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCdpProfileResponse](../../models/operations/removecdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_segment

Remove a segment

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpSegment" method="delete" path="/cdp/{connection_id}/segment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_segment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveCdpSegmentRequest](../../models/operations/removecdpsegmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveCdpSegmentResponse](../../models/operations/removecdpsegmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_source

Remove a source

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpSource" method="delete" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.remove_cdp_source(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveCdpSourceRequest](../../models/operations/removecdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveCdpSourceResponse](../../models/operations/removecdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_activation

Update an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpActivation" method="put" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateCdpActivationRequest](../../models/operations/updatecdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateCdpActivationResponse](../../models/operations/updatecdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_destination

Update a destination

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpDestination" method="put" path="/cdp/{connection_id}/destination/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_destination(request={
        "cdp_destination": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_destination is not None

    # Handle response
    print(res.cdp_destination)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateCdpDestinationRequest](../../models/operations/updatecdpdestinationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateCdpDestinationResponse](../../models/operations/updatecdpdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_event

Update an event

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpEvent" method="put" path="/cdp/{connection_id}/event/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_event(request={
        "cdp_event": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_event is not None

    # Handle response
    print(res.cdp_event)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCdpEventRequest](../../models/operations/updatecdpeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateCdpEventResponse](../../models/operations/updatecdpeventresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_profile

Update a profile

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpProfile" method="put" path="/cdp/{connection_id}/profile/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_profile(request={
        "cdp_profile": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_profile is not None

    # Handle response
    print(res.cdp_profile)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCdpProfileRequest](../../models/operations/updatecdpprofilerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCdpProfileResponse](../../models/operations/updatecdpprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_segment

Update a segment

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpSegment" method="put" path="/cdp/{connection_id}/segment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_segment(request={
        "cdp_segment": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_segment is not None

    # Handle response
    print(res.cdp_segment)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCdpSegmentRequest](../../models/operations/updatecdpsegmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateCdpSegmentResponse](../../models/operations/updatecdpsegmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_source

Update a source

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpSource" method="put" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.cdp.update_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateCdpSourceRequest](../../models/operations/updatecdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateCdpSourceResponse](../../models/operations/updatecdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |