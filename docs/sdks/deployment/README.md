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

Creates a ComputeDeployment. Provide the unified ComputeDeployment fields in the request body; they are mapped to the provider's API. Returns the created ComputeDeployment.

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
            "finished_at": parse_datetime("2025-08-30T08:39:21.131Z"),
            "id": "25ba96fd-fe07-48cd-b826-6741970cfc4f",
            "metadata": [],
            "started_at": parse_datetime("2025-04-10T22:57:28.715Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-03-01T14:20:16.768Z"),
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

Retrieves a single ComputeDeployment by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of ComputeDeployments. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the ComputeDeployment identified by `id`. Provide the unified ComputeDeployment fields to change in the request body.

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
            "finished_at": parse_datetime("2025-08-30T08:39:21.145Z"),
            "id": "d3cda7e1-1d2a-4128-8ecf-16721fcf731a",
            "metadata": [],
            "started_at": parse_datetime("2025-04-10T22:57:28.727Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-03-01T14:20:16.783Z"),
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

Deletes the ComputeDeployment identified by `id`.

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

Updates the ComputeDeployment identified by `id`. Provide the unified ComputeDeployment fields to change in the request body.

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
            "finished_at": parse_datetime("2025-08-30T08:39:21.145Z"),
            "id": "d3cda7e1-1d2a-4128-8ecf-16721fcf731a",
            "metadata": [],
            "started_at": parse_datetime("2025-04-10T22:57:28.727Z"),
            "status": shared.ComputeDeploymentStatus.LIVE,
            "trigger": shared.Trigger.API,
            "updated_at": parse_datetime("2026-03-01T14:20:16.783Z"),
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