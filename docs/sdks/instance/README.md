# Instance

## Overview

### Available Operations

* [create_compute_instance](#create_compute_instance) - Create an instance
* [get_compute_instance](#get_compute_instance) - Retrieve an instance
* [list_compute_instances](#list_compute_instances) - List all instances
* [patch_compute_instance](#patch_compute_instance) - Update an instance
* [remove_compute_instance](#remove_compute_instance) - Remove an instance
* [update_compute_instance](#update_compute_instance) - Update an instance

## create_compute_instance

Create an instance

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeInstance" method="post" path="/compute/{connection_id}/instance" example="compute_instance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.create_compute_instance(request={
        "compute_instance": {
            "allowed_actions": [
                shared.PropertyComputeInstanceAllowedActions.TERMINATE,
            ],
            "architecture": shared.ComputeInstanceArchitecture.OTHER,
            "cpu_count": 8.0,
            "created_at": parse_datetime("2022-10-07T14:18:53.874Z"),
            "currency": "USD",
            "disk_mb": 1024000.0,
            "endpoints": [
                {
                    "is_auth_required": True,
                    "port": 8080.0,
                    "protocol": shared.Protocol.HTTPS,
                    "url": "https://serene-shark.biz/",
                },
            ],
            "gpu_count": 0.0,
            "has_internet_access": True,
            "id": "87ce3443-5e83-4fb2-8f2a-d1c34c1171de",
            "image": "ubuntu:24.04",
            "market": shared.Market.SPOT,
            "memory_mb": 2048.0,
            "metadata": [],
            "name": "digital-panel",
            "on_idle": shared.OnIdle.TERMINATE,
            "price_amount": 24.90336107776966,
            "price_unit": shared.PriceUnit.PER_INSTANCE_HOUR,
            "project_identifier": "g547KrivqY",
            "ssh": {
                "host": "116.42.165.89",
                "port": 22.0,
                "username": "root",
            },
            "started_at": parse_datetime("2025-03-18T21:30:38.003Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-10T15:38:02.618Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_instance is not None

    # Handle response
    print(res.compute_instance)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateComputeInstanceRequest](../../models/operations/createcomputeinstancerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateComputeInstanceResponse](../../models/operations/createcomputeinstanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_instance

Retrieve an instance

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeInstance" method="get" path="/compute/{connection_id}/instance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.get_compute_instance(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_instance is not None

    # Handle response
    print(res.compute_instance)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetComputeInstanceRequest](../../models/operations/getcomputeinstancerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetComputeInstanceResponse](../../models/operations/getcomputeinstanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_instances

List all instances

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeInstances" method="get" path="/compute/{connection_id}/instance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.list_compute_instances(request={
        "connection_id": "<id>",
    })

    assert res.compute_instances is not None

    # Handle response
    print(res.compute_instances)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListComputeInstancesRequest](../../models/operations/listcomputeinstancesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListComputeInstancesResponse](../../models/operations/listcomputeinstancesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_instance

Update an instance

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeInstance" method="patch" path="/compute/{connection_id}/instance/{id}" example="compute_instance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.patch_compute_instance(request={
        "compute_instance": {
            "allowed_actions": [
                shared.PropertyComputeInstanceAllowedActions.TERMINATE,
            ],
            "architecture": shared.ComputeInstanceArchitecture.OTHER,
            "cpu_count": 8.0,
            "created_at": parse_datetime("2022-10-07T14:18:53.874Z"),
            "currency": "USD",
            "disk_mb": 1024000.0,
            "endpoints": [
                {
                    "is_auth_required": True,
                    "port": 8080.0,
                    "protocol": shared.Protocol.HTTPS,
                    "url": "https://serene-shark.biz/",
                },
            ],
            "gpu_count": 0.0,
            "has_internet_access": True,
            "id": "4137c17b-ea0a-44ca-bef8-2c7105d598c2",
            "image": "ubuntu:24.04",
            "market": shared.Market.SPOT,
            "memory_mb": 2048.0,
            "metadata": [],
            "name": "digital-panel",
            "on_idle": shared.OnIdle.TERMINATE,
            "price_amount": 24.90336107776966,
            "price_unit": shared.PriceUnit.PER_INSTANCE_HOUR,
            "project_identifier": "g547KrivqY",
            "ssh": {
                "host": "116.42.165.89",
                "port": 22.0,
                "username": "root",
            },
            "started_at": parse_datetime("2025-03-18T21:30:38.031Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-10T15:38:02.649Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_instance is not None

    # Handle response
    print(res.compute_instance)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchComputeInstanceRequest](../../models/operations/patchcomputeinstancerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchComputeInstanceResponse](../../models/operations/patchcomputeinstanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_instance

Remove an instance

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeInstance" method="delete" path="/compute/{connection_id}/instance/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.remove_compute_instance(request={
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
| `request`                                                                                          | [operations.RemoveComputeInstanceRequest](../../models/operations/removecomputeinstancerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveComputeInstanceResponse](../../models/operations/removecomputeinstanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_instance

Update an instance

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeInstance" method="put" path="/compute/{connection_id}/instance/{id}" example="compute_instance" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.instance.update_compute_instance(request={
        "compute_instance": {
            "allowed_actions": [
                shared.PropertyComputeInstanceAllowedActions.TERMINATE,
            ],
            "architecture": shared.ComputeInstanceArchitecture.OTHER,
            "cpu_count": 8.0,
            "created_at": parse_datetime("2022-10-07T14:18:53.874Z"),
            "currency": "USD",
            "disk_mb": 1024000.0,
            "endpoints": [
                {
                    "is_auth_required": True,
                    "port": 8080.0,
                    "protocol": shared.Protocol.HTTPS,
                    "url": "https://serene-shark.biz/",
                },
            ],
            "gpu_count": 0.0,
            "has_internet_access": True,
            "id": "4137c17b-ea0a-44ca-bef8-2c7105d598c2",
            "image": "ubuntu:24.04",
            "market": shared.Market.SPOT,
            "memory_mb": 2048.0,
            "metadata": [],
            "name": "digital-panel",
            "on_idle": shared.OnIdle.TERMINATE,
            "price_amount": 24.90336107776966,
            "price_unit": shared.PriceUnit.PER_INSTANCE_HOUR,
            "project_identifier": "g547KrivqY",
            "ssh": {
                "host": "116.42.165.89",
                "port": 22.0,
                "username": "root",
            },
            "started_at": parse_datetime("2025-03-18T21:30:38.031Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-10T15:38:02.649Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_instance is not None

    # Handle response
    print(res.compute_instance)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateComputeInstanceRequest](../../models/operations/updatecomputeinstancerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateComputeInstanceResponse](../../models/operations/updatecomputeinstanceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |