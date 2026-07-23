# Segment

## Overview

### Available Operations

* [create_cdp_segment](#create_cdp_segment) - Create a segment
* [get_cdp_segment](#get_cdp_segment) - Retrieve a segment
* [list_cdp_segments](#list_cdp_segments) - List all segments
* [patch_cdp_segment](#patch_cdp_segment) - Update a segment
* [remove_cdp_segment](#remove_cdp_segment) - Remove a segment
* [update_cdp_segment](#update_cdp_segment) - Update a segment

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

    res = unified_to.segment.create_cdp_segment(request={
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

    res = unified_to.segment.get_cdp_segment(request={
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

    res = unified_to.segment.list_cdp_segments(request={
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

    res = unified_to.segment.patch_cdp_segment(request={
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

    res = unified_to.segment.remove_cdp_segment(request={
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

    res = unified_to.segment.update_cdp_segment(request={
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