# Compute

## Overview

### Available Operations

* [create_compute_deployment](#create_compute_deployment) - Create a deployment
* [create_compute_domain](#create_compute_domain) - Create a domain
* [create_compute_envvar](#create_compute_envvar) - Create an envvar
* [create_compute_instance](#create_compute_instance) - Create an instance
* [create_compute_key](#create_compute_key) - Create a key
* [create_compute_service](#create_compute_service) - Create a service
* [create_compute_snapshot](#create_compute_snapshot) - Create a snapshot
* [create_compute_template](#create_compute_template) - Create a template
* [create_compute_volume](#create_compute_volume) - Create a volume
* [get_compute_deployment](#get_compute_deployment) - Retrieve a deployment
* [get_compute_domain](#get_compute_domain) - Retrieve a domain
* [get_compute_envvar](#get_compute_envvar) - Retrieve an envvar
* [get_compute_gputype](#get_compute_gputype) - Retrieve a gputype
* [get_compute_instance](#get_compute_instance) - Retrieve an instance
* [get_compute_key](#get_compute_key) - Retrieve a key
* [get_compute_region](#get_compute_region) - Retrieve a region
* [get_compute_service](#get_compute_service) - Retrieve a service
* [get_compute_snapshot](#get_compute_snapshot) - Retrieve a snapshot
* [get_compute_template](#get_compute_template) - Retrieve a template
* [get_compute_volume](#get_compute_volume) - Retrieve a volume
* [list_compute_deployments](#list_compute_deployments) - List all deployments
* [list_compute_domains](#list_compute_domains) - List all domains
* [list_compute_envvars](#list_compute_envvars) - List all envvars
* [list_compute_gputypes](#list_compute_gputypes) - List all gputypes
* [list_compute_instances](#list_compute_instances) - List all instances
* [list_compute_keys](#list_compute_keys) - List all keys
* [list_compute_regions](#list_compute_regions) - List all regions
* [list_compute_services](#list_compute_services) - List all services
* [list_compute_snapshots](#list_compute_snapshots) - List all snapshots
* [list_compute_templates](#list_compute_templates) - List all templates
* [list_compute_usages](#list_compute_usages) - List all usages
* [list_compute_volumes](#list_compute_volumes) - List all volumes
* [patch_compute_deployment](#patch_compute_deployment) - Update a deployment
* [patch_compute_domain](#patch_compute_domain) - Update a domain
* [patch_compute_envvar](#patch_compute_envvar) - Update an envvar
* [patch_compute_instance](#patch_compute_instance) - Update an instance
* [patch_compute_key](#patch_compute_key) - Update a key
* [patch_compute_service](#patch_compute_service) - Update a service
* [patch_compute_template](#patch_compute_template) - Update a template
* [patch_compute_volume](#patch_compute_volume) - Update a volume
* [remove_compute_deployment](#remove_compute_deployment) - Remove a deployment
* [remove_compute_domain](#remove_compute_domain) - Remove a domain
* [remove_compute_envvar](#remove_compute_envvar) - Remove an envvar
* [remove_compute_instance](#remove_compute_instance) - Remove an instance
* [remove_compute_key](#remove_compute_key) - Remove a key
* [remove_compute_service](#remove_compute_service) - Remove a service
* [remove_compute_snapshot](#remove_compute_snapshot) - Remove a snapshot
* [remove_compute_template](#remove_compute_template) - Remove a template
* [remove_compute_volume](#remove_compute_volume) - Remove a volume
* [update_compute_deployment](#update_compute_deployment) - Update a deployment
* [update_compute_domain](#update_compute_domain) - Update a domain
* [update_compute_envvar](#update_compute_envvar) - Update an envvar
* [update_compute_instance](#update_compute_instance) - Update an instance
* [update_compute_key](#update_compute_key) - Update a key
* [update_compute_service](#update_compute_service) - Update a service
* [update_compute_template](#update_compute_template) - Update a template
* [update_compute_volume](#update_compute_volume) - Update a volume

## create_compute_deployment

Create a deployment

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeDeployment" method="post" path="/compute/{connection_id}/deployment" example="compute_deployment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.create_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-28T17:34:07.237Z"),
            "id": "b1365f38-59f8-496e-a8db-3bdc8a1a6505",
            "metadata": [],
            "started_at": parse_datetime("2025-04-09T12:33:14.274Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-27T17:10:55.755Z"),
            "url": "https://comfortable-petal.name",
        },
        "connection_id": "<id>",
    })

    assert res.compute_deployment is not None

    # Handle response
    print(res.compute_deployment)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateComputeDeploymentRequest](../../models/operations/createcomputedeploymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateComputeDeploymentResponse](../../models/operations/createcomputedeploymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_compute_domain

Create a domain

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeDomain" method="post" path="/compute/{connection_id}/domain" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.create_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "a49a8ba5-0d93-4399-a35f-9f49f01b9a8b",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-02T22:32:52.104Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateComputeDomainRequest](../../models/operations/createcomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateComputeDomainResponse](../../models/operations/createcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_compute_envvar

Create an envvar

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeEnvvar" method="post" path="/compute/{connection_id}/envvar" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.create_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "dd1d05f5-accb-490d-b345-e39da8652d5b",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-02T16:31:51.733Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateComputeEnvvarRequest](../../models/operations/createcomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateComputeEnvvarResponse](../../models/operations/createcomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.compute.create_compute_instance(request={
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
            "id": "1e4a9e22-07ad-4170-ac3f-3a8dd4ee4180",
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
            "started_at": parse_datetime("2025-03-23T05:32:35.472Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-15T09:25:14.575Z"),
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

## create_compute_key

Create a key

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeKey" method="post" path="/compute/{connection_id}/key" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.create_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "20afd750-fcf7-4406-83e5-a2621eb61518",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.588Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateComputeKeyRequest](../../models/operations/createcomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.CreateComputeKeyResponse](../../models/operations/createcomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.compute.create_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "dcce84d9-703d-4371-8300-1b35e622f5b2",
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
            "updated_at": parse_datetime("2025-04-04T02:08:22.363Z"),
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

    res = unified_to.compute.create_compute_snapshot(request={
        "compute_snapshot": {
            "created_at": parse_datetime("2021-09-24T14:40:06.110Z"),
            "id": "4e4b32b9-970a-4994-9b2f-feb9994d16af",
            "metadata": [],
            "name": "snap-alius",
            "size_mb": 169984.0,
            "status": shared.ComputeSnapshotStatus.DELETING,
            "type": shared.ComputeSnapshotType.DISK,
            "updated_at": parse_datetime("2026-03-29T19:28:17.790Z"),
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

## create_compute_template

Create a template

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeTemplate" method="post" path="/compute/{connection_id}/template" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.create_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "b065f6e1-f93e-44ca-a3d9-f638f8ee5b40",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-22T19:54:51.018Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-12T02:55:26.220Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateComputeTemplateRequest](../../models/operations/createcomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateComputeTemplateResponse](../../models/operations/createcomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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

    res = unified_to.compute.create_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "5884cb7e-4cde-4155-a4ed-bcc19cc24365",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-09T12:41:22.933Z"),
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

## get_compute_deployment

Retrieve a deployment

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeDeployment" method="get" path="/compute/{connection_id}/deployment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_deployment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_deployment is not None

    # Handle response
    print(res.compute_deployment)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetComputeDeploymentRequest](../../models/operations/getcomputedeploymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetComputeDeploymentResponse](../../models/operations/getcomputedeploymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_domain

Retrieve a domain

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeDomain" method="get" path="/compute/{connection_id}/domain/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_domain(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeDomainRequest](../../models/operations/getcomputedomainrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeDomainResponse](../../models/operations/getcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_envvar

Retrieve an envvar

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeEnvvar" method="get" path="/compute/{connection_id}/envvar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_envvar(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeEnvvarRequest](../../models/operations/getcomputeenvvarrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeEnvvarResponse](../../models/operations/getcomputeenvvarresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_gputype

Retrieve a gputype

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeGputype" method="get" path="/compute/{connection_id}/gputype/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_gputype(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_gputype is not None

    # Handle response
    print(res.compute_gputype)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetComputeGputypeRequest](../../models/operations/getcomputegputyperequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetComputeGputypeResponse](../../models/operations/getcomputegputyperesponse.md)**

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

    res = unified_to.compute.get_compute_instance(request={
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

## get_compute_key

Retrieve a key

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeKey" method="get" path="/compute/{connection_id}/key/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_key(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetComputeKeyRequest](../../models/operations/getcomputekeyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetComputeKeyResponse](../../models/operations/getcomputekeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_region

Retrieve a region

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeRegion" method="get" path="/compute/{connection_id}/region/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_region(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_region is not None

    # Handle response
    print(res.compute_region)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeRegionRequest](../../models/operations/getcomputeregionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeRegionResponse](../../models/operations/getcomputeregionresponse.md)**

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

    res = unified_to.compute.get_compute_service(request={
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

    res = unified_to.compute.get_compute_snapshot(request={
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

## get_compute_template

Retrieve a template

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeTemplate" method="get" path="/compute/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.get_compute_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetComputeTemplateRequest](../../models/operations/getcomputetemplaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetComputeTemplateResponse](../../models/operations/getcomputetemplateresponse.md)**

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

    res = unified_to.compute.get_compute_volume(request={
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

## list_compute_deployments

List all deployments

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeDeployments" method="get" path="/compute/{connection_id}/deployment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_deployments(request={
        "connection_id": "<id>",
    })

    assert res.compute_deployments is not None

    # Handle response
    print(res.compute_deployments)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListComputeDeploymentsRequest](../../models/operations/listcomputedeploymentsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListComputeDeploymentsResponse](../../models/operations/listcomputedeploymentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_domains

List all domains

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeDomains" method="get" path="/compute/{connection_id}/domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_domains(request={
        "connection_id": "<id>",
    })

    assert res.compute_domains is not None

    # Handle response
    print(res.compute_domains)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeDomainsRequest](../../models/operations/listcomputedomainsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeDomainsResponse](../../models/operations/listcomputedomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_envvars

List all envvars

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeEnvvars" method="get" path="/compute/{connection_id}/envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_envvars(request={
        "connection_id": "<id>",
    })

    assert res.compute_envvars is not None

    # Handle response
    print(res.compute_envvars)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeEnvvarsRequest](../../models/operations/listcomputeenvvarsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeEnvvarsResponse](../../models/operations/listcomputeenvvarsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_gputypes

List all gputypes

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeGputypes" method="get" path="/compute/{connection_id}/gputype" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_gputypes(request={
        "connection_id": "<id>",
    })

    assert res.compute_gputypes is not None

    # Handle response
    print(res.compute_gputypes)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListComputeGputypesRequest](../../models/operations/listcomputegputypesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListComputeGputypesResponse](../../models/operations/listcomputegputypesresponse.md)**

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

    res = unified_to.compute.list_compute_instances(request={
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

## list_compute_keys

List all keys

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeKeys" method="get" path="/compute/{connection_id}/key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_keys(request={
        "connection_id": "<id>",
    })

    assert res.compute_keys is not None

    # Handle response
    print(res.compute_keys)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListComputeKeysRequest](../../models/operations/listcomputekeysrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.ListComputeKeysResponse](../../models/operations/listcomputekeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_regions

List all regions

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeRegions" method="get" path="/compute/{connection_id}/region" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_regions(request={
        "connection_id": "<id>",
    })

    assert res.compute_regions is not None

    # Handle response
    print(res.compute_regions)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeRegionsRequest](../../models/operations/listcomputeregionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeRegionsResponse](../../models/operations/listcomputeregionsresponse.md)**

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

    res = unified_to.compute.list_compute_services(request={
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

    res = unified_to.compute.list_compute_snapshots(request={
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

## list_compute_templates

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeTemplates" method="get" path="/compute/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_templates(request={
        "connection_id": "<id>",
    })

    assert res.compute_templates is not None

    # Handle response
    print(res.compute_templates)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListComputeTemplatesRequest](../../models/operations/listcomputetemplatesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListComputeTemplatesResponse](../../models/operations/listcomputetemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_usages

List all usages

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeUsages" method="get" path="/compute/{connection_id}/usage" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.list_compute_usages(request={
        "connection_id": "<id>",
    })

    assert res.compute_usages is not None

    # Handle response
    print(res.compute_usages)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListComputeUsagesRequest](../../models/operations/listcomputeusagesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListComputeUsagesResponse](../../models/operations/listcomputeusagesresponse.md)**

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

    res = unified_to.compute.list_compute_volumes(request={
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

## patch_compute_deployment

Update a deployment

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeDeployment" method="patch" path="/compute/{connection_id}/deployment/{id}" example="compute_deployment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.patch_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-28T17:34:07.247Z"),
            "id": "c3f9a2f6-d1e7-45fb-a0f5-0e48d6235711",
            "metadata": [],
            "started_at": parse_datetime("2025-04-09T12:33:14.283Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-27T17:10:55.767Z"),
            "url": "https://comfortable-petal.name",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_deployment is not None

    # Handle response
    print(res.compute_deployment)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchComputeDeploymentRequest](../../models/operations/patchcomputedeploymentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchComputeDeploymentResponse](../../models/operations/patchcomputedeploymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_domain

Update a domain

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeDomain" method="patch" path="/compute/{connection_id}/domain/{id}" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.patch_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "c78ad1ca-9a25-4162-a3a8-cd0936135b12",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-02T22:32:52.111Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchComputeDomainRequest](../../models/operations/patchcomputedomainrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchComputeDomainResponse](../../models/operations/patchcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_envvar

Update an envvar

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeEnvvar" method="patch" path="/compute/{connection_id}/envvar/{id}" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.patch_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "ee7b7c7b-19ab-476d-a771-363afa5e67db",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-02T16:31:51.742Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchComputeEnvvarRequest](../../models/operations/patchcomputeenvvarrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchComputeEnvvarResponse](../../models/operations/patchcomputeenvvarresponse.md)**

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

    res = unified_to.compute.patch_compute_instance(request={
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
            "id": "12ca1ad4-a2f3-4f5d-ae0c-8a26a3ccf636",
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
            "started_at": parse_datetime("2025-03-23T05:32:35.489Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-15T09:25:14.593Z"),
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

## patch_compute_key

Update a key

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeKey" method="patch" path="/compute/{connection_id}/key/{id}" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.patch_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "ef7eede9-a69b-4e48-931b-1a2db7a2d8c8",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.593Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchComputeKeyRequest](../../models/operations/patchcomputekeyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.PatchComputeKeyResponse](../../models/operations/patchcomputekeyresponse.md)**

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

    res = unified_to.compute.patch_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "5b3f2283-13d1-42ce-9349-cd37fda16e60",
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
            "updated_at": parse_datetime("2025-04-04T02:08:22.374Z"),
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

## patch_compute_template

Update a template

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeTemplate" method="patch" path="/compute/{connection_id}/template/{id}" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.patch_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "c5d25727-9951-4aaa-8cbd-60b80fe30de8",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-22T19:54:51.039Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-12T02:55:26.233Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchComputeTemplateRequest](../../models/operations/patchcomputetemplaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchComputeTemplateResponse](../../models/operations/patchcomputetemplateresponse.md)**

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

    res = unified_to.compute.patch_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "4a029c9b-c078-482e-bd99-8996eb0a26a9",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-09T12:41:22.937Z"),
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

## remove_compute_deployment

Remove a deployment

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeDeployment" method="delete" path="/compute/{connection_id}/deployment/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.remove_compute_deployment(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveComputeDeploymentRequest](../../models/operations/removecomputedeploymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveComputeDeploymentResponse](../../models/operations/removecomputedeploymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_domain

Remove a domain

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeDomain" method="delete" path="/compute/{connection_id}/domain/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.remove_compute_domain(request={
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
| `request`                                                                                      | [operations.RemoveComputeDomainRequest](../../models/operations/removecomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveComputeDomainResponse](../../models/operations/removecomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_envvar

Remove an envvar

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeEnvvar" method="delete" path="/compute/{connection_id}/envvar/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.remove_compute_envvar(request={
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
| `request`                                                                                      | [operations.RemoveComputeEnvvarRequest](../../models/operations/removecomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveComputeEnvvarResponse](../../models/operations/removecomputeenvvarresponse.md)**

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

    res = unified_to.compute.remove_compute_instance(request={
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

## remove_compute_key

Remove a key

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeKey" method="delete" path="/compute/{connection_id}/key/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.remove_compute_key(request={
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
| `request`                                                                                | [operations.RemoveComputeKeyRequest](../../models/operations/removecomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.RemoveComputeKeyResponse](../../models/operations/removecomputekeyresponse.md)**

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

    res = unified_to.compute.remove_compute_service(request={
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

    res = unified_to.compute.remove_compute_snapshot(request={
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

## remove_compute_template

Remove a template

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeTemplate" method="delete" path="/compute/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.remove_compute_template(request={
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
| `request`                                                                                          | [operations.RemoveComputeTemplateRequest](../../models/operations/removecomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveComputeTemplateResponse](../../models/operations/removecomputetemplateresponse.md)**

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

    res = unified_to.compute.remove_compute_volume(request={
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

## update_compute_deployment

Update a deployment

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeDeployment" method="put" path="/compute/{connection_id}/deployment/{id}" example="compute_deployment" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.update_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-28T17:34:07.247Z"),
            "id": "c3f9a2f6-d1e7-45fb-a0f5-0e48d6235711",
            "metadata": [],
            "started_at": parse_datetime("2025-04-09T12:33:14.283Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-27T17:10:55.767Z"),
            "url": "https://comfortable-petal.name",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_deployment is not None

    # Handle response
    print(res.compute_deployment)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateComputeDeploymentRequest](../../models/operations/updatecomputedeploymentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateComputeDeploymentResponse](../../models/operations/updatecomputedeploymentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_domain

Update a domain

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeDomain" method="put" path="/compute/{connection_id}/domain/{id}" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.update_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "c78ad1ca-9a25-4162-a3a8-cd0936135b12",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-02T22:32:52.111Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateComputeDomainRequest](../../models/operations/updatecomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateComputeDomainResponse](../../models/operations/updatecomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_envvar

Update an envvar

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeEnvvar" method="put" path="/compute/{connection_id}/envvar/{id}" example="compute_envvar" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.update_compute_envvar(request={
        "compute_envvar": {
            "created_at": parse_datetime("2021-08-16T07:52:27.306Z"),
            "environments": [
                shared.PropertyComputeEnvvarEnvironments.PREVIEW,
            ],
            "id": "ee7b7c7b-19ab-476d-a771-363afa5e67db",
            "is_secret": True,
            "metadata": [],
            "name": "AEGER_SUBSTANTIA",
            "updated_at": parse_datetime("2025-07-02T16:31:51.742Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_envvar is not None

    # Handle response
    print(res.compute_envvar)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateComputeEnvvarRequest](../../models/operations/updatecomputeenvvarrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateComputeEnvvarResponse](../../models/operations/updatecomputeenvvarresponse.md)**

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

    res = unified_to.compute.update_compute_instance(request={
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
            "id": "12ca1ad4-a2f3-4f5d-ae0c-8a26a3ccf636",
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
            "started_at": parse_datetime("2025-03-23T05:32:35.489Z"),
            "status": shared.ComputeInstanceStatus.ERROR,
            "status_reason": "Sponte quasi adversus alioqui reiciendis arca carmen canis.",
            "type": shared.ComputeInstanceType.BAREMETAL,
            "updated_at": parse_datetime("2025-06-15T09:25:14.593Z"),
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

## update_compute_key

Update a key

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeKey" method="put" path="/compute/{connection_id}/key/{id}" example="compute_key" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.update_compute_key(request={
        "compute_key": {
            "created_at": parse_datetime("2023-08-19T14:31:46.492Z"),
            "id": "ef7eede9-a69b-4e48-931b-1a2db7a2d8c8",
            "metadata": [],
            "name": "nienow-secret",
            "type": shared.ComputeKeyType.SECRET,
            "updated_at": parse_datetime("2024-10-06T12:55:09.593Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_key is not None

    # Handle response
    print(res.compute_key)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateComputeKeyRequest](../../models/operations/updatecomputekeyrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UpdateComputeKeyResponse](../../models/operations/updatecomputekeyresponse.md)**

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

    res = unified_to.compute.update_compute_service(request={
        "compute_service": {
            "branch": "main",
            "build_command": "npm run build",
            "created_at": parse_datetime("2023-10-04T02:06:29.391Z"),
            "id": "5b3f2283-13d1-42ce-9349-cd37fda16e60",
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
            "updated_at": parse_datetime("2025-04-04T02:08:22.374Z"),
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

## update_compute_template

Update a template

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeTemplate" method="put" path="/compute/{connection_id}/template/{id}" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.compute.update_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "c5d25727-9951-4aaa-8cbd-60b80fe30de8",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-22T19:54:51.039Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-12T02:55:26.233Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateComputeTemplateRequest](../../models/operations/updatecomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateComputeTemplateResponse](../../models/operations/updatecomputetemplateresponse.md)**

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

    res = unified_to.compute.update_compute_volume(request={
        "compute_volume": {
            "created_at": parse_datetime("2022-11-15T15:12:48.055Z"),
            "id": "4a029c9b-c078-482e-bd99-8996eb0a26a9",
            "instance_ids": [],
            "metadata": [],
            "name": "vol-solum",
            "size_mb": 1024000.0,
            "status": shared.ComputeVolumeStatus.OTHER,
            "type": shared.ComputeVolumeType.HIGH_PERFORMANCE,
            "updated_at": parse_datetime("2024-02-09T12:41:22.937Z"),
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