# Service

## Overview

### Available Operations

* [create_compute_service](#create_compute_service) - Create a service
* [get_compute_service](#get_compute_service) - Retrieve a service
* [list_compute_services](#list_compute_services) - List all services
* [patch_compute_service](#patch_compute_service) - Update a service
* [remove_compute_service](#remove_compute_service) - Remove a service
* [update_compute_service](#update_compute_service) - Update a service

## create_compute_service

Create a service

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeService" method="post" path="/compute/{connection_id}/service" example="compute_service" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.create_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "f2b4a9f6-bb79-465b-a438-8abf1f136486",
            "instance_count": 6.0,
            "max_instance_count": 6.0,
            "metadata": [],
            "min_instance_count": 1.0,
            "name": "tame-sideboard",
            "project_identifier": "4nyWICvPfi",
            "repo_url": "https://github.com/Kimberly_Muller95/tame-sideboard",
            "runtime": "python",
            "status": shared.ComputeServiceStatus.SUSPENDED,
            "type": shared.ComputeServiceType.OTHER,
            "updated_at": parse_datetime("2025-03-31T13:58:33.119Z"),
            "url": "https://tame-sideboard.rotating-shoulder.biz",
        },
        "connection_id": "<id>",
    })

    assert res.compute_service is not None

    # Handle response
    print(res.compute_service)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateComputeServiceRequest](../../models/operations/createcomputeservicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateComputeServiceResponse](../../models/operations/createcomputeserviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_service

Retrieve a service

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeService" method="get" path="/compute/{connection_id}/service/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.get_compute_service(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_service is not None

    # Handle response
    print(res.compute_service)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetComputeServiceRequest](../../models/operations/getcomputeservicerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetComputeServiceResponse](../../models/operations/getcomputeserviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_services

List all services

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeServices" method="get" path="/compute/{connection_id}/service" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.list_compute_services(request={
        "connection_id": "<id>",
    })

    assert res.compute_services is not None

    # Handle response
    print(res.compute_services)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListComputeServicesRequest](../../models/operations/listcomputeservicesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListComputeServicesResponse](../../models/operations/listcomputeservicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_service

Update a service

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeService" method="patch" path="/compute/{connection_id}/service/{id}" example="compute_service" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.patch_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "2cbb869e-6003-4247-b58c-8908aad99d64",
            "instance_count": 6.0,
            "max_instance_count": 6.0,
            "metadata": [],
            "min_instance_count": 1.0,
            "name": "tame-sideboard",
            "project_identifier": "4nyWICvPfi",
            "repo_url": "https://github.com/Kimberly_Muller95/tame-sideboard",
            "runtime": "python",
            "status": shared.ComputeServiceStatus.SUSPENDED,
            "type": shared.ComputeServiceType.OTHER,
            "updated_at": parse_datetime("2025-03-31T13:58:33.132Z"),
            "url": "https://tame-sideboard.rotating-shoulder.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_service is not None

    # Handle response
    print(res.compute_service)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchComputeServiceRequest](../../models/operations/patchcomputeservicerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchComputeServiceResponse](../../models/operations/patchcomputeserviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_service

Remove a service

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeService" method="delete" path="/compute/{connection_id}/service/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.remove_compute_service(request={
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
| `request`                                                                                        | [operations.RemoveComputeServiceRequest](../../models/operations/removecomputeservicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveComputeServiceResponse](../../models/operations/removecomputeserviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_service

Update a service

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeService" method="put" path="/compute/{connection_id}/service/{id}" example="compute_service" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.service.update_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "2cbb869e-6003-4247-b58c-8908aad99d64",
            "instance_count": 6.0,
            "max_instance_count": 6.0,
            "metadata": [],
            "min_instance_count": 1.0,
            "name": "tame-sideboard",
            "project_identifier": "4nyWICvPfi",
            "repo_url": "https://github.com/Kimberly_Muller95/tame-sideboard",
            "runtime": "python",
            "status": shared.ComputeServiceStatus.SUSPENDED,
            "type": shared.ComputeServiceType.OTHER,
            "updated_at": parse_datetime("2025-03-31T13:58:33.132Z"),
            "url": "https://tame-sideboard.rotating-shoulder.biz",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_service is not None

    # Handle response
    print(res.compute_service)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateComputeServiceRequest](../../models/operations/updatecomputeservicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateComputeServiceResponse](../../models/operations/updatecomputeserviceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |