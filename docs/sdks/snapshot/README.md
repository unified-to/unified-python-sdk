# Snapshot

## Overview

### Available Operations

* [create_compute_snapshot](#create_compute_snapshot) - Create a snapshot
* [get_compute_snapshot](#get_compute_snapshot) - Retrieve a snapshot
* [list_compute_snapshots](#list_compute_snapshots) - List all snapshots
* [remove_compute_snapshot](#remove_compute_snapshot) - Remove a snapshot

## create_compute_snapshot

Create a snapshot

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeSnapshot" method="post" path="/compute/{connection_id}/snapshot" example="compute_snapshot" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.snapshot.create_compute_snapshot(request={
        "compute_snapshot": {
            "created_at": parse_datetime("2021-09-24T14:40:06.110Z"),
            "id": "f269958b-3607-4340-bef2-0cdc8c8ee673",
            "metadata": [],
            "name": "snap-alius",
            "size_mb": 169984.0,
            "status": shared.ComputeSnapshotStatus.DELETING,
            "type": shared.ComputeSnapshotType.DISK,
            "updated_at": parse_datetime("2026-03-30T21:19:57.943Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_snapshot is not None

    # Handle response
    print(res.compute_snapshot)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateComputeSnapshotRequest](../../models/operations/createcomputesnapshotrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateComputeSnapshotResponse](../../models/operations/createcomputesnapshotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_snapshot

Retrieve a snapshot

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeSnapshot" method="get" path="/compute/{connection_id}/snapshot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.snapshot.get_compute_snapshot(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_snapshot is not None

    # Handle response
    print(res.compute_snapshot)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetComputeSnapshotRequest](../../models/operations/getcomputesnapshotrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetComputeSnapshotResponse](../../models/operations/getcomputesnapshotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_snapshots

List all snapshots

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeSnapshots" method="get" path="/compute/{connection_id}/snapshot" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.snapshot.list_compute_snapshots(request={
        "connection_id": "<id>",
    })

    assert res.compute_snapshots is not None

    # Handle response
    print(res.compute_snapshots)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListComputeSnapshotsRequest](../../models/operations/listcomputesnapshotsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListComputeSnapshotsResponse](../../models/operations/listcomputesnapshotsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_snapshot

Remove a snapshot

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeSnapshot" method="delete" path="/compute/{connection_id}/snapshot/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.snapshot.remove_compute_snapshot(request={
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
| `request`                                                                                          | [operations.RemoveComputeSnapshotRequest](../../models/operations/removecomputesnapshotrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveComputeSnapshotResponse](../../models/operations/removecomputesnapshotresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |