# Destination

## Overview

### Available Operations

* [create_cdp_destination](#create_cdp_destination) - Create a destination
* [get_cdp_destination](#get_cdp_destination) - Retrieve a destination
* [list_cdp_destinations](#list_cdp_destinations) - List all destinations
* [patch_cdp_destination](#patch_cdp_destination) - Update a destination
* [remove_cdp_destination](#remove_cdp_destination) - Remove a destination
* [update_cdp_destination](#update_cdp_destination) - Update a destination

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

    res = unified_to.destination.create_cdp_destination(request={
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

    res = unified_to.destination.get_cdp_destination(request={
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

    res = unified_to.destination.list_cdp_destinations(request={
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

    res = unified_to.destination.patch_cdp_destination(request={
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

    res = unified_to.destination.remove_cdp_destination(request={
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

    res = unified_to.destination.update_cdp_destination(request={
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