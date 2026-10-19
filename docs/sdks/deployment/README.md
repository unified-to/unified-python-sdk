# Deployment

## Overview

### Available Operations

* [create_compute_deployment](#create_compute_deployment) - Create a deployment
* [get_compute_deployment](#get_compute_deployment) - Retrieve a deployment
* [list_compute_deployments](#list_compute_deployments) - List all deployments
* [patch_compute_deployment](#patch_compute_deployment) - Update a deployment
* [remove_compute_deployment](#remove_compute_deployment) - Remove a deployment
* [update_compute_deployment](#update_compute_deployment) - Update a deployment

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

    res = unified_to.deployment.create_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-27T21:37:58.844Z"),
            "id": "41a3561c-5b9f-4ebe-973a-d390947cbcf1",
            "metadata": [],
            "started_at": parse_datetime("2025-04-08T19:00:24.719Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-26T18:09:04.664Z"),
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

    res = unified_to.deployment.get_compute_deployment(request={
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

    res = unified_to.deployment.list_compute_deployments(request={
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

    res = unified_to.deployment.patch_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-27T21:37:58.859Z"),
            "id": "ebcbdbe2-1c53-49a9-ba03-804c6f5f3e3c",
            "metadata": [],
            "started_at": parse_datetime("2025-04-08T19:00:24.732Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-26T18:09:04.681Z"),
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

    res = unified_to.deployment.remove_compute_deployment(request={
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

    res = unified_to.deployment.update_compute_deployment(request={
        "compute_deployment": {
            "branch": "develop",
            "commit_identifier": "fadfe54eefd8fea670bea6d58b4b15d406c4b02b",
            "commit_message": "copy primary pixel",
            "created_at": parse_datetime("2022-06-07T03:52:04.613Z"),
            "environment": shared.Environment.PREVIEW,
            "finished_at": parse_datetime("2025-08-27T21:37:58.859Z"),
            "id": "ebcbdbe2-1c53-49a9-ba03-804c6f5f3e3c",
            "metadata": [],
            "started_at": parse_datetime("2025-04-08T19:00:24.732Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-02-26T18:09:04.681Z"),
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