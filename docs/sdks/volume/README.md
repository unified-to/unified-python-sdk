# Volume

## Overview

### Available Operations

* [create_compute_volume](#create_compute_volume) - Create a volume
* [get_compute_volume](#get_compute_volume) - Retrieve a volume
* [list_compute_volumes](#list_compute_volumes) - List all volumes
* [patch_compute_volume](#patch_compute_volume) - Update a volume
* [remove_compute_volume](#remove_compute_volume) - Remove a volume
* [update_compute_volume](#update_compute_volume) - Update a volume

## create_compute_volume

Create a volume

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeVolume" method="post" path="/compute/{connection_id}/volume" example="compute_volume" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.create_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "16aeff81-972a-45c5-a16f-a067a63d82f7",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-08T15:40:13.558Z"),
            "used_mb": 524986.0,
        },
        "connection_id": "<id>",
    })

    assert res.compute_volume is not None

    # Handle response
    print(res.compute_volume)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateComputeVolumeRequest](../../models/operations/createcomputevolumerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateComputeVolumeResponse](../../models/operations/createcomputevolumeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_volume

Retrieve a volume

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeVolume" method="get" path="/compute/{connection_id}/volume/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.get_compute_volume(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_volume is not None

    # Handle response
    print(res.compute_volume)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeVolumeRequest](../../models/operations/getcomputevolumerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeVolumeResponse](../../models/operations/getcomputevolumeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_volumes

List all volumes

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeVolumes" method="get" path="/compute/{connection_id}/volume" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.list_compute_volumes(request={
        "connection_id": "<id>",
    })

    assert res.compute_volumes is not None

    # Handle response
    print(res.compute_volumes)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeVolumesRequest](../../models/operations/listcomputevolumesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeVolumesResponse](../../models/operations/listcomputevolumesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_volume

Update a volume

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeVolume" method="patch" path="/compute/{connection_id}/volume/{id}" example="compute_volume" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.patch_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "dda9a36b-118b-479e-ab91-3f1ec27564d1",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-08T15:40:13.561Z"),
            "used_mb": 524986.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_volume is not None

    # Handle response
    print(res.compute_volume)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchComputeVolumeRequest](../../models/operations/patchcomputevolumerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchComputeVolumeResponse](../../models/operations/patchcomputevolumeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_volume

Remove a volume

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeVolume" method="delete" path="/compute/{connection_id}/volume/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.remove_compute_volume(request={
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
| `request`                                                                                      | [operations.RemoveComputeVolumeRequest](../../models/operations/removecomputevolumerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveComputeVolumeResponse](../../models/operations/removecomputevolumeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_volume

Update a volume

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeVolume" method="put" path="/compute/{connection_id}/volume/{id}" example="compute_volume" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.volume.update_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "dda9a36b-118b-479e-ab91-3f1ec27564d1",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-08T15:40:13.561Z"),
            "used_mb": 524986.0,
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_volume is not None

    # Handle response
    print(res.compute_volume)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateComputeVolumeRequest](../../models/operations/updatecomputevolumerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateComputeVolumeResponse](../../models/operations/updatecomputevolumeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |